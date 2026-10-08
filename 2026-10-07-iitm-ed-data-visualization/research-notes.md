# Research and fact-check notes — 7 Oct 2026 ED5518 story

**Research checked 8 Oct 2026.** This is an **evidence shelf for Claude Code**, not a required structure, bibliography for display, or design brief. Select material that earns a place in the narrative; feel free to omit most of it. `transcript.md` governs what people actually said; published primary sources and local research govern whether claims are true. Link the *particular evidence behind a claim*, not a generic homepage.

## Findings worth weaving into the story

### The overlooked implication: the same chart now crosses multiple “readers”

- Historically much graphical-perception advice targets **human** readers. [Cleveland and McGill (1984), “Graphical Perception”](https://doi.org/10.1080/01621459.1984.10478080) experimentally studied judgments of positions, lengths, angles, slopes and areas. For many numeric estimation tasks, positions on common scales were relatively accurate; angles/areas were harder. This does **not** mean a fixed chart ranking for every human, task, culture or question.
- **Computer readers are neither perfect digital calculators nor miniature humans.** [ChartQAPro (Findings of ACL 2025)](https://aclanthology.org/2025.findings-acl.978/) studied 1,948 questions on 1,341 charts across **99 sources** (published ACL version) and 21 evaluated models. The original paper compares Claude Sonnet 3.5 at 90.5% on its older ChartQA benchmark and 55.81% on ChartQAPro; this is a **benchmark-to-benchmark** comparison, not a result for 2026 frontier models or all visual questions.
- **An excellent independent cross-check for the teaching argument** is [ChartMuseum, NeurIPS 2025](https://arxiv.org/abs/2505.13444). In the study's 1,162 expert-annotated questions, **human evaluators scored 93%, the best tested model Gemini 2.5 Pro 63%**; the reported largest gaps arose in primarily *visual* reasoning. These are explicitly scores for the **study's tested 2025 models and human protocol**, not a declaration that humans outperform today's models generally. If using a numeric comparison, this external study is more direct evidence of differing *human/AI reading* abilities than a metaphor.
- The **precise novelty of the local research** at `~/code/research/chartqapro/REPORT.md` is inspecting *public per-question predictions of newer/other models*, not discovering that models can fail at charts or inventing an error-analysis methodology. The **original ChartQAPro paper already contains detailed error analyses/ablations**. The local report's separation of **approximate-from-geometry questions vs. explicit number questions** is the strongest candidate insight; its word-based approximation tag and numeric parseability filter are limitations. E.g., START-RL-7B median relative numeric errors reported there: **2.8%** on non-approx vs **33.3%** on approximation questions, among parseable numeric predictions; *not* all 1,948 questions and *not* a causally isolated effect.
- **Version-count conflict:** [published ACL abstract](https://aclanthology.org/2025.findings-acl.978/) specifies 99 sources; an earlier [arXiv abstract](https://arxiv.org/abs/2504.05506) may show a different count (157). Prefer the published ACL version and don't mix versions.

### Design for two readers without pretending the model has eyes like ours

An actionable but non-obvious synthesis: **a chart is a lossy encoding of the underlying numbers.** When you need an exact calculation or engineering dimension, don't force either a person or model to reverse-engineer pixel geometry when a reliable table/specification can travel alongside it. This is an *editorial inference* consistent with the benchmark findings, **not** proof that adding text guarantees correct AI answers.

- [W3C WAI: Complex images and charts](https://www.w3.org/WAI/tutorials/images/complex/) recommends a short textual identification plus a **long description of the essential information**; where useful, include structural information and an accompanying data table. The guidance targets human accessibility, particularly assistive technology—not ChatGPT specifically. The possible benefit to machine readers is **plausible, not tested by W3C**.
- The page itself could **demonstrate**, rather than merely claim, how one numerical question behaves when a chart is supplied as pixels vs. when underlying values/legend are provided. Without a genuine tested model response, present it as an explorable **thought experiment**, not a benchmark or completed A/B test.
- Useful tension: direct labels may help numeric reading, yet clutter dense charts; tabular access aids precise lookup but loses visual pattern recognition; a shape may be the right representation for **discovery**, yet a numerical oracle is better for **verification**. Don't collapse into “charts are obsolete.”
- Most practical closing advice: specify the *decision* the chart supports; expose units, definitions, time frame and relevant exact values; check **data → transformation → encoding → interpretation** separately; use an independent answer oracle when the consequences merit it. This is a proposed workflow, not a verbatim quote from the lecture.

### The real failure in the CAD case was not failure to iterate

The key local evidence is `~/code/research/2026-10-ed-viz/`, not a headline from the public CAD leaderboard. The **frozen, single-task candidate** was genuinely editable and self-correcting, with a valid FreeCAD solid and exact envelope. Its *selected self-tests were inadequate*. Crucial independent scorer readings from the local report: **27/30 checked spec parameters matched**, but geometry score **0.0423**, combined reward **0.079809**, and volume difference **13.7%**.

The distinction is between:
- **Validity**: FreeCAD can open a valid one-solid editable parametric model.
- **Consistency with a few measured features**: bounding dimensions, holes, selected radii can match.
- **Geometric/design correspondence**: missed lower fork profile causes substantial shape difference.
- **Independent evaluation**: hidden reference + richer geometric tests catches a case the candidate's self-written kit accepted.

Public [CAD Bench V3 release, 21 Sep 2026](https://www.gnucleus.ai/cad-bench/news/cad-bench-v3): the **full benchmark** has 100 tasks, split 30 text creation / 30 create-and-edit / 40 image-to-CAD, and uses FreeCAD 1.1.0 with an updated grader. The **single local candidate** is one of the image-to-CAD tasks, not the leaderboard average; don't suggest Codex's local 0.0798 score is a model-wide score. [Official CAD Bench page](https://www.gnucleus.ai/cad-bench), [FreeCAD homepage](https://www.freecad.org/).

There is a second subtle lesson: a benchmark **does not perfectly equal intended correctness either**; the official verifier is broader and independent, but still necessarily operationalizes only certain aspects of shape and spec. Avoid “the benchmark proves it could never work” or “27/30 means 90% understood.”

### The history/medium claim has more texture than Playfair → Excel → AI

- An actual image with known reuse rights: [Wikimedia Commons: William Playfair’s 1786 North America trade chart](https://commons.wikimedia.org/wiki/File:1786_Playfair_-_Chart_of_import_and_exports_of_England_to_and_from_all_North_America_from_the_year_1770_to_1782.jpg) (Commons marks the image **public domain**, original 1,324 × 957). Unlike a random web image, the source page documents author, date and licensing. A different archival resource is the [1786 book scan with Playfair plates and James Corry contribution](https://archive.org/details/bim_eighteenth-century_the-commercial-and-polit_corry-james_1786). The Internet Archive item is catalogued under Corry because of the appended Irish charts; that does **not** mean Playfair didn't make the original statistical atlas.
- Early hand-colored plates and today's code-driven views have a shared affordance—**unusual visual forms were technically possible**—but not comparable labor costs, audiences or interaction. Excel templates neither destroyed diversity nor prevented all custom charts.
- [Microsoft Research SandDance](https://www.microsoft.com/en-us/research/project/sanddance/) and [open-source SandDance](https://github.com/microsoft/SandDance) document **unit visualizations**: one mark per row, transitions preserve continuity between rearrangements. This is a useful conceptual description for the 2,200 extracted McKinsey claims, not automatic proof the page *runs the SandDance software*. Its underlying research: [Park et al., “Atom: A Grammar for Unit Visualizations” (2018)](https://www.microsoft.com/en-us/research/uploads/prod/2019/01/atom.pdf) and [Drucker & Fernandez, “A Unifying Framework for Animated and Interactive Unit Visualizations” (2015)](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/sanddance.pdf).
- Hence a better lesson than “AI makes novel charts”: **chart grammar, provenance and a sense of how data should move become available to people with domain knowledge**. The crucial question is whether motion reveals structure or merely entertains.

### OlmoEarth is a model family, not evidence that Chennai improved

- [Ai2 OlmoEarth program](https://allenai.org/olmoearth); original [OlmoEarth paper (Nov 2025)](https://arxiv.org/abs/2511.13655); newer [OlmoEarth v1.1 paper (May 2026)](https://arxiv.org/abs/2605.20804); [open pretrained models](https://github.com/allenai/olmoearth_pretrain). The foundation model is trained for multimodal, spatiotemporal Earth observation; the map is a **downstream change-insights application**, with its own data-processing assumptions.
- The site's Chennai layer in the talk involves **water coverage**, yet **October `links.md` points to `metric=vegetation_delta`**. An earlier correctly targeted public demo URL is in `../2026-08-12-iitm-ed-data-visualization/links.md`: https://pythonicvarun.github.io/olmoearth-change-insights/outputs/chennai/?basemap=esri_imagery&metric=water_delta&unit=cells&period=10y&opacity=0.15&historical=timeline&speed=1200&lat=13.01385&lng=80.26315&zoom=16.00&historicalDate=2015-01-21&renderMode=variation . Check the **live displayed map and legend**; don't claim that a different green legend means increasing water when it may mean vegetation.
- A color difference in two satellite observations is **not automatically a hydrological trend**: seasonal differences, rainfall/tides, date selection, classification error, cloud/shadow, changing pixel/resampling/resolution can matter. Present “the visualization suggests where to investigate,” not “the river is restored.” Don't assert 100-m cell resolution without checking the actual output pipeline.

## Live demo and link review

A URL check from the connected Linux machine on **8 Oct 2026** returned **HTTP 200 to HEAD** for these eight pages, with no `X-Frame-Options` or `Content-Security-Policy` value shown in response headers. **This does not prove their JavaScript runs, their content is the same as in class, or that embedding is successful.** Test actual rendered pages and their inner document/asset requests before deciding to iframe:

| Source | Public link | Role / factual check |
|---|---|---|
| Eshwar security gate | https://eshwarpotturi.github.io/soc-analyst-jev/ | Dynamic attack requests; verify exact model details in site |
| Football shots | https://premier-shot-lab-202526.miyakokoko-842.chatgpt.site/ | Verify whether plots show **shots vs goals**, student/institution claims |
| OlmoEarth change insight | https://pythonicvarun.github.io/olmoearth-change-insights/ | Compare water vs vegetation layer; avoid causal environmental claim |
| Extracted McKinsey claims | https://files.s-anand.net/pages/mckinsey-gep-validation/ | Check counts, year spans and which marks represent verified facts vs forecast claims |
| Bookshelf benchmark | https://atharva-729.github.io/bookshelf-benchmark/ | Check dataset size, F1 scoring and **model/cost labels**; these aren't universal rankings |
| CAD experiment | https://sanand0.github.io/research/2026-10-ed-viz/ | Standalone engineering study: best reusable comparison and local assets |
| IMF forecast misses | https://sanand0.github.io/datastories/imf-gdp-forecast-errors/ | Public alternative to the private Optum portfolio example |
| CAD Bench research release | https://www.gnucleus.ai/cad-bench/news/cad-bench-v3 | Primary explanation of official benchmark scope |

No public URL means no public endorsement. The **Optum** project is `private.s-anand.net`; avoid live preview, screenshots, exact product or vendor details or an identifiable portfolio without explicit publication approval. The `chatgpt.com/c/...` HTML comments in `prompts.md` are **internal prompt/comic provenance**, not public article links.

## Other evidence that could enhance one scene (optional, not material quotas)

- [ChartMuseum, 2025/2026 revised](https://arxiv.org/abs/2505.13444) as a complementary benchmark: chart perception versus text reasoning; *especially useful if the story needs a human-model comparator rather than multiple AI scores*.
- [W3C WAI Complex Images](https://www.w3.org/WAI/tutorials/images/complex/) as a bridge between chart-reading reliability, accessibility and machine-readable alternatives—but **do not claim W3C established an LLM accuracy gain**.
- [IMF forecast-errors public visualization](https://sanand0.github.io/datastories/imf-gdp-forecast-errors/) uses one dot per verified IMF forecast, with signed error on x-axis and an animated mean/median marker. It is a **credible alternate example for animated unit marks**, but it was not necessarily demonstrated at length in the live lecture. Label it “related example,” not a claim about what happened on screen.
- [August 2026 ED5518 class](https://talks.s-anand.net/2026-08-12-iitm-ed-data-visualization/) establishes continuity: what changes is not abandoning visualization but adding a second nonhuman reader and more demanding verification.
- A memorable, clearly hypothetical exercise inspired by **64:12**: generate a simple chart, write down the expected numeric interpretation from the original data, let a model answer **from the image alone**, and compare against that independent ground truth. Change mark density, labels or axis encoding. If you actually test a model, disclose model/date/prompt/data; otherwise present it as an experiment readers could do.

## Editorial verification priorities

1. **Video and timestamps first.** A timestamp-seek interaction requires an actual WebM; do not treat Opus as an identical playback source with guaranteed timing unless verified.
2. **Visual truth next.** In ChartQA, render a chart at readable native resolution before asking the reader; in CAD, preserve shared camera and alignment. A fancy wipe on independently cropped images is misleading.
3. **Claim provenance.** Each quantitative claim should identify if it comes from original peer-reviewed paper, demo UI, local derived experiment, or attributed spoken anecdote. Check that results aren't copied across datasets, model versions, metrics or dates.
4. **Public-safe assets.** Copied local research figures should carry source/attribution and be bundled for static deployment. Don't leak hidden private links or client-specific taxonomy.
5. **Creative latitude.** These are **ingredients** and potential narrative devices, not a section count, component list, theme or layout prescription. Claude Code should invent the presentation and discard suggestions that don't improve the experience.

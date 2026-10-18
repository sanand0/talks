# Prompts — DataHack Summit, 9 November 2017: Visualizing Machine Learning

<!-- Comic page: https://chatgpt.com/c/6ad4a6c5-0080-83ec-8f9b-5fa7af3555ce -->
<!-- Source: https://chatgpt.com/c/6ad3362f-a414-83ec-9f1c-9e54520c4766 -->
<!--
cd ~/code/talks
dev.sh -p ~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Create a memorable **video-first, evidence-grounded story page** at `2017-11-09-datahack-visualizing-machine-learning/index.html` for Anand S's SOLO 43:19 performance *Visualizing Machine Learning* at Analytics Vidhya **DataHack Summit, Bengaluru, Thursday 9 November 2017**. The exact selected video was published to YouTube **28 March 2020**; do not mistake upload date for presentation date, or confuse this recording with a 2019 FOSSASIA talk on the same theme.

Use `.agents/skills/talk-story/SKILL.md` and the relevant interactive-storytelling, data-visualization, accessible web-design and browser-testing skills. Inspect actual **working story pages** `../2026-10-07-iitm-ed-data-visualization/index.html`, `../2024-08-10-tedx-mdi-gurgaon/index.html` and `../2015-02-28-tedx-nmims-bangalore/index.html` to reuse reader/player semantics, not their look. Create an original editorial design.

## Read-first sources, in order

1. **`transcript.md` and [the ONE original YouTube video](https://youtu.be/sORnCj52COw)** (video ID `sORnCj52COw`), 43:19, video-timed cumulative transcript. Check exact lines/seek moments before quoting. Automated transcription was made in 10-minute segments; some technical words/numbers may be wrong.
2. **`story-context.md`** — proposed spine, scene arcs, timestamp map, interactive ideas and specific dangers. Choose/edit an even sharper narrative; don't interpret its beats as a strict template.
3. **`research-notes.md`** — the surprising 2017 adoption failure, historical facts, 2011 Census district counts, caveats on model scores, correlations, demographics, and source hierarchy.
4. **`links.md` and `sources/README.md`** — official 2017 event and original 2020 video, Bret Victor’s authentic work, independent trust literature and exact gaps.
5. **`frame-map.md` + `slides/*.webp`** — 12 authentic stills from original 2017 performance, covering decision tree, census districts, interpretability dashboard, Bret Victor car simulation, currency correlation and close. Use the best 5–8. These are real frames, not original slide exports. No full original 2017 slide deck was recovered.
6. **Local `2017-11-09-datahack-visualizing-machine-learning.opus`** — mono 43:19 Opus. Don't link a presumed release URL until publication verified.
7. **`comic-page.avif`** — the user will create this shortly. Feature prominently high in page with accessible alt and lightbox once it exists. **Do not create a replacement, stock comic, or synthetic 2017 screenshot.**

## The story: optimizing accuracy can kill adoption

At around **03:00**, the speaker delivers the shock: **a telecom company canned a model-improvement project four months after its scientists made its predictions better.** A simple decision tree was explainable to marketing; an SVM or other stronger but opaque model was not. An insight about predictive accuracy becomes a puzzle about organizations: **Who has to decide what to do with the prediction?**

Possible title: **“They Improved the Model. The Client Cancelled.”** Or “The Model That Nobody Could Use.” A faithful story can begin with the cancelled project, rewind to the decision tree and escalating accuracy, and ask the reader why stronger results were not enough.

Then show *how the talk answers that*:

- **00:19–05:41** — Telecom churn rule, improvements, cancellation; adjacent commodity neural net story. The protagonist is the decision-maker as well as the data scientist. No invented client names or metrics.
- **05:41–13:16** — India's 2011 Census, 640 districts: a K-means algorithm returns 0,1,2,3. Ask: what does that mean? Move from labels to map. More visible, but still not enough.
- **13:16–20:53** — Feature/cluster profiles and media/advertiser groups turn arbitrary numeric segments into human decision categories. Guard against historical demographic stereotyping.
- **21:31–30:00** — Bret Victor's **[Up and Down the Ladder of Abstraction](https://worrydream.com/LadderOfAbstraction/)** brings a trivial steering model alive. Movement → traces → scores/parameter sweep → inspect original motion. **Credit Bret Victor, not Anand, for the authored demonstration.**
- **30:14–35:45** — Currency time series → scatter plots → correlation heatmap → portfolio action. Historical financial data/claims are illustrative; a matrix is not guaranteed investment guidance.
- **35:45–43:11** — Final thesis: visual summaries and domain interpretation, not the tool brand, make a model usable. Q&A on chart selection. Return to the beginning: the client needed an answer it could act on.

**Keep narrative tension and revelations, not six equal mini-tutorials.** Resist a sprawling survey of algorithms; the original talk focuses on making output interpretable.

## Interactive experiments that matter

**Primary choice:** Give reader an explainable decision tree: show an *illustrative* customer, ask which branch applies, then present a more accurate but opaque risk tag and ask what business action should follow. Make it explicit that any numbers/customers are **invented examples for understanding** unless found in historical source. Never claim they are the 2017 dataset or client outcomes.

**Second choice:** start with a cluster label “3” and let reader reveal geographic distribution then feature profile to show why the *algorithm is the easy part*. Use historic film stills and explanatory overlays, **or** a clearly artificial dataset of a handful of sample districts. Do not build made-up exact 2017 census cluster polygons. If credible data is available, document source/method.

**Alternative:** interact with the Bret Victor original or a small, openly-labelled steering reimplementation showing simulation → trails → summaries; actual original https://worrydream.com/LadderOfAbstraction/ should be prominently credited and linked. Two substantial interactions usually suffice. A currency heatmap can be a static original frame with a pointer to the causal-claim caveat.

## Critical fact-check boundaries

- **Event date:** 9 Nov **2017** from original YouTube description; organizer confirms multi-day 9–11 Nov. YouTube upload **28 Mar 2020**. Do not conflate with 2019 FOSSASIA talk.
- **Opening telecom:** “39% improvement” lacks an explicit base metric. “8% monthly churn means all churn yearly” is mathematically loose; a constant 8% monthly loss in a fixed cohort would be ~63% by month 12, not 100%. Never rewrite exact quotation; caveat the math at the claim or omit it. Don't invent cancelled project identity, spending or audited results.
- **Census/K-means:** 640 districts is historically sourced to 2011 government census; not current India geography or verified original client CSV. K-means labels don't intrinsically identify social groups; variables, scaling, method and ethics matter. Do not convert demographic proxies into modern targeting recommendations.
- **Bret Victor author credit** and original nature; don't present this as Anand's independently written car simulator. No unsupported claim that the speaker used later SHAP/agent capabilities in 2017.
- **Correlation matrix:** old financial data unverified, sample/period may be unstable. No advice to rebalance or hedge any real portfolio based on snapshot; client's “large trade” is anecdotal.
- **No fabricated “original 2017” charts** or source notebooks. Exact original deck and data were not recovered. Source visual claims by film frame, research as labelled, and illustrative modern reconstruction as such.

## Film/player experience, design, QA, handoff

Use **only** https://youtu.be/sORnCj52COw as the ONE persistent player via the YouTube IFrame Player API. Story-first/Video-first toggle preserving current time and actual playing state; in-story timestamps seek/play, URL deep links/history restore, transcript popup with accessible content, keyboard/mobile support, reduced motion, working jump navigation and no horizontal overflow. Study recent working pages and test the real interactions, not mere markup.

Visual direction: a warm editorial investigation in which a diagram becomes a decision. Put a *real* decision tree, census map, small model/parameter visualization and currency heatmap in a rhythm of short paragraphs, well-verified quotations and proof at point of need. Different visual language from Minecraft's game aesthetic and the 2012 D3/2013 PowerPoint stories. Include eventual companion comic as visibly illustrated reflection, not stage photo.

After a real `index.html` is built and tested (not this stage), update the **existing** `config.json` entry now dated 2020-03-28 to the **actual 2017-11-09 event**, preserving upload date as metadata or in story, main YouTube, any separately labelled alternate copy and local transcript/audio (public URL only when actually verified). Regenerate catalog using repo-native build and QA. **Do not create final HTML, generate comic, commit, push or deploy at this stage.**

---

slides/f0431-forecast-accuracy.webp feels cropped - maybe the full image would work better here?
It would be nice if #steps-lab had the 5 buttons with role=tab fit in a single line more often, i.e. at more widths, perhaps by making #steps-lab a little wider? Same for #ladder-lab.
Find and fix similar issues.

<!-- claude --resume cffc1c40-f981-4a2e-980a-8f0f8414969f -->

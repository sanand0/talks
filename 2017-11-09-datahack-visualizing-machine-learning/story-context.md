# Story context — The Model That Was Too Accurate to Use

**Event:** Analytics Vidhya DataHack Summit in Bengaluru, 9 November **2017**, speaker Anand S (CEO Gramener at the time). Original chosen video https://youtu.be/sORnCj52COw (43:19), uploaded 28 March **2020**. This is a **solo stage talk** with brief late Q&A. [Transcript](transcript.md), [research ledger](research-notes.md), [sources and media](links.md).

## One escalating story

A telecom client wanted customers to stop leaving. The data scientists built a decision tree, comprehensible enough for marketing to use: how recently did a customer call? Have they recharged? How much? Then an impulse familiar to every AI project took over: *optimize.* Stronger algorithms were tested and prediction accuracy improved. Four months later, the project was **canned**. The model's outputs had become more sophisticated, while the humans expected to use them could not see **why**, what mattered or what to do.

Possible core line: **“A model can get better at predicting and worse at persuading someone to act.”** Or punchier: **“They Improved the Model. Then the Client Cancelled.”** This tension survives eight years of changing AI technology without suggesting 2017 contained GPT-style agents.

The whole talk is a practical answer: visualizing models is not aesthetic decoration. It is *completing the interface between computation and decisions*. There are three different ways it happens in the talk—geographic clusters for media strategy, motion/parameter sweeps for behavior, and correlation heatmaps for portfolio decisions. Select the most dramatic two and make them **carry the story**; others can function as vivid proof points.

## Narrative structure / real scene anchors

### 1. Cold open: the cancelled success (00:19–05:41)

The phrase **“Four months later, the project was canned”** lands about **03:00**; it needs no invented context. First reveal a simple tree the reader can reason with. The tree from the old video has “days since outbound call,” “recharge count,” and an amount threshold (speaker says the actual threshold is not shown). The marketing action follows a legible path. Then an SVM and other black-box alternatives outperform it, but nobody trusts their recommendations enough to operate. The project is shelved.

**Make reader experience this:** give them one hypothetical customer card with *clearly illustrative* values and ask which branch the simple tree takes, then show an opaque `churn_probability = 0.87` value with no explanation. This number must be labelled a **fictional illustration**, not a claim that the 2017 model returned 0.87. Better still, avoid fabricated probability entirely and show “HIGH RISK” vs observed input/action trace.

Careful: transcript mentions “39% improvement,” but the denominator/baseline is undefined; a claim like “39% better churn prevention” would not be supported. No independent customer documents. The 8% monthly figure isn't 100% cohort loss per year; treat remark as anecdote rather than mathematically sound compounding.

Frames `slides/01-churn-tree.webp`, `02-blackbox-accuracy.webp`, `03-cancelled-project.webp`.

### 2. A cluster label is not a strategy (05:41–18:29)

A media company's “Hindi speakers / everyone else” model of India is too crude for local markets. Anand feeds features from India's **2011 Census 640 districts** to K-means; four group IDs appear, and he poses the crucial question: **“Does this make any sense?”** A number 3 in a CSV says nothing to a sales team.

Map the clusters; a pattern appears. Look at *what makes them different* with an interactive profile panel: urban share, education, density, etc. Now interpretation becomes possible. The speaker iterates on number of clusters by both math and practicability. It culminates in an audience strategy map and advertiser groupings; don't present historic demographic categories as modern segment truths, and don't turn protected-class correlations into stereotypes.

**Meaningful interaction**: toggle “Labels” → “Map” → “Profiles” over either an authentic still from this video or a very small **clearly invented example dataset** showing how interpretation builds. Never label fabricated district values as original 2017 census. An essay figure can use original screenshot + interpretive annotation instead of computational re-analysis.

Frames `slides/04-kmeans-census.webp`, `05-map-segments.webp`, `06-cluster-profile.webp` and `07-media-regions.webp`. Watch original playback and choose best of these; some talk footage may make spreadsheet text too small to show without accessible captions.

### 3. The model is too fast to understand (21:31–29:59)

Bret Victor’s **[Up and Down the Ladder of Abstraction](https://worrydream.com/LadderOfAbstraction/)** arrives as a demonstration of explaining a system through *views*: play the animation of a car trying to steer, stop to inspect a path, compare many paths while varying turning angle, then summarize the parameter region in a surface. The point is not that the car AI is ingenious; it's a trivial rule whose behavior still needs visualization.

The speaker credits Bret Victor. Explicitly give original author billing before presenting the example. Instead of recreating his full interactive, link and possibly embed the authentic original if tested; if making a small explanatory demo, mark it as an independent recreation. The reader should be able to move between **an example trajectory** and **a pattern over many parameters**, making the idea of ladder feel concrete.

Frames `slides/08-bret-car.webp` / `09-ladder-abstraction.webp`.

### 4. From exchange rates to a portfolio decision (30:14–35:45)

One currency's time series is hard to compare. Add multiple series, then scatter each pair, then a correlation matrix, then re-order rows and columns so moving-together assets form coloured blocks. The value is in recognizing groups to consolidate or hedge, not in a heatmap's visual sophistication alone. The speaker tells a client-trade anecdote; use the original speech with appropriate limits, no claim of independently audited financial returns.

A simple **value → series → pair → matrix** explainer with illustrative safe data could make this progression intuitive, but if it competes with cluster-label interaction and ladder, simplify. A few original slides and strong prose may be enough.

Frame `slides/10-correlation-heatmap.webp`. Correlation is not causation, and markets change: don't offer investment advice or promise any particular hedge.

### 5. The final argument is about humans (35:45–43:11)

Anand says **“Build a visual summary that explains the model”**, emphasizing domains, familiar mental models and the ladder of abstraction. He then discusses tool stacks—Excel/R/Python/JS—not as status symbols but as instruments. “Tools are versatile enough and are rarely the constraint. People are the constraint. Techniques are the constraint.” An audience member asks how to select a visualization; the answer is less doctrinal: know your objective and your viewer, choose what communicates.

Return to the telecom project: the highest number on a model scorecard can lose in the real world if it doesn't survive the social handoff. This is **the user-facing conclusion**, not “always use decision trees” or “don't bother with accuracy.”

Frame `slides/11-conclusion.webp` / `12-tools-people.webp`.

## Creative and design choices

- Make the page a journey **from scalar prediction to accountable decision**. Choose a visual metaphor perhaps “sealed black box → transparent decision path → map/profile → ladder → heatmap → human decision”.
- **Two** first-class interactions maximum unless you discover a third indispensable: one decision-tree comprehension test / missing explanation and one map/profile or ladder abstraction that changes interpretation. Be sparing with tutorial widgets.
- Use authentic primary stills (review actual frames and source). Don't substitute stock AI brain imagery, fake bank statements, synthetic business dashboards posing as 2017 screenshots.
- Rich quote pacing and argument before tools; keep human context central. Visually distinct from Minecraft bright blocks and D3 graphic grids.
- **Reader-first, video-first:** sticky persistent YouTube player preserving position across Story/Video focus toggle; seeks/deep-links, good transcript reader, sensible mobile/keyboard motion/accessibility.
- Confirm Q&A speaker labels from recording. The host tagged `Unsure` in automated transcript must not receive a guessed identity.
- Use modern retrospective insights only as optional editorial afterword, dated 2026. LIME paper in 2016 supports trust/explainability, but the presenter never cited it.
- A `comic-page.avif` interpretative visual will be supplied by user. Feature it with alt/lightbox when available; **do not generate it now**.

## Known assets, missing assets and acceptance

Ready: normalized transcript, original mono Opus, 12 original video stills + seek map, research and links, actual conference archive, verified Bret Victor original link. **Not recovered:** actual 2017 client datasets, exact deck/code or portfolio trades. Don't create fake “authentic” source data to hide those gaps.

What remains after user provides comic: one self-contained, tested `index.html` narrative page, then update existing catalogue entry from **2020-03-28** (upload) to **2017-11-09** (delivery) while preserving both dates in metadata/documentation, and publish a verified audio release only if separately requested.

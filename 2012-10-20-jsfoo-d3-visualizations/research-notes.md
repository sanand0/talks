# Research and fact-check ledger — JSFoo 2012, Beautiful Visualizations with D3

Prepared 17 Oct 2026. **The biggest discovery is that the full original 2012 demo source still exists** at https://github.com/sanand0/beautiful-visualisations, with original D3 **v2**, named HTML demos and CSV data. See [links.md](links.md) and [story-context.md](story-context.md).

## Source hierarchy, chronology, historical specificity

- **Event:** Saturday 20 October 2012, NIMHANS Convention Centre, Bangalore, JSFoo 2012, 14:00–15:00: https://jsfoo.in/2012/ . Corrects old catalogue date **7 December 2012**, which is the YouTube posting era. Also independently in Anand's talk log https://gist.github.com/sanand0/4554440 .
- **Original YouTube:** https://youtu.be/JAlZ0uJnqkA (HasGeek TV); ~60:55 including questions. `transcript.md` starts with first clearly named speaker at **01:17**; do not imply the first minute has been transcribed in detail or invent an opening quote.
- **Original repository:** https://github.com/sanand0/beautiful-visualisations, checked out for research under `~/Downloads/talks-audio-2026-10-17/beautiful-visualisations-source/`. `README.md` explicitly calls this “Code for a talk on d3.js”; `index.html` links demos. The site https://sanand0.github.io/beautiful-visualisations/ responded HTTP 200 in this session. Each individual demo's modern runtime behaviour must still be tested.
- **D3 version/provenance:** repo includes `d3.v2.js` and `d3.layout.cloud.js` (historical code). D3’s original 2011 research paper https://idl.uw.edu/papers/d3 explains transparent DOM-based data binding; current D3 documentation uses later APIs and is not drop-in compatible.
- **Scientific support:** William Cleveland / Robert McGill's 1984 graphical-perception research https://doi.org/10.1080/01621459.1984.10478080 supports unequal perceptual precision for comparisons using position, length, angle, area and other encodings. **The speaker does not name this article in the transcript;** use it as *supporting research*, never as a quotation from 2012.

## The surprising spine, not a chart catalogue

The talk starts as a parade of astonishing visualizations: rural employment finance, a linting bubble cloud, conference tweet activity, store journeys, weather anomalies and an epic poem in Sanskrit. An audience member then asks whether the bubbles were **actually a sensible way to show the data**. Anand answers at **33:20** that he chose bubbles because they looked cool. The tool showcase turns into a question about judgment. He ranks position on x/y higher than other channels, then exposes D3's actual mechanism: **data → document objects**. End with a live debugging twist: a line of JS runs but circles do not land where planned because an SVG circle uses `cx`/`cy`, not rectangle `x`/`y`, at ~49:59.

The human story is unusually timely without any 2026 claims being attributed to 2012: **making a graphic is not the same as choosing the right one.** A tool's power is a necessary but insufficient condition for insight.

## Fact and attribution ledger (recheck against recording)

| Time | Observed scene or utterance | Nuance / danger |
|---|---|---|
| 01:17 | Anand introduces visualizations using D3 and demos before mechanics. | First ~minute is stage setup; do not fabricate introduction. |
| 02:22–04:54 | NREGA bubbles encode central funding and labour/material spend; circle area/size also shows spend. | Verify chart legend and CSV. This is *historical NREGA data*, not current policy/evaluation. `nrega.csv` exists. |
| 06:05–10:04 | Packed JSLint rule errors in a codebase, switch among counts and normalization. | A bubble diagram may be useful to *find* errors; visual effectiveness for accurate comparison is a separate question. Source `jslint.html`, `jslint.csv`, old jQuery-related raw text. |
| 11:11–17:35 | Animated `#jsfoo` tweets, Twitter conversation/replies, Paris Web and a trending movie hashtag; live social traces. | Tweets are 2012 data; cannot assume old Twitter endpoints still work or that the audience was representative. Data in `tweet-jsfoo.js` etc. |
| 18:25–23:56 | UK supermarket shopping journey through sections, including humorous beer/wine detour. | The talk attributes a retail example without a research methodology. Do not invent sample size, percentages, source retailer or behavioural causal inference. |
| 23:56–25:35 | Weather map across India with contrasting temperatures; Bilaspur mentioned as unusual. | Need independent source/time for climatological claims. Show as **visual observation in old example**, not confirmed weather anomaly science. `weather.csv` and `weather.svg` exist. |
| 25:35–28:48 | Sanskrit Ramayana word cloud: variants of Rama and characters challenge naive token counts. | Linguistic inflection makes counting hard, but don't assert exact morphology without research. The colorful output is an exploratory text visualization, not rigorous philology. Source `ramayana.py` and CSV. |
| 29:23–31:57 | Wealthfront salary/stock compensation visualization. | **NOT created by Anand**; he explicitly credits Wealthfront. No assumed 2012 values in modern screenshot. |
| 31:57–32:33 | Mike Bostock's showreel before coding tutorial. | Credit Bostock as distinct creator. |
| 32:50–33:20 | Audience questions “how does it make sense” to use bubbles for JSLint. | Pivotal *audience intervention*. Check exact attribution/time in video before direct quoting. |
| 33:20–35:58 | Anand says he chose circles because they looked cool, then says choosing appropriate visualization is much harder; ranking of axes, length, angle, area etc. | The exact taxonomy in speech is partly garbled. Present grounded high-level finding, independently sourced to perception research; avoid claiming rigorous identical rank to Cleveland/McGill without checking. |
| 36:34–39:28 | Browser support, asking people for data, Data Visualize This suggestions, inspiration and tools. | IE9/IE10 compatibility reflects 2012; not modern claim. Book is Nathan Yau's *Visualize This*. Audience interjections often **Unsure**. |
| 39:28–45:48 | The NREGA HTML source, `d3.csv`, selections, SVG and the `selectAll(...).data(...)` join. | Use original historical repo. Explain that `selectAll` + data binding yields enter/update/exit semantics; never imply selecting nonexistent elements makes them appear by itself. |
| 45:48–50:30 | Bind array to circles; first attempt fails to place them; audience guesses, then Anand reveals circles need `cx`/`cy`, not `x`/`y`. | Test the interactive reconstruction if making one, and use proper SVG attribute names. Great comic/interactive beat. |
| 50:30–53:21 | Revisit NREGA circles as data-driven objects; final technical summary. | The principle, not a particular library version, is the durable idea. |
| 53:48–60:55 | Questions on D3 timing, graph packing, complementary backend tools, IE and SVG maps; presenter acknowledges large source SVG. | “100 lines of JS” and “SVG over a megabyte” are speaker approximations; distinguish source code length from map data size. |

## Source data already recovered

Original repository file list includes `nrega.html`, `nrega.csv`, `jslint.html`, `jslint.csv`, `tweets.html`, `tweet-jsfoo.js`, `shopping.html`, `weather.html`, `weather.svg`, `weather.csv`, `wordcloud.html`, `wordcloud-ramayana.csv`, `ramayana.csv`, `ramayana.py`, `d3.v2.js`, `d3.layout.cloud.js` and `index.html`. The actual NREGA code makes a CSV-backed D3 selection and appends circles. This is extraordinarily valuable archival source material; link to specific files beside the corresponding story sections. Public demo URLs are collected in [links.md](links.md).

## Design experiments and factual constraints

- A **before/after perceptual test** comparing equal-data circles with a common-axis chart could let readers experience why the Q&A matters. Use *original `jslint.csv` or `nrega.csv`* and label any transformed data with field definitions; do not invent measurements or equate area with diameter.
- A **live data join** can animate [1,2,3,4,5] into circles, then update a few numbers to show what enters, updates, exits. Distinguish a modern recreation from a 2012 screenshot; display a small genuine historical code sample alongside the reconstruction, with an explanatory note about old vs current APIs.
- For the Sanskrit cloud, a toggle to group inflected word forms would be delightful **only if backed by verified linguistic mapping**; otherwise use the original word-cloud source as the exhibit and phrase stem matching as a limitation, not solved fact.
- The tweets, retail paths, data joins, salaries and climate scenes deserve brief, *curated* appearance. Resist one section per demo; the bubbles question is the mid-story turning point, not the 17th mini-tutorial.
- As the title “Beautiful Visualizations” tempts us to celebrate eye candy, the stronger payoff is **beauty + judgment**. Reuse the speaker's own admission without sneering or retroactive embarrassment.
- Archive limitation: Vimeo/YouTube frames often include split-screen stage/desktop and low-resolution projections; use authentic stills or original repo live demos rather than fabricating better-looking “2012 examples”.
- Third-party chart at Wealthfront, Bostock reel, D3 framework itself and user-authored demos must have **different attributions**. No silent ownership transfer.
- Original video release date and talk date differ. **Always** anchor to 20 Oct 2012, not 7 Dec 2012.
- Any audio GitHub release link is a plan until release URL is verified; local Opus exists now.
- Speaker names like `**Unsure**` stay unresolved until video/audible verification. Public transcripts never infer audience identity from generic questions.
- **No comic yet** — specify the slot and future provenance comment, but never fabricate an asset.

## Before implementation

Review the actual 2012 repo's JavaScript and CSV definitions; test direct demo URLs with JS enabled in browser (the landing page alone was checked). Inspect `frame-map.md` for reliable seek points. Inspect historical recording at 33:00–36:00 and ~49:00–50:30 before fixing the cold open and direct quotations. Keep all retrospective context labeled 2026, preferably brief after the original conclusion.

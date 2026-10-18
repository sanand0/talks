# Sources, links and media — JSFoo Bangalore, 20 October 2012: D3

## Original event and talk

- **Only original recording:** https://youtu.be/JAlZ0uJnqkA — approximately 60:55. HasGeek TV publication was in December 2012, NOT the event date.
- **JSFoo 2012 programme:** https://jsfoo.in/2012/ — NIMHANS Convention Centre, Bangalore, **20 October 2012**, 14:00–15:00, “Beautiful Visualizations with d3.js” by Anand S. Recording runs slightly longer including introduction/questions.
- **Archived session proposal:** https://funnel.hasgeek.com/jsfoo/428-d3-js — this older URL can time out; the JSFoo programme remains the strongest event source.
- **Speaker's dated talk log:** https://gist.github.com/sanand0/4554440 — confirms 20 Oct 2012.
- **Original 2012 full source repository:** https://github.com/sanand0/beautiful-visualisations — **not a modern reimplementation**. Archived D3 v2 examples, CSVs, tweets and support scripts; original checked-out source for local research: `~/Downloads/talks-audio-2026-10-17/beautiful-visualisations-source/`.
- **Original demo landing page (HTTP 200 at preparation):** https://sanand0.github.io/beautiful-visualisations/ — use original graphics if still functional; test *individual* demos in a real browser before embedding.

## Original demo catalogue — primary sources

- NREGA bubbles: https://sanand0.github.io/beautiful-visualisations/nrega.html ; [source](https://github.com/sanand0/beautiful-visualisations/blob/gh-pages/nrega.html), [CSV](https://github.com/sanand0/beautiful-visualisations/blob/gh-pages/nrega.csv).
- JSLint error circle-packing: https://sanand0.github.io/beautiful-visualisations/jslint.html ; [source](https://github.com/sanand0/beautiful-visualisations/blob/gh-pages/jslint.html), [CSV](https://github.com/sanand0/beautiful-visualisations/blob/gh-pages/jslint.csv). Derived from old jQuery lint output, not a present-day benchmark.
- Conference tweets: https://sanand0.github.io/beautiful-visualisations/tweets.html?jsfoo ; archived accompanying files include `tweet-jsfoo.js`, `tweet-parisweb.js`, `tweet-soty.js` and other historical captures; platform APIs and tweets may no longer behave as in 2012.
- Shopping paths: https://sanand0.github.io/beautiful-visualisations/shopping.html — contextual exploratory example; **do not claim a representative customer study without provenance**.
- Indian weather: https://sanand0.github.io/beautiful-visualisations/weather.html , [CSV](https://github.com/sanand0/beautiful-visualisations/blob/gh-pages/weather.csv), [original SVG base map](https://github.com/sanand0/beautiful-visualisations/blob/gh-pages/weather.svg). A visual demo, **not proof of statistically significant geographical anomalies**.
- Sanskrit word cloud: https://sanand0.github.io/beautiful-visualisations/wordcloud.html?ramayana ; [wordcloud Ramayana CSV](https://github.com/sanand0/beautiful-visualisations/blob/gh-pages/wordcloud-ramayana.csv), [script](https://github.com/sanand0/beautiful-visualisations/blob/gh-pages/ramayana.py). The source contains D3-v2-era APIs and linguistic simplifications.
- Word cloud JSFoo: https://sanand0.github.io/beautiful-visualisations/wordcloud.html?jsfoo ; contemporary conference text sample.
- Wealthfront compensation chart: discussed and attributed to an **external site** in the transcript at ~29:23, NOT Anand's graphic; do not present as authored by him or silently fetch a modern version of the historical chart.

## Research and visualization method

- **D3 original research paper (2011):** https://idl.uw.edu/papers/d3 — Bostock, Ogievetsky, Heer: bind data to the actual DOM, making expressive, inspectable interactive graphics.
- **Data join mental model:** https://bost.ocks.org/mike/join/ — Bostock's explanation of enter/update/exit; helpful to explain the second half of Anand's live demo.
- **D3 current documentation:** https://d3js.org/ — compare conceptually only; DO NOT execute 2012-era D3 v2 snippets against latest D3 without porting.
- **Cleveland and McGill (1984), graphical perception:** https://doi.org/10.1080/01621459.1984.10478080 — evidence behind accuracy differences among position, length, angle, area etc. Do not say the talk explicitly cites this paper.
- **Mike Bostock historical examples:** https://bost.ocks.org/mike/ — reference the broader community without attributing the samples to Anand.

## Authentic local media

- `slides/` — eleven still frames from original HasGeek recording, indexed in `frame-map.md`. Some show the speaker or projected demo; prefer original repo examples when video projection is fuzzy.
- `2012-10-20-jsfoo-d3-visualizations.opus` — verified mono Opus audio. Its public release URL does NOT exist until published.
- `transcript.md` — historical transcription, with named speaker labels / timestamps, but some audience names marked Unsure.
- `comic-page.avif` — **PENDING**, not yet generated.
- For a production story, test demo URLs with actual browser JS enabled; HTTP 200 on the root alone does not prove every 2012 interactive still works.

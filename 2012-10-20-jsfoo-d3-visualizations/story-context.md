# Story context — The Bubble Chart That Looked Cool: D3 at JSFoo, 20 Oct 2012

**Event:** 20 October 2012, 14:00–15:00, JSFoo 2012 (“JavaScript Everywhere”), NIMHANS Convention Centre, Bangalore. Speaker: Anand S, Gramener. Recording: https://youtu.be/JAlZ0uJnqkA (60:55). Original code + data: https://github.com/sanand0/beautiful-visualisations . The 7 December 2012 date in the old video catalogue reflects the posting period, not the live event.

## The strongest story

A speaker shows a room full of JavaScript developers one beautiful graphic after another. D3 can turn public finance into circles, lint errors into packed bubbles, tweets into a moving timeline, shoppers into paths and a Sanskrit poem into a cloud of words. The room is impressed. Then a participant asks the question that changes the meaning of the presentation: **why are these errors bubbles at all?** Is that really the right shape for comparing error counts? Anand admits that he chose circles because they looked cool. He pivots from demonstrations to **visual judgment**. Later, after explaining that data itself becomes HTML/SVG elements, his live code fails because circles need `cx` and `cy`. The tool empowers creators, but still demands that they know *what object is on the page* and *why it belongs there*.

Possible thesis: **“Once drawing became easy, deciding what to draw became harder.”** Another, more narratively vivid: **“He brought beautiful charts. Someone asked if they were any good.”** It foreshadows the current AI visualization era, but is an honest lesson from **2012**, not a claim that Anand predicted GPT agents. A fresh 2026 closing paragraph may connect the enduring tradeoff, clearly separated from what was said on stage.

The pivotal moment at **32:50–35:58** is arguably the cold open. Let a reader see a spectacular bubble chart and choose which rendering makes comparisons easier. Then reveal that the speaker already confronted the question years ago. Rewind to the visual tour and return to the challenge. A more technical alternative is the live failure at 49:00: circles stubbornly cluster in the corner; why? Then reveal SVG `cx` versus `x`, rewind to the earlier examples and the data binding mechanism. Choose one opener, not two competing tricks.

## Narrative acts with original scene anchors

### 1. The shapes that seem to know the world (01:17–10:04)

Anand starts with a bubble chart from India's National Rural Employment Guarantee programme: labour share on one axis, raw materials another, central funding as horizontal dimension, circles representing spend. There is more information than a table would comfortably display. Then JavaScript lint errors appear as packed circles; the density looks playful and the speaker can click into them. The sources are actual public 2012-era HTML, CSS, JS and CSV files at `beautiful-visualisations/nrega.html` and `jslint.html`.

**Narrative question:** With all that graphic capability, are circles making these comparisons easier? Don't answer yet. Document what fields really mean from `nrega.csv` and `jslint.csv`; don't transpose an axis just because the transcript description is approximate. **Primary frames:** `slides/01-nrega.webp`, `02-jslint.webp`.

### 2. The room becomes a dataset (11:11–17:35)

Dots are JSFoo tweets. Every dot represents a particular tweet with date, time, connections/replies, and the audience starts noticing themselves. This is unusually personal: the conference is literally mapping its own conversation. There is the late-night programmer who tweets after arriving home at 1 AM, the early riser, the other conference (`#parisweb`), and a Bollywood trend. The scene breathes. Every speaker and hashtag is **2012**, not an active Twitter search.

A good miniature interaction: readers reveal a dot's old timestamp and follow its response trail using archival `tweet-jsfoo.js`, **only if authentic mapping can be verified**. A current API call is unnecessary and would break the archival mood. Frame `slides/03-jsfoo-tweets.webp`; original demo `tweets.html?jsfoo`.

### 3. The world becomes patterns; then a poem (18:25–31:57)

The next examples accelerate:
- An illustrated *supermarket journey* — fresh produce to fish, merchandise to other aisles, and the audience's amused question about beer, wine and spirits. This is an exploratory pathway visualization, not established retail causation.
- A weather map — India visually contains contrast, with Bilaspur singled out. It is an illustration using a historical weather sample, not robust proof of a geographical climate mechanism.
- A *Ramayana* word cloud rendered in Sanskrit. Inflections make “how often does Rama appear?” a tricky question; the limitation is as interesting as the visual. Use historical wordcloud CSV/script; don't hallucinate Sanskrit morphology.
- A Wealthfront compensation chart — the source is explicitly **third party**, not Anand's own visualization.
- Then Mike Bostock's D3 showreel — credited to Bostock.

These examples establish delight and breadth, but **do not write one chapter per demo**. Find 2–3 ways to show that data is transformed into a shape, and save the surprising admission for the pivot. Frames `04-shop-paths.webp` through `07-wealthfront.webp`. Original site is https://sanand0.github.io/beautiful-visualisations/ .

### 4. The audience interrupts with the harder problem (32:50–39:28)

At 32:50 the participant asks whether bubbles actually make sense for this data, particularly lint errors. Anand's ~33:20 answer is refreshingly candid: he used them because they looked cool. He differentiates demonstrating the technology from designing the best explanatory chart. At 34:29 he says choosing a chart may be orders of magnitude harder; then he discusses graphical encoding—position, length, angle, area and other properties—in priority order.

This is the **moral pivot**, not an embarrassing gotcha. The original research behind perceptual comparisons predates the 2012 talk: Cleveland & McGill, 1984, https://doi.org/10.1080/01621459.1984.10478080 . Cite this as independent supporting explanation, **not a study the speaker explicitly mentioned**. Some hard-to-hear channel ranking is not precise in the automated transcript; only quote what has been verified.

The next questions about IE support and finding data serve as a quiet coda on the gap between creativity and workability. One practical piece of advice: ask people for data. Another: look at many beautiful charts, let inspiration settle, then try to build one. Do not turn the scene into a pedantic chart-chooser algorithm.

**Reader experiment candidate #1:** Present the same authenticated subset from `jslint.csv` first as packed circles, then as sorted bars or aligned dots. Ask which lets the reader identify the most common error **and by how much**. This allows the audience to feel the difference between detecting a dominant region and comparing exact quantities. Show source, units, and any subset/transformation; never invent “original 2012” results.

**Frame:** `08-bubble-critique.webp` shows the audience member, not necessarily the chart. Use both original `jslint.html` and talk footage to cut between what prompted the challenge and the person asking it.

### 5. What D3 is actually doing (39:28–53:21)

Now the talk changes gears from “look” to “build.” Start with the original NREGA HTML: familiar DOM, SVG, D3 v2 script, CSV loader. `selectAll` and `.data` bind rows of data to DOM elements; `enter()` creates what does not yet exist. The live code grows from a rectangle to five circles. First, they don't behave: the x/y attributes apply to rectangles but circles want `cx`/`cy`. Anand lets the audience discover the error; solving the bug is a wonderfully specific, human moment. A reader can predict the bug with a tiny code choice, see all the circles in the corner, and fix it (using a **modern safe reimplementation**, correctly labelled).

**Reader experiment candidate #2:** A miniature bind/update/enter/exit playground. Show [1, 2, 3, 4, 5] as circles. Change the array; watch nodes appear, transition, disappear; inspect one element as a native SVG/DOM item. Prefer controlled input choices rather than a heavyweight editable environment. Use original repo code in an adjacent panel with an explicit “D3 v2 (2012)” label and a conceptually equivalent current implementation.

**Frames:** `09-d3-selections.webp`, `10-debug-d3.webp`, `11-data-bound.webp`. **Sources:** `nrega.html`, `d3.v2.js`, https://bost.ocks.org/mike/join/ and https://idl.uw.edu/papers/d3 .

### 6. The useful aftertaste (53:21–60:55)

Q&A expands into what D3 *doesn't* do: extract from arbitrary enterprise databases, fix bad information, decide the chart, or turn 100 lines of JavaScript into a complete map when an SVG asset contains most of the geographic detail. It is a flexible rendering and interaction language; analysis/data preparation and choice of encoding remain work.

Close by returning to the opening challenge: **Power is no substitute for perception.** An optional connection to the companion **2013 PowerPoint talk** can show the same underlying principle across two surprising canvases: code gives precise control of elements whether they happen to be DOM nodes or PowerPoint shapes. But in both cases the operator still decides what question the diagram answers. A subtle link, not an unrelated excursus.

## Reader experience to emulate — but not clone

- Make the reader **judge before telling**. The most useful interaction isn't an arbitrary scroll animation; it's a perception comparison grounded in actual historical example data.
- Use original demos directly only if still functional; source-based snapshots are safer for dead 2012-era APIs. The original README explicitly says the site needs a web server and browsers other than old IE.
- Give D3 a visual personality distinct from the companion PowerPoint piece: lightweight native SVG strokes/shapes, data as material, perhaps a “behind the picture” inspection layer. Avoid decorative giant-number cards and identical layouts.
- A few carefully chosen demos are better than a catalogue of seven. The tension between captivating and clarifying must remain legible.
- All direct speech quotations and timestamps must be verified against the original video before publication. Unknown audience voices remain “Audience” or “Unsure”; do not infer names.
- Build the standard video-first reader experience: video/story focus reversible, a single YouTube IFrame player with timestamp jump/deep links, no loss of playback state, on-page transcript, meaningful keyboard controls/ARIA, accessibility/reduced-motion and no mobile overflow.
- For historical 2012 code, **do not silently port** D3 v2 functions without labeling; the modern reader implementation can use SVG/native JS or modern D3 after clear separation.
- Any reproduced weather/cartogram/retail chart needs a source date, explanatory labels, the original vs reconstructed distinction, and no unsupported generalization.
- The user will add **`comic-page.avif` later**. Reserve an accessible prominent position and insert once it exists; do not auto-generate/replace it.

## Quote shortlist (transcript leads; verify exact words)

- 11:11: “Every dot here is a tweet that has the hashtag #jsfoo.”
- 25:35: “what if the word cloud were in Sanskrit?” — breaks expectations.
- 32:50–33:20: audience's “how does it make sense?” followed by speaker's “I wanted to show circles and it looked cool.” **This is the plot twist.**
- 34:29: choosing *which* chart to use is a much harder problem.
- 38:33: spend time looking at charts; let them sink in; build later.
- 45:28–46:28: a selection may contain future elements once data is bound.
- 49:59: SVG circles use `cx`/`cy`, not `x`/`y`.
- 50:30: “we've mapped a dataset onto objects” — conceptual reveal.
- 60:21: “while it's 100 lines of JavaScript, the SVG file behind it is more than a megabyte” — complexity lives somewhere.

## QA risks and needed verification

- Source code original is D3 **v2**. Modern D3 defaults and API are not guaranteed to match; use historical JS files and accurate explanations.
- Check demo security/embeddability; do not iframe a failed script or overwrite user access with a broken frame.
- Historical tweets and weather/retail datasets are not continuously updated; their presence in repo does not independently prove underlying public claims.
- The event is **2012-10-20**, not upload/publishing date. Venue NIMHANS, not the 2013 JSFoo location.
- For visual assets use authentic [frames](frame-map.md) and original repo graphics; synthetic artwork is only the later openly-labelled **comic-page**.
- No unverified D3-vs-other-tool speed/accuracy claims. No sourced-unchecked salary figures or weather assertions.
- Preserve references to the question from the audience; it is the turning point and evidence that teaching was a dialogue, not a solo slide show.
- Publishing, public audio release URL and config entry should wait until real story page exists; do not leave a catalog link to missing HTML.

## Ready-for-build inventory

Here now: original 2012 Opus, cleaned transcript, 11 video-derived original stills with frame map, a checked-out historical source repo, event programme, citation links, research ledger and story context. **Pending user-generated comic and final HTML story.**

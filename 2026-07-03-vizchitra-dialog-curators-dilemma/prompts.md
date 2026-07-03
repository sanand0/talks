# VizChitra Dialog - The Curator's Dilemma

# A3 printouts

<!--
cd /home/sanand/code/talks/2026-07-03-vizchitra-dialog-curators-dilemma
dev.sh -- codex --yolo --model gpt-5.5 --config model_reasoning_effort=medium
-->

I want to create HTMLs of a set of 6 visualizations that I can print on an A3 sheet to hang as posters for my workshop.
e.g. if I print to PDF, it will perfectly print on an A3 PDF - either portrait or landscape.

The visualizations are below and I've added notes.
They are all open on my browser and accessible via CDP at localhost:9222
When printing, no margins are required - unless you think that'll be required for printing.
If you need to resize the viewport, feel free.

1. Statnostics: https://sanand0.github.io/journalists/statnostics/2026-04-27-citizen-survey/05-educated-waiting.svg. I just want this SVG fitted, portrait, into an A3 format, portrait.
2. Popular Actors: https://imageexplore.straivedemo.com/ - I have this open. I want the svg#similarity along with images and axes printed. I also want a title "Popular Actors" and a clear description explaining that the X axis represents how "Chinese" each actor's photo looks and the Y axis represents how "African" each actor's photo looks. Nothing more.
3. Temporal Rosette: https://sanand0.github.io/datastories/novel-dataviz/. I want the entire slide 3, i.e. `#s3` (temporal rosette)
4. Popularity Paradox. https://sanand0.github.io/datastories/imdb-democracy-penalty/. I want the `.chart-container` that has the .chart-title "The Popularity Paradox"
5. LLM Pricing. https://sanand0.github.io/llmpricing/. I want the SVG in `#llm-cost`
6. GDPVal. https://sanand0.github.io/datastories/gdpval/. I want the SVGs in `.legend` and `#treemap`

Create them as .html files in this directory.

--- <!-- steering -->

- 01-statnostics.html should be much bigger on the page.
- 02-popular-actors.html - embed the images base64
  Use this feedback as input for similar tweaks

---

- 01-statnostics.html is fine
- 02-popular-actors.html is fine
- 03-temporal-rosette.html - convert this to light mode - making sure the colors will print well, with contrast, on paper. Also, make the wheels a bit larger.
- 04-popularity-paradox.html - the title and subtitle need better formatting.
- 05-llm-pricing.html - add a title "LLM Model Pricing"
- 06-gdpval.html - include the title, subtitle, etc. and the footer. Effectively, I want the entire page, fit to an A3.

---

I deleted assets/ - can you recreate it?

--- <!-- steering -->

Also, please center 01-statnostics.html vertically AND horizontally

<!-- codex resume 019f264d-9448-75a0-906c-5bc9af7077a2 --yolo -->

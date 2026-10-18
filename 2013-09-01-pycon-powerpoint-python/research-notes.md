# Research and fact-check ledger — PyCon India, 1 September 2013

Prepared 17 Oct 2026. This is a **2013 technical and cultural time capsule**, not a claim that PowerPoint beats modern web tools in 2026. Distinguish **what the speaker demonstrated**, **what the original 2013 code implements**, and **what independently documented sources establish**. Source links: [links.md](links.md); scene map: [story-context.md](story-context.md).

## Primary-source hierarchy and surprising provenance discovery

1. **Original video** https://youtu.be/aKCXj1DyEhM — the chosen, original PyCon recording. Its published upload date of 6 September 2013 was previously used in the talks catalogue, but the original live event was **Sunday 1 September 2013** (PyCon programme and official talk proposal: https://in.pycon.org/2013/ and https://in.pycon.org/funnel/2013/73-data-visualisation-in-powerpoint-with-python/). The event venue is NIMHANS Convention Centre, Bangalore. Correct catalogue date and directory to match event, not YouTube upload.
2. **Talk transcript** [transcript.md](transcript.md) — automatically generated in 2026, cumulative [mm:ss], not a verified verbatim archival transcript. Check source audio and video for important quotations and ambiguities.
3. **Exact original public notebook** https://github.com/sanand0/ipython-notebooks/blob/master/Office.ipynb — the author linked this as *the code used at the talk* in a comment on the PyCon proposal. Local copy `~/code/ipython-notebooks/Office.ipynb` is **nbformat 3**, under `worksheets[0].cells`. Inspect, rather than parsing `cells` top-level. Headings: “Automating Microsoft Office with Python”, “Picturing the IMDb Top 250”, “Real-life examples”, “Live tweeting”. This is stronger than generic reconstructions.
4. **Speaker's 2009 tutorial** https://www.s-anand.net/blog/automating-powerpoint-with-python/ — shows win32com.client, Office/VBA bridge, and a PowerPoint treemap from bank data. It predates the 2013 talk; do NOT confuse its old bank-asset example with the talk's newspaper/cartogram or movie examples.
5. **PyVideo metadata:** https://pyvideo.org/pycon-india-2013/data-visualisation-in-powerpoint-with-python.html — same event date, promise of rich animations, unusual medium, corporate utility.
6. **Authentic video stills:** [frame-map.md](frame-map.md). All extracted from the ORIGINAL YouTube video, not slide deck exports. Legibility varies and speaker overlay/frame layout must be retained or cropped transparently.

## Evidence-led scene / quote ledger

| Time in video | What happens | Best evidence | Claim discipline |
|---|---|---|---|
| 00:00 | A Python conference opens with the puzzle “what ... is PowerPoint doing in a Python conference?” and a claim it made Anand money. | video + transcript | The revenue is a speaker anecdote, not independently audited income; don't quantify it. |
| ~01:00–03:52 | Python opens Windows PowerPoint through COM, creates a presentation and editable shapes. | 2013 notebook + ``slides/01-com-rectangle.webp` | The demo needs Windows Office and the contemporaneous pywin32 setup; the 2013 proposal's ActivePython requirement is *not* absolute (speaker clarifies in comments). |
| 03:52–05:40 | In a world where customers ultimately need presentation slides, code can treat PowerPoint as a drawing canvas, not merely click its UI. | video + proposal | Client namedrops (Novartis/P&G/etc.) establish talk anecdote; don't imply all were clients paying for this precise demo. |
| ~06–09 | Scrape IMDb Top 250 and lay out 250 rectangular poster slots with loops. | `Office.ipynb` + video | 2013 IMDb rankings and posters must not be replaced with today's live list. The demo's actual external scraping endpoints may have changed. |
| ~09–12 | Posters arrive; PowerPoint sometimes draws slowly, while dragging the window appears to speed it up. | video + transcript | Comic/human debugging moment; a quirky observed performance workaround, NOT a reproducible benchmark or current recommended method. |
| 12:31–14:51 | The audience plays “name that movie” from thumbnails. Hover screen tips and hyperlinks make the grid exploratory. | video + original notebook | When illustrating posters, use historical stills rather than recreating a supposedly exact 2013 selection. |
| 14:51–21:03 | The same poster grid reorders by IMDb rank versus alphabetically, with objects visibly moving in PowerPoint. | original notebook's `animate`/`InteractiveSequences` and the recording | D3/Processing comparisons are subjective in the speaker's 2013 context. This is the most visually interesting *mechanism* in the talk. |
| 21:03–~26:50 | Turn from novelty to real work: Vijay Karnataka election graphics on MLA attendance, votes and a substitute constituency cartogram when shape data was missing. | video frames `06-karnataka-mla.webp`/`07-cartogram.webp` | The newspaper example is real *within the talk*, but the chart statistics are not independently verified here. Don't say the data/graphics establish causes of voting. Cartogram is a visual substitute, not a literal geographical map. |
| ~27–30:58 | Corporate dashboards, revenue/app-download drilldowns, other paid/commissioned examples. | video + notebook “Real-life examples” | Treat names and values as speaker/show-and-tell anecdotes; don't publish client-identifiable private numbers from old screenshots. |
| ~30:58–34:39 | A live PowerPoint slide drawing Twitter posts; a “beer” search is replaced with a conference hashtag and produces glitches and laughter. | video; Office notebook TwitterAPI section | Dead 2013 Twitter endpoints cannot be expected to run today. Treat this as archival, not live data or reliable 2026 social statistics. |
| ~35:00–42:45 | Questions: Keynote/Mac compatibility, PowerShell, COM automation for Outlook, distribution and editable files, effort and source code. | transcript + video | Mac/IE/version assertions are **2013 time-bound**. The “one person, one week” production estimate is a conversational approximation, not a general cost survey. |

## Strongest story-worthy mechanisms

**The false category:** Everyone thinks PowerPoint is a manual slide-making app. Strip away the UI and it is an object/animation engine controllable from Python. The interface, not the medium, is the constraint. The code creates PowerPoint objects directly; this is not screen scraping or merely pasting static PNG plots.

**The chase:** A movie grid shows 250 posters. It becomes an index; then it becomes interactive; then the visible reordering bridges to paid news and business work. Each escalates the value and illustrates a different *reason for coding* (volume, metadata, interaction, reusability).

**The counterintuitive monetization:** A creator builds a technically unlikely solution precisely because **clients already live in PowerPoint**. The destination/workflow matters more than tool purity. The funny anecdote about dragging a window while code inserts 250 images adds friction, credibility and human texture.

**The unresolved tradeoff:** PowerPoint makes output portable to business users who already have it, but this particular Windows COM automation is tightly coupled to Office. Contrast *editable familiar output* with *non-portable generation*, rather than claiming universal ease.

## Technical checks before publication

- `win32com.client.Dispatch("PowerPoint.Application")` creates or accesses a COM automation object. COM programming is not an Excel macro or HTML renderer; Python commands manipulate the PowerPoint object model directly. Verify against 2013 notebook and https://learn.microsoft.com/en-us/office/vba/api/overview/powerpoint .
- The original notebook is runnable only after adapting dated Python/Windows Office dependencies; **do not execute against user's Office documents**. A modern HTML interaction may *demonstrate the principle*, but must not masquerade as the actual original PowerPoint file.
- The animation logic uses `Base.TimeLine.InteractiveSequences.Add()`, clickable triggers and movement paths; use real snippets from notebook, not invented pseudo-code.
- The “V(ector)ML path syntax” description is speaker's interpretation; historical documentation https://www.w3.org/TR/NOTE-VML . Do not assert exact identity with SVG path grammar.
- Transcript mentions a Twitter handle that may be an ASR spelling error. Independently verify the actual handle before quoting; source project usernames here are `sanand0`.
- The audience gives Kannada readings and other indistinct words; preserve `[Inaudible]` and avoid inferring a named audience member or a political interpretation.
- No evidence in this research establishes that every named customer bought the specific chart on screen, or the actual sums earned.
- Media copyright: Use a **few short historical excerpts** and original credited stills, not present-day stock imagery or invented visuals falsely labelled 2013. IMDb poster art and newspaper spreads have separate rights; avoid distributing full collections.
- **Original event vs upload date:** update the talks config date to 2013-09-01; keep record of former 2013-09-06 upload date in these notes.
- Audio release path: a local Opus copy exists; GitHub release URL only after explicit publication/verification.

## Further checks a story-building agent should do

1. Read notebook code cells containing `animate`, `Shapes.AddPicture` and actual movie/CSS loops; cite the source notebook in narrative tooltips.
2. Watch [original talk](https://youtu.be/aKCXj1DyEhM) at 16–21 minutes, 22–25 minutes and 31–34 minutes to pick the still with clearest animation, cartogram and live-demo failure. `frame-map.md` is an *initial selection*, not a frame-by-frame truth certificate.
3. Verify whether the specific 2013 Vijay Karnataka spreads are preserved elsewhere before attempting to reconstruct them; otherwise use extracted frames and state source.
4. For an interactive page, build **one** genuinely useful reordering of a small, explicitly *illustrative* poster-like dataset (or the original historical data if genuinely recovered) and make it clear it is an explanatory reconstruction.
5. Keep the historical talk and a modest 2026 perspective clearly separated: “back then” versus “the durable principle”.

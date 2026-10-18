# Sources, links and media — PyCon India 2013: PowerPoint with Python

## Original talk and primary contemporaneous sources

- **Only original video:** https://youtu.be/aKCXj1DyEhM — 42:52; use YouTube IFrame Player API and timestamp seek. Do NOT substitute a local WebM.
- **Official conference schedule:** https://in.pycon.org/2013/ — Sunday **1 September 2013**, 14:00–14:45, NIMHANS Convention Centre, Bangalore. The catalogue's former 6 September date is the uploaded video date, NOT the event date.
- **Original speaker proposal, including audience comments and link to code:** https://in.pycon.org/funnel/2013/73-data-visualisation-in-powerpoint-with-python/ — title, thesis, intended examples, early limitations; includes Anand's link to **the exact notebook used in the talk**.
- **PyVideo mirror/metadata:** https://pyvideo.org/pycon-india-2013/data-visualisation-in-powerpoint-with-python.html — confirms 1 Sep 2013 and contemporaneous framing.
- **Anand's original speaker engagement log:** https://gist.github.com/sanand0/4554440 — independent cross-check against upload date.
- **Talk notebook (exact original source):** https://github.com/sanand0/ipython-notebooks/blob/master/Office.ipynb — local copy: `~/code/ipython-notebooks/Office.ipynb`; nbformat 3, worksheet-based structure. Speaker linked this via nbviewer on the original PyCon proposal. Old preview URL redirects; use GitHub/current nbviewer.
- **Live notebook preview (test availability):** https://nbviewer.org/github/sanand0/ipython-notebooks/blob/master/Office.ipynb

## Earlier techniques, background and demos

- **Anand's 2009 post, “Automating PowerPoint with Python”:** https://www.s-anand.net/blog/automating-powerpoint-with-python/ — early COM scripting, constants, editable treemap created from bank asset data. Earlier than this talk; related context, NOT the complete 2013 demo.
- **Official Microsoft PowerPoint VBA automation reference:** https://learn.microsoft.com/en-us/office/vba/api/overview/powerpoint — underlying object model used through COM.
- **pywin32 package:** https://github.com/mhammond/pywin32 — Windows COM bridge; the 2013 workflow requires Windows/installed Office. The PyCon comment clarifies ActivePython is **convenience**, not a necessity.
- **IMDb Top 250 today:** https://www.imdb.com/chart/top/ — **dynamic/current** data; do not misrepresent as the 2013 selection, titles, posters or ordering. Historical 2013 animation requires the original notebook or recorded slide.
- **Karnataka election coverage example:** a contemporary Vijay Karnataka newspaper commission and spreads are shown in the recording ~21–26 minutes. Original printed spread is visible in `slides/06-karnataka-mla.webp` and `slides/07-cartogram.webp`. Source newspaper images are historical and must be credited; use as examples of the *talk's presentation*, not fresh election statistics.
- **D3 comparison:** https://d3js.org/ — the talk explicitly compares animation ease with D3; the onstage assertion is subjective and version-specific, not a benchmark.
- **VML historical background:** https://www.w3.org/TR/NOTE-VML — Vector Markup Language underlies one motion-path syntax in Anand's notebook; do not confuse with SVG.

## Actual on-screen assets

- `slides/` — ten screenshots captured **from this exact YouTube recording**, not fake redrawings; `frame-map.md` gives timestamps. Priority: poster grid, the reordering demo, Karnataka cartogram, Python animation code, live tweets.
- `2013-09-01-pycon-powerpoint-python.opus` — local verified 42:52 mono Opus audio; no public GitHub release URL yet. DO NOT pretend the conventional release URL exists before publishing and checking it.
- `transcript.md` — cleaned 2026 automated transcript, time-aligned to the YouTube recording; quote only after checking the video.
- `comic-page.avif` — **NOT CREATED**; companion visual summary will be supplied later.

## What to link vs embed

- Embed ONLY the selected original YouTube video. Link source notebook as a code/reader reference, and draw original 2013 media from `slides/`. Do not iframe GitHub/nbviewer unless embeddability is verified; they may refuse it.
- Copy selected code *snippets* from the historical notebook with attribution rather than trying to execute its Windows-only COM code on a modern Linux host.
- The terminal 2013 show and its still frames are evidence; recreated HTML animations are an **interpretation**, not the original PowerPoint file.

# Prompts — PyCon India, 1 September 2013: PowerPoint with Python

<!-- Comic page: https://chatgpt.com/c/6ad4a69e-8948-83ec-9ef8-a165680c7c5e -->
<!-- Source: https://chatgpt.com/c/6ad3362f-a414-83ec-9f1c-9e54520c4766 -->
<!--
cd ~/code/talks
dev.sh -p ~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Create a **remarkable, evidence-grounded, video-first story page** at `2013-09-01-pycon-powerpoint-python/index.html` about Anand's original *Data visualisation in PowerPoint with Python* talk, PyCon India, **Sunday 1 September 2013** (43-minute recording). It's the tale of a programmer who makes hundreds of objects move inside PowerPoint, including an IMDb Top 250 gallery and newspaper/business graphics—because PowerPoint, improbable as it sounds, was where his audiences and clients needed the work. The narration should be funny, insightful, visually compelling, and historically faithful. **Do not build a bland transcription/timeline or a Python tutorial.**

Use the repository's **`.agents/skills/talk-story/SKILL.md`** and relevant data-story, interactive-storytelling, design and browser QA skills. Look at the working story/player implementations in `../2026-10-05-tds-orientation/index.html`, `../2026-10-07-iitm-ed-data-visualization/index.html`, `../2024-08-10-tedx-mdi-gurgaon/index.html` and `../2015-02-28-tedx-nmims-bangalore/index.html`. Reuse stable interactions, not another site's typography, palette or page layout. The narrative must have **its own visual identity**.

## Read in this order

1. **`transcript.md` and [the original YouTube recording](https://youtu.be/aKCXj1DyEhM)**. Speaker quotations must be verbatim, and important anchors checked against the recording; the automated transcript has sparse timestamps in long demo passages. Original video **ID aKCXj1DyEhM is the only player source**.
2. **`story-context.md`** — researched narrative spine, cold opens, scene options, exact seek anchors, editorial guardrails and interaction opportunities. Editorial guidance, not a required chapter order.
3. **`research-notes.md`** — primary-document ledger and context checks, including the crucial correct event date (**1 Sep 2013**, not 6 Sep video upload); original notebook, client anecdotes, Office/COM limits and sources.
4. **`links.md`** — conference programme/proposal, PyVideo, speaker's 2009 COM post, original PyCon code notebook and primary technical sources. Link evidence at relevant points, not a giant appendix.
5. **Original source code:** `~/code/ipython-notebooks/Office.ipynb` (nbformat 3; `worksheets[0].cells`), public https://github.com/sanand0/ipython-notebooks/blob/master/Office.ipynb . **The exact notebook used on stage** is linked by Anand in a comment on his official PyCon 2013 proposal. Use the original source selectively; don't fake working PowerPoint COM on a web page.
6. **Original video stills:** `slides/*.webp` and `frame-map.md` — 10 authentic frames: COM canvas, IMDb posters, animated sorting, Vijay Karnataka newspaper coverage/cartogram, business work and a Twitter slide. Pick strongest 5–8. You may inspect the original video for a clearer frame and capture it, crediting the original. Avoid stock PowerPoint screenshots.
7. **Local Opus audio:** `2013-09-01-pycon-powerpoint-python.opus` (~43m) exists; link it in the actual story **only after** a real public GitHub release or other valid hosted link has been checked. Do not invent a public URL.
8. **`comic-page.avif` is forthcoming** and will be supplied by the user later. When present, feature prominently near the top, describe it as an *interpretive companion comic*, give it alt text and a lightbox. Do **not** create or substitute a comic here.

## Find the escalating STORY — the tool surprise is not enough

**Thesis:** “A PowerPoint slide became a program because that was where the work needed to end.”

Potential openings:
- Someone physically **drags a PowerPoint window** because the presenter found that this apparently caused 250 posters to render faster—a strange act for a Python conference. Why is he doing this? Rewind to his original challenge.
- 250 posters reorder simultaneously in the *same slide* as the audience clicks between rating and alphabet. What did they just witness?
- The direct opening: **“What the heck is PowerPoint doing in a Python conference?”** Use as quoted speech only after verifying the exact recording.

Make every scene earn the next:
- **0–4 min:** A slide is just shapes; Windows COM lets Python construct and animate them. This is not screen scraping; it is manipulating editable native objects.
- **~4–14 min:** 250 IMDb posters from a Python notebook. Scraping, poster layout, quirky window-drag workaround, human movie-guessing scene, hover titles and links.
- **~15–21 min:** The actual magic: **one collection, two useful sort orders, hundreds of moving objects**. The talk compares D3/Processing favourably for this particular 2013 exercise; treat this as a speaker claim.
- **~21–31 min:** “Is it useful?” Newspaper spreads from Vijay Karnataka, an election cartogram when maps were unavailable, and paid/customer-oriented presentation visuals. Familiar editable output beats “cool library purity.”
- **~31–35 min:** Live tweets inside PowerPoint, including comedic demo rough edges. This turns a slide into a primitive live dashboard.
- **~35–43 min:** Audience asks about Macs/Keynote, reusability, effort, distribution, Office API boundaries. Finish on the tradeoff, not a sales pitch.

The strongest payoff might be **“the most interesting programming environment wasn't the one on stage; it was the one the client already opened every day.”** This is an editorial synthesis, NOT a fabricated stage quotation. Keep 2013 technology details historically dated, without retroactively inserting 2026 AI claims.

## Make the surprise felt

- **One high-quality interactive sort**: present an *illustrative, explicitly labelled* grid of several movie-like items, then animate rank/title reorder so the user can locate an item and appreciate preserving identity across states. Better still, recover actual 2013 notebook sample data and cite it; **never call a current IMDb Top 250 the 2013 set**.
- A compact COM-to-slide visualization explaining `Application → Presentation → Slide → Shape` with a real snippet from `Office.ipynb`; don't implement fake COM in JavaScript.
- A brief, legible side-by-side of source code/output to illustrate office program as an editable visualization medium; 2–3 **meaningful** interactions total. Don't clutter with generic counters or animation for animation's sake.
- Images must be authentic video frames or original code/rendering with clear source. Treat the Karnataka voting graphic as a historical newspaper example, not an independently verified election dataset.

## Required player / reading interaction

Create a **reader-first article with a persistent original YouTube IFrame player** and a reversible **Story ↔ Video** focus control. One playing instance; don't tear it down or reset it when toggling. In-story timestamps link/seek to the matching moment. Support URL deep-link restores, browser history navigation, play/pause, keyboard navigation, transcript popup, sticky/compact player on long scroll if appropriate, and responsive mobile layout. Take proven patterns from the 2026 and 2024 reference stories; test them, including when YouTube embedding is unavailable. Keep story focus attractive even for someone who never presses Play.

**ONLY VIDEO:** https://youtu.be/aKCXj1DyEhM . Do not search for, produce, encode, upload, link or fall back to a WebM/MP4 copy or a different recording. The extracted `slides/*.webp` are legitimate authentic archival stills; they are not video sources.

## Fact-check, publication and QA

- Original talk **1 Sep 2013**, PyCon India at Bangalore's NIMHANS. Previous catalog date 6 Sep 2013 corresponds to recording upload; `config.json` must be corrected **when publishing the finished page**. Never leave a primary page link pointing to a missing `index.html`.
- Distinguish Windows-only 2013 COM capabilities, today's Office versions and what the speaker thinks is easier than D3. Do not report a financial amount, current customer endorsement or exactly who paid for what without proof.
- Credit `Office.ipynb` as code from the talk, the 2009 blog post as prior technique, and the actual paper/newspaper/spread as source imagery.
- Cite/label authentic screenshots and reproduce only short excerpts from movies, artworks and newspapers. No fabricated 2013 logos, headlines, votes, poster grids or charts.
- Avoid overlong blocks: break sections every 1–3 paragraphs with a relevant original visual, quote, code, interactive or contrasting full-bleed band. The page should have a crisp narrative arc, surprising demonstrations and clean editorial typography.
- Follow skill's stringent QA: quote/speaker attribution sweep, seek accuracy, focus toggle preserving playback, links, lightbox and transcript affordance, color contrast in all bands, section navigation, mobile no-overflow, keyboard/reduced motion, legal/embed availability. Test actual pages with browser tooling.
- **Do not commit, push, deploy or generate the final HTML until asked**; this `prompts.md` is the ready-to-run next-stage instruction after the comic is provided.

PS: Another process is updating ./config.json, ./README.md, etc. - so avoid conflicts.

---

When I click "Alphabetical" or "Rating" on the poster grid, I assumed the titles will smoothly animate. Nothing happened.
The .trip figures are left-aligned. I'd rather they were centered.
There may be other similar errors. Find and fix them.

<!-- claude --resume 91ee4ffe-5a58-4c51-bb15-ce49f83b0824 -->

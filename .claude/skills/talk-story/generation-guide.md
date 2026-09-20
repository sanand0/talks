# Talk Story — HTML Generation Guide

This reference is loaded by the `talk-story` skill when generating `index.html`.

**Reference implementations go stale; this file's rules don't.** Where a component below names a
specific talk, that was the best example *when written* — the pattern has usually improved since.
Before copying one, find the newest talk that has it and prefer that:
`grep -l 'class="jump"' 20*/index.html | sort | tail -2` (swap in the class you need; `sort` matters
— `grep` here may be a ugrep wrapper that returns matches out of order). Copy the markup and JS from the live example; take the *rules* below as the constraints
that example must satisfy — if they disagree, the rule here wins and the example is the stale one.

## Table of contents

1. [Design philosophy](#design-philosophy)
2. [CSS variables and fonts](#css-variables-and-fonts)
3. [Layout structure](#layout-structure)
4. [Key UI components](#key-ui-components)
5. [Chunking strategy](#chunking-strategy)
6. [Common pitfalls](#common-pitfalls)

---

## Design philosophy

- **Malcolm Gladwell narrative style**: Open with a specific scene or anecdote, build to insight, weave in surprising context.
- **Typography first**: The text should be beautifully readable at 18–20px with generous line-height (1.7–1.8).
- **Scannable**: Use **bold** on key phrases so that reading only the bolded text summarises the article.
- **Breathe**: Generous whitespace. Sections separated by full `margin: 4rem 0`. Every full-width band, wrap, and embed needs a bottom margin.
- **Break out of the column**: Full-width sections with contrasting background colours create visual rhythm. Use for the visual summary, pull quotes, slide galleries, embeds, takeaways.
- **No horizontal scroll**: `body { overflow-x: hidden }` plus `width: 100vw; margin-left: calc(50% - 50vw)` is the ONLY safe breakout pattern.

---

## CSS variables and fonts

Derive the palette and fonts from the example talks named in the prompt (default: the 3 most
recent talks) — loosely, not strictly. Vary them per talk so the pages don't look cloned.
Recent talks used e.g. Fraunces + Source Serif 4 + JetBrains Mono; older ones used Cormorant
Garamond + Libre Baskerville + IBM Plex Mono. Define everything as CSS variables
(`--ink`, `--paper`, `--accent`, `--muted`, `--border`, `--dark`, `--font-display`,
`--font-body`, `--font-mono`) so bands and components stay consistent.

```css
body {
  font-family: var(--font-body);
  background: var(--paper);
  color: var(--ink);
  line-height: 1.78;
  font-size: 18px;
  overflow-x: hidden;   /* ALWAYS include this */
}
```

---

## Layout structure

```html
<body>
  <div class="progress-bar"></div>

  <!-- Sticky header -->
  <header class="masthead">
    <div class="masthead-inner">
      <span class="masthead-brand">TALKS · SANAND0</span>
      <span class="masthead-date"><!-- date --></span>
    </div>
  </header>

  <!-- Hero -->
  <section class="hero">
    <div class="hero-inner">
      <div class="event-label"><!-- Event name --></div>
      <h1 class="hero-title"><!-- Talk title --></h1>
      <p class="hero-subtitle"><!-- One sentence description --></p>
      <div class="hero-meta">
        <!-- date · venue · speaker links -->
        <!-- link to transcript · audio player if audio exists -->
      </div>
    </div>
  </section>

  <!-- Full-width sketchnote (if exists) -->
  <div class="sketchnote-wrap">
    <img src="sketchnote.avif" alt="Sketchnote" ...>
  </div>

  <!-- Main article column -->
  <article class="article">
    <!-- narrative sections, blockquotes, pull quotes, slide grids -->
  </article>

  <!-- Full-width takeaways -->
  <section class="takeaways-wrap">
    <div class="takeaways-inner">
      <h2>Top Takeaways</h2>
      <ol>...</ol>
    </div>
  </section>

  <!-- Footer -->
  <footer>...</footer>

  <!-- Section jump nav: fixed bottom bar, prev/next + "Jump to…" menu -->
  <div class="jump-backdrop" id="jump-backdrop"></div>
  <nav class="jump" aria-label="Jump to section">...</nav>

  <!-- Lightbox overlay (for image popups) -->
  <div id="lightbox" class="lightbox" onclick="closeLightbox()">
    <img id="lightbox-img" src="" alt="">
  </div>

  <!-- Popup overlay (for citations and rich content) -->
  <div id="popup-overlay" class="popup-overlay" onclick="closePopup()">
    <div class="popup-box" onclick="event.stopPropagation()">
      <button class="popup-close" onclick="closePopup()">×</button>
      <div id="popup-content"></div>
    </div>
  </div>

  <script>/* progress bar, lightbox, popup JS */</script>
</body>
```

### Column width

```css
.article { max-width: 720px; margin: 0 auto; padding: 0 1.5rem; }
.hero-inner { max-width: 720px; margin: 0 auto; padding: 0 1.5rem; }
```

### Full-width breakout pattern (NO horizontal scroll)

```css
.sketchnote-wrap,
.pull-quote-wrap,
.slide-grid-wrap,
.takeaways-wrap {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  padding: 3rem 2rem;
  background: var(--dark);
  color: #f0ece4;
}
```

---

## Key UI components

### Blockquote (memorable quotes from transcript)

Make blockquotes stand out. They should be visually prominent — bigger, with room to breathe,
and ideally wider than the main column so they feel like a pause in the reading flow.

```html
<blockquote class="pull-quote">
  <p>"The quote text here."</p>
  <cite>— Speaker Name</cite>
</blockquote>
```

Crib the styling from a recent talk's `.pull-quote`. The rules that matter: a negative horizontal
margin (~`-10%`) so it breaks the column without going full-width; larger, italic, accent border;
`cite` un-italicised and quieter; and a `@media (max-width: 600px)` rule zeroing those negative
margins so it doesn't overflow a phone.

### Slide thumbnail grid

```html
<div class="slide-grid-wrap">
  <div class="slide-grid">
    <figure class="slide-card" onclick="openLightbox('slide-01.avif', 'Slide 1')">
      <img src="slide-01.avif" alt="Slide 1" loading="lazy">
    </figure>
    <!-- repeat for each relevant slide -->
  </div>
</div>
```

`.slide-grid` is a centred `max-width: 1100px` grid of ~200px thumbnails with `cursor: zoom-in`.
`auto-fill` is fine here — it's one grid with nothing to align against (unlike the jump menu).

### Audio player

Audio files are always `.opus`. Place the player in the hero meta section (near the top).

```html
<div class="audio-player">
  <span>🎧 Listen to the recording</span>
  <audio controls preload="metadata" style="width:100%; margin-top:0.5rem; display:block;">
    <source src="audio.opus" type="audio/ogg; codecs=opus">
  </audio>
</div>
```

### Video

YouTube → the iframe card below. A hosted recording (`.webm`, usually on `media.s-anand.net`) →
a `<video>` element with a nested `<source>`, in a full-width container near the top:

```html
<video controls preload="metadata" width="100%">
  <source src="https://media.s-anand.net/<talk>.webm" type='video/webm; codecs="vp9, opus"'>
</video>
```

Short demo clips woven into the narrative (a tool in action, a render, a screen capture) play
themselves — `autoplay muted loop playsinline` with no controls — and carry a caption linking to
the demo, or to the video itself if there's no demo page.

### Tooltip

```html
<span class="tooltip-trigger" data-tip="Brief explanation here">term</span>
```

```css
.tooltip-trigger { border-bottom: 1px dotted var(--accent); cursor: help; position: relative; }
.tooltip-trigger::after {
  content: attr(data-tip);
  position: absolute; bottom: 120%; left: 50%; transform: translateX(-50%);
  background: var(--dark); color: #fff; padding: 0.5rem 0.75rem;
  border-radius: 4px; font-size: 0.85rem; white-space: normal;
  width: 220px; pointer-events: none; opacity: 0; transition: opacity 0.2s;
  font-style: normal;
}
.tooltip-trigger:hover::after { opacity: 1; }
```

### Popup button (for citations, rich content)

The cite button should feel like part of the text flow — a small superscript-style marker.
Do NOT use `vertical-align: super` (breaks line spacing) or remove the border entirely (feels incomplete).

```html
<sup><button class="cite-btn" onclick="openPopup('popup-id-1')" title="View source">①</button></sup>
<div id="popup-id-1" class="popup-data" hidden>
  <h3>Title</h3>
  <p>Rich content here. Can include images, links, markdown converted to HTML.</p>
  <a href="https://source.url" target="_blank">Read more ↗</a>
</div>
```

Style `.cite-btn` as a small monospace chip: transparent, 1px accent border, accent text,
`line-height: 1`, inverting on hover. Crib exact values from a recent talk.

### Chat / prompt excerpt

Verbatim prompts and AI responses are some of the best material in these talks — show them inline
in a block visibly distinct from `.pull-quote` (mono face, labelled "Prompt" / "Response", its own
background), not buried in a popup. Pair the snippet with a popup holding the fuller chat
(a local `.md` rendered as HTML) and a link to the SHARE URL of the original chat.

```html
<div class="prompt-box">
  <div class="plabel">Prompt</div>
  <p>Verbatim prompt text…</p>
  <a href="chat-thing.md" onclick="openPopup('chat-thing'); return false;">Read the full chat ↗</a>
</div>
```

`.prompt-box a` must set its own colour — and the base prose link rule must not out-specify it
(see the specificity trap in Common pitfalls).

### YouTube embed card

```html
<div class="video-card">
  <iframe src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allowfullscreen
    style="width:100%; aspect-ratio:16/9; border-radius:6px;"></iframe>
</div>
```

### Link screenshot card

```html
<a class="link-card" href="URL" target="_blank">
  <img src="screenshot-slug.webp" alt="Description" loading="lazy">
  <div class="link-card-body">
    <strong>Title</strong>
    <p>Brief description</p>
  </div>
</a>
```

A bordered column: 16/9 `object-fit: cover` screenshot above a padded body, `color: inherit`, lifting
on hover. This is also the fallback for any page that refuses to be framed — screenshot it (CDP at
localhost:9222, or `uvx rodney`) and card it instead of shipping a blank iframe.

### Section jump navigation

Always include a way to jump to any section from anywhere — a required default, not a decorative
extra, and the CSS alone is useless: copy the markup and the JS wiring too. A fixed bottom bar with
prev/next buttons plus a current-section label that opens a menu listing every section, grouped by
act. Current best example: `2026-09-19-shree-niketan-schools/index.html` (fixed columns,
left-aligned menu) — but find the newest per the pointer rule at the top of this file:
`grep -l 'class="jump"' 20*/index.html | sort | tail -2`. Older ones still carry the `auto-fit` bug
below.

```html
<div class="jump-backdrop" id="jump-backdrop"></div>
<nav class="jump" aria-label="Jump to section">
  <button id="jump-prev" aria-label="Previous section">‹</button>
  <span class="jump-cur" id="jump-cur">Opening <span class="caret">▾</span></span>
  <button id="jump-next" aria-label="Next section">›</button>
  <div class="jump-menu" id="jump-menu">
    <div class="jm-group">Opening</div>
    <div class="jump-grid"><a href="#sec-1">Title<small>subtitle</small></a>…</div>
    <!-- repeat group heading + grid per act -->
  </div>
</nav>
```

The JS tracks the active section (`IntersectionObserver` or scroll position), updates `#jump-cur`
and the `.is-cur` link, wires prev/next, and toggles `.open` on the menu and backdrop.

```css
/* FIXED column count — NOT auto-fit/auto-fill */
.jump-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: .35rem; }
@media (max-width: 640px) { .jump-grid { grid-template-columns: repeat(2, 1fr); } }
```

**Why fixed columns**: `repeat(auto-fit, minmax(170px, 1fr))` sizes each grid container
independently, so a 2-item group, a 3-item group and a 1-item group each get a different column
count and their edges don't line up — the menu reads as ragged. Any repeating grid split across
sibling containers that must align with each other (grouped nav menus, multi-section card grids)
needs an explicit `repeat(N, 1fr)`.

### Animated SVG (for process explanations)

Keep SVGs self-contained with `<animate>` or `<animateTransform>` tags. No external JS needed.
Width 100%, viewBox set for content. Add `role="img"` and `aria-label`.

---

## Chunking strategy

**Chunk 1 — Scaffold** (~150 lines):
```
<!DOCTYPE html> through </style></head>
<body>
  progress-bar div
  masthead header
  hero section
  sketchnote-wrap (if sketchnote exists)
  <article class="article"> ← open tag only
```

**Chunk 2 — Narrative first half** (~300–400 lines):
```
  Opening anecdote + first 40–50% of narrative
  First blockquotes, first images
```

**Chunk 3 — Narrative second half + media** (~300–400 lines):
```
  Remaining narrative
  Slide grid section (if slides exist)
  YouTube embed (if video URL in context)
  Additional link cards
  </article>
```

**Chunk 4 — Closing** (~200 lines):
```
  takeaways-wrap section
  footer
  lightbox overlay div
  popup overlay div + all popup-data divs
  <script> blocks
  </body></html>
```

---

## Common pitfalls

### Horizontal scroll (the #1 recurring issue)

This appears in almost every generated talk and must be explicitly prevented.

**Root cause**: Any element with `margin-left: -Nvw`, `margin: 0 -100vw`, or `width: 100vw`
without the correct centring trick will cause horizontal overflow.

**The only safe full-width pattern**:
```css
body { overflow-x: hidden; }  /* MUST be on body */

.any-full-width-element {
  width: 100vw;
  margin-left: calc(50% - 50vw);  /* NOT -100vw, NOT -50vw */
}
```

After completing all chunks, grep the file: `grep -n 'margin.*-[0-9]*vw\|margin.*-50%' index.html`
Any match is a horizontal scroll bug — replace with the pattern above.

### Low contrast inside coloured bands (the #2 recurring issue)

Every full-width band with a non-default background needs explicit colours for ALL content it
contains — body text, `<a>`, `<strong>`, figcaptions, labels. Recurring corrections:
black `strong` on dark red, dark-yellow links on light yellow, accent-coloured links on black,
faint captions and band labels. After generating, walk through each band class and check every
descendant style in both light and dark contexts.

**The usual root cause**: `--muted` and `--accent` are tuned against `--paper`, then inherited
unchanged inside a band with a different background. Captions, `figcaption`, band labels and
`.card` subtitles are the repeat offenders (`.sketchnote-caption`, `.band-label`,
`.full-embed-label a`, `.wf-grid figcaption` have all had to be corrected). Give each band its own
muted/link/label tokens rather than reusing the page-level ones, and size band labels for the
prominence they deserve — "too light AND too small" is one complaint, not two.

**Check hover and focus too**, not just the resting state: a `:hover` rule that swaps background
or colour can land text on a near-identical background (`.doclink` on hover was unreadable). Every
interactive element needs contrast in all of resting, hover, and keyboard-focus states.

### Prose link colour beating a component's own link colour (specificity trap)

**Root cause**: a base rule like `.wrap p a, .wrap li a, .wrap-wide > p a { color: var(--teal-dk); }`
scores (0,1,2) — *higher* than a component override like `.prompt-box a { color: #9fd8e6; }` (0,1,1).
Component markup normally wraps its text in `<p>`, so the prose rule wins and the link renders dark
teal on a near-black box: invisible. A per-band contrast sweep misses this unless it traces the cascade.

**The fix**: scope prose link/text rules to the wrapper alone — never add a `p`/`li`/`h*` qualifier —
and define them *before* component rules so source order settles equal-specificity ties:
```css
.wrap a, .wrap-wide a { color: var(--teal-dk); }   /* base — defined FIRST, lowest specificity */
.prompt-box a { color: #9fd8e6; }                  /* any component override now wins */
```
Verify: `grep -nE '\.wrap[a-z-]*( *>)? +(p|li|h[1-6])[^,{]* a[ ,{]' index.html` must return nothing.

### Markdown rendered into a modal/popup loses list indentation

**Root cause**: the reset `*, *::before, *::after { margin: 0; padding: 0 }` zeroes the browser's
default `<ul>/<ol>` indent everywhere. `.wrap ul, .wrap ol { … }` restores it for hand-authored prose,
but `.modal-body` / `#popup-content` are *siblings* of `.wrap`, not descendants, so those rules never
reach them — bullets in a fetched `.md` chat log render flush left with no marker visible.

**The fix**: every container that renders externally-sourced Markdown (marked.js output) needs its own
complete set of element rules — headings, paragraphs, lists, blockquotes, code:
```css
.modal-body h2, .modal-body h3 { margin: 1.2rem 0 .5rem; }
.modal-body p  { margin: 0 0 .8rem; }
.modal-body ul, .modal-body ol { margin: 0 0 .8rem 1.4rem; }  /* the reset killed the indent */
.modal-body li { margin-bottom: .35rem; }
.modal-body blockquote { margin: 0 0 .8rem; padding-left: .9rem; border-left: 3px solid var(--border); }
```
Verify by opening a popup whose source `.md` file contains a bulleted or numbered list.

### Missing bottom margins (the #3 recurring issue)

`.band`, `.wrap`, `.embed`, `.stat-band`, `.gallery-band` and similar full-width sections need
`margin-bottom: 2rem` (or more). Text starting flush against the previous band is a recurring
correction.

### Other pitfalls

- **Misattributed quotes**: transcripts often mislabel speakers. Verify every quote's speaker;
  flag doubtful ones. This has caused more user corrections than any layout bug.
- **Buttons instead of links**: anything that leads to content should be an `<a>` (so
  right-click → open in new tab works), with the click intercepted for popups.
- **Cramped cards**: give card groups extra width (breakout container) so 3–4 fit per row on
  desktop; render takeaways as cards, not a plain list.
- **Orphan card in the last row** (distinct from cramped cards — a count bug, not a width bug):
  for N cards and C columns, if `N mod C == 1` the final row holds one lonely card. Check this
  per card group before settling the CSS, then either pick a C that divides N (5 cards → 5 across
  on wide screens, or a deliberate 2+3 split), or add/merge a card so the rows fill. Extra width
  alone does not fix it.
- **Private links leaked**: `chatgpt.com/c/`, `claude.ai/chat/`, `gemini.google.com/app` must
  never appear — use the share links; anything in `<!-- comments -->` stays out.
- **Broken popup JS**: The `openPopup(id)` function should copy `innerHTML` of `#id` into `#popup-content`. Check that every `openPopup('X')` call has a matching `id="X"` element.
- **Audio not playing**: Use `<audio controls preload="metadata">` with a nested
  `<source src="audio.opus" type="audio/ogg; codecs=opus">`. Never use `<audio src="...">` directly.
- **Truncated chunks**: End each chunk at a complete HTML element boundary, never mid-tag or mid-attribute.
- **TODOs left in file**: `grep -c "TODO" index.html` before finalising — must be 0.
- **White text on white**: Any element inside a dark-background container that inherits `--ink` colour will be invisible. Set explicit `color: #f0ece4` or similar on dark sections.
- **Multiple `<main>` tags**: Only one `<main>` per page. Use `<article>`, `<section>`, or `<div>` for inner wrappers.

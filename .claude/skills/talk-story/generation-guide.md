# Talk Story — HTML Generation Guide

This reference is loaded by the `talk-story` skill when generating `index.html`.

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

```css
blockquote.pull-quote {
  border-left: 4px solid var(--accent);
  padding: 1.25rem 2rem;
  /* Extend 10% past each side of the column — visually striking, not full-width */
  margin: 2.5rem -10%;
  font-style: italic;
  font-size: 1.2rem;
  line-height: 1.65;
  background: var(--highlight-bg);
  border-radius: 0 4px 4px 0;
}
blockquote.pull-quote cite {
  display: block;
  margin-top: 0.75rem;
  font-size: 0.9rem;
  font-style: normal;
  color: var(--muted);
  letter-spacing: 0.03em;
}
/* On narrow viewports, don't overflow the screen */
@media (max-width: 600px) {
  blockquote.pull-quote { margin-left: 0; margin-right: 0; }
}
```

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

```css
.slide-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 0.75rem; max-width: 1100px; margin: 0 auto; }
.slide-card { cursor: zoom-in; border-radius: 4px; overflow: hidden; margin: 0; }
.slide-card img { width: 100%; display: block; }
```

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

```css
.cite-btn {
  background: none;
  border: 1px solid var(--accent);
  color: var(--accent);
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
  font-size: 0.72rem;
  cursor: pointer;
  font-family: var(--font-mono);
  line-height: 1;
}
.cite-btn:hover { background: var(--accent); color: #fff; }
```

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

```css
.link-card { display: flex; flex-direction: column; border: 1px solid var(--border); border-radius: 6px; overflow: hidden; text-decoration: none; color: inherit; transition: box-shadow 0.2s; }
.link-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.12); }
.link-card img { width: 100%; aspect-ratio: 16/9; object-fit: cover; }
.link-card-body { padding: 0.75rem 1rem; }
```

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
- **Private links leaked**: `chatgpt.com/c/`, `claude.ai/chat/`, `gemini.google.com/app` must
  never appear — use the share links; anything in `<!-- comments -->` stays out.
- **Broken popup JS**: The `openPopup(id)` function should copy `innerHTML` of `#id` into `#popup-content`. Check that every `openPopup('X')` call has a matching `id="X"` element.
- **Audio not playing**: Use `<audio controls preload="metadata">` with a nested
  `<source src="audio.opus" type="audio/ogg; codecs=opus">`. Never use `<audio src="...">` directly.
- **Truncated chunks**: End each chunk at a complete HTML element boundary, never mid-tag or mid-attribute.
- **TODOs left in file**: `grep -c "TODO" index.html` before finalising — must be 0.
- **White text on white**: Any element inside a dark-background container that inherits `--ink` colour will be invisible. Set explicit `color: #f0ece4` or similar on dark sections.
- **Multiple `<main>` tags**: Only one `<main>` per page. Use `<article>`, `<section>`, or `<div>` for inner wrappers.

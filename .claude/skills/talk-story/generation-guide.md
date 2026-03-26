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
- **Breathe**: Generous whitespace. Sections separated by full `margin: 4rem 0`.
- **Break out of the column**: Full-width (`width: 100vw; margin-left: calc(-50vw + 50%)`) sections with contrasting background colours create visual rhythm. Use for sketchnote, pull quotes, slide galleries, takeaways.
- **No horizontal scroll**: Every `width: 100vw` element MUST use `overflow-x: hidden` on body, or use `margin-left: calc(50% - 50vw); width: 100vw` with `body { overflow-x: hidden }`.

---

## CSS variables and fonts

```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,500&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
:root {
  --ink:          #0f0f0f;
  --paper:        #f8f6f1;
  --accent:       #b8243f;
  --gold:         #c49b2a;
  --muted:        #5e5e5e;
  --faint:        #9a9a9a;
  --border:       #d9d5cc;
  --highlight-bg: #fdf5e6;
  --dark:         #1a1a2e;
  --font-display: 'Cormorant Garamond', Georgia, serif;
  --font-body:    'Libre Baskerville', Georgia, serif;
  --font-mono:    'IBM Plex Mono', monospace;
}

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

```html
<blockquote class="pull-quote">
  <p>"The quote text here."</p>
  <cite>— Speaker Name</cite>
</blockquote>
```

```css
blockquote.pull-quote {
  border-left: 4px solid var(--accent);
  padding: 1rem 1.5rem;
  margin: 2rem 0;
  font-style: italic;
  font-size: 1.15rem;
  background: var(--highlight-bg);
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

```html
<div class="audio-player">
  <span>🎧 Listen to the recording</span>
  <audio controls preload="none" style="width:100%">
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

```html
<button class="cite-btn" onclick="openPopup('popup-id-1')">Source</button>
<div id="popup-id-1" class="popup-data" hidden>
  <h3>Title</h3>
  <p>Rich content here. Can include images, links, markdown converted to HTML.</p>
</div>
```

```css
.cite-btn { background: none; border: 1px solid var(--accent); color: var(--accent); padding: 0.15rem 0.5rem; border-radius: 3px; font-size: 0.8rem; cursor: pointer; vertical-align: middle; }
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

- **Horizontal scroll**: Always add `overflow-x: hidden` to `body`. Full-width elements MUST use `margin-left: calc(50% - 50vw)` pattern, not `margin: 0 -100vw`.
- **Broken popup JS**: The `openPopup(id)` function should read the `innerHTML` of `#id` and inject it into `#popup-content`.
- **Audio not playing**: Always use `<source>` inside `<audio>`, not `src=` directly, for opus files.
- **Truncated chunks**: End each chunk at a complete HTML element, never mid-tag.
- **TODOs left in file**: Search for "TODO" before finalising.

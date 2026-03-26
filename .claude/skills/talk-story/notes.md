# Talk Story Skill — Notes

## Process

### What I studied

Examined 12 `prompts.md` files across talks dating from 2025–2026. Key patterns that repeat
in virtually every prompt:

- **Malcolm Gladwell narrative style** — always the writing target
- **Chunked generation** — almost every prompt warns about token limits, asks for small chunks
- **Three fixed reference talks** — `2026-02-11-amat-dt-day`, `2025-12-06-mining-digital-exhaust`,
  `2026-01-11-nptel-vibe-coding-workshop` appear as example files in 4+ prompts
- **Full-width breakout sections** — sketchnote, pull quotes, slide grids all expand beyond the
  column and use a contrasting background
- **Horizontal scroll bug** — appears in 4 prompts as something to fix; always caused by
  full-width elements using `-100vw` margin rather than the `calc(50% - 50vw)` pattern
- **Popup pattern** — tooltips for brief context, popups for rich citations/reference material,
  animated SVGs for process explanations
- **Top takeaways** — every talk ends with a numbered list
- **Audio player** — present whenever `audio.opus` exists
- **Sketchnote** — always full-width near the top, clicking opens full-size
- **README update** — always asked to update the main README

### SKILL.md best practices applied

- Description written in third person with trigger conditions
- Under 500 lines (SKILL.md itself is ~130 lines)
- Progressive disclosure: generation details in `generation-guide.md`, not inlined
- Clear numbered workflow — Claude can check off steps
- `${CLAUDE_SKILL_DIR}` used to reference scripts portably
- `context.md` pattern for user input: Claude infers as much as possible, marks TODO, stops and
  asks before generating HTML — no silent failures
- Chunk strategy specified exactly (4 chunks) to prevent Claude from trying to write everything
  at once

---

## Evaluations

### Sample 1: `2026-03-12-nie-ai-roadmap/`

**Assets present:** `transcript.md`, `sketchnote.avif`, 33 `slide-*.avif` files (already extracted),
`story.html` (prior attempt), `index.html` (final version). No audio, no context.md.

**Trace through skill:**
1. Directory found, `transcript.md` exists ✓
2. Inventory: sketchnote ✓, 33 slide images ✓, no audio, no PDF
3. No PDF → skip conversion
4. No `context.md` → skill reads transcript, infers:
   - Speakers: **Srikanth** (co-founder of Trustt), **Anand** (LLM Psychologist at Straive), plus **N.R. Narayana Murthy** in audience
   - Date: 12 Mar 2026 (from directory name and transcript)
   - Event: NIE, Mysore
   - TODOs: LinkedIn URLs, YouTube URL, deployment URL, additional demo links
5. Creates `context.md`, stops with clear list of what to fill in
6. After user fills in: reads supporting context, generates chunked HTML
7. With 33 slides available, would create a thumbnail grid section
8. Strong quotes available (Narayana Murthy quotes about AI summit: *"In any of these things, you should not have more than one major speaker in the morning"*)

**Expected output quality:** Excellent. The slide images and a famous speaker in the audience make
this especially rich. The skill would produce output comparable to the actual `index.html`.

**Gap identified:** The `prompts.md` contains additional demo links (LLM pricing, data stories,
etc.) that a first-time `context.md` won't have. User would need to add them to `context.md`
under "Links to weave in".

---

### Sample 2: `2026-03-21-design-in-the-age-of-infinite-generativity/`

**Assets present:** `transcript.md`, `sketchnote.avif`, `audio.opus`, 25+ images (`.avif`, `.webp`),
3 videos (`.webm`), `everyday-design.md`, `sustainable-ideas.md`, `critique.html`, `index.html`.
No context.md.

**Trace through skill:**
1. Directory found, `transcript.md` exists ✓
2. Inventory: sketchnote ✓, audio ✓, images ✓, videos ✓, supporting .md files ✓
3. No PDF, no slide images → skip conversion
4. No `context.md` → infer:
   - Speaker: Anand, LLM Psychologist at Straive
   - Event: Chennai Design Festival, 21 Mar 2026
   - Supporting files: `everyday-design.md`, `sustainable-ideas.md`
   - TODOs: Event URL, YouTube URL, deployment URL, external links from talk
5. Creates `context.md` with supporting files pre-populated, stops
6. After user fills in: rich media page with audio player, image galleries, video embeds,
   `critique.html` embedded in iframe, citations from supporting .md files as popups

**Expected output quality:** Very good. Particularly rich media. The skill correctly identifies
`everyday-design.md` and `sustainable-ideas.md` as supporting files.

**Gap identified:** The `critique.html` embed (with special iframe sizing) and the Xerox-style
image links would need to be listed explicitly in `context.md` under "Additional notes". The skill
doesn't automatically discover `*.html` files as embeds.

---

### Sample 3: `2026-03-15-pyconf-ai-in-sdlc/`

**Assets present:** `transcript.md`, `sketchnote.avif`, `audio.opus`. No slides, no context.md.

**Trace through skill:**
1. Directory found, `transcript.md` exists ✓
2. Inventory: sketchnote ✓, audio ✓, no slides, no PDF, no supporting .md files
3. Skip conversion
4. No `context.md` → infer:
   - Panel: Usha Rengaraju (Chief of Research, Exa Protocol), Anand S (LLM Psychologist),
     Lakshman Peethani (Director, EPAM Systems), Snehith Allamraju (Moderator, RSM US LLP)
   - Event: PyConf Hyderabad 2026, 15 Mar 2026
   - TODOs: Speaker LinkedIn URLs, speaker page URLs, YouTube URL
5. Creates `context.md`, stops
6. After user fills in: panel narrative with multiple voices; excellent transcript quotes
   (*"I am saving like 60, 70 lakhs on interns' salaries every year"*, *"AI is my SDLC"*)

**Expected output quality:** Good. No slides, but the panel format has rich multi-voice quotes
that the Malcolm Gladwell structure handles well. Audio player adds value.

**Gap identified:** For panel talks, the skill could suggest a "speaker introduction" section at
the top (like the existing `index.html` does with profile cards). This isn't in the current
generation guide.

---

## What works well

1. **Context-first approach**: Stopping before generation to fill `context.md` prevents the most
   common failure — generating an HTML with wrong names, dates, or missing links.

2. **Chunk strategy**: The 4-chunk plan mirrors what worked in practice (all prompts.md request
   chunked generation). Specifying exactly 4 chunks removes ambiguity.

3. **Script modularity**: PDF conversion and screenshot are separate scripts, so they can be
   improved independently without touching the skill.

4. **`generation-guide.md` separation**: Keeps SKILL.md readable while providing Claude with
   the exact CSS patterns that avoid known bugs (horizontal scroll, broken audio, etc.).

5. **TODO sentinel**: Using `TODO:` in context.md makes it scannable — Claude can grep for
   remaining TODOs before finalising HTML.

---

## Suggested improvements

### Near-term

1. **Auto-embed `*.html` files**: If a directory contains `.html` files other than `index.html`,
   the skill should list them in `context.md` as potential iframe embeds (e.g. `critique.html`,
   `weekly-report-data-story.html`). Currently the user must add these manually.

2. **Speaker profile cards section**: For panel talks (multiple speakers detected), suggest a
   speaker introduction section with cards — name, role, photo if available. The transcript
   intro often contains enough info.

3. **Sketchnote generation prompt**: The `prompts.md` files all include a "Sketchnote" section
   instructing Gemini to generate one. A companion skill `/talk-sketchnote` could handle this.
   It's currently a separate workflow (Gemini, not Claude Code).

4. **Screenshot automation trigger**: If the `context.md` "Screenshots" section is empty but
   links in the "Links to weave in" section look interactive (tools, data visualizations,
   GitHub Pages), prompt the user to move them to the Screenshots section.

5. **YouTube timestamp links**: Several talks include `<a href="https://youtu.be/...?t=NNN">`
   links at quotes. The skill could extract YouTube timestamp patterns from transcripts
   (e.g. `[00:05:23]`) and auto-link blockquotes to the video.

### Longer-term

6. **Design variant selection**: The skill currently defaults to two example talks. A
   `context.md` field `## Design mood` (options: `magazine`, `academic`, `minimal`) could
   steer towards different CSS variable sets and layout densities.

7. **Incremental update mode**: When `index.html` already exists, a `/talk-story --update`
   mode that reads the existing file and only adds new sections (e.g. adding a YouTube video
   that wasn't available at first generation) would be useful.

8. **Validation script**: A `scripts/validate-html.sh` that checks for horizontal scroll
   triggers, broken image `src` attributes (missing files), and TODOs left in the HTML.

9. **Multi-model sketchnote support**: The user currently uses Gemini for sketchnotes. A
   `scripts/sketchnote.sh` wrapper around Claude Artifacts API could close this gap.

10. **README format consistency**: The main README.md uses a table with columns for date, title,
    and link. The skill updates README, but a dedicated `scripts/update-readme.sh` would make
    this reliable across README format changes.

---

## Files created

```
.claude/skills/talk-story/
├── SKILL.md               # Main skill (130 lines) — workflow and entry point
├── generation-guide.md    # HTML patterns, CSS, component library, chunk strategy
├── context-template.md    # Template Claude copies to <talk-dir>/context.md
├── scripts/
│   ├── pdf-to-images.sh   # PDF → AVIF/WebP slide images (poppler + avifenc/ImageMagick)
│   └── screenshot-url.sh  # URL → WebP screenshot (Playwright / Puppeteer / Chromium)
└── notes.md               # This file
```

## Design decisions

- **Folder**: `.claude/skills/talk-story/` — standard Claude Code skill location, co-located
  with the repo rather than `~/.claude/` so the skill travels with the codebase.
- **`context.md` in talk dir, not a global config**: Each talk has unique context. Keeping it
  per-talk avoids cross-talk and lets the file be committed alongside the talk.
- **Two-step flow (context → generate)**: The alternative (one big prompt with all context
  gathered interactively) is fragile in automated/headless use. The file-based approach is
  reproducible and inspectable.
- **AVIF primary, WebP fallback**: AVIF is ~50% smaller than WebP at same quality; it's
  supported by all major browsers since 2023. WebP is the fallback for environments without
  `avifenc`.

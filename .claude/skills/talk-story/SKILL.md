---
name: talk-story
description: Generate an engaging narrative HTML story page for a conference talk or workshop. Use when the user asks for a "narrative story" about a talk, typically pasting a prompts.md-style brief for a talk directory containing transcript.md. Handles context gathering, PDF-to-slide conversion, screenshots, chunked HTML generation in Malcolm Gladwell narrative style, and a quality/fact-check pass. Invoke as /talk-story <talk-dir> or when the user's prompt names the talk directory.
allowed-tools: Read, Glob, Grep, Bash, Write, Edit, WebFetch, WebSearch
---

# Talk Story Generator

Generates a magazine-style narrative HTML page (`index.html` or `story.html`) for a talk.

The user's prompt is the source of truth. It usually specifies the event, speakers, output
file, example talks, media assets, and a link list with LINK / EMBED / DO NOT LINK directives.
This skill supplies everything the prompt doesn't repeat: style, structure, media conventions,
and the QA pass. Where the prompt contradicts this skill, the prompt wins.

If essential facts (event, date, speaker, output path) are missing and not inferrable from the
prompt, directory name, or transcript, ask the user before generating. Do NOT create a
context.md file.

## Workflow

### 1. Inventory

Resolve the talk directory (from the prompt, `$ARGUMENTS`, or cwd). List its contents.
Typical assets: `transcript.md` (primary content), `summary.avif` / `sketchnote.avif` /
`comic-page.avif` (visual summary), `slide-NN.avif`, `*.pdf`, supporting `.md` files
(chat exports like `claude-chat.md`, `chatgpt-*.md`, `preparation.md`), survey data
(`form.yaml`, `responses.tsv`), extra `.html` pages, images, videos.

Defaults derivable from the directory name `<talk-dir>`:
- Deployment URL: `https://sanand0.github.io/talks/<talk-dir>/`
- Audio (if the prompt mentions a recording): `https://github.com/sanand0/talks/releases/download/talks/<talk-dir>.opus`

### 2. Gather context

Read, in this order:
1. The transcript(s). Multiple transcripts of the same talk: use only content unambiguously
   inferrable from both.
2. Supporting `.md` files and survey data in the directory — mine them for quotes, insights,
   and narrative material.
3. Links in the transcript/prompt that are readable (GitHub → raw, blog posts, local files).
4. The example talks named in the prompt (default: the 3 most recent `index.html`/`story.html`
   in this repo). Read ~300 lines of each for design reference — follow LOOSELY, not strictly.
   Vary the palette and fonts per talk; don't clone one design forever.

Use sub-agents for token efficiency: delegate bulk reading/summarising of long chat exports,
survey analysis, and link research to cheaper models; keep the main context for writing.

Search the web and LIBERALLY add inline links: everything mentioned directly or indirectly in
the talk (tools, papers, people, companies, concepts) plus material giving the reader context.

### 3. Convert / capture assets (only if needed)

- PDF with no `slide-*.avif`: `bash ${CLAUDE_SKILL_DIR}/scripts/pdf-to-images.sh <pdf> <talk-dir>`
- Screenshots: use the existing browser via CDP at localhost:9222 (reuse EXISTING tabs, don't
  open new ones) or `uvx rodney` (start once per batch). Save as `.webp`/`.avif` in the talk dir.

### 4. Write the narrative

See [generation-guide.md](generation-guide.md) for HTML patterns and components.

Style (applies always, even if the prompt doesn't repeat it):
- Malcolm Gladwell: open with a scene, build to insight, weave anecdotes into a narrative arc.
- Weave in plenty of memorable, funny, or insightful quotes as stand-out blockquotes.
  Quotes must be VERBATIM from the transcript — no paraphrase, no punch-up.
- Highlight what was insightful or funny.
- Use **bold** for scannability: reading only the bolded text should summarise the article.
- End with top takeaways rendered as cards.

Structure and media conventions:
- Near the top: video embed (full-width) if there's a recording; audio player
  (`<audio controls preload="metadata">` with a `<source>` element); link to the transcript
  that opens in a popup rendered as HTML.
- Visual summary (`summary.avif` / sketchnote / comic page): prominent, max-width 100%;
  clicking opens the full-size image in a new tab.
- Full-width breakout bands with contrasting backgrounds create rhythm — and every band,
  wrap, and embed gets a bottom margin.
- Card groups get extra width so 3–4 cards fit per row on desktop.
- Tooltips: context for non-obvious terms; extra context for references.
- Popups: citations (cite the key point, link to the source) and supporting material
  (extended quotes, chat excerpts, extracts).

Link conventions:
- Every link the prompt lists MUST appear, at the right place (narrative, caption, or card).
- Use SHARE links only: `chatgpt.com/share/...`, `claude.ai/share/...` or `/public/artifacts/`,
  `gemini.google.com/share/...`. Links inside `<!-- HTML comments -->` in the prompt or
  transcript are PRIVATE — never include them.
- Honour DO NOT LINK instructions: mention the thing, omit the hyperlink.
- Images: include with a caption; image and caption link to the associated URL if any,
  else open the full-size image in a new tab.
- Website embeds: IFRAME in a full-width container, slightly under 100vh (inspect content for
  the right aspect ratio), with a caption linking to the source in a new window.
- Local `.md` files: open in a popup, rendered as HTML (skip or prettify YAML frontmatter).
- Local `.html` files: embed full-width at ~90vh.
- Clickable elements that lead somewhere are `<a>` tags (so right-click → open in new tab
  works), with the click intercepted for popups — not `<button>`s.
- Slides: include only relevant ones, as thumbnails/grids; clicking opens a lightbox.

### 5. Generate in chunks

Claude stalls generating large HTML in one shot. Write the file in small chunks or layered
edits (≤100KB each, practically ~200–400 lines): scaffold+head+hero first, then narrative
sections, then closing (takeaways, footer, overlays, scripts). Save and sanity-check after
each chunk; end every chunk at a complete element boundary.

### 6. QA pass (do this without being asked)

1. **Quote attribution fact-check.** Transcripts frequently mislabel speakers. Re-check every
   quote and attributed statement against the transcript; flag ambiguous attributions to the
   user in your final report. This has been the #1 source of corrections.
2. **Contrast sweep.** Check text, links, `strong`, and captions inside every coloured band
   in both dark and light contexts. Low-contrast links inside bands are the #2 recurring bug.
3. **Spacing.** Bands/wraps/embeds have bottom margins; sections breathe.
4. **No horizontal scroll.** `body { overflow-x: hidden }` plus only the
   `width: 100vw; margin-left: calc(50% - 50vw)` breakout pattern.
   `grep -n 'margin.*-[0-9]*vw' <file>` must return nothing.
5. **All links present.** Grep the output for every URL the prompt required.
6. **No private links leaked.** `grep -nE 'chatgpt\.com/c/|claude\.ai/chat/|gemini\.google\.com/app' <file>`
   must return nothing.
7. **Popups/lightbox work.** Every `openPopup('X')` has a matching `id="X"`; audio uses a
   `<source>` element; no leftover TODOs.

### 7. Finish

- Update the repo `README.md` with this talk, matching the existing format.
- Report: what was generated, quotes whose attribution you're unsure about, links you could
  not resolve, and anything skipped.

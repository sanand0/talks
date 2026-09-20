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
Typical assets: transcript files (sometimes multiple/per-day, occasionally in `README.md`),
`summary.avif` / `sketchnote.avif` / `comic-page.avif` (visual summary), `slide-NN.avif`,
`*.pdf`, supporting `.md` files (chat exports like `*chat*.md`, `preparation.md`),
survey data (`form.yaml`, `responses.tsv`), extra `.html` pages, images, videos.

Respect the output shape in the prompt/existing directory: it may be one story, a landing page
plus `story.html`, companion pages, or a multi-day/multilingual microsite. Existing companion
pages such as surveys, demos, or data stories may be deliberate parts of the talk; inspect and
link/embed them rather than automatically folding everything into the main story. When updating
an existing story, preserve its structure and patch it rather than regenerating it unless a
rewrite is requested.

Defaults derivable from the directory name `<talk-dir>`:
- Deployment URL: `https://talks.s-anand.net/<talk-dir>/`
- Audio (if the prompt mentions a recording): `https://github.com/sanand0/talks/releases/download/talks/<talk-dir>.opus`

### 2. Gather context

Read, in this order:
1. The transcript(s). Multiple transcripts of the same session are noisy versions of the same
   source: reconcile phonetic errors, timestamps, and speaker labels using both; don't discard a
   useful passage just because only one captured it clearly.
2. Supporting `.md` files and survey data in the directory — mine them for quotes, insights,
   and narrative material.
3. Links in the prompt, transcript, and supporting files that are readable (GitHub → raw,
   blog posts, local files). Follow useful ones for context and material worth weaving in.
4. Recent `index.html`/`story.html` files in this repo. Follow these LOOSELY, not strictly.
   Vary the palette and fonts per talk; don't clone one design forever.

Use sub-agents for token efficiency: delegate bulk reading/summarising of long chat exports,
survey analysis, and link research to cheaper models; complex tasks requiring judgement
(planning, analysis, storyline, etc.) to advanced models; keep the main context for writing.

Search the web and LIBERALLY add useful inline links. Link named tools, papers, people,
companies, concepts, demos, and relevant context where they are discussed. Do not rely only on
the URLs explicitly listed in the prompt; mine the transcript/supporting files too. Avoid a
link-dump: links should help the reader at the point they appear.

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
- Keep a visual cadence: never run more than ~3–4 plain paragraphs before something breaks the
  column — a band, pull quote, image, embed, card group, or rendered artefact. "Monotonous long
  blocks of text" and "too long, undifferentiated" are standing complaints, and they arrive
  section by section, so check the WHOLE page, not just the opening.
- End with top takeaways rendered as cards.

Structure and media conventions:
- Near the top: video embed (full-width) if there's a recording; audio player
  (`<audio controls preload="metadata">` with a `<source>` element); link to the transcript
  that opens in a popup rendered as HTML.
- Visual summary (`summary.avif` / sketchnote / comic page): prominent, max-width 100%;
  clicking opens the full-size image in a new tab.
- Full-width breakout bands with contrasting backgrounds create rhythm — and every band,
  wrap, and embed gets a bottom margin. By default let visual elements (comic page, videos,
  embedded content, galleries) expand past the main column, even to full width, each on a
  distinct background colour so it pops.
- Card groups get extra width so 3–4 cards fit per row on desktop, and the column count must not
  strand a single card alone in the last row (see generation-guide.md).
- Section jump navigation: ALWAYS include a way to jump to any section from anywhere on the page
  (a fixed prev/next bar with a "Jump to…" menu). Ship the HTML markup and JS wiring, not just the
  CSS. This is a required default, not an optional flourish. See generation-guide.md for the
  pattern and how to find the current best example.
- Tooltips: context for non-obvious terms; extra context for references.
- Popups: citations (cite the key point, link to the source) and supporting material
  (extended quotes, chat excerpts, extracts).

Link conventions:
- Every link the prompt lists MUST appear, at the right place (narrative, caption, or card).
  Also preserve/use relevant links discovered in transcripts and supporting files rather than
  silently dropping them.
- Use SHARE links only: `chatgpt.com/share/...` or `chatgpt.com/s/...`, `claude.ai/share/...` or
  `/public/artifacts/`, `gemini.google.com/share/...`. Links inside `<!-- HTML comments -->` in the
  prompt or transcript are PRIVATE — never include them.
- Honour DO NOT LINK instructions: mention the thing, omit the hyperlink.
- Images: include with a caption; image and caption link to the associated URL if any,
  else open the full-size image in a new tab.
- Website embeds: IFRAME in a full-width container, slightly under 100vh (inspect content for
  the right aspect ratio), with a caption linking to the source in a new window.
- Check embeddability BEFORE writing the iframe — many sites refuse framing via
  `X-Frame-Options`/CSP `frame-ancestors` and render blank. `curl -sI <url> | grep -i
  'x-frame-options\|content-security-policy'`, or load it and look. Known refusers include
  `claude.ai`, `chatgpt.com`, `github.com`, `agentskills.io`, most SaaS dashboards. Fallbacks, in
  order: screenshot + link card (generation-guide.md); for GitHub/raw Markdown, fetch the raw file
  and render it in a popup; plain link last. Conversely, don't assume a resource is permanently
  gated: if a source file records someone offering to publish it, flag that to the user ("this is
  private — make it public and I'll embed it?") instead of writing the restriction into the story.
- Where a talk has a primary speaker and a secondary host/organiser/co-presenter, the secondary
  party gets ONE hyperlinked mention (usually the first substantive one) and plain-text mentions
  thereafter. The same external link repeated in nav, hero, body and footer reads as promoting
  someone who isn't the subject of the story.
- Local `.md` files: open in a popup, rendered as HTML (skip or prettify YAML frontmatter).
- Local `.html` files: embed full-width at ~90vh.
- Clickable elements that lead somewhere are `<a>` tags (so right-click → open in new tab
  works), with the click intercepted for popups — not `<button>`s.
- Slides: include only relevant ones, as thumbnails/grids; clicking opens a lightbox.

### 5. Generate in chunks

Claude stalls generating large HTML in one shot. Write the file in small chunks or layered
edits (≤100KB each, practically ~200–400 lines): scaffold+head+hero first, then narrative
sections, then closing (takeaways, footer, overlays, scripts). Save and sanity-check after
each chunk; end every chunk at a complete element boundary. The sanity check includes tag
balance — run it after EVERY chunk, especially right after any edit that closes `.wrap` to
insert a full-width band and reopens it afterwards (the highest-risk pattern for a dropped or
duplicated `</div>`, which silently breaks the layout of everything below).

### 6. QA pass (do this without being asked)

1. **Quote attribution fact-check.** Transcripts frequently mislabel speakers. Re-check every
   quote and attributed statement against the transcript; flag ambiguous attributions to the
   user in your final report. This has been the #1 source of corrections. Errors cluster in
   panels and multi-speaker sessions — list the speakers first, then verify per speaker, and
   check narrative attributions too ("X's demo", "Y raises the objection", "Z's 70 students"),
   not just text inside quotation marks. One found error means more: re-verify all of them.
2. **Contrast sweep.** Check text, links, `strong`, captions, `figcaption`s and band labels
   inside every coloured band, in resting AND hover/focus states, in both dark and light
   contexts. Don't eyeball the declared colours — trace the cascade: a more specific prose rule
   elsewhere can override a component's own colour (see generation-guide.md's specificity trap).
   Low-contrast links inside bands are the #2 recurring bug.
3. **Spacing.** Bands/wraps/embeds have bottom margins; sections breathe.
4. **No horizontal scroll.** `body { overflow-x: hidden }` plus only the
   `width: 100vw; margin-left: calc(50% - 50vw)` breakout pattern.
   `grep -n 'margin.*-[0-9]*vw' <file>` must return nothing.
5. **All links present.** Grep the output for every URL the prompt required.
6. **No private links leaked.** `grep -nE 'chatgpt\.com/c/|claude\.ai/chat/|gemini\.google\.com/app' <file>`
   must return nothing.
7. **Popups/lightbox work.** Every `openPopup('X')` has a matching `id="X"`; audio uses a
   `<source>` element; no leftover TODOs.
8. **Tag balance.** Every opened tag is closed exactly once. Parse the file, or count:
   `grep -o '<div' <file> | wc -l` must equal `grep -o '</div>' <file> | wc -l` (repeat for
   `section`, `article`, `figure`). Unbalanced `div`s break every section below the mismatch.

Fix the CLASS, not the instance. Every defect above generalises: when you find — or the user
reports — one low-contrast link, one missing margin, one dead click, one wrong attribution, sweep
the whole file for others of the same kind before replying. "Fix these AND SIMILAR ERRORS" and
"find similar issues and fix them" recur in the prompts because single-instance fixes don't hold.

### 7. Update the catalog and finish

Update `config.json`, not the generated talk list in `README.md`. Find and update the existing
talk row; add one only for a genuinely new talk. Preserve the one-talk-object-per-line format.

- Talk fields: `date`, `title`, `categories`, `links`; optional `time`, `duration`, `details`,
  `event`, `location`, `speakers`, `images`. Categories are `latest`, `archive`, `videos`, `others`.
- `date`: `YYYY-MM-DD`. `time`: offset-aware ISO 8601 start time when known. `duration`: whole elapsed
  minutes for the session itself. Omit `time`/`duration` rather than guessing.
- `details`: one concise sentence with the talk's thesis/insight.
- `event`: `{name, url?}`; `location`: text; `speakers`: `[{name, url?}]`.
- `links`: `{type, url, label?, minutes?, primary?, ignore?}`. At most one `primary:true`; it
  becomes the title link. `label` overrides the default label. `minutes` is whole elapsed minutes.
  `ignore:true` marks the generated Markdown link `:ignore` for link checking; it does not hide it.
- `images`: only the one/few prominent `{type, url, label?}` images, not every slide/frame.
- Reuse an existing `type` rather than inventing one — list what's in use with
  `jaq -r '[.talks[].links[].type] + [.talks[].images[]?.type] | unique | join(" ")' config.json`.
- Top-level `youtube_playlist` is catalog metadata; change it only if the playlist changes.

Run `just build` after editing `config.json`; it regenerates the catalog in `README.md` and root
`index.html`. Do not hand-edit generated catalog entries.

Report: what was generated, quotes whose attribution you're unsure about, links you could not
resolve, anything skipped, and the `just build` result.

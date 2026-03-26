---
name: talk-story
description: Generate an engaging narrative HTML story page for a conference talk. Use when a talk directory has transcript.md and the user wants to create index.html. Handles PDF-to-slide image conversion, link screenshots, context gathering, and chunked HTML generation in Malcolm Gladwell narrative style. Invoke as /talk-story <talk-dir> or /talk-story when already in the talk directory.
allowed-tools: Read, Glob, Grep, Bash, Write, Edit, WebFetch, WebSearch
---

# Talk Story Generator

Generates `index.html` — a beautiful magazine-style narrative — for a conference talk.

## Invocation

`/talk-story $ARGUMENTS` where `$ARGUMENTS` is the talk directory path (e.g. `2026-03-12-nie-ai-roadmap`).
If omitted, use the current working directory.

---

## Workflow

### Step 1 — Find the talk directory

Resolve the talk directory:
- If `$ARGUMENTS` is given, treat it as relative to the talks root. Confirm it exists.
- Otherwise use the current working directory.

Verify `transcript.md` exists in that directory. If not, stop and tell the user.

### Step 2 — Inventory assets

Run `ls -la <talk-dir>/` and note which assets are present. Categorise them:

| Asset | Variable | Notes |
|---|---|---|
| `transcript.md` | REQUIRED | Primary content |
| `context.md` | REQUIRED | Event/speaker metadata — see Step 4 |
| `sketchnote.avif` / `sketchnote.webp` | optional | Visual summary |
| `audio.opus` | optional | Recording (only .opus is used) |
| `slide-NN.avif` / `slide-NN.webp` | optional | Extracted slide images |
| `*.pdf` | optional | Slide deck — convert if no slide images |
| `*.avif` / `*.webp` / `*.webm` / `*.mp4` | optional | Images/videos referenced in talk |
| Supporting `*.md` (ideas.md, preparation.md, etc.) | optional | Additional context |

### Step 3 — Convert PDF to images (if needed)

If a `*.pdf` exists **and** no `slide-*.avif` / `slide-*.webp` files exist, run:

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/pdf-to-images.sh <pdf-path> <talk-dir>
```

This creates `slide-01.avif`, `slide-02.avif`, etc. in the talk directory.
If the script reports missing tools, tell the user what to install.

### Step 4 — Check for context.md

**If `context.md` does NOT exist:**

1. Read `transcript.md` and infer as much as possible (speaker names, event name, date).
2. Copy `${CLAUDE_SKILL_DIR}/context-template.md` to `<talk-dir>/context.md`.
3. Fill in every field you can infer; mark genuinely unknown fields with `TODO:`.
4. Output a clear message listing the `TODO:` fields the user must supply.
5. **STOP** — do not generate HTML. Tell the user to fill in `context.md` and re-run `/talk-story`.

**If `context.md` exists**, proceed.

### Step 5 — Screenshot key links (if needed)

If `context.md` contains a `## Screenshots` section listing URLs, screenshot each one using `uvx rodney`:

```bash
uvx rodney start
uvx rodney open "<url>"
uvx rodney screenshot -w 1280 -h 800 "<talk-dir>/screenshot-<slug>.png"
uvx rodney stop
```

Then convert to WebP if `cwebp` is available: `cwebp -q 80 screenshot-<slug>.png -o screenshot-<slug>.webp && rm screenshot-<slug>.png`

Only screenshot when the output file doesn't already exist. Start rodney once per batch, not once per URL.

### Step 6 — Read all context

Read these files in order (all that exist):
1. `<talk-dir>/context.md`
2. `<talk-dir>/transcript.md`
3. Any supporting `.md` files listed in `context.md` under `## Supporting files`
4. Example reference HTML files listed in `context.md` under `## Example talks` (or defaults below)

**Default example talks** (read only the first 200 lines of each for style reference):
- `2026-02-11-amat-dt-day/index.html`
- `2025-12-06-mining-digital-exhaust/index.html`

### Step 7 — Generate HTML in chunks

See [generation-guide.md](generation-guide.md) for complete design patterns and HTML structure.

**Generate in exactly these 4 chunks** to avoid truncation. Write/Edit the file after each:

1. **Scaffold**: `<!DOCTYPE html>` … `</head>` + `<body>` opening + masthead + hero section. Write to `<talk-dir>/index.html`.
2. **Narrative part 1**: Opening section through roughly the midpoint of the talk. Edit/append.
3. **Narrative part 2**: Remainder of narrative + slide gallery (if slides exist) + media embeds. Edit/append.
4. **Closing**: Top takeaways section + footer + all `<script>` blocks + `</body></html>`. Edit/append.

After each chunk, verify the file is valid (no truncated tags, matching open/close).

**After all chunks**, do a final review pass:
- No horizontal scrollbar: grep for `margin.*-[0-9]*vw` or `margin.*-100` — these always cause overflow. The only safe full-width pattern is `margin-left: calc(50% - 50vw)` with `body { overflow-x: hidden }`.
- Audio player present if `audio.opus` exists
- Sketchnote is full-width with contrasting background
- Slide thumbnails open in popup lightbox
- All `TODO:` placeholders removed
- README.md updated with this talk

### Step 8 — Update README.md

Add the talk to the main `README.md` in the same format as existing entries.

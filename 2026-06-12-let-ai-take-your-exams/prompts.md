# Prompts

## Techniques, 08 Jun 2026

<!--
cd /home/sanand/code/talks/2026-06-12-let-ai-take-your-exams/
dev.sh -p ~/code/
claude --dangerously-skip-permissions --model claude-opus --effort medium
-->

Modify `techniques.html` - which was designed for a different `techniques.jsonl` format - to work with the current `techniques.jsonl`. Specifically:

- There is no `n`. Either add it to `techniques.jsonl` or modify the code to work without it.
- Use "category" instead of "stage". setting" is an additional tag.
- Use "steps" instead of "move".
- "provenance" and "try_it" are unused. "learn_instead" is used.
- etc.

Read `claude-chat.md` to understand the context and how `techniques.jsonl` was generated.

Modify the title and any other framing appropriate to the context - but the rest of the _functionality_ in `techniques.html` (no label-overlap, tour, hover tooltip, brush, popup on click, URL state, light/dark mode, ...) should be preserved and adapted to the new format.

Ensure that the points are spread out. The values are subjective - you can edit the impact and ease values to make them distinguishable, as long as you are convinced that the relative ordering is correct.

Go through the content in "techniques.jsonl". Will a layman understand it, standalone? For example, "A constrained format that travels on social and survives print" isn't as clear as "A fixed format can be repeatedly used on print and social media as a recurring series". Revise the tagline, move, why, try_it, watch_for and examples.context in `techniques.jsonl` where required to make it simple and clear for a layman.

---

Rewrite `techniques.jsonl` to remove & avoid LLM smells.

- Write plainly. No aphoristic punchlines, no slogan-like closers, no rule-of-three lists, no "X is the Y of Z," no "not just X but Y," no, "it's not X it's Y", no "more X than Y", no "the wrong X... the right one is Y", no "honest/genuine X", no "X matters", no excessive bullets, no em-dash or unicode.
- Vary sentence length: don't stack short ones for effect.
- Use my wording and examples where possible.

Find more examples of these 30 techniques as you can from ~/code/exam/ or ~/code/blog/ (or ~/Documents/notes/transcripts/ or ~/Documents/claude/).
Include them only if they're apt and absolutely spot-on as an exemplar for that technique - and make sure that comes through when you write the "context" for each example.

---

In the "Solve - Study - Verify" legend row, also add filters for "Open book OK", "Endorsed" and "Demo only".
Drop the "Delegate to AI, then keep what AI can't do:".

---

Where you are linking to an exam/q*.js, instead, find the exam that uses it and link to that. For example, `q-axis-scale-manipulation-repair.js` is used in ~/code/exam/src/exam-tds-2026-01-ga7.js - so you can link to <https://exam.sanand.workers.dev/tds-2026-01-ga7#q-axis-scale-manipulation-repair>.

<!-- claude --resume 27e30390-48d5-47d5-9aaf-dddabed9a94f --dangerously-skip-permissions -->

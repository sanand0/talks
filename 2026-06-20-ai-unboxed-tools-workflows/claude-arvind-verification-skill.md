---
title: "Automated answer verification skillShared by godzillamanning"
date: 2026-06-21T11:20:22+08:00
source: "https://claude.ai/share/5120479c-c715-407c-88d0-eb0a6738aae6"
---

## User

Create a Claude skill for verifying answers which runs after every workflow.

---

## Claude

<details>
<summary>Viewed 2 files</summary>

> Read the skill-creator conventions. Now building the verification skill, tuned to your epistemic standards (no invented numbers, re-derive decision-critical figures, flag confidence, kill filler).

</details>

<details>
<summary>Created a file, read a file</summary>

> Creating the answer-verification skill folder + SKILL.md
>
> SKILL.md
>
> Presented file
>
> Done

</details>

Done. Folder `answer-verification/` with `SKILL.md`.

**What it does**

- Five-check audit run on the draft _before_ delivery: (1) question-fit, (2) numbers, (3) facts/recency, (4) logic, (5) confidence.
- Scaled by stakes — trivial replies skip it, single facts get numbers+recency, anything decision-relevant gets the full pass. Keeps it from becoming bureaucratic overhead.
- Tuned to your standards: re-derive decision-critical numbers _independently_ (not re-check the same arithmetic), classify every figure as derived / sourced / from-memory-and-dangerous, force stale recency-sensitive numbers to a live search, name the load-bearing assumption, and gate confidence to evidence strength.
- Output discipline matches your prefs: fix silently → deliver answer-first → footer **only when residual risk remains**. No "✓ all passed" stamp — that's filler.

**The one honest gap — read this**

- You asked for it to run "after _every_ workflow." Skill triggering is **request-driven, not turn-driven**: a skill fires when the model judges the _incoming task_ would benefit from it. I wrote the description deliberately pushy so it fires on essentially anything analytical/quantitative/decision-relevant — but it will _not_ reliably fire on every trivial turn, and arguably shouldn't (auditing "what's the SGD ticker" is noise).
- If you want a hard guarantee it runs on literally every substantive turn regardless of the model's judgment, the reliable lever is a **line in your user preferences** pointing at it, treated as a standing instruction — not skill triggering alone. Confidence: high on this; it's how the mechanism works, not a guess.

**Next**

- Want me to draft that preferences line so it actually fires every time?
- Or run it live against 2–3 of your real cases (a mock trade thesis, a sizing calc, a regime-parallel) to see what it catches and tighten from there?

---

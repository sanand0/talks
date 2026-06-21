---
title: "Claude skill for answer verification- Shared by Bikram"
date: 2026-06-21T11:18:29+08:00
source: "https://claude.ai/share/eb99f0c5-b9d8-4668-908f-046d16d689d1"
---

## User

Create a Claude skill for verifying answers which runs after every workflow

---

## Claude

<details>
<summary>Viewed 3 files</summary>

> Quick note before I build it: a skill can't literally auto-run after every task — skills get consulted when Claude decides their description matches what it's doing. But I can write the description to be "pushy" enough that Claude pulls it up before finalizing any non-trivial answer, which gets you the same effect. The body would then walk Claude through a verification pass.
>
> Two quick things to scope it well:

</details>

---

## User

Q: What should the verification focus on most? (Select all that apply) A: Numbers & calculations

Q: How heavy should the check be? A: Quick sanity-check

---

## Claude

<details>
<summary>Ran a command, created a file</summary>

> Create the skill directory
>
> Script
>
> Writing the SKILL.md for a quick numerical verification pass
>
> SKILL.md
>
> Done

</details>

<details>
<summary>Ran 4 commands, read a file</summary>

> Packaging the skill into an installable .skill file
>
> Script
>
> Check packaging script options for output path
>
> Script
>
> Inspect packaging script to find where it writes output
>
> Script
>
> Package the skill into the outputs directory
>
> Script
>
> Presented 2 files
>
> Done

</details>

Focused on numbers, quick sanity-check — that fits well. Let me build it.

Let me package it so you can install it.

Here's your **`numerical-sanity-check`** skill, packaged and ready to install (download the `.skill` file and add it via Settings → Capabilities → Skills).

How it works: the description is written to be "pushy," so Claude pulls the skill up as a final pass whenever it's about to hand you a figure — a total, a percentage, an IRR or margin, a reconciliation, a spreadsheet output — even when you didn't ask it to double-check. That's the closest thing to "runs after every workflow," since skills are consulted by description-match rather than auto-fired.

The body keeps it a _quick_ check rather than a full re-derivation, ordered by value-per-second: ballpark/magnitude, sign, units-and-type (the decimal-vs-percent and monthly-vs-annual traps), whether the right inputs/columns were actually used, a re-check of just the load-bearing step, and reasonableness bounds. It also tells Claude to keep the visible output light — no note on a trivial total, one short line on a substantive result, and a clear concrete callout when it actually catches and fixes something.

A quick illustration of it in action on the kind of error it's built for: a draft answer of "monthly return: 850%" trips the magnitude and units checks → trace it → 0.085 got multiplied by 100 twice → corrected to 8.5%, surfaced as a one-line note. That catch is the whole point of the skill.

Two things worth knowing. It's scoped to numbers, as you chose — it won't vet citations or code logic. And if you ever want it heavier (an independent re-derivation rather than a sanity-check), that's a one-line change to the rigor; say the word and I'll make a "thorough" variant.

---

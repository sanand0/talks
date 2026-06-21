---
title: "Automated answer verification skill"
date: 2026-06-21T10:58:33+08:00
source: "https://claude.ai/chat/b9b521b3-5ea8-417b-85ff-1ce4a7cfbdf2"
---

## User

Create a Claude skill for verifying answers which runs after every workflow.

---

## Claude

<details>
<summary>Distinguishing complementary verification approaches and architectural placement</summary>

> I'm parsing what Anand is looking for—a verification skill that integrates into his workflow system, likely leveraging his existing Verifiable Autonomy framework and the skill library he's already built out. He seems to be thinking about how to systematize answer validation across his tools. I need to understand what actually works empirically for verification—naive "check your work" prompts often backfire because models rationalize their original answers or "correct" correct answers to wrong ones. The real research shows verification works best when grounded in independent external signals like running code or recomputing, not just self-reflection. This is the foundation I need for a skill that actually improves output quality.
>
> The skill should probably work as a modifier that triggers after substantial tasks, lightweight enough not to be intrusive but rigorous when it matters. The core mechanism is replacing self-assessment with independent re-derivation—having the model actually re-check claims against external evidence rather than just re-reading and feeling confident about the work. ally answer what was asked? Did I drop any constraints? This is crucial and often overlooked. The verification skill should explicitly check whether I addressed what was actually requested, which directly counters the tendency to jump to a preferred solution before understanding the real need. Then I need to calibrate the report honestly — state my confidence level, flag what I'm still uncertain about, and avoid claiming I've verified something I haven't actually checked. The key design principle is avoiding fake verification where I just go through the motions. Since self-correction without external validation is unreliable, the skill needs to push hard toward actually executing checks — running code, recomputing numbers — rather than just reasoning about whether something seems right.
>
> Verification should also be proportional and know when to stop. Not every task requires deep verification, and I shouldn't loop endlessly. I also need to guard against the failure mode where verification "corrects" a correct answer into a wrong one — any proposed change should be justified by a concrete, identified error, not a vague sense that something could be better. I'm thinking about the format now and planning to create this as a SKILL.md file that can be added to the skill library. I'm weighing whether to present the SKILL.md file as a downloadable artifact or inline in the chat. Since he prefers markdown in chat and will likely want to review and edit it, I think showing the content directly makes the most sense — though the file itself is substantial, so I'll need to be thoughtful about how much to display at once. I need to review his existing skills to match the format and voice conventions, especially expert-lens since it's the closest parallel to what I'm building. Let me examine that one carefully along with a couple others to understand the structure and tone I should adopt. I'll read expert-lens and skill-creator to nail the format and triggering mechanism, then maybe spot-check another skill for consistency. The key is avoiding duplication with expert-lens while getting the description right for a skill that runs after every workflow. Let me start with those two reads and see if any hidden complexity surfaces.
>
> Done

</details>

<details>
<summary>Calibrating description clarity and triggering mechanisms</summary>

> Read the expert-lens skill to avoid duplication and match style
>
> Expert-lens handles upfront analysis with verification built in as one step, while this new skill functions as a downstream verification gate that can operate after any workflow and dig deeper into verification specifics—like failure-mode taxonomy, independent re-derivation discipline, stopping criteria, and calibrated reporting.
>
> I'm studying the style conventions of these skills: YAML frontmatter with name and description (where the description acts as the trigger, phrased as "Use this for X. Skip it for Y"), terse numbered imperatives, a "Hard rules" section, "Prefer X over Y" formulations, and aggressive compression that cuts anything unproductive. I want to echo key phrases like "Prefer external checks over self-critique," "run code/tests, look up sources," "fact-check like an untrusted solution," and "Prefer a deterministic check over judgment" so the verification skill feels aligned with the existing philosophy. Now I'm checking the skill-creator documentation for triggering best practices and frontmatter requirements.
>
> Done

</details>

<details>
<summary>Crafting inline content with workflow verification caveats</summary>

> Read skill-creator for frontmatter and triggering best practices
>
> I'm working through how to write the description so it clearly signals both what the skill does and when to use it—making sure Claude actually triggers it even though it tends to be conservative about consulting skills. The tricky part is balancing that with the need to avoid firing after simple tasks, so the description has to distinguish between substantial work and trivial one-liners.
>
> I'm also grounding this in the research on LLM self-correction. The key finding is that self-correction without external signals is unreliable—models can't tell which answers are actually wrong, so they sometimes "fix" correct ones. This means any verification needs to anchor to something concrete like execution results or independent recomputation, not just the model's own judgment. There's also a verification-generation gap where checking an answer is often easier than producing it from scratch.
>
> The real power comes from independent re-derivation rather than re-reading the same reasoning path, and breaking claims into atomic sub-claims that can each be checked separately. Asking targeted questions about known failure modes works better than generic review.
>
> Models tend to be overconfident, so verification should recalibrate claims to what's actually supported and flag uncertainty. A major class of errors isn't factual wrongness but answering a different question than asked or dropping stated constraints. Verification also needs a stopping rule — over-verifying trivial things creates its own failure mode.
>
> The skill itself functions as a modifier or gate. After a workflow produces output, it runs a verification pass and reports calibrated confidence before presenting results. I'm considering names like `verify`, `verification-gate`, or `answer-check` — his existing skills use short kebab-case names, so `verify` is clean, but `verification-gate` better conveys that it's a checkpoint you pass before shipping. I think `verify` works best given the pattern. Two-word kebab naming fits his convention best, so I'm settling on `verification-gate` — it captures both the checkpoint nature and the "runs after workflows" requirement. The folder structure would be `verification-gate/SKILL.md`. I'm settling on `verification-gate` as the final name since it clearly signals the post-workflow checkpoint role and won't get confused with a generic verb. Now I need to structure the content following Anand's style—terse, numbered, imperative with a "Hard rules" section and "Prefer X over Y" comparisons. The core philosophy is to re-derive and validate against external signals rather than just re-reading, since self-rationalization defeats the purpose, and I should only flag changes when I can articulate a concrete reason.
>
> The procedure starts by scoping whether verification is even worth the effort, then reconstructs the original spec to catch invisible failures like answering the wrong question or dropping constraints. Next I decompose the output into atomic, checkable units—each fact, code path, or logical step tagged as either verifiable against ground truth or a judgment call. Then I need to pull in independent signals to validate against.
>
> For verifiable claims, I actually execute and test code rather than just re-reading it, refetch sources to confirm citations match what's claimed, recompute numbers a different way, and verify that names and APIs actually exist and are spelled correctly. The key is using a genuinely different route to ground truth—just re-reading and feeling confident doesn't count.
>
> I also systematically hunt for common LLM failure modes: overclaiming beyond evidence, silently dropping constraints, fabricating citations, off-by-one errors, stale facts, reversed causality, plausible-but-wrong specifics, internal contradictions, and ignored ambiguities. For judgment calls that can't be fully verified, I stress-test them by considering the strongest counterargument and what would have to be true for them to hold. Then I only fix the specific defects I've actually identified, rather than revising broadly.
>
> When reporting, I'm explicit about what I checked and how — whether I executed something, sourced it, or recomputed it — and I calibrate confidence to the weakest load-bearing unit, not the average. I avoid claiming verification for things I've only re-read, and I make sure to re-verify any changes I make, since revision itself introduces new error risk.
>
> The key insight is that a clean pass with nothing wrong found is itself valuable information — I should report that plainly rather than manufacturing problems to appear thorough. Verification isn't about finding flaws; it's about honest assessment of what I've actually checked and what remains uncertain. The trigger should fire after any substantive output—analysis, code, plans, deliverables—as a final verification step, but skip trivial tasks like arithmetic to keep it sane. I'll phrase it as "by default, after producing any substantive answer" to match his intent while being practical. For delivery, I'll write the file to the working directory since the skills library is read-only in this context. SKILL.md file itself. I'll create the file in the verification-gate folder and present it, then explain the key design choices in chat—particularly the core idea of re-deriving rather than re-reading and only fixing named defects, and how that complements the expert-lens approach.
>
> Given his preference for direct Markdown answers, I'll show the SKILL.md content inline in a fenced block so he can read it immediately, then create the file for download as the usable artifact. I should offer a brief, one-line option to test and iterate on the skill if he wants, since that's genuinely new scope beyond the creation he asked for. Now I'll write out the skill file itself, keeping his house style — terse, numbered, imperative, with hard rules and clear preferences, no padding. I need to identify the load-bearing claims that the conclusion depends on and verify those specifically, rather than checking everything equally. Then I'm reconstructing the original spec to make sure I'm actually answering what was asked before validating the answer itself, and finally breaking the output into atomic, checkable units—each fact, code path, and logical step—so I can tag what has ground truth versus what's a judgment call.
>
> For anything verifiable, I'm getting independent confirmation by re-deriving or re-running it rather than just re-reading; that means executing code to confirm outputs, refetching sources to verify citations actually say what I claim, recomputing numbers a different way, and checking that APIs and functions exist as written. If I can only re-read and feel confident, that's still unverified—I mark it as such instead of treating it as confirmed.
>
> Now I'm actively hunting for specific failure modes rather than just asking if something looks right: overclaiming beyond what the evidence supports, outdated facts that changed after my training cutoff, off-by-one errors or unhandled edge cases, reversed causality, plausible-sounding specifics that are actually wrong, internal contradictions, and ambiguities I've silently resolved in my favor. For judgment calls I can't prove, I stress-test them by finding the strongest counterargument, considering what would have to be true for them to hold, and looking for disconfirming cases—anything that doesn't survive that scrutiny gets downranked. Once I've identified specific defects, I fix them and then re-verify.
>
> When reporting, I'm careful to state exactly what I checked and how—whether I executed something, sourced it, recomputed it, or reasoned through it—what held up, and what remains uncertain. My confidence is only as strong as the weakest part of the argument, not the average. I never claim something is verified if I only re-read it; I need a second route or ground truth. And I only change things where I can point to a concrete defect with evidence. independence emphasized, failure-mode hunting over generic review, spec reconstruction as the highest-yield first step, weakest-link confidence calibration, and a proportional stopping rule that avoids looping or manufacturing problems. This verification gate complements the expert-lens approach by running after any workflow as a dedicated back-end check, with minimal overlap since the expert-lens is front-loaded analysis while this catches issues across all output types.
>
> Now checking the style against his preferences: terse, numbered, imperative voice, "Hard rules:" framing, "Prefer X over Y" comparisons, minimal bold, no examples—all matching. The length is around 55 lines, which fits his range. The triggering description is appropriately pushy without firing constantly, scoped to skip trivial cases, and lists the workflow types it applies to. I think adding "By default" at the start would signal this is the standard final step and strengthen the framing.
>
> Now I'm creating the SKILL.md file in the outputs folder. I have enough context from the expert-lens and skill-creator conventions to proceed without reading additional skills—more would be diminishing returns. I'm clarifying what "runs after every workflow" means in the SKILL.md paradigm—whether it's a literal mechanical hook or a convention about when the skill should be invoked.
>
> Done

</details>

<details>
<summary>Decided to present content inline with verification caveat and testing offer</summary>

> Create the verification-gate SKILL.md, grounded in self-correction research
>
> SKILL.md
>
> Presented file
>
> I'll show the content inline so he can read it directly in the chat, then mention the key caveat that this runs after every workflow, and offer to test or iterate on it.
>
> Done

</details>

I'll design this carefully — naive "check your work" verification is known to *hurt* output quality (models rationalize their original answer or "correct" right answers to wrong ones), so the skill has to be grounded in what actually works. Let me first read your closest existing skill to avoid overlap and match conventions, plus the skill-creator guidance on triggering.

Good — expert-lens already has a "verify as a fresh reviewer" step, so the new skill must *complement* it (a back-end gate) rather than duplicate it, and extend the same "external checks over self-critique" philosophy. Let me check the skill-creator guidance for description/triggering conventions.

I have what I need. Here's the design rationale, then the skill.

**The core problem this has to avoid:** the empirical literature is clear that naive self-verification *doesn't work* and often backfires. When a model re-reads its own output and judges it, it tends to rationalize the original answer; when it "corrects," it flips right answers to wrong ones about as often as the reverse (Huang et al., *LLMs Cannot Self-Correct Reasoning Yet*). What actually works is (a) **re-deriving** by an independent route or checking against ground truth rather than re-reading (the mechanism behind self-consistency and chain-of-verification), (b) **decomposing** into atomic checkable units, (c) **hunting specific failure modes** instead of asking "is this good?", and (d) **only changing what you can name a defect for**. The skill is built entirely around those four, and it deliberately extends `expert-lens`'s "external checks over self-critique" rather than restating it — `expert-lens` front-loads analysis with verify as one step; this is the dedicated back-end gate that goes deep and fires after *any* workflow (including code/deliverables, not just analysis).

markdown


```
---
name: verification-gate
description: "Run this by default as the final step after any non-trivial workflow — analysis, code, data work, a plan, a factual answer, a deliverable — before presenting it, even when not explicitly asked to verify. Skip it for trivial lookups, chitchat, and pure-tone tasks where there is nothing to be wrong about."
---

Verification is not re-reading your work and feeling confident — that mostly re-confirms the original answer and, when it "corrects," turns right answers wrong about as often as the reverse. Verification is getting an *independent signal* and changing only what you can name a defect for.

0. Scope the pass.
   Trivial or unfalsifiable → skip, say nothing. Otherwise scale depth to stakes × irreversibility. Identify the *load-bearing* units — the few claims the conclusion actually rests on — and spend the budget there, not on the easy ones.

1. Reconstruct the spec — before checking the answer is right, check it answers the question.
   List the explicit asks, every stated constraint, and the implied success criteria. The most common failure is not being wrong but answering a nearby/easier question, or silently dropping a constraint. Flag any ask unmet or constraint dropped.

2. Decompose into checkable units.
   Split the output into atomic pieces: each number, factual claim, citation, code path, named entity (API / function / field / person), and load-bearing logical step. Tag each VERIFIABLE (has ground truth) or JUDGMENT (defensible, not provable).

3. Get an independent signal for every VERIFIABLE unit — re-derive, don't re-read.
   - Code / data: run it. Execute, hit edge cases, confirm it actually produces the claimed output. Recompute key numbers a *second* way.
   - Facts / citations: refetch the source and confirm it says what you claim — not merely that it exists. Half-remembered and fabricated citations are the default failure here.
   - Arithmetic / units / conversions: recompute independently; check dimensions.
   - Names / identifiers: confirm the API, function, field, or spelling exists as written.
   A second *different* route, or ground truth, counts. If all you can do is re-read and feel sure, it is **unverified** — mark it that way, don't launder it into "checked."

4. Hunt the known failure modes — don't ask "is this good?", try to find specific defects.
   Actively look for an instance of each: overclaiming past the evidence; stale fact (changed since cutoff); off-by-one or unhandled edge case; reversed causality or direction; plausible-but-wrong specific (exact figure, date, name); internal contradiction; an ambiguity you resolved silently in your own favor.

5. Stress-test JUDGMENT units.
   You can't prove them — try to break them: the strongest counterargument, "what would have to be true," one disconfirming case. Down-rank anything that doesn't survive.

6. Fix only identified defects — then re-verify the fix.
   Revise only where steps 1–5 named a concrete defect with evidence. Found no error → leave it exactly as is; editing on a hunch usually injects error. Every changed unit is a new unit — run it back through step 3.

7. Report calibrated.
   State what you checked and how (executed / sourced / recomputed vs. merely reasoned), what survived, and what is still uncertain or unverified. Confidence tracks the *weakest load-bearing unit*, not the average. A clean pass is a real result — say "checked X, Y, Z; holds" plainly. Never report "verified" for anything you only re-read.

Hard rules:

- Re-derive, don't re-read. A second route or ground truth, or it stays unverified.
- Change only what you can name a defect for. Found no error → change nothing.
- Verify the load-bearing units; confidence = weakest link, not the average.
- Did it answer the question and keep every constraint? Check that before correctness.
- Prefer execution / source / recompute over "this looks right."
- "Unverified" is an honest, valid output. Don't manufacture problems to look thorough, and don't launder a hunch into a check.
- Proportional and bounded: stop once the load-bearing units are checked. Don't loop.
```

One mechanism caveat worth flagging, since "runs after every workflow" is the explicit goal: a SKILL.md can't *force* itself to run — triggering is description-driven, and Claude under-triggers skills it thinks it can skip. The description is written pushy to compensate, but if you want hard enforcement of a post-workflow gate, the reliable lever is a one-line pointer in an always-on instruction (Claude Code's `CLAUDE.md`, a project instruction, or a stop/post-tool hook) that says "before presenting any non-trivial result, run `verification-gate`." The skill supplies the *method*; the always-on line supplies the *guarantee*.

Want me to run it against a few test cases (one code task, one factual-claim task, one strategy task) so you can see whether it actually catches planted errors versus rubber-stamping — that's the failure mode that matters most here.

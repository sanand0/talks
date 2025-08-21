---
marp: true
title: AI Coding Guide
author: Anand S
url: https://sanand0.github.io/talks/2025-08-21-ai-coding-guide/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
---

# AI Coding Guide

[DataHack Summit](https://www.analyticsvidhya.com/datahacksummit/) · 21 Aug 2025 · [Bangalore](https://maps.app.goo.gl/fBAcQ6VopycH8z9T8)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Slides](https://sanand0.github.io/talks/2025-08-21-ai-coding-guide/) · [Transcript](https://github.com/sanand0/talks/blob/main/2025-08-21-ai-coding-guide/transcript.md)

![h:200px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-08-21-ai-coding-guide/)

---

## Jagged edge. **Don’t promise**. Parallel-prototype, _then_ share outcomes

**Why:** AI capability is _uneven and unpredictable_ across tasks (“the jagged frontier”).

Don't commit to your manager/client. Build it. **Then** share it.
**Fixing is 10X effort**.

Or, commit to _broad_ improvement, not specific apps.

**Do next:** run _k_ variants, _then_ talk.

---

## Specs/tests _are_ the product. Code is a build artifact

**Why:** AI makes typing cheap; the bottleneck becomes unambiguous intent. Structured instructions, diffs, and schemas consistently reduce error and review time.

**Do next (CLI-first):** keep `PROMPTS.md`/`SPEC.md`; use schema-constrained outputs (JSON Schema/Typed objects), and PR diffs only.

---

## **Optimize the validation loop, not the coding loop**

**Why:** Copilot-style tools boost raw speed (55% faster on a benchmark task), shifting value to verification. Evals/property tests and "fail-first" tests pay compounding returns.

**Do next:** add property tests (Hypothesis/fast-check), hidden tests, metamorphic checks; gate merges on evals.

---

## **Make repos "LLM-ergonomic"**

**Why:** Models perform better with consistent structure, fast tests, and machine-readable context (e.g., repo "manuals" for LLMs).

**Do next:** add `llms.txt` (or Context7), keep small files, consistent names, fast lint/test targets; ship sample I/O fixtures.

---

## **Adopt "diff-native" workflows**

**Why:** Modern coding models are trained to propose/apply file diffs; diff-first workflows reduce accidental edits and review effort.

**Do next:** require patch hunks in PRs; auto-reject whole-file rewrites; prefer editors/agents that apply diffs deterministically.

---

## **Prefer typed interfaces & DSLs over prose**

**Why:** Structured outputs (schemas/grammars) and typed APIs minimize ambiguity and regression surface; typed stacks (TS/Rust/Go or Python+typing/Pydantic) tend to vibe-code more reliably.

**Do next:** define JSON Schemas/OpenAPI for tasks, emit DSLs (SQL, GraphQL, Vega-Lite) instead of free-form code where possible.

---

## **Re-design process around _short feedback loops_**

**Why:** With AI in the loop, the classic "tighten the loop" wisdom matters more-fast, frequent checks beat elaborate prompts.

**Do next:** pre-commit hooks to run `lint && test && typecheck`; CI must be <2 minutes; default to many small PRs.

---

## **Build evals-in-the-loop; let models compete**

**Why:** Evolutionary/iterative systems that mutate code and auto-evaluate consistently outperform single-shot prompting.

**Do next:** spin N variants per change; auto-benchmark; keep a league table; merge winners only.

---

## **Instrument the AI itself (observability/usage/cost)**

**Why:** You can't improve what you don't measure-usage, drift, regressions, and spend must be visible like any service.

**Do next:** log prompts/traces, attach test results to PRs, track latency/cost per task, alert on eval regressions.

---

## **Adopt defensive UX and "ask-to-ask" patterns**

**Why:** Mature human-AI guidelines reduce silent failure and overreach; agentic systems need clear opt-outs and confirmations.

**Do next:** design prompts/agents with explicit "don't know" paths, confirmations for risky ops, and post-action summaries.

---

## **Expect uneven gains: seniors benefit differently than novices**

**Why:** Experienced devs get sizable productivity boosts, but novices can develop an _illusion of competence_ without robust verification. Plan training, not just tooling.

**Do next:** teach code review and failure-mode literacy; require short "how I verified" notes in PRs.

---

## **Plan for non-determinism and drift**

**Why:** Agents/models change; determinism degrades over time if you don't pin specs, tools, and checks. Cursor's own guidance emphasizes tight build/test gates.

**Do next:** pin model versions where possible; snapshot prompts/specs; baseline tests; run periodic re-evals.

---

## **Small, typed, tool-rich teams will out-ship bigger ones**

**Why:** Market trend: tiny, principled teams can now reach millions; the leverage is in tooling/process, not headcount.

**Do next:** invest in infra (fast CI, evals, repo ergonomics), not seats; cultivate "QC + ops + evals" as first-class roles.

---

# Concrete practices to operationalize this

- **Repository scaffolding:** `PROMPTS.md`, `SPEC.md`, `llms.txt`, `CONTRIBUTING.md` (with diff rules), `Makefile/justfile` targets: `lint`, `typecheck`, `test`, `eval`.
- **Pipelines:** pre-commit `ruff/black/pyright` (or `eslint/biome/tsc`), unit+property tests, scenario evals, and **mandatory** PR diffs.
- **Agent settings:** require confirm-before-dangerous-ops; parallelize safe tasks; log traces; budget limits; nightly re-evals.
- **Stack bias:** typed where possible; push tasks into DSLs (SQL/Vega-Lite/OpenAPI) instead of free text.

---

## Avoid path-dependence

- Don't over-index on one editor/agent; **measure** your stack (METR-style tasks) quarterly.
- Avoid "prompt maximalism": prefer **shorter, schema-bound prompts + evals** over mega-prompts.
- Docs for humans might shrink, but **docs for models** (schemas/examples/fixtures) must grow.

---

# AI Coding Guide

[DataHack Summit](https://www.analyticsvidhya.com/datahacksummit/) · 21 Aug 2025 · [Bangalore](https://maps.app.goo.gl/fBAcQ6VopycH8z9T8)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Slides](https://sanand0.github.io/talks/2025-08-21-ai-coding-guide/) · [Transcript](https://github.com/sanand0/talks/blob/main/2025-08-21-ai-coding-guide/transcript.md)

![h:200px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-08-21-ai-coding-guide/)

<!--

https://chatgpt.com/c/68a6b799-a9d4-8321-85ea-9899be41e7af

-->

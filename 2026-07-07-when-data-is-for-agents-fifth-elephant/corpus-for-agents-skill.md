---
name: corpus-for-agents
description: Convert a corpus meant for humans (folders, exports, docs, data files) into one meant for AI agents. Use whenever the user wants to make data "agent-ready", organize files for an agent, set up data for RAG or retrieval, or asks how an agent should access a dataset — even if they don't say "corpus". Measures first; sometimes the right answer is to change nothing.
---

# Corpus for Agents

Turn a human-oriented corpus into an agent-oriented one — but only where
measurement says it will help. This skill is a decision rule, not a
uniform transform. Every rule below traces to a 13-run benchmark
(see Evidence at the end). Do not add advice from general knowledge.

## Step 1: Measure before touching anything

1. **Corpus size in tokens.** Estimate as total text bytes / 4.
2. **Target model and its context window W.** Which model will actually
   read this data? What is its capability tier (frontier / mid / small)?
3. **Task mix.** Will queries be single-fact lookups, or aggregation and
   multi-hop questions (sums, joins, "latest value as of date")?
4. **Versioning.** Does the corpus contain updates, amendments, or
   conflicting dated records?

Report these four numbers to the user before acting.

## Step 2: Decide

| Situation | Action |
|---|---|
| Corpus < ~0.5×W AND tasks are mostly lookups | **Do nothing.** Plain grep-able files are already just-in-time access. An index here is pure overhead (measured: 0.4–0.9× WORSE on tokens). |
| Corpus > ~0.5×W, or growing, or tasks are aggregation/multi-hop | **Never preload. Build a catalog** (Step 3). Measured savings: 2.4×–27.6× input tokens at equal accuracy, growing with corpus size. |
| Target model is small or weak at tool use | **Don't build a catalog.** Weak models fail to drive the fetch loop: measured accuracy loss on gpt-4o-mini class, total collapse plus HIGHER cost on a 24B model. Prefer fewer, larger, pre-filtered files instead. |
| Corpus has versions/amendments and you plan to shard | **Shard only with freshness metadata** (Step 4). Sharding without it caused wrong answers (p=0.03). |

The single strongest rule, valid in every confirmed run: **never
concatenate the corpus into the agent's prompt.** The catastrophic case
is preloading, not bad folder structure.

## Step 3: Build the catalog (only when Step 2 says so)

Create one compact `CATALOG.md` at the corpus root:
- One line per file or shard: path, one-sentence description, record
  count, date range covered.
- Keep the whole catalog small enough to sit in a prompt (~1–3k tokens).
- Do not copy content into it. Paths and metadata only.
- The agent's entry prompt should carry the catalog, not the corpus;
  content is fetched on demand with read/grep.

Run `scripts/make_catalog.py <corpus_dir>` for the deterministic parts
(file listing, counts, date ranges); write the one-line descriptions
yourself.

## Step 4: Sharding rule

If you split data into per-entity or per-topic shards, every shard that
contains dated or versioned values must state, in the shard itself,
how to pick the current one (e.g. "latest effective_date wins; ties
broken by recorded_on"). Without this, agents pick stale values —
this was the one statistically significant harm we measured.

## Known failure modes (from run traces)

- Agent given a truncated preload thrashes through tools hunting the
  missing tail — worst of both worlds (27.6× cost at 2×W corpus).
- Weak model emits tool-call JSON as text instead of calling tools;
  catalog becomes unusable.
- Index overhead: on simple lookups, agents read the catalog AND the
  file, paying twice.
- Near-miss entity names: agents skim-match the wrong twin unless an
  exact-ID lookup path exists.

## When NOT to apply this skill

- Corpus comfortably fits in context and queries are simple lookups.
- The consuming model is small or unreliable at multi-step tool use.
- The "corpus" is a single document. Just let the agent read it.
- You cannot maintain the catalog. A stale catalog is worse than none.

## Verify (optional, for high-stakes conversions)

Run the A/B benchmark (portal-preload vs catalog-fetch, 24 paired tasks,
3 difficulty levels, fresh sub-agents) before and after. If the catalog
does not win on tokens at non-inferior accuracy, revert.

## Evidence

13 attested experiments (7 + 6 re-runs), ~600 fresh sub-agent runs,
Fifth Elephant workshop, 2026-07-07. Synthetic corpora 50k–500k tokens
with distractors and version conflicts; single-question tasks;
15-tool-call cap.
- Confirmed (Haiku 4.5, gpt-5.4-mini): catalog+fetch non-inferior on
  accuracy, 2.4×–27.6× cheaper than prompt preload; gap grows with size.
- Conditional (Haiku 4.5): savings appear only above ~100k tokens and
  on aggregation tasks; index HURTS below that (0.36–0.9×).
- Refuted for weak models (gpt-4o-mini: −4 answers; voxtral-24B: floor,
  higher cost).
- Harm (gpt-5.4-mini, p=0.03): shards exposing unresolved version
  conflicts caused wrong answers.

Not tested: real (non-synthetic) corpora, multi-turn tasks, markdown
conversion, semantic IDs, llms.txt, or any other technique from the
research round. This skill claims nothing about them.

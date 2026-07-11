---
title: "Data for Agents"
date: 2026-07-11T15:28:04+05:30
source: "https://chatgpt.com/c/6a4c51b7-9700-83ec-8d88-8798ccff3b79"
---

## User

I'm running this workshop. <WORKSHOP> Title: When Data is for Agents, Not Humans, Fifth Elephant Workshop, 07 Jul 2026 **Overview** Who will be consuming your data - humans or agents? When it’s agents, do you structure it differently? Optimize for token budgets instead of disk or query cost? From what I see, we might not need clean, joined data (agents can do that), but descriptions of relationships. Functions become checklists. Tools beat tables. Logs beat docs. Ambiguity + context might work better than a single-source of truth. It’s a 4-hour hands-on session. You’ll be doing the work and sharing results, not watching slides. We’ll share prompts live and the recording afterwards. **What this workshop is about** In this workshop, we’ll (together) explore: 1. How data engineering for agents is different than for humans 2. How agents themselves can help engineer the data for agents **Audience** This session is for: - data engineers connecting agents into pipelines - analytics/BI folks whose dashboards are vanishing into chatbots - anyone publishing docs, schemas, or APIs that agents will read **What you’ll leave with** 1. A working feel for how the same dataset looks different to a human and to an agent 2. An agent data checklist: can an agent discover, understand, efficiently retrieve, call the right tool, trust the source, recover from errors? 3. Prompts and small scripts to make your tables, docs, and logs agent-accessible 4. Your results, published and shared, reproducibly **What to bring** - Laptop (your tablet/phone won’t do for this session), a modern browser - A paid ChatGPT Plus or Claude Pro account (\~Rs 2,000 - just buy a month). The free tiers won’t do some exercises. - Optional, for coders: uv, Node.js, and DuckDB installed - Datasets, docs, logs, photos, or anything you care about. We’ll work with your data What are approaches or organize data for agents? </WORKSHOP> "Data" includes any content, data, tool, or any other input an agent might read or use, which includes: - structured data: tables, spreadsheets, databases, JSON, YAML, configuration, ... - unstructured data: code, markdown, web pages, PDFs, other documents, videos, images, any files, blobs, ... - organization: folders, archives, websites, schemas, ontologies, taxonomies, ... - tools: tool choice, tool docs/descriptions, tool configuration, ... - tool outputs: error messages, session/program logs, telemetry, diagnostics, progress, ... - SKIP harness artifacts: prompts, AGENTS.md/CLAUDE.md, SKILL.md, memory systems, permissions, hooks, plugins, ... **QUESTION 1**: What else? Am I missing something? List prioritized by importance to agents. --- Next, I'd like an AI agent to research online for the modern best practices on how to structure and optimize inputs for agent consumption. Specifically, how to go about organizing these for agents **as opposed to humans**, listing the key differences in thought process. Of course, some of these are only meant for humans (e.g. harness artifacts) - so let's skip those. But whatever is traditionally meant for humans AND can be used by agents, let's include that. In this context, I want the agent to research the best practices, emerging techniques, ways of working top AI companies like Anthropic internally use, opinions of experts who create / curate data for AI agent consumption, etc. This should be shared in a priorized way, i.e. highest impact (value x frequency) + highest difference between how we would organize it for humans vs agents. I will then have the audience 1. Run this prompt across multiple agents (Claude, ChatGPT, etc.) and compare the results 2. Pick the top few techniques 3. Have a coding agent (Codex, Claude, etc.) generate synthetic data for each of these techniques, run a test / benchmark to see how well agents perform against a task when the data is organized the way it typically is for humans vs the way it is organized for agents, and share the results. - I want to make sure that this will not cost too much (i.e. ideally included in a single run of a $20 plan of Claude or Codex), so each person is able to test at least 1 and potentially 3 data organization techniques - I would like the results to be reasonably statistically significant - it should give enough confidence that it works - The test should involve invoking sub-agents with the right model + config in a way that will not be polluted by the parent agent's context, so that the test is fair and reproducible. - The result should be documented in a single Markdown file they can share that CLEARLY documents the setup, the test, the results, and the conclusions. This should be reproducible by anyone else who wants to run it just with that single Markdown file - Any other factors I have not thought of? **QUESTION 2**: What would be an apt, concise prompt for step 1 that will allow the participants to easily pick the first few techniques to test? **QUESTION 3**: What would be an apt, concise prompt for step 3 that will allow the participants to paste it, then pick any one technique to test, and run it? They should be able to copy-paste the prompt, copy-paste one technique from prompt #1, and press enter - so prompt #1 should also be designed to be copy-paste friendly.

---

## ChatGPT

I’ll separate the answer into: the missing input types, a ranked set of agent-oriented design principles, and two copy-paste prompts with a low-cost reproducible benchmark protocol.

Thought for 2m 15s

The useful organizing frame is not file type. It is the agent’s path:

**discover → select → retrieve → interpret → act → observe → verify → recover → learn**

Your current list covers the payloads. What is mostly missing is the **control plane around those payloads**.

## Question 1: What is missing?

Prioritized by how frequently it determines agent success:

1. **Semantics and relationships**

Data dictionaries, entity definitions, stable IDs, units, null meanings, valid ranges, candidate keys, cardinality, join evidence, dependencies, causal or temporal relationships, synonyms and domain vocabulary.

Humans infer much of this from conventions, visual grouping and institutional knowledge. Agents need it made explicit. An agent may discover a join, but it should not have to guess whether it is one-to-one, historical, approximate or unsafe. 2. **Discovery and routing information**

Catalogs, manifests, indexes, sitemaps, inventories, stable URIs, concise resource descriptions, aliases and “use this source when…” guidance.

This may be the most distinctly agent-oriented layer. OpenAI describes replacing a monolithic manual with a small map pointing to deeper sources, while Anthropic recommends lightweight identifiers and just-in-time retrieval rather than loading everything into context. [OpenAI+1](https://openai.com/index/harness-engineering/) 3. **Provenance, authority and time**

Source, owner, lineage, citation, version, observed time, effective time, last verified time, freshness expectations, confidence, supersession and whether something is fact, estimate or opinion.

An agent often sees several plausible answers simultaneously. It needs enough metadata to choose, reconcile or surface the disagreement rather than silently collapse it. Microsoft’s agentic retrieval guidance explicitly recommends citation fields and resource descriptions that help an agent decide whether to use an index. [Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-create-index) 4. **Contracts, constraints and side effects**

Schemas, invariants, preconditions, postconditions, validation rules, permissions at the data boundary, destructive effects, idempotency, reversibility, latency, cost, quotas, pagination and retry semantics.

This is larger than tool documentation. It includes database constraints, business rules, API contracts and operational limits. MCP, for example, provides hints for read-only, destructive, idempotent and open-world tools. [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/schema?utm_source=chatgpt.com) 5. **State, events and change**

Current snapshots, event streams, transactions, diffs, changelogs, tombstones, pending states, queues and distinctions such as requested versus started versus completed.

A document usually describes what should happen. An operating agent needs to know **what has already happened, what changed and what remains uncertain**. 6. **Examples, fixtures and executable evidence**

Valid examples, invalid examples, sample calls and responses, edge cases, counterexamples, tests, validators, expected outputs and known failure cases.

Examples expose conventions that prose and schemas frequently omit. Anthropic recommends detailed tool descriptions, strict data models and examples for complex inputs; it also found that useful error messages can teach agents how to correct calls. [Claude Platform Docs+1](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use?utm_source=chatgpt.com) 7. **Feedback, outcomes and ground truth**

Corrections, accepted and rejected outputs, reviewer comments, labels, user actions, downstream outcomes, quality scores, evaluation cases and adjudicated answers.

These let an agent distinguish “the operation completed” from “the operation produced a useful result.” 8. **Observation surfaces**

Queryable metrics, traces, screenshots, rendered previews, health checks, progress events and state inspection—not merely raw logs.

OpenAI reports making application UI, logs, metrics and traces directly queryable by Codex so it can validate work and close its own feedback loop. [OpenAI+1](https://openai.com/index/harness-engineering/) 9. **Access, sensitivity and governance metadata**

Audience, ownership, confidentiality, licence, retention, residency, consent, redaction status and permissible transformations.

This is data-level governance, distinct from agent-harness permissions. 10. **Machine-usable multimodal derivatives**

OCR text with coordinates, transcripts with timestamps and speakers, image captions and regions, video chapters, table extraction, reading order and links back to the original pixels or frames.

The derivative should not replace the original. Agents need both a cheap searchable representation and a route back to the source.

### A few hypotheses in the overview should be softened

I would present these as questions to test, not conclusions:

- Not **“agents do not need clean, joined data”**, but: **preserve raw, versioned data and expose relationships clearly; avoid prematurely flattening everything into one canonical table.**
- Not **“tools beat tables”**, but: **tools beat bulk dumps when the agent needs bounded retrieval or action; tables remain excellent for inspection, filtering and batch computation.**
- Not **“logs beat docs”**, but: **docs explain intended behaviour; logs, metrics and tests reveal actual behaviour. Agents need both.**
- Not **“ambiguity may beat a single source of truth”**, but: **retain competing claims when appropriate, while making disagreement, provenance and confidence explicit.**
- Not **“optimize only for tokens”**, but: **optimize useful evidence per token, tool call, second and failure opportunity.**

Long context alone is not a substitute for organization: models can use information unevenly depending on its position, while current agent systems increasingly use progressive disclosure, targeted queries and just-in-time retrieval. [arXiv+2Anthropic+2](https://arxiv.org/abs/2307.03172?utm_source=chatgpt.com)

## Factors to add to the benchmark design

The most important additions are:

1. **Classify the intervention.** Is it reorganizing identical information, adding new information, or changing how information is accessed? Otherwise “better organization” may merely mean “more clues.”
2. **Use paired instances.** Each underlying synthetic world should generate both variants. This removes much of the variation between tasks.
3. **Blind the evaluator.** Evaluation agents should see condition `A` or `B`, not “human” versus “agent,” and should not receive the hypothesis.
4. **Prevent floor and ceiling effects.** Pilot first. If both variants score almost 0% or 100%, the benchmark cannot reveal much.
5. **Predeclare one primary metric.** Secondary metrics can include tokens, tool calls, latency, unsupported claims and recovery rate, but significance should be based on the declared primary metric.
6. **Prefer deterministic grading.** Exact answers, state checks and executable validators are better than an LLM judge. For open-ended tasks, combine coverage, groundedness and source-quality checks rather than one holistic score. [Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
7. **Use genuinely isolated runs.** Each evaluation should receive only its task and one variant. Anthropic’s subagents use separate context windows and return only selected results, which is the pattern to reproduce even when using another platform. [Anthropic](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
8. **Measure the cost of the intervention.** An agent version that improves accuracy by 3% but consumes four times as many tokens may not be better.
9. **Keep execution deterministic.** Use local mock tools and fixed synthetic data instead of live websites or changing APIs unless freshness is the subject being tested.
10. **Limit the claim.** A 12–20-pair workshop experiment can provide useful evidence of a substantial effect on one model and task family. It does not establish a universal best practice.

## Question 2: Research and selection prompt

This produces a comparable ranking plus self-contained technique cards that participants can paste into the experiment prompt.

Edit

## Question 3: Build-and-run benchmark prompt

Edit

For the workshop, **12 paired instances with a predeclared extension to 20** is a better default than demanding significance regardless of cost. It can detect a strong, consistent effect while keeping the benchmark small enough for each participant to test more than one technique.

---

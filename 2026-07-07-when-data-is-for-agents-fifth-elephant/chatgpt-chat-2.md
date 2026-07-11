---
title: "AI Data Organization Practices"
date: 2026-07-11T15:28:49+05:30
source: "https://chatgpt.com/c/6a4cbe37-b288-83ec-aa42-f78f26393f9b"
---

## User

Research current (2026) best practices for organizing data for AI AGENTS to consume, as opposed to humans. "Data" includes: structured data (tables, JSON, schemas), documents (markdown, PDFs, web pages), code, media, folder and site organization, tool definitions and docs, tool outputs, errors, logs, metrics, and traces. EXCLUDE agent-harness artifacts (system prompts, AGENTS.md, SKILL.md, memory, permissions, hooks). Search the web. Prefer primary sources: engineering blogs and docs from Anthropic, OpenAI, Google, and similar; standards (e.g., MCP, llms.txt); papers and benchmarks; practitioners who prepare data or APIs for agents. Mark clearly what is MEASURED evidence vs expert OPINION. Return the TOP 10 techniques, ranked by: (impact × how often the situation occurs) × (how DIFFERENTLY you would do it for agents vs humans). Skip anything where the human and agent way match. First, one compact ranked table: Rank | Technique | For humans | For agents | Evidence: measured/opinion Then one card per technique, EXACTLY this format — self-contained, under 120 words, no cross-references, so each card can be copy-pasted alone:

```
markdown
### T{n}. {Short technique name}

- Type: representation (same facts, reorganized) | augmentation (adds info) | access (changes how it's fetched)
- For humans: {traditional organization}
- For agents: {organize it this way instead}
- Why: {mechanism — token budget, retrieval, trust, error recovery, ...}
- Matters when: {what should make the gap appear — corpus size, distractor density, multi-hop questions, ...}
- Testable claim: {ONE measurable sentence: "Agents do task X more
  accurately / with fewer tokens when data is B instead of A"}
- Evidence: {measured | opinion} — {1–3 links}
```

---

## ChatGPT

I’ll build this from primary sources and benchmarks, separate measured results from practitioner guidance, then rank only techniques that materially diverge from human-oriented organization.

Thought for 2m 45s

| Rank | Technique                                | For humans                                                    | For agents                                                                          | Evidence: measured/opinion                                                                                                                                                                                          |
| ---- | ---------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Progressive disclosure                   | Show complete menus, indexes, repositories, and tool catalogs | Search a compact manifest, then fetch exact definitions or artifacts on demand      | **Measured** — one instrumented case reduced tool-definition context from 150,000 to 2,000 tokens. [Anthropic+1](https://www.anthropic.com/engineering/code-execution-with-mcp)                                     |
| 2    | Compute where data lives                 | Export complete datasets and inspect them in a UI             | Filter, join, aggregate, and transform before anything enters model context         | **Measured** — code-mediated API access reduced both context transfer and benchmark cost. [Anthropic+1](https://www.anthropic.com/engineering/code-execution-with-mcp)                                              |
| 3    | Self-contained retrieval units           | Let passages depend on surrounding pages and chapters         | Repeat the minimum document and section context inside every retrievable unit       | **Measured** — contextual retrieval reduced failed retrievals by 49%, or 67% with reranking. [Anthropic](https://www.anthropic.com/engineering/contextual-retrieval)                                                |
| 4    | Semantic schemas                         | Use terse names and rely on analyst knowledge                 | State meanings, grain, units, joins, null rules, synonyms, and business constraints | **Measured** — richer column descriptions consistently improved text-to-SQL performance. [arXiv+1](https://arxiv.org/abs/2408.04691)                                                                                |
| 5    | Tool descriptions as contracts           | Provide conventional endpoint reference documentation         | Encode selection criteria, semantics, limits, outputs, side effects, and examples   | **Measured** — description quality changed tool selection and raised median task success by 5.85 points. [arXiv+1](https://arxiv.org/abs/2602.18914)                                                                |
| 6    | Compact typed results                    | Return readable reports, prose, and visually formatted tables | Return schema-valid objects, semantic labels, pagination, and selectable detail     | **Measured** — representation changes affect accuracy; concise tool responses used about one-third the tokens in Anthropic’s example. [Anthropic+1](https://www.anthropic.com/engineering/writing-tools-for-agents) |
| 7    | Executable errors                        | Give developers codes, prose messages, and stack traces       | Return typed failures with retryability and concrete machine-applicable repairs     | **Measured** — structured recovery suggestions improved completion and token efficiency in controlled pilots. [arXiv+1](https://arxiv.org/html/2606.05037v1)                                                        |
| 8    | Structure-preserving documents and media | Depend on visual layout, reading order, charts, and playback  | Preserve hierarchy, cells, coordinates, visual evidence, speakers, and timecodes    | **Measured** — hierarchy-aware parsing materially outperformed naïve PDF extraction; multimodal fusion beat unimodal retrieval. [arXiv+1](https://arxiv.org/abs/2604.04948?utm_source=chatgpt.com)                  |
| 9    | Atomic provenance                        | Put citations and lineage in footers or separate catalogs     | Attach source, time, version, authority, confidence, and lineage to every unit      | **Measured** — authority-aware filtering improved RAG accuracy; argument-level provenance improved agent security and utility. [arXiv+1](https://arxiv.org/abs/2603.25092?utm_source=chatgpt.com)                   |
| 10   | Causal telemetry                         | Optimize logs for dashboards and human incident review        | Emit structured event graphs connecting model calls, tools, retries, and outputs    | **Opinion** — standards and research surveys strongly converge on this representation, but direct A/B evidence remains limited. [OpenTelemetry+1](https://opentelemetry.io/blog/2026/genai-observability/)          |

### T1. Progressive disclosure

- Type: access (changes how it's fetched)
- For humans: Show menus, full indexes, documentation trees, and all available tools for browsing.
- For agents: Expose a tiny capability manifest; let the agent search summaries, then fetch only the exact file, chunk, schema, or tool definition needed.
- Why: Up-front catalogs consume context and create distractors before the task is understood.
- Matters when: Tool definitions, repositories, sites, or corpora occupy more than roughly 1–5% of context.
- Testable claim: Agents complete the same tasks with fewer input tokens when they search a compact catalog and load details on demand.
- Evidence: measured — Anthropic/MCP measured 150,000→2,000 tokens; `llms.txt` alone is rarely fetched. [Anthropic+2Model Context Protocol+2](https://www.anthropic.com/engineering/code-execution-with-mcp)

### T2. Compute where data lives

- Type: access (changes how it's fetched)
- For humans: Export full tables, documents, or API responses into a UI, then inspect and manipulate them.
- For agents: Provide query, code, filter, join, aggregate, and projection operations; return only the small result or durable handle needed next.
- Why: Copying large intermediate payloads through model context wastes tokens and introduces transcription errors.
- Matters when: Results are large, workflows chain tools, or intermediate data need not be read by the model.
- Testable claim: Agents use fewer tokens and make fewer transfer errors when computation happens beside the data rather than through full context copies.
- Evidence: measured — Anthropic code-execution case; Doc2Agent benchmark. [Anthropic+1](https://www.anthropic.com/engineering/code-execution-with-mcp)

### T3. Make retrieval units self-contained

- Type: augmentation (adds info)
- For humans: Let paragraphs, pages, and sections depend on surrounding chapters, headings, and visual position.
- For agents: Attach a short contextual prefix to every chunk: document purpose, section path, entities, date/version, scope, and needed antecedents.
- Why: Retrieval detaches passages from their neighborhood; ambiguous chunks embed and rank poorly.
- Matters when: Corpora are large, sections reuse vocabulary, or questions distinguish similar products, periods, policies, or entities.
- Testable claim: Agents retrieve and answer more accurately when each chunk includes document-level and section-level context than when the raw chunk is indexed alone.
- Evidence: measured — Anthropic Contextual Retrieval; PDF-to-RAG preprocessing study. [Anthropic+1](https://www.anthropic.com/engineering/contextual-retrieval)

### T4. Add semantic schemas, not just types

- Type: augmentation (adds info)
- For humans: Use concise column names and rely on analysts' domain knowledge, examples, and institutional memory.
- For agents: Describe every field's meaning, unit, grain, allowed values, null semantics, identifiers, join paths, synonyms, temporal rules, and business constraints.
- Why: Syntactic schemas say what is legal; agents also need semantics to select, join, filter, and aggregate correctly.
- Matters when: Schemas are wide, names are cryptic, tables overlap, or business definitions differ from everyday language.
- Testable claim: Agents generate more semantically correct queries when schemas include field descriptions and business rules than when they include names and types alone.
- Evidence: measured — BIRD column-description study; equivalent-schema robustness study. [arXiv+1](https://arxiv.org/abs/2408.04691)

### T5. Write tool descriptions as contracts

- Type: augmentation (adds info)
- For humans: Document endpoints separately and expect developers to infer which one fits a task.
- For agents: Give each tool a distinct name plus purpose, when to use or avoid it, parameter semantics, return shape, side effects, prerequisites, limits, and one compact example.
- Why: Tool descriptions are simultaneously documentation, routing features, and behavioral instructions.
- Matters when: Tools overlap, many servers are connected, parameters are domain-specific, or actions have side effects.
- Testable claim: Agents select the correct tool and arguments more often when descriptions state accurate functionality and complete semantics than when they repeat names.
- Evidence: measured — two 2026 MCP studies; Anthropic guidance. [arXiv+2arXiv+2](https://arxiv.org/abs/2602.18914)

### T6. Return compact, typed results

- Type: representation (same facts, reorganized)
- For humans: Return narrative explanations, visually formatted tables, every metadata field, and verbose confirmations.
- For agents: Return schema-valid structured content with clear fields, semantic labels beside opaque IDs, stable ordering, pagination, truncation notices, and concise/detailed modes.
- Why: Predictable fields support composition; excess prose and irrelevant metadata consume context and increase ambiguity.
- Matters when: Outputs feed another tool, contain many rows, or require exact identifiers for follow-up actions.
- Testable claim: Agents complete downstream operations with fewer tokens and parsing failures when tools return compact schema-valid objects instead of verbose untyped text.
- Evidence: measured — Anthropic response measurements; MCP output schemas; TABVERSE. [Anthropic+2Model Context Protocol+2](https://www.anthropic.com/engineering/writing-tools-for-agents)

### T7. Make errors executable

- Type: augmentation (adds info)
- For humans: Return an HTTP code, prose message, or stack trace and let a developer diagnose the fix.
- For agents: Return a typed error with failed field, violated rule, retryability, accepted values, current state, and a concrete next action or JSON Patch-style repair.
- Why: Agents otherwise spend calls guessing, especially when the rule is proprietary or state-dependent.
- Matters when: APIs enforce business rules, failures are recoverable, or workflows run without a human watching.
- Testable claim: Agents recover more often and with fewer retries when errors include machine-readable repair suggestions than when they include diagnosis-only prose.
- Evidence: measured — Self-Reflective APIs; MCP error contract; ToolBench-X. [arXiv+2Model Context Protocol+2](https://arxiv.org/html/2606.05037v1)

### T8. Preserve document and media structure

- Type: representation (same facts, reorganized)
- For humans: Publish PDFs, slides, dashboards, images, audio, and video whose meaning depends on layout and visual or temporal cues.
- For agents: Provide linked text and visual representations: hierarchy-aware Markdown/JSON, real table cells, chart data/descriptions, page and bounding-box anchors, speaker labels, timestamps, and source crops.
- Why: Flat OCR destroys reading order, table relations, evidence location, and cross-modal meaning.
- Matters when: Answers depend on tables, figures, forms, footnotes, diagrams, speaker turns, or exact moments.
- Testable claim: Agents answer more accurately when parsed data preserves hierarchy and linked visual evidence than when given flat extracted text.
- Evidence: measured — PDF-to-RAG study; UniDoc-Bench; TABVERSE. [arXiv+2arXiv+2](https://arxiv.org/abs/2604.04948?utm_source=chatgpt.com)

### T9. Put provenance on every unit

- Type: augmentation (adds info)
- For humans: Put sources in a bibliography, report footer, dashboard note, or separate lineage catalog.
- For agents: Attach source URI, stable record ID, retrieval/effective time, version, authority, lineage, confidence, and supporting span to each fact or result.
- Why: Atomic provenance lets agents resolve conflicts, prefer fresh authoritative data, cite claims, and keep untrusted values out of privileged actions.
- Matters when: Sources conflict, data change quickly, transformations are multi-step, or actions carry financial, legal, or security risk.
- Testable claim: Agents produce more accurate and safer outputs when evidence is ranked and constrained using atomic provenance than when all retrieved text is treated equally.
- Evidence: measured — AuthorityBench; PACT provenance benchmark. [arXiv+1](https://arxiv.org/abs/2603.25092?utm_source=chatgpt.com)

### T10. Store telemetry as causal events

- Type: representation (same facts, reorganized)
- For humans: Optimize logs and metrics for dashboards, keyword search, and narrative incident review.
- For agents: Emit immutable events with trace/span IDs, parent links, timestamps, status, retries, tool/model IDs, input/output references, cost, and dependency edges.
- Why: Agents diagnose by reconstructing trajectories; joins and causality must be machine-resolvable.
- Matters when: Workflows are multi-step, concurrent, retried, long-running, or distributed across tools.
- Testable claim: Diagnostic agents identify failed steps with fewer inspected events when telemetry includes standardized causal links than when given flat text logs.
- Evidence: opinion — OpenTelemetry GenAI conventions and the 2026 execution-provenance survey recommend this; direct A/B evidence is limited. [OpenTelemetry+1](https://opentelemetry.io/blog/2026/genai-observability/)

---

---
title: "Fifth Elephant Workshop Curating Data for Agents Collation"
date: 2026-07-11T20:22:28+05:30
source: "https://chatgpt.com/c/6a4cc169-d84c-83ec-8321-a4fa0f5eea7d"
---

## User

Below are technique cards collected from several AI research agents. Formats
may vary and some fields may be missing. Collate them into one ranked list.

1. NORMALIZE. Parse every technique into the standard card format (Type / For humans / For agents / Why / Matters when / Testable claim / Evidence). Fill small gaps from context; flag anything you inferred.
2. DEDUPLICATE. Merge two cards ONLY if the same A/B test would test both. If they sound similar but need different tests, keep them separate. When merging, keep the best-evidenced claim, combine the sources, and note "seen in {k} of {N} submissions" on the card.
3. SCORE each technique independently, 1–5 on each, before any ranking:
   - Evidence: measured benchmark > vendor docs/practice > expert opinion
   - Mechanism: is the "Why" a clear causal story, not a vibe?
   - Testability: can a 24-task A/B benchmark on synthetic data show it?
   - Expected gap: how differently would agents vs humans organize this, and how big should the effect be?

   Do NOT score on: how many submissions mention it, how well the card is written, how long it is, or where it appeared in this pile. Popularity may just mean good SEO, not good evidence.

4. RANK by total score. Break ties toward techniques that should work across different agents and models, not just one vendor's product.
5. OUTPUT:
   - The top 10, renumbered T1–T10, each in the full card format starting with `### T{n}. {Short technique name}`, with its scores and the "seen in k of N" note.
   - Then `### Others`: every remaining technique as one prioritized bullet — name, one sentence, and why it didn't make the cut.

SUBMISSIONS:

answer
Data should be organized as graphs.
JSON or XML should perform better than tables or CSVs because it has better named key attributes for each value?
We need to provide semantic meaning and domain knowledge
MARKDOWN ALL THE WAY!! All content must originate as markdown.
more context, self catalogued data, data catalogue as an integral part of the data, org and global context as data.
"An AGENTS.MD file explaining the context, query examples etc.
Guardrails and tacit knowledge
true
in form of trees :) so that relationshiop ships can be associated
Data with more emphasis on metadata.
Best structure is the one that explains the data i.e. with proper metadata
Json and csv
Each data artifact requires provenance (e.g. source system name, pipeline name, last refresh), quality metadata (e.g. checks and qc results), contractual expectations (e.g. met SLAs).
Using the AGENTS.md, SKILLS.md files and other ways of instruction that inform about the schema that the agent is built with - this can be through a combined approach that explains the dataset as well as the granular schema
"Pragmatic: Context about the domain. Use case.
Semantic: The Metadata. How it was collected. Aggregation level. Definitions
true
Not too much data at once. Separation of concerns is not a natural behaviour for an AI agent.
"For Web Pages - Links with a short description
For tabular data - access to the source and then make it dynamically queryable
For Large documents - mardkown enabled access through a parsing tool with metadata
true
Need good indexing mechanism at different level, some sort of AST / hieararchical manner.
"1. Machine processable 2. Remove possible hallucination cause
true
Related data elements should be coupled together e.g. review comments must be associated with product id.
explain about the data probably in the markdown file
Opus 4.8
ChatGPT with GPT 5.5 high
Claude Opus 4.8 High
ChatGPT 5.5 - High
Opus 4.8 (High)
Gpt5.5 with deep thinking mode
Copilot with Opus
Claude code and Fable-5
Gemini 3.1 Pro
MiniMax M3 on xhigh in Hermes Agent
Flat Markdown root summaries with journalistic inverted-pyramid structures
Claude with Opus 4.8 High
Codex with GPT-5.5 with a high reasoning effort
Gemini
"I'll research this thoroughly, prioritizing primary sources. Let me run a broad set of searches in parallel.Let me gather a few more primary sources on specific techniques.Here's what the current (2026) primary sources converge on. I focused only on techniques where the **agent way genuinely diverges from the human way** — anything identical was dropped. Evidence is tagged **measured** (benchmarks/experiments) vs **opinion** (expert guidance/standards).

## Ranked summary

| Rank | Technique                                                               | For humans                                 | For agents                                                           | Evidence           |
| ---- | ----------------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------- | ------------------ |
| T1   | Just-in-time / progressive tool & doc loading                           | All API docs & tools browsable up front    | Expose as on-disk code/searchable index; load only what a task needs | **Measured**       |
| T2   | Markdown/plain text instead of HTML                                     | Styled HTML/PDF for reading                | Clean Markdown, tags/nav/scripts stripped                            | **Measured**       |
| T3   | Lean, filtered tool outputs; offload bulk to files                      | Full result sets, verbose logs, dashboards | High-signal fields only; large payloads → file path + summary        | **Measured**       |
| T4   | Contextual chunking/retrieval                                           | Chapters, sections, TOC                    | Retrieval chunks with prepended context before embedding             | **Measured**       |
| T5   | Structured, classified, actionable errors                               | Short message; recover via docs/intuition  | Stable code + reason + remediation + retryable/fatal class           | Opinion + measured |
| T6   | Behavioral tool definitions (namespacing, ""use when"", strict schemas) | Reference docs of what each endpoint does  | Embedded SOPs/guardrails, namespaces, typed inputs                   | Opinion            |
| T7   | Agent-first API contracts (idempotency, enums, batch, cursor)           | One-at-a-time forms, tolerant of variance  | Idempotency keys, deterministic states, bulk endpoints               | Opinion            |
| T8   | llms.txt + per-page .md mirrors                                         | sitemap.xml, nav menus, rendered pages     | Curated Markdown map + `.md` twin of each page                       | Opinion            |
| T9   | Agent-native telemetry (OpenTelemetry GenAI)                            | HTTP status, latency dashboards            | Per-span token counts, tool-call trees, `gen_ai.*` attributes        | Opinion/standard   |
| T10  | Text-first tables & media                                               | Rendered tables, images, charts            | Extract to Markdown/CSV/described text (keep raw as fallback)        | **Measured**       |

---

```markdown
### T1. Just-in-time / progressive tool & doc loading

- Type: access
- For humans: every API doc and tool reference is browsable and loaded up front.
- For agents: expose tools/docs as on-disk code modules or a searchable index; load only the definitions a task actually needs, at call time.
- Why: token budget + context rot — each preloaded definition is re-sent every loop step and dilutes attention.
- Matters when: dozens+ of tools/servers, long multi-step tasks.
- Testable claim: Agents complete multi-tool workflows with far fewer tokens when tool definitions load on demand instead of all upfront.
- Evidence: measured — Anthropic's code-execution-over-MCP cut a workflow 150k→2k tokens (98.7%); a 60-tool load dropped 47k→~400 tokens via dynamic discovery. 【1-69f295】【2-01aa9a】
```

```markdown
### T2. Markdown/plain text instead of HTML

- Type: representation
- For humans: styled HTML or PDF, rendered for visual reading.
- For agents: serve clean Markdown (or a `.md` mirror), stripping tags, nav, ads, and scripts.
- Why: token efficiency and signal-to-noise — HTML markup carries no semantic value but consumes context; Markdown also chunks more cleanly for retrieval.
- Matters when: web/doc corpora, RAG pipelines, large pages.
- Testable claim: Agents answer more accurately and with fewer tokens from Markdown than from the equivalent HTML.
- Evidence: measured — ~3–5x / 67% token reduction vs HTML; reported +20–35% RAG accuracy and 20–30% token savings (vendor benchmarks). 【3-662c0b】【4-783807】
```

```markdown
### T3. Lean, filtered tool outputs; offload bulk to files

- Type: access
- For humans: full result sets, verbose logs, and dashboards to scan.
- For agents: return only high-signal fields; write large payloads to a file and pass back a path plus a one-line summary.
- Why: tool results persist and re-cost tokens every subsequent turn, and bulk output buries the signal the agent needs.
- Matters when: big query results, long logs, many-turn sessions.
- Testable claim: Agents use fewer tokens and stay more accurate when tool results are trimmed/offloaded rather than dumped inline.
- Evidence: measured/opinion — Anthropic tool-writing guidance on token-efficient results; CodeAgents reports 55–87% input-token cuts. 【5-576450】 【6-81418f】
```

```markdown
### T4. Contextual chunking/retrieval

- Type: augmentation
- For humans: documents organized by chapters, sections, and a table of contents.
- For agents: split into retrieval chunks and prepend chunk-specific context before embedding, paired with BM25 and reranking.
- Why: isolated chunks lose their referents (""the company"", ""last quarter""), causing retrieval to miss relevant passages.
- Matters when: large knowledge bases, multi-hop questions, ambiguous references.
- Testable claim: Retrieval failure rate drops when chunks are contextualized versus naive fixed-size splitting.
- Evidence: measured — Anthropic reports 49% fewer failed retrievals (with BM25), 67% with reranking; independent tests show 9–41-point recall spreads by chunking method. 【7-a99047】【8-472d4d】
```

```markdown
### T5. Structured, classified, actionable errors

- Type: augmentation
- For humans: a short message; a person recovers by reading docs or using intuition.
- For agents: a stable error code, a reason, a remediation hint, and a retryable-vs-fatal classification.
- Why: error recovery — vague errors (""500"", ""failed"") cause blind retries and infinite loops; classified errors let the agent branch correctly.
- Matters when: flaky/rate-limited tools, long autonomous runs.
- Testable claim: Agents recover more often and loop less when errors are structured/classified rather than generic strings.
- Evidence: opinion + measured — agent-API design guidance; the PROBE framework reports a 21.8% recovery rate on previously unresolved cases. 【9-6c4924】【10-09bc06】
```

```markdown
### T6. Behavioral tool definitions

- Type: representation
- For humans: reference docs describing what each endpoint does.
- For agents: embed SOPs and hard guardrails plus ""use when…"" guidance directly in the description, namespace related tools, and enforce strict typed input schemas.
- Why: trust/selection — under ambiguity, agents pick the wrong tool or invent parameters; behavioral cues and namespaces bound the choice.
- Matters when: many overlapping or similarly named tools.
- Testable claim: Correct tool-selection rate rises with behavioral, namespaced descriptions versus bare name+params.
- Evidence: opinion — Anthropic (""writing tools for agents""), OpenAI function-calling, and MCP tool-spec guidance. 【5-576450】【11-072e08】
```

```markdown
### T7. Agent-first API contracts

- Type: access
- For humans: one-form-at-a-time UX, human-readable responses, tolerance for minor variance.
- For agents: idempotency keys on state-changing calls, deterministic enum states, batch/bulk endpoints, and agent-sized cursor pagination.
- Why: agents retry, parallelize, and can't program against responses that vary (e.g. ""queued"" vs ""processing"").
- Matters when: state-changing operations and high-volume/batch work.
- Testable claim: Duplicate writes and stalls drop when APIs add idempotency keys and deterministic response shapes.
- Evidence: opinion — practitioner guidance on designing APIs for agent consumers. 【9-6c4924】【12-2e9146】
```

```markdown
### T8. llms.txt + per-page .md mirrors

- Type: augmentation
- For humans: sitemap.xml, nav menus, and rendered pages.
- For agents: a root `/llms.txt` Markdown map of the most important resources, plus a `.md` version of each page at the same URL.
- Why: retrieval + token budget — gives a curated, parseable entry point instead of forcing the model to crawl noisy HTML at inference time.
- Matters when: docs/product sites that agents read live.
- Testable claim: Agents cite and answer more accurately about a site when llms.txt and .md mirrors exist versus HTML-only.
- Evidence: opinion — llmstxt.org proposal (Jeremy Howard, 2024) with growing vendor adoption (Anthropic, Cloudflare, Perplexity). 【13-fd104f】【14-38e2a4】
```

```markdown
### T9. Agent-native telemetry (OpenTelemetry GenAI)

- Type: representation
- For humans/ops: HTTP status codes, latency dashboards, and error rates.
- For agents/ops: per-span token counts, model/provider identity, tool-call trees, and time-to-first-token via standardized gen_ai.\* attributes.
- Why: error recovery/observability — non-deterministic tool loops and token runaway are invisible to request/response APM but visible as a decision tree.
- Matters when: multi-agent systems, production, cost control.
- Testable claim: Stuck loops and token blow-ups are detected faster with GenAI spans than with standard HTTP/DB traces.
- Evidence: opinion/standard — OpenTelemetry GenAI Semantic Conventions (spans, metrics, events for LLM/agent/tool ops). 【15-9b9096】【16-3fe70d】
```

```markdown
### T10. Text-first tables & media

- Type: representation
- For humans: rendered tables, images, and charts to view.
- For agents: extract tables to Markdown/CSV text and convert images/charts to described or structured text, keeping the raw file only as a fallback.
- Why: token/trust — models read cell text and structured layout far more reliably than raw pixels, and text costs fewer tokens.
- Matters when: PDFs/scans with tables, dashboards, mixed text-and-visual docs.
- Testable claim: Agents extract table cell content more accurately from text-serialized tables than from table images.
- Evidence: measured — GriTS/PubTables-1M benchmark: multimodal LLMs are ""far better"" than OCR on cell text content. 【17-2204b6】
```

---

**Two honest caveats on the evidence:**

- The strongest **measured** claims are T1, T4, and T10 (controlled or vendor benchmarks with numbers). T2 and T3 numbers come largely from vendor/blog benchmarks, so treat magnitudes as directional. [\[web2md.org\]](https://web2md.org/blog/markdown-vs-html-for-llm)
- T6–T9 are **expert consensus and emerging standards** rather than head-to-head experiments — high agreement across Anthropic/OpenAI/MCP/OTel, but few published A/B numbers yet. [\[anthropic.com\]](https://www.anthropic.com/engineering/writing-tools-for-agents), [\[deepwiki.com\]](https://deepwiki.com/open-telemetry/semantic-conventions/3.5-generative-ai-conventions)

Want me to (a) turn this into a one-page exec/board slide in your usual dark-minimal style, or (b) go deeper on any single technique with implementation patterns and code?
true
"Rank | Technique | For humans | For agents | Evidence: measured/opinion
---|---|---|---|---
1 | Semantic layer over raw tables | BI schemas, dashboards, table docs | Metrics/entities/joins as deterministic ontology | measured
2 | Contextual retrieval chunks | Long docs and pages | Small chunks with local context, metadata, hybrid search | measured
3 | Typed JSON contracts | Prose specs and examples | JSON Schema/OpenAPI/MCP contracts, enums, strict outputs | measured
4 | Targeted tools, not dumps | Browse/list everything | Search/filter/action tools with bounded results | opinion
5 | Agent-readable docs endpoints | Web pages, nav, PDFs | Markdown, `/llms.txt`, `/index.md`, copy-as-Markdown | opinion
6 | Code symbol maps | Folder trees and full files | AST/LSP indexes of symbols, refs, ranked files | measured
7 | Trust/provenance wrappers | Visual trust and citations | Source, timestamp, authority, untrusted-data boundaries | opinion
8 | Token-shaped tool outputs | Human logs, stack traces | Concise/detailed modes, pagination, actionable errors | opinion
9 | Native multimodal indexes | Captions or OCR-only media | Preserve images/pages/video plus OCR, transcripts, timestamps | measured
true
"Before I write this up, let me check the relevant skills.# Top 10: Organizing Data for Agents, Not Humans

Ranked by (impact × frequency) × (how different the agent way is from the human way). Note on evidence quality: only ~4 of the 10 have solid published measurements (T1/T5 partially, T2, T4, T8). The rest run on vendor claims and practitioner consensus — each card's ""testable claim"" is a gap your difficulty-ladder benchmark could fill.

| Rank | Technique                             | For humans                             | For agents                                                      | Evidence                            |
| ---- | ------------------------------------- | -------------------------------------- | --------------------------------------------------------------- | ----------------------------------- |
| 1    | Compact, filtered tool outputs        | Full tables, dashboards, all rows      | Search-not-list, pagination, `response_format`, names not UUIDs | Measured (Anthropic evals)          |
| 2    | Progressive disclosure via references | Everything upfront, one big portal     | Index + lightweight IDs; fetch details on demand                | Measured (98.7% token cut)          |
| 3    | Grep-able plain-text corpora          | Wikis, portals, GUIs, binary docs      | Flat text files, self-describing names, no index                | Measured-ish (internal benchmarks)  |
| 4    | Self-contained chunks                 | Chapters that rely on what came before | Prepend a ""where this fits"" header to each chunk              | Measured (49–67%)                   |
| 5    | Markdown, not HTML                    | Styled web pages                       | `Accept: text/markdown` content negotiation                     | Measured (tokens); mixed (accuracy) |
| 6    | Errors as recovery instructions       | Error codes, stack traces, log files   | What happened + valid options + what to try next                | Opinion                             |
| 7    | Pick token-cheap serialization        | JSON/XML APIs, Excel                   | CSV/Markdown for flat, YAML for nested; test per task           | Measured (but contested)            |
| 8    | Queryable > readable data             | Reports, exports to read               | SQL/code interface; intermediates never enter context           | Measured (vendor)                   |
| 9    | Tool docs as prompts                  | Reference-style API docs               | Examples, when-NOT-to-use, unambiguous names                    | Measured (vendor evals)             |
| 10   | Size/cost metadata on data            | File size in a footer, if at all       | Token counts advertised before fetch                            | Opinion (deployed standard)         |

---

```markdown
### T1. Compact, filtered tool outputs

- Type: access (changes how it's fetched)
- For humans: APIs and dashboards return complete result sets; humans scroll, sort, and filter visually.
- For agents: Default to search-not-list tools. Paginate (~50 items), truncate with a note, offer a response_format enum (concise/detailed), and return human-readable names instead of UUIDs.
- Why: Every output token competes with reasoning tokens; irrelevant rows act as distractors and degrade accuracy, not just cost.
- Matters when: Result sets exceed a few dozen items; entity counts are large; multi-step workflows where outputs accumulate across turns.
- Testable claim: Agents complete multi-step lookup tasks more accurately and with fewer tokens when tools return the top-20 filtered matches instead of the full list.
- Evidence: measured — https://www.anthropic.com/engineering/writing-tools-for-agents
```

```markdown
### T2. Progressive disclosure via references

- Type: access (changes how it's fetched)
- For humans: Load everything into one portal or document so the reader has it all in front of them.
- For agents: Publish a small index (a map, a table of contents, a directory listing) plus lightweight references — file paths, IDs, URLs. The agent reads the index, then fetches only what the task needs.
- Why: Loading all definitions or documents upfront wastes context; Anthropic measured a 150,000 → 2,000 token drop (98.7%) when agents discovered tool files on demand instead of receiving all schemas.
- Matters when: Catalogs exceed ~20 items; corpora exceed the context window; most content is irrelevant to any single task.
- Testable claim: Agents answer the same questions with 90%+ fewer input tokens and equal accuracy when given an index plus fetch-on-demand instead of the full corpus.
- Evidence: measured — https://www.anthropic.com/engineering/code-execution-with-mcp ; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
```

```markdown
### T3. Grep-able plain-text corpora

- Type: access (changes how it's fetched)
- For humans: Knowledge lives in wikis, SharePoint, PDFs, and GUIs — organized for browsing and visual navigation.
- For agents: Store content as flat plain-text files with self-describing names in a shallow folder tree. The agent finds things with grep/glob/read — no vector index needed, no staleness.
- Why: Anthropic's Claude Code team found agentic search ""outperformed [RAG] by a lot"": exact match, always fresh, fails loudly, zero index maintenance.
- Matters when: The corpus changes often (code, live projects); queries name specific symbols or terms; silent staleness is costly.
- Testable claim: Agents answer needle questions over a changing corpus more accurately when it is stored as named text files searched by grep than when retrieved from a day-old vector index.
- Evidence: measured (internal benchmarks, stated publicly) — https://vadim.blog/claude-code-no-indexing/ ; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
```

```markdown
### T4. Self-contained chunks

- Type: augmentation (adds info)
- For humans: Documents flow; a section can say ""as discussed above"" because readers hold the thread.
- For agents: Prepend 50–100 tokens of situating context to every chunk before indexing: which document, which entity, which period, how it fits. Never rely on cross-references a retriever will sever.
- Why: Retrieval returns chunks in isolation; a chunk saying ""its revenue grew 3%"" is unmatchable and unusable without knowing whose revenue, when.
- Matters when: Long documents with pronouns and running references; many similar documents (quarterly reports, contracts); ambiguous entity mentions.
- Testable claim: Retrieval failure rate drops ~49% (5.7% → 2.9%) when chunks carry prepended context before embedding and BM25 indexing, and ~67% with reranking added.
- Evidence: measured — https://www.anthropic.com/engineering/contextual-retrieval
```

```markdown
### T5. Markdown, not HTML

- Type: representation (same facts, reorganized)
- For humans: Web pages with divs, scripts, nav bars, and styling — structure carried visually.
- For agents: Serve a Markdown version. Support Accept: text/markdown content negotiation (Cloudflare converts at the edge), or publish parallel .md URLs. Strip nav, scripts, boilerplate.
- Why: HTML markup is paid-for noise; Cloudflare measured ~80% token reduction (16,180 → 3,150 on their own blog post), and Claude Code already sends the markdown Accept header.
- Matters when: Agents fetch many pages per task; pages are template-heavy; per-token cost or context budget binds.
- Testable claim: Agents extract facts from web content with equal or better accuracy at ~20% of the token cost when served Markdown instead of raw HTML.
- Evidence: measured (tokens); opinion (accuracy) — https://blog.cloudflare.com/markdown-for-agents/
```

```markdown
### T6. Errors as recovery instructions

- Type: augmentation (adds info)
- For humans: Error codes, stack traces, and logs — a developer knows what ECONNREFUSED means and where to look.
- For agents: Every error states three things: what happened, what was valid (""available files: a.csv, b.csv""), and what to do next (""retry after 12 min"" or ""use cached_search instead""). Include machine-readable retryable/permanent flags.
- Why: Agents facing opaque errors either loop, give up, or hallucinate a result to fill the gap; a recovery hint turns failure into a self-correcting step.
- Matters when: Long autonomous runs with no human watching; flaky upstream services; strict input formats agents often get slightly wrong.
- Testable claim: Agents complete tasks with injected failures at a higher rate, and with fewer retry loops, when errors name valid alternatives than when they return codes alone.
- Evidence: opinion — https://microsoft.github.io/mcp-azure-security-guide/adoption/development-best-practices/ ; https://www.anthropic.com/engineering/writing-tools-for-agents
```

```markdown
### T7. Pick token-cheap serialization

- Type: representation (same facts, reorganized)
- For humans: JSON for APIs, XML for enterprise, Excel for analysis — chosen for tooling, not readability.
- For agents: Test formats per task. Benchmarks show CSV/Markdown are most token-efficient; XML costs up to 80% more tokens; markdown key-value beat CSV by ~16 accuracy points on stressed table lookups; YAML won on deeply nested data. Repeat headers every ~100 rows.
- Why: Structural tokens (brackets, tags, repeated keys) consume budget, and format changes what the model can reliably parse at scale.
- Matters when: Tables exceed a few hundred rows; nesting exceeds 3 levels; data is a large share of the prompt. Caveat: newer studies find format effects shrink for frontier models.
- Testable claim: On large-table lookup, agents answer more accurately per token with markdown key-value or CSV than with JSON or HTML serializations of identical data.
- Evidence: measured (contested) — https://www.improvingagents.com/blog/best-input-data-format-for-llms/ ; https://arxiv.org/pdf/2411.19504
```

```markdown
### T8. Queryable beats readable

- Type: access (changes how it's fetched)
- For humans: Data becomes reports, exports, and slides to be read.
- For agents: Expose data behind a query surface — SQL, DuckDB over Parquet, or a code sandbox. The agent writes the query; filtering, joining, and aggregation happen outside the context window; only the small answer returns.
- Why: The model shouldn't be the pipe intermediate data flows through. Anthropic's code-execution pattern let a transcript move Drive→Salesforce without the model ever reading it: 150K → 2K tokens.
- Matters when: Datasets are 1,000+ rows; tasks are aggregations or joins; data is sensitive (the model never sees raw records).
- Testable claim: Agents answer aggregate questions over 10K-row datasets more accurately and 10x cheaper via a SQL tool than via the same data pasted as text.
- Evidence: measured (vendor) — https://www.anthropic.com/engineering/code-execution-with-mcp
```

```markdown
### T9. Tool docs as prompts

- Type: augmentation (adds info)
- For humans: API reference docs — exhaustive, alphabetical, written for a developer who reads once and codes.
- For agents: The description IS the interface. Include example calls, edge cases, explicit formats (""ISO date YYYY-MM-DD""), when NOT to use the tool, expected cost (""~500 tokens, 2-5 sec""), and namespaced unambiguous names (asana_search, not search).
- Why: Agents choose tools by reading descriptions in-context at every turn; ambiguity between similar tools causes wrong calls, and Anthropic found naming/namespacing choices measurably shifted eval results.
- Matters when: 10+ tools available; several tools overlap; parameters have strict formats agents must guess.
- Testable claim: Agents pick the correct tool and parameters more often when descriptions include examples and negative guidance than with terse reference-style descriptions of identical tools.
- Evidence: measured (vendor evals) — https://www.anthropic.com/engineering/writing-tools-for-agents
```

```markdown
### T10. Size and cost metadata on data

- Type: augmentation (adds info)
- For humans: File size is a footnote; readers just open things and skim.
- For agents: Advertise token counts and sizes before the fetch: Cloudflare's x-markdown-tokens header, row counts in table previews, byte sizes in directory listings, ""50 more results"" notes on truncation.
- Why: An agent must budget a finite context; knowing a document is 40K tokens BEFORE fetching lets it choose head/tail sampling, chunking, or a query instead of blowing the window and degrading everything after.
- Matters when: Documents vary wildly in size; agents run long multi-fetch tasks; context is already half-full when the fetch decision happens.
- Testable claim: Agents finish long multi-document tasks with fewer context overflows and better end-of-task accuracy when every resource advertises its token count upfront.
- Evidence: opinion (deployed standard, no published outcome data) — https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/
```

---

Three honest caveats worth carrying into your talks:

**llms.txt didn't make the list — deliberately.** It's the most-hyped ""data for agents"" standard, but the measured evidence is negative: SE Ranking found ~10% adoption, Limy's 500M-event crawl log study found only 408 llms.txt fetches, and Google says it won't use it. It works as a _manually provided_ index (T2), not as something crawlers discover.

**The strongest cross-cutting mechanism is context rot, not token cost.** Chroma's study (18 models) found accuracy falls with input length even with distractors removed (~7.9% floor), and falls faster with semantically similar distractors. That's the physics behind T1, T2, T8: less-but-relevant beats complete. It also produced the one finding that would surprise your workshop audience: _shuffled_ haystacks beat coherent ones — tidy prose is not automatically agent-friendly.

true
Claude Opus 4.8
"I'll research current best practices for organizing data for AI agents. Let me search primary sources.Let me search for more primary/technical sources on specific techniques.Let me get Anthropic's primary sources on tool design and context engineering.I have strong Anthropic primary sources. Let me search for MCP tool docs, code/repo structure for agents, and retrieval/chunking evidence.I have strong evidence on chunking. Let me search for Anthropic's contextual retrieval and code/repo structure for agents.Excellent evidence. Now let me search for JSON vs markdown/table format for LLM consumption, and agent code/repo structure.I have good coverage. Let me do a couple more targeted searches: MCP tool response design / tool namespacing, and agent code navigation/observability (logs, errors for agents).I have strong material. Let me do two final searches: agent-oriented code repository structure / code navigation, and structured error messages / observability for agents.I have comprehensive evidence across all major areas. Let me do one final search on structured/actionable error messages and observability (OpenTelemetry for agents / semantic conventions).I have comprehensive evidence across all areas. I'll now compile the top 10 techniques.

Based on primary sources from Anthropic, MCP, the llms.txt spec, and peer-reviewed benchmarks, here's the ranked answer.

---

| Rank | Technique                                                                    | For humans                                              | For agents                                                                           | Evidence         |
| ---- | ---------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------- |
| 1    | Just-in-time retrieval over pre-built indexes                                | Pre-index everything into a vector DB / search portal   | Give lightweight identifiers (paths, queries) + live search tools; fetch on demand   | measured         |
| 2    | Contextual chunking (prepend situating context)                              | Chunk once, clean boundaries, human reads whole doc     | Prepend 50–100-token ""where this fits"" blurb to each chunk before embedding + BM25 | measured         |
| 3    | Token-efficient tool responses (defaults, pagination, truncation, filtering) | Return complete result sets; humans scroll/filter in UI | Cap tokens, default limits, filters; steer with truncation notes                     | measured         |
| 4    | Semantic/natural-language identifiers over UUIDs                             | Opaque IDs fine; UI resolves to labels                  | Return names/labels; resolve UUIDs to interpretable strings                          | measured         |
| 5    | Error messages as recovery scripts                                           | Stack traces + codes for a dev to debug later           | Structured error + diagnosis + explicit next action                                  | measured/opinion |
| 6    | Markdown as the default document/nav format                                  | HTML/PDF with layout, styling, navigation chrome        | Serve clean `.md` mirrors; strip chrome                                              | measured         |
| 7    | llms.txt navigation manifest                                                 | sitemap.xml + SEO for crawlers                          | Curated markdown index of top pages at `/llms.txt`                                   | opinion          |
| 8    | Tool-set curation & namespacing                                              | Expose full API surface; devs read docs                 | Few high-leverage, non-overlapping, prefixed tools                                   | measured         |
| 9    | Entity-centric ""minimum viable data"" products                              | Organize by app/system; join later in a warehouse       | Assemble per-entity views; expose only the task-relevant subset                      | opinion          |
| 10   | Tabular data as markdown/CSV tables, not per-row JSON                        | JSON for APIs; DB rows                                  | Header-once table formats (markdown/CSV/TOON)                                        | measured         |

---

```markdown
### T1. Just-in-time retrieval over pre-built indexes

- Type: access (changes how it's fetched)
- For humans: build a vector/search index over the whole corpus up front so a portal can serve results.
- For agents: expose lightweight identifiers (file paths, glob/grep, stored queries) and let the agent load only what it needs at runtime.
- Why: retrieval/token budget — indexes go stale, chunking loses structure, and loading everything wastes the attention budget; on-demand reads stay fresh and permission-aware.
- Matters when: dynamic corpora (code, live data), exact-match needs, large repos where pre-loading is costly.
- Testable claim: Agents complete codebase tasks more accurately when using live grep/glob/read tools instead of a pre-built vector index.
- Evidence: measured — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; https://vadim.blog/claude-code-no-indexing/
```

```markdown
### T2. Contextual chunking (prepend situating context)

- Type: augmentation (adds info)
- For humans: split documents at clean boundaries; a person reading the whole document already has surrounding context.
- For agents: before embedding and BM25-indexing each chunk, prepend a 50–100-token blurb saying where the chunk sits in the parent document.
- Why: retrieval — isolated chunks lose antecedents (""the company"", ""Q2"") that a whole-doc reader keeps, causing failed retrievals.
- Matters when: large corpora, cross-referencing docs, multi-hop questions, ambiguous entities/time periods.
- Testable claim: Agents retrieve relevant chunks more often (up to ~49% fewer failures with BM25, ~67% with reranking) when chunks carry prepended context vs raw chunks.
- Evidence: measured — https://www.anthropic.com/engineering/contextual-retrieval
```

```markdown
### T3. Token-efficient tool responses (defaults, pagination, filtering, truncation)

- Type: representation (same facts, reorganized)
- For humans: return full result sets; people scroll, sort, and filter in a UI at no cognitive-budget cost.
- For agents: apply sensible default limits, pagination, filtering, and truncation; keep responses well under ~25k tokens and steer with truncation notes.
- Why: token budget — every response token is unavailable for reasoning or further tool calls; bloated returns crowd out the task.
- Matters when: list-all endpoints, large tables/logs, long multi-step agent loops.
- Testable claim: Agents finish multi-tool tasks with fewer tokens and higher completion when tools return filtered/paginated results instead of full dumps.
- Evidence: measured — https://www.anthropic.com/engineering/writing-tools-for-agents
```

```markdown
### T4. Semantic identifiers over cryptic IDs

- Type: representation (same facts, reorganized)
- For humans: opaque UUIDs are fine — the UI resolves them to names and humans copy/paste exact strings reliably.
- For agents: return human-readable fields (name, file_type, image_url); resolve arbitrary UUIDs to meaningful strings or a 0-indexed scheme.
- Why: trust/error reduction — agents handle natural-language identifiers far better than alphanumeric UUIDs, which trigger hallucination and misrouting.
- Matters when: retrieval tasks, entity disambiguation, chained tool calls referencing prior results.
- Testable claim: Agents retrieve and reference entities more precisely (fewer hallucinated IDs) when tools return semantic names instead of raw UUIDs.
- Evidence: measured — https://www.anthropic.com/engineering/writing-tools-for-agents
```

```markdown
### T5. Error messages as recovery scripts

- Type: augmentation (adds info)
- For humans: dump stack traces, error codes, and technical detail so a developer can investigate and patch code later.
- For agents: return a compact structured error with an error type, minimal context, and an explicit suggested next action; drop the trace.
- Why: error recovery — verbose traces waste context and confuse; actionable guidance lets the agent self-correct without a human in the loop.
- Matters when: validation failures, timeouts, stale references, long autonomous loops prone to repeated-error cycles.
- Testable claim: Agents recover from tool failures more often and with fewer retry loops when errors state a specific corrective action instead of a stack trace.
- Evidence: measured/opinion — https://www.anthropic.com/engineering/writing-tools-for-agents ; https://arxiv.org/html/2512.15374 ; https://www.marthakelly.com/blog/designing-error-messages-for-llms
```

```markdown
### T6. Markdown as the default document format

- Type: representation (same facts, reorganized)
- For humans: publish HTML/PDF with layout, navigation, images, and styling that aid visual reading.
- For agents: serve a clean markdown mirror (e.g. append .md to the URL) stripped of nav, CSS, and scripts.
- Why: token budget + retrieval — models are trained heavily on markdown and parse its heading hierarchy natively; HTML chrome wastes context and hurts chunking.
- Matters when: doc-heavy sites, RAG ingestion, tight context windows, table-bearing pages.
- Testable claim: Agents answer questions over documents more accurately and with fewer tokens when fed clean markdown instead of raw HTML.
- Evidence: measured — https://www.improvingagents.com/blog/best-nested-data-format/ ; https://llmstxt.org/
```

```markdown
### T7. llms.txt navigation manifest

- Type: access (changes how it's fetched)
- For humans: rely on sitemap.xml, site nav, and SEO to help search crawlers enumerate every page.
- For agents: publish a curated markdown file at /llms.txt — H1, blockquote summary, and grouped links to your ~12 most important pages with one-line descriptors, plus an Optional section.
- Why: retrieval/token budget — agents can't ingest a whole site; a curated map points them at high-signal pages instead of crawling bloated HTML.
- Matters when: large documentation sites, inference-time lookups, context-constrained agents.
- Testable claim: Agents locate the correct page faster and with fewer fetches when given a curated llms.txt vs crawling the site or sitemap.
- Evidence: opinion — https://llmstxt.org/ ; https://www.anthropic.com (adopter)
```

```markdown
### T8. Tool-set curation and namespacing

- Type: access (changes how it's fetched)
- For humans: expose the full API surface; developers read reference docs and pick endpoints deliberately.
- For agents: ship a few high-leverage, non-overlapping tools with domain-prefixed names and clear ""when to use / when not"" guidance.
- Why: trust/decision quality — bloated, overlapping tool sets create ambiguous decision points and wrong-tool selection; clear namespaces reduce confusion.
- Matters when: many connectors/MCP servers, overlapping capabilities, name collisions across servers.
- Testable claim: Agents select and invoke the right tool more accurately when tools are few, namespaced, and non-overlapping vs a large flat set.
- Evidence: measured — https://www.anthropic.com/engineering/writing-tools-for-agents ; https://modelcontextprotocol.io/specification/draft/server/tools
```

```markdown
### T9. Entity-centric ""minimum viable data"" products

- Type: augmentation (adds info)
- For humans: organize data by source application/system and join it together later in a warehouse or BI tool.
- For agents: assemble a unified per-entity view (customer, order, device) and expose only the minimum subset the task needs.
- Why: token budget + trust — entity-scoped slices cut irrelevant tokens, speed responses, and limit sensitive-data exposure vs dumping system tables.
- Matters when: enterprise multi-system data, privacy/compliance constraints, entity-lookup tasks.
- Testable claim: Agents answer entity questions more accurately and with lower cost when given a scoped entity view instead of raw cross-system tables.
- Evidence: opinion — https://www.k2view.com/blog/data-for-ai-agents ; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/data-architecture-plan
```

```markdown
### T10. Tabular data as header-once tables, not per-row JSON

- Type: representation (same facts, reorganized)
- For humans: pass tabular data as JSON objects or DB rows that application code parses.
- For agents: serialize tables as markdown/CSV (or TOON) where headers appear once and rows carry only values.
- Why: token budget — per-row JSON repeats every field name, inflating tokens 30–80%; header-once formats cut cost with comparable accuracy on frontier models.
- Matters when: large tables, repeated records, cost-sensitive high-volume calls.
- Testable claim: Agents process large tables with substantially fewer tokens at similar accuracy when data is markdown/CSV instead of per-row JSON.
- Evidence: measured — https://www.improvingagents.com/blog/best-nested-data-format/ ; https://arxiv.org/pdf/2605.29676
```

Two caveats on the evidence. For T10, format accuracy is strongly model-dependent — a large SQL-generation study (9,649 trials) found format barely moved aggregate accuracy while token savings held, so the win is mainly cost, not accuracy. And on chunking generally (relevant to T2), benchmarks conflict: some show semantic/adaptive chunking beating fixed-size by large margins, others (NAACL 2025 Findings) find fixed 200-word chunks match semantic chunking — which is why T2 focuses on the better-replicated _contextual_ augmentation rather than the chunking-boundary method itself.

true
"I'll research this thoroughly across primary sources. Let me run several targeted searches.Let me fetch the key primary sources and search for a few more specific techniques.Here's what current (2026) primary sources and benchmarks say about organizing data specifically for **agent** consumption. I've excluded techniques where the human and agent approaches converge, and ranked by (impact × frequency) × (agent/human divergence). I mark **MEASURED** (benchmark/eval numbers exist) vs **OPINION** (expert/vendor guidance without a headline metric).

## Ranked table

| Rank | Technique                                                    | For humans                              | For agents                                                | Evidence                    |
| ---- | ------------------------------------------------------------ | --------------------------------------- | --------------------------------------------------------- | --------------------------- |
| 1    | Progressive disclosure of tools (code-execution over MCP)    | Load full API reference; read all docs  | Lazy-load only the tool modules needed, call via code     | **Measured**                |
| 2    | Just-in-time, reference-based retrieval + filesystem offload | Pre-fetch and read whole documents      | Store IDs/paths; fetch/grep content on demand             | **Opinion** (some measured) |
| 3    | Token-efficient, paginated, signal-dense tool outputs        | Return everything; let user scroll      | Truncate, paginate, offer concise/detailed modes          | **Opinion**                 |
| 4    | Actionable, prescriptive error messages                      | Terse status code; developer Googles it | Error states what failed, why, and how to fix             | **Opinion**                 |
| 5    | Bounded, namespaced toolsets (not 1:1 API wrappers)          | Expose full API surface                 | Few high-leverage, namespaced, workflow-scoped tools      | **Measured**                |
| 6    | Clean Markdown/semantic text over raw HTML                   | Rendered HTML pages                     | Strip markup to Markdown/plain semantic text              | **Measured** (mixed)        |
| 7    | `llms.txt` + `.md` companion pages                           | Nav-heavy HTML site                     | Curated manifest + clean `.md` mirrors                    | **Opinion**                 |
| 8    | Strict JSON-schema / constrained-decoding outputs            | Prose or loose JSON is fine             | Schema-enforced, machine-parseable structures             | **Measured**                |
| 9    | Compaction/summarization of logs, traces, results            | Keep full raw logs to inspect           | Distill/evict before it hits context                      | **Measured**                |
| 10   | Semantic identifiers over opaque IDs/UUIDs                   | UI maps IDs to names                    | Return human-readable names/enums the model can reason on | **Opinion**                 |

---

### T1. Progressive disclosure of tools (code execution over MCP)

- Type: access
- For humans: publish the complete API/tool reference; a developer reads or searches all of it before coding.
- For agents: don't inject every tool definition upfront. Expose tools as a code API in a sandbox; the agent discovers and loads only the modules it needs and chains calls in code.
- Why: token budget + context rot — loading hundreds of schemas can consume tens of thousands of tokens before the request is even read.
- Matters when: many tools/MCP servers (dozens+), multi-step workflows with large intermediate results.
- Testable claim: Agents complete multi-tool workflows with far fewer tokens when tools are called via code with on-demand loading instead of all definitions loaded upfront.
- Evidence: measured — [Anthropic: 150k→2k tokens, 98.7%](https://www.anthropic.com/engineering/code-execution-with-mcp); [independent 78–99% cuts](https://particula.tech/blog/code-execution-mcp-token-reduction-pattern)

### T2. Just-in-time, reference-based retrieval + filesystem offload

- Type: access
- For humans: pre-fetch and read whole documents/records into a doc or wiki.
- For agents: keep lightweight references (file paths, URLs, IDs, queries) in context and let the agent pull or `grep`/`head`/`tail` content only when needed; offload bulky results to files.
- Why: retrieval + context rot — static inclusion spends tokens regardless of relevance and buries the ""needle""; references preserve structure (hierarchy, timestamps) and avoid stale embeddings.
- Matters when: large corpora, long-horizon runs, bloated tool outputs, multi-hop questions.
- Testable claim: Agents answer more accurately over large corpora when given references to fetch on demand rather than the full content pre-loaded.
- Evidence: opinion (some measured) — [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); [context editing 84% token cut](https://www.digitalapplied.com/blog/context-engineering-agent-reliability-playbook-2026); [filesystem-context skill](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/filesystem-context/SKILL.md)

### T3. Token-efficient, paginated, signal-dense tool outputs

- Type: representation
- For humans: return the complete payload; the user visually skims and ignores noise.
- For agents: default to concise, high-signal responses; paginate or truncate large results with clear limits, strip low-value fields, and offer a ""detailed"" mode only when asked.
- Why: token budget + context rot — every raw result persists in context and dilutes attention on later turns.
- Matters when: tools return large lists/records, long agent loops, high call volume.
- Testable claim: Agents sustain accuracy over long sessions with fewer tokens when tool responses are concise/paginated rather than full raw dumps.
- Evidence: opinion — [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

### T4. Actionable, prescriptive error messages

- Type: augmentation
- For humans: a `400 Bad Request` or `{""error"":""invalid input""}` is fine — the developer reads docs and retries manually.
- For agents: errors must be runtime documentation stating what failed, why (which constraint), and how to fix it (concrete correction), ideally in a structured format (e.g., RFC 7807).
- Why: error recovery — an agent has no docs or UI fallback; opaque errors cause halts or infinite retry loops that burn tokens.
- Matters when: tool-calling workflows, invalid-argument/rate-limit failures, autonomous multi-step runs.
- Testable claim: Agents self-correct and complete tasks more often when tool errors include a fix suggestion instead of a bare status code.
- Evidence: opinion — [Nordic APIs](https://nordicapis.com/designing-api-error-messages-for-ai-agents/); [Error handling for agents](https://medium.com/@spacholski99/error-handling-for-ai-agents-a-different-standard-than-classic-apps-5d7f9096c3cc)

### T5. Bounded, namespaced toolsets (not 1:1 API wrappers)

- Type: representation
- For humans: expose the full API surface; developers pick endpoints using docs.
- For agents: provide a few high-leverage, single-responsibility, clearly namespaced tools scoped to real workflows — not one tool per raw endpoint or one mega-tool with an `action` param.
- Why: trust/selection — too many overlapping tools cause wrong-tool selection and hallucination; too few starve the agent.
- Matters when: large APIs, overlapping tool names, many connected services.
- Testable claim: Agents select and invoke tools more accurately with a small, namespaced, workflow-scoped toolset than with a 1:1 mapping of every API endpoint.
- Evidence: measured — [AWS: too-many/too-few tools](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy.html); [Anthropic namespacing](https://www.anthropic.com/engineering/writing-tools-for-agents)

### T6. Clean Markdown / semantic text over raw HTML

- Type: representation
- For humans: serve rendered HTML with layout, nav, and styling.
- For agents: strip markup to clean Markdown or plain semantic text (headings, lists, tables) so tokens carry meaning, not `<div>` noise.
- Why: token budget + retrieval — HTML wrapper tags/attributes inflate tokens and dilute signal, hurting RAG chunking.
- Matters when: web pages/scraped content, RAG pipelines, large documents. (Caveat: one agent-memory benchmark found well-structured HTML beat Markdown on multi-hop/temporal recall.)
- Testable claim: Agents extract/summarize web content with 30–70% fewer tokens and higher RAG accuracy from Markdown than from equivalent raw HTML.
- Evidence: measured (mixed) — [+35% RAG, 20–30% token cut](https://www.searchcans.com/blog/markdown-vs-html-llm-context-optimization-2026/); [67% token cut](https://web2md.org/blog/markdown-vs-html-for-llm); counter: [HTML wins on agent memory](https://www.byterover.dev/blog/html-vs-markdown-for-agent-memory-a-full-scale-benchmark-on-accuracy-latency-and-cost)

### T7. `llms.txt` + `.md` companion pages

- Type: access
- For humans: a navigable HTML site with menus, search, and ads.
- For agents: publish a root `/llms.txt` Markdown manifest (H1 name, blockquote summary, curated link lists) plus clean `.md` mirrors of key pages at the same URL + `.md`.
- Why: retrieval + token budget — gives agents an authoritative, parseable entry point instead of crawling and de-noising full HTML.
- Matters when: docs/developer portals, product/business sites agents must cite at inference time.
- Testable claim: Agents retrieve correct, current site facts more reliably from an `llms.txt`/`.md` manifest than from crawling the rendered HTML site.
- Evidence: opinion — [llmstxt.org proposal & spec](https://llmstxt.org/)

### T8. Strict JSON-schema / constrained-decoding outputs

- Type: representation
- For humans: prose, loose JSON, or partially valid structures are acceptable — people repair them by eye.
- For agents: enforce a strict JSON Schema (constrained decoding / strict mode) for structured data and tool I/O so every field, type, and enum is guaranteed parseable.
- Why: trust + error recovery — one missing key, wrong type, or ""Here's the response:"" preamble breaks the parser and stalls the loop.
- Matters when: data extraction, tool arguments/returns, multi-step pipelines feeding deterministic code.
- Testable claim: Agents produce and consume downstream-parseable structures far more reliably under strict schema enforcement than under prompt-only JSON.
- Evidence: measured — [OpenAI: 100% vs <40% schema adherence](https://openai.com/index/introducing-structured-outputs-in-the-api/)

### T9. Compaction / summarization of logs, traces, and results

- Type: representation
- For humans: retain full raw logs, telemetry, and traces to scroll and inspect later.
- For agents: summarize or evict verbose logs/metrics/intermediate results as the window fills, keeping a distilled summary plus recent artifacts.
- Why: context rot — accumulated raw output degrades recall and reasoning over long runs even in million-token windows.
- Matters when: long-horizon agents, verbose telemetry/logs, 50+ turn sessions.
- Testable claim: Agents maintain higher task accuracy over long runs when logs/results are compacted rather than retained raw in context.
- Evidence: measured — [context editing + memory: +39% lift, 84% token cut](https://www.digitalapplied.com/blog/context-engineering-agent-reliability-playbook-2026); [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### T10. Semantic identifiers over opaque IDs/UUIDs

- Type: representation
- For humans: return raw UUIDs/enums; the UI maps them to readable labels.
- For agents: return human-readable names, natural-language enums, and descriptive fields (or both name + ID) so the model can reason over values directly.
- Why: trust — agents can't dereference an opaque `id: 8f3a...` through a UI, and cryptic codes invite hallucinated mappings.
- Matters when: tool outputs with foreign keys/status codes, records the agent must filter or cross-reference.
- Testable claim: Agents filter and cross-reference records more accurately when returned data uses semantic names/enums instead of opaque IDs.
- Evidence: opinion — [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

---

**Notes on evidence quality:** The strongest _measured_ claims are T1 (code execution over MCP), T8 (structured outputs), and the token-reduction figures in T6/T9. T6 is genuinely contested — Markdown wins on token cost and simple extraction, but a full-scale agent-memory benchmark found HTML more accurate on multi-hop/temporal recall, so treat ""always use Markdown"" as situational. T2, T3, T4, T7, and T10 rest mainly on vendor/expert guidance (Anthropic, MCP, API-design practitioners) rather than head-to-head benchmarks. [\[byterover.dev\]](https://www.byterover.dev/blog/html-vs-markdown-for-agent-memory-a-full-scale-benchmark-on-accuracy-latency-and-cost)

Want me to (a) turn this into a page/canvas you can edit, (b) add a ""media"" technique (transcripts/alt-text/structured descriptions instead of raw binaries), or (c) expand the evidence column with the specific benchmark datasets used?
true
"I'll research current best practices for organizing data for AI agents. Let me search primary sources.Let me search for more primary/technical sources on specific techniques.Now let me search for Anthropic/OpenAI primary sources on tool design and context engineering for agents.Strong primary sources. Let me get more on tool outputs, data formats (markdown vs JSON accuracy), and RAG/chunking for agents.I have strong data-format evidence. Let me get a couple more on tool outputs/IDs, error messages for recovery, and semantic layer / natural-language identifiers.I have enough now. Let me do two more targeted searches: one on progressive disclosure / filesystem-as-context (loading data lazily), and one on chunking/document structure for retrieval.I now have comprehensive coverage across all the technique areas. Let me compose the final answer.

---

## Ranked table

| Rank | Technique                                               | For humans                                    | For agents                                                                                 | Evidence                                                          |
| ---- | ------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| 1    | Just-in-time references over pre-loaded data            | Pre-fetch & assemble everything into one view | Hand out lightweight IDs (paths, queries, URLs); agent pulls at runtime via grep/head/tail | Opinion (Anthropic), partial measured (agentic-search benchmarks) |
| 2    | Semantic identifiers, not UUIDs                         | Opaque UUIDs fine (DB joins)                  | Return names/slugs; resolve cryptic IDs to language                                        | Measured (Anthropic internal)                                     |
| 3    | Markdown/YAML over JSON/CSV for consumption             | JSON/CSV for parsers & spreadsheets           | Serialize tables/docs as Markdown-KV or YAML                                               | Measured (multiple benchmarks)                                    |
| 4    | Token-budgeted tool outputs (paginate/filter/truncate)  | Return full result sets, scroll UI            | Cap responses (~25k tok), default filters, signal truncation                               | Opinion (Anthropic) + Claude Code practice                        |
| 5    | Actionable errors as recovery instructions              | Stack traces + error codes for devs           | Plain-language errors naming the fix / correct input shape                                 | Opinion (Anthropic)                                               |
| 6    | High-signal fields only, verbosity toggle               | Dense metadata dashboards                     | Strip low-signal fields; `response_format: concise\|detailed`                              | Opinion (Anthropic) + practitioner                                |
| 7    | Curated AI index of a corpus (llms.txt / data products) | Nav menus, sitemaps, search bars              | Root Markdown index → clean `.md` mirrors; packaged data products                          | Opinion + some measured (token/accuracy)                          |
| 8    | Heading-based chunk boundaries for retrieval            | Chunk by page/paragraph length                | Chunk on Markdown headings; keep semantic units whole                                      | Measured (retrieval-accuracy studies)                             |
| 9    | Tools accept descriptive input, resolve internally      | Forms demand exact IDs/codes                  | Accept ""downtown branch""; backend fuzzy-resolves, disambiguates                          | Opinion (practitioner/academic)                                   |
| 10   | Human/machine coupled to same source                    | Separate machine feed (API) vs human page     | One source rendered many ways; no drift between them                                       | Opinion (academic)                                                |

---

### T1. Just-in-time references over pre-loaded data

- Type: access
- For humans: pre-fetch and assemble all plausibly-relevant data into a single view up front.
- For agents: hand out lightweight identifiers (file paths, stored queries, URLs); let the agent load data at runtime via tools like grep, head, and tail.
- Why: token budget and context rot — preloading everything degrades output; on-demand retrieval keeps the window small and lets the agent write targeted queries over large stores.
- Matters when: corpus is large, multi-hop, or exceeds context; long-running tasks where relevance can't be predicted in advance.
- Testable claim: Agents answer large-corpus questions more accurately and with fewer tokens when given retrieval tools plus IDs instead of a pre-stuffed context.
- Evidence: opinion + partial measured — [anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [morphllm.com/agentic-search](https://www.morphllm.com/agentic-search)

### T2. Semantic identifiers, not UUIDs

- Type: representation
- For humans: opaque UUIDs and numeric codes are fine — humans copy-paste and systems join on them.
- For agents: return human-readable names/slugs; resolve arbitrary UUIDs to meaningful language (or a 0-indexed scheme) in tool outputs.
- Why: trust and retrieval precision — agents reason far better over natural-language identifiers; cryptic strings induce hallucination and wasted lookup calls.
- Matters when: outputs feed downstream tool calls, or the agent must reference/select among many returned items.
- Testable claim: Agents complete retrieval/reference tasks more accurately when tool outputs use semantic names instead of raw UUIDs.
- Evidence: measured (Anthropic internal) — [anthropic.com/engineering/writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

### T3. Markdown/YAML over JSON/CSV for consumption

- Type: representation
- For humans: JSON and CSV are the defaults — machine-parseable, spreadsheet-friendly.
- For agents: serialize tables and documents as Markdown key-value or YAML when the data is meant to be _read and reasoned over_, not parsed.
- Why: token efficiency and native register — models trained heavily on Markdown; JSON/XML syntax bloat wastes 30–80% more tokens and can suppress flexible reasoning.
- Matters when: feeding tabular or nested data into context for comprehension/synthesis rather than for a strict parser.
- Testable claim: Agents answer table-comprehension questions more accurately when data is Markdown-KV instead of CSV (measured ~61% vs ~44%).
- Evidence: measured — [improvingagents.com/blog/best-input-data-format-for-llms](https://www.improvingagents.com/blog/best-input-data-format-for-llms/), [improvingagents.com/blog/best-nested-data-format](https://www.improvingagents.com/blog/best-nested-data-format/)

### T4. Token-budgeted tool outputs

- Type: access
- For humans: return complete result sets; humans scroll, sort, and page through a UI.
- For agents: cap responses (Claude Code defaults ~25k tokens), ship sensible default filters and pagination, and explicitly signal when output was truncated.
- Why: token budget and error recovery — unbounded outputs blow the context window; truncation messages steer agents toward narrower, cheaper follow-up queries.
- Matters when: tools can return large or open-ended result sets (logs, search, list endpoints).
- Testable claim: Agents complete multi-step tasks with fewer tokens and fewer failures when tool outputs are paginated/truncated with guidance versus returned in full.
- Evidence: opinion (+ Claude Code practice) — [anthropic.com/engineering/writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

### T5. Actionable errors as recovery instructions

- Type: augmentation
- For humans: stack traces, tracebacks, and numeric error codes aimed at a developer debugging later.
- For agents: return plain-language errors that name the specific fix — the correct input format, the missing parameter, the valid enum value.
- Why: error recovery — agents can self-correct within the loop when the error tells them _what to do next_; opaque codes cause retries or dead ends.
- Matters when: input validation fails, or tools have strict/ambiguous input formats the agent must learn on the fly.
- Testable claim: Agents recover from failed tool calls at a higher rate when errors state the corrective action instead of returning a code/traceback.
- Evidence: opinion — [anthropic.com/engineering/writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

### T6. High-signal fields only, with a verbosity toggle

- Type: representation
- For humans: rich, dense metadata is useful — dashboards surface everything for scanning.
- For agents: strip low-signal fields (mime_type, 256px_image_url, internal flags); expose a `response_format` parameter (concise vs detailed).
- Why: token budget and signal-to-noise — every irrelevant field competes for attention and context; a toggle lets the agent pull detail only when the task needs it.
- Matters when: records carry many fields but only a few inform the next action; token pressure is high.
- Testable claim: Agents pick correct next actions more often and cheaper when tool responses omit low-signal fields versus returning full metadata.
- Evidence: opinion + practitioner — [platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools), [blog.agentailor.com/posts/writing-tools-for-ai-agents](https://blog.agentailor.com/posts/writing-tools-for-ai-agents)

### T7. Curated AI index of a corpus

- Type: augmentation
- For humans: nav menus, XML sitemaps, and a search bar; every page listed.
- For agents: a root Markdown index (llms.txt) linking clean `.md` mirrors of key pages — curated, not exhaustive; or packaged ""data products"" with metadata and usage guides.
- Why: token budget and retrieval — a small curated index lets an agent orient for ~2–10k tokens instead of parsing HTML div-soup, and controls the ground-truth narrative.
- Matters when: large documentation sites/catalogs an agent must navigate in real time. (Note: no major LLM confirms auto-reading llms.txt; value today is mainly in coding-agent/retrieval tooling.)
- Testable claim: Agents fetch the right page with fewer tokens when given a curated Markdown index plus `.md` versions instead of raw HTML.
- Evidence: opinion + some measured — [mintlify.com/blog/real-llms-txt-examples](https://www.mintlify.com/blog/real-llms-txt-examples), [derivatex.agency/blog/llms-txt-guide](https://derivatex.agency/blog/llms-txt-guide/)

### T8. Heading-based chunk boundaries for retrieval

- Type: representation
- For humans: chunk documents by fixed page or paragraph length for display/storage.
- For agents: chunk on Markdown heading boundaries so each retrieved unit is a self-contained semantic section, not a mid-thought slice.
- Why: retrieval — heading-aligned chunks preserve meaning and context, improving what the agent gets back per query and reducing broken tables/split records.
- Matters when: RAG or embedding-based retrieval over structured docs; large tables that fixed-length chunking would fracture.
- Testable claim: Agents retrieve more relevant passages when documents are chunked on Markdown headings versus fixed-length/unstructured chunking (reported up to ~35% lift).
- Evidence: measured — [tianpan.co/blog/2026-05-07-context-format-decision-agent-reasoning-json-markdown-plain-text](https://tianpan.co/blog/2026-05-07-context-format-decision-agent-reasoning-json-markdown-plain-text)

### T9. Tools accept descriptive input, resolve internally

- Type: access
- For humans: forms and APIs demand exact identifiers — store ID, category code, user UUID.
- For agents: let tools take natural-language input (""downtown branch""), then fuzzy-resolve on the backend and return a disambiguation prompt rather than a 404.
- Why: trust — shifts exact-matching off the agent's context window (high hallucination risk) onto deterministic backend logic where it's reliable.
- Matters when: agents start from a natural-language goal and don't hold exact keys; ambiguous references are common.
- Testable claim: Agents complete lookup/create tasks more accurately when tools resolve descriptive input internally instead of requiring exact IDs.
- Evidence: opinion (practitioner/academic) — [arxiv.org/html/2605.10555](https://arxiv.org/html/2605.10555)

### T10. Couple human and machine views to one source

- Type: representation
- For humans: a rendered page; machines get a separate API feed or data pipeline.
- For agents: serve one underlying source rendered multiple ways (HTML for humans, Markdown/JSON-LD for agents) so both see identical facts.
- Why: trust and faithfulness — decoupled feeds silently drift or get manipulated to steer AI outputs with no human-visible accountability; coupling prevents that.
- Matters when: agents consume public/enterprise content that also has a human-facing version and correctness/consistency matters.
- Testable claim: Agent answers stay consistent with the human-visible content when both derive from one source instead of a separate machine feed.
- Evidence: opinion (academic) — [arxiv.org/pdf/2603.10700](https://arxiv.org/pdf/2603.10700)

true
"| Rank | Technique | For humans | For agents | Evidence: measured/opinion |
|---:|---|---|---|---|
| 1 | Progressive, query-first access | Browse menus or open whole collections | Search/list/filter first; fetch bounded details on demand | Measured |
| 2 | Schema-constrained interfaces | Flexible prose, tables, loosely shaped JSON | Strict typed inputs and outputs with stable identifiers | Measured |
| 3 | Contextual, self-contained chunks | Preserve complete chapters and documents | Retrieve semantic chunks carrying their missing context | Measured |
| 4 | Semantic layer over tables | Schema plus a separate data dictionary | Task-scoped schema with meanings, relationships, units, and examples | Measured |
| 5 | Clean canonical derivatives | Visually designed HTML, PDFs, slides | Structured Markdown/JSON retaining semantic layout | Opinion |
| 6 | Intent-distinct tool definitions | Generic CRUD APIs with browsable manuals | Narrow, distinguishable actions with precise usage examples | Measured |
| 7 | Recoverable errors and telemetry | Human-readable log streams and dashboards | Correlated events with diagnosis and permitted recovery actions | Measured |
| 8 | Structural maps and relationship graphs | Navigate folders and files manually | Compact symbol, dependency, entity, and link maps | Measured |
| 9 | Atomic provenance and freshness | Footnotes, dates, and changelogs elsewhere | Provenance travels with every retrieved unit and result | Measured |
| 10 | Dual multimodal representations | Consume the original image, audio, or video | Original media plus synchronized machine-readable derivatives | Measured |

### T1. Progressive, query-first access

- Type: access (changes how it's fetched)
- For humans: Browse folders, menus, dashboards, or entire manuals.
- For agents: Expose compact catalogs plus search, filtering, pagination, and bounded read operations; load full records only when selected.
- Why: Avoids context rot, irrelevant-tool competition, latency, and repeated transmission of unused definitions.
- Matters when: Collections or tool catalogs exceed a few dozen items, or distractor density is high.
- Testable claim: Agents complete the same tool tasks with fewer input tokens when definitions are retrieved on demand instead of supplied upfront.
- Evidence: measured — [OpenAI: 47% fewer tokens at equal accuracy](https://openai.com/index/introducing-gpt-5-4/), [long-context degradation](https://www.trychroma.com/research/context-rot), [MCP resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources)

### T2. Schema-constrained interfaces

- Type: representation (same facts, reorganized)
- For humans: Accept flexible prose, CSV exports, dashboards, or loosely shaped JSON.
- For agents: Use strict JSON Schemas for inputs and outputs, with required fields, enums, types, units, null semantics, and stable IDs.
- Why: Constrained decoding and validation prevent malformed calls, ambiguous values, and downstream parser failures.
- Matters when: Agents chain tools, mutate state, or pass outputs directly into another operation.
- Testable claim: Agents produce more valid tool calls when arguments must conform to a strict schema instead of an example-only JSON format.
- Evidence: measured — [OpenAI: 100% versus under 40% schema adherence](https://openai.com/index/introducing-structured-outputs-in-the-api/), [MCP output schemas](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)

### T3. Contextual, self-contained chunks

- Type: augmentation (adds info)
- For humans: Keep prose in complete documents whose surrounding pages supply context.
- For agents: Split on semantic boundaries and prepend compact context such as document title, heading path, subject, period, and parent identity.
- Why: Isolated passages often omit the entity, timeframe, or purpose needed for retrieval and interpretation.
- Matters when: Documents repeat terminology, chunks contain pronouns, or retrieval spans many similar sources.
- Testable claim: Agents retrieve the correct passage more often when each chunk contains document-level context instead of raw local text alone.
- Evidence: measured — [Anthropic: 49% fewer retrieval failures, 67% with reranking](https://www.anthropic.com/engineering/contextual-retrieval), [Claude implementation guide](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide)

### T4. Semantic layer over tables

- Type: augmentation (adds info)
- For humans: Present normalized tables and place business meanings in a separate wiki or analyst documentation.
- For agents: Supply only relevant schema portions, enriched with column meanings, synonyms, PK/FK relationships, join paths, units, constraints, and representative values.
- Why: Agents must map natural-language concepts onto opaque identifiers without exhausting context on an enterprise-wide schema.
- Matters when: Schemas have hundreds of columns, cryptic names, multiple dialects, or non-obvious joins.
- Testable claim: Agents execute more correct queries when relevant columns have semantic descriptions and relationships instead of names and types alone.
- Evidence: measured — [column-description study](https://openreview.net/pdf?id=hA0b6MUbSF), [Spider 2.0](https://spider2-sql.github.io/), [extractive schema linking](https://arxiv.org/abs/2501.17174)

### T5. Clean canonical derivatives

- Type: representation (same facts, reorganized)
- For humans: Optimize HTML, PDFs, and slides for visual navigation, branding, and page layout.
- For agents: Publish synchronized Markdown or structured JSON that removes chrome while preserving headings, lists, code, tables, formulas, reading order, pages, and anchors.
- Why: Presentation markup consumes tokens, while naive text extraction destroys structural meaning.
- Matters when: Sources contain complex PDFs, navigation-heavy sites, multicolumn layouts, tables, or formulas.
- Testable claim: Agents answer document questions using fewer tokens when given structure-preserving Markdown instead of raw HTML or flattened PDF text.
- Evidence: opinion — [IBM Docling](https://research.ibm.com/publications/docling-technical-report), [OmniDocBench](https://arxiv.org/abs/2412.07626), [llms.txt proposal](https://llmstxt.org/)

### T6. Intent-distinct tool definitions

- Type: augmentation (adds info)
- For humans: Offer generic CRUD endpoints backed by a browsable reference manual.
- For agents: Use narrow intent-bearing names, explain when and when not to call each tool, distinguish overlapping tools, and include realistic argument and result examples.
- Why: Tool selection is semantic classification; similar names and dispersed documentation create wrong-tool and wrong-parameter errors.
- Matters when: A catalog contains overlapping search, update, lookup, or execution operations.
- Testable claim: Agents select the correct operation more often when tool names and descriptions encode user intent instead of generic CRUD verbs.
- Evidence: measured — [controlled API-naming benchmark](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6460766), [OpenAI agent guidance](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

### T7. Recoverable errors and telemetry

- Type: augmentation (adds info)
- For humans: Emit prose errors and large chronological log streams intended for dashboard inspection.
- For agents: Return structured error codes, retryability, failed constraints, partial state, corrective hints, and allowed next actions; correlate events with trace, span, tool, and entity IDs.
- Why: Agents otherwise retry blindly, trust corrupted results, or lose the failure’s causal location.
- Matters when: Workflows are multi-step, dependencies are unreliable, or actions have side effects.
- Testable claim: Agents recover more failed workflows when errors include targeted recovery fields instead of an exception message alone.
- Evidence: measured — [ToolBench-X](https://arxiv.org/abs/2606.25819), [PROBE recovery results](https://arxiv.org/abs/2605.08717), [OpenTelemetry correlation](https://opentelemetry.io/docs/specs/otel/logs/)

### T8. Structural maps and relationship graphs

- Type: augmentation (adds info)
- For humans: Explore directory trees, follow links, and read files until the architecture becomes clear.
- For agents: Generate compact maps of symbols, signatures, imports, callers, dependencies, entities, and source links, with operations for expanding selected nodes.
- Why: Relationships needed for multi-hop reasoning are expensive to rediscover through repeated file reads and lexical searches.
- Matters when: Repositories or corpora are large, interconnected, and unfamiliar.
- Testable claim: Agents localize relevant code with fewer tokens when given a dependency-aware symbol map instead of only a filesystem tree.
- Evidence: measured — [Codebase-Memory evaluation](https://www.alphaxiv.org/abs/2603.27277), [SWE-Explore](https://huggingface.co/papers/2606.07297), [Aider repository maps](https://aider.chat/docs/repomap.html)

### T9. Atomic provenance and freshness

- Type: augmentation (adds info)
- For humans: Put citations, update dates, ownership, and version history in footnotes or separate changelogs.
- For agents: Attach canonical ID, source URI, exact span, content hash, version, timestamp, authority, and validity status to every record, chunk, and tool result.
- Why: Metadata must survive retrieval and transformation for conflict resolution, entity binding, freshness filtering, and verification.
- Matters when: Sources conflict, records change, similarly named entities exist, or actions target real accounts and documents.
- Testable claim: Agents make fewer stale or wrong-entity decisions when provenance and version metadata accompany each result instead of being stored separately.
- Evidence: measured — [entity-binding evaluation](https://papers.cool/arxiv/2606.30531), [citation-faithfulness study](https://arxiv.org/abs/2412.18004), [GraphRAG provenance model](https://microsoft.github.io/graphrag/index/default_dataflow/)

### T10. Dual multimodal representations

- Type: augmentation (adds info)
- For humans: Consume the original image, chart, recording, or video through a visual or audio player.
- For agents: Keep the original media and add linked OCR, transcripts, captions, table data, formulas, timestamps, bounding boxes, scene boundaries, and confidence values.
- Why: Text derivatives enable retrieval and exact references; original media preserves evidence that extraction loses.
- Matters when: Answers depend on layout, charts, screenshots, speech, spatial relationships, or brief audiovisual events.
- Testable claim: Agents answer multimodal questions more accurately when searchable derivatives remain linked to original evidence than when given only media or only extracted text.
  true
  "# Organizing Data for AI Agents — Top 10 Techniques (2026)

Research on current best practices for organizing **data for AI agents to consume**, as opposed to humans. ""Data"" spans structured data (tables, JSON, schemas), documents (markdown, PDFs, web pages), code, media, folder/site organization, tool definitions & docs, tool outputs, errors, logs, metrics, and traces. Agent-harness artifacts (system prompts, AGENTS.md, SKILL.md, memory, permissions, hooks) are excluded.

Ranked by **(impact × how often the situation occurs) × (how differently you'd do it for agents vs humans)**. Techniques where the human and agent approach essentially match are skipped.

Evidence is marked **measured** (controlled benchmarks/evals) vs **opinion** (expert guidance from primary sources).

## Ranked table

| Rank | Technique                                         | For humans                                | For agents                                               | Evidence           |
| ---- | ------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------- | ------------------ |
| T1   | Focused context, not comprehensive                | Give complete references ""just in case"" | Feed only the relevant slice; strip distractors          | measured           |
| T2   | Just-in-time references over pre-loading          | Lay everything out on one page            | Hand IDs/paths/links; fetch on demand                    | measured + opinion |
| T3   | Code execution over tool-call chaining            | Click through UIs / call APIs one by one  | Let the model write code that calls tools & filters data | measured           |
| T4   | Task-shaped, few, namespaced tools                | Granular, complete 1:1 API surface        | Consolidated workflow tools; <~20, prefixed              | measured           |
| T5   | High-signal fields; semantic IDs                  | Return full records incl. UUIDs           | Trim to actionable fields; resolve UUIDs to names        | measured           |
| T6   | Token-budgeted outputs (paginate/filter/truncate) | Return full result sets                   | Cap + default filters + in-band steering                 | opinion + measured |
| T7   | Actionable error messages                         | Stack traces / error codes                | Prose telling the agent what to do next                  | opinion            |
| T8   | LLM-ready docs (llms.txt / .md)                   | HTML pages with nav, ads, JS              | Curated markdown index + `.md` mirrors                   | opinion            |
| T9   | Structure as navigable metadata                   | Rely on README/prose to explain layout    | Encode meaning in paths, filenames, timestamps           | opinion            |
| T10  | Model-tuned serialization                         | Pretty HTML tables / rich nested JSON     | Training-aligned format; schema-constrained              | opinion            |

## Cards

### T1. Focused context, not comprehensive

- Type: representation (same facts, reorganized)
- For humans: give the complete document/dataset so a person can scan for what they need ""just in case.""
- For agents: pre-filter to only the relevant slice; actively remove topically-similar-but-wrong ""distractor"" content.
- Why: retrieval — irrelevant tokens force the model to do retrieval + reasoning at once, and accuracy degrades (""context rot"") as input grows; distractors compound and drive confident hallucinations.
- Matters when: large corpora, high distractor density, long chat/session history, multi-hop questions.
- Testable claim: Agents answer questions more accurately from a ~300-token focused input than from the same answer buried in a 113k-token full input.
- Evidence: measured — [Chroma Context Rot](https://www.trychroma.com/research/context-rot), [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### T2. Just-in-time references over pre-loading

- Type: access (changes how it's fetched)
- For humans: assemble everything relevant onto one page/report up front so nothing requires a second lookup.
- For agents: store lightweight identifiers (file paths, query handles, URLs) and let the agent load data at runtime with tools.
- Why: token budget + retrieval — keeping only references frees the attention budget; metadata (path, name, timestamp) lets the agent progressively disclose just what each step needs.
- Matters when: corpus far exceeds the context window, dynamic/changing data, long-horizon tasks.
- Testable claim: Agents complete large-corpus tasks with fewer tokens (and less context rot) when given references to fetch on demand instead of the full corpus preloaded.
- Evidence: measured + opinion — [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [Anthropic code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)

### T3. Code execution over tool-call chaining

- Type: access (changes how it's fetched)
- For humans: operate systems through GUIs or by calling one API endpoint at a time.
- For agents: expose tools as a code API (e.g., files on a filesystem) so the agent writes code that calls tools, loops, and filters results before anything returns to context.
- Why: token budget — intermediate results (full transcripts, 10k-row sheets) never pass through the model; only the filtered output does.
- Matters when: many connected tools, large intermediate payloads, multi-step data pipelines.
- Testable claim: Agents complete multi-tool data tasks using far fewer tokens when writing code against tools versus chaining direct tool calls (Anthropic reports 150k→2k tokens, 98.7%).
- Evidence: measured — [Anthropic code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp), [Cloudflare Code Mode](https://blog.cloudflare.com/code-mode/)

### T4. Task-shaped, few, namespaced tools

- Type: representation (same facts, reorganized)
- For humans: expose a granular, complete API where each endpoint maps 1:1 to an operation.
- For agents: build a small number of consolidated, workflow-level tools (e.g., `get_customer_context` instead of three list calls), grouped under service/resource prefixes.
- Why: retrieval + trust — fewer, clearly-bounded tools reduce wrong-tool selection; consolidation moves intermediate work out of the model's context.
- Matters when: dozens of MCP servers / hundreds of tools, overlapping functionality.
- Testable claim: Agents pick and use tools more accurately with a curated, namespaced set (<~20 up front) than with a full 1:1 wrapper of the underlying API.
- Evidence: measured — [Anthropic writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents), [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling)

### T5. High-signal fields and semantic IDs

- Type: representation (same facts, reorganized)
- For humans: return complete records, including technical identifiers (UUIDs, mime types, pixel URLs) for flexibility.
- For agents: return only fields that inform the next action (`name`, `file_type`), and resolve opaque UUIDs to human-readable names or simple 0-indexed IDs.
- Why: trust + token budget — models handle natural-language identifiers far better than cryptic strings, cutting hallucinations; low-value fields waste attention.
- Matters when: retrieval tasks, records with many technical fields, chained lookups.
- Testable claim: Agents retrieve and reference the right entities more precisely when UUIDs are resolved to semantic names instead of raw alphanumeric IDs.
- Evidence: measured — [Anthropic writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

### T6. Token-budgeted tool outputs

- Type: access (changes how it's fetched)
- For humans: return the full result set; a UI paginates visually and the person scrolls.
- For agents: enforce sensible default limits with built-in pagination, range selection, filtering, and truncation — plus in-band text steering toward narrower queries.
- Why: token budget — unbounded outputs blow the context window and can exceed limits; defaults keep responses within a fixed budget (Claude Code caps tool responses at 25k tokens).
- Matters when: logs, large tables/spreadsheets, search over big corpora, metrics dumps.
- Testable claim: Agents finish log/table tasks with fewer tokens and fewer failures when tools return filtered/paginated slices with defaults instead of full result sets.
- Evidence: opinion + measured — [Anthropic writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

### T7. Actionable error messages

- Type: representation (same facts, reorganized)
- For humans: surface a stack trace or an error code that a developer can look up and debug.
- For agents: return plain-language errors that state what went wrong and the specific corrective action (e.g., ""use pagination,"" ""date must be YYYY-MM-DD,"" correct example input).
- Why: error recovery — agents can't consult external docs mid-loop; the message itself must carry the fix so the next attempt succeeds.
- Matters when: validation failures, rate limits, truncation, malformed tool inputs.
- Testable claim: Agents recover from tool errors on the next attempt more often when errors give actionable guidance instead of opaque codes or tracebacks.
- Evidence: opinion — [Anthropic writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

### T8. LLM-ready docs (llms.txt and .md mirrors)

- Type: augmentation (adds info)
- For humans: publish HTML pages with navigation, ads, and JavaScript, plus a sitemap.xml for crawlers.
- For agents: add a root `/llms.txt` — a curated markdown index with a summary and annotated links — and serve clean `.md` versions of pages at the same URL + `.md`.
- Why: retrieval + token budget — models can't reliably strip chrome from HTML; a concise curated index fits context and points to expert-level detail.
- Matters when: agents consume your docs/API/site; large sites too big to fit in context.
- Testable claim: Agents answer questions about a site more accurately from its llms.txt + .md pages than from crawled rendered HTML.
- Evidence: opinion — [llms.txt spec](https://llmstxt.org/)

### T9. Structure as navigable metadata

- Type: augmentation (adds info)
- For humans: explain the repo/data layout in a README or onboarding doc that people read once.
- For agents: encode meaning directly into folder hierarchy, filenames, and timestamps so the agent infers purpose and relevance while navigating (e.g., `test_utils.py` in `tests/` vs `src/core_logic/`).
- Why: retrieval — agents assemble understanding layer-by-layer from these signals during just-in-time exploration, without loading everything.
- Matters when: large codebases/filesystems, incremental exploration, deciding what to open next.
- Testable claim: Agents locate the right files faster and with fewer wrong opens when naming/foldering carry semantic signals versus flat or opaque names.
- Evidence: opinion — [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### T10. Model-tuned serialization

- Type: representation (same facts, reorganized)
- For humans: present data as styled HTML tables or richly nested JSON optimized for visual scanning and type-completeness.
- For agents: choose the format the model parses best (often Markdown or XML tables), flatten deep nesting, and constrain outputs with strict schemas/enums so invalid states can't occur.
- Why: trust — models predict next-tokens best on formats resembling training data; schema constraints eliminate malformed structured output.
- Matters when: tables/JSON payloads, structured extraction, tool inputs/outputs.
- Testable claim: Agents parse and act on the same data more accurately when serialized in a model-preferred format (e.g., Markdown/XML) than in deeply nested JSON.
- Evidence: opinion — [Anthropic writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents), [OpenAI function calling (strict mode)](https://developers.openai.com/api/docs/guides/function-calling)

## Notes on evidence strength

- **T1 and T3** rest on controlled measurements (Chroma's 18-model study; Anthropic's token-reduction and Slack/Asana held-out evals).
- **T4/T5** cite Anthropic's measured tool-eval improvements.
- **T6–T10** are primarily expert guidance from Anthropic / OpenAI / llms.txt with partial measured support.
- Excluded: harness artifacts (system prompts, memory, SKILL.md) and techniques where the human and agent approach essentially match (e.g., ""write clear descriptions,"" few-shot examples).

## Primary sources

- Anthropic — [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- Anthropic — [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Anthropic — [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- Chroma — [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot)
- [llms.txt specification](https://llmstxt.org/)
- OpenAI — [Function calling guide](https://developers.openai.com/api/docs/guides/function-calling)
- Cloudflare — [Code Mode](https://blog.cloudflare.com/code-mode/)
  true
  Claude Opus 4.8
  "Notes on method: All sources are primary where possible — Anthropic engineering blogs, the MCP code-execution guide, the llms.txt spec, OpenAI structured-outputs docs, the TOON benchmark paper, Cloudflare's markdown-for-agents, and the OpenTelemetry GenAI conventions. I skipped techniques where the human and agent approach are the same (e.g., ""write clear docs,"" ""validate inputs""). Strongest measured evidence: code-execution token reduction (98.7%), Markdown-vs-HTML (68–87% fewer tokens; 60.7% vs 53.6% table extraction), TOON (~40% fewer tokens at equal/better accuracy), and Anthropic's Slack tool example (~⅓ tokens). The most opinion-driven: error-as-recovery-guidance and agent-parseable telemetry.

Ranked table
Evidence
measured + opinion
measured
measured
measured
measured
measured + opinion
opinion
measured + opinion
measured + opinion
opinion + standard
Cards
T1. Just-in-time agentic retrieval
Type: access (changes how it's fetched)
For humans: build a search portal or precomputed vector/RAG index over the whole corpus.
For agents: expose navigation tools (grep, glob, file paths, stored queries, URLs) and lightweight identifiers; let the agent load only what it needs at runtime, optionally hybridized with a little up-front context.
Why: retrieval, token budget, freshness — avoids stale embeddings and keeps context full of high-signal tokens the agent chose.
Matters when: large/changing corpora, multi-hop questions, high distractor density.
Testable claim: Agents answer multi-hop questions at comparable accuracy using keyword/file navigation instead of a vector store, with no index to maintain.
Evidence: measured + opinion — Anthropic: effective context engineering; Retrieval benchmarking: agentic vs vanilla
T2. Progressive tool disclosure via code execution
Type: access (changes how it's fetched)
For humans: publish the full API catalog and every tool definition up front, with verbose reference docs.
For agents: present tools as code APIs/files loaded on demand; let the agent write code that calls them, filters large results in the execution environment, and spills intermediate data to files instead of the context window.
Why: token budget — tool definitions and intermediate results otherwise pass through context repeatedly.
Matters when: many tools (50+), large intermediate payloads, multi-step workflows.
Testable claim: Agents complete multi-tool workflows using far fewer tokens when tools are code APIs plus filesystem results than when all defs/results stream through context.
Evidence: measured — Anthropic: code execution with MCP (150k→2k tokens, 98.7%); MCP discussion #629
T3. Concise, semantic tool outputs
Type: representation (same facts, reorganized)
For humans: return complete payloads with UUIDs, mime types, pixel-exact URLs, and every field.
For agents: return the smallest high-signal response — human-readable fields (name, file_type), semantic or 0-indexed IDs instead of UUIDs, with pagination, filtering, and truncation defaults.
Why: token budget, trust — verbose IDs waste tokens and induce hallucination; concise fields improve precision.
Matters when: high-volume tool calls, large result sets, ID-heavy APIs.
Testable claim: Agents resolve references more accurately and with ~⅓ the tokens when tool responses use concise semantic fields instead of full technical payloads.
Evidence: measured — Anthropic: writing tools for agents (Slack ~⅓ tokens; UUID→semantic improves precision)
T4. Serve Markdown, not HTML
Type: representation (same facts, reorganized)
For humans: ship styled HTML with nav bars, divs, and scripts.
For agents: serve clean Markdown via content negotiation (Accept: text/markdown) or build-time .md mirrors of each page.
Why: token budget, retrieval — HTML chrome burns tokens and buries content; Markdown's explicit structure extracts cleanly.
Matters when: agents consume docs, web pages, or knowledge bases; token cost or extraction accuracy matters.
Testable claim: Agents extract tables and answer doc questions more accurately and with far fewer tokens from Markdown than from the equivalent HTML.
Evidence: measured — Cloudflare: Markdown for Agents (68–87% fewer tokens); HTML vs Markdown for agents (table extraction 60.7% vs 53.6%)
T5. Tabular data as TOON/CSV, not verbose JSON
Type: representation (same facts, reorganized)
For humans: nested JSON, one self-describing object per record.
For agents: for arrays of uniform records, use a token-oriented tabular notation (TOON) or CSV that declares fields once, then rows.
Why: token budget — repeating keys on every record wastes 30–60% of tokens with no added signal.
Matters when: large uniform datasets, many rows, repeated schemas passed inline.
Testable claim: Agents answer data-retrieval questions at equal-or-better accuracy using ~40% fewer tokens when uniform tabular data is TOON/CSV instead of JSON.
Evidence: measured — TOON format; TOON vs JSON benchmark (TOON ~73.9% vs JSON 69.7% at ~40% fewer tokens)
T6. Flat, self-describing schemas
Type: representation (same facts, reorganized)
For humans: normalized, deeply nested models optimized for storage and evolution.
For agents: keep nesting to 2–3 levels, use semantic field names, treat descriptions/enums as prompts, reference entities by IDs rather than embedding, and enforce strict mode with explicit required/nullable fields.
Why: retrieval, trust — deep nesting raises error rates and loses context; descriptions steer the model's attention.
Matters when: structured extraction, function-calling arguments, agent state passing.
Testable claim: Agents produce valid structured outputs and aggregations more reliably from flat schemas with rich field descriptions than from deeply nested ones.
Evidence: measured + opinion — OpenAI structured outputs; PARSE schema optimization
T7. Errors & logs as recovery guidance
Type: augmentation (adds info)
For humans: terse error codes, HTTP statuses, and raw stack traces to be read by an engineer.
For agents: return actionable natural-language messages that name the cause and suggest the corrective action (valid input example, use a filter, retry differently); avoid ambiguous phrasing.
Why: error recovery — self-healing agents adjust their next call from the message text; vague or minimal errors cause loops.
Matters when: failure-prone tools, long autonomous runs, ambiguous success/empty states.
Testable claim: Agents recover from tool failures in fewer retries when errors include prescriptive recovery guidance instead of raw codes/traces.
Evidence: opinion — Anthropic: writing tools for agents (""no output"" caused needless retries); Anthropic: context engineering
T8. Workflow-level, namespaced tools
Type: representation (same facts, reorganized)
For humans: expose one endpoint per resource and let developers compose CRUD calls.
For agents: build a few consolidated tools targeting high-impact workflows, with clear distinct names namespaced as service_resource (e.g., asana_projects_search).
Why: retrieval, trust — fewer overlapping tools reduce selection errors; consistent namespacing disambiguates similar tools.
Matters when: many similar tools, overlapping capabilities, multi-service agents.
Testable claim: Agents select and call the right tool more accurately when the surface is a few namespaced workflow tools rather than many thin API wrappers.
Evidence: measured + opinion — Anthropic: writing tools for agents (SWE-bench SOTA after tool refinement; namespacing has non-trivial eval effects)
T9. llms.txt + machine-readable entry points
Type: access (changes how it's fetched)
For humans: navigation menus and sitemap.xml enumerating every indexable page.
For agents: a root /llms.txt Markdown file that curates the handful of documents that matter, linking to .md sources and OpenAPI specs, so an agent reasoning in real time finds authoritative content fast.
Why: retrieval, token budget — curates signal over an exhaustive crawl and points to clean source formats.
Matters when: large doc sites/APIs, agents entering an unfamiliar corpus, real-time lookup.
Testable claim: Agents locate the correct documentation faster and with fewer fetches when a site provides a curated llms.txt index versus only HTML nav/sitemap.
Evidence: measured + opinion — llms.txt spec; Cloudflare: Markdown for Agents (adoption >10% of major domains by early 2026)
T10. Structured, agent-parseable telemetry
Type: representation (same facts, reorganized)
For humans: dashboards and free-text log lines read visually by an SRE.
For agents: emit telemetry as OpenTelemetry GenAI spans with standardized attributes (gen_ai.request.model, gen_ai.usage.input/output_tokens, gen_ai.response.finish_reasons) so a debugging or ops agent can parse tool calls, latency, and token cost programmatically.
Why: retrieval, error recovery — a consistent vocabulary lets agents query and reason over traces instead of scraping prose logs.
Matters when: agents debug other agents/systems, multi-agent pipelines, cost/latency analysis.
Testable claim: Agents diagnose failures in agent runs more accurately from OTel GenAI-structured spans than from unstructured log text.
Evidence: opinion + standard — OTel: GenAI observability; OTel: AI agent observability
true
DeepSeek-V3.2
Chatgpt
"I'll research this thoroughly, prioritizing primary sources from major AI labs, standards bodies, and practitioners. Let me run a series of targeted searches.Let me fetch the core Anthropic tools post in full since it's central and contains measured evidence.Excellent, that's a rich primary source. Now let me research the llms.txt standard.Now let me look at Anthropic's ""code execution with MCP"" post, which has measured token-reduction data.Let me research document formats for LLMs and Anthropic's contextual retrieval (both have measured data).Now let me research how data format (markdown/JSON/HTML/tables) affects LLM comprehension, which has benchmark evidence.Let me research OpenAI's tool/function design guidance and structured outputs.Let me check the observability/logs/traces angle for a distinct agent-specific technique.Marked throughout: **MEASURED** = a study/benchmark reports numbers; **OPINION** = expert recommendation without a controlled number. I skipped techniques where the agent and human approach are effectively the same (version control, clear docs, consistent schemas, backups).

## Ranked table

| Rank | Technique                                            | For humans                                         | For agents                                                | Evidence                    |
| ---- | ---------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------- | --------------------------- |
| 1    | Search/retrieval tools, not list-all dumps           | Paginated list UIs to scroll/scan                  | Server-side search returning only matching rows + context | MEASURED                    |
| 2    | Just-in-time references + navigable filesystem       | Preload/ETL everything into one store or dashboard | Lightweight IDs/paths/queries; load slices on demand      | MEASURED                    |
| 3    | Concise-by-default payloads, strip low-signal fields | Full records; more detail is harmless              | Minimal fields; opt-in `detailed` mode                    | MEASURED                    |
| 4    | Semantic IDs over opaque UUIDs                       | UUIDs/codes fine (humans don't read them)          | Resolve to names/enums/0-indexed handles                  | MEASURED                    |
| 5    | Actionable error messages, not stack traces          | Stack traces + codes to debug                      | Plain-language cause + fix + valid-input example          | OPINION (+related MEASURED) |
| 6    | Markdown/YAML for tables, not HTML/CSV/XML           | Rendered HTML tables, spreadsheets                 | Markdown-KV / YAML source text                            | MEASURED                    |
| 7    | Tools-as-code-API + code execution                   | Wire APIs; data flows through app                  | Agent writes code; bulk data stays out of context         | MEASURED                    |
| 8    | Contextual chunking before embedding                 | Read whole doc; no chunking                        | Prepend chunk-situating context before indexing           | MEASURED                    |
| 9    | Namespaced, consolidated, minimal tool sets          | Many granular endpoints in API docs                | Few prefixed tools that bundle multi-step calls           | MEASURED                    |
| 10   | llms.txt + clean `.md` page twins                    | HTML site w/ nav, ads, JS                          | Curated markdown map + `.md` versions at root             | OPINION                     |

---

### T1. Search tools, not list-all dumps

- Type: access
- For humans: paginated list views and dashboards a person scrolls and visually filters.
- For agents: server-side `search_*`/`get_*_context` tools that return only matching records plus surrounding context, never the full collection.
- Why: token budget — an agent reading every row token-by-token wastes finite context on distractors, degrading retrieval and reasoning.
- Matters when: large corpora/log stores where the answer is a few records among thousands.
- Testable claim: agents complete multi-step retrieval tasks more accurately and with fewer tokens when given `search_contacts` instead of `list_contacts`.
- Evidence: MEASURED — Anthropic's held-out Slack/Asana tool evals improved after replacing list/dump tools with search-focused, consolidated ones. https://www.anthropic.com/engineering/writing-tools-for-agents

### T2. Just-in-time references + navigable filesystem

- Type: access
- For humans: pre-load or ETL all relevant data into one store or dashboard up front.
- For agents: keep lightweight identifiers (file paths, stored queries, URLs); organize the corpus as a navigable file tree the agent lists, greps, and loads slice-by-slice at runtime.
- Why: token budget and error recovery — pre-loading blobs floods context; on-demand loading keeps only active data resident.
- Matters when: corpora exceed the context window, or multi-step tasks touch many files.
- Testable claim: agents finish large-corpus tasks with fewer tokens when data is referenced and loaded on demand versus preloaded.
- Evidence: MEASURED — code-execution/filesystem approach cut context overhead up to 98.7%. https://www.anthropic.com/engineering/code-execution-with-mcp ; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

### T3. Concise-by-default payloads

- Type: representation
- For humans: return complete records; extra fields are harmless and sometimes handy.
- For agents: return minimal high-signal fields (`name`, `file_type`) by default; expose a `response_format` enum so the agent opts into `detailed` only when it needs IDs for follow-up calls.
- Why: token budget — every low-signal field (`uuid`, `mime_type`, `256px_url`) consumes context and adds distraction.
- Matters when: tool outputs are large or chained across many calls.
- Testable claim: agents answer with fewer tokens at equal accuracy when tools default to concise output.
- Evidence: MEASURED — Anthropic reports concise Slack responses used ~⅓ the tokens of detailed ones. https://www.anthropic.com/engineering/writing-tools-for-agents

### T4. Semantic IDs over opaque UUIDs

- Type: representation
- For humans: UUIDs and numeric codes are fine — people don't read or transcribe them.
- For agents: resolve arbitrary alphanumeric IDs to meaningful names, enums, or a simple 0-indexed scheme in what the model sees (keep raw IDs available for follow-up calls).
- Why: trust/hallucination — models handle natural-language handles far better than cryptic strings and mis-copy long UUIDs.
- Matters when: retrieval and ID-passing tasks where the model must reference specific records.
- Testable claim: agents retrieve and reference the correct records more accurately when identifiers are semantic rather than raw UUIDs.
- Evidence: MEASURED — Anthropic reports resolving UUIDs to semantic IDs ""significantly improved"" retrieval precision and reduced hallucinations (internal evals; no public number). https://www.anthropic.com/engineering/writing-tools-for-agents

### T5. Actionable error messages, not stack traces

- Type: augmentation
- For humans: raw stack traces, error codes, and tracebacks to diagnose and fix by hand.
- For agents: plain-language messages stating the cause, the corrective action, and a correctly formatted input example, returned inline.
- Why: error recovery — an agent can't click through a debugger; it self-corrects from the next tokens it reads, so the fix must be in the message.
- Matters when: tool inputs are validated, or tasks require several retry loops.
- Testable claim: agents recover from failed tool calls more often when errors state the fix instead of returning opaque codes.
- Evidence: OPINION, with related MEASURED — refining tool descriptions/messages cut error rates on SWE-bench; OpenAI recommends passing tool errors back to the model. https://www.anthropic.com/engineering/writing-tools-for-agents ; https://developers.openai.com/cookbook/examples/o-series/o3o4-mini_prompting_guide

### T6. Markdown/YAML for tables, not HTML/CSV/XML

- Type: representation
- For humans: rendered HTML tables and spreadsheets that display cleanly.
- For agents: feed structured data as markdown key-value or YAML source text; repeat headers periodically in long tables.
- Why: retrieval/reasoning — LLMs were trained heavily on markdown, and verbose HTML/XML burns tokens without aiding comprehension.
- Matters when: large tabular/nested data where the model must look up or compare specific fields.
- Testable claim: agents answer table-lookup questions more accurately from markdown-KV than from CSV or HTML at comparable data.
- Evidence: MEASURED — markdown-KV ~60.7% vs CSV ~44% accuracy; markdown ~60.7% vs HTML ~53.6%; XML ~80% more tokens than markdown. https://www.improvingagents.com/blog/best-input-data-format-for-llms/ ; https://www.improvingagents.com/blog/best-nested-data-format/

### T7. Tools-as-code-API + code execution

- Type: access
- For humans: APIs wired together in application code; data flows through your app, not a reasoning loop.
- For agents: expose tools as code modules the agent imports and calls in a sandbox, filtering/aggregating locally so only results — not raw intermediate data — return to context.
- Why: token budget and trust — bulk data moving between tool calls needn't pass through (or be exposed to) the model.
- Matters when: many connected tools/servers, or large intermediate payloads between steps.
- Testable claim: agents complete multi-tool workflows with far fewer input tokens at equal success when tools are code APIs.
- Evidence: MEASURED — Anthropic reports up to 98.7% context reduction; an independent test found 78.5% fewer input tokens. https://www.anthropic.com/engineering/code-execution-with-mcp ; https://aimultiple.com/code-execution-with-mcp

### T8. Contextual chunking before embedding

- Type: augmentation
- For humans: read the whole document in order; no chunking exists.
- For agents: before indexing each chunk, prepend a short LLM-generated sentence situating it within its parent document (e.g., which filing, company, quarter), then embed and BM25-index that enriched chunk.
- Why: retrieval — isolated chunks (""revenue grew 3%"") lose the identifiers a query needs to match.
- Matters when: RAG over many similar documents where bare chunks are ambiguous.
- Testable claim: agents retrieve the correct chunk more often when chunks carry prepended document context.
- Evidence: MEASURED — Anthropic: 35% fewer failed retrievals (contextual embeddings), 49% with BM25, 67% with reranking. https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide

### T9. Namespaced, consolidated, minimal tool sets

- Type: representation
- For humans: API docs list many granular endpoints; developers pick and compose them.
- For agents: expose few tools with common prefixes (`asana_search`, `asana_projects_search`) that each bundle a natural multi-step task; drop overlapping or rarely-useful tools.
- Why: retrieval/trust — overlapping or vague tools cause wrong-tool selection; consolidation offloads work from the context into the tool.
- Matters when: agents connect to many servers/hundreds of tools.
- Testable claim: agents select and sequence tools more accurately with a small, namespaced set than with many overlapping endpoints.
- Evidence: MEASURED — Anthropic found namespacing had non-trivial eval effects; tool-description refinement drove SWE-bench gains; OpenAI notes reliability within ~100 tools. https://www.anthropic.com/engineering/writing-tools-for-agents

### T10. llms.txt + clean `.md` page twins

- Type: access
- For humans: a full HTML site with navigation, ads, and JavaScript.
- For agents: a root `/llms.txt` markdown file summarizing the site with curated links, plus a clean `.md` version of each important page at the same URL.
- Why: retrieval/token budget — converting cluttered HTML to text at inference is lossy and expensive; a curated map points agents straight to high-value content.
- Matters when: agents browse docs sites or products expose knowledge bases.
- Testable claim: agents answer site-specific questions more accurately/cheaply given llms.txt + `.md` pages than raw HTML.
- Evidence: OPINION — an emerging Answer.AI spec; adoption is uneven and no controlled accuracy benchmark yet. https://llmstxt.org/

---

Two notes on the ranking. Evidence quality drops toward the bottom: T1–T4, T6–T8 rest on published numbers, while T5 and T10 are largely expert consensus. And several ""measured"" numbers come from the vendor proposing the technique (Anthropic's own evals for T1–T4, T7–T9), so treat them as directional rather than independent — the format benchmarks (T6) and the independent code-execution replication (T7) are the least conflicted.

true
"Top 10 below. Rank is by (impact × frequency) × divergence-from-human. I skip the obvious ""markup languages are similar for both"" cases.

==============================================================================
RANKED TABLE
==============================================================================

Rank | Technique | For humans | For agents | Evidence
-----+-----------+------------+------------+----------
1 | Progressive disclosure / metadata-as-signal | Flat pages, big buttons, navigation menus | Lightweight IDs + URIs, schema-annotated resources, breadcrumb-style hierarchy the model parses | MEASURED + opinion
2 | Token-budgeted tool responses | Verbose, human-readable API responses | Compact, structured, paginated, token-budgeted returns; cap defaults; throw informative errors | MEASURED + opinion
3 | Structured outputs (JSON Schema for everything) | Mixed prose + tables | Strict JSON Schema end-to-end; constraining both directions of the data flow | MEASURED
4 | Just-in-time retrieval over pre-loading | Pre-computed dashboards, full docs in one place | Agent holds identifiers, calls tools to fetch on demand; scratchpads outside the window | MEASURED + opinion
5 | LLM-ready site/doc entry point (llms.txt + .md mirrors) | Sitemap.xml + human HTML | /llms.txt with curated Markdown, .md mirrors of every page, ""Optional"" sections for ellision | MEASURED + opinion
6 | Curated toolset + namespaced tool descriptions | Many overlapping APIs | Minimal, atomically-scoped tools; clear non-overlap; RAG over tool registry | MEASURED
7 | Front-load / inverted pyramid for long-form docs | Narrative, conclusion-last | Headline-first, abstract-first, ""Optional"" sections, deterministic order | MEASURED (human web) + opinion (agent)
8 | Document as raw data + structured extraction | Read the PDF as pages | Convert PDFs/DOCX to text, separate reference from content, ship text + images with stable IDs | MEASURED + opinion
9 | Treat errors / logs as first-class structured data | Stack traces, ANSI, free-text | Stable error codes + compact human-readable note + remediation hint; structured fields agents can grep | OPINION (with measured backing from tool-engineering work)
10 | Progressive summarization + scratchpads | Append full history; unlimited scroll | Auto-compact at threshold, write planning to external scratchpad, prune old tool results | MEASURED + opinion

==============================================================================
T1. Progressive disclosure / metadata-as-signal
==============================================================================

```markdown
### T1. Progressive disclosure + metadata-as-signal

- Type: access (changes how it's fetched)
- For humans: Flat pages, nav menus, big buttons, breadcrumbs the eye can scan
- For agents: Lightweight identifiers (file paths, URIs, IDs) plus structured metadata (mimeType, lastModified, audience, priority) so the model can decide whether to fetch now
- Why: Context rot — every token you preload consumes the attention budget; lightweight refs let the model pull only what's needed when it's needed, and the metadata on those refs (folder hierarchy, timestamps, names) encodes meaning without burning tokens
- Matters when: corpus is bigger than a few thousand tokens, when distractors have to be filtered out, when multi-hop traversal is required
- Testable claim: On the same QA task over a 100k-token corpus, agents using identifier-then-fetch resolve multi-hop questions with 2-3x higher accuracy than agents given the full corpus up front, at one-tenth the input tokens
- Evidence: opinion + measured backing — Anthropic ""Effective context engineering for AI agents"" (Sep 2025); MCP Server Resources spec 2025-06-18 §""Annotations""; LangChain ""Context Engineering for Agents"" (Jul 2025); NIST-style needle-in-haystack degradation work cited inside both
```

==============================================================================
T2. Token-budgeted tool responses
==============================================================================

```markdown
### T2. Token-budgeted tool / API responses

- Type: augmentation (adds info) + representation
- For humans: Verbose, prose-y API responses with full nested objects, unlimited arrays, human-readable error messages
- For agents: Compact structured fields, default page caps, total counts, deterministic ordering, explicit error_code + next-step hint
- Why: Tool output becomes part of the LLM's context; oversized returns spend the model's attention on fields it never uses, and ambiguous errors force retry loops; Anthropic's internal Slack/Asana tool evals show clear accuracy gains when returns are trimmed and namespaced
- Matters when: tools return large lists (logs, results, file contents), when agents chain multiple tool calls, when response variability causes the agent to re-query
- Testable claim: Capping tool list responses at 20 items with a `next_cursor` reduces redundant follow-up tool calls by 50%+ on log/search-style agents vs returning full unbounded lists
- Evidence: measured (Anthropic held-out evals, chart in ""Writing effective tools for agents"", Sep 2025) + opinion (MCP community guidance)
```

==============================================================================
T3. Strict structured outputs everywhere (JSON Schema end-to-end)
==============================================================================

```markdown
### T3. Strict structured outputs end-to-end

- Type: representation
- For humans: Prose, free-form tables, conditional narration — humans parse noise easily
- For agents: JSON Schema-constrained generation on every contract: tool inputs, tool outputs, intermediate scratchpads, final answers; refusals made programmatically detectable
- Why: Removes a whole class of retry failures, lets the model reason over the same shape it parses, and unlocks cacheable, diffable responses; OpenAI measured 100% schema adherence where JSON mode gave only syntactic validity
- Matters when: tool inputs are complex, agents call each other in a loop, fields are reused across turns, downstream parsers must be reliable
- Testable claim: Agents using Structured Outputs for tool arguments complete the same multi-step task with zero re-parse failures versus ~5-15% retry rate under vanilla JSON mode
- Evidence: measured — OpenAI ""Structured model outputs"" docs; cross-reference MMLU-Pro (arXiv 2406.01574) on option-set and noise sensitivity reduction
```

==============================================================================
T4. Just-in-time retrieval (identifiers > preloading)
==============================================================================

```markdown
### T4. Just-in-time retrieval instead of pre-loading

- Type: access
- For humans: Pre-rendered dashboards, all docs visible, ""everything on one page""
- For agents: Agent holds lightweight references (paths, URIs, query handles) and calls tools to fetch slices on demand, mirroring human file-system navigation
- Why: Constant-time attention budget per token means preloading 100k tokens costs both money and accuracy; Anthropic's research on context rot shows recall falls off as context grows, so the right move is to keep identifiers cheap and pay for content only when something is actually needed
- Matters when: working set exceeds ~10% of the model's effective context budget, when most of the data is irrelevant to the current question, when multi-step agents traverse references
- Testable claim: On long-horizon agent tasks, agents that store paths-as-state and fetch on demand complete tasks in 1/3 the tokens and with higher final-step accuracy than agents pre-loaded with the entire dataset
- Evidence: opinion + measured backing — Anthropic ""Effective context engineering for AI agents"" (Sep 2025); LangChain ""Context Engineering for Agents"" (Jul 2025); needle-in-haystack degradation literature
```

==============================================================================
T5. /llms.txt + .md mirrors as site entry points
==============================================================================

```markdown
### T5. /llms.txt + .md page mirrors

- Type: access + representation
- For humans: Visual navigation, semantic HTML, JS-driven apps, sitemaps
- For agents: A curated `/llms.txt` Markdown summary at the root with H2 sections, link lists, and an ""Optional"" section the agent can elide; each HTML page duplicated at `<url>.md` (or `index.html.md`); `llms-ctx.txt` / `llms-ctx-full.txt` pre-flattened for one-shot reads
- Why: Real sites lose ~90% of their bytes to chrome, JS, ads, navigation — agents reading raw HTML burn tokens on noise; the spec gives a deterministic parser-friendly format and a markdown-only fallback that's pre-flat for direct context use
- Matters when: external sites, docs sites, e-commerce catalogs, regulatory or legislative text — anywhere humans and agents both need the same authoritative content
- Testable claim: Agents answering questions over a documentation site complete 30-50% faster (fewer fetches, lower tokens) when the site ships `/llms.txt` and `.md` mirrors than when they must scrape rendered HTML
- Evidence: opinion + measured design rationale — Jeremy Howard / Answer.AI llms.txt proposal (Sep 2024, now widely adopted including Cloudflare, Anthropic API docs themselves)
```

==============================================================================
T6. Curated + namespaced tool descriptions (RAG the tool registry)
==============================================================================

```markdown
### T6. Curated, namespaced tool descriptions

- Type: representation
- For humans: One mega-API with broad parameters, or many small endpoints behind good docs
- For agents: A minimal, non-overlapping set of tools with namespaced verbs (`slack_send_message`, not `send`), explicit ""use X instead of Y"" guidance in descriptions, and tool definitions selected by embedding-search at runtime
- Why: LLMs pick tools by description similarity — overlapping or vague descriptions produce wrong-tool calls and longer trajectories; LangChain cites recent papers showing RAG over tool definitions lifts tool-selection accuracy ~3×
- Matters when: any MCP server or function-calling surface exposes more than ~10 tools, when descriptions overlap, when agents must pick between parameterized variants
- Testable claim: For an MCP server with 100+ tools, agents selecting from an embedding-retrieved top-k subset achieve 3× higher first-attempt tool-call correctness than agents seeing all 100 definitions in context
- Evidence: measured (papers cited in LangChain ""Context Engineering for Agents"", Jul 2025) + opinion (Anthropic ""Writing effective tools for agents"", Sep 2025; MCP best-practice guidance)
```

==============================================================================
T7. Inverted-pyramid / front-load structure for long-form docs
==============================================================================

```markdown
### T7. Inverted pyramid + front-load structure

- Type: representation (same facts, reorganized)
- For humans: Narrative flow, anecdotal lead, conclusion last — the journalistic convention
- For agents: One-sentence TL;DR, then structured summary blocks, then ranked detail, then the ""Optional"" appendix; first sentence of every paragraph carries the load-bearing claim
- Why: Attention budget is per-token; agents reading top-to-bottom (or chunking in order) benefit disproportionately from facts being at the top, and they can stop early when they have enough — the inversion also makes any truncation safe
- Matters when: documents exceed the model's working chunk, when the agent may bail out partway, when the answer must be extractable from any prefix
- Testable claim: An agent given a long policy doc with a TL;DR + summary + body answers extraction questions more accurately than the same doc without a TL;DR, and matches human skim-readers on whether the top paragraph carries the answer
- Evidence: measured on humans (NN/g, ""Inverted Pyramid: Writing for Comprehension"") + opinion for agent context (consistent with Anthropic context-engineering guidance and lang-chain compression sections)
```

==============================================================================
T8. Documents as raw data + structured extraction
==============================================================================

```markdown
### T8. Documents as raw data + structured extraction

- Type: representation
- For humans: PDFs and DOCX rendered faithfully, page-faithful screenshots, pixel-perfect typesetting
- For agents: Plain text + extracted structure (markdown, headings, tables as JSON, images by stable IDs); offer the original as a referenced asset but never force the model to parse the binary; use vision only when tables/charts carry information that text cannot
- Why: Binary formats cost 5-10× the tokens and lose the model's ability to grep, quote, or cite; Anthropic's PDF docs explicitly call out that text-only PDFs use ~1k tokens vs ~7k for visual, and a single request can include up to 600 PDF pages or 100 pages under a 200k window — so the docs already encode the agent trade-off
- Matters when: ingesting PDFs, spreadsheets, slide decks; any time you give the model a binary it didn't ask for
- Testable claim: Agents given a converted Markdown version of a PDF answer factoid questions 2-4× faster and with measurably higher faithfulness than agents given the raw PDF on the same requests, especially on tables
- Evidence: measured — Anthropic ""PDF support"" docs token-per-page numbers; opinion on the broader strategy (""Working with other file formats"" page)
```

==============================================================================
T9. Errors and logs as first-class structured data
==============================================================================

```markdown
### T9. Errors and logs as first-class structured data

- Type: representation
- For humans: Colored stack traces, ANSI codes, long free-text messages readable only by the originating developer
- For agents: Stable machine-readable codes (`E_TIMEOUT_DB`, `E_RATE_LIMIT`), short human-readable note, structured fields (request_id, attempt, elapsed_ms), and an explicit remediation hint (""retry with backoff"", ""increase page size"")
- Why: Agents parse errors to decide whether to retry, switch tools, or give up — a free-text stack trace costs tokens to read and rarely disambiguates failure modes; codes let the agent branch deterministically and lets you measure error frequencies across runs
- Matters when: tools fail often, agents must self-recover, you want eval signals on failure modes, error budgets and alerts need to fire
- Testable claim: Agents given structured error responses with a `code` field resolve transient failures via retry ~2× more often than agents given the same failure as a free-text message, with fewer redundant tool calls
- Evidence: opinion + measured backing — Anthropic ""Writing effective tools for agents"" recommends collecting tool-error metrics and improving descriptions; broader SRE practice; no single canonical benchmark found, so mark as opinion
```

==============================================================================
T10. Progressive summarization + external scratchpads
==============================================================================

```markdown
### T10. Progressive summarization + external scratchpads

- Type: representation (compression) + access (scratchpad)
- For humans: Infinite scroll, full histories kept on screen forever, no automatic compaction
- For agents: Auto-summarize trajectory above a threshold (e.g. 95% of window), write plans / decisions / intermediate results to a scratchpad outside the window, prefer trained summarizers at agent-to-agent handoff
- Why: A 200-turn agentic loop accumulates tool calls and reasoning that exceeds the useful attention budget by orders of magnitude; Drew Breunig's long-context failure modes (poisoning, distraction, confusion, clash) all worsen monotonically with size, and Anthropic's LeadResearcher example saves its plan to memory precisely because the window can be truncated at 200k
- Matters when: agents run for many turns, when sub-agents hand off, when you must keep cost and latency bounded across long sessions
- Testable claim: Multi-turn agents with auto-compaction at 95% window usage complete twice-as-long tasks within the same token budget and with higher final-turn accuracy than agents that retain the full trajectory
- Evidence: opinion + measured backing — LangChain ""Context Engineering for Agents"" (Jul 2025, summarization + scratchpad sections); Anthropic context-engineering post (Sep 2025, compaction); Claude Code ""auto-compact at 95%""; Drew Breunig long-context failure taxonomy
```

==============================================================================
EVIDENCE LEGEND
==============================================================================
""measured"" = the source documents report quantified before/after numbers (Anthropic held-out tool evals, OpenAI Structured Outputs schema adherence, MMLU-Pro accuracy deltas, llms.txt adoption metrics).

true
"### T1. Agent-shaped API/tool facades

- Type: access
- For humans: Expose full REST/OpenAPI surfaces, broad docs, and raw payloads.
- For agents: Wrap APIs into narrow task tools with explicit names, JSON schemas,
  constrained parameters, and minimal result fields.
- Why: Agents pay attention to every tool and field; irrelevant schema and output
  increase tool-selection errors, latency, and context noise.
- Matters when: APIs have many endpoints, overloaded operations, or large response
  objects with fields irrelevant to the task.
- Testable claim: Agents complete workflow tasks more accurately with fewer tokens
  when using narrow wrappers instead of full raw API schemas.
  true
  "| Rank | Technique | For humans | For agents | Evidence: measured/opinion |
  | --- | --- | --- | --- | --- |
  | 1 | Codebase Context via AST Repo-Maps | File explorer trees | PageRank-scored symbol graphs | Measured |
  | 2 | Model Context Protocol (MCP) | REST endpoints with UI/Docs | Standardized stdio/HTTP servers | Opinion |
  | 3 | Documentation Mapping (llms.txt) | HTML index and visual nav | llms.txt mapping canonical Markdown | Opinion |
  | 4 | Tool Schema as Prompts | Tutorial-style documentation | Strict schemas with prompt-like descriptions | Measured |
  | 5 | Semantic Document Flattening | PDFs with visual layouts/columns | Linearized Markdown retaining H1/H2 | Measured |
  | 6 | Structured Remedial Errors | Visual stack traces | JSON errors with explicit fix actions | Opinion |
  | 7 | Flattened Tabular Data | HTML tables with merged cells | Flat CSV or JSON with repeating keys | Measured |
  | 8 | Filter-First Pagination | Page numbers and ""Next"" buttons | Semantic filtering and high-limit cursors | Opinion |
  | 9 | Dual-Mode Tool Outputs | Rendered dashboards/UI | Raw JSON coupled with a text summary | Opinion |
  | 10 | Correlated Trace Execution | Chronological text logs | ID-grouped JSON phase logs | Opinion |

```markdown
### T1. Codebase Context via AST Repo-Maps

- Type: representation
- For humans: File explorer trees and deep directory nesting.
- For agents: PageRank-scored symbol graphs extracting signatures via tree-sitter.
- Why: Minimizes token usage while providing global codebase context, preventing context window exhaustion.
- Matters when: Repositories exceed 50 files or require cross-file reference tracking.
- Testable claim: Agents resolve multi-file dependencies with fewer tokens when provided an AST-based repo-map instead of raw file reads.
- Evidence: measured — Aider Benchmarks (https://aider.chat/docs/repomap.html)
```

```markdown
### T2. Model Context Protocol (MCP)

- Type: access
- For humans: REST endpoints accessed via visual API portals like Swagger.
- For agents: Standardized stdio or HTTP servers exposing tools and resources directly.
- Why: Eliminates the need for custom API integration code per service, allowing universal tool discovery.
- Matters when: Integrating multiple distinct external tools or databases simultaneously.
- Testable claim: Agents invoke external data sources more accurately when connected via MCP compared to writing custom REST clients.
- Evidence: opinion — Anthropic MCP Specification (https://modelcontextprotocol.io/)
```

```markdown
### T3. Documentation Mapping (llms.txt)

- Type: access
- For humans: HTML homepages with visual navigation bars and CSS layouts.
- For agents: `llms.txt` file at the domain root mapping out canonical Markdown paths.
- Why: Bypasses web scraping obstacles and complex DOM structures, feeding raw text efficiently.
- Matters when: Ingesting broad documentation sets, APIs, or developer platforms.
- Testable claim: Agents answer API usage queries more accurately when reading from `llms.txt` routed Markdown instead of HTML scraping.
- Evidence: opinion — GitBook Blog (https://www.gitbook.com/blog/what-is-llms-txt)
```

```markdown
### T4. Tool Schema as Prompts

- Type: representation
- For humans: Tutorial-style documentation with conversational examples.
- For agents: Strict OpenAPI schemas where parameter descriptions act as prompt instructions.
- Why: Models use schema descriptions directly for parameter synthesis; unstructured text degrades instruction compliance.
- Matters when: Tool interfaces have tight type constraints or complex nested parameters.
- Testable claim: Agents generate valid JSON payloads more reliably when descriptions are written as explicit imperatives instead of prose.
- Evidence: measured — OpenAI Structured Outputs API (https://platform.openai.com/docs/guides/structured-outputs)
```

```markdown
### T5. Semantic Document Flattening

- Type: representation
- For humans: PDFs with multi-column layouts, visual callouts, and page numbers.
- For agents: Linearized Markdown stripping layout but preserving semantic headings.
- Why: Spatial reasoning over columns often fails; linear semantic structures match token processing mechanisms.
- Matters when: Parsing research papers, manuals, or standard corporate documents.
- Testable claim: Agents extract factual entities from two-column PDFs more accurately when converted to semantic Markdown.
- Evidence: measured — Docling Benchmarks (https://github.com/DS4SD/docling)
```

```markdown
### T6. Structured Remedial Errors

- Type: augmentation
- For humans: Stack traces with syntax highlighting and implicit fixes.
- For agents: Structured JSON errors listing exact failure domains and actionable next steps.
- Why: Agents struggle to guess implicit environment fixes; they require explicit boundary feedback to recover state.
- Matters when: Tools fail due to state mismatches, missing authentication, or rate limits.
- Testable claim: Agents recover from tool execution failures in fewer turns when errors include explicit remedial suggestions.
- Evidence: opinion — Toucan Toco Production Lessons (https://www.toucantoco.com/en/blog/error-handling-observability-multi-agents-system)
```

```markdown
### T7. Flattened Tabular Data

- Type: representation
- For humans: HTML or Excel tables with merged cells and visual grouping.
- For agents: Flat CSV or JSON arrays repeating primary keys on every row.
- Why: Token attention mechanisms lose track of hierarchical visual groupings over long contexts.
- Matters when: Querying financial reports, large datasets, or schedules.
- Testable claim: Agents perform aggregate math tasks more accurately on flattened CSVs compared to tables with merged categorical headers.
- Evidence: measured — WikiTableQuestions benchmarks (https://aclanthology.org/P15-1142/)
```

```markdown
### T8. Filter-First Pagination

- Type: access
- For humans: Page numbers, ""Next"" buttons, or infinite scroll.
- For agents: High-limit cursors combined with exact semantic filtering endpoints.
- Why: Agents exhaust context limits rapidly if forced to sequentially loop through paginated results.
- Matters when: Searching large databases for a single matching entity or record.
- Testable claim: Agents retrieve specific database records with lower token costs when provided a search filter versus an offset paginator.
- Evidence: opinion — API Design Practitioner Consensus
```

```markdown
### T9. Dual-Mode Tool Outputs

- Type: representation
- For humans: Rendered UI elements, graphs, or rich text summaries.
- For agents: Raw JSON payload coupled with a dense string summary for parsing guidance.
- Why: Raw data ensures precision, while the summary grounds semantic understanding for subsequent reasoning.
- Matters when: Tool executions return massive data objects requiring immediate filtering.
- Testable claim: Agents synthesize multi-step answers more accurately when tool outputs provide both raw JSON and a semantic summary.
- Evidence: opinion — Multi-Agent Engineering Patterns
```

```markdown
### T10. Correlated Trace Execution

- Type: representation
- For humans: Chronological text logs read via terminal searches.
- For agents: ID-grouped JSON phase logs tracking intent across multiple tool calls.
- Why: Allows agents to read their own execution history without losing track of distinct sub-agent boundaries.
- Matters when: Multi-agent systems run parallel sub-tasks over extended durations.
- Testable claim: Agents summarize their own execution trajectories more accurately when reading phase-grouped JSON logs instead of raw chronologies.
- Evidence: opinion — Toucan Toco Production Lessons (https://www.toucantoco.com/en/blog/error-handling-observability-multi-agents-system)
```

---

## ChatGPT

I’ll treat each distinct answer block as one submission, normalize claims to A/B-testable units, and merge only when the benchmark intervention is effectively identical.

Thought for 1m 38s

I counted **15 distinct submission blocks**. The initial free-form block counts as one; model labels and trailing `true` markers do not. Evidence descriptions below reflect the supplied cards and were not independently re-verified. `[Inferred]` marks fields filled from context. Mention frequency did not affect scores.

```markdown
### T1. Progressive, just-in-time access

- Scores: **Evidence 5/5 · Mechanism 5/5 · Testability 5/5 · Expected gap 5/5 = 20/20**
- Seen in **11 of 15 submissions**.
- Type: Access
- For humans: Assemble all plausibly relevant documents, schemas, and references in one portal or view before work begins.
- For agents: Provide a compact catalog of paths, IDs, URLs, metadata, or query handles; let the agent search and fetch selected content only when needed.
- Why: Preloaded material consumes attention regardless of relevance. Progressive disclosure keeps distractors out, preserves context for reasoning, and avoids stale copies.
- Matters when: Corpora exceed a few documents, relevance is task-dependent, or data changes frequently. `[Inferred]`
- Testable claim: On 24 large-corpus tasks, index-and-fetch agents achieve equal or higher success with substantially fewer input tokens than agents given the full corpus upfront.
- Evidence: Measured. Submissions cited Anthropic’s context-engineering work, context-rot experiments, and code-execution-over-MCP results reporting reductions as large as 150,000 to 2,000 tokens.

### T2. Execute queries and transformations outside context

- Scores: **Evidence 5/5 · Mechanism 5/5 · Testability 5/5 · Expected gap 5/5 = 20/20**
- Seen in **7 of 15 submissions**.
- Type: Access
- For humans: Export data into spreadsheets, reports, or application screens and inspect intermediate results directly.
- For agents: Expose SQL, code, DuckDB, or tool APIs so filtering, joining, looping, and aggregation happen in an execution environment; return only the final small result or a file reference.
- Why: Intermediate tables and payloads need not pass through the model. External execution reduces tokens, limits data exposure, and performs deterministic operations more reliably.
- Matters when: Tasks involve joins, aggregation, large intermediate results, or multiple tool calls. `[Inferred]`
- Testable claim: Agents answer 24 aggregation and multi-tool tasks more accurately and at least 10× more token-efficiently through execution tools than from equivalent inline data and direct call chaining.
- Evidence: Measured. Anthropic’s code-execution-over-MCP example reported a 98.7% context reduction; several submissions also cited independent replications and code-mode implementations.

### T3. Schema-constrained interfaces

- Scores: **Evidence 5/5 · Mechanism 5/5 · Testability 5/5 · Expected gap 4/5 = 19/20**
- Seen in **8 of 15 submissions**.
- Type: Representation
- For humans: Accept prose, loosely shaped JSON, optional conventions, and values that people can repair or interpret by eye.
- For agents: Enforce typed schemas on tool inputs and outputs, including required fields, enums, units, null semantics, and stable machine-readable result shapes.
- Why: Constrained generation prevents malformed calls and eliminates downstream ambiguity that would otherwise trigger parser failures or retries.
- Matters when: Outputs feed another tool, mutate state, or must be consumed automatically without human repair. `[Inferred]`
- Testable claim: Across 24 chained-tool tasks, strict schemas yield more valid first-attempt calls and fewer repair turns than prompt-only JSON examples.
- Evidence: Measured. Submissions cited OpenAI Structured Outputs reporting 100% schema adherence in its evaluation versus under 40% for unconstrained model output, plus MCP input/output schema support.

### T4. Search and filter before listing

- Scores: **Evidence 4/5 · Mechanism 5/5 · Testability 5/5 · Expected gap 5/5 = 19/20**
- Seen in **13 of 15 submissions**.
- Type: Access
- For humans: Display a complete list or paginated table and let the person scroll, sort, and visually filter.
- For agents: Require or strongly prefer server-side search, predicates, date ranges, field selection, and bounded retrieval before returning records.
- Why: Visual scanning is cheap for a person but every irrelevant row is an attention-consuming token for an agent. Filtering also reduces the chance that a plausible distractor is selected.
- Matters when: The desired records are sparse within logs, catalogs, contacts, tables, or document collections. `[Inferred]`
- Testable claim: Agents retrieve the correct records with higher success and fewer tokens using search/filter tools than by traversing list-all or offset-pagination endpoints.
- Evidence: Vendor-measured practice. Several submissions cited Anthropic’s held-out Slack and Asana tool evaluations, where search-oriented and consolidated tools outperformed broad list/dump interfaces.

### T5. Concise, bounded tool outputs

- Scores: **Evidence 4/5 · Mechanism 5/5 · Testability 5/5 · Expected gap 5/5 = 19/20**
- Seen in **12 of 15 submissions**.
- Type: Representation
- For humans: Return complete records, every technical field, verbose logs, and all matching rows for flexible inspection.
- For agents: Default to high-signal fields, deterministic ordering, pagination, truncation notices, and concise/detailed response modes; offload bulky payloads to files.
- Why: Tool results persist in context and are repeatedly paid for. Low-value fields dilute relevant evidence and can crowd out later reasoning.
- Matters when: Workflows are long, responses contain many fields, or tools can emit open-ended logs and result sets. `[Inferred]`
- Testable claim: Agents complete 24 multi-step tasks with equal or greater accuracy and fewer tokens when tools return concise bounded payloads rather than complete raw responses.
- Evidence: Measured vendor practice. Submissions repeatedly cited Anthropic’s tool evaluations, including a Slack response redesign using roughly one-third the tokens, plus token-efficient code-agent results.

### T6. Contextual, self-contained retrieval chunks

- Scores: **Evidence 5/5 · Mechanism 5/5 · Testability 5/5 · Expected gap 4/5 = 19/20**
- Seen in **6 of 15 submissions**.
- Type: Augmentation
- For humans: Preserve a flowing document in which surrounding pages establish the entity, period, and referents.
- For agents: Prepend each retrievable chunk with compact parent context such as document title, heading path, entity, timeframe, and purpose before indexing it.
- Why: Retrieved passages arrive in isolation. A chunk saying “its revenue increased” may be unusable or unretrievable without the omitted company and period.
- Matters when: Many documents share vocabulary, chunks contain pronouns, or questions require distinguishing similar entities and reporting periods. `[Inferred]`
- Testable claim: On 24 retrieval tasks, context-prepended chunks produce fewer missed or misinterpreted passages than identical raw chunks.
- Evidence: Measured. Anthropic reported 49% fewer retrieval failures with contextualized chunks plus BM25 and 67% fewer with reranking. This card does **not** merge the separate claim that headings are better chunk boundaries.

### T7. Semantic layers over raw schemas

- Scores: **Evidence 4/5 · Mechanism 5/5 · Testability 5/5 · Expected gap 5/5 = 19/20**
- Seen in **3 of 15 submissions**.
- Type: Augmentation
- For humans: Supply normalized tables and place business definitions, relationships, and caveats in separate documentation.
- For agents: Attach meanings, synonyms, units, aggregation levels, PK/FK relationships, join paths, constraints, provenance, and representative values to the task-relevant schema subset.
- Why: Agents must map natural-language intent to opaque columns and joins. Names and types alone leave this mapping implicit and error-prone.
- Matters when: Schemas are large, identifiers are cryptic, joins are non-obvious, or several metrics have similar names. `[Inferred]`
- Testable claim: Agents generate more correct queries on 24 synthetic enterprise-schema tasks when given enriched semantic metadata than when given only table names, columns, and types.
- Evidence: Measured research plus practice. Submissions cited column-description studies, Spider 2.0, extractive schema-linking research, and enterprise semantic-layer practice.

### T8. Task-shaped tool surfaces

- Scores: **Evidence 4/5 · Mechanism 5/5 · Testability 5/5 · Expected gap 5/5 = 19/20**
- Seen in **10 of 15 submissions**.
- Type: Access
- For humans: Expose the complete API, often one endpoint per CRUD operation, and rely on developers to compose workflows.
- For agents: Offer a smaller set of workflow-level tools that perform coherent tasks and hide unnecessary intermediate calls.
- Why: Every exposed operation creates another classification decision. Consolidated tools reduce wrong-tool choices and move deterministic orchestration outside the model.
- Matters when: APIs expose dozens of granular endpoints or common tasks require predictable multi-call sequences. `[Inferred]`
- Testable claim: Agents complete 24 workflow tasks more reliably with a curated task-level facade than with a one-to-one wrapper around every underlying API endpoint.
- Evidence: Vendor evaluation and expert practice. Submissions cited Anthropic tool-refinement evaluations, AWS MCP strategy guidance, and agent-API design practice.

### T9. Behavioral tool definitions

- Scores: **Evidence 4/5 · Mechanism 5/5 · Testability 5/5 · Expected gap 5/5 = 19/20**
- Seen in **11 of 15 submissions**.
- Type: Augmentation
- For humans: Provide reference documentation describing what each endpoint does; the reader infers when to choose it.
- For agents: Put selection guidance directly in the tool definition: intent-bearing names, namespaces, “use when” and “do not use when” rules, parameter formats, realistic examples, and distinctions from neighboring tools.
- Why: Tool selection is performed from the definitions currently in context. Ambiguous names or dispersed guidance directly produce wrong calls and invented parameters.
- Matters when: Tools overlap, several services expose similarly named operations, or parameters have strict but non-obvious formats. `[Inferred]`
- Testable claim: Using the same underlying operations, agents select and parameterize tools more accurately with behavioral descriptions than with terse name-plus-schema definitions.
- Evidence: Measured vendor evaluation and guidance. Submissions cited Anthropic’s tool-writing evaluations, OpenAI function-calling guidance, MCP documentation, and controlled API-naming work.

### T10. Structural maps for connected corpora

- Scores: **Evidence 4/5 · Mechanism 5/5 · Testability 5/5 · Expected gap 5/5 = 19/20**
- Seen in **5 of 15 submissions**.
- Type: Augmentation
- For humans: Explore directory trees, files, links, and source code until the relationships become clear.
- For agents: Provide compact expandable maps of symbols, signatures, callers, imports, dependencies, entities, and links, ranked by likely relevance.
- Why: Multi-hop relationships are expensive to rediscover through repeated lexical reads. A compact graph supplies global structure while allowing selective expansion.
- Matters when: Codebases, document networks, or entity collections are large, interconnected, and unfamiliar. `[Inferred]`
- Testable claim: Agents localize and modify the correct components in 24 multi-file tasks using fewer reads and tokens with a dependency-aware map than with only a filesystem tree.
- Evidence: Measured in code-oriented evaluations. Submissions cited Aider repository maps, tree-sitter/PageRank symbol maps, Codebase-Memory, and SWE-Explore. It ranks last among the 19-point ties because its strongest evidence is code-specific rather than cross-domain.

### Others

- **Actionable, retry-aware errors** — **18/20** `(E3 M5 T5 G5; seen in 12/15)`: return cause, failed constraint, retryability, valid alternatives, and a corrective action instead of a code or trace; it missed because most supporting evidence was expert practice rather than controlled A/B results.
- **Original media plus synchronized derivatives** — **18/20** `(E4 M5 T5 G4; seen in 5/15)`: retain images, audio, video, or pages while linking OCR, transcripts, tables, timestamps, coordinates, and confidence; strong mechanism, but less universal than the 19-point techniques.
- **Live lexical/file navigation instead of a pre-built embedding index** — **18/20** `(E3 M5 T5 G5; seen in 4/15)`: grep/glob/read may outperform stale vector retrieval for exact, fast-changing corpora; evidence was internal and corpus-dependent, while one submission simply advocated storing embeddings.
- **Clean Markdown derivatives of HTML/PDF** — **17/20** `(E4 M4 T5 G4; seen in 13/15)`: structure-preserving Markdown usually saves many tokens, but the submitted evidence for consistent task-accuracy gains was mixed.
- **Semantic identifiers instead of UUIDs** — **17/20** `(E4 M4 T5 G4; seen in 7/15)`: names or short handles reduce copying and reference errors; the effect is useful but narrower than redesigning the surrounding retrieval or tool interface.
- **Header-once tabular serialization** — **17/20** `(E4 M4 T5 G4; seen in 9/15)`: CSV, Markdown, YAML, or TOON can beat repeated-key JSON on token cost; accuracy depends materially on model, nesting, and task.
- **Atomic provenance and freshness metadata** — **17/20** `(E4 M4 T5 G4; seen in 3/15)`: attach source, version, timestamp, authority, span, and content hash to every retrieved unit; important for trust, but the submissions offered limited clean causal measurements.
- **Entity-centric minimum viable views** — **17/20** `(E2 M5 T5 G5; seen in 1/15)`: expose a task-scoped customer/order/device view rather than source-system tables; excellent mechanism, but supported mainly by practitioner opinion.
- **Context compaction and external scratchpads** — **17/20** `(E4 M5 T4 G4; seen in 2/15)`: summarize old trajectories and move state outside context; excluded from the top ten because it is an agent-harness technique rather than data organization.
- **Shallow, self-describing schemas** — **16/20** `(E3 M4 T5 G4; seen in 2/15)`: reduce nesting and use explicit field descriptions and references; plausible but partly overlaps strict schemas, while the distinct nesting-depth claim had weaker evidence.
- **Curated `/llms.txt` manifests** — **16/20** `(E2 M4 T5 G5; seen in 10/15)`: provide an agent-oriented map of important site resources; highly testable and agent-specific, but controlled evidence remains sparse despite frequent mention.
- **Heading-aligned chunk boundaries** — **16/20** `(E3 M4 T5 G4; seen in 2/15)`: split documents at semantic headings rather than fixed lengths; kept separate from contextual chunk augmentation because the A/B test differs, and submitted benchmark results were mixed.
- **Advertised size and token cost before fetching** — **16/20** `(E2 M4 T5 G5; seen in 1/15)`: publish row, byte, or token counts so an agent can choose sampling or querying; clear mechanism, but no submitted outcome benchmark.
- **Resolve descriptive inputs inside tools** — **15/20** `(E2 M4 T5 G4; seen in 1/15)`: accept “downtown branch” and deterministically resolve or disambiguate it rather than requiring an exact ID; strong testability, weak evidence.
- **Structured agent telemetry and correlated traces** — **15/20** `(E2 M4 T5 G4; seen in 5/15)`: use standardized span, tool, entity, model, token, and phase fields rather than prose logs; backed mainly by emerging standards, not task-performance tests.
- **Self-describing paths and folder names** — **15/20** `(E2 M4 T5 G4; seen in 2/15)`: encode function, date, and scope in paths so navigation itself carries meaning; plausible but under-measured and weaker than explicit structural maps.
- **Dual raw-plus-summary tool outputs** — **15/20** `(E2 M4 T5 G4; seen in 1/15)`: pair exact JSON with a semantic summary; it may help reasoning, but it also adds tokens and lacked comparative evidence.
- **One canonical source for human and agent views** — **14/20** `(E2 M4 T4 G4; seen in 1/15)`: derive HTML, Markdown, and machine feeds from the same underlying content to prevent drift; valuable governance practice, but the expected 24-task performance gap is uncertain.
- **Inverted-pyramid documents** — **13/20** `(E2 M3 T4 G4; seen in 2/15)`: put the conclusion and key facts first so truncation remains safe; supported strongly for human web reading but only indirectly for agents.
- **Generic “store as embeddings”** — **11/20** `(E2 M2 T4 G3; seen in 1/15)`: too underspecified to identify when embeddings beat lexical, structured, or live retrieval and therefore lacks a clear causal intervention.
- **MCP as the technique itself** — **10/20** `(E2 M2 T3 G3; seen in 1/15)`: MCP standardizes access but does not by itself determine how data should be organized, represented, filtered, or returned.
- **AGENTS.md, SKILL.md, memory, guardrails, and scratchpad instructions** — not scored: these are agent-harness artifacts and were outside the stated scope.
```

A merge ledger mapping all 15 submissions to these normalized techniques would make the deduplication auditable.

---

## User

Some of these hypotheses are clearly uncontentious. For example, we tested one, and it wasn't clear that that was an obvious win. But the second and third, maybe even fourth, seem like they would obviously and almost always be true. Is that the case? Or put another way, if you had to pick one of these that people may not agree with, and yet is likely to be true, then what would those be? Give me the top three.

---

## ChatGPT

<details>
<summary>Thought for 12s</summary>

Thinking

Analyzing token wins and controversial tech assumptions

I’m considering different tech tools and ideas, such as live lexical navigation vs. embeddings, and semantic layers. Some are contested, but may be true under certain conditions. I’ll explore hypotheses, like how live navigation might beat embeddings in dynamic corpora. The task will be to clarify and test these ideas.

Thought for 12s

Done

</details>

Yes. T2–T4 are mostly **engineering hygiene**, not interesting hypotheses:

- Execute filtering and aggregation outside the context window.
- Use strict schemas when deterministic code consumes the output.
- Search before returning thousands of records.

They may fail at the margins, but a benchmark would mostly estimate the size of an unsurprising benefit.

The three more useful bets are:

### 1. For changing, text-heavy corpora, grep-style navigation can beat embeddings

**Claim:** Give an agent filenames, paths, `grep`, `glob`, and bounded reads; it will often outperform vector retrieval over the same corpus.

Why people disagree: Embeddings and RAG are treated as the default architecture for large corpora. Lexical search sounds primitive and unable to handle semantic queries.

Why it is likely true: Agents can iteratively reformulate searches, inspect directory structure, follow references, and verify exact matches. The index is always current, failures are visible, and identifiers such as function names, error strings, product codes, and dates are often lexical anyway.

The claim should be bounded to **frequently changing corpora with meaningful names and exact textual anchors**—codebases, project files, logs, policies—not general semantic search over millions of unrelated documents.

**Test:** Fresh filesystem + grep/glob/read versus a vector index, including mutations made after indexing. Measure task success, false confidence, tokens, and maintenance assumptions.

### 2. Uniform tables should often be serialized less “machine-readably,” not more

**Claim:** For data placed directly in model context, CSV, Markdown, or another header-once format will often beat repeated-key JSON on accuracy per token—and sometimes on raw accuracy.

Why people disagree: JSON is typed, explicit, ubiquitous in APIs, and usually considered the safest format for machines. Repeating keys feels like useful redundancy.

Why it is likely true: For a uniform table, repeated keys communicate almost no new information. They consume attention, separate adjacent values, and reduce how many rows fit in the useful context. Models can reason well over compact textual tables, especially when headers are repeated occasionally and missing values are explicit.

This does **not** claim that CSV should replace JSON for irregular nested objects or strict tool contracts. The surprise is that **the best interchange format for software may not be the best reasoning format for an agent**.

**Test:** Identical datasets in JSON objects, CSV, Markdown tables, and Markdown key-value rows across lookup, comparison, aggregation, and anomaly tasks. Plot accuracy against tokens, not accuracy alone.

### 3. A compact relationship map can be more valuable than additional source content

**Claim:** For multi-hop work, an agent given a compact symbol/dependency/entity map plus selective reads will outperform one given the same token budget of raw files or documents.

Why people disagree: Generated maps can be incomplete, lossy, stale, or simply another abstraction the model must understand. Many practitioners prefer letting the agent inspect the primary source directly.

Why it is likely true: Agents commonly waste calls rediscovering global structure—what imports what, where an entity is defined, which tables join, which document refers to which policy. A small map answers “where should I look?” while preserving most of the context for the actual evidence. Humans acquire such mental maps gradually; an unfamiliar agent starts from zero each run.

The map should remain **navigational, not authoritative**: relationships, signatures, locations, and provenance, with source material fetched for verification.

**Test:** Multi-file debugging, schema-join, and cross-document questions using filesystem tree only versus dependency/entity map plus bounded reads. Measure localization accuracy, unnecessary opens, tokens, and unsupported conclusions.

My ranking would therefore be:

1. **Grep/navigation can beat embeddings**
2. **Compact tables can beat JSON**
3. **Relationship maps can beat more raw context**

These are strong workshop hypotheses because knowledgeable participants can reasonably predict opposite outcomes before seeing the experiment.

---

## User

For the "2. Uniform tables should often be serialized less “machine-readably,” not more" which hypothesis number was it? Can you give it to me again?

---

## ChatGPT

<details>
<summary>Thought for a couple of seconds</summary>

Thinking

Thought for a couple of seconds

Done

</details>

It was **#2 in the three contrarian hypotheses**, but it was **not in the ranked T1–T10**. In the full collation, it appeared under **Others** as **“Header-once tabular serialization”**, scoring **17/20** and seen in **9 of 15 submissions**.

### H2. Uniform tables should be serialized compactly, not as repeated-key JSON

- **Type:** Representation
- **For humans/software:** Use JSON objects, where every row repeats its field names.
- **For agents:** Use a header-once format such as CSV, Markdown tables, or TOON for uniform records.
- **Why:** Repeated JSON keys consume tokens without adding much information. Compact formats fit more rows into useful context and keep related values closer together.
- **Matters when:** Data is large, flat, and regular; the model must inspect, compare, aggregate, or find anomalies across many rows.
- **Testable claim:** Given identical uniform tables, agents achieve better accuracy per token—and possibly higher raw accuracy—using header-once formats than repeated-key JSON.
- **Evidence:** Measured but model- and task-dependent. Submitted sources reported substantial token savings, while accuracy findings varied.

The important boundary is: **this applies to uniform tabular data placed in model context, not nested objects or strict tool-call contracts.**

---

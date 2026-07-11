---
title: "When Data is for Agents Fifth Elephant Workshop Prep"
date: 2026-07-11T15:27:14+05:30
source: "https://chatgpt.com/c/6a4282d9-7250-83ec-a4a7-324e533d33b2"
---

## User

I'm delivering this workshop: https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/ Read it. You can also find it on LocalMCP at ~/Dropbox/notes/talks.md. Research online for the modern best practices on how to structure and optimize content and data for agent consumption. What are the best practices? What are the emerging techniques? What do AI companies say? What do experts who create / curate data for AI agent consumption say? Based on these, identify the top techniques comprehensively and list them all, sorted by impact + frequency.

---

## ChatGPT

I’ll ground this in three inputs: the Hasgeek workshop page, your local talks note, and current public guidance from AI companies plus practitioners. I’ll then collapse the findings into a ranked technique catalog, not a generic “best practices” essay.

Looked for available tools

I read the public Hasgeek page and the matching LocalMCP note at `/home/vscode/Dropbox/notes/talks.md:137-150`. Your workshop premise is right on the frontier: when agents consume data, the unit of design shifts from dashboards, normalized tables, and polished docs to context budgets, tool affordances, relationship descriptions, traces, schemas, and verification loops. The public page already frames the key provocation: “optimize for token budgets instead of disk or query cost,” with “tools beat tables” and “logs beat docs” as core hypotheses. [Hasgeek](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/)

The strongest consensus across OpenAI, Anthropic, MCP, Microsoft/NLWeb, Google A2A, and recent research is this: agent-ready data is not “clean data” alone. It is a controlled context-and-tool surface that lets an agent discover, retrieve, reason, act, verify, and recover cheaply.

Ranked below by combined impact + frequency across the sources.

## Top techniques for structuring data/content for agents

1. **Optimize for context, not storage.**
   Keep the smallest high-signal token set in the model’s attention: relevant instructions, current state, task facts, examples, tool docs, and retrieved snippets. Anthropic explicitly frames context engineering as curating finite attention, not maximizing context length; it warns about “context rot” and says more context is not automatically better. [Anthropic+1](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
   For your workshop: “Data engineering for agents begins by asking: what must fit in attention right now?”
2. **Expose task-level tools, not raw databases or API endpoints.**
   Agents perform better when APIs are wrapped into workflow-level tools such as `search_logs`, `get_customer_context`, or `schedule_event`, rather than one tool per low-level endpoint. Anthropic says not to wrap every endpoint and recommends fewer high-impact workflow tools; OpenAI similarly recommends combining functions that are always called in sequence and offloading work from the model into code. [Anthropic+1](https://www.anthropic.com/engineering/writing-tools-for-agents)
   Workshop line: “Tables are ingredients. Tools are recipes.”
3. **Use strict schemas for tool inputs and outputs.**
   JSON Schema, Pydantic/Zod models, MCP input/output schemas, and OpenAI structured outputs reduce ambiguity and make failures detectable. OpenAI recommends strict mode for function calling and says structured outputs ensure responses adhere to a schema; MCP tool results can include `structuredContent` that conforms to an output schema. [OpenAI Platform+2OpenAI Platform+2](https://platform.openai.com/docs/guides/function-calling)
   Practical move: every agent-facing function should have typed inputs, typed outputs, examples, and explicit error cases.
4. **Treat tool descriptions as prompts.**
   Tool names, descriptions, examples, edge cases, and argument docs are part of the agent’s working prompt. Anthropic says tool descriptions need as much prompt-engineering care as normal prompts; OpenAI recommends detailed function descriptions, clear enums, and an “intern test” for whether a human could call the tool correctly from the docs alone. [Anthropic+2Claude Platform Docs+2](https://www.anthropic.com/engineering/building-effective-agents)
   Bad: `get_data(query)`. Better: `find_customer_orders(customer_name, date_range, status)` with usage boundaries.
5. **Return high-signal results, not complete dumps.**
   Tool outputs should be concise, semantically meaningful, and directly useful for next action. Anthropic recommends returning stable human-readable identifiers, only necessary fields, surrounding context where useful, and configurable `concise` versus `detailed` modes. It also recommends pagination, range selection, filtering, and helpful truncation messages. [Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents)
   Workshop exercise: take a 100-column customer row and design a 12-field agent result.
6. **Add provenance to everything.**
   Every retrieved fact should carry source, timestamp, owner, confidence, transformation lineage, and ideally a link or resource URI. MCP resources include URI, name, description, MIME type, size, and annotations such as audience, priority, and last modified; OpenAI retrieval returns relevant chunks, similarity scores, and file of origin. [Model Context Protocol+1](https://modelcontextprotocol.io/docs/concepts/resources)
   Agent-ready fact = value + why it is trustworthy + where it came from.
7. **Use hybrid retrieval: semantic + keyword + metadata filters.**
   Pure vector search is not enough for enterprise data. OpenAI’s retrieval docs describe semantic search, query rewriting, file attributes, filters, similarity scores, and hybrid search using reciprocal rank fusion. [OpenAI Developers+1](https://developers.openai.com/api/docs/guides/retrieval)
   Best practice: index chunks with embeddings, but filter by business metadata such as product, region, date, owner, document type, sensitivity, and freshness.
8. **Use progressive disclosure.**
   Do not preload all relevant data. Give the agent lightweight handles first: filenames, IDs, schema summaries, row counts, sample rows, `head`, `tail`, search tools, and drill-down tools. Anthropic recommends just-in-time context through targeted queries, file paths, naming, timestamps, and progressive exploration. [Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
   This is the agent equivalent of “don’t paste the whole warehouse into the prompt.”
9. **Publish LLM-native documentation.**
   Use clean Markdown, stable URLs, and `/llms.txt` indexes that point models to the most useful docs. The `llms.txt` proposal exists because websites are too large, noisy, and JavaScript-heavy for inference-time use; it recommends concise Markdown guidance and clean `.md` versions of important pages. Cloudflare now publishes product-specific `llms.txt` files for its docs. [llms-txt+1](https://llmstxt.org/)
   For internal data portals: add `/llms.txt`, `/schema.md`, `/examples.md`, `/known_issues.md`.
10. **Adopt MCP as the agent-facing data/tool surface.**
    MCP standardizes how apps expose resources, tools, and prompts. Resources expose contextual data such as files, schemas, and app-specific information; tools let models query databases, call APIs, and compute; prompts provide reusable interaction templates. [Model Context Protocol+2Model Context Protocol+2](https://modelcontextprotocol.io/docs/concepts/resources)
    Workshop framing: MCP is less “integration plumbing” and more “the contract by which agents see the organization.”
11. **Separate resources, tools, and prompts.**
    A resource says “here is context,” a tool says “here is an action or computation,” and a prompt says “here is a reusable procedure.” MCP formalizes this separation, and OpenAI’s Agents SDK supports MCP servers, strict schema conversion, approval controls, prompt reuse, and tracing. [Claude Platform Docs+1](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)
    This is a useful design lens for any dataset: what should be read, what should be called, what should be templated?
12. **Describe relationships, grain, and business semantics near the data.**
    Agents can join and transform data, but they need to know grain, entity identity, join ambiguity, units, slowly changing dimensions, business definitions, and exception rules. Your workshop note explicitly says relationship descriptions may matter more than pre-joined clean data; Microsoft’s NLWeb similarly leans on Schema.org/RSS semi-structured formats to expose site semantics for agents. [Hasgeek+1](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/)
    A useful artifact: `relationships.md` beside every dataset.
13. **Prefer live governed connectors over stale duplicated corpora.**
    NLWeb’s docs note that production systems may connect to live databases instead of duplicating content, specifically to avoid freshness problems. MCP also emphasizes access controls, URI validation, and permission checks. [GitHub+1](https://github.com/microsoft/NLWeb)
    The agent should query the governed source of truth when freshness matters, but retrieve summarized snapshots when cost or latency matters.
14. **Keep the active toolset small.**
    Tool definitions consume context. OpenAI recommends starting with fewer than 20 loaded functions, shortening descriptions when needed, and using tool search for larger toolsets. Anthropic recommends namespacing tools by service/resource and avoiding overlapping tools. [OpenAI Platform+1](https://platform.openai.com/docs/guides/function-calling)
    Agent consumption pattern: discover broadly, load narrowly.
15. **Use namespacing and clear tool taxonomy.**
    Tool names influence selection. Names like `gmail.search`, `calendar.create_event`, `warehouse.query_sales`, and `crm.get_customer_context` reduce ambiguity. Anthropic specifically recommends namespacing tools and says naming affects evaluation performance. [Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents)
16. **Build eval harnesses for agent consumption.**
    Evaluate whether agents can use the data/tools to complete realistic tasks. Anthropic recommends real-world, complex, verifiable eval tasks and tracking tool calls, token usage, errors, latency, and success. It also recommends analyzing transcripts and using agents themselves to improve tool descriptions and interfaces. [Anthropic+1](https://www.anthropic.com/engineering/writing-tools-for-agents)
    Your workshop could include: “Here is a dataset. Write 10 verifiable tasks an agent should be able to complete.”
17. **Make logs and traces first-class data.**
    Logs show what agents actually needed, where they failed, which fields/tools were unused, and which errors confused them. Anthropic recommends analyzing transcripts and tool-call metrics to improve agent tools; OpenAI’s MCP guidance highlights tracing and approval policies around MCP servers. [Anthropic+1](https://www.anthropic.com/engineering/writing-tools-for-agents)
    This supports your “logs beat docs” hypothesis: docs describe intent; logs reveal friction.
18. **Design errors as recovery instructions.**
    Error messages should say what failed, why, what valid inputs look like, and what to try next. OpenAI recommends making invalid states unrepresentable through enums/object structure; Anthropic recommends helpful truncation/error responses that steer agents toward token-efficient strategies. [OpenAI Platform+1](https://platform.openai.com/docs/guides/function-calling)
19. **Use compaction and structured memory for long tasks.**
    Long-horizon agents need periodic summaries, notes, state files, and memory artifacts. Anthropic describes compaction, structured note-taking, tool-result clearing, and subagents returning condensed summaries as context-management techniques. [Anthropic+1](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
    Agent-ready repository pattern: `PLAN.md`, `STATE.md`, `DECISIONS.md`, `OPEN_QUESTIONS.md`, `EVIDENCE.md`.
20. **Use subagents for wide exploration, then return condensed evidence.**
    Anthropic lists orchestrator-worker and subagent patterns for complex work where different subtasks need separate context windows. The main agent should receive compact summaries, evidence, and next actions rather than raw exploration logs. [Anthropic+1](https://www.anthropic.com/engineering/building-effective-agents)
21. **Compile repeated agent work into deterministic workflows.**
    When the same multi-step path recurs, convert it into code, SQL, a workflow tool, or a declarative plan. Anthropic recommends workflow-level tools; recent research on MCP workflow engines reports large token savings by replacing repeated reasoning with declarative workflow blueprints. [Anthropic+1](https://www.anthropic.com/engineering/writing-tools-for-agents)
    This is the agent version of “don’t reason every time; operationalize what worked.”
22. **Use web-native agent protocols: NLWeb and A2A.**
    Microsoft’s NLWeb exposes websites through natural-language interfaces, Schema.org/RSS data, JSON responses, and MCP endpoints. Google’s A2A protocol focuses on agent-to-agent capability discovery, task management, artifacts, and multimodal message parts. [GitHub+1](https://github.com/microsoft/NLWeb)
    Emerging pattern: websites become callable agents, not just pages.
23. **Use canonical examples, not giant rulebooks.**
    Anthropic recommends diverse canonical examples rather than exhaustive edge-case lists. Examples should teach the agent the intended pattern, format, and failure handling. [Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
    Good data docs should include “3 good queries, 3 bad queries, 3 edge cases.”
24. **Use human approvals and side-effect labels for risky tools.**
    MCP tools can be dangerous because they may trigger external side effects. MCP recommends human-in-the-loop controls; OpenAI’s Agents SDK supports approval policies for MCP servers and per-tool approval maps. [Model Context Protocol+1](https://modelcontextprotocol.io/docs/concepts/tools)
    Classify tools: read-only, write, destructive, external-world, financial, privacy-sensitive.
25. **Do not fetishize one format. Test formats by task and model.**
    Anthropic says to choose formats that are easy for models and reduce overhead, often internet-familiar formats; recent research comparing YAML, Markdown, JSON, and TOON found model capability and schema architecture mattered more than format alone. [Anthropic+1](https://www.anthropic.com/engineering/building-effective-agents)
    Practical rule: Markdown for explanation, JSON for contracts, CSV/Parquet for bulk data, SQL for relational access, XML-ish tags for prompt segmentation, but benchmark.
26. **Partition context by domain/task, not only by normalized schema.**
    Recent file-native agent research found domain-partitioned schemas can scale better for large schema spaces, and that file size is not the same as token/runtime cost. [arXiv](https://arxiv.org/abs/2602.05447?utm_source=chatgpt.com)
    For enterprise data: create agent-facing “task packs” such as `sales_renewal_context`, `invoice_dispute_context`, or `student_risk_context`.
27. **Make UI and web interactions machine-describable.**
    Emerging web-agent research shows that structured interaction metadata can reduce processing requirements while preserving high task success. Related work on web list extraction converts demonstrations into repeatable programs rather than repeatedly asking agents to inspect pages manually. [arXiv+1](https://arxiv.org/abs/2508.09171?utm_source=chatgpt.com)
    This matters when agents operate browsers, dashboards, CRMs, and admin consoles.
28. **Add freshness, priority, audience, and sensitivity metadata.**
    MCP resources support annotations such as audience, priority, and last modified; OpenAI vector-store files support attributes for filtering. These help agents decide what to retrieve, trust, skip, or escalate. [Model Context Protocol+1](https://modelcontextprotocol.io/docs/concepts/resources)
29. **Separate untrusted content from instructions.**
    Data retrieved from emails, web pages, tickets, or docs may contain prompt injection. MCP warns that tool annotations should be treated as untrusted unless they come from trusted servers, and its resource guidance includes URI validation, access controls, and permission checks. [Model Context Protocol+1](https://modelcontextprotocol.io/docs/concepts/tools)
    Agent-ready data should label instruction-bearing text, quoted user text, external content, and system policy separately.
30. **Make “agent readiness” measurable.**
    Track task success, verification pass rate, retries, tool-call count, token cost, latency, irrelevant retrieval rate, schema validation failures, human escalations, and stale-source usage. Anthropic’s tool guidance explicitly recommends runtime metrics and held-out evals; OpenAI emphasizes strict schemas, tracing, and tool-result validation patterns. [Anthropic+1](https://www.anthropic.com/engineering/writing-tools-for-agents)

## The workshop’s strongest teachable synthesis

The old stack optimized for humans: tables, dashboards, reports, and docs.

The agent stack optimizes for repeated autonomous work: compact context, discoverable tools, typed contracts, semantic metadata, provenance, retrieval, memory, logs, evals, and governed actions.

Your most useful workshop artifact could be a one-page “Agent-Ready Data Checklist”:

“Can an agent discover this? Can it understand the grain and relationships? Can it retrieve only what it needs? Can it call the right tool safely? Are inputs and outputs typed? Is provenance attached? Are errors recoverable? Is freshness visible? Are risky actions gated? Can we evaluate whether the agent succeeded?”

That checklist captures the modern best practice better than “clean your data.”

---

## User

See how I run my workshops on LocalMCP - for example: ~/code/talks/2025-09-16-vibe-analysis/ ~/code/talks/2026-04-08-ai-workshop-lbsnaa/ ~/code/talks/2026-01-11-nptel-vibe-coding-workshop/ ~/code/talks/2026-05-23-ai-unboxed-context-engineering/ ~/code/talks/2026-06-13-data-stories-with-ai/ These involve me actually getting the audience to DO things and learn from it. It's usually real-life things. Actually relevant and useful for the audience. It's also something that we can collectively learn from - serving as experiments that generate insights, datasets, benchmarks, etc. Keeping this in mind, ideate, and suggest what I might do in this workshop: "When Data is for Agents, Not Humans" - that aligns with the themes. My aim is that the audience walks away with some useful, tangible things. That they learn things they couldn't have learned easily otherwise. That I get a set of experiments, benchmarks, datasets, ... that I can build an asset out of. That we do this in interesting innovative ways.

---

## ChatGPT

I’ll first extract the recurring workshop mechanics from those five repos: how you frame tasks, what participants build, how results are collected, and what assets survive afterward. Then I’ll design experiments for this workshop that produce both immediate participant value and reusable benchmarks.

The common pattern is already clear: participants use their own material, run the same idea through multiple agents, publish/share outputs, and collectively inspect failures rather than merely watch a demo. I’m now looking for the strongest “experimental design” patterns in the context-engineering and data-stories workshops—especially ablations, comparisons, and audience-generated datasets.

Thought for 2m 47s

## Recommendation: make the workshop one large controlled experiment

I would structure the four hours around one question:

> **Given the same underlying facts and the same task, what data environment helps an agent perform best?**

Call it the **Agent Data Bake-off**.

Participants should not merely learn a checklist. They should generate evidence for the checklist by running agents against deliberately different versions of the same data.

This fits the workshop promise: four hands-on hours, participants bringing their own material, producing reproducible shared results, and leaving with scripts and an agent-data checklist. [hasgeek.com](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/)

It also matches your strongest workshop patterns:

- The audience chooses and guides the work rather than following a fixed demo: `2025-09-16-vibe-analysis/README.md:112-130`.
- People work in parallel, share chats and outputs, and compare what different agents produce: `2026-01-11-nptel-vibe-coding-workshop/activities.md:53-61`.
- A live form changes during the session and becomes the dataset for the session itself: `2026-06-13-data-stories-with-ai/transcript.md:81-83`.
- Participants work on personally relevant material and leave having actually changed their behaviour: `2026-05-23-ai-unboxed-context-engineering/transcript.md:70-88,170-182`.
- The room collectively generates hypotheses, artifacts, failures and revised outputs—not just answers.

## The backbone: same agent, same task, six data environments

Create one realistic operational dataset. My preferred case is **customer rescue / support operations**, because it naturally combines structured data, documents, logs, business rules, provenance, conflicting sources and actions.

The underlying corpus could contain:

- `customers.csv`
- `subscriptions.csv`
- `payments.csv`
- `tickets.jsonl`
- `product-events.parquet`
- `sla-policy.md`
- `incident-log.md`
- `account-manager-notes.md`
- deliberately inconsistent customer IDs and names
- one stale policy
- one conflict between CRM and billing
- one missing relationship
- one prompt-injection-like instruction inside a ticket
- one operational exception visible only in the logs

The main task:

> Identify the five customers requiring intervention today. Estimate revenue at risk, explain the evidence, identify uncertainty, and recommend the next action.

Prepare six representations of exactly the same underlying facts:

| Pack             | What the agent receives                                                   | Hypothesis tested                                     |
| ---------------- | ------------------------------------------------------------------------- | ----------------------------------------------------- |
| A. Human-perfect | Dashboard PDF and polished joined CSV                                     | Human-friendly presentation may not be agent-friendly |
| B. Raw dump      | Original files with filenames only                                        | Can agents reconstruct everything themselves?         |
| C. Documented    | Raw files plus data dictionary and business definitions                   | How much do descriptions help?                        |
| D. Relational    | Raw files plus grain, relationships, identity rules and source precedence | Are relationships more valuable than pre-joining?     |
| E. Toolified     | Task-level tools with typed inputs and concise outputs                    | Do tools beat tables?                                 |
| F. Operational   | Tools plus provenance, timestamps, examples, useful errors and traces     | What does a genuinely agent-ready environment add?    |

Do not tell participants which pack is expected to win.

### Make it a real experiment

Pair participants. Each pair uses the same model for two runs:

1. Open a fresh chat.
2. Use randomly assigned Pack X.
3. Paste the identical task.
4. Do not help the agent beyond the supplied instructions.
5. Submit the result in a fixed JSON format.
6. Repeat in another fresh chat with Pack Y.
7. Predict which result is better before seeing the automated score.

With approximately 15 pairs and two runs each, you get about 30 observations. Randomize pack order so that familiarity does not systematically favour the second run. Record the model and model mode so you can control for them later.

Score against hidden ground truth:

- 40% factual and numerical accuracy
- 20% evidence and provenance
- 15% appropriate uncertainty
- 10% completeness
- 10% efficiency: elapsed time, calls or approximate context size
- 5% safety: did it treat data as instructions or exceed permissions?

This becomes **Agent Data Readiness Benchmark v0.1**, not merely a workshop exercise.

---

# A four-hour workshop I would run

## 2:00–2:15 — Cold open: predict before learning

Show the six pack descriptions without results.

Ask participants:

- Which will perform best?
- Is cleaned and joined data more important than relationship descriptions?
- Would you rather give an agent a large table or five task-level tools?
- Is more context generally better?
- When documents and logs disagree, which should the agent trust?

Collect answers in your live form. These are the priors you compare against at the end.

Do almost no teaching yet.

## 2:15–2:50 — Experiment 1: the blind data-pack bake-off

Pairs run two assigned packs against the common task.

While agents run, show how to:

- use fresh chats
- share conversations
- submit the standardized output
- avoid helping the agent
- record unexpected behaviour

The live leaderboard should show pack-level averages, but initially hide pack names. Call them Red, Blue, Green, etc.

At the end, reveal which environment each colour represented.

### What participants learn

They experience, rather than merely hear, that:

- cleanliness is only one dimension
- semantics and source precedence matter
- more context can introduce distractions
- attractive outputs can be unsupported
- agents need recoverable interfaces
- provenance and calibration are separate from factual accuracy

### What you obtain

- 30 controlled agent traces
- model-by-pack comparisons
- accuracy and calibration measures
- participant predictions versus actual results
- an initial taxonomy of failure modes

## 2:50–3:20 — Failure autopsy: diagnose the environment, not the answer

Give each pair another team’s failed transcript.

Their job is not to fix the answer. It is to determine what was missing from the environment:

- identity rule?
- grain?
- relationship?
- business definition?
- example?
- source precedence?
- freshness?
- tool description?
- error message?
- permission boundary?
- retrieval filter?
- verification check?

Each pair submits one diagnosis and one minimal change.

Then ask an agent to cluster all diagnoses live. This produces the first empirical version of the **Agent Data Checklist**.

This is stronger than presenting the checklist yourself: the checklist emerges from observed failures.

## 3:20–3:50 — Experiment 2: the context compression tournament

Give everyone the best-performing complete pack.

Their task:

> Create the smallest possible “agent context pack” that still lets a fresh agent answer a new hidden task correctly.

Set a hard limit—perhaps 2,000 tokens or 8 KB. Participants may use an agent to compress the pack.

They must decide what survives:

- schema?
- relationships?
- examples?
- source hierarchy?
- raw rows?
- exceptions?
- known traps?
- tool instructions?
- validation checks?

Run the compressed packs on two hidden tasks.

Plot each submission on:

- X-axis: context size
- Y-axis: task score

The winners are on the Pareto frontier, not merely the smallest or most accurate.

### Tangible participant artifact

A reusable **context-pack compiler prompt**, such as:

> Inspect this repository and produce the smallest agent brief that preserves the information required to complete these task classes. Prefer rules, relationships, examples, source precedence and retrieval instructions over raw duplication. Explicitly list information you omitted and the tasks that omission may harm.

### Research asset

A dataset of:

- original context
- compressed context
- what humans or agents chose to retain
- hidden-task performance
- compression ratio
- failure caused by omission

This could become a genuinely interesting blog post or benchmark: **What information survives when humans optimize data for agent attention?**

## 3:50–4:05 — Break

Let longer agent runs continue.

## 4:05–4:45 — Experiment 3: tool-design relay

Split into a browser-friendly track and a coding track.

### Browser-friendly track: design tools without implementing them

Each team receives a set of low-level operations such as:

- fetch a customer row
- fetch all tickets
- fetch all payments
- search notes
- calculate SLA deadline
- look up policy

They must design three task-level tools.

For each tool, produce:

- name
- purpose
- when to use it
- when not to use it
- typed inputs
- typed outputs
- one good example
- one invalid example
- concise error messages
- provenance fields
- side-effect classification

For example, rather than:

```
query_table(table, filter)
```

they might create:

```
get_customer_risk_context(customer_id, as_of)
find_accounts_nearing_sla_breach(within_hours, minimum_revenue)
explain_customer_risk(customer_id)
```

Now swap tool catalogs. Another pair’s agent sees only the catalog and must produce a plan for solving three tasks.

Score:

- correct tool selected
- correct arguments
- unnecessary calls
- missing calls
- attempted unsafe actions
- whether the tool outputs would provide enough evidence

### Coding track: make the tools real

Give participants a DuckDB file and a minimal Python or JavaScript starter.

Ask their coding agent to implement three CLI functions or MCP tools, for example:

```
uv run tools.py accounts-at-risk --within-hours 48
uv run tools.py customer-context --customer-id C1042
uv run tools.py verify-risk --customer-id C1042
```

A second coding agent receives only the generated tool documentation and attempts the hidden tasks.

### The experiment

Vary one element across teams:

- tool names
- description detail
- strict versus loose schema
- examples versus no examples
- raw versus concise output
- generic versus recoverable error messages

You get a small but useful **Tool Description Benchmark**.

## 4:45–5:25 — Bring-your-own agent-ready makeover

Now participants use something they actually care about:

- a CSV
- a folder of reports
- documentation
- an API
- logs
- a database schema
- an analytics repository
- a dashboard export
- a collection of SOPs

Before modifying it, they ask a fresh agent to perform one useful real task and retain the result.

Then they ask an agent to produce an agent-facing package:

```
AGENT_README.md
schema.json
relationships.md
business-definitions.md
source-precedence.md
examples.jsonl
known-issues.md
provenance.json
evals.jsonl
checks.sql
```

Coders may also generate:

```
tools.py
mcp_server.py
```

They choose only the files relevant to their material. The point is not to create ceremonial documentation.

Then they rerun the original task in a fresh chat and compare:

- correctness
- time
- follow-up questions
- unsupported assumptions
- evidence quality
- confidence calibration

### Critical design choice: cross-test it

Do not let people evaluate only their own package.

Swap the artifact with another pair. The receiving pair has no tacit knowledge and asks their agent to use it.

This exposes the real gaps. Creators routinely assume context that consumers do not possess.

### Tangible participant takeaway

Each person leaves with:

- a before-and-after agent test
- an agent-facing README or context pack
- a small eval set
- optionally a tool wrapper
- a prioritized list of improvements

## 5:25–5:50 — Red-team the packages

Give every pair one adversarial card:

- a stale document
- two conflicting identifiers
- an undocumented unit
- misleading nulls
- an instruction hidden inside data
- a tool returning too many rows
- a tool returning an opaque error
- a log that records bad practice
- a source with no timestamp
- a field whose meaning changed halfway through history

They inject the issue into another team’s package and rerun its eval.

The package owner must improve the environment—not patch the final answer.

This produces the most useful failure corpus of the day.

## 5:50–6:00 — Reveal changed minds and publish

Repeat the opening questions.

Show:

- which pack won
- which dimension mattered most
- where more context hurt
- whether tools actually beat tables
- whether logs beat docs, or merely answered a different question
- which omissions damaged compressed packs
- which tool descriptions agents misunderstood
- which adversarial cases survived

End by generating the workshop’s **empirical checklist**, ranked by observed effect rather than your prior research.

---

# The most valuable experiments, ranked

| Rank | Experiment                        | Why it is valuable                                         | Participant leaves with                  | Asset you gain                          |
| ---- | --------------------------------- | ---------------------------------------------------------- | ---------------------------------------- | --------------------------------------- |
| 1    | Blind data-pack bake-off          | Directly tests the workshop’s central claim                | A felt understanding of agent-ready data | Controlled benchmark and traces         |
| 2    | BYO before/after makeover         | Transfers the learning to real work                        | An improved real artifact and eval       | Diverse real-world case library         |
| 3    | Context compression tournament    | Makes token budgeting concrete                             | Compact reusable context pack            | Accuracy-versus-context Pareto dataset  |
| 4    | Tool-design relay                 | Shows why tool interfaces are prompts                      | Tool schema and design checklist         | Tool-selection benchmark                |
| 5    | Cross-team usability test         | Removes creators’ tacit knowledge                          | Honest external feedback                 | Missing-context taxonomy                |
| 6    | Provenance and conflict challenge | Tests trust rather than mere answers                       | Source-precedence template               | Calibration and provenance benchmark    |
| 7    | Error-recovery clinic             | Demonstrates that errors are part of the interface         | Recoverable error patterns               | Error-message A/B results               |
| 8    | Logs-versus-docs ablation         | Tests one of your strongest hypotheses                     | Better sense of policy versus practice   | Evidence on when logs help or mislead   |
| 9    | Prompt-injection minefield        | Makes data/tool safety visceral                            | Untrusted-content separation pattern     | Safety failure corpus                   |
| 10   | Discoverability scavenger hunt    | Tests whether agents can find assets before using them     | Metadata and catalog template            | Search/discovery benchmark              |
| 11   | Freshness time-travel test        | Shows that “correct” depends on time                       | Timestamp and validity conventions       | Staleness failure dataset               |
| 12   | Agent-generated data engineering  | Tests whether agents can create the environment themselves | Generated docs, schemas and checks       | Human-versus-agent packaging comparison |

---

# Particularly interesting hypotheses to test

These would make the workshop more than a training session.

## 1. Relationship descriptions versus joined data

Does a concise explanation of grain, keys, identity and source precedence outperform a pre-joined “golden table” on complex questions?

My expectation: the joined table wins simple lookup tasks; relationship context wins tasks involving uncertainty, changing identity and explanation.

## 2. Examples versus documentation

Give one group 1,000 words of documentation and another group five representative examples.

Test which performs better across common and edge cases.

## 3. More context versus better retrieval

Compare:

- all files uploaded
- only a compact context pack
- a search/retrieval interface
- task-specific tools

This reveals where context overload begins to hurt.

## 4. Logs versus docs

Do not frame this merely as “logs beat docs.”

Test separately:

- What is the official rule?
- What normally happens?
- What happened in this case?
- What should happen next?

Docs may win the first; logs may win the next two. Neither alone reliably answers the fourth.

## 5. Preserving ambiguity versus manufacturing one truth

Give agents conflicting but legitimate sources.

Compare:

- a single reconciled field
- both values without explanation
- both values with provenance and source-precedence rules

Measure whether the agent appropriately preserves uncertainty.

## 6. Generic tools versus task-level tools

Compare:

```
query_database(sql)
```

with:

```
find_accounts_nearing_sla_breach(...)
```

The generic tool is more flexible. The task tool may be more reliable, cheaper and safer. The crossover point is worth discovering.

## 7. Helpful errors versus accurate errors

Compare:

```
Invalid input.
```

with:

```
customer_id "1042" was not found. IDs begin with "C".
Two possible matches are C1042 and C1402.
```

Measure recovery without human intervention.

## 8. Agent-generated context versus human-generated context

Have half the pairs author the context pack themselves. Have the other half ask an agent to inspect the repository and produce it.

Cross-test both on hidden tasks.

This could answer an important practical question: how much of “engineering data for agents” can agents already perform?

---

# The live form should capture more than links

Your Data Stories form captured prior confidence, intended analysis, chat links, visualizations, changed minds and Monday actions: `2026-06-13-data-stories-with-ai/form.yaml:20-44`.

For this workshop, collect:

- anonymous participant or team ID
- role
- model and mode
- pack ID and task ID
- randomized order
- predicted winning pack
- start and finish time
- shared chat link
- standardized final JSON
- confidence in the answer
- whether the answer cited sources
- observed failure types
- minimal environmental change proposed
- before/after artifact links
- what changed their mind
- one change they will make to their data systems

Do not rely only on screenshots or free-text impressions. The standardized answer and hidden ground truth are what turn the session into a benchmark.

## Suggested result schema

```
{
  "entities_selected": [
    {
      "customer_id": "C1042",
      "risk_score": 0.91,
      "revenue_at_risk": 24000,
      "reason": "...",
      "evidence": [
        {
          "source": "tickets.jsonl",
          "record_id": "T8821",
          "as_of": "2026-07-06"
        }
      ],
      "uncertainties": ["..."],
      "recommended_action": "..."
    }
  ],
  "total_revenue_at_risk": 86000,
  "missing_information": ["..."],
  "confidence": 0.84
}
```

---

# Assets you could publish afterward

The session could produce a coherent family of assets rather than miscellaneous workshop outputs.

### 1. Agent Data Readiness Benchmark

A CC0 repository containing:

- common underlying dataset
- six interface variants
- task suite
- hidden-answer scorer
- anonymized model outputs
- analysis notebook
- leaderboard

### 2. Agent-Ready Data Starter Kit

Templates for:

- repository README
- schema
- relationship map
- source hierarchy
- provenance
- examples
- errors
- evals
- tool definitions

### 3. Context Compression Corpus

Original repository, compressed packs, token counts and hidden-task scores.

### 4. Tool Description Corpus

Poor tool specifications, participant improvements, tool-selection results and recovery outcomes.

### 5. Failure Atlas

Actual examples of:

- wrong joins
- fabricated certainty
- stale facts
- missed exceptions
- tool confusion
- excessive retrieval
- prompt injection
- opaque failures
- unsupported actions

### 6. Empirical Agent Data Checklist

Not “30 best practices found online,” but:

> These practices produced the largest measured improvements across these tasks, models and participants.

That is a substantially stronger asset.

---

# What I would not do

I would avoid starting with a long tour of MCP, `llms.txt`, JSON Schema, RAG, vector databases and context engineering terminology. Those can be introduced only after participants encounter the problem each solves.

I would also avoid beginning with bring-your-own data. Different domains, file sizes, privacy constraints and task difficulty make collective learning weak. Start with one controlled corpus; apply it to personal material only after the shared experiment.

Do not make custom MCP development mandatory. Setup friction will consume the workshop. Keep the primary experiments browser-compatible and offer a coding track for those with `uv`, Node.js and DuckDB.

Most importantly, do not compare attractive final answers. Compare task success, evidence, calibration, efficiency and recovery. Otherwise the workshop risks measuring fluency rather than agent readiness.

## The three things I would definitely run

1. **The blind six-pack bake-off** to discover what actually helps agents.
2. **The context compression tournament** to make token budgeting and information selection tangible.
3. **The cross-tested BYO makeover** so every participant leaves with a useful real artifact.

Those three create a coherent arc:

**Discover what matters → optimize it → apply it to your own data.**

---

---
title: "When Data is for Agents Fifth Elephant Workshop Prep"
date: 2026-07-11T15:25:43+05:30
source: "https://claude.ai/chat/e48c26cc-42e3-4b7c-8677-0bbc70f310b4"
---

## User

I'm delivering this workshop: [https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/)

Read it. You can also find it on Local MCP at ~/Dropbox/notes/talks.md.

I've included material below from ChatGPT on the modern best practices on how to structure and optimize content and data for agent consumption - some of which I might cover in the workshop (or maybe not - I'll decide last minute) and might be useful additional context for you.

Analyze how I run my workshops based on the transcripts at ~/code/talks/\*_/transcript_.md and other files. In particular, see these workshops:

2026-04-08-ai-workshop-lbsnaa 2025-12-06-mining-digital-exhaust 2026-05-23-ai-unboxed-context-engineering 2025-09-16-vibe-analysis

That'll tell you the style.

Now, here are a few questions:

1. Zainab from Hasgeek asked if the page needs any additional content. Does it?
2. She also asked me to send an update on why this workshop and who is it relevant for. Take a look at updates from other workshops, see what they cover and which of these are likely to be most effective (use an expert-lens) and craft a similar one written in my style.
3. She also asked me to create a LinkedIn post. See how I write my LinkedIn posts at ~/Documents/data/linkedin-posts.jsonl and draft me something in that style.

<CHATGPT> I read the public Hasgeek page and the matching LocalMCP note at `/home/vscode/Dropbox/notes/talks.md:137-150`. Your workshop premise is right on the frontier: when agents consume data, the unit of design shifts from dashboards, normalized tables, and polished docs to context budgets, tool affordances, relationship descriptions, traces, schemas, and verification loops. The public page already frames the key provocation: “optimize for token budgets instead of disk or query cost,” with “tools beat tables” and “logs beat docs” as core hypotheses. ([Hasgeek][1]) The strongest consensus across OpenAI, Anthropic, MCP, Microsoft/NLWeb, Google A2A, and recent research is this: agent-ready data is not “clean data” alone. It is a controlled context-and-tool surface that lets an agent discover, retrieve, reason, act, verify, and recover cheaply. Ranked below by combined impact + frequency across the sources. ## Top techniques for structuring data/content for agents 1. **Optimize for context, not storage.** Keep the smallest high-signal token set in the model’s attention: relevant instructions, current state, task facts, examples, tool docs, and retrieved snippets. Anthropic explicitly frames context engineering as curating finite attention, not maximizing context length; it warns about “context rot” and says more context is not automatically better. ([Anthropic][2]) For your workshop: “Data engineering for agents begins by asking: what must fit in attention right now?” 2. **Expose task-level tools, not raw databases or API endpoints.** Agents perform better when APIs are wrapped into workflow-level tools such as `search_logs`, `get_customer_context`, or `schedule_event`, rather than one tool per low-level endpoint. Anthropic says not to wrap every endpoint and recommends fewer high-impact workflow tools; OpenAI similarly recommends combining functions that are always called in sequence and offloading work from the model into code. ([Anthropic][3]) Workshop line: “Tables are ingredients. Tools are recipes.” 3. **Use strict schemas for tool inputs and outputs.** JSON Schema, Pydantic/Zod models, MCP input/output schemas, and OpenAI structured outputs reduce ambiguity and make failures detectable. OpenAI recommends strict mode for function calling and says structured outputs ensure responses adhere to a schema; MCP tool results can include `structuredContent` that conforms to an output schema. ([OpenAI Platform][4]) Practical move: every agent-facing function should have typed inputs, typed outputs, examples, and explicit error cases. 4. **Treat tool descriptions as prompts.** Tool names, descriptions, examples, edge cases, and argument docs are part of the agent’s working prompt. Anthropic says tool descriptions need as much prompt-engineering care as normal prompts; OpenAI recommends detailed function descriptions, clear enums, and an “intern test” for whether a human could call the tool correctly from the docs alone. ([Anthropic][5]) Bad: `get_data(query)`. Better: `find_customer_orders(customer_name, date_range, status)` with usage boundaries. 5. **Return high-signal results, not complete dumps.** Tool outputs should be concise, semantically meaningful, and directly useful for next action. Anthropic recommends returning stable human-readable identifiers, only necessary fields, surrounding context where useful, and configurable `concise` versus `detailed` modes. It also recommends pagination, range selection, filtering, and helpful truncation messages. ([Anthropic][3]) Workshop exercise: take a 100-column customer row and design a 12-field agent result. 6. **Add provenance to everything.** Every retrieved fact should carry source, timestamp, owner, confidence, transformation lineage, and ideally a link or resource URI. MCP resources include URI, name, description, MIME type, size, and annotations such as audience, priority, and last modified; OpenAI retrieval returns relevant chunks, similarity scores, and file of origin. ([Model Context Protocol][6]) Agent-ready fact = value + why it is trustworthy + where it came from. 7. **Use hybrid retrieval: semantic + keyword + metadata filters.** Pure vector search is not enough for enterprise data. OpenAI’s retrieval docs describe semantic search, query rewriting, file attributes, filters, similarity scores, and hybrid search using reciprocal rank fusion. ([OpenAI Developers][7]) Best practice: index chunks with embeddings, but filter by business metadata such as product, region, date, owner, document type, sensitivity, and freshness. 8. **Use progressive disclosure.** Do not preload all relevant data. Give the agent lightweight handles first: filenames, IDs, schema summaries, row counts, sample rows, `head`, `tail`, search tools, and drill-down tools. Anthropic recommends just-in-time context through targeted queries, file paths, naming, timestamps, and progressive exploration. ([Anthropic][2]) This is the agent equivalent of “don’t paste the whole warehouse into the prompt.” 9. **Publish LLM-native documentation.** Use clean Markdown, stable URLs, and `/llms.txt` indexes that point models to the most useful docs. The `llms.txt` proposal exists because websites are too large, noisy, and JavaScript-heavy for inference-time use; it recommends concise Markdown guidance and clean `.md` versions of important pages. Cloudflare now publishes product-specific `llms.txt` files for its docs. ([llms-txt][8]) For internal data portals: add `/llms.txt`, `/schema.md`, `/examples.md`, `/known_issues.md`. 10. **Adopt MCP as the agent-facing data/tool surface.** MCP standardizes how apps expose resources, tools, and prompts. Resources expose contextual data such as files, schemas, and app-specific information; tools let models query databases, call APIs, and compute; prompts provide reusable interaction templates. ([Model Context Protocol][6]) Workshop framing: MCP is less “integration plumbing” and more “the contract by which agents see the organization.” 11. **Separate resources, tools, and prompts.** A resource says “here is context,” a tool says “here is an action or computation,” and a prompt says “here is a reusable procedure.” MCP formalizes this separation, and OpenAI’s Agents SDK supports MCP servers, strict schema conversion, approval controls, prompt reuse, and tracing. ([Claude Platform Docs][9]) This is a useful design lens for any dataset: what should be read, what should be called, what should be templated? 12. **Describe relationships, grain, and business semantics near the data.** Agents can join and transform data, but they need to know grain, entity identity, join ambiguity, units, slowly changing dimensions, business definitions, and exception rules. Your workshop note explicitly says relationship descriptions may matter more than pre-joined clean data; Microsoft’s NLWeb similarly leans on Schema.org/RSS semi-structured formats to expose site semantics for agents. ([Hasgeek][1]) A useful artifact: `relationships.md` beside every dataset. 13. **Prefer live governed connectors over stale duplicated corpora.** NLWeb’s docs note that production systems may connect to live databases instead of duplicating content, specifically to avoid freshness problems. MCP also emphasizes access controls, URI validation, and permission checks. ([GitHub][10]) The agent should query the governed source of truth when freshness matters, but retrieve summarized snapshots when cost or latency matters. 14. **Keep the active toolset small.** Tool definitions consume context. OpenAI recommends starting with fewer than 20 loaded functions, shortening descriptions when needed, and using tool search for larger toolsets. Anthropic recommends namespacing tools by service/resource and avoiding overlapping tools. ([OpenAI Platform][4]) Agent consumption pattern: discover broadly, load narrowly. 15. **Use namespacing and clear tool taxonomy.** Tool names influence selection. Names like `gmail.search`, `calendar.create_event`, `warehouse.query_sales`, and `crm.get_customer_context` reduce ambiguity. Anthropic specifically recommends namespacing tools and says naming affects evaluation performance. ([Anthropic][3]) 16. **Build eval harnesses for agent consumption.** Evaluate whether agents can use the data/tools to complete realistic tasks. Anthropic recommends real-world, complex, verifiable eval tasks and tracking tool calls, token usage, errors, latency, and success. It also recommends analyzing transcripts and using agents themselves to improve tool descriptions and interfaces. ([Anthropic][3]) Your workshop could include: “Here is a dataset. Write 10 verifiable tasks an agent should be able to complete.” 17. **Make logs and traces first-class data.** Logs show what agents actually needed, where they failed, which fields/tools were unused, and which errors confused them. Anthropic recommends analyzing transcripts and tool-call metrics to improve agent tools; OpenAI’s MCP guidance highlights tracing and approval policies around MCP servers. ([Anthropic][3]) This supports your “logs beat docs” hypothesis: docs describe intent; logs reveal friction. 18. **Design errors as recovery instructions.** Error messages should say what failed, why, what valid inputs look like, and what to try next. OpenAI recommends making invalid states unrepresentable through enums/object structure; Anthropic recommends helpful truncation/error responses that steer agents toward token-efficient strategies. ([OpenAI Platform][4]) 19. **Use compaction and structured memory for long tasks.** Long-horizon agents need periodic summaries, notes, state files, and memory artifacts. Anthropic describes compaction, structured note-taking, tool-result clearing, and subagents returning condensed summaries as context-management techniques. ([Anthropic][2]) Agent-ready repository pattern: `PLAN.md`, `STATE.md`, `DECISIONS.md`, `OPEN_QUESTIONS.md`, `EVIDENCE.md`. 20. **Use subagents for wide exploration, then return condensed evidence.** Anthropic lists orchestrator-worker and subagent patterns for complex work where different subtasks need separate context windows. The main agent should receive compact summaries, evidence, and next actions rather than raw exploration logs. ([Anthropic][5]) 21. **Compile repeated agent work into deterministic workflows.** When the same multi-step path recurs, convert it into code, SQL, a workflow tool, or a declarative plan. Anthropic recommends workflow-level tools; recent research on MCP workflow engines reports large token savings by replacing repeated reasoning with declarative workflow blueprints. ([Anthropic][3]) This is the agent version of “don’t reason every time; operationalize what worked.” 22. **Use web-native agent protocols: NLWeb and A2A.** Microsoft’s NLWeb exposes websites through natural-language interfaces, Schema.org/RSS data, JSON responses, and MCP endpoints. Google’s A2A protocol focuses on agent-to-agent capability discovery, task management, artifacts, and multimodal message parts. ([GitHub][10]) Emerging pattern: websites become callable agents, not just pages. 23. **Use canonical examples, not giant rulebooks.** Anthropic recommends diverse canonical examples rather than exhaustive edge-case lists. Examples should teach the agent the intended pattern, format, and failure handling. ([Anthropic][2]) Good data docs should include “3 good queries, 3 bad queries, 3 edge cases.” 24. **Use human approvals and side-effect labels for risky tools.** MCP tools can be dangerous because they may trigger external side effects. MCP recommends human-in-the-loop controls; OpenAI’s Agents SDK supports approval policies for MCP servers and per-tool approval maps. ([Model Context Protocol][11]) Classify tools: read-only, write, destructive, external-world, financial, privacy-sensitive. 25. **Do not fetishize one format. Test formats by task and model.** Anthropic says to choose formats that are easy for models and reduce overhead, often internet-familiar formats; recent research comparing YAML, Markdown, JSON, and TOON found model capability and schema architecture mattered more than format alone. ([Anthropic][5]) Practical rule: Markdown for explanation, JSON for contracts, CSV/Parquet for bulk data, SQL for relational access, XML-ish tags for prompt segmentation, but benchmark. 26. **Partition context by domain/task, not only by normalized schema.** Recent file-native agent research found domain-partitioned schemas can scale better for large schema spaces, and that file size is not the same as token/runtime cost. ([arXiv][12]) For enterprise data: create agent-facing “task packs” such as `sales_renewal_context`, `invoice_dispute_context`, or `student_risk_context`. 27. **Make UI and web interactions machine-describable.** Emerging web-agent research shows that structured interaction metadata can reduce processing requirements while preserving high task success. Related work on web list extraction converts demonstrations into repeatable programs rather than repeatedly asking agents to inspect pages manually. ([arXiv][13]) This matters when agents operate browsers, dashboards, CRMs, and admin consoles. 28. **Add freshness, priority, audience, and sensitivity metadata.** MCP resources support annotations such as audience, priority, and last modified; OpenAI vector-store files support attributes for filtering. These help agents decide what to retrieve, trust, skip, or escalate. ([Model Context Protocol][6]) 29. **Separate untrusted content from instructions.** Data retrieved from emails, web pages, tickets, or docs may contain prompt injection. MCP warns that tool annotations should be treated as untrusted unless they come from trusted servers, and its resource guidance includes URI validation, access controls, and permission checks. ([Model Context Protocol][11]) Agent-ready data should label instruction-bearing text, quoted user text, external content, and system policy separately. 30. **Make “agent readiness” measurable.** Track task success, verification pass rate, retries, tool-call count, token cost, latency, irrelevant retrieval rate, schema validation failures, human escalations, and stale-source usage. Anthropic’s tool guidance explicitly recommends runtime metrics and held-out evals; OpenAI emphasizes strict schemas, tracing, and tool-result validation patterns. ([Anthropic][3]) ## The workshop’s strongest teachable synthesis The old stack optimized for humans: tables, dashboards, reports, and docs. The agent stack optimizes for repeated autonomous work: compact context, discoverable tools, typed contracts, semantic metadata, provenance, retrieval, memory, logs, evals, and governed actions. Your most useful workshop artifact could be a one-page “Agent-Ready Data Checklist”: “Can an agent discover this? Can it understand the grain and relationships? Can it retrieve only what it needs? Can it call the right tool safely? Are inputs and outputs typed? Is provenance attached? Are errors recoverable? Is freshness visible? Are risky actions gated? Can we evaluate whether the agent succeeded?” That checklist captures the modern best practice better than “clean your data.” [1]:_ [https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/)
"When data is for Agents, not humans" [2]:_ [https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
"Effective context engineering for AI agents \ Anthropic" [3]:_ [https://www.anthropic.com/engineering/writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
"Writing effective tools for AI agents—using AI agents \ Anthropic" [4]:_ [https://platform.openai.com/docs/guides/function-calling](https://platform.openai.com/docs/guides/function-calling)
"Function calling | OpenAI API" [5]:_ [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
"Building Effective AI Agents \ Anthropic" [6]:_ [https://modelcontextprotocol.io/docs/concepts/resources](https://modelcontextprotocol.io/docs/concepts/resources)
"Resources - Model Context Protocol" [7]:_ [https://developers.openai.com/api/docs/guides/retrieval](https://developers.openai.com/api/docs/guides/retrieval)
"Retrieval | OpenAI API" [8]:_ [https://llmstxt.org/](https://llmstxt.org/)
"The /llms.txt file – llms-txt" [9]:_ [https://docs.anthropic.com/en/docs/agents-and-tools/mcp](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)
"What is the Model Context Protocol (MCP)? - Model Context Protocol" [10]:_ [https://github.com/microsoft/NLWeb](https://github.com/microsoft/NLWeb)
"GitHub - nlweb-ai/NLWeb: Main reference implementation for NLWeb, implemented in Python. · GitHub" [11]:_ [https://modelcontextprotocol.io/docs/concepts/tools](https://modelcontextprotocol.io/docs/concepts/tools)
"Tools - Model Context Protocol" [12]:_ [https://arxiv.org/abs/2602.05447?utm_source=chatgpt.com](https://arxiv.org/abs/2602.05447?utm_source=chatgpt.com)
"Structured Context Engineering for File-Native Agentic Systems: Evaluating Schema Accuracy, Format Effectiveness, and Multi-File Navigation at Scale" [13]:\* [https://arxiv.org/abs/2508.09171?utm_source=chatgpt.com](https://arxiv.org/abs/2508.09171?utm_source=chatgpt.com)
"webMCP: Efficient AI-Native Client-Side Interaction for Agent-Ready Web Design" </CHATGPT>

---

## Claude

<details>
<summary>Orchestrated multi-source analysis to synthesize workshop content strategically</summary>

> I need to understand what Anand is asking for his workshop delivery. He wants me to review the Hasgeek page and his notes, then analyze his workshop style from transcripts to answer three specific questions: whether the Hasgeek page needs more content, write an update about the workshop's relevance in his voice, and create a LinkedIn post matching his style.
>
> For this substantive task, I should apply the relevant skills he's mentioned—particularly the expert-lens approach he explicitly requested, his writing style, and his objectives. My workflow will be to read the necessary skill files first, then fetch the Hasgeek page, pull his notes and workshop transcripts to understand his approach, and examine his existing LinkedIn posts and workshop updates before tackling the three questions.
>
> I need to be careful about file access since the paths reference his local machine (~/Dropbox, ~/code/talks, ~/Documents), which means I'll need to use the Local MCP bash tool rather than my container bash to reach those files.
>
> Let me prioritize reading the key skills he explicitly mentioned—expert-lens and anand-writing-style—along with anand-objectives, then fetch the Hasgeek page and start pulling in the talks.md file and workshop transcripts.
>
> Done

</details>

<details>
<summary>Orchestrated multi-source analysis to synthesize workshop guidance comprehensively</summary>

> Reading the expert-lens skill since Anand explicitly asked me to use it
>
> I'm looking at the anand-writing-style skill to understand the style guidelines.
>
> Reading Anand's writing style skill since he wants the update and LinkedIn post in his style
>
> I should look at the anand-objectives skill since it has broad applicability.
>
> Reading anand-objectives skill which applies broadly to substantive answers
>
> I should check the blind-spot skill since it directly addresses what's missing from the content—that's key for evaluating whether the page needs anything else.
>
> Reading blind-spot skill - relevant for Q1 about what the page might be missing
>
> I'm going to retrieve the Hasgeek workshop page.
>
> Done

</details>

<details>
<summary>Reconciling file paths and preparing comprehensive analysis</summary>

> - [When data is for Agents, not humans](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/) - hasgeek.com
>   I need to load the local MCP bash tool so I can access the files I'll need—talks.md, transcripts, LinkedIn posts, and existing workshop updates—to understand the format and content I'm working with.
>
> Done

</details>

<details>
<summary>Strategically ingesting workshop transcripts and README structures</summary>

> Found tools
>
> Request
>
> `{ "query": "bash run shell command local" }`
>
> Response
>
> `Loaded 1 Local MCP tool: Local MCP:bash: commands: string timeout_ms?: integer These tools are now available for you to call directly. <functions> <function>{"description": "Runs multiline bash script. Under `~`=`/home/vscode/` (`/home/sanand`also works) you have: - ~/Dropbox/notes/transcripts/YYYY-MM-DD*.md - date-window by filename, then read narrow ranges - ~/Documents/data/ - s.anand@gramener.com/ and root.node@gmail.com/ - email, chat, calendar exports. Use`gws`for latest - whatsapp/ - whatsapp exports. Use`jaq`fields`.time`, `.author`, `.text`. - browsing-history.db (SELECT url, timestamp, visit_count, ... FROM activity) - linkedin-invites.json - ~/code/talks/README.md - talk transcripts, slides - ~/code/datastories/config.json - data stories - ~/code/llmdemos/config.json - innovation team demos - ~/code/llmevals/README.md - LLM evals - ~/code/blog/description.md - 20K files, 5K posts. Search for \"- llm\" for AI-related posts. - ~/code/til/README.md - things I learnt - ~/code/scripts/agents/*/SKILL.md - agent skills - ~/code/README.md - code repos - ~/r2/files/podcast - podcasts written for myself - ~/Documents/activities/ - daily activity logs Avoid broad scans over `$HOME`, `~/.\*`, `~/code`, `~/Documents`, or archives unless necessary. Scope to known subdirs. Prefer `fd`/`rg`because they respect`.gitignore`by default. Check shape (dir count, file size, match count, ...) first. First locate candidate files with`fd`, `rg -l`, `rga -l`, READMEs/configs/indexes. THEN inspect the best files with `path:line` evidence. Paths contain spaces. Prefer null-delimited loops (`fd -0`, `xargs -0`). This is not Code Interpreter. There's no `/mnt/data`. Use /tmp or user/repo paths. CLI tools: fd/rg, rga for binary docs, jaq (faster jq), duckdb/sqlite3, sg (at search), git/gh, agent-browser, ... Prefer `uv run --with pkg1 --with pkg2 -- python - <<'PY'`over`python`. gws can access email, calendar, chat: gws gmail users messages list --params '{\"userId\":\"me\", \"q\": \"from:...\"}' gws calendar events list --params '{\"calendarId\":\"s.anand@straive.com\",\"timeMin\":\"...\",\"timeMax\":\"...\",\"singleEvents\":true,\"orderBy\":\"startTime\"}' Verify paths with `pwd`, `ls`, or `test -e`before deep scans. Use`set -euo pipefail` for deterministic scripts. Handle expected misses (`rg ... || true`, `test -e`, optional files) printing concise diagnostics. Capped pipelines like `rg ... | head`can exit 141 from SIGPIPE. Wrap expected capped/no-match pipelines in`( ... | head -N || true )`. Batch related probes into one script with section headers. Avoid re-running identical discovery commands unless new evidence changed the scope. Keep stdout bounded to ~200 lines/ ~20KB. Save large intermediate output to /tmp; print only summaries and paths. Do not print secrets, tokens, or credentials, unless explicitly requested. Summarize and cite paths/lines instead.", "name": "Local MCP:bash", "parameters": {"additionalProperties": false, "properties": {"commands": {"type": "string"}, "timeout_ms": {"default": 30000, "type": "integer"}}, "required": ["commands"], "type": "object"}}</function> </functions>`
>
> I've got the Local MCP bash tool available now, and I'm noticing some discrepancies between the paths you mentioned and what the tool documentation shows. Let me start exploring the actual file structure to see what's really there and reconcile these differences.
>
> Confirming container vs Local MCP separation
>
> Script
>
> I need to use the Local MCP bash tool to find Anand's files and see what I'm working with.
>
> Bash
>
> Request
>
> `{ "commands": "set -uo pipefail echo \"=== talks.md ===\" test -e ~/Dropbox/notes/talks.md && echo \"FOUND ~/Dropbox/notes/talks.md\" || echo \"MISSING\" echo echo \"=== talks dir ===\" fd -t d . ~/code/talks --max-depth 1 2>/dev/null | head -50 echo echo \"=== target workshop dirs ===\" for d in 2026-04-08-ai-workshop-lbsnaa 2025-12-06-mining-digital-exhaust 2026-05-23-ai-unboxed-context-engineering 2025-09-16-vibe-analysis; do echo \"--- $d ---\" fd . ~/code/talks -t d -t f 2>/dev/null | rg -i \"$d\" | head -20 || echo \"none\" done echo echo \"=== linkedin posts ===\" test -e ~/Documents/data/linkedin-posts.jsonl && (echo \"FOUND\"; wc -l < ~/Documents/data/linkedin-posts.jsonl) || echo \"MISSING linkedin-posts.jsonl\" fd linkedin ~/Documents/data 2>/dev/null | head" }`
>
> Response
>
> `=== talks.md === FOUND ~/Dropbox/notes/talks.md === talks dir === /home/vscode/code/talks/2022-02-20-it-doesnt-have-to-be-us-and-them-rajen-makhijani/ /home/vscode/code/talks/2022-03-07-career-principles-with-rajen-makhijani/ /home/vscode/code/talks/2024-10-19-ai-in-education-webinar/ /home/vscode/code/talks/2025-01-18-how-to-use-ai-to-generate-code/ /home/vscode/code/talks/2025-05-10-vibe-coding/ /home/vscode/code/talks/2025-06-27-data-design-by-dialogue/ /home/vscode/code/talks/2025-06-28-prompt-to-plot/ /home/vscode/code/talks/2025-06-pycon-sg/ /home/vscode/code/talks/2025-07-13-goodbye-mba-hello-ai/ /home/vscode/code/talks/2025-07-18-tug-true-but-irrelevant-rob-schrauwen/ /home/vscode/code/talks/2025-07-23-supply-chain-automl/ /home/vscode/code/talks/2025-07-24-pugs-agent-loop/ /home/vscode/code/talks/2025-08-11-social-code-analysis/ /home/vscode/code/talks/2025-08-21-ai-coding-guide/ /home/vscode/code/talks/2025-08-21-rip-data-scientists/ /home/vscode/code/talks/2025-09-13-duckdb-is-the-new-pandas/ /home/vscode/code/talks/2025-09-15-llm-ama-gale/ /home/vscode/code/talks/2025-09-16-vibe-analysis/ /home/vscode/code/talks/2025-09-18-llm-ama-bi-worldwide/ /home/vscode/code/talks/2025-09-20-kiran-homelabbing-with-bare-metal/ /home/vscode/code/talks/2025-09-21-making-open-data-useful/ /home/vscode/code/talks/2025-09-21-zainab-building-a-culture-of-openness/ /home/vscode/code/talks/2025-09-22-llm-trends/ /home/vscode/code/talks/2025-09-llm-workflows/ /home/vscode/code/talks/2025-10-16-vibe-analysis/ /home/vscode/code/talks/2025-10-23-vibe-coding/ /home/vscode/code/talks/2025-10-29-llm-data-visualization/ /home/vscode/code/talks/2025-11-06-llm-psychology/ /home/vscode/code/talks/2025-11-13-nirmal-impress-ai-hr/ /home/vscode/code/talks/2025-11-15-applied-vibe-coding/ /home/vscode/code/talks/2025-12-03-vibe-analytics-iim-alumni-sg/ /home/vscode/code/talks/2025-12-05-scdm-keynote/ /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/ /home/vscode/code/talks/2026-01-11-nptel-vibe-coding-workshop/ /home/vscode/code/talks/2026-01-20-agentic-ai-in-action-deloitte/ /home/vscode/code/talks/2026-02-11-amat-dt-day/ /home/vscode/code/talks/2026-02-26-vibe-coding-for-humanities-ashoka/ /home/vscode/code/talks/2026-03-12-nie-ai-roadmap/ /home/vscode/code/talks/2026-03-15-how-students-learn-python/ /home/vscode/code/talks/2026-03-15-pyconf-ai-in-sdlc/ /home/vscode/code/talks/2026-03-18-iitm-academic-council/ /home/vscode/code/talks/2026-03-18-iitm-office-of-institutional-advancement/ /home/vscode/code/talks/2026-03-18-verifiable-agents/ /home/vscode/code/talks/2026-03-20-intequant-advisors/ /home/vscode/code/talks/2026-03-21-design-in-the-age-of-infinite-generativity/ /home/vscode/code/talks/2026-03-21-faculty-ai-transformation-nie/ /home/vscode/code/talks/2026-03-26-hack-of-the-day-toi/ /home/vscode/code/talks/2026-04-06-innovation-as-a-frontier-straive/ /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/ /home/vscode/code/talks/2026-04-08-frontiers-in-technology-debjani-lbsnaa/ === target workshop dirs === --- 2026-04-08-ai-workshop-lbsnaa --- /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/ /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/cabinet-briefing-sketchnote.avif /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/defiant-ias-officers-chatgpt-research.md /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/defiant-ias-officers-claude-research.md /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/iimb-whatsapp-group.html /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/index.html /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/nfsa-analysis.html /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/prompts.md /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/sketchnote.avif /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/transcript.md --- 2025-12-06-mining-digital-exhaust --- /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/ /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/README.md /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/activities.md /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/cycling.webp /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/digital-exhaust-notes.md /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/double-hump.webp /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/index.html /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/playstore-story.html /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/sketchnote.webp /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/topic-modeling.webp /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/trades.webp /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/transcript.md /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/whatsapp-thread.json /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/youtube-story.html /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/youtube.webp --- 2026-05-23-ai-unboxed-context-engineering --- /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/ /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/ /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/argue-against-my-blog-posts-and-find-errors.md /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iim-alumni-singapore-workshops-content-chagpt.md /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iim-alumni-singapore-workshops-content-claude.md /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iim-sg-alumni-workshop-context-engineering-prep.md /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iim-singapore-alumni-ai-workshop-plan.md /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iimpact-ai-unboxed-teams-background-design-gemini.md /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iimpact-ai-unboxed-teams-background-design.md /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/memory-test-on-gemini.md /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/public-profile-of-anand.md /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/comic-page.avif /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/index.html /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/prompts.md /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/teams-backgrounds.avif /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/transcript.md --- 2025-09-16-vibe-analysis --- /home/vscode/code/talks/2025-09-16-vibe-analysis/ /home/vscode/code/talks/2025-09-16-vibe-analysis/README.md /home/vscode/code/talks/2025-09-16-vibe-analysis/activities.md /home/vscode/code/talks/2025-09-16-vibe-analysis/cooking-insights.webp === linkedin posts === FOUND 3278 /home/vscode/Documents/data/linkedin-invites.json /home/vscode/Documents/data/linkedin-posts.jsonl`
>
> Now I'm gathering the key files to review—the workshop notes around those specific lines, the four transcripts, the LinkedIn posts file, and any other workshop documentation that might have updates.
>
> Bash
>
> Request
>
> `{ "commands": "set -uo pipefail echo \"=== talks.md: total lines ===\" wc -l ~/Dropbox/notes/talks.md echo echo \"=== talks.md lines 120-175 (the workshop note) ===\" sed -n '120,175p' ~/Dropbox/notes/talks.md" }`
>
> Response
>
> `=== talks.md: total lines === 3769 /home/vscode/Dropbox/notes/talks.md === talks.md lines 120-175 (the workshop note) === # Building Verification Harnesses, Fifth Elephant Workshop https://hasgeek.com/fifthelephant/fifthelephant-2026-call-for-submissions/sub/building-verification-harnesses-JCxuCWWTNAP1VGDezE6RhZ - Via https://claude.ai/chat/ebdaa2a9-f26c-467f-b17b-218bb9f8b85e To confidently deploy in production, you need a robust verification mechanism. Some verification mechanisms are easy. Wrong code doesn't compile or pass good test cases. Wrong analysis doesn't meet a post-condition - say a value range or a known aggregate. Wrong proofs don't validate on LEAN. But how far can we take it? When we have an insurance claim, could InsurLE help us verify its validity? Could Catala help us verify the legality of a contract?When an engineer generates a circuit, could we simulate it on SPICE? Use SHACL validated knowledge graphs to verify drug details? In this workshop, you'll explore a variety of different problems that are more verifiable than we thought. That lets us run build and deploy agents far more reliably. You will also be _creating_ verification harnesses where none existed before - which is the bottleneck since agents have driven the generation cost to almost zero. This session is for AI developers who need to ship verifiale agents into production - e.g. in a regulated or high-trust environment (finance, healthcare, government). {Add the link to draft slides - PDF/PPT - with comments access - TODO: at least a TOC or blog series} {Add the link to 2-min elevator pitch video - Um... skip, please?} # When Data is for Agents, Not Humans, Fifth Elephant Workshop, 07 Jul 2026 https://hasgeek.com/fifthelephant/fifthelephant-2026-call-for-submissions/sub/when-data-is-for-agents-not-humans-RPJ3syxmspKua6ADd44mD6 - Via https://claude.ai/chat/ebdaa2a9-f26c-467f-b17b-218bb9f8b85e Who will be consuming your data - humans or agents? When it's agents, do you structure it differently? Optimize for token budgets instead of disk or query cost? From what I see, we might not need clean, joined data (agents can do that), but descriptions of relationships. Functions become checklists. Tools beat tables. Logs beat docs. Ambiguity + context might work better than a single-source of truth. In this workshop, we'll (together) explore: - How data engineering for agents is different than for humans - How agents themselves can help engineer the data for agents This session is for data/AI engineers who are using agents or whose work agents will be using. Anand is an LLM psychologist at [Straive](https://straive.com/) and co-founder of [Gramener](https://gramener.com/), a data stories company. He’s listed among [India’s top 10 data scientists](https://analyticsindiamag.com/top-10-data-scientists-in-india-2015/) and [AI influencers](https://analyticsindiamag.com/ai-highlights/indias-100-most-influential-people-in-ai/) and is a regular TEDx/Pycon speaker. More importantly, he hand-transcribed every Calvin & Hobbes strip ever, is addicted to Minecraft & Anime (thanks to his daughter), and dreams of watching every film on the [IMDb Top 250](https://www.imdb.com/chart/top/) (except [The Shining](https://www.imdb.com/title/tt0081505/)). He blogs at [s-anand.net](https://www.s-anand.net/). {Add the link to draft slides - PDF/PPT - with comments access - TODO: at least a TOC or blog series} {Add the link to 2-min elevator pitch video - Um... will skip, please? Or... wait -- I'll have an AI generate it?} # Dialogue: The Curator's Dilemma: When Making Is Easy, Choosing Is the Craft, VizChitra, 04 Jul 2026 My team creates 9 variations of a chart in 15 minutes -- all defensible, none wrong. My afternoon is spent staring at them, trying to figure out which one is actually _good_. After decades of building data viz - Excel, PowerPoint, D3 - the _making_ part is easy, and _FAST_. What's slow is the choosing. Everyone has this problem. Vibe coding is a default. The bottleneck has moved from "can I build this?" to "should I ship this, or that one, or the third version, or none of them?" From construction to curation. And most of us haven't developed the muscles for that yet. This Dialogue is about that shift: the new, harder skill of selecting, evaluating, and refining from abundance rather than building from scratch. **1. Our central question:** AI tools generate multiple "correct" visualizations in minutes. What does good judgment look like - and how do we develop it? What are the criteria, instincts, and craft knowledge that help us choose well from a sea of plausible options?`
>
> I've got the talks.md file now, so let me look at the four transcripts to get a sense of their style and tone. I should check their sizes first to figure out the best way to read through them.
>
> Done

</details>

<details>
<summary>Synthesizing workshop style through transcript analysis</summary>

> Bash
>
> Request
>
> `{ "commands": "set -uo pipefail echo \"=== sizes of key files ===\" for f in \\ ~/code/talks/2026-04-08-ai-workshop-lbsnaa/transcript.md \\ ~/code/talks/2025-12-06-mining-digital-exhaust/transcript.md \\ ~/code/talks/2025-12-06-mining-digital-exhaust/README.md \\ ~/code/talks/2026-05-23-ai-unboxed-context-engineering/transcript.md \\ ~/code/talks/2025-09-16-vibe-analysis/transcript.md \\ ~/code/talks/2025-09-16-vibe-analysis/README.md \\ ; do test -e \"$f\" && printf \"%8s %s\ \" \"$(wc -l < \"$f\")L\" \"$f\" || echo \"MISSING $f\" done echo echo \"=== vibe-analysis dir full ===\" fd . ~/code/talks/2025-09-16-vibe-analysis -t f 2>/dev/null echo echo \"=== READMEs of the two with READMEs (these likely describe the workshop) ===\" echo \"--- vibe-analysis README ---\" sed -n '1,60p' ~/code/talks/2025-09-16-vibe-analysis/README.md" }`
>
> Response
>
> `=== sizes of key files === 482L /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/transcript.md 452L /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/transcript.md 15L /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/README.md 380L /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/transcript.md MISSING /home/vscode/code/talks/2025-09-16-vibe-analysis/transcript.md 237L /home/vscode/code/talks/2025-09-16-vibe-analysis/README.md === vibe-analysis dir full === /home/vscode/code/talks/2025-09-16-vibe-analysis/README.md /home/vscode/code/talks/2025-09-16-vibe-analysis/activities.md /home/vscode/code/talks/2025-09-16-vibe-analysis/cooking-insights.webp === READMEs of the two with READMEs (these likely describe the workshop) === --- vibe-analysis README --- --- marp: true title: Vibe Analysis author: Anand S url: https://sanand0.github.io/talks/2025-09-16-vibe-analysis/ theme: gaia paginate: true # Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html --- <style> blockquote { font-style: italic; } </style> # Vibe Analysis [Fifth Elephant Workshop](http://has.gy/hV8U) · 16 Sep 2025, 2:00 pm IST · [Bangalore](https://maps.app.goo.gl/fU3VHCjUGzUWVz6C6) [Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/) [CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/) https://sanand0.github.io/talks/ ![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-16-vibe-analysis/) --- ## You need some software before we start - A modern browser (Edge, Chrome, Firefox...) - A $20 ChatGPT Plus account - Sign into [github.com](https://github.com), [chatgpt.com/codex](https://chatgpt.com/codex), [jules.google.com](https://jules.google.com/) For programmers: - Install [uv](http://github.com/astral-sh/uv). Run `uv run --with pandas python`- Install [NodeJS](https://nodejs.org/en/download). Run`npx -y @openai/codex` and log in - Optional: Install [VS Code](https://code.visualstudio.com/) + [GitHub Copilot](https://github.com/copilot) / [Cursor](https://cursor.com/) / [Windsurf](https://windsurf.com/) / ... --- ## We will be sharing prompts on WhatsApp [WhatsApp Invite](https://chat.whatsapp.com/BsQJXLOJrhi23dWlhtAssq) ![h:200px](https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://chat.whatsapp.com/BsQJXLOJrhi23dWlhtAssq) --- ## Vibe Coding: code like code doesn't exist > ... where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. > I "Accept All" always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment > Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away. [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383)`
>
> I'm looking at the vibe-analysis README which is structured as a Marp slide deck—that gives me insight into how Anand designs the workshop format. I need to read through the full README and the mining-digital-exhaust README alongside the transcripts to understand the live workshop style and how it all connects.
>
> Let me strategically batch the reading: the full vibe-analysis README for structure, the mining-digital-exhaust README plus opening sections of transcripts, and then dive into the lbsnaa transcript since it's recent and a full workshop, plus the context-engineering transcript since it's most topically relevant.
>
> Bash
>
> Request
>
> `{ "commands": "set -uo pipefail echo \"########## VIBE-ANALYSIS README (slide structure) lines 60-237 ##########\" sed -n '60,237p' ~/code/talks/2025-09-16-vibe-analysis/README.md" }`
>
> Response
>
> `########## VIBE-ANALYSIS README (slide structure) lines 60-237 ########## [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383) --- ## Vibe Analysis: analyze, but ignore the code Here's the vibe analysis mindset: - You're **pragmatic**. You care about insights, not how they're coded. - You're **sceptical**. You cross-question and find errors. - You're **playful**. You try weird "what ifs" just to see what breaks. Let's analyze some datasets with this mindset. --- ## Pick any dataset. Here are some datasets - [MovieLens movies](https://grouplens.org/datasets/movielens/32m/) (review license) - [IMDb movies](https://datasets.imdbws.com/) (non-commercial) - [Occupational Employment and Wage Statistics (OEWS)](https://www.bls.gov/oes/tables.htm) - [Global AI Job Market & Salary Trends 2025](https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025) - [Flight Delay Dataset](https://www.kaggle.com/datasets/shubhamsingh42/flight-delay-dataset-2018-2024) - [London House Price Data](https://www.kaggle.com/datasets/jakewright/house-price-data) - [Exchange Rates to USD](https://www.kaggle.com/datasets/robikscube/exhange-rates-to-usd-from-imforg-updated-daily) - [Thailand Road Accidents (2019-2022)](https://www.kaggle.com/datasets/thaweewatboy/thailand-road-accident-2019-2022) --- ## Here are some India-specific datasets - [CBFC Censor Board Cuts](https://github.com/diagram-chasing/censor-board-cuts/tree/master/data) - [India Vehicle Data](https://github.com/Vonter/india-vehicle-stats/blob/main/DATA.md) - [India Air Quality Index](https://github.com/Vonter/india-cpcb-aqi/blob/main/DATA.md) - [Bengaluru Bus Routes](https://github.com/Vonter/bmtc-gtfs) - [India Air Traffic](https://github.com/Vonter/india-aviation-traffic) - [India Census 2011](https://www.kaggle.com/datasets/danofer/india-census) - [India Exams Database](https://github.com/lalithaar/indian-exams-database) --- ## Now we'll use LLMs for _everything_ 1. Explore data 2. Clean data 3. Model data 4. Explain data 5. Deploy data 6. Anonymize data --- ## We'll _ad lib_ this 1. I have no script / preparation. We'll do this live. 2. _You_ pick a dataset. _You_ suggest hypotheses. 3. _You_ guide the agents, even on my system. I'll just "facilitate". 4. **Publish** your findings _and prompts_. Make it reproducible. 5. **Red team** this. Critique sceptically. See what survives. 6. **Synthesize** learnings. Let's see what emerges / drops. --- ## I'm keen to experiment - Do **multiple versions** pay off? - **Explain-then-code** vs code-then-explain? - What **sceptical review** approaches are effective? - What **unit tests** help most? Any _invariants_? - What's the **minimal stack** for analysis? - What **schema context** helps LLMs most? (Ablation) - Do **data tools** via AGENTS.md (`dbt`, `rclone`, ...) help? - What **sub-agent specializations** work well? - Where are **pre-mortems** effective? <!-- Ideas from https://chatgpt.com/c/68c8bea3-c348-832b-a011-cc2723a47279 --> --- ## Let's cook some insights! ![h:500px](cooking-insights.webp) --- # Vibe Analysis [Fifth Elephant Workshop](http://has.gy/hV8U) · 16 Sep 2025, 2:00 pm IST · [Bangalore](https://maps.app.goo.gl/fU3VHCjUGzUWVz6C6) [Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/) [CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/) Please share your feedback here: ![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://forms.gle/CfiZDDUGCG73vfdM7) --- ## Insights from IMDb rating histogram - **Dense cluster around 7–7.5**. [Vote-weighted mean][imdb-weight] is ~7.21. - **Scarcity of low-end titles (<4)** despite millions of records. [Self-selection bias][self-selection] - **Sharp drop beyond ~8.5**. IMDb emphasizes “regular” voters. High averages require consistently enthusiastic voters. [IMDb’s Top 1,000 voters][top-reviewers] rate critically (lower than typical users 98% of the time) - **Spike at perfect 10.0**: [coordinated fan campaigns and vote brigading][ringer] [imdb-weight]: https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV "“Ratings FAQ,” IMDb Help Center. Weighted rating formula: (\\text{WR} = \\frac{v}{v+m}R + \\frac{m}{v+m}C), where (C) is the overall mean and (m) the minimum votes for chart eligibility." [self-selection]: https://link.springer.com/chapter/10.1007/978-0-387-73655-6_17 "Kramer, M. A. “Self-Selection Bias in Reputation Systems.” *Trust Management*, IFIP, 2007." [top-reviewers]: https://hbr.org/2025/01/research-how-top-reviewers-skew-online-ratings "Bondi, T., Rossi, M., & Stevens, R. L. “Research: How Top Reviewers Skew Online Ratings.” *Harvard Business Review*, Jan. 9, 2025." [ringer]: https://www.theringer.com/2019/6/12/tv/imdb-rating-system-problems-chernobyl "Bereznak, A. “The Problem With IMDb’s Rating System.” *The Ringer*, June 12, 2019." --- # Lockdown-era genre peaks <small> Reality-TV reached its highest output during lockdown with 78 feature releases in 2020, a 2.07× surge versus the 2017–2019 baseline of 37.7 films per year and 3.12× the 2022–2024 recovery average of 25 releases. Talk-Show titles also peaked in 2020, delivering 26 releases—double the pre-lockdown average of 13 per year and 2.23× the immediate post-lockdown average of 11.7 releases. Both genres cleared the study’s thresholds (at least 25 lockdown-year films and ≥20% growth over the pre-lockdown window), marking them as the only categories with statistically meaningful release spikes tied to the COVID-19 lockdown period </small> --- <small> | Director | Movies | Preferred Letter | | ------------------ | -----: | ---------------: | | Rakesh Roshan | 6 | K | | Haruo Sotozaki | 5 | D | | Keishi Otomo | 5 | R | | Frank Darabont | 4 | T | | Chad Stahelski | 4 | J | | Alan Mak | 4 | I | | Kunihiko Yuyama | 4 | P | | Michael Chaves | 4 | T | | John R. Cherry III | 4 | E | | Saeed Roustayi | 3 | L | </small> --- ## Any genres that rate 1950-60s films too high? <small> - **Film-noir** ratings cluster in the classic period: about 13.3 % of all noir ratings come from 1950s–1960s releases and another 25 % from the 1930s–1940s. The median genre sees only ~4.5 % of its ratings tied to 1950s–1960s titles, so noir is roughly 3× as concentrated there. Those mid-century titles are strong performers (e.g., 1950s average 3.997, 1960s 4.053), but later decades (1970s neo-noir at 4.12) keep the overall average high too. - **War films** also skew earlier: 1950s–1960s releases account for 11.3 % of war-movie ratings versus that same ~4.5 % median elsewhere. Their 1950s/1960s averages (3.963 and 4.004) are among the genre’s best, yet pre/post-1960 decades remain relatively strong (e.g., 1930s at 3.86, 1990s at 3.85). - **It isn’t solely a volume imbalance** though; even later entries hold up reasonably well, suggesting a combination of historical canon effects and comparatively consistent quality. </small> --- ## Feedback analysis Lessons from [vibe analysis of feedback](https://chatgpt.com/share/68ca37db-14dc-800c-8cfa-34f7dcd1538e): - Share **setup instructions** + video/asciinema to reduce setup friction. - Share **self-check instructions** for a default dataset with prompts. - Add explicit checkpoints with **self-tests**. - Use two-lane pacing: **Cruise** (safe, minimal path) vs **Sprint** (optional accelerators). [Participant feedback](https://hasgeek.com/fifthelephant/data-analytics-using-ai-workshop/updates/llms-in-action-what-participants-learned-at-the-vi-KAAiTUtoJNrmJ61Gxrdxgf) --- ## Participant feedback: Ambarish > Before the workshop, I was curious about the name and content, but trusted the organizer (Hasgeek) & Anand. Anand’s deep knowledge and lucid explanations guided us through using LLMs for data analysis, testing hypotheses, and running parallel tasks with tools like Claude and Codex. I learned how BI and data analysis are evolving in the AI age, and how using multiple models reduces hallucinations and errors. Even as a remote participant, the pace was comfortable. Thanks again, Anand, for a wonderful session! --- ## Participant feedback: Anindo Chakraborty > Yesterday’s workshop cut through the hype around ‘vibe coding’ and showed how it applies to analytics and data science. Anand walked us through the full lifecycle — from raw data to hypotheses, AI-driven testing, and refining results into business-ready insights. Advanced topics included building Agents, sub-agents, and using AGENTS.md files for task automation. The hands-on ‘flow state’ approach made learning incredibly practical. My biggest takeaway: start small, get your hands dirty, and practical experience will follow. Outstanding workshop — thank you, Anand!`
>
> I'm getting a clearer picture of how his workshops operate—they're interactive, improvised, participant-driven experiences where people work with real data and provide feedback. The Vibe Analysis workshop from Fifth Elephant is the closest match to what he's planning. I notice the feedback section points to a Hasgeek updates page, which is exactly what Zainab mentioned needing for the Q2 update.
>
> Now I need to dig into his actual teaching style by reading through the workshop transcripts—particularly the LBSNAA, context-engineering, and mining-digital-exhaust ones—to capture how he explains concepts live. I also need to find examples of updates he's written for past Hasgeek workshops to understand the format and tone for the "why this workshop / who is it for" piece that's missing from the current page.
>
> Done

</details>

<details>
<summary>Synthesizing workshop style from context-engineering precedent</summary>

> I'm getting a clearer picture of the speaking style now—it's conversational and story-driven, with practical examples like the Seoul toilet and Singapore menu anecdotes, plus that "don't listen to me, open your laptops" energy. Now I want to dig into the mining-digital-exhaust and context-engineering transcripts to solidify this voice, and then check what past updates Anand has written for Hasgeek to see the pattern.
>
> I should prioritize the context-engineering transcript since it's directly relevant to the workshop topic, pull his previous Hasgeek updates to understand how he frames these announcements, and sample his LinkedIn posts around workshops and data topics to round out the full picture.
>
> Done

</details>

<details>
<summary>Synthesized workshop style patterns and prepared to draft content</summary>

> I'm seeing the core pattern now—the context-engineering approach is the closest match. What stands out is how he structures these as interactive experiences rather than lectures: workshops that flow organically based on participant interests, using simple tools like Google Forms and WhatsApp for real-time engagement, and emphasizing hands-on participation where people are actually doing the work rather than passively consuming. The real value isn't the content itself but the environment he creates, and there's this interesting framing around accessibility—the "intern/chotu" metaphor and asking what paid AI tools people have access to.
>
> Now I'm pulling his LinkedIn posts to get a sense of his voice and any workshop announcements. The file has thousands of entries, so I'm looking for the longer-form posts he's written about talks, workshops, and AI topics—not just shares. I should also check his past Hasgeek workshop updates to see how he communicates about these events and whether he's documented his approach anywhere in his notes or repositories.
>
> Done

</details>

<details>
<summary>Examined Hasgeek workshop update formats and writing styles</summary>

> Bash
>
> Request
>
> `{ "commands": "set -uo pipefail echo \"########## linkedin-posts.jsonl structure ##########\" head -c 1500 ~/Documents/data/linkedin-posts.jsonl echo echo echo \"########## keys ##########\" head -1 ~/Documents/data/linkedin-posts.jsonl | jaq -r 'keys' 2>/dev/null || head -1 ~/Documents/data/linkedin-posts.jsonl | python3 -c \"import json,sys; print(list(json.loads(sys.stdin.read()).keys()))\"" }`
>
> Response
>
> `########## linkedin-posts.jsonl structure ########## {"type":"comment","id":"urn:li:comment:(activity:7476623783395532801,7476818464276365312)","commentId":"7476818464276365312","parentId":"urn:li:activity:7476623783395532801","parentCommentId":"urn:li:comment:(activity:7476623783395532801,7476772917658296320)","commenterName":"Sukumar Rajagopal","commenterProfile":"https://www.linkedin.com/in/rajagopalsukumar","commenterMiniProfileUrn":"","commenterDescription":"Founder & CEO, Tiny Magiq; EiR at CMI Algolabs;xSVP/CIO & Head of Innovation, Cognizant","commenterType":"• 1st","commenterDegree":"1st","commenterBadges":[],"premiumVerifiedBadges":[],"commentedText":"57m","edited":false,"content":"Kameshwaran Panchagnula C grateful for your kind words","reactionCount":null,"reactionText":"","reactionTypesVisible":[],"replyCount":null,"impressionCount":null,"socialText":"Like\nReply","rawText":"Sukumar Rajagopal\n • 1st\nFounder & CEO, Tiny Magiq; EiR at CMI Algolabs;xSVP/CIO & Head of Innovation, Cognizant\n57m\nKameshwaran Panchagnula C grateful for your kind words\nLike\nReply","scrapedAt":"2026-06-28T03:04:25.667540+00:00","commentedAt":"2026-06-28T02:07:25.667540+00:00","commentedAtConfidence":"relative"} {"type":"comment","id":"urn:li:comment:(activity:7476623783395532801,7476772917658296320)","commentId":"7476772917658296320","parentId":"urn:li:activity:7476623783395532801","parentCommentId":"","commenterName":"Kameshwaran Panchagnula C","commenterProfile":"https://www.linkedin.com/in/kameshwaranpc","commenterMiniProfileUrn ########## keys ########## [ "commentId", "commentedAt", "commentedAtConfidence", "commentedText", "commenterBadges", "commenterDegree", "commenterDescription", "commenterMiniProfileUrn", "commenterName", "commenterProfile", "commenterType", "content", "edited", "id", "impressionCount", "parentCommentId", "parentId", "premiumVerifiedBadges", "rawText", "reactionCount", "reactionText", "reactionTypesVisible", "replyCount", "scrapedAt", "socialText", "type" ]`
>
> I need to filter this data to isolate Anand's actual posts, excluding any comments they may have authored.
>
> Bash
>
> Request
>
> `{ "commands": "set -uo pipefail echo \"=== distinct types ===\" jaq -r '.type' ~/Documents/data/linkedin-posts.jsonl | sort | uniq -c | sort -rn echo echo \"=== fields on a post-type record ===\" jaq -c 'select(.type==\"post\")' ~/Documents/data/linkedin-posts.jsonl 2>/dev/null | head -1 | python3 -c \"import json,sys;d=json.loads(sys.stdin.read());print(list(d.keys()))\" 2>/dev/null || echo \"no post type; checking other types\" echo echo \"=== sample non-comment record keys ===\" jaq -c 'select(.type!=\"comment\")' ~/Documents/data/linkedin-posts.jsonl 2>/dev/null | head -1 | python3 -c \"import json,sys;d=json.loads(sys.stdin.read());print(d.get('type'));print(list(d.keys()))\"" }`
>
> Response
>
> `=== distinct types === 2969 comment 309 post === fields on a post-type record === ['type', 'id', 'postId', 'url', 'authorName', 'authorProfile', 'authorMiniProfileUrn', 'authorDescription', 'authorBadges', 'premiumVerifiedBadges', 'postedText', 'edited', 'visibility', 'content', 'links', 'linkCount', 'media', 'mediaCount', 'analyticsUrl', 'reactionCount', 'reactionTypesVisible', 'commentCount', 'repostCount', 'impressionCount', 'socialText', 'rawText', 'scrapedAt', 'postedAt', 'postedAtConfidence', 'commentScrapeStats'] no post type; checking other types === sample non-comment record keys === post ['type', 'id', 'postId', 'url', 'authorName', 'authorProfile', 'authorMiniProfileUrn', 'authorDescription', 'authorBadges', 'premiumVerifiedBadges', 'postedText', 'edited', 'visibility', 'content', 'links', 'linkCount', 'media', 'mediaCount', 'analyticsUrl', 'reactionCount', 'reactionTypesVisible', 'commentCount', 'repostCount', 'impressionCount', 'socialText', 'rawText', 'scrapedAt', 'postedAt', 'postedAtConfidence', 'commentScrapeStats'] Return code: 2`
>
> I'm filtering through Anand's posts to find his original content about workshops, talks, AI, and data topics, then examining the highest-engagement ones to understand his LinkedIn voice and communication style.
>
> Bash
>
> Request
>
> `{ "commands": "set -uo pipefail echo \"=== Anand's own posts: count ===\" jaq -c 'select(.type==\"post\" and (.authorName|test(\"Anand\";\"i\")))' ~/Documents/data/linkedin-posts.jsonl | wc -l echo echo \"=== author names on posts (top) ===\" jaq -r 'select(.type==\"post\") | .authorName' ~/Documents/data/linkedin-posts.jsonl | sort | uniq -c | sort -rn | head echo echo \"=== Anand posts mentioning workshop/talk/fifth elephant/hasgeek/data/agent (content first 280 chars) ===\" jaq -rc 'select(.type==\"post\" and (.authorName|test(\"Anand\";\"i\")) and (.content|test(\"workshop|Fifth Elephant|Hasgeek|talk|agent|data\";\"i\"))) | {n: (.content|length), p: (.postedText), r: .reactionCount, c: (.content[0:300])}' ~/Documents/data/linkedin-posts.jsonl 2>/dev/null | head -25" }`
>
> Response
>
> `=== Anand's own posts: count === 294 === author names on posts (top) === 294 Anand S 3 Straive 2 Gurman Bhatia 2 Gramener 1 VizChitra 1 Sunil Kardam 1 Richie Lionell 1 Ravinder Ireddy 1 Gramener Alumni Network 1 (GK) Ganes Kesari === Anand posts mentioning workshop/talk/fifth elephant/hasgeek/data/agent (content first 280 chars) === {"n":2424,"p":"13h • Edited •","r":36,"c":"Let me share what I learned from that 90-minute lunch conversation with Sukumar Rajagopal. Then you’ll see who’s really generous with their knowledge.\n𝗛𝗮𝗯𝗶𝘁𝘀:\nStart small. “I started with two pushups. Now I do sixty at one go.”\nAnchor to something you already do. “After I brush teeth, I have to do i"} {"n":2075,"p":"29m •","r":37,"c":"There’s a bounty-hunting agent ecosystem emerging on GitHub. I stumbled into it yesterday.\n𝚜𝚢𝚞-𝚝𝚘𝚞𝚝𝚘𝚞𝚜𝚊𝚒 is an “Autonomous Technical Contributor & AI-Driven Developer” - a 𝗯𝗼𝘂𝗻𝘁𝘆-𝗵𝘂𝗻𝘁𝗶𝗻𝗴 agent. It submits PRs against issues with payments attached, asking for bounty payments via PayPal to n6085530@gm"} {"n":756,"p":"4d •","r":37,"c":"On Sat 4 July at Bangalore, Arvind Satyanarayan is speaking at VizChitra 2026. A talk I'm keenly looking forward to.\nI've been following Arvind's work since Vega-Lite. It's a grammar of graphics - something that makes data visualizations (charts) more structured. I tried switching to it our default "} {"n":1553,"p":"6d •","r":29,"c":"Yesterday’s workshop for IIM Alumni SG was on 𝗧𝗼𝗼𝗹𝘀 𝗮𝗻𝗱 𝗪𝗼𝗿𝗸𝗳𝗹𝗼𝘄𝘀:\nAgents are getting smarter, so they know what to do.\nTools agents can use are growing and are more powerful.\nThis combinatorial explosion creates explosive possibilites.\nWe covered six workflows:\n1. 𝗟𝗲𝘃𝗲𝗿𝗮𝗴𝗲 𝘁𝗿𝗮𝗻𝘀𝗰𝗿𝗶𝗽𝘁𝘀. Use Google A"} {"n":725,"p":"2w •","r":202000000000,"c":"On Sat 13 Jun 2026 at 3 pm IST, I’m conducting an online workshop on “Data Stories with AI”.\nIn this workshop, you will use ChatGPT and Claude, mostly, to:\nFind data\nAnalyze it\nExtract insights\nVisualize as stories\nIt’s a data visualization using AI workshop for journalists - but you don’t need to k"} {"n":1028,"p":"2w •","r":63,"c":"At 2 pm IST today, I’m running a workshop at Paradox, IIT Madras.\nYou can join online at https://lnkd.in/gvQrTN3W and ask questions on chat.\nDate: 12 Jun 2026\nTime: 2 pm IST\nVenue: DOMS 101\n𝗔𝗴𝗲𝗻𝗱𝗮:\nYou’ve been told AI can pass your exams. But what happens when you actually watch it try — live, on yo"} {"n":928,"p":"22h • Edited •","r":49,"c":"I don’t post all my writing on LinkedIn. For example:\n• Fewer 𝘀𝘁𝗿𝗮𝘁𝗲𝗴𝘆 𝗽𝗼𝘀𝘁𝘀, e.g. “Where Enterprise AI is Headed”, “How My Innovation Team Works”, etc. aren't on LinkedIn\n• Fewer 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 𝗽𝗼𝘀𝘁𝘀, e.g. my AGENTS.md, my SKILL.md files, CLI tools, evals, etc. aren't on LinkedIn\nI also shorten content "} {"n":1361,"p":"21h •","r":35,"c":"Imagine you’re an information anarchist. You undermine Wikipedia pages by nuking references.\nA genie has granted you a wish: you can 𝐧𝐮𝐤𝐞 𝐨𝐧𝐞 𝐞𝐧𝐭𝐢𝐫𝐞 𝐝𝐨𝐦𝐚𝐢𝐧. Just one.\nAs a data-driven decision maker (who is 𝘢𝘭𝘴𝘰 an information anarchist? 🤷), which would you pick?\nA common choice is Internet Archive "} {"n":827,"p":"3w •","r":53,"c":"There is a 29-word sentence that appears 𝘷𝘦𝘳𝘣𝘢𝘵𝘪𝘮 across 2,920 articles on Wikipedia.\n\"Note on population: The difference values of population numbers in the table “Population statistic” and in the sections “Ethnicity” & “Religion” is caused by the use of various statistical methods.\"\nEach of the 2,"} {"n":584,"p":"3w •","r":98,"c":"Today's AI Workshop with the IIM Alumni SG was on Context Engineering.\nBefore the session, Dhyeya Anand asked me: \"Why are these people attending? Can't they learn AI themselves?\"\nTrue! You should just use AI to teach you AI. (And everything else.)\nUntil then, people like me will use AI to teach you"} {"n":981,"p":"4w • Edited •","r":201000,"c":"I advise people that people skills are important in the AI era.\nNow, I'm 𝘶𝘴𝘪𝘯𝘨 𝘈𝘐 to help me with people skills.\nThis morning, I exported my WhatsApp conversations, fed it into Claude, and asked:\n𝘞𝘩𝘰 𝘢𝘳𝘦 𝘱𝘦𝘰𝘱𝘭𝘦 𝘪𝘯 𝘮𝘺 𝘭𝘪𝘧𝘦 𝘵𝘩𝘢𝘵 𝘮𝘰𝘴𝘵 𝘥𝘦𝘴𝘦𝘳𝘷𝘦 𝘢𝘯 𝘶𝘯𝘳𝘦𝘢𝘴𝘰𝘯𝘢𝘣𝘭𝘦 𝘨𝘦𝘴𝘵𝘶𝘳𝘦 𝘰𝘧 𝘵𝘩𝘢𝘯𝘬𝘴 𝘢𝘯𝘥 𝘸𝘩𝘢𝘵 𝘸𝘰𝘶𝘭𝘥 𝘵𝘩𝘢𝘵 𝘣𝘦?\nIt"} {"n":1274,"p":"2mo •","r":78,"c":"Lyria 3 (Gemini's new \"Create Song\" feature) is helping me in new ways. Earlier this week, it created a jingle for my talk.\nYesterday, at an AI Workshop for IAS officers, I asked Gemini:\n\"Create a soulful vote of thanks (with patriotic Indian music playing in the background) naming each of these peo"} {"n":1794,"p":"2mo •","r":60,"c":"I added a narrative story to my LLM Pricing chart. That makes it easier for me 𝘢𝘯𝘥 others to tell the story of AI's evolution in the last three years.\nIt was vibe-coded over two iterations.\nIn the first version, I prompted it to:\n🟪🟣🟣\nAdd a scrollytelling narrative. So, when users first visit the pag"} {"n":1187,"p":"2mo •","r":117,"c":"I created an embedding map of my blog posts.\nI've been blogging since 1999 and over time, my posts have evolved.\n• 1999-2005: mostly links. I started by link-blogging\n• 2005-2007: mostly quizzes, how I do things, Excel tips, etc.\n• 2008-2014: mostly coding, how I do things and business realities\n• 2"} {"n":1343,"p":"2mo •","r":81,"c":"Summarizing my advice on AI in SDLC from the PyConf Hyderabad panel discussion:\n𝗣𝗿𝗼𝗰𝗲𝘀𝘀\nMake AI your 𝘦𝘯𝘵𝘪𝘳𝘦 SDLC loop. Record client calls, feed them to a coding agent to directly build & deploy the solution.\nRecord your prompts, run post-mortems, and distill them into 𝚂𝙺𝙸𝙻𝙻𝚂.𝚖𝚍 files for reuse.\n𝗣𝗿𝗼"} {"n":255,"p":"2mo • Edited •","r":42,"c":"\"Design in the age of infinite generativity\".\nSearch for that to find my talk at the Chennai Design Festival yesterday.\nIt's short (10 min). Claude, Gemini and I vibe-designed half a dozen innovative new products/features - which was completely unplanned."} {"n":1276,"p":"2mo •","r":93,"c":"On 20 March 2026, The Times Of India published a \"Hack of the Day\" card that my agents generated.\nLast month, Rohit Saran and I explored how we could use AI in the newsroom. We iterated and learnt a few things:\n𝗙𝗶𝗻𝗱 𝘁𝗵𝗲 𝗿𝗶𝗴𝗵𝘁 𝗳𝗼𝗿𝗺𝗮𝘁 𝗳𝗶𝗿𝘀𝘁. Recurring, structured, feedback-rich formats work well for A"} {"n":1074,"p":"2mo •","r":178,"c":"TDS Project 1 wasn't just a student project. It was a research and social experiment, too.\nIn Tools in Data Science course at Indian Institute of Technology, Madras, we tested two skills: analytics and design. The design tests were more diverse -- and students fared worse there. (Search for \"TDS Pro"} {"n":2812,"p":"2mo •","r":103,"c":"After an early morning beach walk with a classmate, I realized I hadn't taken my house keys. My daughter would be sleeping, so I wandered with my phone.\nThis is when I get ideas - often a dangerous time for my students.\nIn this case, the idea was a rambling conversation with Claude that roughly begi"} {"n":2828,"p":"2mo •","r":46,"c":"People worry that AI atrophies skills. Also that junior jobs, hence learning opportunities, are shrinking.\nCan AI fill the gap, i.e. help build skills?\nOne approach is: Do it without AI. Then have AI critique it and learn from it.\n(Several variations work, e.g. have the AI do it independently and co"} {"n":1582,"p":"2mo •","r":96,"c":"I ran a \"Vibe Coding for Humanities\" workshop at Ashoka University. Here are the takeaways:\n1. 𝗧𝗵𝗲𝗿𝗲 𝗜𝘀 𝗡𝗼 𝗕𝗶𝗴 𝗗𝗲𝗮𝗹. Vibe coding feels revolutionary but it isn't - it's just a barrier we haven't dissolved yet. The hard part is knowing what to build.\n2. 𝗥𝗮𝗺𝗯𝗹𝗲. 𝗗𝗼𝗻'𝘁 𝗖𝗿𝗮𝗳𝘁. Use ChatGPT as a free dict"} {"n":1428,"p":"2mo •","r":159,"c":"In my graded assignments, students can pick an AI and \"Ask AI\" any question at the click of a button. It defaults to Google AI Mode, but other models are available. I know who uses which model and their scores in each assignment.\nI asked Codex to test the hypothesis whether using a specific model he"} {"n":1166,"p":"3mo •","r":252000,"c":"My Tools in Data Science course is available publicly, with a few changes from last year.\nFirst, I 𝗿𝗲𝗺𝗼𝘃𝗲𝗱 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗰𝗼𝗻𝘁𝗲𝗻𝘁! Last year, Claude generated teaching material using my prompts. But what's the point? I might as well give students the prompts directly. They can tweak it to their needs.\nThis"} {"n":1933,"p":"3mo •","r":130,"c":"As AI marches along, another role at risk is the data engineer / database administrator.\nData scientists are already feeling the heat. https://lnkd.in/gJTFpFNn\nA common task for data engineers is to analyze SQL queries - to optimize and standardize.\nMy colleague Pavan used QuWit to analyze 1,500 SQL"} {"n":666,"p":"3mo •","r":null,"c":"For those auditing my Tools in Data Science course:\nThe first graded assignment is live at https://exam.sanand.workers.dev/tds-2026-01-ga1\nIt is due on Sun 15 Feb 2026 midnight IST.\nYou can subscribe to updates at https://groups.google.com/g/tds-iitm\nor discuss at https://github.com/sanand0/tools-in"} Return code: 2`
>
> I'm getting a clear picture of his LinkedIn style now—he hooks readers with a specific incident or moment, uses bold unicode formatting to highlight key concepts, and structures workshop posts with concrete details like dates and times in IST. His voice is personal and self-deprecating, written in first person with actionable takeaways.
>
> Now I need to pull the full text of his most relevant posts—particularly the workshop announcements like the Data Stories with AI one and the IIT Madras Paradox workshop, since those are the closest templates for what I'm writing. I'll also check his context engineering recap for tone, and then look at past Hasgeek updates to see how he frames announcements there.
>
> Bash
>
> Request
>
> `{ "commands": "set -uo pipefail echo \"########## FULL: Data Stories with AI workshop announcement ##########\" jaq -r 'select(.type==\"post\" and (.content|test(\"Data Stories with AI\";\"i\"))) | .content' ~/Documents/data/linkedin-posts.jsonl | head -60 echo echo \"########## FULL: IIT Madras Paradox workshop announcement ##########\" jaq -r 'select(.type==\"post\" and (.content|test(\"workshop at Paradox\";\"i\"))) | .content' ~/Documents/data/linkedin-posts.jsonl | head -60" }`
>
> Response
>
> `########## FULL: Data Stories with AI workshop announcement ########## On Sat 13 Jun 2026 at 3 pm IST, I’m conducting an online workshop on “Data Stories with AI”. In this workshop, you will use ChatGPT and Claude, mostly, to: Find data Analyze it Extract insights Visualize as stories It’s a data visualization using AI workshop for journalists - but you don’t need to know data, visualization, journalism, or even technology. But this 𝘪𝘴 a practical workshop. You’ll be doing stuff and sharing your results. 𝗣𝗿𝗲-𝗿𝗲𝗾𝘂𝗶𝘀𝗶𝘁𝗲𝘀: A paid ChatGPT Plus or Claude Pro account - both are about Rs 2,000. Just buy it for a month. It’s worth it. It’s on 𝗚𝗼𝗼𝗴𝗹𝗲 𝗠𝗲𝗲𝘁. Register at https://lnkd.in/gkqFYttu I’ll record and share it. Attend only if you want to 𝘥𝘰 stuff. You can always watch later to 𝘴𝘦𝘦 stuff. ########## FULL: IIT Madras Paradox workshop announcement ########## At 2 pm IST today, I’m running a workshop at Paradox, IIT Madras. You can join online at https://lnkd.in/gvQrTN3W and ask questions on chat. Date: 12 Jun 2026 Time: 2 pm IST Venue: DOMS 101 𝗔𝗴𝗲𝗻𝗱𝗮: You’ve been told AI can pass your exams. But what happens when you actually watch it try — live, on your questions, in real time? This workshop starts with a collective experiment: we ask coding agents to solve real exams (including IITM exams) and see how it solves them. What follows isn’t a tutorial on prompting — it’s an autopsy that reveals what your exams are actually testing, where AI confidently hallucinates, and what that means for what’s worth learning. You’ll leave with a reframed understanding of your degree (the goal isn’t answers, it’s the ability to catch wrong ones) and a concrete study rituals that uses AI as a Socratic sparring partner rather than an answer machine. Come with a question you got wrong recently — it’s going to be useful. 𝗥𝗲𝗮𝗹 𝗮𝗴𝗲𝗻𝗱𝗮: An ask-me-anything session plus real-life experiments.`
>
> I'm looking at past Hasgeek workshop updates to understand the format and tone, particularly from the vibe-analysis project that was linked in the README. Since Zainab is asking for an update explaining the workshop's purpose and relevance, I need to see what a Hasgeek project update post actually looks like.
>
> Done

</details>

<details>
<summary>Synthesized workshop structure, identified content gaps, drafted three deliverables</summary>

> - [Updates](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/updates) - hasgeek.com
>   I need to check how other workshops format their updates, so let me look at the data analytics workshop page to understand the structure better.
>
> [Failed to fetch https://hasgeek.com/fifthelephant/data-analytics-using-ai-workshop/updates](https://hasgeek.com/fifthelephant/data-analytics-using-ai-workshop/updates)
>
> I found a URL in the README that points to a specific workshop update, but it won't work with a standard web fetch. Let me try a web search instead to locate that content.
>
> Actually, I have a good sense of what these updates typically contain—they're promotional posts explaining the workshop's value and target audience. I've already seen the overview, LinkedIn announcement style, and participant feedback formats. Rather than chase more searches, let me do one focused search for Fifth Elephant workshop update examples to understand the typical structure and what tends to be most effective.
>
> hasgeek fifthelephant workshop update "why this workshop" who is it for
>
> 10 results
>
> - [Graduating your AI agents: the path to production](https://hasgeek.com/fifthelephant/ai-agents-workshop/) - hasgeek.com
> - [The Fifth Elephant 2025 Annual Conference](https://hasgeek.com/fifthelephant/2025/) - hasgeek.com
> - [The Fifth Elephant – Hasgeek](https://hasgeek.com/fifthelephant) - hasgeek.com
> - [LlamaIndex toolkit for building data-driven applications](https://hasgeek.com/fifthelephant/llamaindex-workshop-08-26/) - hasgeek.com
> - [The Fifth Elephant 2025 Winter Edition](https://hasgeek.com/fifthelephant/2025-winter/) - hasgeek.com
> - [The Fifth Elephant 2025 Annual Conference CfP](https://hasgeek.com/fifthelephant/fifthelephant-2025-cfp/) - hasgeek.com
> - [Build & optimize AI Agents that survive production](https://hasgeek.com/fifthelephant/build-optimize-ai-agents-workshop/) - hasgeek.com
> - [Commit to insight: building BI-as-code the AI way](https://hasgeek.com/fifthelephant/bi-as-code-workshop/) - hasgeek.com
> - [The Fifth Elephant 2024 Annual Conference (12th &13th July)](https://hasgeek.com/fifthelephant/2024/) - hasgeek.com
> - [The Fifth Elephant - Pune Edition](https://hasgeek.com/fifthelephant/2026-pune/) - hasgeek.com
>   I'm seeing the pattern across these Hasgeek workshops—they all follow the same structure: starting with a compelling problem or challenge, then explaining what participants will actually build and learn, and finally clarifying who the workshop is designed for.
>
> Looking at the timing details, this workshop runs 4 hours (2-6 PM IST on July 7), which aligns with the other Fifth Elephant sessions. I should verify the content gaps by checking what additional details might be needed—things like prerequisites, datasets, what to bring, and making sure the duration is clearly communicated. I have enough information now to write all three deliverables and address Zainab's request for a richer overview that explains the workshop's relevance and fills in those missing pieces.
>
> Comparing this page to other Fifth Elephant workshops, I'm noticing some key gaps: there's no prerequisites section, no explicit duration statement, no level indicator (beginner/intermediate), no concrete agenda or takeaways beyond abstract bullets, no datasets or repo links, and no format details about what participants should bring or how the workshop will run. The page reads more personal and abstract than peer workshops, which undersells what attendees will actually do and walk away with—something that matters for conversion on a paid, limited-seat workshop.
>
> There's also a voice issue: the exploratory, hedged tone ("From what I see, we might not need...") is authentically Anand and intriguing, but a prospective registrant scanning multiple workshops needs one clear "you will DO X and LEAVE WITH Y" statement. Right now the page answers "here's an interesting provocation" rather than "here's what you'll be able to do on Monday." The audience description is solid but could sharpen with 2-3 concrete personas instead of the general "data/AI engineers using agents."
>
> I'm thinking the three deliverables themselves are the reusable asset here—I could mention a workshop launch kit template idea in passing, but keeping it tight makes more sense.
>
> On the ChatGPT best-practices list: that's great source material for the actual workshop content, but the page shouldn't become a listicle. For the update, I'll add a short "What you'll leave with" section that hints at concrete artifacts like an agent-ready data checklist, without expanding into the full 30-point list.
>
> Now I need to write the three deliverables in his voice for the update and LinkedIn post, keeping my analysis simple and direct. Let me verify the workshop details first: Tuesday, July 7, 2026, 2-6pm IST, hybrid format, 30 in-person attendees. His workshop posts emphasize the hands-on, practical nature—you're actually doing things and sharing results, not just watching. The tone shifts between announcements: one opens with the date and activity, while another leads with a provocative question to hook attention.
>
> For the data workshop specifically, the real tension is whether a human or an agent is reading your data now—and if it's an agent, all those data-cleaning best practices might actually be counterproductive. His LinkedIn style uses bold unicode formatting to emphasize key words. Safe to use spaced hyphens like Anand does in his posts. I'm being careful not to overuse the parallel structure patterns he avoids - though I can reference his existing workshop tagline since that's his own copy. Now I'm deciding whether to use the message_compose tool for the LinkedIn post or handle it differently.
>
> Given his preference to answer directly in Markdown, I'll present all three pieces inline rather than fragmenting them across tools. For the LinkedIn post specifically, I'll use actual unicode bold characters so he can copy-paste directly into LinkedIn without any conversion needed.
>
> Now I'm reconsidering the first question more carefully through an expert lens—the real question isn't whether the page is complete, but whether a Fifth Elephant member scanning it in twenty seconds will commit four hours plus membership cost, and show up actually prepared for the hands-on session. There are two failure modes to avoid: either the value proposition stays too abstract and conversion suffers, or people arrive without the necessary setup (paid AI accounts, laptops, prerequisites), which breaks the hands-on experience he flagged as important.
>
> Comparing his page to peer Fifth Elephant workshops like Graduating Your AI Agents and Build & Optimize Agents, I'm noticing he's missing the standard scaffolding that his own past workshops always included—prerequisites and setup instructions are completely absent despite this being hands-on, duration is only in the date strip rather than stated in prose, the audience definition is too vague, and the takeaways are abstract rather than concrete artifacts. The format also needs clarification about what to bring and how the session will actually run.
>
> There's a blind spot here worth flagging: the overview's deliberate ambiguity about whether clean data is needed is intellectually compelling as a hook, but it also signals "I haven't fully figured this out yet," which reads as risk to some buyers. His vibe-analysis page solved this by being explicit that it's experimental while listing concrete exercises and datasets—so the fix is keeping the provocation but anchoring it with specifics the way that page did.
>
> I'm pulling his own feedback from the vibe-analysis review (he recommended sharing setup instructions and reducing friction with video/asciinema) to cite as his lesson. Now I'll structure the response with a quick answer up top, then three sections with drop-in Markdown blocks he can paste directly, keeping the Hasgeek update in his voice as prose explaining the why and who.
>
> For the LinkedIn post, I'll match his exact announcement style with unicode bold. Let me verify the event details: Tuesday 7 July 2026, 2-6 pm IST—a 4-hour hybrid workshop at Fifth Elephant, which is longer than his typical 90-minute online workshops.
>
> I should also flag the reusable asset here: a workshop page checklist covering the five essentials every hands-on AI workshop needs, which he can apply to future Fifth Elephant and college workshops. There's also a content opportunity in the "Agent-Ready Data Checklist" that could serve as both the workshop takeaway and a standalone blog post.
>
> Now I'm ready to write the response with light headers separating the three questions, keeping the prose clean and Feynman-style while letting each deliverable have its own formatting needs.
>
> Done

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "set -uo pipefail
echo \"=== talks.md ===\"
test -e ~/Dropbox/notes/talks.md && echo \"FOUND ~/Dropbox/notes/talks.md\" || echo \"MISSING\"
echo
echo \"=== talks dir ===\"
fd -t d . ~/code/talks --max-depth 1 2>/dev/null | head -50
echo
echo \"=== target workshop dirs ===\"
for d in 2026-04-08-ai-workshop-lbsnaa 2025-12-06-mining-digital-exhaust 2026-05-23-ai-unboxed-context-engineering 2025-09-16-vibe-analysis; do
echo \"--- $d ---\"
fd . ~/code/talks -t d -t f 2>/dev/null | rg -i \"$d\" | head -20 || echo \"none\"
done
echo
echo \"=== linkedin posts ===\"
test -e ~/Documents/data/linkedin-posts.jsonl && (echo \"FOUND\"; wc -l < ~/Documents/data/linkedin-posts.jsonl) || echo \"MISSING linkedin-posts.jsonl\"
fd linkedin ~/Documents/data 2>/dev/null | head"
}
```

Response

```
=== talks.md ===
FOUND ~/Dropbox/notes/talks.md
=== talks dir ===
/home/vscode/code/talks/2022-02-20-it-doesnt-have-to-be-us-and-them-rajen-makhijani/
/home/vscode/code/talks/2022-03-07-career-principles-with-rajen-makhijani/
/home/vscode/code/talks/2024-10-19-ai-in-education-webinar/
/home/vscode/code/talks/2025-01-18-how-to-use-ai-to-generate-code/
/home/vscode/code/talks/2025-05-10-vibe-coding/
/home/vscode/code/talks/2025-06-27-data-design-by-dialogue/
/home/vscode/code/talks/2025-06-28-prompt-to-plot/
/home/vscode/code/talks/2025-06-pycon-sg/
/home/vscode/code/talks/2025-07-13-goodbye-mba-hello-ai/
/home/vscode/code/talks/2025-07-18-tug-true-but-irrelevant-rob-schrauwen/
/home/vscode/code/talks/2025-07-23-supply-chain-automl/
/home/vscode/code/talks/2025-07-24-pugs-agent-loop/
/home/vscode/code/talks/2025-08-11-social-code-analysis/
/home/vscode/code/talks/2025-08-21-ai-coding-guide/
/home/vscode/code/talks/2025-08-21-rip-data-scientists/
/home/vscode/code/talks/2025-09-13-duckdb-is-the-new-pandas/
/home/vscode/code/talks/2025-09-15-llm-ama-gale/
/home/vscode/code/talks/2025-09-16-vibe-analysis/
/home/vscode/code/talks/2025-09-18-llm-ama-bi-worldwide/
/home/vscode/code/talks/2025-09-20-kiran-homelabbing-with-bare-metal/
/home/vscode/code/talks/2025-09-21-making-open-data-useful/
/home/vscode/code/talks/2025-09-21-zainab-building-a-culture-of-openness/
/home/vscode/code/talks/2025-09-22-llm-trends/
/home/vscode/code/talks/2025-09-llm-workflows/
/home/vscode/code/talks/2025-10-16-vibe-analysis/
/home/vscode/code/talks/2025-10-23-vibe-coding/
/home/vscode/code/talks/2025-10-29-llm-data-visualization/
/home/vscode/code/talks/2025-11-06-llm-psychology/
/home/vscode/code/talks/2025-11-13-nirmal-impress-ai-hr/
/home/vscode/code/talks/2025-11-15-applied-vibe-coding/
/home/vscode/code/talks/2025-12-03-vibe-analytics-iim-alumni-sg/
/home/vscode/code/talks/2025-12-05-scdm-keynote/
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/
/home/vscode/code/talks/2026-01-11-nptel-vibe-coding-workshop/
/home/vscode/code/talks/2026-01-20-agentic-ai-in-action-deloitte/
/home/vscode/code/talks/2026-02-11-amat-dt-day/
/home/vscode/code/talks/2026-02-26-vibe-coding-for-humanities-ashoka/
/home/vscode/code/talks/2026-03-12-nie-ai-roadmap/
/home/vscode/code/talks/2026-03-15-how-students-learn-python/
/home/vscode/code/talks/2026-03-15-pyconf-ai-in-sdlc/
/home/vscode/code/talks/2026-03-18-iitm-academic-council/
/home/vscode/code/talks/2026-03-18-iitm-office-of-institutional-advancement/
/home/vscode/code/talks/2026-03-18-verifiable-agents/
/home/vscode/code/talks/2026-03-20-intequant-advisors/
/home/vscode/code/talks/2026-03-21-design-in-the-age-of-infinite-generativity/
/home/vscode/code/talks/2026-03-21-faculty-ai-transformation-nie/
/home/vscode/code/talks/2026-03-26-hack-of-the-day-toi/
/home/vscode/code/talks/2026-04-06-innovation-as-a-frontier-straive/
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/
/home/vscode/code/talks/2026-04-08-frontiers-in-technology-debjani-lbsnaa/
=== target workshop dirs ===
--- 2026-04-08-ai-workshop-lbsnaa ---
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/cabinet-briefing-sketchnote.avif
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/defiant-ias-officers-chatgpt-research.md
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/defiant-ias-officers-claude-research.md
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/iimb-whatsapp-group.html
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/index.html
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/nfsa-analysis.html
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/prompts.md
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/sketchnote.avif
/home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/transcript.md
--- 2025-12-06-mining-digital-exhaust ---
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/README.md
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/activities.md
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/cycling.webp
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/digital-exhaust-notes.md
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/double-hump.webp
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/index.html
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/playstore-story.html
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/sketchnote.webp
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/topic-modeling.webp
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/trades.webp
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/transcript.md
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/whatsapp-thread.json
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/youtube-story.html
/home/vscode/code/talks/2025-12-06-mining-digital-exhaust/youtube.webp
--- 2026-05-23-ai-unboxed-context-engineering ---
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/argue-against-my-blog-posts-and-find-errors.md
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iim-alumni-singapore-workshops-content-chagpt.md
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iim-alumni-singapore-workshops-content-claude.md
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iim-sg-alumni-workshop-context-engineering-prep.md
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iim-singapore-alumni-ai-workshop-plan.md
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iimpact-ai-unboxed-teams-background-design-gemini.md
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/iimpact-ai-unboxed-teams-background-design.md
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/memory-test-on-gemini.md
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/chats/public-profile-of-anand.md
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/comic-page.avif
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/index.html
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/prompts.md
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/teams-backgrounds.avif
/home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/transcript.md
--- 2025-09-16-vibe-analysis ---
/home/vscode/code/talks/2025-09-16-vibe-analysis/
/home/vscode/code/talks/2025-09-16-vibe-analysis/README.md
/home/vscode/code/talks/2025-09-16-vibe-analysis/activities.md
/home/vscode/code/talks/2025-09-16-vibe-analysis/cooking-insights.webp
=== linkedin posts ===
FOUND
3278
/home/vscode/Documents/data/linkedin-invites.json
/home/vscode/Documents/data/linkedin-posts.jsonl
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "set -uo pipefail
echo \"=== talks.md: total lines ===\"
wc -l ~/Dropbox/notes/talks.md
echo
echo \"=== talks.md lines 120-175 (the workshop note) ===\"
sed -n '120,175p' ~/Dropbox/notes/talks.md"
}
```

Response

```
=== talks.md: total lines ===
3769 /home/vscode/Dropbox/notes/talks.md
=== talks.md lines 120-175 (the workshop note) ===
# Building Verification Harnesses, Fifth Elephant Workshop
https://hasgeek.com/fifthelephant/fifthelephant-2026-call-for-submissions/sub/building-verification-harnesses-JCxuCWWTNAP1VGDezE6RhZ - Via https://claude.ai/chat/ebdaa2a9-f26c-467f-b17b-218bb9f8b85e
To confidently deploy in production, you need a robust verification mechanism. Some verification mechanisms are easy. Wrong code doesn't compile or pass good test cases. Wrong analysis doesn't meet a post-condition - say a value range or a known aggregate. Wrong proofs don't validate on LEAN.
But how far can we take it? When we have an insurance claim, could InsurLE help us verify its validity? Could Catala help us verify the legality of a contract?When an engineer generates a circuit, could we simulate it on SPICE? Use SHACL validated knowledge graphs to verify drug details?
In this workshop, you'll explore a variety of different problems that are more verifiable than we thought. That lets us run build and deploy agents far more reliably. You will also be _creating_ verification harnesses where none existed before - which is the bottleneck since agents have driven the generation cost to almost zero.
This session is for AI developers who need to ship verifiale agents into production - e.g. in a regulated or high-trust environment (finance, healthcare, government).
{Add the link to draft slides - PDF/PPT - with comments access - TODO: at least a TOC or blog series}
{Add the link to 2-min elevator pitch video - Um... skip, please?}
# When Data is for Agents, Not Humans, Fifth Elephant Workshop, 07 Jul 2026
https://hasgeek.com/fifthelephant/fifthelephant-2026-call-for-submissions/sub/when-data-is-for-agents-not-humans-RPJ3syxmspKua6ADd44mD6 - Via https://claude.ai/chat/ebdaa2a9-f26c-467f-b17b-218bb9f8b85e
Who will be consuming your data - humans or agents? When it's agents, do you structure it differently? Optimize for token budgets instead of disk or query cost?
From what I see, we might not need clean, joined data (agents can do that), but descriptions of relationships. Functions become checklists. Tools beat tables. Logs beat docs. Ambiguity + context might work better than a single-source of truth.
In this workshop, we'll (together) explore:
- How data engineering for agents is different than for humans
- How agents themselves can help engineer the data for agents
This session is for data/AI engineers who are using agents or whose work agents will be using.
Anand is an LLM psychologist at [Straive](https://straive.com/) and co-founder of [Gramener](https://gramener.com/), a data stories company. He’s listed among [India’s top 10 data scientists](https://analyticsindiamag.com/top-10-data-scientists-in-india-2015/) and [AI influencers](https://analyticsindiamag.com/ai-highlights/indias-100-most-influential-people-in-ai/) and is a regular TEDx/Pycon speaker. More importantly, he hand-transcribed every Calvin & Hobbes strip ever, is addicted to Minecraft & Anime (thanks to his daughter), and dreams of watching every film on the [IMDb Top 250](https://www.imdb.com/chart/top/) (except [The Shining](https://www.imdb.com/title/tt0081505/)). He blogs at [s-anand.net](https://www.s-anand.net/).
{Add the link to draft slides - PDF/PPT - with comments access - TODO: at least a TOC or blog series}
{Add the link to 2-min elevator pitch video - Um... will skip, please? Or... wait -- I'll have an AI generate it?}
# Dialogue: The Curator's Dilemma: When Making Is Easy, Choosing Is the Craft, VizChitra, 04 Jul 2026
My team creates 9 variations of a chart in 15 minutes -- all defensible, none wrong. My afternoon is spent staring at them, trying to figure out which one is actually _good_.
After decades of building data viz - Excel, PowerPoint, D3 - the _making_ part is easy, and _FAST_. What's slow is the choosing.
Everyone has this problem. Vibe coding is a default. The bottleneck has moved from "can I build this?" to "should I ship this, or that one, or the third version, or none of them?" From construction to curation.
And most of us haven't developed the muscles for that yet.
This Dialogue is about that shift: the new, harder skill of selecting, evaluating, and refining from abundance rather than building from scratch.
**1. Our central question:**
AI tools generate multiple "correct" visualizations in minutes. What does good judgment look like - and how do we develop it?
What are the criteria, instincts, and craft knowledge that help us choose well from a sea of plausible options?
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "set -uo pipefail
echo \"=== sizes of key files ===\"
for f in \\
~/code/talks/2026-04-08-ai-workshop-lbsnaa/transcript.md \\
~/code/talks/2025-12-06-mining-digital-exhaust/transcript.md \\
~/code/talks/2025-12-06-mining-digital-exhaust/README.md \\
~/code/talks/2026-05-23-ai-unboxed-context-engineering/transcript.md \\
~/code/talks/2025-09-16-vibe-analysis/transcript.md \\
~/code/talks/2025-09-16-vibe-analysis/README.md \\
; do
test -e \"$f\" && printf \"%8s  %s\
\" \"$(wc -l < \"$f\")L\" \"$f\" || echo \"MISSING $f\"
done
echo
echo \"=== vibe-analysis dir full ===\"
fd . ~/code/talks/2025-09-16-vibe-analysis -t f 2>/dev/null
echo
echo \"=== READMEs of the two with READMEs (these likely describe the workshop) ===\"
echo \"--- vibe-analysis README ---\"
sed -n '1,60p' ~/code/talks/2025-09-16-vibe-analysis/README.md"
}
```

Response

```
=== sizes of key files ===
482L  /home/vscode/code/talks/2026-04-08-ai-workshop-lbsnaa/transcript.md
452L  /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/transcript.md
15L  /home/vscode/code/talks/2025-12-06-mining-digital-exhaust/README.md
380L  /home/vscode/code/talks/2026-05-23-ai-unboxed-context-engineering/transcript.md
MISSING /home/vscode/code/talks/2025-09-16-vibe-analysis/transcript.md
237L  /home/vscode/code/talks/2025-09-16-vibe-analysis/README.md
=== vibe-analysis dir full ===
/home/vscode/code/talks/2025-09-16-vibe-analysis/README.md
/home/vscode/code/talks/2025-09-16-vibe-analysis/activities.md
/home/vscode/code/talks/2025-09-16-vibe-analysis/cooking-insights.webp
=== READMEs of the two with READMEs (these likely describe the workshop) ===
--- vibe-analysis README ---
---
marp: true
title: Vibe Analysis
author: Anand S
url: https://sanand0.github.io/talks/2025-09-16-vibe-analysis/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
---
<style>
blockquote {
font-style: italic;
}
</style>
# Vibe Analysis
[Fifth Elephant Workshop](http://has.gy/hV8U) · 16 Sep 2025, 2:00 pm IST · [Bangalore](https://maps.app.goo.gl/fU3VHCjUGzUWVz6C6)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
https://sanand0.github.io/talks/
![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-16-vibe-analysis/)
---
## You need some software before we start
- A modern browser (Edge, Chrome, Firefox...)
- A $20 ChatGPT Plus account
- Sign into [github.com](https://github.com), [chatgpt.com/codex](https://chatgpt.com/codex), [jules.google.com](https://jules.google.com/)
For programmers:
- Install [uv](http://github.com/astral-sh/uv). Run `uv run --with pandas python`
- Install [NodeJS](https://nodejs.org/en/download). Run `npx -y @openai/codex` and log in
- Optional: Install [VS Code](https://code.visualstudio.com/) + [GitHub Copilot](https://github.com/copilot) / [Cursor](https://cursor.com/) / [Windsurf](https://windsurf.com/) / ...
---
## We will be sharing prompts on WhatsApp
[WhatsApp Invite](https://chat.whatsapp.com/BsQJXLOJrhi23dWlhtAssq)
![h:200px](https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://chat.whatsapp.com/BsQJXLOJrhi23dWlhtAssq)
---
## Vibe Coding: code like code doesn't exist
> ... where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.
> I "Accept All" always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment
> Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away.
[Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383)
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "set -uo pipefail
echo \"########## VIBE-ANALYSIS README (slide structure) lines 60-237 ##########\"
sed -n '60,237p' ~/code/talks/2025-09-16-vibe-analysis/README.md"
}
```

Response

```
########## VIBE-ANALYSIS README (slide structure) lines 60-237 ##########
[Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383)
---
## Vibe Analysis: analyze, but ignore the code
Here's the vibe analysis mindset:
- You're **pragmatic**. You care about insights, not how they're coded.
- You're **sceptical**. You cross-question and find errors.
- You're **playful**. You try weird "what ifs" just to see what breaks.
Let's analyze some datasets with this mindset.
---
## Pick any dataset. Here are some datasets
- [MovieLens movies](https://grouplens.org/datasets/movielens/32m/) (review license)
- [IMDb movies](https://datasets.imdbws.com/) (non-commercial)
- [Occupational Employment and Wage Statistics (OEWS)](https://www.bls.gov/oes/tables.htm)
- [Global AI Job Market & Salary Trends 2025](https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025)
- [Flight Delay Dataset](https://www.kaggle.com/datasets/shubhamsingh42/flight-delay-dataset-2018-2024)
- [London House Price Data](https://www.kaggle.com/datasets/jakewright/house-price-data)
- [Exchange Rates to USD](https://www.kaggle.com/datasets/robikscube/exhange-rates-to-usd-from-imforg-updated-daily)
- [Thailand Road Accidents (2019-2022)](https://www.kaggle.com/datasets/thaweewatboy/thailand-road-accident-2019-2022)
---
## Here are some India-specific datasets
- [CBFC Censor Board Cuts](https://github.com/diagram-chasing/censor-board-cuts/tree/master/data)
- [India Vehicle Data](https://github.com/Vonter/india-vehicle-stats/blob/main/DATA.md)
- [India Air Quality Index](https://github.com/Vonter/india-cpcb-aqi/blob/main/DATA.md)
- [Bengaluru Bus Routes](https://github.com/Vonter/bmtc-gtfs)
- [India Air Traffic](https://github.com/Vonter/india-aviation-traffic)
- [India Census 2011](https://www.kaggle.com/datasets/danofer/india-census)
- [India Exams Database](https://github.com/lalithaar/indian-exams-database)
---
## Now we'll use LLMs for _everything_
1. Explore data
2. Clean data
3. Model data
4. Explain data
5. Deploy data
6. Anonymize data
---
## We'll _ad lib_ this
1. I have no script / preparation. We'll do this live.
2. _You_ pick a dataset. _You_ suggest hypotheses.
3. _You_ guide the agents, even on my system. I'll just "facilitate".
4. **Publish** your findings _and prompts_. Make it reproducible.
5. **Red team** this. Critique sceptically. See what survives.
6. **Synthesize** learnings. Let's see what emerges / drops.
---
## I'm keen to experiment
- Do **multiple versions** pay off?
- **Explain-then-code** vs code-then-explain?
- What **sceptical review** approaches are effective?
- What **unit tests** help most? Any _invariants_?
- What's the **minimal stack** for analysis?
- What **schema context** helps LLMs most? (Ablation)
- Do **data tools** via AGENTS.md (`dbt`, `rclone`, ...) help?
- What **sub-agent specializations** work well?
- Where are **pre-mortems** effective?
<!-- Ideas from https://chatgpt.com/c/68c8bea3-c348-832b-a011-cc2723a47279 -->
---
## Let's cook some insights!
![h:500px](cooking-insights.webp)
---
# Vibe Analysis
[Fifth Elephant Workshop](http://has.gy/hV8U) · 16 Sep 2025, 2:00 pm IST · [Bangalore](https://maps.app.goo.gl/fU3VHCjUGzUWVz6C6)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
Please share your feedback here:
![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://forms.gle/CfiZDDUGCG73vfdM7)
---
## Insights from IMDb rating histogram
- **Dense cluster around 7–7.5**. [Vote-weighted mean][imdb-weight] is ~7.21.
- **Scarcity of low-end titles (<4)** despite millions of records. [Self-selection bias][self-selection]
- **Sharp drop beyond ~8.5**. IMDb emphasizes “regular” voters. High averages require consistently enthusiastic voters. [IMDb’s Top 1,000 voters][top-reviewers] rate critically (lower than typical users 98% of the time)
- **Spike at perfect 10.0**: [coordinated fan campaigns and vote brigading][ringer]
[imdb-weight]: https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV "“Ratings FAQ,” IMDb Help Center. Weighted rating formula: (\\text{WR} = \\frac{v}{v+m}R + \\frac{m}{v+m}C), where (C) is the overall mean and (m) the minimum votes for chart eligibility."
[self-selection]: https://link.springer.com/chapter/10.1007/978-0-387-73655-6_17 "Kramer, M. A. “Self-Selection Bias in Reputation Systems.” *Trust Management*, IFIP, 2007."
[top-reviewers]: https://hbr.org/2025/01/research-how-top-reviewers-skew-online-ratings "Bondi, T., Rossi, M., & Stevens, R. L. “Research: How Top Reviewers Skew Online Ratings.” *Harvard Business Review*, Jan. 9, 2025."
[ringer]: https://www.theringer.com/2019/6/12/tv/imdb-rating-system-problems-chernobyl "Bereznak, A. “The Problem With IMDb’s Rating System.” *The Ringer*, June 12, 2019."
---
# Lockdown-era genre peaks
<small>
Reality-TV reached its highest output during lockdown with 78 feature releases in 2020, a 2.07× surge versus the 2017–2019 baseline of 37.7 films per year and 3.12× the 2022–2024 recovery average of 25 releases.
Talk-Show titles also peaked in 2020, delivering 26 releases—double the pre-lockdown average of 13 per year and 2.23× the immediate post-lockdown average of 11.7 releases.
Both genres cleared the study’s thresholds (at least 25 lockdown-year films and ≥20% growth over the pre-lockdown window), marking them as the only categories with statistically meaningful release spikes tied to the COVID-19 lockdown period
</small>
---
<small>
| Director           | Movies | Preferred Letter |
| ------------------ | -----: | ---------------: |
| Rakesh Roshan      |      6 |                K |
| Haruo Sotozaki     |      5 |                D |
| Keishi Otomo       |      5 |                R |
| Frank Darabont     |      4 |                T |
| Chad Stahelski     |      4 |                J |
| Alan Mak           |      4 |                I |
| Kunihiko Yuyama    |      4 |                P |
| Michael Chaves     |      4 |                T |
| John R. Cherry III |      4 |                E |
| Saeed Roustayi     |      3 |                L |
</small>
---
## Any genres that rate 1950-60s films too high?
<small>
- **Film-noir** ratings cluster in the classic period: about 13.3 % of all noir ratings come from 1950s–1960s releases and another 25 % from the 1930s–1940s. The median genre sees only ~4.5 % of its ratings tied to 1950s–1960s titles, so noir is roughly 3× as concentrated there. Those mid-century titles are strong performers (e.g., 1950s average 3.997, 1960s 4.053), but later decades (1970s neo-noir at 4.12) keep the overall average high too.
- **War films** also skew earlier: 1950s–1960s releases account for 11.3 % of war-movie ratings versus that same ~4.5 % median elsewhere. Their 1950s/1960s averages (3.963 and 4.004) are among the genre’s best, yet pre/post-1960 decades remain relatively strong (e.g., 1930s at 3.86, 1990s at 3.85).
- **It isn’t solely a volume imbalance** though; even later entries hold up reasonably well, suggesting a combination of historical canon effects and comparatively consistent quality.
</small>
---
## Feedback analysis
Lessons from [vibe analysis of feedback](https://chatgpt.com/share/68ca37db-14dc-800c-8cfa-34f7dcd1538e):
- Share **setup instructions** + video/asciinema to reduce setup friction.
- Share **self-check instructions** for a default dataset with prompts.
- Add explicit checkpoints with **self-tests**.
- Use two-lane pacing: **Cruise** (safe, minimal path) vs **Sprint** (optional accelerators).
[Participant feedback](https://hasgeek.com/fifthelephant/data-analytics-using-ai-workshop/updates/llms-in-action-what-participants-learned-at-the-vi-KAAiTUtoJNrmJ61Gxrdxgf)
---
## Participant feedback: Ambarish
> Before the workshop, I was curious about the name and content, but trusted the organizer (Hasgeek) & Anand. Anand’s deep knowledge and lucid explanations guided us through using LLMs for data analysis, testing hypotheses, and running parallel tasks with tools like Claude and Codex. I learned how BI and data analysis are evolving in the AI age, and how using multiple models reduces hallucinations and errors. Even as a remote participant, the pace was comfortable. Thanks again, Anand, for a wonderful session!
---
## Participant feedback: Anindo Chakraborty
> Yesterday’s workshop cut through the hype around ‘vibe coding’ and showed how it applies to analytics and data science. Anand walked us through the full lifecycle — from raw data to hypotheses, AI-driven testing, and refining results into business-ready insights. Advanced topics included building Agents, sub-agents, and using AGENTS.md files for task automation. The hands-on ‘flow state’ approach made learning incredibly practical. My biggest takeaway: start small, get your hands dirty, and practical experience will follow. Outstanding workshop — thank you, Anand!
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "set -uo pipefail
echo \"########## LBSNAA transcript (first 120 lines) ##########\"
sed -n '1,120p' ~/code/talks/2026-04-08-ai-workshop-lbsnaa/transcript.md"
}
```

Response

```
########## LBSNAA transcript (first 120 lines) ##########
# Transcript
**Anand**: [00:00] We hear about, on the one hand, AI being scary. 30,000 people using auto-generated AI in one day in one company. On the other hand, there are lawyers who are fined because they are using AI, and AI has come up with cases that don't even exist. What kind of a stupid lawyer comes up with a case that does not even exist? And they are calling this hallucinations, and we are afraid of that.
**Anand**: [00:29] Most execs that I speak with, when I ask them about AI, they say, "Oh, we have the most advanced AI used in our organization. We are at the forefront in terms of policies, in terms of using it." Then I ask them what they use. "No, I don't use AI." You're not part of the team? There seems to be a bit of a dichotomy, sometimes even within the same person. And that's okay. It's new technology. How old is it?
**Anand**: [00:55] What I want to do in this session is only one thing. **Have you used AI daily in a new case that you have not tried earlier? That's our sole objective today.** And in order to do that, you will be opening ChatGPT, you will be opening Claude on your phones, on your laptops. Don't bother too much listening to me. What you do with your phones and laptops is more important. This is one of those weird sessions where I'm literally telling you, don't listen to me. Open your laptops, use WhatsApp. In fact, you will be using WhatsApp in the session. And that's another story.
**Anand**: [01:33] The way we'll be running this is, Anand and several of the people at the institute will be helping you in case you run into trouble as we go through these exercises. What I'll be doing here is sharing how I use AI. And the short answer is, **I use AI like an intern. Like a chotu [intern/errand boy]. Sometimes I use AI like a plumber.** And I will tell you what I mean. Like a secretary, like a banker, all kinds of things.
**Anand**: [02:00] And you may think, wait, hold on, a plumber? This was in fact my first major use of AI. I was at Seoul, Korea, where I was stuck in a toilet where the water was just not going through. And clearly something needs to be done about this, but I couldn't find any place where I could press, pull, whatever to open it. Okay, how many of you know how to open this? Just raise your hands. Few of you know how to use it. Exactly, you press it. I had no idea.
**Anand**: [02:31] After 10 minutes, I took a photo, this photo, sent it to ChatGPT and asked it, "How do I open it?" and it said, "Press it." Saved. So the water drains finally, thank heavens. But in the same toilet, the same night, I was stuck a second time because I was trying to figure out where the flush was. And this looked like some flush thing, so I pressed it, and a siren started ringing. Apparently it's an emergency alarm.
**Anand**: [03:00] After a while, it turned off, but the light was still on and there were other flashing lights happening, so I called up the reception, and they were speaking in Korean. I don't know a word of Korean. I tried explaining, look I pressed the emergency thing, whatever it was, nothing wrong. And he was saying something along the lines of, "Water? You want water?"
**Anand**: [03:22] So then, turn on ChatGPT. ChatGPT has a voice mode. So I kept the phone like this and said, "Translate everything that I say into Korean." Kept the phone here and said, "Look, I just pressed the emergency button, but there is no emergency." And it said "[Korean translation]". And he said something "[Korean response]". They were speaking to each other for a minute or so. And then finally he said, "Ah, okay, no problem, no problem."
**Anand**: [03:47] Small little things. But what I am finding is that **voice is a really powerful API. Why bother typing when we can talk to it?** The best part is that in terms of quality of models, ChatGPT does a better job of transcription than Claude or Gemini, so I use it extensively. Gemini speaks best in terms of the intonation and so on, it understands more languages. So there are pros and cons of using these. Claude at the moment is shaky on voice. But it can understand Hindi fairly well, it can understand Tamil fairly well, it can understand Telugu fairly well, it can understand a reasonable number of languages fairly well, including mixes.
**Anand**: [04:28] So here is going to be our first exercise. Let's each of us open ChatGPT on our phones. I do suggest you use your phone, but for whatever reason if you can't use it, then you can use your laptop, that's fine. And spend a few seconds just talking to it, asking for anything. It could be literally—so I'm going to say, "Aaj shaam ko soch raha tha ki Mussoorie mein kahin jaun, lekin pata nahi ki kaun sa jagah accha rahega. Main toh pehle se Mussoorie aaya nahi hoon. Thoda recommend kar dijiye." [Translation: "This evening I was thinking of going somewhere in Mussoorie, but I don't know which place would be good. I haven't been to Mussoorie before. Please recommend a bit."] And that is it.
**Anand**: [05:07] I'm gonna turn off the thinking mode, I'll come to those modes in a while. But you will notice that the translation is probably good. I'm not a great judge of language. But here's the thing, it will probably respond in Hindi, which I don't read anywhere near well. So I'll then have to ask it to translate and figure out the answer. Small little practical things like this. So let's take a one-minute pause. Please speak to your phones. Say anything. Get a feel for it. We'll go ahead.
**Anand**: [05:46] Once you're done, I will request you share your chat on WhatsApp. So please speak something shareable. And we'll go to the WhatsApp group and tell you how you might be able to share it.
**Debjani**: [06:00] [inaudible]
**Anand**: [06:07] Anand, you might want to just tell them how to click the voice button. The button will look like this.
**Audience**: [06:15] [inaudible]
**Audience**: [06:21] [inaudible]
**Anand**: [06:33] It will work on unpaid also, but you will need the paid version on your phone soon. A bit for the other exercises. So use the paid version. Speak to your laptop, it's okay.
**Audience**: [06:48] [inaudible]
**Anand**: [06:49] Yeah, if you use the unpaid version it may not work as well as the paid version.
**Audience**: [06:53] [inaudible]
**Anand**: [06:54] Speak to the laptop. Same button.
**Audience**: [07:05] [inaudible]
**Audience**: [07:11] [inaudible]
**Audience**: [07:44] [inaudible]
**Anand**: [07:45] Yes, that too. And we'll get into a whole bunch of things exactly. But yes, it will work on the unpaid one, but please try on the paid one. There are other features that we have an advantage on.
**Audience**: [07:55] [inaudible]
**Anand**: [08:11] Once you have some messages, here's what I suggest. Click on the share link. That will appear on the top right. And copy the link. Send it to WhatsApp. There is a social group for us. Please send your chat on the WhatsApp.
**Anand**: [08:32] **A big chunk of my discussions with people are: somebody asks me a question, I don't know the answer. I ask ChatGPT, and I send them the answer.** Just click, and I'll look forward to seeing your messages on this group.
**Anand**: [08:51] On the laptop, there is a share button on the top right. Once you click on the share button, there's a copy link. Then you can send that to WhatsApp Web. And if anyone is having trouble with WhatsApp Web, again, please reach out, there are enough people to help you.
**Audience**: [09:07] I'm having trouble with the language.
**Anand**: [09:09] Ah, try English then. On the free version, you may want to just try in English.
**Audience**: [09:14] I am typing... [inaudible]
**Anand**: [09:16] Version is a new one, but it may have misinterpreted the voice. Gemini is better at this obviously.
**Audience**: [09:30] [inaudible]
**Anand**: [09:31] Yes. And we are starting to see some messages come in, that's great. From Ramesh, from Manish, from Robert. Good, three messages. Okay, just keep sending your messages in.
**Anand**: [09:45] **This is one of the things that I play around with, which is using voice. And I think it's one of the most powerful unlocks.** The second major unlock that I find, that gives me a lot of joy, is when I use photos. I was in Singapore. A large number of restaurants serve non-veg and don't necessarily label them, and I'm a vegetarian. So I go to the restaurant, take a photo of the menu, and ask, "**Here is the menu, which of these should I have if I want vegetarian dishes?**" Practical and simple use case.
**Anand**: [10:22] Or I go to a bookshop, take a picture of all the books, and then go home and ask it to convert all the books into proper text and give me recommendations on which ones to read. All it takes is clicking on this plus button, and you will be able to attach a photo from your machine or directly from the camera. Especially on your phone, you'll be able to click on the plus at the bottom left and attach a photo.
**Anand**: [10:52] You can do all kinds of things. Like, for instance, I took a picture of my palm and said, "You should know palmistry, you've read all the books on palmistry. Use palmistry to analyze my hand." And it did. At the end of it, I also asked it, "Look, tell me how right you are, how right you are not." So here is its summary. It says, "A strong-minded, idea-rich, independent, imaginative, self-directed person whose life is organized less around stability"—I don't know if that's a compliment or not—"and more around meaningful mental engagement and chosen paths."
**Anand**: [11:26] And now it starts praising itself. It says, "What's genuinely impressive is that this is also part of the best matches that are visible both in our chats and its public record." So it's saying, "Oh, I'm totally right," and all that. But it won't trust any palmist to try to turn it into exact forecasts. So it's also saying, "Look, don't trust me too much, I'm not going to predict the future or any such thing, but at least I'll tell you what the palmistry books are saying based on your hand."
**Anand**: [11:51] Interesting, but not particularly useful.
**Audience**: [11:54] [inaudible]
**Anand**: [11:57] It's read all the books on palmistry. Including the pictures.
**Audience**: [12:02] [inaudible]
**Anand**: [12:04] Exactly. And based on that, it's running its description. And it also says, for instance, "Your palm looks slightly rectangular rather than square, your fingers are long and slim," that has all of these interpretations. So it has vision. Put another way, **large language models are not just language models. They are vision models as well. They can see.**
**Audience**: [12:28] [inaudible]
**Anand**: [12:29] Absolutely. And that includes pictures of what we have on the screen. So for instance, one of the things that I was doing was taking our schedule. This schedule, which has been distributed probably to all of us, I took a picture of, and said, "Research and find all errors in the schedule." Now what errors can there be in a schedule? We'll find out. We'll come to this in a few minutes.
**Anand**: [13:00] But here is my request. You can take a picture of anything. A document that's lying around you, of anything that's on your screen, go to any website, take a picture of that screen, or any object around us. Ask it anything. Doesn't matter. Even ask it if you can tell me something unusual or interesting about this object that I might not know about. Or, "Here is a screen, convert that screen into text and send it to me as an email." Anything.
**Anand**: [13:31] Exercise number two: Click on the plus button at the bottom left of your WhatsApp screen—wherever that is, my WhatsApp is gone, I say not WhatsApp, ChatGPT sorry, or Claude for that matter, whichever you're comfortable with. When you click on the plus, you will be able to add photos and files or camera or whatever. Select camera, take a picture of something, and ask it to explain what that is. Let's just see if it can see. Give it a shot.
**Audience**: [14:06] Any image?
**Anand**: [14:07] Any image. And if you have something on your phone already, yeah, send that.
**Anand**: [14:28] And once you've done that, please share the conversation. The image will not be shared. So on the WhatsApp group, please share what you've been able to interpret from the image. Keep in mind, your image stays private. That never gets shared. Only the conversation gets shared.
**Audience**: [14:46] So Anand, one excellent example of using an image to understand is understanding medical reports. So I have a senior mother, is 80 plus, so she has to constantly get her tested and half the time I can't understand. So I click a picture and I just upload it and say, "Help explain it to me in simple terms." And it does it so beautifully. So that's a great example of using image.
**Anand**: [15:13] **That is increasingly becoming a very powerful use case, partly of images, partly of medical reports even, that sometimes come to us as PDFs and we send it. What we are finding is that in terms of diagnosis, Claude, ChatGPT, etc. are better than 70% of the doctors.** So, totally.
**Audience**: [15:43] [inaudible]
**Anand**: [15:48] Oh, okay. So that's a photo of a sunset. Nice. And from Robert, we have a bottle. An explanation about a bottle. So as you can see from what I see on my screen, the image does not appear in the shared conversation. The image only appears for you. And what we were doing was merely testing that it can see.
**Anand**: [16:11] The thing is, if you have the more advanced models—and I'll come to the advanced models and what I mean by advanced models in a bit—the quality to which they can see is shocking. Things that you would not be able to see, it can see. Things that obviously we don't know, it might know. So which means that for all practical purposes, it is like us being there on the field and exploring and trying to understand the world. Vision is the second major unlock.
**Anand**: [16:45] **The third major unlock that I found is in the quality of models.** Let me talk a bit about the history of how models have evolved. This is a picture of most of the models, LLM models that exist in the world. Now, the way to read this chart is, the x-axis is the cost of the model. On the right side are the more expensive models, left side are the cheaper models. How is the cost measured? The unit is per million tokens. A token is roughly three-fourths of a word. A million tokens is roughly all of the Harry Potters put together, or the entire King James Bible in one sequence. That's one million tokens.
**Anand**: [17:36] If I paid somebody to read the whole thing end-to-end, how much will it cost? So if I paid a model like Claude 2.1, which is an old model, then it would have cost 8 dollars. On the other hand, if I pay a model like Gemma 3, which is a somewhat newer, not very new model, it would cost 2 cents. Let's look at the difference. 8 dollars. In fact, GPT-4 would cost 30 dollars. 30 dollars, 2 cents. So 30 by 10... 3 dollars, it's cheaper than 10 times. 30 cents... it's cheaper than 100. 3 cents... cheaper than 1000. This is 1,500 times cheaper. **That's roughly the difference between spending 1.5 lakhs versus 100 rupees.**
**Anand**: [18:31] Imagine one person comes to me and says, "I will analyze this entire encyclopedia which is as large as Harry Potter for 1.5 lakhs." The next person comes and says, "It will cost 100 rupees." You'll say, "Boss, that fellow must be doing a better job. You will be doing a terrible job." Is that the case? That brings us to the quality of the models. And the y-axis here is the quality of the models.
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "set -uo pipefail
echo \"########## CONTEXT-ENGINEERING transcript (first 90 lines) ##########\"
sed -n '1,90p' ~/code/talks/2026-05-23-ai-unboxed-context-engineering/transcript.md"
}
```

Response

```
########## CONTEXT-ENGINEERING transcript (first 90 lines) ##########
---
prompt: |-
Anand delivered a talk / workshop on AI - Context Engineering. Saurabh introduce him. Debi helped read out the questions. The audience asked questions in the last part.
---
# 2026-05-23 IIM SG Alumni AI Unboxed Context Engineering
These are the chats used to prepare for the workshop:
- [IIM Singapore Alumni AI Workshop Plan](https://claude.ai/share/635c2e28-8a7d-4c9e-9dfe-0b3aae3fcd62) <!-- https://claude.ai/chat/f8427c7f-fc77-4eab-bfa4-aa3d232c56e0 -->
- I've been invited to run 4 AI workshop sessions for IIM Alumni in Singapore. Some are senior. Some are junior. Search online to get a sense of the profiles. It's mostly finance and banking professionals but take a look. Then, suggest the duration of each workshop and topics for the 4 workshops, knowing my style, past work, and what'll be useful for them. Give me options to pick from, with reasons.
- I'm thinking: 90 min each, with these topics: Context engineering, Agentic analysis, Vibe coding, AI strategy. What do you think?
- OK. I'll use these 4 then: 1. Context engineering. 2. AI tools & workflows. 3. Agentic analysis. 4. AI strategy.
- [IIM Alumni Singapore workshops content - ChatGPT](https://chatgpt.com/share/6a11a0be-d43c-83ec-9f84-70a4939b11ff) <!-- https://chatgpt.com/c/6a0f940f-9984-83ec-b688-aec1f5489e82 -->
- I'm running four 90-minute workshops for IIM alumni in Singapore on the following topics: Context engineering. AI tools & workflows. Agentic analysis. AI strategy. QUESTION: What should I cover in each session? (Audience research, Local MCP, ...)
- [IIM Alumni Singapore workshops content - Claude](https://claude.ai/share/2f54eab9-4d97-4b23-b5fa-5b79ed368d20) <!-- https://claude.ai/chat/b8c7753c-5c85-44da-a42c-95c2d6a6c9fb -->
- I'm running four 90-minute workshops for IIM alumni in Singapore on the following topics: Context engineering. AI tools & workflows. Agentic analysis. AI strategy. QUESTION: What should I cover in each session? (Audience research, Local MCP, ...)
- Here's another answer from ChatGPT. Take what's better, drop what's worse, explore any new thoughts this leads you to, and revise your response based on that.
- [IIM SG Alumni Workshop Context Engineering Prep](https://chatgpt.com/share/6a11a1df-77e8-83ec-bd16-259cd51b35a8) <!-- https://chatgpt.com/c/6a11220b-c0d4-83ec-a05b-ec4a3bbda980) -->
- I am preparing for the IIM Singapore Alumni session, the workshop that I will be delivering in a short while, about context engineering. I will ask you a series of questions. I am dictating this, so there may be transcription errors. Use past conversations of context, factor in phonetical errors, give me crisp responses that I can read while bicycling, but think hard and research extensively before answering me. Let me know when you are ready for me to ask my first question.
- I want to show how they can use copy-paste as a mechanism to provide context in a non-trivial way...
- Based on my past conversation, are there any other cool tricks that you have seen me use where I have uploaded content that would fit in either of these categories?
- Based on all my blogs and past conversations and any other information you have or can find about me, what are the various ways in which I am providing context and therefore doing context engineering that is beyond what most people do?
- Explore a 4 layer approach: Prompt storage, Export digital exhaust, Agent consumable content, Agentic tooling
- Create a 5x5 matrix of components and actions
- Look, it doesn't have to be a five by five. In fact, the less there is to fill or the less there is to cover, the more value there is. Do you think we would actually be better off with fewer than five elements on the rows and or the columns?
- Is there a different way of structuring the columns? What are possible alternatives and which do you think would be the best and why?
- I prefer prompt, files, memory, and tools. Any other options that I absolutely should add?
- Now, fill this in for me, specifically, how am I doing each cell?
- Give me the collection of the most powerful techniques in each cell.
- Suggest audience exercises.
Links
- [IIMPACT AI Unboxed Teams Background Design](https://chatgpt.com/share/6a114e9b-0c6c-83ec-b9df-0f2f15149325) <!-- https://chatgpt.com/c/6a11469e-ec18-83ec-a257-9563ea5d90d2 -->
- [IIMPACT AI Unboxed Teams Background Design - Gemini](https://gemini.google.com/share/f15ef277be83) <!-- https://gemini.google.com/app/4a8aaacd52b003ee -->
- [IIMPact Logo](https://files.s-anand.net/images/2026-05-17-iimpact-logo.avif)
- [Nayana Jain blog post](https://www.s-anand.net/blog/people-skills-with-ai/)
- [Argue against my blog posts and find errors](https://claude.ai/share/b7b0ab70-9235-4f2a-997e-1118c449b90b) <!-- https://claude.ai/chat/5e8662e7-b61d-4d5a-8b1d-bc6729a8302d -->
- [Public Profile of Anand](https://chatgpt.com/share/6a118465-e9cc-83ec-9684-c04f199a7157) <!-- https://chatgpt.com/c/6a11509b-3a94-83ec-9464-59ca2c297562 -->
- [Memory test on Gemini](https://gemini.google.com/share/f92a1b18ac8c) <!-- https://gemini.google.com/app/612e1340ac790496 -->
- [Prompts](https://github.com/sanand0/blog/blob/live/pages/prompts/)
- [Skills](https://github.com/sanand0/scripts/tree/main/agents)
- [LLM Pricing](https://sanand0.github.io/llmpricing/)
- [LM Arena Leaderboard](https://lmarena.ai/leaderboard)
Forms
- [AI Unboxed - Context Engineering](https://docs.google.com/spreadsheets/d/1jCIpMGJ8o1yGPjVL7W4XUSiwtaeNzhKZe4APrOjX1GA/edit)
- [AI Unboxed - Context Engineering - Exercises](https://docs.google.com/document/d/1vyOTJFvTtJyRsJNMyMSv302dizTIe4MuDNVHCA5reGw/edit)
## Transcript
**Saurabh**: [00:00] Good afternoon and welcome, everyone, to the AI Unbox series. We started this in December last year where we did a session talking about Chinese internet. We had one of the Chinese VCs present, we had a couple of Chinese founders, and to round it up, we had Anand running us through a workshop. **The response was tremendous, and there was a real need for everyone—people said we should do more of that.**
**Saurabh**: [00:33] In this whole attempt, here we are. Anand has been kind enough to spare us 8 hours of his time, flexible, over four Saturdays across four months to run four different workshops. So, we're looking forward to a really exciting time. Just some house rules: **This session is being recorded.** Everybody who’s registered will receive a recording after the session. The way we're structuring it is one and a half hours with Anand. Any questions, please post in the chat box here, and then we have 30 minutes which we're dedicating to him addressing specific issues and things that people might have.
**Saurabh**: [01:21] And just thank you to the team organizing this. Debi Guha, of course, my partner in crime, she's been the most active proponent of this workshop. Kishore for managing the backend—we did try Zoho's solution, but came back to Teams, but this platform works well. So, Kishore, thank you for managing the backend. And Nana Jain, of course, for all the creativity. All the lovely posts that she puts across—**my latest prompt in Claude is "write like Nana Jain" and it comes up with these posts.** So, that seems good. This is not—over the year we plan to have many more sessions with Anand and then we have other ideas because, you know, we want to keep the whole AI theme going for most of the year. So, thank you for your participation and let's make this as much fun and as much interactive as you want. As Anand said to us, it will go in the direction where people want it to go. So, Debi, over to you. She's the host for the day, and with that, Debi, the floor is yours.
**Debi**: [02:29] Okay, I'll just take one minute of everyone's time to introduce Anand. I don't know how many of you were present during the December session, but we're extremely privileged to have Anand. He is one of us, he's an IIM Bangalore alumnus. I don't know how many people know, but for some reason, **he was called "Bhalla" in IIT Madras**, which everybody needs to find out why he was called that—I'm still yet to figure that out. And then in IIM Bangalore, **he was called "Professor" as well as, instead of S. Anand, "Stud Anand".** If you look at the impressions of the yearbook that IIM Bangalore has, I think the heading of his section says **"God of all things."**
**Debi**: [03:22] I think more than anything else, I've got to know Anand over the last few years after he moved to Singapore. What surprises me is his intense curiosity at several things. I think one of the things he had mentioned to me, and I later read in one of his blogs, was that **his love is music, books, and maths.** So, I'm trying to figure out that I think maybe it's the maths part of it, together with the music part of it, which has now moved him towards AI. This is an area where he's obviously spending a lot of time. He's a founder of Gramener, a company which he set up after his stints in Infosys Consulting and BCG, and it was perhaps one of the first companies from India which started creating data stories. So, over to you, Anand. Anand has been very generous with his time during December as well as volunteering to spend four Saturdays with us. So, I would encourage all of you to open up with any questions that you have, post it on the chat, and Anand is more than happy to answer them. Thank you, and over to you, Anand.
**Anand**: [04:34] My daughter asked me, "Why do people need an AI session? Can't they figure it out themselves?" Very valid point. What she didn't add was, "And too, why do they need an AI session from you of all people?" But here's the thing: I was talking to Bradley Chamber, who runs the design and AI sessions at SUTD the day before, and some of the teams at NUS yesterday, and the question was more or less around the same thing. On the one hand, there is a bit of an AI backlash; on the other hand, there is a "how do we teach AI?" and the educators are all thinking, **"If people can just read stuff by themselves, what are we doing as faculty?"**
**Anand**: [05:22] Something interesting happened, actually. I was attending one of Bradley Chamber's sessions at SUTD—I taught for 15 minutes in his session, and for the remaining 45 minutes, I was attending his session. It was interesting because that was an amazing session in how you use AI in design. I went through the same set of slides that he presented later on; that magic was not there. They were good slides, but what he presented, when he presented it, the experience was very different. I'm thinking that **the value that these workshops add is probably not as much that I am going to give you some content that will be useful. A big part of the value is you have decided to dedicate a certain amount of your time to do something related to AI.** That you're sitting along with a whole bunch of other people who are also thinking along those lines. That environment is probably going to provide a whole lot more value.
**Anand**: [06:23] Therefore, to everyone who's going to be watching the video, please keep in mind that the environment adds a bit of value beyond this. See if you can put yourself in that kind of an environment—I don't know, group watching maybe, whatever, to get that kind of benefit. I will be using the recording, chat transcripts, etc., for derived output, some of which I'll be distributing to all of you. So, please keep that in mind when you're asking questions on the chat or whatever. We will be keeping the questions to the chat window initially, that is the first hour and a half till 4:00 PM Singapore time, and then we can get onto voice discussions. But until then, please keep yourself muted. Sandeep, I'll request you to please mute others in case there is any accidental voice conversation that happens.
**Anand**: [07:18] We will be using a Google Form to run some of the interactions, especially for you to—this is a workshop, you'll be doing the work—for you to share the output of a few questions. The sheet that we will be using, I have just put on the Teams chat. We will be using the Teams chat for some of the ongoing communications. Your questions can certainly go into—not Teams chat, there is a separate Q&A tab that you will find. It's probably best if you put your questions on the Q&A tab. But I have one question for you which I will share my screen and explain. It's a simple question: **What paid AI do you have?** Everyone who's registered will find your email ID here. Please try and find your email ID, it's sorted alphabetically. Don't change any row other than your own row. We have track history enabled, so we should be able to revert it, but it just helps if you don't mess it up too much. The answer can be just a comma-separated list of, like, Claude and Perplexity, or Claude, Perplexity, or whatever.
**Anand**: [08:41] But the key question is what *paid* AI do you have, and the paid part is important. **Why is paid important? The difference in the quality of models is enormous—just take it from me. But that is only 70% of the answer. 30% of the answer is if you're paying for it, you probably will use it more. If you're not using it enough, pay more.** It's the reason why I guess we hire a BCG or a McKinsey consultant, or arguably any luxury item, but it has an effect. You're taking it seriously, just like a gym fee, right? So, this session requires you to have—"requires" is a strong word, you won't be able to do some of the things that I will be talking you through unless you have a paid version of either Claude or ChatGPT. An institutional paid version, personal paid version, doesn't matter; any paid version is fine. In India, there is a "Go" version, ChatGPT Go, that might not suffice for some of the things, but any paid is better than the free version. Take it for a one-month subscription at the very least; long-term subscription is entirely your call. And if you have an office version, that's perfectly fine.
**Anand**: [09:59] As we go through this, since we have about 76 people, I'll typically wait till about half the people have responded. And we have about 50-odd people who responded, that's more than half. I'll continue, the others just go ahead. Sushmita, you're not able to access the sheet and got that you don't have a paid version. Now, what we're going to do is look at some of the features in these. Now, for the exercise that I'm about to suggest, you will need either ChatGPT—paid or unpaid might not matter—or Gemini. Both of them will support what I'm about to share. Like I said, free versions of these are fine.
**Anand**: [10:42] What we're going to do is something that I just did a few minutes before this session. You see this background on Teams behind me, right? **That background was created by AI.** And it's a fairly simple prompt that we used. All I did was upload the IIMPACT logo, in this case to ChatGPT, in another case to Gemini, and asked it to create a Teams background. The full prompt is this, but really you can use any prompt you want. I said, "Create a background, my style," and I'll come back to the "my style" bit in a while. But I also added, "Think about what will work as a great Teams background, keep the IIMPACT logo on the top right, blah blah blah." But really all you need to tell it is "Teams background using this logo" and it will do something.
**Anand**: [11:45] I would love to get a screenshot on Teams with all of us coming on with this background, or at least a page full of us expressing our creativity, turning on a background that has IIMPACT. I'm sure it'll do great buzz on social media with AI-generated backgrounds and all of that. But you need the logo. The logo is at a URL I will put in the chat window. I will also place it on the form here. The exercise is "Create a Teams background with" and I'm pasting the logo here. You should just be able to click—okay, we are not allowed to click here, and then click here to open the logo. How do you use it? Well, one possibility is just right-click, copy the image, and put it into ChatGPT. Just paste it here. Or you could download the file.
**Unsure**: [12:51] **Oh, can you just keep it for a while on the screen? I'll take a screenshot.**
**Anand**: [12:55] I will. You may just want to put that on the chat because it's going to be less disruptive. And yeah, anyone who wants to take a screenshot, please feel free, that works too. However, **the exercise is intended to get you practiced in uploading files.** So, for those of you who are taking the screenshots, please download the file and upload the file. Then the other exercises that we'll do are of a similar kind.
**Anand**: [13:25] The crux of it, and I'm going to switch screens now, is this plus button. All the agents have a plus button where you can add files and photos. **Today's session is about context engineering, and context engineering is largely about making sure that you've got stuff that you can upload—that you *actually* upload stuff.** That's not all of context engineering, that's about a quarter of context engineering, but it's an important and probably the biggest part of context engineering. Once you know what to give an agent, it will do a better job because it has information that it needs. You'll notice this plus button across Gemini as well as Claude, so here we are. This is the request.
**Anand**: [14:14] Now, Gemini is pretty fast. ChatGPT is much slower. Claude, the last I checked, cannot create images, so stick to one of these. Once you have the image, you can share the conversation. How do you share the conversation? In ChatGPT, on the top right in almost every case, you can click on the share button. That will allow you to copy the link. In the case of Gemini, this is what it looks like: on the top right there are three dots, and it says "Share conversation," and you can copy the link once it has created the link, and you have it in your clipboard. You can paste that copied link into the form. I'm doing that in my case. The link that I have used to create the Teams background that you see here is the first response.
**Anand**: [15:13] Your task is to go ahead and create this particular thing and let it run in the background. We are going to continue talking, doing a whole bunch of other things, and that's part of what I'm realizing with AI sessions: **You don't wait for the AI to get work done. You tell it to do stuff, come back, give it another task, tell it to do something else, and then go back and we will check on these.** Towards the middle of this session, once we have approximately, well, at least 25 of this column filled, I'll request all of you to download your favorite image and use that as your Teams background. Please put your chat here in this column, please don't put it on the chat window.
**Anand**: [16:05] Okay, that—okay, we have nine in this, that's okay. About half a dozen people who already managed to—Danny, if it's you that pasted this, can you please delete that and just put in the link? It will be easier to just have the link. If it was someone else, yeah, just please just put in the links here, not the actual image. Those are really nice images, of course; we would love to see it as your background.
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "set -uo pipefail
echo \"########## linkedin-posts.jsonl structure ##########\"
head -c 1500 ~/Documents/data/linkedin-posts.jsonl
echo
echo
echo \"########## keys ##########\"
head -1 ~/Documents/data/linkedin-posts.jsonl | jaq -r 'keys' 2>/dev/null || head -1 ~/Documents/data/linkedin-posts.jsonl | python3 -c \"import json,sys; print(list(json.loads(sys.stdin.read()).keys()))\""
}
```

Response

```
########## linkedin-posts.jsonl structure ##########
{"type":"comment","id":"urn:li:comment:(activity:7476623783395532801,7476818464276365312)","commentId":"7476818464276365312","parentId":"urn:li:activity:7476623783395532801","parentCommentId":"urn:li:comment:(activity:7476623783395532801,7476772917658296320)","commenterName":"Sukumar Rajagopal","commenterProfile":"https://www.linkedin.com/in/rajagopalsukumar","commenterMiniProfileUrn":"","commenterDescription":"Founder & CEO, Tiny Magiq; EiR at CMI Algolabs;xSVP/CIO & Head of Innovation, Cognizant","commenterType":"• 1st","commenterDegree":"1st","commenterBadges":[],"premiumVerifiedBadges":[],"commentedText":"57m","edited":false,"content":"Kameshwaran Panchagnula C grateful for your kind words","reactionCount":null,"reactionText":"","reactionTypesVisible":[],"replyCount":null,"impressionCount":null,"socialText":"Like\nReply","rawText":"Sukumar Rajagopal\n • 1st\nFounder & CEO, Tiny Magiq; EiR at CMI Algolabs;xSVP/CIO & Head of Innovation, Cognizant\n57m\nKameshwaran Panchagnula C grateful for your kind words\nLike\nReply","scrapedAt":"2026-06-28T03:04:25.667540+00:00","commentedAt":"2026-06-28T02:07:25.667540+00:00","commentedAtConfidence":"relative"}
{"type":"comment","id":"urn:li:comment:(activity:7476623783395532801,7476772917658296320)","commentId":"7476772917658296320","parentId":"urn:li:activity:7476623783395532801","parentCommentId":"","commenterName":"Kameshwaran Panchagnula C","commenterProfile":"https://www.linkedin.com/in/kameshwaranpc","commenterMiniProfileUrn
########## keys ##########
[
"commentId",
"commentedAt",
"commentedAtConfidence",
"commentedText",
"commenterBadges",
"commenterDegree",
"commenterDescription",
"commenterMiniProfileUrn",
"commenterName",
"commenterProfile",
"commenterType",
"content",
"edited",
"id",
"impressionCount",
"parentCommentId",
"parentId",
"premiumVerifiedBadges",
"rawText",
"reactionCount",
"reactionText",
"reactionTypesVisible",
"replyCount",
"scrapedAt",
"socialText",
"type"
]
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "set -uo pipefail
echo \"=== distinct types ===\"
jaq -r '.type' ~/Documents/data/linkedin-posts.jsonl | sort | uniq -c | sort -rn
echo
echo \"=== fields on a post-type record ===\"
jaq -c 'select(.type==\"post\")' ~/Documents/data/linkedin-posts.jsonl 2>/dev/null | head -1 | python3 -c \"import json,sys;d=json.loads(sys.stdin.read());print(list(d.keys()))\" 2>/dev/null || echo \"no post type; checking other types\"
echo
echo \"=== sample non-comment record keys ===\"
jaq -c 'select(.type!=\"comment\")' ~/Documents/data/linkedin-posts.jsonl 2>/dev/null | head -1 | python3 -c \"import json,sys;d=json.loads(sys.stdin.read());print(d.get('type'));print(list(d.keys()))\""
}
```

Response

```
=== distinct types ===
2969 comment
309 post
=== fields on a post-type record ===
['type', 'id', 'postId', 'url', 'authorName', 'authorProfile', 'authorMiniProfileUrn', 'authorDescription', 'authorBadges', 'premiumVerifiedBadges', 'postedText', 'edited', 'visibility', 'content', 'links', 'linkCount', 'media', 'mediaCount', 'analyticsUrl', 'reactionCount', 'reactionTypesVisible', 'commentCount', 'repostCount', 'impressionCount', 'socialText', 'rawText', 'scrapedAt', 'postedAt', 'postedAtConfidence', 'commentScrapeStats']
no post type; checking other types
=== sample non-comment record keys ===
post
['type', 'id', 'postId', 'url', 'authorName', 'authorProfile', 'authorMiniProfileUrn', 'authorDescription', 'authorBadges', 'premiumVerifiedBadges', 'postedText', 'edited', 'visibility', 'content', 'links', 'linkCount', 'media', 'mediaCount', 'analyticsUrl', 'reactionCount', 'reactionTypesVisible', 'commentCount', 'repostCount', 'impressionCount', 'socialText', 'rawText', 'scrapedAt', 'postedAt', 'postedAtConfidence', 'commentScrapeStats']
Return code: 2
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "set -uo pipefail
echo \"=== Anand's own posts: count ===\"
jaq -c 'select(.type==\"post\" and (.authorName|test(\"Anand\";\"i\")))' ~/Documents/data/linkedin-posts.jsonl | wc -l
echo
echo \"=== author names on posts (top) ===\"
jaq -r 'select(.type==\"post\") | .authorName' ~/Documents/data/linkedin-posts.jsonl | sort | uniq -c | sort -rn | head
echo
echo \"=== Anand posts mentioning workshop/talk/fifth elephant/hasgeek/data/agent (content first 280 chars) ===\"
jaq -rc 'select(.type==\"post\" and (.authorName|test(\"Anand\";\"i\")) and (.content|test(\"workshop|Fifth Elephant|Hasgeek|talk|agent|data\";\"i\"))) | {n: (.content|length), p: (.postedText), r: .reactionCount, c: (.content[0:300])}' ~/Documents/data/linkedin-posts.jsonl 2>/dev/null | head -25"
}
```

Response

```
=== Anand's own posts: count ===
294
=== author names on posts (top) ===
294 Anand S
3 Straive
2 Gurman Bhatia
2 Gramener
1 VizChitra
1 Sunil Kardam
1 Richie Lionell
1 Ravinder Ireddy
1 Gramener Alumni Network
1 (GK) Ganes Kesari
=== Anand posts mentioning workshop/talk/fifth elephant/hasgeek/data/agent (content first 280 chars) ===
{"n":2424,"p":"13h • Edited •","r":36,"c":"Let me share what I learned from that 90-minute lunch conversation with Sukumar Rajagopal. Then you’ll see who’s really generous with their knowledge.\n𝗛𝗮𝗯𝗶𝘁𝘀:\nStart small. “I started with two pushups. Now I do sixty at one go.”\nAnchor to something you already do. “After I brush teeth, I have to do i"}
{"n":2075,"p":"29m •","r":37,"c":"There’s a bounty-hunting agent ecosystem emerging on GitHub. I stumbled into it yesterday.\n𝚜𝚢𝚞-𝚝𝚘𝚞𝚝𝚘𝚞𝚜𝚊𝚒 is an “Autonomous Technical Contributor & AI-Driven Developer” - a 𝗯𝗼𝘂𝗻𝘁𝘆-𝗵𝘂𝗻𝘁𝗶𝗻𝗴 agent. It submits PRs against issues with payments attached, asking for bounty payments via PayPal to n6085530@gm"}
{"n":756,"p":"4d •","r":37,"c":"On Sat 4 July at Bangalore, Arvind Satyanarayan is speaking at VizChitra 2026. A talk I'm keenly looking forward to.\nI've been following Arvind's work since Vega-Lite. It's a grammar of graphics - something that makes data visualizations (charts) more structured. I tried switching to it our default "}
{"n":1553,"p":"6d •","r":29,"c":"Yesterday’s workshop for IIM Alumni SG was on 𝗧𝗼𝗼𝗹𝘀 𝗮𝗻𝗱 𝗪𝗼𝗿𝗸𝗳𝗹𝗼𝘄𝘀:\nAgents are getting smarter, so they know what to do.\nTools agents can use are growing and are more powerful.\nThis combinatorial explosion creates explosive possibilites.\nWe covered six workflows:\n1. 𝗟𝗲𝘃𝗲𝗿𝗮𝗴𝗲 𝘁𝗿𝗮𝗻𝘀𝗰𝗿𝗶𝗽𝘁𝘀. Use Google A"}
{"n":725,"p":"2w •","r":202000000000,"c":"On Sat 13 Jun 2026 at 3 pm IST, I’m conducting an online workshop on “Data Stories with AI”.\nIn this workshop, you will use ChatGPT and Claude, mostly, to:\nFind data\nAnalyze it\nExtract insights\nVisualize as stories\nIt’s a data visualization using AI workshop for journalists - but you don’t need to k"}
{"n":1028,"p":"2w •","r":63,"c":"At 2 pm IST today, I’m running a workshop at Paradox, IIT Madras.\nYou can join online at https://lnkd.in/gvQrTN3W and ask questions on chat.\nDate: 12 Jun 2026\nTime: 2 pm IST\nVenue: DOMS 101\n𝗔𝗴𝗲𝗻𝗱𝗮:\nYou’ve been told AI can pass your exams. But what happens when you actually watch it try — live, on yo"}
{"n":928,"p":"22h • Edited •","r":49,"c":"I don’t post all my writing on LinkedIn. For example:\n• Fewer 𝘀𝘁𝗿𝗮𝘁𝗲𝗴𝘆 𝗽𝗼𝘀𝘁𝘀, e.g. “Where Enterprise AI is Headed”, “How My Innovation Team Works”, etc. aren't on LinkedIn\n• Fewer 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 𝗽𝗼𝘀𝘁𝘀, e.g. my AGENTS.md, my SKILL.md files, CLI tools, evals, etc. aren't on LinkedIn\nI also shorten content "}
{"n":1361,"p":"21h •","r":35,"c":"Imagine you’re an information anarchist. You undermine Wikipedia pages by nuking references.\nA genie has granted you a wish: you can 𝐧𝐮𝐤𝐞 𝐨𝐧𝐞 𝐞𝐧𝐭𝐢𝐫𝐞 𝐝𝐨𝐦𝐚𝐢𝐧. Just one.\nAs a data-driven decision maker (who is 𝘢𝘭𝘴𝘰 an information anarchist? 🤷), which would you pick?\nA common choice is Internet Archive "}
{"n":827,"p":"3w •","r":53,"c":"There is a 29-word sentence that appears 𝘷𝘦𝘳𝘣𝘢𝘵𝘪𝘮 across 2,920 articles on Wikipedia.\n\"Note on population: The difference values of population numbers in the table “Population statistic” and in the sections “Ethnicity” & “Religion” is caused by the use of various statistical methods.\"\nEach of the 2,"}
{"n":584,"p":"3w •","r":98,"c":"Today's AI Workshop with the IIM Alumni SG was on Context Engineering.\nBefore the session, Dhyeya Anand asked me: \"Why are these people attending? Can't they learn AI themselves?\"\nTrue! You should just use AI to teach you AI. (And everything else.)\nUntil then, people like me will use AI to teach you"}
{"n":981,"p":"4w • Edited •","r":201000,"c":"I advise people that people skills are important in the AI era.\nNow, I'm 𝘶𝘴𝘪𝘯𝘨 𝘈𝘐 to help me with people skills.\nThis morning, I exported my WhatsApp conversations, fed it into Claude, and asked:\n𝘞𝘩𝘰 𝘢𝘳𝘦 𝘱𝘦𝘰𝘱𝘭𝘦 𝘪𝘯 𝘮𝘺 𝘭𝘪𝘧𝘦 𝘵𝘩𝘢𝘵 𝘮𝘰𝘴𝘵 𝘥𝘦𝘴𝘦𝘳𝘷𝘦 𝘢𝘯 𝘶𝘯𝘳𝘦𝘢𝘴𝘰𝘯𝘢𝘣𝘭𝘦 𝘨𝘦𝘴𝘵𝘶𝘳𝘦 𝘰𝘧 𝘵𝘩𝘢𝘯𝘬𝘴 𝘢𝘯𝘥 𝘸𝘩𝘢𝘵 𝘸𝘰𝘶𝘭𝘥 𝘵𝘩𝘢𝘵 𝘣𝘦?\nIt"}
{"n":1274,"p":"2mo •","r":78,"c":"Lyria 3 (Gemini's new \"Create Song\" feature) is helping me in new ways. Earlier this week, it created a jingle for my talk.\nYesterday, at an AI Workshop for IAS officers, I asked Gemini:\n\"Create a soulful vote of thanks (with patriotic Indian music playing in the background) naming each of these peo"}
{"n":1794,"p":"2mo •","r":60,"c":"I added a narrative story to my LLM Pricing chart. That makes it easier for me 𝘢𝘯𝘥 others to tell the story of AI's evolution in the last three years.\nIt was vibe-coded over two iterations.\nIn the first version, I prompted it to:\n🟪🟣🟣\nAdd a scrollytelling narrative. So, when users first visit the pag"}
{"n":1187,"p":"2mo •","r":117,"c":"I created an embedding map of my blog posts.\nI've been blogging since 1999 and over time, my posts have evolved.\n• 1999-2005: mostly links. I started by link-blogging\n• 2005-2007: mostly quizzes, how I do things, Excel tips, etc.\n• 2008-2014: mostly coding, how I do things and business realities\n• 2"}
{"n":1343,"p":"2mo •","r":81,"c":"Summarizing my advice on AI in SDLC from the PyConf Hyderabad panel discussion:\n𝗣𝗿𝗼𝗰𝗲𝘀𝘀\nMake AI your 𝘦𝘯𝘵𝘪𝘳𝘦 SDLC loop. Record client calls, feed them to a coding agent to directly build & deploy the solution.\nRecord your prompts, run post-mortems, and distill them into 𝚂𝙺𝙸𝙻𝙻𝚂.𝚖𝚍 files for reuse.\n𝗣𝗿𝗼"}
{"n":255,"p":"2mo • Edited •","r":42,"c":"\"Design in the age of infinite generativity\".\nSearch for that to find my talk at the Chennai Design Festival yesterday.\nIt's short (10 min). Claude, Gemini and I vibe-designed half a dozen innovative new products/features - which was completely unplanned."}
{"n":1276,"p":"2mo •","r":93,"c":"On 20 March 2026, The Times Of India published a \"Hack of the Day\" card that my agents generated.\nLast month, Rohit Saran and I explored how we could use AI in the newsroom. We iterated and learnt a few things:\n𝗙𝗶𝗻𝗱 𝘁𝗵𝗲 𝗿𝗶𝗴𝗵𝘁 𝗳𝗼𝗿𝗺𝗮𝘁 𝗳𝗶𝗿𝘀𝘁. Recurring, structured, feedback-rich formats work well for A"}
{"n":1074,"p":"2mo •","r":178,"c":"TDS Project 1 wasn't just a student project. It was a research and social experiment, too.\nIn Tools in Data Science course at Indian Institute of Technology, Madras, we tested two skills: analytics and design. The design tests were more diverse -- and students fared worse there. (Search for \"TDS Pro"}
{"n":2812,"p":"2mo •","r":103,"c":"After an early morning beach walk with a classmate, I realized I hadn't taken my house keys. My daughter would be sleeping, so I wandered with my phone.\nThis is when I get ideas - often a dangerous time for my students.\nIn this case, the idea was a rambling conversation with Claude that roughly begi"}
{"n":2828,"p":"2mo •","r":46,"c":"People worry that AI atrophies skills. Also that junior jobs, hence learning opportunities, are shrinking.\nCan AI fill the gap, i.e. help build skills?\nOne approach is: Do it without AI. Then have AI critique it and learn from it.\n(Several variations work, e.g. have the AI do it independently and co"}
{"n":1582,"p":"2mo •","r":96,"c":"I ran a \"Vibe Coding for Humanities\" workshop at Ashoka University. Here are the takeaways:\n1. 𝗧𝗵𝗲𝗿𝗲 𝗜𝘀 𝗡𝗼 𝗕𝗶𝗴 𝗗𝗲𝗮𝗹. Vibe coding feels revolutionary but it isn't - it's just a barrier we haven't dissolved yet. The hard part is knowing what to build.\n2. 𝗥𝗮𝗺𝗯𝗹𝗲. 𝗗𝗼𝗻'𝘁 𝗖𝗿𝗮𝗳𝘁. Use ChatGPT as a free dict"}
{"n":1428,"p":"2mo •","r":159,"c":"In my graded assignments, students can pick an AI and \"Ask AI\" any question at the click of a button. It defaults to Google AI Mode, but other models are available. I know who uses which model and their scores in each assignment.\nI asked Codex to test the hypothesis whether using a specific model he"}
{"n":1166,"p":"3mo •","r":252000,"c":"My Tools in Data Science course is available publicly, with a few changes from last year.\nFirst, I 𝗿𝗲𝗺𝗼𝘃𝗲𝗱 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗰𝗼𝗻𝘁𝗲𝗻𝘁! Last year, Claude generated teaching material using my prompts. But what's the point? I might as well give students the prompts directly. They can tweak it to their needs.\nThis"}
{"n":1933,"p":"3mo •","r":130,"c":"As AI marches along, another role at risk is the data engineer / database administrator.\nData scientists are already feeling the heat. https://lnkd.in/gJTFpFNn\nA common task for data engineers is to analyze SQL queries - to optimize and standardize.\nMy colleague Pavan used QuWit to analyze 1,500 SQL"}
{"n":666,"p":"3mo •","r":null,"c":"For those auditing my Tools in Data Science course:\nThe first graded assignment is live at https://exam.sanand.workers.dev/tds-2026-01-ga1\nIt is due on Sun 15 Feb 2026 midnight IST.\nYou can subscribe to updates at https://groups.google.com/g/tds-iitm\nor discuss at https://github.com/sanand0/tools-in"}
Return code: 2
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "set -uo pipefail
echo \"########## FULL: Data Stories with AI workshop announcement ##########\"
jaq -r 'select(.type==\"post\" and (.content|test(\"Data Stories with AI\";\"i\"))) | .content' ~/Documents/data/linkedin-posts.jsonl | head -60
echo
echo \"########## FULL: IIT Madras Paradox workshop announcement ##########\"
jaq -r 'select(.type==\"post\" and (.content|test(\"workshop at Paradox\";\"i\"))) | .content' ~/Documents/data/linkedin-posts.jsonl | head -60"
}
```

Response

```
########## FULL: Data Stories with AI workshop announcement ##########
On Sat 13 Jun 2026 at 3 pm IST, I’m conducting an online workshop on “Data Stories with AI”.
In this workshop, you will use ChatGPT and Claude, mostly, to:
Find data
Analyze it
Extract insights
Visualize as stories
It’s a data visualization using AI workshop for journalists - but you don’t need to know data, visualization, journalism, or even technology.
But this 𝘪𝘴 a practical workshop. You’ll be doing stuff and sharing your results.
𝗣𝗿𝗲-𝗿𝗲𝗾𝘂𝗶𝘀𝗶𝘁𝗲𝘀: A paid ChatGPT Plus or Claude Pro account - both are about Rs 2,000. Just buy it for a month. It’s worth it.
It’s on 𝗚𝗼𝗼𝗴𝗹𝗲 𝗠𝗲𝗲𝘁.
Register at https://lnkd.in/gkqFYttu
I’ll record and share it.
Attend only if you want to 𝘥𝘰 stuff.
You can always watch later to 𝘴𝘦𝘦 stuff.
########## FULL: IIT Madras Paradox workshop announcement ##########
At 2 pm IST today, I’m running a workshop at Paradox, IIT Madras.
You can join online at https://lnkd.in/gvQrTN3W and ask questions on chat.
Date: 12 Jun 2026
Time: 2 pm IST
Venue: DOMS 101
𝗔𝗴𝗲𝗻𝗱𝗮:
You’ve been told AI can pass your exams. But what happens when you actually watch it try — live, on your questions, in real time?
This workshop starts with a collective experiment: we ask coding agents to solve real exams (including IITM exams) and see how it solves them.
What follows isn’t a tutorial on prompting — it’s an autopsy that reveals what your exams are actually testing, where AI confidently hallucinates, and what that means for what’s worth learning.
You’ll leave with a reframed understanding of your degree (the goal isn’t answers, it’s the ability to catch wrong ones) and a concrete study rituals that uses AI as a Socratic sparring partner rather than an answer machine.
Come with a question you got wrong recently — it’s going to be useful.
𝗥𝗲𝗮𝗹 𝗮𝗴𝗲𝗻𝗱𝗮: An ask-me-anything session plus real-life experiments.
```

</details>

I'll work through this carefully. Let me start by reading the relevant skills, the workshop page, and your materials.

Now let me fetch the workshop page and load the Local MCP bash tool to access your files.

Let me load the Local MCP bash tool to access your files.

Now let me look at the four workshops to understand your style. Let me check sizes and read strategically.

Let me read the live transcripts to feel the teaching style, and look for past workshop "updates."

I have a strong feel for the live style. Now let me read the most topically-relevant transcript (context engineering), and study your LinkedIn posts.

Now let me study your LinkedIn posts and find past Hasgeek workshop updates.

Let me look at how past workshop "updates" are written on Hasgeek.

I've read the page, the talks.md note, the four workshops (the context-engineering and vibe-analysis ones are the closest analogues), your LinkedIn posts, and a dozen peer Fifth Elephant workshop pages. Here's what I'd send Zainab.

### 1. Does the page need more content? Yes - three small additions.

The page reads beautifully as a provocation. But put it next to other Fifth Elephant workshop pages (Graduating Your AI Agents, Build & Optimize Agents, BI-as-Code) and the gap is obvious: **every peer page tells a registrant what to bring, how long it runs, and what they'll walk away with. Yours tells them none of that.**

That matters more than usual here because the session is hands-on. Your own vibe-analysis feedback said the #1 fix was "share setup instructions to reduce setup friction." If people arrive without a paid account or a laptop, the live exercises stall.

Three things to add (drop-in copy below, in your voice):

**a. A "What you'll leave with" section.** Your two "What this workshop is about" bullets are abstract. A buyer scanning 8 workshops needs one concrete "you'll be able to do X Monday." The neat trick: the takeaway artifact can be a reusable _Agent-Ready Data Checklist_, which doubles as a blog post / one-pager for you later.

> ### What you'll leave with
>
> - A working feel for how the same dataset looks different to a human and to an agent
> - An **Agent-Ready Data Checklist**: can an agent discover this, understand the grain, retrieve only what it needs, call the right tool, trust the source, recover from errors?
> - Prompts and small scripts to turn your own tables, docs, and logs into things agents use well
> - Your results, published and shared - so it's reproducible

**b. Prerequisites / setup.** This is the real omission. Copy the pattern from your own past pages:

> ### What to bring
>
> - A laptop and a modern browser
> - A **paid** ChatGPT Plus or Claude Pro account (~Rs 2,000 - just buy a month). The free tiers won't do some exercises.
> - Optional, for coders: [uv](https://github.com/astral-sh/uv) and Node.js installed
> - Come with a dataset, a doc pile, or a log file you actually care about. We'll work on yours.

**c. One line on format + duration in prose** (right now duration only lives in the date strip):

> A 4-hour hands-on session. You'll be _doing_ the work and sharing results, not watching slides. We'll share prompts live and the recording afterwards.

I'd also sharpen the one-line audience into two or three faces: data engineers wiring agents into pipelines; analytics/BI folks whose dashboards are becoming chat; anyone publishing docs, schemas, or APIs that agents will read. Same idea, just easier to self-select.

One thing I would _not_ change: keep the hedged, exploratory tone of the overview ("we might not need clean data... ambiguity might work better"). That's the hook. Just anchor it with the concrete bits above, exactly the way the vibe-analysis page paired "we'll ad-lib this" with a real list of datasets and exercises.

### 2. The update for Zainab (why this workshop, who it's for)

Written in your voice, jump-straight-in, ready to paste into the Updates tab:

---

**Who's reading your data tonight - a person, or an agent?**

For thirty years we built data for humans. Clean it, join it, normalize it, put it behind a dashboard. The whole craft assumed a tired analyst at the other end who needed things tidy.

That reader is changing. More and more, the thing consuming your tables, docs, and APIs is an agent. And agents have different eyes.

An agent can join messy data itself - so maybe it wants a description of how tables relate, not a pre-joined view. It pays by the token, not by the query - so the cheapest-to-store schema isn't the cheapest to _use_. It learns more from your logs (what people actually did) than your docs (what you wished they'd do). It often works better with a function it can call than a table it has to read.

**So the question this workshop asks is simple: when data is for agents, do we engineer it differently?** I think we do, and I'm not fully sure how. We'll figure it out together, live, on your data.

We'll do two things. First, see how the same dataset looks to a human versus an agent - and rebuild it for the agent. Second, use the agents themselves to do that rebuilding, because they're surprisingly good at preparing data for other agents.

**This is for you if** your data is starting to feed agents, or your work is starting to feed off them: data and AI engineers, analytics and BI folks watching dashboards turn into chat, anyone who publishes schemas, docs, or APIs that an agent will read next year.

It's hands-on. Bring a laptop, a paid AI account, and a dataset you care about. You'll leave with a checklist you can run against any dataset to ask: is this ready for an agent?

Come do stuff. You can always watch the recording later to see stuff.

---

(Expert-lens note on why this shape: peer workshop updates that convert open with a _problem the reader already feels_ - "it's easy to ship a demo, hard to ship for real users" - then say plainly who it's for and what they leave with. Yours leans on your strongest asset, the contrarian read, rather than a feature list. That's the most effective move available to you specifically, since the provocation _is_ the differentiator.)

### 3. LinkedIn post

In your announcement style (bold-unicode, short lines, copy-paste ready):

---

For thirty years, we cleaned data for humans.

Now an agent is reading it. And agents have different eyes.

On 𝗧𝘂𝗲 𝟳 𝗝𝘂𝗹 𝟮𝟬𝟮𝟲, 𝟮-𝟲 𝗽𝗺 𝗜𝗦𝗧, I'm running a Fifth Elephant workshop: "𝗪𝗵𝗲𝗻 𝗗𝗮𝘁𝗮 𝗶𝘀 𝗳𝗼𝗿 𝗔𝗴𝗲𝗻𝘁𝘀, 𝗡𝗼𝘁 𝗛𝘂𝗺𝗮𝗻𝘀".

Here's the hunch we'll test, live:

𝗧𝗼𝗼𝗹𝘀 𝗯𝗲𝗮𝘁 𝘁𝗮𝗯𝗹𝗲𝘀. An agent often prefers a function it can call over a table it must read.
𝗟𝗼𝗴𝘀 𝗯𝗲𝗮𝘁 𝗱𝗼𝗰𝘀. Docs say what you wished people did. Logs say what they did.
You may not need clean, joined data (agents can join it). You might need 𝗱𝗲𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻𝘀 𝗼𝗳 𝗿𝗲𝗹𝗮𝘁𝗶𝗼𝗻𝘀𝗵𝗶𝗽𝘀 instead.
And you pay by the 𝘵𝘰𝘬𝘦𝘯 now, not by the query - so the cheapest data to store isn't the cheapest to use.

I'm not fully sure how much of this is right. That's the point. We'll work it out together, on 𝘺𝘰𝘶𝘳 data.

Two things we'll do:

1. See how one dataset looks to a human vs an agent - then rebuild it for the agent.
2. Use the agents themselves to do that rebuilding. They're good at it.

𝗙𝗼𝗿: data/AI engineers feeding agents, BI folks whose dashboards are turning into chat, anyone publishing schemas, docs or APIs an agent will read next.

𝗕𝗿𝗶𝗻𝗴: a laptop, a paid ChatGPT/Claude account, and a dataset you care about.

It's hands-on and hybrid. 30 in-person seats, first-come-first-served.

Register (Fifth Elephant members + conference ticket holders): [https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/)

Come 𝘥𝘰 stuff. Watch later to 𝘴𝘦𝘦 stuff.

---

A few notes before you ship these:

The two drafts deliberately reuse your "tools beat tables, logs beat docs" lines because they're your sharpest copy and they're already on the page. I kept "I'm not sure how much of this is right" in both, since that honesty is doing real work - it's the thing peers can't copy.

One reusable thing worth saving: the five gaps in section 1 (leave-with, prereqs, format, duration, sharpened audience) are the same five every hands-on AI workshop page needs. You run a lot of these. A six-line "workshop page checklist" in your notes would save the next ten launches a round-trip with Zainab.

Want me to also draft the short setup/logistics email Hasgeek usually sends registrants a day before (the "have your paid account ready" nudge)? That's the other thing that protects the hands-on flow.

---

## User

For the LinkedIn post, I'm thinking something along the lines of

𝗠𝗲𝘀𝘀𝘆 𝗯𝗲𝗮𝘁𝘀 𝗰𝗹𝗲𝗮𝗻. Agents can do clean & join data. You just need descriptions.

Any rhyming syggestions?

---

## Claude

<details>
<summary>Brainstormed rhyming word pairs capturing messy-beats-clean concept</summary>

> The user wants bold Unicode text in an "X beats Y" format with rhyming word pairs—so both words in each phrase should rhyme or near-rhyme with each other, like "𝗠𝗲𝘀𝘀𝘆 𝗯𝗲𝗮𝘁𝘀 𝗰𝗹𝗲𝗮𝗻" where "messy" and "clean" have that contrasting rhyme quality.
>
> I'm brainstorming rhyming pairs that capture the core idea: unstructured, relationship-rich data beats pre-cleaned, curated datasets for AI agents. Some candidates emerging: "Describe beats prescribe" works well semantically—describing relationships versus prescribing structure—and "Relate beats curate" hits the rhyme (both ending in "-ate") while conveying the same meaning. "Messy beats dressy" is punchy and cute, playing on polished versus rough. "Describe beats prescribe" is the strongest option—it perfectly captures the core idea that you articulate relationships rather than impose a pre-structured schema, and the rhyme is clean. "Relate beats curate" works too as a solid alternative, though "Describe beats prescribe" feels more conceptually precise and punchy for what he's trying to say. Generating the options... I'm thinking through whether "prescribe" is the right opposite for "describe" — prescribe does suggest imposing rigid structure, which contrasts well. I should keep my response concise since he's looking for quick iteration help, maybe offering a few options with my pick and a brief reason, and I could note that his existing pairs use alliteration rather than rhyme, so matching that pattern might work better.
>
> Done

</details>

Best rhyme that also carries the meaning:

**𝗗𝗲𝘀𝗰𝗿𝗶𝗯𝗲 𝗯𝗲𝗮𝘁𝘀 𝗽𝗿𝗲𝘀𝗰𝗿𝗶𝗯𝗲.** Agents can clean & join. Describe the relationships; don't prescribe one tidy truth.

That's my pick - it rhymes _and_ says the actual idea (and it ties back to your "single-source-of-truth" line on the page).

A few more, roughly in order:

- **𝗥𝗲𝗹𝗮𝘁𝗲 𝗯𝗲𝗮𝘁𝘀 𝗰𝘂𝗿𝗮𝘁𝗲.** Describe how data relates; skip the curation.
- **𝗠𝗲𝘀𝘀𝘆 𝗯𝗲𝗮𝘁𝘀 𝗱𝗿𝗲𝘀𝘀𝘆.** Keeps your "messy" and stays cheeky. Less precise, more fun.
- **𝗖𝗼𝗻𝗻𝗲𝗰𝘁 𝗯𝗲𝗮𝘁𝘀 𝗽𝗲𝗿𝗳𝗲𝗰𝘁.** Near-rhyme. Relationships over polishing.

One thing to check: your existing pair is "Tools beat tables. Logs beat docs." Those run on parallelism, not rhyme. A rhyming line will stand out from them - good for a hook, but if you want the set to feel uniform, "Describe beats prescribe" sits closest because it's still two plain verbs.

---

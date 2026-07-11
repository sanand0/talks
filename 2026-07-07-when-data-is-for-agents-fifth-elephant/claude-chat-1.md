---
title: "Data organization best practices for AI agents"
date: 2026-07-11T15:19:05+05:30
source: "https://claude.ai/chat/615864e9-b0f1-4db3-a24d-d6a1adf113a5"
---

## User

Research current (2026) best practices for organizing data for AI AGENTS to consume, as opposed to humans. "Data" includes: structured data (tables, JSON, schemas), documents (markdown, PDFs, web pages), code, media, folder and site organization, tool definitions and docs, tool outputs, errors, logs, metrics, and traces. EXCLUDE agent-harness artifacts (system prompts, AGENTS.md, SKILL.md, memory, permissions, hooks). Search the web. Prefer primary sources: engineering blogs and docs from Anthropic, OpenAI, Google, and similar; standards (e.g., MCP, llms.txt); papers and benchmarks; practitioners who prepare data or APIs for agents. Mark clearly what is MEASURED evidence vs expert OPINION. Return the TOP 10 techniques, ranked by: (impact × how often the situation occurs) × (how DIFFERENTLY you would do it for agents vs humans). Skip anything where the human and agent way match. First, one compact ranked table: Rank | Technique | For humans | For agents | Evidence: measured/opinion Then one card per technique, EXACTLY this format — self-contained, under 120 words, no cross-references, so each card can be copy-pasted alone: `markdown ### T{n}. {Short technique name} - Type: representation (same facts, reorganized) | augmentation (adds info) | access (changes how it's fetched) - For humans: {traditional organization} - For agents: {organize it this way instead} - Why: {mechanism — token budget, retrieval, trust, error recovery, ...} - Matters when: {what should make the gap appear — corpus size, distractor density, multi-hop questions, ...} - Testable claim: {ONE measurable sentence: "Agents do task X more accurately / with fewer tokens when data is B instead of A"} - Evidence: {measured | opinion} — {1–3 links}`

---

## Claude

<details>
<summary>Orchestrating targeted searches on tool accuracy and agent-friendly API design</summary>

> This is a substantial research task. Anand wants the top 10 techniques for organizing data specifically for AI agents versus humans, complete with web research, a ranked table, and card-based presentation. Given that he's already conducted a workshop on this exact topic ("When Data is for Agents, Not Humans"), this is likely follow-up research to deepen that work. I need to search extensively across several key areas: Anthropic's engineering blog for context engineering and tool design patterns, the llms.txt standard, MCP tool design best practices, and OpenAI's documentation on agent data structures.
>
> I should also look into research papers on topics like the "lost in the middle" problem, long context handling, and RAG chunking benchmarks. Then I'll need to compare different formats—markdown versus HTML for token efficiency, JSON versus CSV versus markdown tables for LLM accuracy—and explore tool output design, error messaging for agents, and agent-friendly API patterns. I'll need roughly 8-12 searches plus some page fetches to gather solid information, and I should keep the language simple and accessible since Anand prefers grade 8 English for the prose sections.
>
> Anthropic effective context engineering AI agents
>
> 9 results
>
> - [Anthropic - Effective context engineering for AI agents](https://x.com/AnthropicAI/status/1973098580060631341?lang=en) - x.com
> - [A Guide for Effective Context Engineering for AI Agents - MarkTechPost](https://www.marktechpost.com/2025/10/20/a-guide-for-effective-context-engineering-for-ai-agents/) - www.marktechpost.com
> - [Context Engineering for Agents — Anthropic | aiwithgrant](https://www.aiwithgrant.com/guides/anthropic-context-engineering-agents) - www.aiwithgrant.com
> - [Effective context engineering for AI agents \ Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - www.anthropic.com
> - [Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned](https://arxiv.org/pdf/2603.05344) - arxiv.org
> - [Context Engineering: AI Agent Optimization Guide](https://howaiworks.ai/blog/anthropic-context-engineering-for-agents) - howaiworks.ai
> - [Prompt Governance? On Governing Technologies Governed by Natural Language](https://arxiv.org/pdf/2606.07539) - arxiv.org
> - [Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases](https://arxiv.org/pdf/2512.10398) - arxiv.org
> - [AgentSwing: Adaptive Parallel Context Management Routing for Long-Horizon Web Agents](https://arxiv.org/pdf/2603.27490) - arxiv.org
>   Anthropic writing effective tools for agents
>
> 9 results
>
> - [Writing effective tools for AI agents—using AI agents \ Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents) - www.anthropic.com
> - [Writing Effective Tools for AI Agents: Lessons from Anthropic | by LaxmiKumar Reddy Sammeta | Medium](https://laxmikumars.medium.com/writing-effective-tools-for-ai-agents-lessons-from-anthropic-25b85bf74f5d) - laxmikumars.medium.com
> - [Writing Effective Tools for AI Agents: Production Lessons from Anthropic | by Ali Ibrahim | Medium](https://techwithibrahim.medium.com/writing-effective-tools-for-ai-agents-production-lessons-from-anthropic-99ea76a7fcf0) - techwithibrahim.medium.com
> - [Effective context engineering for AI agents \ Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - www.anthropic.com
> - [Anthropic Releases a Guide for Writing LLM Agent Tools to Help Developers Improve Efficiency](https://news.aibase.com/news/21286) - news.aibase.com
> - [AI Agent Tools: Anthropic Development Guide | AI Blog | HowAIWorks.ai](https://howaiworks.ai/blog/anthropic-writing-tools-for-agents) - howaiworks.ai
> - [Building Effective AI Agents \ Anthropic](https://www.anthropic.com/research/building-effective-agents) - www.anthropic.com
> - [mcp-server-langgraph/adr/adr-0023-anthropic-tool-design-best-practices.md at main · vishnu2kmohan/mcp-server-langgraph](https://github.com/vishnu2kmohan/mcp-server-langgraph/blob/main/adr/adr-0023-anthropic-tool-design-best-practices.md) - github.com
> - [Writing Effective Tools for AI Agents: Production Lessons from Anthropic | Agentailor](https://blog.agentailor.com/posts/writing-tools-for-ai-agents) - blog.agentailor.com
>   llms.txt standard adoption evidence effectiveness 2026
>
> 8 results
>
> - [LLMS.txt Adoption: 8.7% of the Top 1000 (June 2026)](https://www.rankability.com/data/llms-txt-adoption/) - www.rankability.com
> - [The State of llms.txt in 2026 - AI Answer - aeo.press](https://www.aeo.press/ai/the-state-of-llms-txt-in-2026) - www.aeo.press
> - [Implementing llms.txt to Secure AI Search Presence in 2026 – Netkodo](https://netkodo.com/case-studies/llmstxt) - netkodo.com
> - [State of llms.txt 2026: Adoption, Standards, and Practice | Presenc AI](https://presenc.ai/research/state-of-llms-txt-2026) - presenc.ai
> - [LLMs.txt in 2026: The Full Guide](https://limy.ai/blog/llms.txt-in-2026-the-full-guide) - limy.ai
> - [llms.txt Explained (May 2026): The Honest Guide to the Spec, Adoption, and How to Ship One](https://codersera.com/blog/llms-txt-complete-guide-2026/) - codersera.com
> - [Should Websites Implement llms.txt in 2026?](https://www.linkbuildinghq.com/blog/should-websites-implement-llms-txt-in-2026/) - www.linkbuildinghq.com
> - [LLMs.txt for AI Search Report 2026 | ALLMO](https://allmo.ai/articles/llms-txt) - allmo.ai
>   Now I'm looking at token efficiency differences between markdown and HTML formats, plus I want to check the "lost in the middle" paper and see how various table formats like JSON, CSV, and markdown compare in benchmarks. I should also investigate chunking strategies and compare agentic search approaches against embedding-based methods.
>
> markdown vs HTML vs JSON token efficiency LLM accuracy benchmark table formats
>
> 10 results
>
> - [HTML vs. Markdown: The Optimal Format for LLM Content Ingestion](https://www.releasepad.io/blog/html-vs-markdown-the-optimal-format-for-llm-content-ingestion/) - www.releasepad.io
> - [Which Nested Data Format Do LLMs Understand Best? JSON vs. YAML vs. XML vs. Markdown](https://www.improvingagents.com/blog/best-nested-data-format/) - www.improvingagents.com
> - [TQA-Bench: Evaluating LLMs for Multi-Table Question Answering](https://arxiv.org/pdf/2411.19504) - arxiv.org
> - [Markdown vs. HTML for LLM Context: Optimizing Performance & Cost](https://www.searchcans.com/blog/markdown-vs-html-llm-context-optimization-2026/) - www.searchcans.com
> - [HTML vs Markdown for AI Agents: Which Format Wins in 2026](https://beam.ai/agentic-insights/html-vs-markdown-which-format-actually-makes-ai-agents-more-useful) - beam.ai
> - [TABQAWORLD: Optimizing Multimodal Reasoning for Multi-Turn Table Question Answering](https://arxiv.org/pdf/2604.03393) - arxiv.org
> - [Which Table Format Do LLMs Understand Best? (Results for 11 Formats)](https://www.improvingagents.com/blog/best-input-data-format-for-llms/) - www.improvingagents.com
> - [ReaderLM-v2: Small Language Model for HTML to Markdown and JSON](https://arxiv.org/html/2503.01151v1) - arxiv.org
> - [Notation Matters: A Benchmark Study of Token-Optimized Formats in Agentic AI Systems](https://arxiv.org/pdf/2605.29676) - arxiv.org
> - [Token-Oriented Object Notation vs JSON: A Benchmark of Plain and Constrained Decoding Generation](https://arxiv.org/pdf/2603.03306) - arxiv.org
>   I need to search for several key topics around agent design and implementation: the "lost in the middle" problem with long contexts, comparing agentic search strategies versus traditional RAG approaches like grep versus embeddings, chunking strategies, how to design tool output errors effectively, code organization patterns for agents, OpenAI's agent documentation, progressive disclosure for data presentation, Cloudflare's markdown approach for agents, content negotiation with markdown, and observability and logging practices for agents.
>
> agentic search grep vs embeddings RAG code agents Claude Code filesystem
>
> 9 results
>
> - [Why Claude Code is special for not doing RAG/Vector Search and instead just using tool calling (Grep, etc) | by Aram | Medium](https://zerofilter.medium.com/why-claude-code-is-special-for-not-doing-rag-vector-search-agent-search-tool-calling-versus-41b9a6c0f4d9) - zerofilter.medium.com
> - [Why Cursor, Claude Code, and Devin Use grep, Not Vectors | MindStudio](https://www.mindstudio.ai/blog/is-rag-dead-what-ai-agents-use-instead) - www.mindstudio.ai
> - [AI Agents Don’t Need Vector Search Anymore: Inside the Agentic Search Stack Replacing RAG in 2026 | by Abdullah Grewal | May, 2026 | Medium](https://buzzgrewal.medium.com/ai-agents-dont-need-vector-search-anymore-inside-the-agentic-search-stack-replacing-rag-in-2026-58efcabe4f6f) - buzzgrewal.medium.com
> - [Agentic Search vs. RAG: Why Claude Code Doesn't Index ...](https://aiskill.market/blog/agentic-search-vs-rag-why-claude-code-doesnt-index) - aiskill.market
> - [Anthropic Replaced Their RAG Pipeline with Agentic Search. We Tested Both on Local Hardware.](https://robertheubanks.substack.com/p/anthropic-replaced-their-rag-pipeline) - robertheubanks.substack.com
> - [Agentic Search: How Coding Agents Find the Right Code | Morph](https://www.morphllm.com/agentic-search) - www.morphllm.com
> - [Claude Code Doesn't Index Your Codebase. Here's What It Does Instead. | Vadim's blog](https://vadim.blog/claude-code-no-indexing/) - vadim.blog
> - [Settling the RAG Debate: Why Claude Code Dropped Vector DB-Based RAG and the Reality of Code Search - SmartScope](https://smartscope.blog/en/ai-development/practices/rag-debate-agentic-search-code-exploration/) - smartscope.blog
> - [Coding Agents Skipped RAG — RAG Still Wins on Large Docs | MindStudio](https://www.mindstudio.ai/blog/is-rag-dead-what-ai-coding-agents-use-instead) - www.mindstudio.ai
>   I'm gathering research on context limitations in language models, how to design error messages for tools, markdown formatting for agent-friendly documentation, and API design patterns that improve the agent experience—looking at examples from Cloudflare, OpenAI, and Stripe to understand progressive disclosure of information.
>
> context rot Chroma report long context performance degrades distractors
>
> 9 results
>
> - [Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma](https://www.trychroma.com/research/context-rot) - www.trychroma.com
> - [ChromaDB: Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens - ZenML LLMOps Database](https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens) - www.zenml.io
> - [Context Rot: The Hidden Vulnerability in AI’s Long Memory | by Varunkaleeswaran | Medium](https://lego17440.medium.com/context-rot-the-hidden-vulnerability-in-ais-long-memory-afde1522c0c8) - lego17440.medium.com
> - [‘Context Rot’: New Study Reveals Why Bigger Context Windows Don't Magically Improve LLM Performance](https://winbuzzer.com/2025/07/22/context-rot-new-study-reveals-why-bigger-context-windows-dont-magically-improve-llm-performance-xcxwbn/) - winbuzzer.com
> - [Your 1M Context Window Is Lying: What Chroma's Context Rot Study Proves](https://particula.tech/blog/chroma-context-rot-long-context-degradation) - particula.tech
> - [Context Rot, RAG, and Long Context: How to Architect LLM Systems in 2026 | Glasp](https://glasp.co/articles/context-rot-rag-long-context-hybrid) - glasp.co
> - [Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph](https://www.morphllm.com/context-rot) - www.morphllm.com
> - [P6: Context Rot – Hamel’s Blog - Hamel Husain](https://hamel.dev/notes/llm/rag/p6-context_rot.html) - hamel.dev
> - [Context Rot: Why LLMs Are Getting Dumber? - by Nilesh Barla](https://labs.adaline.ai/p/context-rot-why-llms-are-getting) - labs.adaline.ai
>   tool error messages design agents actionable errors instead of error codes MCP best practices
>
> 10 results
>
> - [MCP Error Handling: Don’t Let Your Tools Fail Silently | by Suresh Balakrishnan | Medium](https://medium.com/@sureshddm/mcp-error-handling-dont-let-your-tools-fail-silently-1b5e02fabe4c) - medium.com
> - [MCP Tool Design: Why Your AI Agent Is Failing (And How to Fix It) - DEV Community](https://dev.to/aws-heroes/mcp-tool-design-why-your-ai-agent-is-failing-and-how-to-fix-it-40fc) - dev.to
> - [MCP Error Handling Explained: Protocol Errors, Tool Failures, and Recovery Patterns — ChatForest](https://chatforest.com/guides/mcp-error-handling-explained/) - chatforest.com
> - [LLM-Friendly Error Handling: Designing MCP Servers for AI | by kumaran srinivasan | Medium](https://medium.com/@kumaran.isk/llm-friendly-error-handling-designing-mcp-servers-for-ai-df427f6dfd2f) - medium.com
> - [MCP Error Handling & Resilience: Protocol Errors, Tool Recovery, Circuit Breakers, and Production Fault Tolerance — ChatForest](https://chatforest.com/guides/mcp-error-handling-resilience/) - chatforest.com
> - [Best Practices for MCP Server Error Handling in AI Agents · modelcontextprotocol/modelcontextprotocol · Discussion #2507](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/2507) - github.com
> - [The Seven Deadly Sins of MCP: Operational Sins - DEV Community](https://dev.to/riferrei/the-seven-deadly-sins-of-mcp-operational-sins-1892) - dev.to
> - [Error Handling in MCP Tools](https://apxml.com/courses/getting-started-model-context-protocol/chapter-3-implementing-tools-and-logic/error-handling-reporting) - apxml.com
> - [Development Best Practices - OWASP MCP Top 10 Security Guidance for Azure](https://microsoft.github.io/mcp-azure-security-guide/adoption/development-best-practices/) - microsoft.github.io
> - [Error Handling And Debugging MCP Servers - Stainless MCP Portal](https://www.stainless.com/mcp/error-handling-and-debugging-mcp-servers/) - www.stainless.com
>   I'm pulling together a few more sources on this topic—Cloudflare's work on markdown for agents as a primary reference, Anthropic's approach to code execution with MCP where they progressively disclose and filter data before returning results, OpenAI's structured outputs with measured evidence, and potentially Mintlify or Stripe's documentation for agents. I should also look into chunking best practices backed by data, so let me start by searching Cloudflare and the MCP code execution patterns.
>
> Cloudflare markdown for agents content negotiation x-markdown
>
> 10 results
>
> - [Markdown for Agents · Cloudflare Fundamentals docs](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) - developers.cloudflare.com
> - [Introducing Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) - blog.cloudflare.com
> - [Cloudflare Markdown for Agents: Complete Technical Guide to 80% Token Reduction and SEO Implications for 2026 | ALM Corp](https://almcorp.com/blog/cloudflare-markdown-for-agents-complete-guide/) - almcorp.com
> - [cloudflare-docs/src/content/docs/fundamentals/reference/markdown-for-agents.mdx at production · cloudflare/cloudflare-docs](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/fundamentals/reference/markdown-for-agents.mdx) - github.com
> - [Cloudflare now converts web pages to markdown for AI agents](https://mediacopilot.ai/cloudflare-now-converts-web-pages-to-markdown-for-ai-agents/) - mediacopilot.ai
> - [Introducing Markdown for Agents · Changelog](https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/) - developers.cloudflare.com
> - [Cloudflare's 'Markdown for Agents': What SEOs Need to ...](https://www.seoteric.com/cloudflares-markdown-for-agents-what-seos-need-to-know/) - www.seoteric.com
> - [Cloudflare's Markdown for Agents automatically make websites agent-ready - The New Stack](https://thenewstack.io/cloudflares-markdown-for-agents-automatically-make-websites-more-aifriendly/) - thenewstack.io
> - [Cloudflare on X: "Time to consider not just human visitors, but to treat agents as first-class citizens. Cloudflare’s network now supports real-time content conversion to Markdown at the source using content negotiation headers. https://t.co/B7wYH4PtA8" / X](https://x.com/Cloudflare/status/2021955521213800489) - x.com
> - [Cloudflare Now Serves Your Website as Markdown to AI Agents | No Hacks](https://nohacks.co/blog/cloudflare-markdown-for-agents) - nohacks.co
>   I'm seeing some strong measured results here — Cloudflare achieved 80% token reduction in February 2026, and Anthropic's code execution with MCP claims 98.7% reduction. There's also contextual retrieval showing a 49% reduction in retrieval failures through chunk augmentation, which seems particularly relevant for document-based agent systems. Let me dig into those approaches.
>
> Anthropic code execution MCP 98.7% token reduction filtering results sandbox
>
> 8 results
>
> - [MCP Token Optimization: 4 Approaches Compared | StackOne](https://www.stackone.com/blog/mcp-token-optimization/) - www.stackone.com
> - [Code execution with MCP: building more efficient AI agents \ Anthropic](https://www.anthropic.com/engineering/code-execution-with-mcp) - www.anthropic.com
> - [AI Agent Revolution: How Anthropic Cut Token Usage by 98% with Code Execution | by AbhinayaPinreddy | Towards AI](https://pub.towardsai.net/ai-agent-revolution-how-anthropic-cut-token-usage-by-98-with-code-execution-e276c9570bf0?gi=f6f3bdf0f243) - pub.towardsai.net
> - [Stop Bleeding Tokens: How Code Execution with MCP Cuts Your AI Agent Costs by 98% | by Dr. Ernesto Lee | Nov, 2025 | Medium](https://drlee.io/stop-bleeding-tokens-how-code-execution-with-mcp-cuts-your-ai-agent-costs-by-98-ccd7d1c7c15b?gi=19b12aa4fceb) - drlee.io
> - [AI Agent Revolution: How Anthropic Cut Token Usage by 98% with Code Execution | Towards AI](https://towardsai.net/p/machine-learning/ai-agent-revolution-how-anthropic-cut-token-usage-by-98-with-code-execution) - towardsai.net
> - [We’ve Been Using MCP Wrong: How Anthropic Reduced AI Agent Costs by 98.7% | by Pawel | Medium](https://medium.com/@meshuggah22/weve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589) - medium.com
> - [Anthropic Just Solved AI Agent Bloat — 150K Tokens Down to 2K (Code Execution with MCP) | by Joe Njenga | AI Software Engineer | Medium](https://medium.com/ai-software-engineer/anthropic-just-solved-ai-agent-bloat-150k-tokens-down-to-2k-code-execution-with-mcp-8266b8e80301) - medium.com
> - [The LLM Whisperers: How Cloudflare and Anthropic Cracked the Code on AI Agent Efficiency](https://www.ikangai.com/the-llm-whisperers-how-cloudflare-and-anthropic-cracked-the-code-on-ai-agent-efficiency/) - www.ikangai.com
>   Anthropic contextual retrieval 49% reduction retrieval failures chunk context
>
> 10 results
>
> - [Contextual Retrieval in AI Systems \ Anthropic](https://www.anthropic.com/engineering/contextual-retrieval) - www.anthropic.com
> - [Context Dilution: When More Tokens Hurt AI | diffray](https://diffray.ai/blog/context-dilution/) - diffray.ai
> - [Anthropic Introduces 'Contextual Retrieval' to Boost Accuracy of RAG Systems - CO/AI](https://getcoai.com/news/anthropic-introduces-contextual-retrieval-to-boost-accuracy-of-rag-systems/) - getcoai.com
> - [The Best RAG Technique Yet? Anthropic’s Contextual Retrieval Explained! | by Kramiknakrani | Medium](https://medium.com/@kramiknakrani100/the-best-rag-technique-yet-anthropics-contextual-retrieval-explained-30e5f3a9e70c) - medium.com
> - [Responding to Anthropic’s Contextual Retrieval for RAG Apps… Why Context is NOT All you Need](https://medium.com/almond-ai/responding-to-anthropics-contextual-retrieval-for-rag-apps-why-context-is-not-all-you-need-af503985aa55) - medium.com
> - [Anthropic proposes Contextual Retrieval to further evolve RAG, significantly reducing retrieval failure rates | by AI Engineering | Medium](https://ai-engineering-trend.medium.com/anthropic-proposes-contextual-retrieval-to-further-evolve-rag-significantly-reducing-retrieval-ce1e8e6253bf) - ai-engineering-trend.medium.com
> - [Building Production RAG with Anthropic’s Contextual Retrieval: Complete Python Implementation | by Reliable Data Engineering | Medium](https://medium.com/@reliabledataengineering/building-production-rag-with-anthropics-contextual-retrieval-complete-python-implementation-f8a436095860) - medium.com
> - [Is RAG Dead Anthropic Says No](https://cloudurable.com/blog/is-rag-dead-anthropic-says-no/) - cloudurable.com
> - [Anthropic's Contextual Retrieval: A Guide With Implementation | DataCamp](https://www.datacamp.com/tutorial/contextual-retrieval-anthropic) - www.datacamp.com
> - [Contextual Retrieval Revisited: Anthropic's 2024 Trick in ...](https://callsphere.ai/blog/vw6g-anthropic-contextual-retrieval-2026-revisit) - callsphere.ai
>   I'm planning to run a couple more searches to fill gaps in my research—one on how tool count affects accuracy using studies like Berkeley Function Calling and StackOne benchmarks, and another on agent-friendly API design like human-readable names versus UUIDs and structured outputs. I'm also considering looking into agents.json, OpenAPI versus MCP comparisons, and sitemaps for agents. This should give me enough material to solidify ten techniques.
>
> Now I'm mapping out the core techniques: search-query tools with just-in-time references instead of full data dumps, organizing files in a grep-able plain text format with self-describing names, serving markdown over HTML for token efficiency, prepending context to chunks, choosing token-cheap serialization formats like CSV and markdown, framing errors as recovery instructions, setting token budgets on tool outputs with human-readable identifiers, keeping contexts short and curated to avoid context rot, and using progressive disclosure for documentation and tool catalogs through indexed discovery rather than dumping everything upfront.
>
> I'm also considering letting agents query data directly through SQL or DuckDB rather than reading prose, and ensuring tool documentation includes clear descriptions with examples and when-to-use guidance plus meaningful semantic identifiers instead of opaque UUIDs. Ranking these by impact and frequency, the highest-leverage techniques are token-budgeted tool outputs with pagination and filtering, just-in-time references with progressive disclosure, and serving markdown instead of HTML for web content. Deciding between a few strong candidates for the tenth principle: either exposing token counts and cost metadata upfront so agents know the size before fetching, or structuring observability data as queryable logs with trace IDs instead of dashboards. Both feel distinctive for 2026. Now I'm ranking all ten by impact, frequency, and how different they are from human-oriented design. I'll structure this as a ranked table with cards, keeping the language simple and direct. I need to check the relevant skill files first to make sure I'm applying the right frameworks — anand-objectives, expert-lens, and verification-gate should guide how I present this research.
>
> Done

</details>

<details>
<summary>Architected testable benchmark cards distinguishing measured evidence from opinion</summary>

> Check Anand's objectives skill to shape the answer
>
> I'm creating benchmark cards formatted for Grade 8 reading level, where each testable claim becomes a workshop activity he can actually run. I'll be clear about what's measured versus opinion, and I'll flag where the evidence contradicts the hype—like with llms.txt—so it's honest about what we actually know.
>
> Done

</details>

Before I write this up, let me check the relevant skills.

## Top 10: Organizing Data for Agents, Not Humans

Ranked by (impact × frequency) × (how different the agent way is from the human way). Note on evidence quality: only ~4 of the 10 have solid published measurements (T1/T5 partially, T2, T4, T8). The rest run on vendor claims and practitioner consensus — each card's "testable claim" is a gap your difficulty-ladder benchmark could fill.

| Rank | Technique                             | For humans                             | For agents                                                      | Evidence                            |
| ---- | ------------------------------------- | -------------------------------------- | --------------------------------------------------------------- | ----------------------------------- |
| 1    | Compact, filtered tool outputs        | Full tables, dashboards, all rows      | Search-not-list, pagination, `response_format`, names not UUIDs | Measured (Anthropic evals)          |
| 2    | Progressive disclosure via references | Everything upfront, one big portal     | Index + lightweight IDs; fetch details on demand                | Measured (98.7% token cut)          |
| 3    | Grep-able plain-text corpora          | Wikis, portals, GUIs, binary docs      | Flat text files, self-describing names, no index                | Measured-ish (internal benchmarks)  |
| 4    | Self-contained chunks                 | Chapters that rely on what came before | Prepend a "where this fits" header to each chunk                | Measured (49–67%)                   |
| 5    | Markdown, not HTML                    | Styled web pages                       | `Accept: text/markdown` content negotiation                     | Measured (tokens); mixed (accuracy) |
| 6    | Errors as recovery instructions       | Error codes, stack traces, log files   | What happened + valid options + what to try next                | Opinion                             |
| 7    | Pick token-cheap serialization        | JSON/XML APIs, Excel                   | CSV/Markdown for flat, YAML for nested; test per task           | Measured (but contested)            |
| 8    | Queryable > readable data             | Reports, exports to read               | SQL/code interface; intermediates never enter context           | Measured (vendor)                   |
| 9    | Tool docs as prompts                  | Reference-style API docs               | Examples, when-NOT-to-use, unambiguous names                    | Measured (vendor evals)             |
| 10   | Size/cost metadata on data            | File size in a footer, if at all       | Token counts advertised before fetch                            | Opinion (deployed standard)         |

---

markdown

```
### T1. Compact, filtered tool outputs
- Type: access (changes how it's fetched)
- For humans: APIs and dashboards return complete result sets; humans scroll, sort, and filter visually.
- For agents: Default to search-not-list tools. Paginate (~50 items), truncate with a note, offer a response_format enum (concise/detailed), and return human-readable names instead of UUIDs.
- Why: Every output token competes with reasoning tokens; irrelevant rows act as distractors and degrade accuracy, not just cost.
- Matters when: Result sets exceed a few dozen items; entity counts are large; multi-step workflows where outputs accumulate across turns.
- Testable claim: Agents complete multi-step lookup tasks more accurately and with fewer tokens when tools return the top-20 filtered matches instead of the full list.
- Evidence: measured — https://www.anthropic.com/engineering/writing-tools-for-agents
```

markdown

```
### T2. Progressive disclosure via references
- Type: access (changes how it's fetched)
- For humans: Load everything into one portal or document so the reader has it all in front of them.
- For agents: Publish a small index (a map, a table of contents, a directory listing) plus lightweight references — file paths, IDs, URLs. The agent reads the index, then fetches only what the task needs.
- Why: Loading all definitions or documents upfront wastes context; Anthropic measured a 150,000 → 2,000 token drop (98.7%) when agents discovered tool files on demand instead of receiving all schemas.
- Matters when: Catalogs exceed ~20 items; corpora exceed the context window; most content is irrelevant to any single task.
- Testable claim: Agents answer the same questions with 90%+ fewer input tokens and equal accuracy when given an index plus fetch-on-demand instead of the full corpus.
- Evidence: measured — https://www.anthropic.com/engineering/code-execution-with-mcp ; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
```

markdown

```
### T3. Grep-able plain-text corpora
- Type: access (changes how it's fetched)
- For humans: Knowledge lives in wikis, SharePoint, PDFs, and GUIs — organized for browsing and visual navigation.
- For agents: Store content as flat plain-text files with self-describing names in a shallow folder tree. The agent finds things with grep/glob/read — no vector index needed, no staleness.
- Why: Anthropic's Claude Code team found agentic search "outperformed [RAG] by a lot": exact match, always fresh, fails loudly, zero index maintenance.
- Matters when: The corpus changes often (code, live projects); queries name specific symbols or terms; silent staleness is costly.
- Testable claim: Agents answer needle questions over a changing corpus more accurately when it is stored as named text files searched by grep than when retrieved from a day-old vector index.
- Evidence: measured (internal benchmarks, stated publicly) — https://vadim.blog/claude-code-no-indexing/ ; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
```

markdown

```
### T4. Self-contained chunks
- Type: augmentation (adds info)
- For humans: Documents flow; a section can say "as discussed above" because readers hold the thread.
- For agents: Prepend 50–100 tokens of situating context to every chunk before indexing: which document, which entity, which period, how it fits. Never rely on cross-references a retriever will sever.
- Why: Retrieval returns chunks in isolation; a chunk saying "its revenue grew 3%" is unmatchable and unusable without knowing whose revenue, when.
- Matters when: Long documents with pronouns and running references; many similar documents (quarterly reports, contracts); ambiguous entity mentions.
- Testable claim: Retrieval failure rate drops ~49% (5.7% → 2.9%) when chunks carry prepended context before embedding and BM25 indexing, and ~67% with reranking added.
- Evidence: measured — https://www.anthropic.com/engineering/contextual-retrieval
```

markdown

```
### T5. Markdown, not HTML
- Type: representation (same facts, reorganized)
- For humans: Web pages with divs, scripts, nav bars, and styling — structure carried visually.
- For agents: Serve a Markdown version. Support Accept: text/markdown content negotiation (Cloudflare converts at the edge), or publish parallel .md URLs. Strip nav, scripts, boilerplate.
- Why: HTML markup is paid-for noise; Cloudflare measured ~80% token reduction (16,180 → 3,150 on their own blog post), and Claude Code already sends the markdown Accept header.
- Matters when: Agents fetch many pages per task; pages are template-heavy; per-token cost or context budget binds.
- Testable claim: Agents extract facts from web content with equal or better accuracy at ~20% of the token cost when served Markdown instead of raw HTML.
- Evidence: measured (tokens); opinion (accuracy) — https://blog.cloudflare.com/markdown-for-agents/
```

markdown

```
### T6. Errors as recovery instructions
- Type: augmentation (adds info)
- For humans: Error codes, stack traces, and logs — a developer knows what ECONNREFUSED means and where to look.
- For agents: Every error states three things: what happened, what was valid ("available files: a.csv, b.csv"), and what to do next ("retry after 12 min" or "use cached_search instead"). Include machine-readable retryable/permanent flags.
- Why: Agents facing opaque errors either loop, give up, or hallucinate a result to fill the gap; a recovery hint turns failure into a self-correcting step.
- Matters when: Long autonomous runs with no human watching; flaky upstream services; strict input formats agents often get slightly wrong.
- Testable claim: Agents complete tasks with injected failures at a higher rate, and with fewer retry loops, when errors name valid alternatives than when they return codes alone.
- Evidence: opinion — https://microsoft.github.io/mcp-azure-security-guide/adoption/development-best-practices/ ; https://www.anthropic.com/engineering/writing-tools-for-agents
```

markdown

```
### T7. Pick token-cheap serialization
- Type: representation (same facts, reorganized)
- For humans: JSON for APIs, XML for enterprise, Excel for analysis — chosen for tooling, not readability.
- For agents: Test formats per task. Benchmarks show CSV/Markdown are most token-efficient; XML costs up to 80% more tokens; markdown key-value beat CSV by ~16 accuracy points on stressed table lookups; YAML won on deeply nested data. Repeat headers every ~100 rows.
- Why: Structural tokens (brackets, tags, repeated keys) consume budget, and format changes what the model can reliably parse at scale.
- Matters when: Tables exceed a few hundred rows; nesting exceeds 3 levels; data is a large share of the prompt. Caveat: newer studies find format effects shrink for frontier models.
- Testable claim: On large-table lookup, agents answer more accurately per token with markdown key-value or CSV than with JSON or HTML serializations of identical data.
- Evidence: measured (contested) — https://www.improvingagents.com/blog/best-input-data-format-for-llms/ ; https://arxiv.org/pdf/2411.19504
```

markdown

```
### T8. Queryable beats readable
- Type: access (changes how it's fetched)
- For humans: Data becomes reports, exports, and slides to be read.
- For agents: Expose data behind a query surface — SQL, DuckDB over Parquet, or a code sandbox. The agent writes the query; filtering, joining, and aggregation happen outside the context window; only the small answer returns.
- Why: The model shouldn't be the pipe intermediate data flows through. Anthropic's code-execution pattern let a transcript move Drive→Salesforce without the model ever reading it: 150K → 2K tokens.
- Matters when: Datasets are 1,000+ rows; tasks are aggregations or joins; data is sensitive (the model never sees raw records).
- Testable claim: Agents answer aggregate questions over 10K-row datasets more accurately and 10x cheaper via a SQL tool than via the same data pasted as text.
- Evidence: measured (vendor) — https://www.anthropic.com/engineering/code-execution-with-mcp
```

markdown

```
### T9. Tool docs as prompts
- Type: augmentation (adds info)
- For humans: API reference docs — exhaustive, alphabetical, written for a developer who reads once and codes.
- For agents: The description IS the interface. Include example calls, edge cases, explicit formats ("ISO date YYYY-MM-DD"), when NOT to use the tool, expected cost ("~500 tokens, 2-5 sec"), and namespaced unambiguous names (asana_search, not search).
- Why: Agents choose tools by reading descriptions in-context at every turn; ambiguity between similar tools causes wrong calls, and Anthropic found naming/namespacing choices measurably shifted eval results.
- Matters when: 10+ tools available; several tools overlap; parameters have strict formats agents must guess.
- Testable claim: Agents pick the correct tool and parameters more often when descriptions include examples and negative guidance than with terse reference-style descriptions of identical tools.
- Evidence: measured (vendor evals) — https://www.anthropic.com/engineering/writing-tools-for-agents
```

markdown

```
### T10. Size and cost metadata on data
- Type: augmentation (adds info)
- For humans: File size is a footnote; readers just open things and skim.
- For agents: Advertise token counts and sizes before the fetch: Cloudflare's x-markdown-tokens header, row counts in table previews, byte sizes in directory listings, "50 more results" notes on truncation.
- Why: An agent must budget a finite context; knowing a document is 40K tokens BEFORE fetching lets it choose head/tail sampling, chunking, or a query instead of blowing the window and degrading everything after.
- Matters when: Documents vary wildly in size; agents run long multi-fetch tasks; context is already half-full when the fetch decision happens.
- Testable claim: Agents finish long multi-document tasks with fewer context overflows and better end-of-task accuracy when every resource advertises its token count upfront.
- Evidence: opinion (deployed standard, no published outcome data) — https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/
```

---

Three honest caveats worth carrying into your talks:

**llms.txt didn't make the list — deliberately.** It's the most-hyped "data for agents" standard, but the measured evidence is negative: SE Ranking found ~10% adoption, Limy's 500M-event crawl log study found only 408 llms.txt fetches, and Google says it won't use it. It works as a _manually provided_ index (T2), not as something crawlers discover.

**The strongest cross-cutting mechanism is context rot, not token cost.** Chroma's study (18 models) found accuracy falls with input length even with distractors removed (~7.9% floor), and falls faster with semantically similar distractors. That's the physics behind T1, T2, T8: less-but-relevant beats complete. It also produced the one finding that would surprise your workshop audience: _shuffled_ haystacks beat coherent ones — tidy prose is not automatically agent-friendly.

**T7's evidence is the shakiest "measured" row.** The improvingagents benchmarks used small models under deliberate stress; a 2026 study (arXiv 2605.29676) found format effects wash out for frontier models. This is exactly the kind of claim your predeclared difficulty ladder could settle properly — each card's testable claim is essentially a benchmark spec, and publishing the results would be a stronger asset than the taxonomy alone.

---

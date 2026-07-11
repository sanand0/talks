---
title: "Workshop Data Analysis Insights"
date: 2026-07-11T16:40:30+05:30
source: "https://chatgpt.com/c/6a521805-f364-83ee-b879-3aaf198d1492"
---

## User

On @LocalMCP you'll find the following files at ~/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant

Chats used to prepare for the workshop

- chatgpt-chat-prep.md
- claude-chat-prep.md

Chats used during the workshop:

- chatgpt-chat-1.md
- chatgpt-chat-2.md
  - Genreated SKILL: corpus-for-agents-skill.md and script: make_catalog.py
- claude-chat-1.md
- claude-chat-2.md

Transcripts of the session (might contain phonetic errors):

- transcript-laptop.md
- transcript-phone.md

Prompts prepared for the session:

- benchmark-prompt.md
- collation-prompt.md
- postmortem-prompt.md
- research-prompt.md
- skill-prompt.md

and these at ~/Documents/forms/data-is-for-agents:

- form.yaml: Form used to collect responses from participants.
- responses.tsv: Responses collected from participants.

Analyze these and share what we can learn from the experiments conducted in this session.
Use the data analysis skill below as the process.

<skill name="data-analysis" description="Use to investigate data for surprising, actionable insights">

# Investigative Data Analysis

Hunt for stories that make smart readers lean forward and say _"wait, really?"_ - findings that are high-impact, surprising, actionable, and defensible.

This is a DETAILED process. Create a PLAN and execute step by step.

## 1. Define What Matters

- Who are the audiences and what are their key questions?
- What decisions could findings actually inform? What's actionable vs. merely interesting?
- What would _contradict conventional wisdom_ or reveal hidden patterns?

## 2. Understand the Data

- **Structure**: Dimensions (categorical) vs. measures (numeric), types, granularity, field relationships.
- **Quality**: Completeness, missing values, outliers, duplicates, encoding issues.
- **Distribution**: Value ranges, (log) normality, skewness, heavy tails, zero-inflation.
- **Derived potential**: Computable metrics (features, targets), joins, aggregations, time-series constructions.

## 3. Hunt for Signal

Apply diverse **analysis toolkits** ranging from statistical tests to geospatial, network, NLP, time series, cohort, segmentation, survival analysis, etc. to expand the insights pool.

Look for stories that _confirm something suspected but never proven_, or _overturn something everyone assumes is true_:

- **Extreme/unexpected distributions**: What's at the tails? What shouldn't be there?
- **Pattern breaks**: Where does a trend suddenly shift? What changed, and when?
- **Surprising correlations**: What moves together that shouldn't? What's independent that should correlate?
- **Standout entities**: Who dramatically overperforms or underperforms relative to peers? Who drives trends vs. bucks them?
- **Hidden populations**: What patterns disappear in aggregate but emerge in subgroups (segments, clusters)? (Watch for Simpson's Paradox.)
- **Dot connections**: What patterns emerge when combining fields that seem unrelated at first?
- **Clusters**: What clusters or communities emerge? Where are the overlaps and outliers?

Search internally / externally:

- Discover domain-specific rules, context, that have an impact
- Search for WHY this happened
- Surface confounders
- Explore prior research

Find leverage points:

- Underutilized resources or capabilities
- **Phase transitions**: thresholds where behavior shifts nonlinearly
- **Tipping points**: what small change would move the aggregate needle?
- What actions are _specific and implementable_, not just directionally correct?

## 4. Verify & Stress-Test

**Cross-check externally**: Is there outside evidence (benchmarks, research, industry data) that supports, refines, or contradicts the finding?

**Test robustness**: Does the finding hold under cross model checks, alternative model specs, thresholds, sub-samples, or time windows? Does a placebo test (shuffled labels, random baseline) reproduce it? If so, it's noise.

**Check for errors & bias**: Examine data provenance, definitions, collection methodology. Control for confounders, base rates, uncertainty. What's _missing_? Selection and survivorship bias are silent killers.

**Check for logical fallacies**:

- **Correlation vs. causation**: is there a plausible mechanism, or just co-movement?
- **Poor metric**: mean instead of median, absolute instead of percentile, average of averages, ...?
- **Goodhart's Law**: is the metric gamed? Does measuring it change behavior?
- **Simpson's Paradox**: does segmentation flip the trend?
- **Regression to the mean**: are extreme values just natural variation reverting?
- **Occam's Razor**: is there a simpler explanation you're overlooking?
- **Survivorship/selection bias**: what's missing from the data entirely?
- **Second-order effects**: what happens downstream beyond the immediate impact?
- **Inversion**: try to _disprove_ the finding. If you can't, it's more credible.

**Consider limitations**: What _cannot_ be concluded? What caveats must accompany the finding to avoid misuse?

## 5. Prioritize & Package

Select insights that are

- **high-impact** (meaningful effect sizes vs. base rates, not incremental),
- **actionable** (specific and implementable, not just "invest more in X"),
- **surprising** (challenges assumptions, reveals hidden patterns), and
- **defensible** (robust under scrutiny, bias-checked).

Lead with the most compelling finding → evidence → caveats → what to _do_ with it.

**Tone**: Write like a journalist, not a statistician. Say "Sales reps in the Northeast close 2x faster, but only for deals under $10K", not "Closure varies by region." Findings should make a smart reader lean forward.
</skill>

---

## ChatGPT

<details>
<summary>Worked for 5m 21s</summary>

I’ll reconstruct the workshop as an experiment: map intended hypotheses to what participants actually did, quantify response patterns, then triangulate against the chats and transcripts. I’ll distinguish strong evidence from suggestive anecdotes and end with specific changes for the next workshop.


<details>
<summary>Inspected file sizes, analyzed transcripts, and computed statistics</summary>

Thinking

Inspecting file sizes, contents, and schema for analysis

`{ "commands": "set -euo pipefail\nbase=\"$HOME/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant\"\nforms=\"$HOME/Documents/forms/data-is-for-agents\"\nprintf '## paths\\n'\npwd\nfor d in \"$base\" \"$forms\"; do\n printf '\\n### %s\\n' \"$d\"\n test -d \"$d\"\n fd -t f -d 1 . \"$d\" -0 | xargs -0 -r stat -c '%n\\t%s bytes' | sort\n printf '\\nline counts:\\n'\n fd -t f -d 1 . \"$d\" -0 | xargs -0 -r wc -l | sort -n\n done\nprintf '\\n## markdown headings\\n'\nfor f in \"$base\"/*.md; do\n printf '\\n### %s\\n' \"$(basename \"$f\")\"\n (rg -n '^(#{1,4}) ' \"$f\" | head -40 || true)\ndone\nprintf '\\n## form schema / response header\\n'\nnl -ba \"$forms/form.yaml\" | sed -n '1,220p'\nprintf '\\n### responses header + first rows\\n'\nawk 'NR<=8 {print NR \":\" $0}' \"$forms/responses.tsv\"", "timeout_ms": 30000 }`

Inspecting workshop flow and experiment outcomes

`{ "commands": "set -euo pipefail\nbase=\"$HOME/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant\"\nprintf '## selected chat lines\\n'\nfor f in chatgpt-chat-1.md chatgpt-chat-2.md claude-chat-1.md claude-chat-2.md; do\n printf '\\n### %s\\n' \"$f\"\n rg -n -i 'T1|progressive|catalog|preload|portal|benchmark|result|accuracy|token|significant|p=|rerun|revised|skill|weak model|shard|freshness|collapse' \"$base/$f\" | sed -n '1,220p'\ndone\nprintf '\\n## transcript lines around exercises/results\\n'\nfor f in transcript-laptop.md transcript-phone.md; do\n printf '\\n### %s\\n' \"$f\"\n rg -n -i 'hypothesis|research|T1|technique|benchmark|result|accuracy|token|catalog|preload|progressive|model|rerun|revise|skill|experiment|significant|p-value|shard|freshness|failed|failure|Claude|Codex|ChatGPT|form' \"$base/$f\" | sed -n '1,300p'\ndone", "timeout_ms": 30000 }`

Searching arxiv.org

[arxiv.org](https://arxiv.org/abs/2307.03172)

Inspecting files with LocalMCP for specific contents

`{ "commands": "set -euo pipefail\nbase=\"$HOME/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant\"\nforms=\"$HOME/Documents/forms/data-is-for-agents\"\nfor spec in \\\n 'transcript-laptop.md:20:40' \\\n 'transcript-laptop.md:100:142' \\\n 'transcript-laptop.md:198:310' \\\n 'transcript-laptop.md:386:482' \\\n 'transcript-laptop.md:506:522' \\\n 'claude-chat-2.md:540:602' \\\n 'claude-chat-2.md:704:786' \\\n 'corpus-for-agents-skill.md:1:118' \\\n 'benchmark-prompt.md:1:20' \\\n 'postmortem-prompt.md:1:20'; do\n f=${spec%%:*}; rest=${spec#*:}; a=${rest%%:*}; b=${rest##*:}\n printf '\\n===== %s:%s-%s =====\\n' \"$f\" \"$a\" \"$b\"\n nl -ba \"$base/$f\" | sed -n \"${a},${b}p\"\ndone\nprintf '\\n===== form.yaml =====\\n'\nnl -ba \"$forms/form.yaml\" | sed -n '1,80p'", "timeout_ms": 30000 }`

Searching the web

[arxiv.org](https://arxiv.org/abs/2607.04576)

Worked for 5m 21s

Done

Sources · 24

* * [Anthropic](https://www.anthropic.com/engineering/code-execution-with-mcp) - Code execution with MCP: building more efficient AI agents \ Anthropic
* * [arXiv](https://arxiv.org/abs/2607.04576) - Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation
* * [arXiv](https://arxiv.org/abs/2307.03172) - Lost in the Middle: How Language Models Use Long Contexts
* * [Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents) - Writing effective tools for AI agents—using AI agents \ Anthropic

* * [arxiv.org](https://arxiv.org/abs/2607.04576) - Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation - July 6, 2026
* * [arxiv.org](https://arxiv.org/abs/2605.10052) - Swarm Skills: A Portable, Self-Evolving Multi-Agent System Specification for Coordination Engineering - May 11, 2026
* * [www.tomshardware.com](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-model-context-protocol-has-critical-security-flaw-exposed) - Anthropic's Model Context Protocol includes a critical remote code execution vulnerability - newly discovered exploit puts 200,000 AI servers at risk - April 22, 2026 — Security researchers at OX Security have uncovered a critical remote code execution vulnerability in Anthropic's Model Context Protocol (MCP), affecting its official SDKs in Python, TypeScript, Java, and Rust. The issue stems from insecure STDIO handling, where unsanitized user input is directly executed, impacting up to 200,000 server instances and over 150 million downloads. Despite the severity, Anthropic declined to patch the flaw, considering it “expected behavior.” MCP, an open standard enabling AI model integration with external tools, was donated to the Linux Foundation but remains maintained by Anthropic. Major platforms including OpenAI and Google have adopted it. OX identified four major exploitation vectors, including UI injection, prompt injection in IDEs, bypasses in hardened tools, and supply chain poisoning. They successfully infiltrated 9 of 11 MCP registries, executing code on six live systems. At least 10 critical CVEs have been issued, with only some patched. The researchers urged protocol-level fixes, such as command whitelisting, but Anthropic declined. This vulnerability disclosure follows a recent source code leak from Anthropic and raises questions about the company’s internal security practices, especially after launching Claude Mythos, a new AI model touted for its security testing capabilities.
* * [arxiv.org](https://arxiv.org/abs/2603.09619) - Context Engineering: From Prompts to Corporate Multi-Agent Architecture - March 10, 2026
* * [www.theverge.com](https://www.theverge.com/report/874308/anthropic-claude-code-opus-hype-moment) - Claude has been having a moment - can it keep it up? - February 5, 2026 — Since the release of Claude Code in February 2025, Anthropic has seen a dramatic surge in popularity, culminating in what many consider a pivotal moment during the 2025 holiday season. The AI model gained momentum on social media and among software engineers, outpacing competitors like OpenAI and cementing its role in enterprise coding workflows. Claude Code usage skyrocketed as the Opus 4.5 model brought a shift in agentic performance, allowing users to complete multistep tasks with minimal oversight. Its impact was so significant that developers, startups, and executives devoted holiday downtime to testing and building with the tool. Anthropic capitalized on this success by doubling rate limits for users during the holidays and expanding its customer base significantly. Internally, teams at Anthropic reported up to 90% of code written by Claude Code itself. With the launch of Opus 4.6, the company aims to improve upon speed, precision, and complex task handling. However, challenges remain: competitors like OpenAI are launching new products, security concerns have surfaced with earlier models, and public trust has dipped slightly. Nonetheless, users cite Claude Code’s productivity, superior UX, brand reliability, and limited controversy as reasons it may retain its leading role in AI coding tools.
* * [arxiv.org](https://arxiv.org/abs/2510.10276) - Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs - October 11, 2025
* * [arxiv.org](https://arxiv.org/abs/2510.04618) - Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models - October 6, 2025
* * [arxiv.org](https://arxiv.org/abs/2406.16008) - Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization - June 23, 2024
* * [arxiv.org](https://arxiv.org/abs/2311.09198) - Never Lost in the Middle: Mastering Long-Context Question Answering with Position-Agnostic Decompositional Training - November 16, 2023
* * [arxiv.org](https://arxiv.org/abs/2307.03172) - Lost in the Middle: How Language Models Use Long Contexts - July 6, 2023
* * [arxiv.org](https://arxiv.org/abs/2607.04576) - Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation - Total lines: 265
* * [arxiv.org](https://arxiv.org/abs/2307.03172) - Lost in the Middle: How Language Models Use Long Contexts - Total lines: 266
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Anthropic) - Anthropic
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Claude_%28language_model%29) - Claude (language model)
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/LLM_aided_design) - LLM aided design
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Model_Context_Protocol) - Model Context Protocol
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Anthropic%27s_Responsible_Scaling_Policy) - Anthropic's Responsible Scaling Policy
* * [de.wikipedia.org](https://de.wikipedia.org/wiki/Context_Engineering) - Context Engineering
* * [www.anthropic.com](https://www.anthropic.com/engineering/code-execution-with-mcp) - Code execution with MCP: building more efficient AI agents \ Anthropic - Total lines: 340
* * [www.anthropic.com](https://www.anthropic.com/engineering/writing-tools-for-agents) - Writing effective tools for AI agents—using AI agents \ Anthropic - Total lines: 282

</details>

The response file contains 97 actual submissions from 24 people, not 22,878 records—the apparent size comes from long multiline benchmark reports. Thirteen completed the first benchmark, eight revised it, and only two reached the second technique, so the strongest evidence is about T1 and the revision loop.

Inspected workshop flow, parsed data, and validated experiment results

A second pattern is emerging: the human priors emphasized metadata and authority, while the agents emphasized access efficiency. The only statistically significant harm in the first round—stale/conflicting shards—shows these are complements, not competing schools of thought.


<details>
<summary>Searched for code, models, and tools across multiple sources</summary>

Thinking

Inspecting file sizes, contents, and schema for analysis

`{ "commands": "set -euo pipefail\nbase=\"$HOME/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant\"\nforms=\"$HOME/Documents/forms/data-is-for-agents\"\nprintf '## paths\\n'\npwd\nfor d in \"$base\" \"$forms\"; do\n printf '\\n### %s\\n' \"$d\"\n test -d \"$d\"\n fd -t f -d 1 . \"$d\" -0 | xargs -0 -r stat -c '%n\\t%s bytes' | sort\n printf '\\nline counts:\\n'\n fd -t f -d 1 . \"$d\" -0 | xargs -0 -r wc -l | sort -n\n done\nprintf '\\n## markdown headings\\n'\nfor f in \"$base\"/*.md; do\n printf '\\n### %s\\n' \"$(basename \"$f\")\"\n (rg -n '^(#{1,4}) ' \"$f\" | head -40 || true)\ndone\nprintf '\\n## form schema / response header\\n'\nnl -ba \"$forms/form.yaml\" | sed -n '1,220p'\nprintf '\\n### responses header + first rows\\n'\nawk 'NR<=8 {print NR \":\" $0}' \"$forms/responses.tsv\"", "timeout_ms": 30000 }`

Inspecting workshop flow and experiment outcomes

`{ "commands": "set -euo pipefail\nbase=\"$HOME/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant\"\nprintf '## selected chat lines\\n'\nfor f in chatgpt-chat-1.md chatgpt-chat-2.md claude-chat-1.md claude-chat-2.md; do\n printf '\\n### %s\\n' \"$f\"\n rg -n -i 'T1|progressive|catalog|preload|portal|benchmark|result|accuracy|token|significant|p=|rerun|revised|skill|weak model|shard|freshness|collapse' \"$base/$f\" | sed -n '1,220p'\ndone\nprintf '\\n## transcript lines around exercises/results\\n'\nfor f in transcript-laptop.md transcript-phone.md; do\n printf '\\n### %s\\n' \"$f\"\n rg -n -i 'hypothesis|research|T1|technique|benchmark|result|accuracy|token|catalog|preload|progressive|model|rerun|revise|skill|experiment|significant|p-value|shard|freshness|failed|failure|Claude|Codex|ChatGPT|form' \"$base/$f\" | sed -n '1,300p'\ndone", "timeout_ms": 30000 }`

Searching arxiv.org

[arxiv.org](https://arxiv.org/abs/2307.03172)

Inspecting files with LocalMCP for specific contents

`{ "commands": "set -euo pipefail\nbase=\"$HOME/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant\"\nforms=\"$HOME/Documents/forms/data-is-for-agents\"\nfor spec in \\\n 'transcript-laptop.md:20:40' \\\n 'transcript-laptop.md:100:142' \\\n 'transcript-laptop.md:198:310' \\\n 'transcript-laptop.md:386:482' \\\n 'transcript-laptop.md:506:522' \\\n 'claude-chat-2.md:540:602' \\\n 'claude-chat-2.md:704:786' \\\n 'corpus-for-agents-skill.md:1:118' \\\n 'benchmark-prompt.md:1:20' \\\n 'postmortem-prompt.md:1:20'; do\n f=${spec%%:*}; rest=${spec#*:}; a=${rest%%:*}; b=${rest##*:}\n printf '\\n===== %s:%s-%s =====\\n' \"$f\" \"$a\" \"$b\"\n nl -ba \"$base/$f\" | sed -n \"${a},${b}p\"\ndone\nprintf '\\n===== form.yaml =====\\n'\nnl -ba \"$forms/form.yaml\" | sed -n '1,80p'", "timeout_ms": 30000 }`

Searching the web

[arxiv.org](https://arxiv.org/abs/2607.04576)

Worked for 5m 21s

Done

Sources · 24

* * [Anthropic](https://www.anthropic.com/engineering/code-execution-with-mcp) - Code execution with MCP: building more efficient AI agents \ Anthropic
* * [arXiv](https://arxiv.org/abs/2607.04576) - Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation
* * [arXiv](https://arxiv.org/abs/2307.03172) - Lost in the Middle: How Language Models Use Long Contexts
* * [Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents) - Writing effective tools for AI agents—using AI agents \ Anthropic

* * [arxiv.org](https://arxiv.org/abs/2607.04576) - Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation - July 6, 2026
* * [arxiv.org](https://arxiv.org/abs/2605.10052) - Swarm Skills: A Portable, Self-Evolving Multi-Agent System Specification for Coordination Engineering - May 11, 2026
* * [www.tomshardware.com](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-model-context-protocol-has-critical-security-flaw-exposed) - Anthropic's Model Context Protocol includes a critical remote code execution vulnerability - newly discovered exploit puts 200,000 AI servers at risk - April 22, 2026 — Security researchers at OX Security have uncovered a critical remote code execution vulnerability in Anthropic's Model Context Protocol (MCP), affecting its official SDKs in Python, TypeScript, Java, and Rust. The issue stems from insecure STDIO handling, where unsanitized user input is directly executed, impacting up to 200,000 server instances and over 150 million downloads. Despite the severity, Anthropic declined to patch the flaw, considering it “expected behavior.” MCP, an open standard enabling AI model integration with external tools, was donated to the Linux Foundation but remains maintained by Anthropic. Major platforms including OpenAI and Google have adopted it. OX identified four major exploitation vectors, including UI injection, prompt injection in IDEs, bypasses in hardened tools, and supply chain poisoning. They successfully infiltrated 9 of 11 MCP registries, executing code on six live systems. At least 10 critical CVEs have been issued, with only some patched. The researchers urged protocol-level fixes, such as command whitelisting, but Anthropic declined. This vulnerability disclosure follows a recent source code leak from Anthropic and raises questions about the company’s internal security practices, especially after launching Claude Mythos, a new AI model touted for its security testing capabilities.
* * [arxiv.org](https://arxiv.org/abs/2603.09619) - Context Engineering: From Prompts to Corporate Multi-Agent Architecture - March 10, 2026
* * [www.theverge.com](https://www.theverge.com/report/874308/anthropic-claude-code-opus-hype-moment) - Claude has been having a moment - can it keep it up? - February 5, 2026 — Since the release of Claude Code in February 2025, Anthropic has seen a dramatic surge in popularity, culminating in what many consider a pivotal moment during the 2025 holiday season. The AI model gained momentum on social media and among software engineers, outpacing competitors like OpenAI and cementing its role in enterprise coding workflows. Claude Code usage skyrocketed as the Opus 4.5 model brought a shift in agentic performance, allowing users to complete multistep tasks with minimal oversight. Its impact was so significant that developers, startups, and executives devoted holiday downtime to testing and building with the tool. Anthropic capitalized on this success by doubling rate limits for users during the holidays and expanding its customer base significantly. Internally, teams at Anthropic reported up to 90% of code written by Claude Code itself. With the launch of Opus 4.6, the company aims to improve upon speed, precision, and complex task handling. However, challenges remain: competitors like OpenAI are launching new products, security concerns have surfaced with earlier models, and public trust has dipped slightly. Nonetheless, users cite Claude Code’s productivity, superior UX, brand reliability, and limited controversy as reasons it may retain its leading role in AI coding tools.
* * [arxiv.org](https://arxiv.org/abs/2510.10276) - Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs - October 11, 2025
* * [arxiv.org](https://arxiv.org/abs/2510.04618) - Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models - October 6, 2025
* * [arxiv.org](https://arxiv.org/abs/2406.16008) - Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization - June 23, 2024
* * [arxiv.org](https://arxiv.org/abs/2311.09198) - Never Lost in the Middle: Mastering Long-Context Question Answering with Position-Agnostic Decompositional Training - November 16, 2023
* * [arxiv.org](https://arxiv.org/abs/2307.03172) - Lost in the Middle: How Language Models Use Long Contexts - July 6, 2023
* * [arxiv.org](https://arxiv.org/abs/2607.04576) - Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation - Total lines: 265
* * [arxiv.org](https://arxiv.org/abs/2307.03172) - Lost in the Middle: How Language Models Use Long Contexts - Total lines: 266
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Anthropic) - Anthropic
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Claude_%28language_model%29) - Claude (language model)
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/LLM_aided_design) - LLM aided design
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Model_Context_Protocol) - Model Context Protocol
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Anthropic%27s_Responsible_Scaling_Policy) - Anthropic's Responsible Scaling Policy
* * [de.wikipedia.org](https://de.wikipedia.org/wiki/Context_Engineering) - Context Engineering
* * [www.anthropic.com](https://www.anthropic.com/engineering/code-execution-with-mcp) - Code execution with MCP: building more efficient AI agents \ Anthropic - Total lines: 340
* * [www.anthropic.com](https://www.anthropic.com/engineering/writing-tools-for-agents) - Writing effective tools for AI agents—using AI agents \ Anthropic - Total lines: 282

</details>

Inspected files with LocalMCP for specific contents


<details>
<summary>Searched the web and arxiv.org</summary>

Thinking

Inspecting file sizes, contents, and schema for analysis

`{ "commands": "set -euo pipefail\nbase=\"$HOME/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant\"\nforms=\"$HOME/Documents/forms/data-is-for-agents\"\nprintf '## paths\\n'\npwd\nfor d in \"$base\" \"$forms\"; do\n printf '\\n### %s\\n' \"$d\"\n test -d \"$d\"\n fd -t f -d 1 . \"$d\" -0 | xargs -0 -r stat -c '%n\\t%s bytes' | sort\n printf '\\nline counts:\\n'\n fd -t f -d 1 . \"$d\" -0 | xargs -0 -r wc -l | sort -n\n done\nprintf '\\n## markdown headings\\n'\nfor f in \"$base\"/*.md; do\n printf '\\n### %s\\n' \"$(basename \"$f\")\"\n (rg -n '^(#{1,4}) ' \"$f\" | head -40 || true)\ndone\nprintf '\\n## form schema / response header\\n'\nnl -ba \"$forms/form.yaml\" | sed -n '1,220p'\nprintf '\\n### responses header + first rows\\n'\nawk 'NR<=8 {print NR \":\" $0}' \"$forms/responses.tsv\"", "timeout_ms": 30000 }`

Inspecting workshop flow and experiment outcomes

`{ "commands": "set -euo pipefail\nbase=\"$HOME/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant\"\nprintf '## selected chat lines\\n'\nfor f in chatgpt-chat-1.md chatgpt-chat-2.md claude-chat-1.md claude-chat-2.md; do\n printf '\\n### %s\\n' \"$f\"\n rg -n -i 'T1|progressive|catalog|preload|portal|benchmark|result|accuracy|token|significant|p=|rerun|revised|skill|weak model|shard|freshness|collapse' \"$base/$f\" | sed -n '1,220p'\ndone\nprintf '\\n## transcript lines around exercises/results\\n'\nfor f in transcript-laptop.md transcript-phone.md; do\n printf '\\n### %s\\n' \"$f\"\n rg -n -i 'hypothesis|research|T1|technique|benchmark|result|accuracy|token|catalog|preload|progressive|model|rerun|revise|skill|experiment|significant|p-value|shard|freshness|failed|failure|Claude|Codex|ChatGPT|form' \"$base/$f\" | sed -n '1,300p'\ndone", "timeout_ms": 30000 }`

Searching arxiv.org

[arxiv.org](https://arxiv.org/abs/2307.03172)

Inspecting files with LocalMCP for specific contents

`{ "commands": "set -euo pipefail\nbase=\"$HOME/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant\"\nforms=\"$HOME/Documents/forms/data-is-for-agents\"\nfor spec in \\\n 'transcript-laptop.md:20:40' \\\n 'transcript-laptop.md:100:142' \\\n 'transcript-laptop.md:198:310' \\\n 'transcript-laptop.md:386:482' \\\n 'transcript-laptop.md:506:522' \\\n 'claude-chat-2.md:540:602' \\\n 'claude-chat-2.md:704:786' \\\n 'corpus-for-agents-skill.md:1:118' \\\n 'benchmark-prompt.md:1:20' \\\n 'postmortem-prompt.md:1:20'; do\n f=${spec%%:*}; rest=${spec#*:}; a=${rest%%:*}; b=${rest##*:}\n printf '\\n===== %s:%s-%s =====\\n' \"$f\" \"$a\" \"$b\"\n nl -ba \"$base/$f\" | sed -n \"${a},${b}p\"\ndone\nprintf '\\n===== form.yaml =====\\n'\nnl -ba \"$forms/form.yaml\" | sed -n '1,80p'", "timeout_ms": 30000 }`

Searching the web

[arxiv.org](https://arxiv.org/abs/2607.04576)

Worked for 5m 21s

Done

Sources · 24

* * [Anthropic](https://www.anthropic.com/engineering/code-execution-with-mcp) - Code execution with MCP: building more efficient AI agents \ Anthropic
* * [arXiv](https://arxiv.org/abs/2607.04576) - Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation
* * [arXiv](https://arxiv.org/abs/2307.03172) - Lost in the Middle: How Language Models Use Long Contexts
* * [Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents) - Writing effective tools for AI agents—using AI agents \ Anthropic

* * [arxiv.org](https://arxiv.org/abs/2607.04576) - Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation - July 6, 2026
* * [arxiv.org](https://arxiv.org/abs/2605.10052) - Swarm Skills: A Portable, Self-Evolving Multi-Agent System Specification for Coordination Engineering - May 11, 2026
* * [www.tomshardware.com](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-model-context-protocol-has-critical-security-flaw-exposed) - Anthropic's Model Context Protocol includes a critical remote code execution vulnerability - newly discovered exploit puts 200,000 AI servers at risk - April 22, 2026 — Security researchers at OX Security have uncovered a critical remote code execution vulnerability in Anthropic's Model Context Protocol (MCP), affecting its official SDKs in Python, TypeScript, Java, and Rust. The issue stems from insecure STDIO handling, where unsanitized user input is directly executed, impacting up to 200,000 server instances and over 150 million downloads. Despite the severity, Anthropic declined to patch the flaw, considering it “expected behavior.” MCP, an open standard enabling AI model integration with external tools, was donated to the Linux Foundation but remains maintained by Anthropic. Major platforms including OpenAI and Google have adopted it. OX identified four major exploitation vectors, including UI injection, prompt injection in IDEs, bypasses in hardened tools, and supply chain poisoning. They successfully infiltrated 9 of 11 MCP registries, executing code on six live systems. At least 10 critical CVEs have been issued, with only some patched. The researchers urged protocol-level fixes, such as command whitelisting, but Anthropic declined. This vulnerability disclosure follows a recent source code leak from Anthropic and raises questions about the company’s internal security practices, especially after launching Claude Mythos, a new AI model touted for its security testing capabilities.
* * [arxiv.org](https://arxiv.org/abs/2603.09619) - Context Engineering: From Prompts to Corporate Multi-Agent Architecture - March 10, 2026
* * [www.theverge.com](https://www.theverge.com/report/874308/anthropic-claude-code-opus-hype-moment) - Claude has been having a moment - can it keep it up? - February 5, 2026 — Since the release of Claude Code in February 2025, Anthropic has seen a dramatic surge in popularity, culminating in what many consider a pivotal moment during the 2025 holiday season. The AI model gained momentum on social media and among software engineers, outpacing competitors like OpenAI and cementing its role in enterprise coding workflows. Claude Code usage skyrocketed as the Opus 4.5 model brought a shift in agentic performance, allowing users to complete multistep tasks with minimal oversight. Its impact was so significant that developers, startups, and executives devoted holiday downtime to testing and building with the tool. Anthropic capitalized on this success by doubling rate limits for users during the holidays and expanding its customer base significantly. Internally, teams at Anthropic reported up to 90% of code written by Claude Code itself. With the launch of Opus 4.6, the company aims to improve upon speed, precision, and complex task handling. However, challenges remain: competitors like OpenAI are launching new products, security concerns have surfaced with earlier models, and public trust has dipped slightly. Nonetheless, users cite Claude Code’s productivity, superior UX, brand reliability, and limited controversy as reasons it may retain its leading role in AI coding tools.
* * [arxiv.org](https://arxiv.org/abs/2510.10276) - Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs - October 11, 2025
* * [arxiv.org](https://arxiv.org/abs/2510.04618) - Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models - October 6, 2025
* * [arxiv.org](https://arxiv.org/abs/2406.16008) - Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization - June 23, 2024
* * [arxiv.org](https://arxiv.org/abs/2311.09198) - Never Lost in the Middle: Mastering Long-Context Question Answering with Position-Agnostic Decompositional Training - November 16, 2023
* * [arxiv.org](https://arxiv.org/abs/2307.03172) - Lost in the Middle: How Language Models Use Long Contexts - July 6, 2023
* * [arxiv.org](https://arxiv.org/abs/2607.04576) - Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation - Total lines: 265
* * [arxiv.org](https://arxiv.org/abs/2307.03172) - Lost in the Middle: How Language Models Use Long Contexts - Total lines: 266
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Anthropic) - Anthropic
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Claude_%28language_model%29) - Claude (language model)
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/LLM_aided_design) - LLM aided design
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Model_Context_Protocol) - Model Context Protocol
* * [en.wikipedia.org](https://en.wikipedia.org/wiki/Anthropic%27s_Responsible_Scaling_Policy) - Anthropic's Responsible Scaling Policy
* * [de.wikipedia.org](https://de.wikipedia.org/wiki/Context_Engineering) - Context Engineering
* * [www.anthropic.com](https://www.anthropic.com/engineering/code-execution-with-mcp) - Code execution with MCP: building more efficient AI agents \ Anthropic - Total lines: 340
* * [www.anthropic.com](https://www.anthropic.com/engineering/writing-tools-for-agents) - Writing effective tools for AI agents—using AI agents \ Anthropic - Total lines: 282

</details>

</details>

# What the workshop actually established

The strongest conclusion is not “catalogs are better.” It is:

> **Progressive disclosure is load-shifting. It trades context cost for navigation work. It pays when context is scarce and the model can navigate reliably; otherwise it can be overhead—or actively harmful.**

The workshop also demonstrated something arguably more valuable: AI can generate a sophisticated benchmark remarkably cheaply, but **determining whether that benchmark measures the intended construct remains the scarce human skill**.

## Evidence base

I parsed `responses.tsv` as multiline TSV rather than treating its 22,878 physical lines as separate records.

| Stage | Participants submitting | What it supports |
| --- | --- | --- |
| Unaided hypothesis | 22 | Human priors |
| Agent research | 17 | Candidate techniques |
| T1 first experiment | 13 | Useful boundary evidence, but wrong main construct |
| T1 revised experiment | 8 | Four clean strict comparisons, one useful alternative comparison, three unusable/floor/stopped runs |
| T2 experiment | 2 | No valid evidence about CSV versus JSON |

There were 97 submissions from 24 people in total. The session therefore generated a surprisingly large body of work, but the evidential funnel narrows sharply: **only about five revised T1 runs support substantive conclusions**.

## 1. The first “null result” was really a benchmark bug

The first benchmark gave both conditions a folder plus identical `read`, `grep`, and `bash` tools. That meant both conditions already had just-in-time access. It compared:

* ordinary searchable files, versus
* searchable files plus an index or shards.

It did **not** compare:

* full corpus loaded into context, versus
* catalog plus selective fetch.

This was correctly diagnosed during the workshop: “the protocol worked, the construct didn’t.” `transcript-laptop.md:247-269`

That distinction explains the apparent reversal:

* T1 v1 mostly found no accuracy difference.
* T1 v2, after moving the intervention into the sub-agent prompt, found large token savings.

This is not evidence that the first experiment “failed.” It established an important boundary condition:

> **A grep-able filesystem is already a form of progressive disclosure. Adding a catalog is a much smaller intervention than replacing context preload with selective access.**

The revised prompt fixed the construct, aligned the metric with the joint accuracy-and-cost claim, sized levels relative to the model’s context window, and required explicit execution attestation. The original benchmark’s predeclared difficulty ladder was already a strong design choice because it converted “retry until significant” into a legitimate search for a crossover point. `claude-chat-2.md:546-594`

### Action

Every generated benchmark should begin with a **construct preflight**:

1. Show one complete prompt from A and B.
2. State exactly which bytes differ.
3. Run one trace from each condition.
4. Ask an independent reviewer: “Does this operationalize the claimed distinction?”

Do this before the 48 scored runs.

## 2. Against actual preloading, selective access saves a lot—but capable models are required

The four interpretable strict PORTAL-versus-CATALOG reruns gave this pattern:

| Model/run | Portal accuracy | Catalog accuracy | Overall input-token reduction |
| --- | --- | --- | --- |
| Haiku 4.5 | 20/24 | 21/24 | 7.3× |
| GPT-5.4-mini | 24/24 | 24/24 | 2.4× |
| GPT-5.4-mini | 15/24 | 15/24 | 7.1× |
| GPT-4o-mini | 15/24 | 11/24 | 21.1×, but accuracy failed |

For the three capable-model runs, catalog-and-fetch preserved accuracy and used **2.4×–7.3× fewer input tokens overall**. In the largest Haiku condition, where the portal exceeded the context window, the difference reached **27.6×**. `claude-chat-2.md:727-749`

But the weaker GPT-4o-mini run exposed the trade-off: the catalog was dramatically cheaper, yet its agents made more tool calls, hit the cap more often, and lost four answers.

A still weaker tool-using model largely failed to invoke tools and sometimes emitted tool-call JSON as prose. That run also exposed `canonical-facts.json` inside the accessible folder, so it is not a valid organization experiment. It is useful only as a **tool-use floor effect**.

The mechanism is therefore:

* PORTAL spends tokens on content.
* CATALOG spends agent capability and tool calls on navigation.
* Strong tool users win the exchange.
* Weak tool users may not.

### Action

Do not classify models merely as “small” or “large.” Add a six-task preflight:

* locate one file from catalog metadata;
* follow a two-hop relationship;
* resolve an “as of date” value;
* reject a near-miss entity;
* perform one aggregate;
* report an absent value correctly.

Only use catalog-driven access if the intended model passes this navigation test reliably within the call budget.

## 3. There is a crossover point, but “0.5× context window” is not established

One clean GPT-5.4-mini run showed:

* Level 1: catalog used about **10% more** tokens;
* Level 2: catalog used **1.7× fewer**;
* Level 3: catalog used **4.1× fewer**.

The alternative Haiku experiment—flat files with read/search versus indexed SQLite plus code—found:

* around 50k tokens: the index was overhead;
* around 200k: about 3× saving;
* around 500k: about 2.3× saving;
* simple off-target lookups: indexed access was substantially worse;
* targeted aggregation tasks: indexed access was better.

The most surprising trace was that Haiku correctly grep-filtered and mentally summed as many as 236 three-digit values. The expected accuracy failure never arrived; only the context-cost difference appeared.

So the workshop supports the existence of a **phase transition**, but not a universal threshold. The generated skill’s “approximately 0.5×W” rule is a useful hypothesis, not yet a measured constant.

The crossover depends on:

* corpus size relative to the *effective* context budget;
* whether the task is narrow lookup, broad discovery, or aggregation;
* catalog size;
* file predictability;
* model navigation ability;
* whether the baseline already has grep/code access.

### Action

Treat roughly **0.25W–0.75W as the zone worth benchmarking**, not as a fixed cutoff. Below it, preload or direct file access may be simpler and cheaper. Above it, selective access is increasingly likely to dominate.

## 4. The humans and agents each noticed half of the answer

The unaided human responses concentrated on:

* metadata and semantic meaning;
* provenance, freshness and authority;
* relationships and hierarchy;
* documentation and schemas.

The research agents converged most strongly on progressive access: 11 of the 15 submissions available during the live collation suggested it. `transcript-laptop.md:105-139`

At first these seem like different theories:

* humans: **make the data interpretable and trustworthy**;
* agents: **avoid loading irrelevant data**.

The first-round harm result shows they are complementary. In one statistically significant run, the sharded agent representation lost six tasks because shards exposed stale or conflicting values without making authority rules sufficiently clear; the human layout won 24/24 versus 18/24, with paired p≈0.03. `transcript-laptop.md:257-263`

Thus:

> **Retrieval efficiency without authority metadata merely lets the agent reach the wrong fact faster.**

This may be the most defensible substantive lesson from the whole workshop.

### Action

Every fetchable unit containing changing facts should carry or inherit:

* authoritative source;
* effective date and recorded date;
* supersession rule;
* entity identity;
* version or commit;
* freshness timestamp;
* scope and exceptions.

A catalog is not a substitute for these. It should expose them.

## 5. Accuracy was often the wrong primary measure

Many v1 runs were at or near ceiling:

* 48/48 correct;
* 47/48 correct;
* 23/24 versus 24/24.

A McNemar p-value of 1.0 in that situation does not establish equivalence. It often means there were no discordant pairs and therefore no statistical information.

The technique card made a joint claim:

1. preserve success;
2. consume substantially fewer tokens.

But the original benchmark made accuracy the primary metric and token consumption secondary. This mismatch was identified during the session. `transcript-laptop.md:247-253`

The revised “within one answer” non-inferiority rule was practical, but it is a **decision rule**, not a formal statistical non-inferiority result with a confidence interval.

For this class of experiment, the better outcome is:

> **Cost per successful answer under a fixed latency/tool-call budget.**

Report at least:

* success rate;
* total input tokens;
* tokens per correct answer;
* tool calls;
* latency;
* truncations;
* errors and cap hits.

And report them by task type. The off-target results showed that a representation optimized for pinpoint retrieval may perform worse on whole-corpus questions.

## 6. The workshop’s biggest productivity result was benchmark creation—not the data technique

The session began explicitly as a “teach people how to find out” workshop rather than an attempt to provide a fixed doctrine. `transcript-laptop.md:23-35`

It demonstrated that agents could generate, in minutes:

* synthetic worlds;
* controlled transformations;
* canonical answer keys;
* task sets;
* execution harnesses;
* deterministic graders;
* statistical reports;
* reproducible scripts.

That is genuinely new leverage.

But the effort moved downstream. The host repeatedly struggled to locate the actual conclusion inside 30,000–60,000-character submissions, then had to use another agent to audit the benchmark. The final reflection captured this precisely: creating the benchmark became easy; judging whether it was a good benchmark became the bottleneck. `transcript-laptop.md:511-517`

The participation funnel also reflects the operational weight:

* 22 supplied priors;
* 13 completed T1 v1;
* 8 completed the revision;
* 2 reached T2.

This cannot be read purely as participant attrition—the session was time-boxed—but it shows that custom harness setup, API availability, quota failures and huge reports do not scale cleanly in a live workshop.

### Action

Require every report to begin with a machine-readable experiment card of perhaps 30 lines:


```
experiment_id:
claim:
actual_contrast:
model:
effective_context_window:
real_llm_runs:
answer_key_exposed: false
primary_decision:
accuracy_A:
accuracy_B:
input_tokens_A:
input_tokens_B:
tool_calls_A:
tool_calls_B:
cap_hits_A:
cap_hits_B:
truncations_A:
truncations_B:
validity_verdict:
one_sentence_conclusion:
```

Keep code and raw traces as attachments. Do not make the live synthesis depend on reading the full report.

## 7. T2 produced no evidence about CSV versus JSON

The session selected the claim that header-once CSV might beat repeated-key JSON. But the prompt sent to participants still contained the progressive-disclosure intervention.

One submission explicitly admitted it had rerun PORTAL versus CATALOG, not CSV versus JSON. The other attempted the correct representation comparison, but almost every task failed and the inputs were heavily truncated, producing a floor effect.

The error was caught live and participants were told to stop. `transcript-laptop.md:445-477`

Therefore:

> **The workshop tells us nothing defensible about CSV versus JSON.**

That should be stated prominently because a generated skill could otherwise silently absorb the apparent result.

### Action

Put immutable identifiers in every prompt and result:


```
EXPERIMENT_ID: T2-TABLE-SERIALIZATION-v1
THE ONLY INTENDED DIFFERENCE:
A = repeated-key JSON rows
B = header-once CSV rows
```

Have the runner abort if its report’s claimed contrast does not match the experiment manifest.

# Audit of the generated `corpus-for-agents-skill.md`

The generated skill is directionally good because it is a **decision rule rather than a universal transformation**. Its strongest parts are:

* measure before acting;
* recognize ordinary grep as progressive access;
* preserve freshness rules when sharding;
* account for model tool-use capability;
* state what was not tested.
`corpus-for-agents-skill.md:13-32, 52-58, 84-101`

But it overstates the evidence in several places.

1. **“Never concatenate the corpus into the prompt” is too absolute.** One small-corpus run found preload cheaper, with identical accuracy. The defensible rule is “avoid preloading near or beyond the effective context budget; benchmark it for small corpora and broad/global tasks.”
2. **The 0.5W threshold is provisional.** It comes largely from one alternative comparison and should be framed as a starting heuristic.
3. **“Stale catalog is worse than none” was not tested.** Plausible advice should be labelled as engineering judgment rather than workshop evidence.
4. **The evidence ledger is too compressed.** “13 attested experiments” groups clean runs, floor effects, a deterministic proxy and stopped harnesses. The skill should list each experiment’s validity status.
5. **“Weak model” is not operational.** Replace it with the six-task navigation preflight.

A more defensible core rule would be:

> Start with existing searchable files. Add a compact catalog only when discovery or context cost is material. Never discard authority, identity or version semantics while sharding. Validate the catalog with the actual model and representative tasks, optimizing tokens per correct answer rather than token count alone.

# External stress-test

The workshop’s conclusions align unusually well with outside evidence.

Anthropic’s motivating MCP example reported a reduction from 150,000 to 2,000 tokens by loading tool definitions selectively and processing intermediate data in code. But that is an extreme many-tools case, not evidence that every ordinary file corpus needs a catalog. [Anthropic](https://www.anthropic.com/engineering/code-execution-with-mcp)

More strikingly, a preregistered study published on July 6, 2026—one day before the workshop—tested progressive disclosure on a real 709-page wiki. Its capable agent often skipped the index entirely and inferred the target path, closely matching the workshop’s v1 discovery that self-routing filesystem agents already perform just-in-time access. The retrofit remained quality-non-inferior and reduced costs by about 30–34% under free or constrained self-routing, and more under forced preload; the measured mechanism was more targeted reading, not merely avoiding an index load. [arXiv](https://arxiv.org/abs/2607.04576)

Long-context research also supports the underlying concern: models do not always exploit long input uniformly, particularly when relevant information is buried in the middle. [arXiv](https://arxiv.org/abs/2307.03172)

Finally, Anthropic’s guidance on tool evaluation recommends realistic rather than superficial tasks, held-out test sets, multiple operational metrics and raw-trace review—the exact improvements the workshop discovered through experience. [Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents)

# The three most valuable takeaways

1. **Do not ask “What format is best for agents?” Ask “Where should each unit of work happen?”** Context, filesystem, query engine, code sandbox and model reasoning have different costs and capabilities.
2. **An eval can execute perfectly while measuring the wrong thing.** Construct validation, answer-key leakage checks and trace inspection matter more than statistical polish applied afterward.
3. **The durable asset is not the answer; it is the hypothesis → benchmark → audit → conditional skill loop.** The workshop successfully demonstrated that knowledge can be converted into an executable, revisable asset rather than something the human must remember. `transcript-laptop.md:513-519`

The resulting headline for the workshop is:

> **Give agents less data only when you also give them a reliable way to find the right data—and enough metadata to know which fact to trust.**

---

---
title: "Data engineering for agents workshop"
date: 2026-07-11T15:19:44+05:30
source: "https://claude.ai/chat/8827adb5-7e3b-415a-af71-7f3950057ecf"
---

## User

I'm running this workshop. <WORKSHOP> Title: When Data is for Agents, Not Humans, Fifth Elephant Workshop, 07 Jul 2026 **Overview** Who will be consuming your data - humans or agents? When it’s agents, do you structure it differently? Optimize for token budgets instead of disk or query cost? From what I see, we might not need clean, joined data (agents can do that), but descriptions of relationships. Functions become checklists. Tools beat tables. Logs beat docs. Ambiguity + context might work better than a single-source of truth. It’s a 4-hour hands-on session. You’ll be doing the work and sharing results, not watching slides. We’ll share prompts live and the recording afterwards. **What this workshop is about** In this workshop, we’ll (together) explore: 1. How data engineering for agents is different than for humans 2. How agents themselves can help engineer the data for agents **Audience** This session is for: - data engineers connecting agents into pipelines - analytics/BI folks whose dashboards are vanishing into chatbots - anyone publishing docs, schemas, or APIs that agents will read **What you’ll leave with** 1. A working feel for how the same dataset looks different to a human and to an agent 2. An agent data checklist: can an agent discover, understand, efficiently retrieve, call the right tool, trust the source, recover from errors? 3. Prompts and small scripts to make your tables, docs, and logs agent-accessible 4. Your results, published and shared, reproducibly **What to bring** - Laptop (your tablet/phone won’t do for this session), a modern browser - A paid ChatGPT Plus or Claude Pro account (\~Rs 2,000 - just buy a month). The free tiers won’t do some exercises. - Optional, for coders: uv, Node.js, and DuckDB installed - Datasets, docs, logs, photos, or anything you care about. We’ll work with your data What are approaches or organize data for agents? </WORKSHOP> "Data" includes any content, data, tool, or any other input an agent might read or use, which includes: - structured data: tables, spreadsheets, databases, JSON, YAML, configuration, ... - unstructured data: code, markdown, web pages, PDFs, other documents, videos, images, any files, blobs, ... - organization: folders, archives, websites, schemas, ontologies, taxonomies, ... - tools: tool choice, tool docs/descriptions, tool configuration, ... - tool outputs: error messages, session/program logs, telemetry, diagnostics, progress, ... - SKIP harness artifacts: prompts, AGENTS.md/CLAUDE.md, SKILL.md, memory systems, permissions, hooks, plugins, ... **QUESTION 1**: What else? Am I missing something? List prioritized by importance to agents. --- Next, I'd like an AI agent to research online for the modern best practices on how to structure and optimize inputs for agent consumption. Specifically, how to go about organizing these for agents **as opposed to humans**, listing the key differences in thought process. Of course, some of these are only meant for humans (e.g. harness artifacts) - so let's skip those. But whatever is traditionally meant for humans AND can be used by agents, let's include that. In this context, I want the agent to research the best practices, emerging techniques, ways of working top AI companies like Anthropic internally use, opinions of experts who create / curate data for AI agent consumption, etc. This should be shared in a priorized way, i.e. highest impact (value x frequency) + highest difference between how we would organize it for humans vs agents. I will then have the audience 1. Run this prompt across multiple agents (Claude, ChatGPT, etc.) and compare the results 2. Pick the top few techniques 3. Have a coding agent (Codex, Claude, etc.) generate synthetic data for each of these techniques, run a test / benchmark to see how well agents perform against a task when the data is organized the way it typically is for humans vs the way it is organized for agents, and share the results. - I want to make sure that this will not cost too much (i.e. ideally included in a single run of a $20 plan of Claude or Codex), so each person is able to test at least 1 and potentially 3 data organization techniques - I would like the results to be reasonably statistically significant - it should give enough confidence that it works - The test should involve invoking sub-agents with the right model + config in a way that will not be polluted by the parent agent's context, so that the test is fair and reproducible. - The result should be documented in a single Markdown file they can share that CLEARLY documents the setup, the test, the results, and the conclusions. This should be reproducible by anyone else who wants to run it just with that single Markdown file - Any other factors I have not thought of? **QUESTION 2**: What would be an apt, concise prompt for step 1 that will allow the participants to easily pick the first few techniques to test? **QUESTION 3**: What would be an apt, concise prompt for step 3 that will allow the participants to paste it, then pick any one technique to test, and run it? They should be able to copy-paste the prompt, copy-paste one technique from prompt #1, and press enter - so prompt #1 should also be designed to be copy-paste friendly.

---

## Claude

<details>
<summary>Architected taxonomy gaps, research prompt structure, and reproducible benchmark design</summary>

> Anand needs three specific deliverables for his Fifth Elephant workshop today: identifying gaps in his data taxonomy ranked by agent relevance, plus concise research and benchmark prompts for participants. I'm considering whether to apply my skills framework here, though this is a straightforward chat response rather than file work.
>
> I should check my relevant skills first—anand-objectives, expert-lens, and blind-spot seem applicable, and I'll keep the language simple and direct per Anand's preference. Let me pull up those skill files to make sure I'm approaching this the right way.
>
> Read anand-objectives skill since this is a substantive answer for Anand
>
> Read expert-lens skill for non-trivial analysis guidance
>
> Read blind-spot skill since this task asks "what am I missing"
>
> The workshop is happening today, so I need to move fast and stay practical. I'm thinking through three core deliverables: identifying what's missing from the taxonomy that matters most to agents, crafting a research prompt that participants can use to surface actionable techniques, and building a quick benchmark prompt they can test with. I'm leaning toward skipping web research myself since the participants will be doing that legwork anyway—my focus should be on designing prompts that guide them effectively, though I could do a quick sanity check on current best practices to make sure I'm not steering them wrong.
>
> For Q1, I'm looking at what gaps exist in the current taxonomy beyond structured data, unstructured data, organization, tools, and tool outputs. The big missing pieces I'm seeing are metadata and provenance—things like data dictionaries, column descriptions, units, freshness timestamps, and lineage information that agents can't just ask someone about. Then there's the retrieval and access layer: how agents actually discover and fetch data through search indexes, embeddings, vector stores, chunking strategies, and APIs. And finally, examples and few-shot corpora—sample queries with answers and worked examples that help agents understand interfaces better.
>
> Beyond those top three, I'm also thinking about environment state like file system layout and git history as a form of documentation, verification artifacts like tests and schemas that let agents validate their own work, communication exhaust from emails and chat threads that provide rich context, stable identifiers and linking mechanisms for navigation, access control and credentials context, temporal data like changelogs, negative knowledge about what not to do and known gotchas, human context for escalation, and real-time streams. Prioritizing by what matters most to agents: metadata and provenance, examples, verification and ground truth, then the retrieval and discovery interfaces.
>
> For the research prompt itself, I need to structure it so participants can paste it into Claude or ChatGPT with web search enabled, and get back a prioritized list of techniques. The output format needs to be rigid — each technique as a self-contained block with name, definition, how humans versus agents approach it differently, why agents differ, a measurable claim, and difficulty level. I'm targeting around ten techniques ranked by impact times frequency times the delta between human and agent approaches, with each technique capped at roughly 120 words so any single one can be extracted and used in a follow-up prompt. The research prompt itself should ask for current best practices from 2025-2026 across engineering blogs from major AI labs and practitioners who specialize in data curation for agents, covering structured data, unstructured documents, folder organization, tool definitions, outputs, logs, and error messages — but explicitly excluding agent harness artifacts.
>
> For the benchmark prompt, I'm designing a test that can run within a $20 budget as a single execution, using sub-agents with isolated context so the parent's framing doesn't contaminate the results. The test should be statistically meaningful through paired comparisons where the same tasks run under both conditions, randomized order, and the sub-agent kept blind to which condition it's evaluating. Output should be a single reproducible markdown file, and I need to think through grading strategy — deterministic checks where possible, exact answers preferred — and sample size calibration to avoid ceiling or floor effects. For each task and condition, I'll spin up a fresh sub-agent with only the question and access to that folder's data, keeping the technique description and expected answers hidden to avoid bias. I'll record the answer, correctness, tokens, and timing, then grade everything deterministically with a script and run a paired statistical test. The final report needs to include the full setup, all 20 tasks with expected answers, the exact sub-agent prompt, raw results, statistics with p-value, and reproduction instructions—staying under 60 calls and small file sizes. Key gotchas: the synthetic data must use invented entities so it's not answerable from training data, and both conditions need identical facts just organized differently, otherwise I'm testing data availability rather than the technique itself. I should publish the prompts and a results template as a GitHub repo so participants can clone it and submit results via pull requests. The blind-spot weave for Q1 is really the core insight here—surfacing what might be missed. I'll keep the writing straightforward and substantial without unnecessary flourish.
>
> Done

</details>

Great structure. Answers to all three, plus a few traps to avoid.

### Question 1: What's missing from your "data" list

Ranked by how much agents depend on it:

1. **Metadata, provenance, and freshness** — data dictionaries, column meanings, units, "last updated" stamps, lineage, licenses. A human asks a colleague what `amt_usd_adj` means. An agent can't. This is probably the single biggest gap in your list.
2. **Worked examples and golden records** — sample queries with correct answers, example API calls with real responses, test fixtures. Agents learn interfaces from examples faster than from specs. Humans skim examples; agents pattern-match on them.
3. **Verification artifacts** — tests, validators, checksums, expected outputs, eval sets. Agents need a way to check their own work mid-task. Humans carry this in their heads.
4. **Discovery and retrieval interfaces** — search indexes, sitemaps, llms.txt, embeddings, "table of contents" files, pagination and API affordances. Not the data itself, but how an agent _finds_ it. You hint at this under "organization" but it deserves its own slot.
5. **Change history** — changelogs, diffs, git history, commit messages, version tags. Commit messages are docs written for humans that agents mine heavily.
6. **Negative knowledge** — deprecations, known bugs, gotchas, "don't do this" notes. Humans learn these socially; agents only know them if written down.
7. **Communication exhaust** — Slack threads, emails, tickets, meeting transcripts, PR review comments. Traditionally human-only; increasingly agent food.
8. **Identifiers and links** — stable IDs, resolvable URLs, explicit foreign keys. Agents navigate by following references, so dangling or implicit links hurt them more than humans.
9. **Cost and access constraints** — rate limits, quotas, auth scopes, price per call. Agents must plan around these; they're data about the data.
10. **Ownership and escalation info** — who owns this table, who to ask. Matters when the agent has to hand off to a human.

One meta-gap: your list is all _nouns_. Agents also consume _processes_ — runbooks, SOPs, checklists. You touch this with "functions become checklists" in your overview but it's not in the taxonomy.

### Question 2: The research prompt

The key design choice: force a fixed template per technique, self-contained, so one block can be copy-pasted straight into prompt #3. Here it is:

```
Research current (2025–2026) best practices for organizing data for AI AGENTS
to consume, as opposed to humans. "Data" here means: structured data (tables,
JSON, schemas), documents (markdown, PDFs, web pages), folder and site
organization, tool definitions and docs, tool outputs, logs, and error
messages. EXCLUDE agent-harness artifacts (system prompts, AGENTS.md,
SKILL.md, memory, permissions).

Search the web for: engineering blogs from Anthropic, OpenAI, Google, and
similar labs; writing by practitioners who prepare data, docs, or APIs for
agents; emerging conventions (e.g., llms.txt, MCP tool-design guidance);
any benchmarks comparing data formats for agents.

Return the TOP 10 techniques, ranked by:
(impact × how often the situation occurs) × (how DIFFERENTLY you would do it
for agents vs humans). Skip anything where the human way and agent way are
the same.

Format each technique EXACTLY as below — self-contained, under 120 words,
no references to other techniques, so each block can be copy-pasted alone:

### T{n}. {Short technique name}
- For humans: {how this is traditionally organized}
- For agents: {how to organize it instead}
- Why: {the mechanism — token budget, retrieval, error recovery, trust, ...}
- Testable claim: {ONE measurable sentence: "Agents complete task X more
  accurately / with fewer tokens when data is organized as B instead of A"}
- Sources: {1–3 links}
```

The "Testable claim" line is what makes step 3 work — it hands the coding agent a hypothesis, not just a description.

### Question 3: The benchmark prompt

```
You are running a controlled experiment. The hypothesis: organizing data the
AGENT way (vs the traditional HUMAN way) improves agent task performance.
The technique to test is pasted at the end after "TECHNIQUE:".

1. SETUP. Generate a synthetic dataset with INVENTED entities, names, and
   numbers (so no agent can answer from world knowledge). Save two
   information-equivalent versions: ./human/ organized the traditional human
   way, and ./agent/ organized per the technique. Same facts in both — only
   the organization differs. Keep every file under 50 KB.
2. TASKS. Write 20 questions answerable ONLY from the data, each with one
   exact expected answer (a string or number a script can check). Mix easy,
   medium, and hard so neither version scores near 100% or 0%.
3. RUN. For each task × each version, launch a FRESH sub-agent with a clean
   context. Give it only: the question, and read access to that one folder.
   Same model and settings for both versions. Never show the sub-agent the
   technique description, the expected answer, or the other folder. Record:
   its answer, correct (normalized exact match), tokens used, tool calls.
4. SCORE. Grade with a deterministic script — no LLM judging. Compare
   accuracy with a paired sign test / McNemar and report the p-value. Also
   report median tokens and tool calls per version.
5. REPORT. Write RESULTS.md containing: the technique, the hypothesis, how
   the data was generated (include the generation script inline), both
   folder trees with sample files, all 20 tasks with expected answers, the
   exact sub-agent prompt verbatim, the raw results table, the statistics,
   and a conclusion (supported / not supported / inconclusive). Anyone
   should be able to reproduce the whole experiment from this one file.

Budget guard: stay under ~50 sub-agent calls total. If the technique can't
be tested this cheaply, scale it down and note that in RESULTS.md.

TECHNIQUE:
{paste one ### T{n} block from the research step here}
```

### Factors you haven't listed

Two are serious, the rest are worth a sentence in your intro:

1. **Information equivalence is the #1 confound.** If the agent-organized version quietly contains _more_ facts (say, added descriptions), you're testing data availability, not organization. The prompt forces "same facts, only organization differs," but participants should eyeball both folders before running. Worth saying out loud in the workshop.
2. **Be honest about statistical power.** 20 paired tasks with a sign test only detects _large_ effects (roughly a 30+ point accuracy gap). That's fine — you want "directional confidence you can share," not a paper. Say so, or someone will (rightly) challenge a p-value from n=20. If a participant's result is borderline, the fix is 30–40 tasks, not reruns.
3. **Ceiling effects kill more benchmarks than anything else.** If both versions score 19/20, the technique looks useless. The easy/medium/hard mix handles this, but tell participants: if you hit a ceiling, make the questions harder and rerun.
4. **Report tokens, not just accuracy.** Many agent-organization wins are equal accuracy at half the tokens. That's a real result — and it maps directly to your "token budget vs disk cost" framing.
5. **Tool parity.** Both sub-agents should get identical tools (read, grep, bash). Otherwise you're testing tooling, not data.
6. **ChatGPT Plus users can't easily run clean sub-agents** — that part needs Claude Code or Codex CLI. Your "optional, for coders" note may undersell this; step 3 realistically needs the CLI tools installed.

One asset suggestion: put both prompts plus an empty RESULTS.md template in a small public repo before the session, and have participants submit results as PRs. You'll walk away with a crowd-sourced mini-benchmark of data-organization techniques — reusable for VizChitra, the blog, and the next run of this workshop.

---

## User

Here's another answer from ChatGPT.

Fact-check and critically evaluate yours and theirs, take what's better, drop what's worse, explore any new thoughts this leads you to, and revise your response based on that.

I like your style of writing, so keep that.

<CHATGPT>

The useful organizing frame is not file type. It is the agent’s path: **discover → select → retrieve → interpret → act → observe → verify → recover → learn** Your current list covers the payloads. What is mostly missing is the **control plane around those payloads**. ## Question 1: What is missing? Prioritized by how frequently it determines agent success: 1. **Semantics and relationships** Data dictionaries, entity definitions, stable IDs, units, null meanings, valid ranges, candidate keys, cardinality, join evidence, dependencies, causal or temporal relationships, synonyms and domain vocabulary. Humans infer much of this from conventions, visual grouping and institutional knowledge. Agents need it made explicit. An agent may discover a join, but it should not have to guess whether it is one-to-one, historical, approximate or unsafe. 2. **Discovery and routing information** Catalogs, manifests, indexes, sitemaps, inventories, stable URIs, concise resource descriptions, aliases and “use this source when…” guidance. This may be the most distinctly agent-oriented layer. OpenAI describes replacing a monolithic manual with a small map pointing to deeper sources, while Anthropic recommends lightweight identifiers and just-in-time retrieval rather than loading everything into context. ([OpenAI][1]) 3. **Provenance, authority and time** Source, owner, lineage, citation, version, observed time, effective time, last verified time, freshness expectations, confidence, supersession and whether something is fact, estimate or opinion. An agent often sees several plausible answers simultaneously. It needs enough metadata to choose, reconcile or surface the disagreement rather than silently collapse it. Microsoft’s agentic retrieval guidance explicitly recommends citation fields and resource descriptions that help an agent decide whether to use an index. ([Microsoft Learn][2]) 4. **Contracts, constraints and side effects** Schemas, invariants, preconditions, postconditions, validation rules, permissions at the data boundary, destructive effects, idempotency, reversibility, latency, cost, quotas, pagination and retry semantics. This is larger than tool documentation. It includes database constraints, business rules, API contracts and operational limits. MCP, for example, provides hints for read-only, destructive, idempotent and open-world tools. ([Model Context Protocol][3]) 5. **State, events and change** Current snapshots, event streams, transactions, diffs, changelogs, tombstones, pending states, queues and distinctions such as requested versus started versus completed. A document usually describes what should happen. An operating agent needs to know **what has already happened, what changed and what remains uncertain**. 6. **Examples, fixtures and executable evidence** Valid examples, invalid examples, sample calls and responses, edge cases, counterexamples, tests, validators, expected outputs and known failure cases. Examples expose conventions that prose and schemas frequently omit. Anthropic recommends detailed tool descriptions, strict data models and examples for complex inputs; it also found that useful error messages can teach agents how to correct calls. ([Claude Platform Docs][4]) 7. **Feedback, outcomes and ground truth** Corrections, accepted and rejected outputs, reviewer comments, labels, user actions, downstream outcomes, quality scores, evaluation cases and adjudicated answers. These let an agent distinguish “the operation completed” from “the operation produced a useful result.” 8. **Observation surfaces** Queryable metrics, traces, screenshots, rendered previews, health checks, progress events and state inspection—not merely raw logs. OpenAI reports making application UI, logs, metrics and traces directly queryable by Codex so it can validate work and close its own feedback loop. ([OpenAI][1]) 9. **Access, sensitivity and governance metadata** Audience, ownership, confidentiality, licence, retention, residency, consent, redaction status and permissible transformations. This is data-level governance, distinct from agent-harness permissions. 10. **Machine-usable multimodal derivatives** OCR text with coordinates, transcripts with timestamps and speakers, image captions and regions, video chapters, table extraction, reading order and links back to the original pixels or frames. The derivative should not replace the original. Agents need both a cheap searchable representation and a route back to the source. ### A few hypotheses in the overview should be softened I would present these as questions to test, not conclusions: _ Not **“agents do not need clean, joined data”**, but: **preserve raw, versioned data and expose relationships clearly; avoid prematurely flattening everything into one canonical table.** _ Not **“tools beat tables”**, but: **tools beat bulk dumps when the agent needs bounded retrieval or action; tables remain excellent for inspection, filtering and batch computation.** _ Not **“logs beat docs”**, but: **docs explain intended behaviour; logs, metrics and tests reveal actual behaviour. Agents need both.** _ Not **“ambiguity may beat a single source of truth”**, but: **retain competing claims when appropriate, while making disagreement, provenance and confidence explicit.** _ Not **“optimize only for tokens”**, but: **optimize useful evidence per token, tool call, second and failure opportunity.** Long context alone is not a substitute for organization: models can use information unevenly depending on its position, while current agent systems increasingly use progressive disclosure, targeted queries and just-in-time retrieval. ([arXiv][5]) ## Factors to add to the benchmark design The most important additions are: 1. **Classify the intervention.** Is it reorganizing identical information, adding new information, or changing how information is accessed? Otherwise “better organization” may merely mean “more clues.” 2. **Use paired instances.** Each underlying synthetic world should generate both variants. This removes much of the variation between tasks. 3. **Blind the evaluator.** Evaluation agents should see condition `A` or `B`, not “human” versus “agent,” and should not receive the hypothesis. 4. **Prevent floor and ceiling effects.** Pilot first. If both variants score almost 0% or 100%, the benchmark cannot reveal much. 5. **Predeclare one primary metric.** Secondary metrics can include tokens, tool calls, latency, unsupported claims and recovery rate, but significance should be based on the declared primary metric. 6. **Prefer deterministic grading.** Exact answers, state checks and executable validators are better than an LLM judge. For open-ended tasks, combine coverage, groundedness and source-quality checks rather than one holistic score. ([Anthropic][6]) 7. **Use genuinely isolated runs.** Each evaluation should receive only its task and one variant. Anthropic’s subagents use separate context windows and return only selected results, which is the pattern to reproduce even when using another platform. ([Anthropic][7]) 8. **Measure the cost of the intervention.** An agent version that improves accuracy by 3% but consumes four times as many tokens may not be better. 9. **Keep execution deterministic.** Use local mock tools and fixed synthetic data instead of live websites or changing APIs unless freshness is the subject being tested. 10. **Limit the claim.** A 12–20-pair workshop experiment can provide useful evidence of a substantial effect on one model and task family. It does not establish a universal best practice. ## Question 2: Research and selection prompt This produces a comparable ranking plus self-contained technique cards that participants can paste into the experiment prompt. Research current best practices for organizing inputs for AI agents rather than humans. “Inputs” includes structured data, documents, code, media, folders and websites, schemas and taxonomies, tools and APIs, tool descriptions, tool results, errors, logs, metrics, traces and other observable system state. Exclude agent-harness artifacts such as prompts, AGENTS.md/CLAUDE.md, skills, memory systems, hooks, plugins and harness permissions. Use current primary sources wherever possible: engineering posts and documentation from leading AI companies, standards, research papers and published benchmarks. Include an internal company practice only when it is publicly documented. Distinguish measured evidence from expert opinion. Find at most 12 narrow, independently testable techniques. Rank them by: priority = expected effect × frequency of use × difference from human-oriented organization Use evidence strength and ease of running a small inexpensive benchmark as tie-breakers. First provide a compact ranked table with: Rank | Technique | Applies to | Typical human version | Agent-oriented version | Why it should help | Evidence strength | Ease of testing | Sources Then provide one copy-paste YAML card per technique: `yaml id: T01 name: applies_to: intervention_type: representation | augmentation | access human_baseline: agent_variant: mechanism: suitable_agent_task: minimal_ab_test: primary_metric: important_confounds: expected_result: evidence: - title: url: finding: confidence: high | medium | low` Make each technique specific enough to test in isolation. Prefer transformations such as progressive disclosure, explicit metadata, relationship descriptions, bounded retrieval tools or structured errors over broad advice such as “improve documentation.” Do not recommend a technique merely because it sounds machine-readable; explain why it changes agent behaviour. ## Question 3: Build-and-run benchmark prompt Run a small, controlled and reproducible A/B benchmark of the technique pasted below. Do not merely design the benchmark: create it, execute it, analyze it and write the final report. Do not ask me questions; make reasonable choices and document them. <TECHNIQUE> PASTE ONE YAML TECHNIQUE CARD HERE </TECHNIQUE> Use this protocol: 1. Define a concrete hypothesis and one primary success metric before running the main experiment. Classify the intervention as representation, augmentation or access. 2. Generate a canonical synthetic dataset with fixed random seeds and known answers. Produce two conditions: _ A: the conventional human-oriented organization _ B: the agent-oriented technique Keep the underlying facts identical for representation or access interventions. If the technique intentionally adds information, state exactly what was added rather than claiming equal information. 3. Create three pilot task pairs. Adjust difficulty until the baseline is neither trivial nor impossible; aim roughly for 20–80% success. Do not include pilot results in the final test. 4. Run 12 paired task instances across at least three difficulty levels. Extend to at most 20 pairs only if the predeclared stopping rule says the result is inconclusive. Hard limit: 40 evaluation-agent runs. 5. Run every evaluation in a fresh isolated context using the same model, configuration, tools, maximum steps and output budget. Prefer the platform’s isolated subagent/task mechanism; otherwise launch separate non-interactive CLI processes. Never evaluate inside this parent conversation. _ Give each evaluator only its task and one condition. _ Do not reveal the hypothesis, technique, other condition, gold answers or previous runs. _ Use separate temporary working directories containing only permitted files. _ Disable cross-run memory. _ Randomize condition labels and run order; unblind only after scoring. _ Record the exact model and isolation method actually used. 6. Keep the experiment inexpensive: _ Prefer a fast, capable model. _ Keep each input and answer compact. _ Use deterministic local mock tools rather than network services. _ Use the lowest available randomness and record any settings that cannot be controlled. 7. Grade automatically wherever possible using exact answers, executable validators or final environment state. Use a blinded LLM judge only when unavoidable, with an explicit rubric. Record: _ primary task score _ complete success rate _ input size or estimated tokens _ output tokens where available _ tool calls or steps _ latency and cost where available _ errors and unsupported claims 8. Analyze paired differences. Report the absolute and relative effect, a 95% bootstrap confidence interval, and an exact paired permutation test or McNemar/binomial test for binary outcomes. Base the significance claim only on the predeclared primary metric. Report the result as supports, weakly supports, inconclusive or contradicts the hypothesis; do not overgeneralize beyond this model and task family. Create `RESULTS.md` as the sole shareable artifact. It must contain: _ the original technique card _ hypothesis and preregistered protocol _ exact model, configuration and isolation method _ canonical data design and both transformations _ evaluator prompt and grading rules _ pilot decisions _ complete raw results table _ statistical analysis _ token/cost-efficiency comparison _ failure analysis with representative examples _ conclusion and limitations _ exact reproduction commands _ all generator, runner, grader and analysis code in fenced blocks The Markdown file alone must contain enough information to recreate every generated file and rerun the benchmark. Prefer one embedded Python program using the standard library; when dependencies are needed, declare them inline so it can be run with `uv run`. For the workshop, **12 paired instances with a predeclared extension to 20** is a better default than demanding significance regardless of cost. It can detect a strong, consistent effect while keeping the benchmark small enough for each participant to test more than one technique. [1]:_ [https://openai.com/index/harness-engineering/](https://openai.com/index/harness-engineering/)
"Harness engineering: leveraging Codex in an agent-first world | OpenAI" [2]:_ [https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-create-index](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-create-index)
"Create an Index for Agentic Retrieval - Azure AI Search | Microsoft Learn" [3]:_ [https://modelcontextprotocol.io/specification/2025-06-18/schema?utm_source=chatgpt.com](https://modelcontextprotocol.io/specification/2025-06-18/schema?utm_source=chatgpt.com)
"Schema Reference" [4]:_ [https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use?utm_source=chatgpt.com](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use?utm_source=chatgpt.com)
"Define tools - Claude Platform Docs" [5]:_ [https://arxiv.org/abs/2307.03172?utm_source=chatgpt.com](https://arxiv.org/abs/2307.03172?utm_source=chatgpt.com)
"Lost in the Middle: How Language Models Use Long Contexts" [6]:_ [https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
"Demystifying evals for AI agents \ Anthropic" [7]:_ [https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
"Building agents with the Claude Agent SDK | Claude by Anthropic"

</CHATGPT>

---

## Claude

<details>
<summary>Synthesized competing frameworks, verified claims empirically, merged approaches strategically</summary>

> I need to verify the sources both answers cite—checking whether OpenAI's post on harness engineering and Anthropic's pieces on evals and subagents actually exist—then decide which answer is stronger overall and revise accordingly, keeping the language accessible.
>
> ChatGPT's framing of an agent's journey through stages is genuinely useful and maps well to Anand's existing six-point checklist, though nine stages feels redundant. The "intervention type" breakdown—representation, augmentation, access—is the sharpest contribution here and clarifies what I was calling information equivalence. I notice ChatGPT is partly re-deriving Anand's own framework rather than adding something entirely new, which is worth acknowledging.
>
> The methodological suggestions are solid: blinding conditions as A/B rather than human/agent, a pilot phase to calibrate difficulty, predeclared primary metrics with stopping rules. The YAML card format adds structure but at the cost of bulk—15 fields will likely produce inconsistent, bloated submissions across participants, whereas my ~120-word markdown card is easier to compare across agents, which matters since Anand wants cross-agent comparison. I should steal the "intervention_type" and "primary_metric" fields though.
>
> On the statistical side, 12 paired instances is quite weak for binary outcomes; even with the extension to 20, that's borderline for detecting real effects. The bootstrap CI and permutation test are reasonable but maybe overkill for a workshop setting where a sign test would be simpler and more transparent about power limitations.
>
> ChatGPT's weaknesses: the benchmark prompt is verbose—a wall of text to copy-paste when conciseness was requested. The YAML card will invite hallucination on fields like "important_confounds" and "evidence.finding." The ranked table plus cards feels duplicative, though I see the value now—Anand's workflow is "run across multiple agents and compare," so a compact ranked table actually helps with that comparison. Maybe the table becomes the comparison artifact and the cards stay as the test artifact, but I should slim the card down. Some citations have utm tracking junk, and the Q1 list overlaps with mine rather than adding much new.
>
> ChatGPT dropped some things I included that are worth keeping: negative knowledge (deprecations, gotchas), communication exhaust, ownership/escalation, and the nouns-versus-processes distinction (runbooks). My biggest miss was no intervention classification—representation, augmentation, access—and I didn't blind condition labels or include a pilot phase. ChatGPT allows blinded LLM judges when unavoidable, which is more practical than my hard "no LLM grading" stance. I also didn't cite sources like ChatGPT did, and I should verify that OpenAI harness engineering post claim. Let me search for those references and check if there are newer evals posts I'm missing. Now I'll run some searches to verify the key claims before finalizing the response.
>
> OpenAI harness engineering Codex agent-first world
>
> 10 results
>
> - [GitHub - walkinglabs/awesome-harness-engineering: 🛠️ Awesome tools & guides for harness engineering.](https://github.com/walkinglabs/awesome-harness-engineering) - github.com
> - [[Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://openai.com/index/harness-engineering/)](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html) - jessetomchak.com
> - [Natural-Language Agent Harnesses](https://arxiv.org/pdf/2603.25723) - arxiv.org
> - [OpenAI’s Harness Engineering Post Is a Blueprint for the Agent-First Era | by ADITHYA GIRIDHARAN | Medium](https://medium.com/@AdithyaGiridharan/openais-harness-engineering-post-is-a-blueprint-for-the-agent-first-era-d9932851dcee) - medium.com
> - [Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://openai.com/index/harness-engineering/) - openai.com
> - [From Model Scaling to System Scaling: Scaling the Harness in Agentic AI](https://arxiv.org/pdf/2605.26112) - arxiv.org
> - [OpenAI's Agent-First Codebase Learnings | Blog](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/) - alexlavaee.me
> - [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/pdf/2602.12670) - arxiv.org
> - [OpenAI Introduces Harness Engineering: Codex Agents Power Large‑Scale Software Development - InfoQ](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex/) - www.infoq.com
> - [The Last Harness You'll Ever Build](https://arxiv.org/pdf/2604.21003) - arxiv.org
>   The OpenAI harness engineering post from February 2026 by Ryan Lopopolo checks out—the key points about environment legibility bottlenecks, documentation structure, mechanical enforcement, and queryable observability all align with what ChatGPT cited. Now I'm verifying the Anthropic "Demystifying evals for AI agents" post and checking the current status of llms.txt evidence.
>
> llms.txt adoption evidence do AI agents actually use it
>
> 10 results
>
> - [llms.txt and AI Visibility: Results from OtterlyAI's GEO Study](https://otterly.ai/blog/the-llms-txt-experiment/) - otterly.ai
> - [llms.txt: What It Does and How It Fits Into AI Search Optimization | Stellar AEO Labs](https://stellar-ai.co/blog/llms-txt-ai-search-optimization/) - stellar-ai.co
> - [The value of llms.txt: Hype or real?](https://www.mintlify.com/blog/the-value-of-llms-txt-hype-or-real) - www.mintlify.com
> - [Debunking LLMs.txt Myths: What You Need to Know for AI Visibility](https://www.wix.com/studio/ai-search-lab/llms-txt-myths) - www.wix.com
> - [The Complete Guide to llms.txt: Should You Care About This AI Standard?](https://getpublii.com/blog/llms-txt-complete-guide.html) - getpublii.com
> - [LLMs.txt: Why Brands Rely On It and Why It Doesn’t Work](https://seranking.com/blog/llms-txt/) - seranking.com
> - [LLMs.txt in 2026: The Full Guide](https://limy.ai/blog/llms.txt-in-2026-the-full-guide) - limy.ai
> - [Do llms.txt files actually improve AI search visibility? | Contentful](https://www.contentful.com/blog/llms-txt-search-visibility/) - www.contentful.com
> - [Does anyone actually have an llms.txt? I checked millions of websites · Casey Burridge](https://caseyrb.com/blog/state-of-llms-txt-adoption/) - caseyrb.com
> - [The Adoption and Usage of AI Agents: Early Evidence from Perplexity](https://arxiv.org/pdf/2512.07828) - arxiv.org
>   The llms.txt case is interesting because it's the canonical example of agent-ready data, yet the actual evidence of adoption is surprisingly thin. This is a valuable teaching moment about not relying on intuition—we need to verify claims with real benchmarks. I'm also tracking down the OpenAI harness engineering post from February 2026 by Ryan Lopopolo to verify those ChatGPT claims. I'm mapping the taxonomy onto Anand's checklist to avoid duplication, merging in the elements both responses cover—negative knowledge, communication exhaust, processes, multimodal derivatives, observation surfaces, contracts, and feedback loops. For Q2, I'll stick with the markdown card format since it renders better in chat and is easier to copy-paste, but add intervention type and evidence strength fields. For Q3, I'm blending both approaches—keeping mine concise but folding in ChatGPT's additions like pilot phases, blinding, predeclared metrics, and stopping rules without bloating it too much. I'll deduplicate the factors list and keep the repo/PR suggestion with a note about ChatGPT Plus limitations.
>
> Done

</details>

I checked ChatGPT's sources. They hold up. The OpenAI "harness engineering" post is real (Feb 2026) and says what ChatGPT claims: the biggest bottleneck isn't model capability but environment legibility — agents fail when they can't find or reason about the information they need, and internal docs act as the single source of truth for agents, with cross-linked design docs mechanically enforced by linters and CI. "Lost in the Middle" is a real 2023 paper. The MCP tool hints (read-only, destructive, idempotent) are real. No fabricated citations that I can find. [Alexlavaee](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/)[InfoQ](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex/)

So here's my honest scoring, then the revised answer.

**Where ChatGPT beat me:**

1. **Classifying the intervention** (representation vs augmentation vs access) is the single best idea in either answer. It turns my vague "information equivalence" warning into a rule participants can apply. Steal it.
2. **Blinding the labels** (call the folders A and B, not "human" and "agent") — I missed this. A sub-agent that sees a folder named `agent-optimized` may try harder.
3. **A pilot phase** to tune difficulty is better than my "if you hit a ceiling, rerun."
4. **Predeclaring one primary metric** stops p-hacking across accuracy, tokens, and tool calls.
5. Its Q1 adds real items I missed: observation surfaces (queryable metrics, not raw logs), contracts and side effects, and multimodal derivatives (OCR with coordinates, transcripts with timestamps).

**Where mine was better:**

1. **Card format.** ChatGPT's 15-field YAML card is too heavy. Agents will fill fields like `important_confounds` with filler, and your participants need to _compare cards across ChatGPT and Claude_ — short markdown cards compare in seconds, YAML walls don't. Keep the compact card, add two fields from theirs.
2. **Concision.** Its benchmark protocol is rigorous but reads like a pre-registration form. In a 4-hour workshop, a prompt participants can skim and trust matters.
3. It **dropped things worth keeping**: negative knowledge (deprecations, gotchas — humans learn these socially, agents only if written), communication exhaust (Slack, tickets, PR comments), and my "your list is all nouns" point — runbooks and checklists are data too.
4. Its "agent's path" frame (discover → select → retrieve → ...) is nice, but notice: **it's your own checklist from the overview**, re-derived and stretched to nine steps. You already have the frame. Use yours.

**A new thought this comparison triggered:** llms.txt — the poster child of "data for agents" — has weak evidence of actual use. A SE Ranking study of 300,000 domains found only ~10% adoption after eighteen months, Google says its AI features rely on traditional signals instead, and SEO logs show GPTBot fetches llms.txt only rarely — while Anthropic asked Mintlify to implement it and crawl data shows some models do fetch these files. The evidence is genuinely contested. That's a gift for your workshop: the most famous "agent data" technique is exactly the kind of claim your step-3 benchmark exists to test. Say this out loud — it motivates the whole afternoon. [Limy + 2](https://limy.ai/blog/llms.txt-in-2026-the-full-guide)

---

### Question 1 (revised): What's missing

Your list covers the _payloads_. What's missing is mostly the _layer around them_ that lets an agent trust and navigate them. Ranked by how often it decides agent success, mapped to your own checklist (discover, understand, retrieve, call, trust, recover):

1. **Semantics: metadata, dictionaries, relationships** _(understand)_ — column meanings, units, what null means, stable IDs, join keys and whether a join is safe, synonyms. A human asks a colleague what `amt_usd_adj` means. An agent can't.
2. **Discovery and routing** _(discover)_ — catalogs, manifests, indexes, sitemaps, llms.txt, "use this source when..." notes. A small map beats a big manual. (And per above: benchmark it, don't assume it.)
3. **Provenance, freshness, and authority** _(trust)_ — source, owner, version, last-verified date, fact vs estimate. When an agent sees two plausible answers, this is how it picks — or knows to surface the conflict instead of silently choosing.
4. **Examples and golden records** _(call, understand)_ — sample queries with correct answers, valid _and invalid_ examples, fixtures. Agents pattern-match on examples faster than they parse specs.
5. **Verification artifacts and ground truth** _(recover)_ — tests, validators, checksums, expected outputs, accepted/rejected past outputs. How an agent tells "the operation ran" from "the result is right."
6. **Contracts and side effects** _(call, recover)_ — preconditions, idempotency, what's destructive and reversible, rate limits, cost per call. MCP's read-only/destructive hints are one formalization.
7. **Change history** _(understand, trust)_ — changelogs, diffs, git history, tombstones. Commit messages are docs humans wrote that agents mine heavily.
8. **Negative knowledge** — deprecations, known bugs, gotchas, "don't do this." Humans learn these over coffee; agents only know what's written down.
9. **Observation surfaces** _(recover)_ — queryable metrics, traces, screenshots, health checks — not just raw log files. OpenAI made its app's telemetry directly queryable so Codex could validate its own work.
10. **Communication exhaust** — Slack threads, tickets, PR reviews, transcripts. Written for humans, increasingly agent food.
11. **Multimodal derivatives** — OCR with coordinates, transcripts with timestamps and speakers, table extractions, each linking back to the original. Agents need both the cheap searchable form and the route to the source.
12. **Processes as data** — runbooks, SOPs, checklists. Your list is all nouns; agents also consume verbs. (Your "functions become checklists" line belongs in the taxonomy, not just the pitch.)

On ChatGPT's advice to soften your overview hypotheses: half right. Your phrasing already hedges ("we might not need..."), and provocative hypotheses are good workshop marketing — they're what step 3 will test. But do steal one reframe as your closing line: don't optimize tokens, **optimize useful evidence per token**.

### Question 2 (revised): The research prompt

Changes from my first version: a compact ranked table first (so participants can compare across ChatGPT/Claude at a glance), plus two fields stolen from ChatGPT — intervention type and evidence strength.

```
Research current (2025–2026) best practices for organizing data for AI AGENTS
to consume, as opposed to humans. "Data" includes: structured data (tables,
JSON, schemas), documents (markdown, PDFs, web pages), code, media, folder
and site organization, tool definitions and docs, tool outputs, errors, logs,
metrics, and traces. EXCLUDE agent-harness artifacts (system prompts,
AGENTS.md, SKILL.md, memory, permissions, hooks).

Search the web. Prefer primary sources: engineering blogs and docs from
Anthropic, OpenAI, Google, and similar; standards (e.g., MCP, llms.txt);
papers and benchmarks; practitioners who prepare data or APIs for agents.
Mark clearly what is MEASURED evidence vs expert OPINION.

Return the TOP 10 techniques, ranked by:
(impact × how often the situation occurs) × (how DIFFERENTLY you would do it
for agents vs humans). Skip anything where the human and agent way match.

First, one compact ranked table:
Rank | Technique | For humans | For agents | Evidence: measured/opinion

Then one card per technique, EXACTLY this format — self-contained, under
120 words, no cross-references, so each card can be copy-pasted alone:

### T{n}. {Short technique name}
- Type: representation (same facts, reorganized) | augmentation (adds info)
  | access (changes how it's fetched)
- For humans: {traditional organization}
- For agents: {organize it this way instead}
- Why: {mechanism — token budget, retrieval, trust, error recovery, ...}
- Testable claim: {ONE measurable sentence: "Agents do task X more
  accurately / with fewer tokens when data is B instead of A"}
- Evidence: {measured | opinion} — {1–3 links}
```

### Question 3 (revised): The benchmark prompt

Merged: my structure and length, plus ChatGPT's pilot phase, blinded labels, intervention classification, predeclared metric, and "don't ask me questions."

```
Run a small, controlled A/B experiment testing the data-organization
technique pasted at the end after "TECHNIQUE:". Build it, run it, analyze
it, and write the report. Don't ask me questions — make sensible choices
and document them.

1. HYPOTHESIS. State one testable hypothesis and ONE primary metric
   (usually accuracy) before running anything. Note the technique's Type:
   if "representation" or "access", both versions MUST contain identical
   facts — only organization differs. If "augmentation", state exactly
   what information was added.
2. SETUP. Generate a synthetic dataset with INVENTED names and numbers (so
   nothing is answerable from world knowledge). Save two versions from the
   same generator with a fixed seed: ./A/ and ./B/ (randomly assign which
   is human-style, which is agent-style; record the mapping but never show
   it to sub-agents). Files under 50 KB.
3. PILOT. Write 3 trial questions and run them once per version. If scores
   are near 0% or 100%, adjust difficulty. Discard pilot results.
4. TASKS. Write 20 questions answerable ONLY from the data, each with one
   exact expected answer a script can check. Mix easy, medium, hard.
5. RUN. For each task × version, launch a FRESH sub-agent (clean context —
   Task tool or a separate non-interactive CLI process, never this
   conversation). It gets ONLY the question and read access to one folder,
   with identical tools (read, grep, bash), model, and settings. Never
   reveal the hypothesis, the technique, the expected answer, or the other
   folder. Record: answer, tokens, tool calls.
6. SCORE. Grade with a deterministic script (normalized exact match — no
   LLM judging). Compare accuracy with a paired sign test / McNemar and
   report the p-value. Report median tokens and tool calls as secondary.
7. REPORT. Write RESULTS.md: the technique card, hypothesis, exact model
   and isolation method used, how data was generated (generator script
   inline, runnable via `uv run` with inline deps), both folder trees with
   samples, all 20 tasks + expected answers, the sub-agent prompt verbatim,
   raw results table, statistics, and a conclusion: supports / weakly
   supports / inconclusive / contradicts — for this model and task family
   only. This one file must be enough to reproduce everything.

Budget guard: stay under ~50 sub-agent calls total. If the technique can't
be tested this cheaply, scale down and say so in RESULTS.md.

TECHNIQUE:
{paste one ### T{n} card here}
```

### Factors beyond your list (merged, deduped)

1. **Information equivalence is the #1 confound** — now enforced by the Type field, but tell participants to eyeball both folders before running. "Better organized" often smuggles in "more information."
2. **Be honest about power.** 20 paired tasks detects only large effects (roughly 25–30+ point gaps). That's fine — say "directional confidence, one model, one task family," and no one can ambush you with the p-value. ChatGPT's 12-pairs-extend-to-20 rule is clever but adds moving parts; a flat 20 is simpler for a room of 40 people.
3. **Ceiling and floor effects** — handled by the pilot. If both versions ace it, the workshop "learns" the technique is useless when the test was just too easy.
4. **Report tokens, not just accuracy.** Equal accuracy at half the tokens is a win — and it's literally your workshop's thesis.
5. **Blind the labels** (A/B folders). Cheap insurance against sub-agents playing to the hypothesis.
6. **Determinism**: fixed seeds, local files, no live websites — unless freshness is the thing being tested.
7. **ChatGPT Plus users can't run clean sub-agents easily.** Step 3 realistically needs Claude Code or Codex CLI. Your "optional, for coders" note undersells this — consider making one CLI tool a soft requirement, or pre-pairing non-coders with coders.

One asset suggestion, unchanged and now stronger: put the two prompts plus a RESULTS.md template in a public repo before the session and collect results as PRs. Forty participants × 1–3 techniques is a crowd-sourced mini-benchmark of agent-data practices — including, possibly, the first workshop-grade test of whether llms.txt actually earns its hype. That's a blog post, a VizChitra exhibit, and the opening slide of this workshop's next run.

---

## User

"Files under 50KB" might be too narrow a limit. How do we ensure that the files are sized and organized so that it will produce the most useful differentiation between A/ and B/?

Also, for synthetic data generation, I thought I'd point it to this skill - just by adding "Generate a synthetic dataset (see [https://raw.githubusercontent.com/sanand0/scripts/refs/heads/main/agents/generate-fake-data/SKILL.md](https://raw.githubusercontent.com/sanand0/scripts/refs/heads/main/agents/generate-fake-data/SKILL.md)) with ..." - but what do you think?

Along similar lines, any other revisions to the benchmark prompt? When you look at it strategically from a expert-lens what experiment design flaws do you see given my objective?

Revise and share the prompt based on these.

---

## Claude

<details>
<summary>Architected benchmark design with corpus scaling, condition differentiation, and experimental safeguards</summary>

> Anand is asking about three things: how to size the data files so they meaningfully differentiate between the two conditions, whether to reference his fake data generation skill in the prompt, and a critical review of the experiment design itself to identify and fix any flaws. I should look at his skill documentation first to understand what he's working with, then think through the core issue—that the differentiation between A and B really hinges on having enough data to make the comparison meaningful.
>
> The key realization is that if the dataset is small enough to read all at once, organization doesn't matter—both conditions perform identically because the agent just ingests everything. The real constraint isn't file size limits but rather making the total corpus large enough that a naive read-everything approach becomes prohibitively expensive, forcing the agent to actually navigate and retrieve. The design variable is the ratio of total corpus size to what each task actually needs—ideally 10-50x larger so organization effects emerge. File organization itself is often the technique being tested, so the prompt shouldn't prescribe it; instead, set a total corpus budget and let the condition define the structure. I should also note that scale needs to be calibrated in a pilot run—if both conditions score the same, increase the corpus size and distractor volume until they separate, but be careful not to p-hack by tuning until an effect appears. Better approach: predeclare the scale upfront, pilot for difficulty, and report it transparently.
>
> For distractors, the real power comes from near-misses—similar names, outdated versions, conflicting values with timestamps—where good organization actually pays off. On the skill URL approach, it's generally sound and reusable, but there are practical concerns: sub-agents won't see it (fine), fetching mid-prompt requires web access (Claude Code can handle it, but Codex may have sandbox restrictions, so a fallback to generate synthetic data with fixed seeds is wise), and there's a risk that realistic fake data could introduce world-knowledge contamination—though actually Faker-generated data is fine for that since the combinations are random. The real question is whether the skill supports relational structure and ground-truth answers, so I should check it directly.
>
> Looking at the expert-level flaws: the biggest issue is the scale confound—if the corpus is too small, both conditions score the same and the result looks inconclusive for the wrong reason. The fix is predeclaring corpus scale, including distractors, and designing tasks that require lookup rather than full reads. The second major flaw is that the parent agent generates both conditions _and_ the tasks while knowing the hypothesis, which creates a risk of unconscious bias—it might write tasks that favor condition B or construct a strawman version of A that's artificially weak.
>
> To address this, I should generate the human baseline first as "how a realistic team would actually organize this," then derive condition B by applying the technique—never degrade A. Alternatively, tasks could be generated from canonical ground-truth facts independent of either representation. I could also include a strawman check in the results by describing condition A and asking whether a real team would recognize it as normal practice. A third concern is relying on a single dataset instance; ideally there'd be 2-3 generated worlds to rule out quirks, though that's budget-limited. There's also the risk of task-technique misalignment: if all tasks are retrieval lookups, techniques about error recovery won't show. The tasks need to match the technique's testable claim, but I should also include some off-target tasks—maybe 15 on-target and 5 off-target—to check whether the technique actually helps or just happens to shine on its designed use case. Finally, stronger models with grep and bash can overcome poor organization, so the effect size will shrink with model capability, which I should report.
>
> Using a cheaper, faster model like Haiku as the sub-agent would actually differentiate more and cost less, though I'd need to predeclare that the claim is "for weaker models." I should also keep token accounting as a secondary metric—approximating via tool-result bytes is fine. For fairness, the sub-agent prompt must be identical across conditions; if condition B includes an index file, I can't tell the agent to "start with INDEX.md"—discovery has to be intrinsic to the data structure itself. The grading approach of normalized exact match is solid, and the sign test with n=20 is already handled. I'm also revising the file limit guidance: instead of "files under 50KB," I'll frame it corpus-level—total around 0.5–2MB with each task's answer needing less than 1-2% of it, plus distractors—and let the technique dictate file granularity. Now I need to pull the skill file.
>
> - [https://raw.githubusercontent.com/sanand0/scripts/refs/heads/main/agents/generate-fake-data/SKILL.md](https://raw.githubusercontent.com/sanand0/scripts/refs/heads/main/agents/generate-fake-data/SKILL.md) - raw.githubusercontent.com
>   The skill was built for demo scenarios with compelling narratives and surprising insights, but that's fundamentally misaligned with benchmark requirements, which demand precise, verifiable facts with clear right answers and plausible distractors. Steps like hypothesis research and critical review consume tokens and budget without contributing to benchmark performance.
>
> Using real names for people and products introduces contamination risk — an agent could exploit world knowledge to guess answers rather than reasoning through the data. The better approach is to fork this into a dedicated benchmark generator that emits three synchronized outputs from a single seed: a canonical answer key in JSON, plus two distinct conditions that both derive from that ground truth. This structural design prevents the bias where the task creator unconsciously favors one condition over another.
>
> For corpus organization, the real constraint isn't individual file size but total corpus scale relative to task difficulty — aim for 50–100× larger than what a single task requires, roughly 200k–500k tokens spread across many files, so agents can't simply read everything in a few calls and collapse the differentiation between conditions.
>
> The key design flaws to fix: prevent experimenter bias by generating canonical facts first, then building condition A as a realistic human-created structure and deriving condition B from applying the technique, with tasks derived only from the canonical facts; scale the haystack aggressively during piloting if both conditions perform too well; and use cheaper, slower sub-agents like Haiku-class models instead of powerful ones, since strong agents with grep can brute-force past organizational differences — the real test needs the organization to matter.
>
> I also need to add off-target tasks (5 out of 20) to catch unintended harms, cap sub-agent steps at something like 15 tool calls to prevent wandering and control costs, and ensure the sub-agent prompt is identical between conditions with only the file paths differing — no hints about the technique. For the synthetic world quirk, I'll at least note it as a limitation and optionally run 2 seeds with 10 tasks each if budget allows. On timing, running 40 trials sequentially at 30–60 seconds each could take 40 minutes, so I should parallelize the sub-agent calls where possible.
>
> For the revised prompt itself, I'm going to inline the benchmark generation instructions directly rather than linking to an external skill — keeps it self-contained for reproducibility and avoids network dependency issues in sandboxed environments. I'll extract three key ideas from the existing demo (seeded causal simulation, messy realism as camouflage, generator script) and bake them into the prompt. The structure will include predeclared hypothesis type and primary metric, a ground truth section with canonical facts and the generator logic, clear condition definitions (A = baseline human org, B = with technique), a corpus scale rule capping each task at under 1% of the total budget, a pilot phase to calibrate difficulty, and the task set split between on-target and off-target questions with exact answers.
>
> For execution, I'm running fresh sub-agents with a cheap fast model, capping tool calls around 15 with parallelization allowed, and recording answer, token count or proxy, tool calls, and whether the cap was hit. Scoring uses deterministic methods like sign test or McNemar with secondary metrics, and the report follows a RESULTS.md spec that flags limitations. The whole thing runs on roughly 50 sub-agent calls within budget.
>
> Done

</details>

### The file size question — you've spotted a real flaw

The 50KB limit was solving the wrong problem. Here's the principle:

**Organization only matters when reading everything is too expensive.** If the whole corpus fits in a few tool calls, the sub-agent just swallows the haystack, and A and B score the same — you get a null result by construction, and the workshop "learns" that data organization doesn't matter. The differentiation between A and B lives in the _gap between what a task needs and what the corpus contains_.

So the constraints should be:

1. **Budget the total corpus, not individual files.** Roughly 200k–500k tokens of text (about 1–2 MB), spread across dozens of files or records. Big enough that "read it all" blows the step budget; small enough to generate and run cheaply.
2. **Each task should need under ~1% of the corpus.** The agent must _find_, not ingest.
3. **Plant distractors.** Near-miss entities, stale versions, conflicting values with different dates. Finding the needle among look-alikes is exactly where organization pays off.
4. **Don't constrain file granularity at all.** One giant CSV vs many small files with an index is often _the technique being tested_. A per-file limit quietly forbids condition A from being what humans actually do.
5. **Cap the sub-agent's steps instead** (say, 15 tool calls). That's what protects context and cost — and it's realistic, since real agents have budgets. "Hit the cap" counts as failure.

### Your skill link — I'd say no, and here's why

I read the skill. It's excellent for what it's for — demo data that makes a client go "wow." But that's a different objective from benchmark data, and three things clash:

1. It spends Steps 1 and 4 hunting counter-intuitive business hypotheses and passing a cynical-reviewer check. For a benchmark, that's tokens and minutes spent on realism theatre nobody will inspect — straight out of your $20 budget.
2. It insists on **real names** for people, places, and products. Your benchmark needs the opposite: invented entities, so nothing is answerable from world knowledge.
3. It optimizes for _insight-rich_ data (surprising correlations, standout entities). You need _fact-dense_ data with an exact answer key.

Three ideas from it are worth stealing inline: seeded causal simulation (entities with hidden traits interacting — great for multi-hop questions), messy realism as camouflage for the planted facts, and shipping the generator script for reproducibility. I've folded those in.

There's also a practical reason to inline rather than link: Codex sandboxes may block the fetch, and your own requirement is that RESULTS.md alone reproduces everything — an external URL breaks that. Separately, fork the skill into a `generate-benchmark-data` SKILL.md for your library. Same bones, different goal: camouflage instead of wow, answer key instead of insights. That's a reusable asset this workshop leaves behind.

### Expert-lens: the design flaws that remain

Given your objective — results credible enough to share publicly, cheap enough for a $20 plan — the threats in rough order of damage:

1. **The parent agent is judge, jury, and defendant.** It knows the hypothesis, then writes the baseline, the treatment, _and_ the questions. It can strawman A (build a lazy "human" version) or write B-flavored questions without meaning to. This is the flaw a skeptic at Fifth Elephant will hit first. Fix structurally: generate **canonical facts first** (a ground-truth JSON), build A as "how a competent team actually stores this today," derive B by applying the technique to A, and derive tasks **from the canonical facts only** — never from either folder. Plus a no-strawman rule: A must be an organization a real team would defend.
2. **Strong sub-agents erase the effect.** A frontier model with grep will brute-force any layout. Use a fast, cheap model (Haiku-class) for sub-agents — you get bigger differentiation _and_ it fits the budget. Predeclare it and scope the claim to that model.
3. **All-on-target tasks turn the test into a demo.** Twenty questions crafted to the technique's exact strength measures its best case. Add 5 off-target tasks — ordinary questions the technique wasn't built for — to catch cases where the reorganization _hurts_ everything else. That "cost of the intervention" number is often the most interesting result.
4. **One synthetic world is one sample.** A quirk of the generated world can drive the whole result. The full fix (multiple worlds) blows the budget, so name it as a limitation in RESULTS.md. Participants with budget left can rerun with a second seed.
5. **Prompt leakage through the sub-agent instructions.** If the sub-agent prompt says "check the index first," you've smuggled the technique into the harness. The sub-agent prompt must be identical, verbatim, across conditions — only the folder path changes. Discovery has to live in the data.
6. **Token counts may not be visible per sub-agent.** Use a proxy: bytes of tool results returned plus tool-call count. Crude but comparable across conditions.
7. **Workshop clock.** 40 sequential runs at ~30–60 seconds each is most of an hour. Tell the agent to run sub-agents in parallel batches.

### The revised prompt

```
Run a small, controlled A/B experiment testing the data-organization
technique pasted at the end after "TECHNIQUE:". Build it, run it, analyze
it, and write the report. Don't ask me questions — make sensible choices
and document them.

1. HYPOTHESIS. State one testable hypothesis and ONE primary metric
   (usually accuracy). Note the technique's Type: if "representation" or
   "access", both conditions MUST contain identical facts — only the
   organization differs. If "augmentation", state exactly what was added.

2. GROUND TRUTH. Write a seed-fixed generator script that simulates
   entities with hidden traits interacting over time (a small causal
   simulation), using INVENTED names and numbers so nothing is answerable
   from world knowledge. It must output canonical-facts.json: every fact,
   with its answer. Make the data messy and realistic — noise, near-miss
   entities, stale versions, conflicting values with dates — so finding
   the right fact takes work.

3. CONDITIONS. From the canonical facts, build two folders, ./A/ and ./B/
   (randomly assign which is which; record the mapping, never reveal it
   to sub-agents):
   - Human condition: how a competent team would actually store this
     today. No strawman — a real team should defend it as normal.
   - Agent condition: apply the technique to the human condition.
   Scale: 200k–500k tokens of text total per condition, spread across
   many files or records. Any task should need under 1% of the corpus.
   No per-file size limits — let each condition organize files the way
   that condition naturally would.

4. TASKS. From canonical-facts.json ONLY (never from the folders), write
   20 questions, each with one exact expected answer a script can check:
   15 on-target (the situations the technique targets) and 5 off-target
   (ordinary questions it wasn't built for). Mix easy, medium, hard.

5. PILOT. Run 3 trial questions once per condition. If both conditions
   score near 0% or 100%, adjust difficulty or grow the corpus and
   distractors, then discard pilot results.

6. RUN. For each task × condition, launch a FRESH sub-agent with a clean
   context (Task tool or a separate non-interactive CLI process — never
   this conversation), using a fast, cheap model. Run in parallel batches.
   Every sub-agent gets the SAME verbatim prompt — only the folder path
   differs — with the question, read access to one folder, identical
   tools (read, grep, bash), and a cap of 15 tool calls (hitting the cap
   = failure). Never reveal the hypothesis, the technique, the expected
   answer, or the other folder. Record: answer, tool calls, bytes of tool
   results (as a token proxy), and whether the cap was hit.

7. SCORE. Grade with a deterministic script (normalized exact match — no
   LLM judging). Compare accuracy with a paired sign test / McNemar and
   report the p-value, on-target and off-target separately. Report median
   tool calls and result-bytes as secondary metrics.

8. REPORT. Write RESULTS.md: the technique card, hypothesis, exact models
   and isolation method used, the generator script inline (runnable via
   `uv run` with inline deps, fixed seed), both folder trees with sample
   files, all 20 tasks + expected answers, the sub-agent prompt verbatim,
   raw results table, statistics, a conclusion (supports / weakly
   supports / inconclusive / contradicts — for this model and task family
   only), and limitations (one synthetic world, one model, n=20). This
   one file must be enough for anyone to reproduce everything.

Budget guard: stay under ~50 sub-agent calls total. If the technique
can't be tested this cheaply, scale down and say so in RESULTS.md.

TECHNIQUE:
{paste one ### T{n} card here}
```

The three changes that matter most, if you're explaining them from the stage: canonical facts come first so nobody can accuse the agent of rigging the questions; the corpus must be too big to swallow, because that's the only regime where organization exists; and five off-target questions, because a technique that helps its own party trick but taxes everything else is a finding too.

---

## User

In case the results are indistinguishable, is there a way we could make the data progressively easier / harder so that we can find out which approach works better for agents?

My aim here is to make sure that the audience understands robustly whether there is a difference between the two kinds of data organizations, and even if the first attempt fails, the agent could try a second, or a third -- and if it goes beyond too many sub-agent calls, then stop, at which point we can more reliably conclude that the experiment failed to reveal a result.

Of course, that might make cross-experiment comparison uneven - some experiments reveal a result on the first try, some take 2-3 tries. But of course, we could document this and compare. Also, agents might not get the right comparable data structure differences the first time, so maybe this IS the more valid experiment. Maybe this IS the right way to discover the difference in how to structure data for agents vs humans.

These were my thoughts, but using the expert-lens and thinking along these directions, what improvements would you suggest in the benchmark prompt? Share the revised version. Don't bloat it or add things just for the same of it or because I asked. Add only when it has real value - but make sure you're able to infer my objective well.

If, based on these, you think the first prompt needs to change too, feel free to share a revised version of that. Your call. Again, don't feel compelled to change. See if there's compelling reason to change.

---

## Claude

<details>
<summary>Reframed adaptive retries as predeclared staircase design to avoid p-hacking</summary>

> Anand is suggesting we could use adaptive retries to escalate the difficulty or scale of the problem until the two approaches diverge, which would reveal where organization actually matters—treating the search for divergence itself as the core discovery. He acknowledges this breaks cross-experiment comparability, but argues the adaptive approach might be more scientifically valid since finding _where_ methods differ is the real insight. I'm starting to see the statistical trap here...
>
> The "keep retrying until you find significance" approach is classic p-hacking—the garden of forking paths. If you run multiple attempts and report whichever one hits p<0.05, your false positive rate balloons. But there's an honest, established way to get exactly what he wants: a dose-response or staircase design from psychophysics. Instead of hidden retries, you predeclare an escalation ladder of difficulty levels and run the experiment at each rung. Now the finding isn't "B beats A at p=0.04 on attempt 3"—it's "B outperforms A once the corpus exceeds roughly X tokens or distractor density reaches Y; below that, both perform similarly." This is statistically legitimate because the ladder is the experimental design itself, not a post-hoc retry strategy. It's also far more informative for a workshop: a threshold finding like "organization doesn't matter until your data outgrows the agent's easy reach" is concrete and actionable, directly addressing his thesis about token budgets and when you need agent-organization. A monotone dose-response pattern across levels is actually stronger evidence than a single p-value too—consistency beats a one-shot significance test. So the reframe is to convert the "pilot then run 20" approach into a structured staircase where each difficulty level is a planned step.
>
> For the practical design: run 8 paired comparisons across 3 predeclared difficulty rungs—corpus size, distractor density, hops per question—for roughly 48 sub-agent calls, fitting within the ~50 cap. The cleanest honest rule is to run all three rungs with fixed conditions and no stopping rules, then report per-rung accuracy for both approaches and visualize the trend. The primary analysis pools all 24 pairs using a McNemar or sign test with difficulty as a blocking factor, avoiding multiplicity issues while the per-rung breakdown shows the dose-response picture.
>
> His second concern—that agents might not get the data structure right on the first try, so iteration could be the valid experiment—conflates two different questions: whether organization B beats A under fixed conditions versus whether an agent can discover and refine good organization through iteration.
>
> If the parent agent keeps revising B until it wins, that's overfitting to the test set and rigging the demo. But that's actually a separate, legitimate experiment worth naming: have the agent iterate B on a development set, then evaluate on held-out unseen tasks. That directly connects to his workshop's second theme about agents engineering data for agents, so it deserves a short optional extension with a proper train-test split rather than dismissal. For the main path, keep conditions frozen—only iterate difficulty, never the transformation itself, unless tasks are split into dev and test sets.
>
> The revised prompt should predeclare three difficulty rungs with specific knobs like corpus size and distractor density, run eight paired tasks per rung with a mix of on and off-target examples, and keep the A→B transformation identical across all rungs. The pilot becomes mostly redundant since rung one is designed to be easy, though a couple of quick sanity checks on the harness itself are still worth keeping. The budget stays around fifty calls total, and the optional iterate-B experiment only happens if budget allows.
>
> One small addition to the research prompt could help: adding a "Matters when" field to the technique card that hints at what conditions make the technique's difference appear—corpus size, distractor density, multi-hop reasoning, etc. It's borderline compelling since the staircase design needs those knobs anyway, and the researching agent knows the mechanism best. One added line, that's all.
>
> The threshold results actually solve his comparability worry nicely. With a fixed three-rung ladder, every experiment has the same shape, and the rung number where a difference appears becomes the comparison itself. Across the room you get a map of which techniques matter at what scale—a genuinely useful artifact for the repo. The staircase is also the honest version of his retry instinct: instead of retrying until you get significance, you predeclare the dose-response ladder upfront.
>
> Done

</details>

Your instinct is right, but the version you described has a trap. Let me separate the good idea from the trap, because a skeptic in the room will find it.

### The trap: "retry until you see a difference"

If the rule is "run, and if there's no difference, make it harder and run again," you've created optional stopping. Three attempts at p<0.05 gives you roughly a 14% false-positive rate, not 5%. Worse, the experiments that "worked on the first try" and those that "needed three tries" aren't comparable — which you spotted yourself.

### The fix: don't retry — predeclare a ladder

There's an honest, well-worn version of exactly what you want: a **dose-response design** (psychophysics has used the "staircase" version for a century). Instead of retrying until something shows up, you declare three difficulty rungs _up front_ — say, small / medium / large corpus, with rising distractor density and more multi-hop questions — and run a small paired battery at every rung, always.

This is better than the retry version in four ways:

1. **It's the same budget.** 3 rungs × 8 paired tasks × 2 conditions = 48 sub-agent calls. Same ~50-call cap.
2. **The result is a threshold, not a coin flip.** "B beats A once the corpus passes ~200k tokens; below that, both are fine" is a far better workshop takeaway than "B beat A, p=0.04." It directly answers your workshop's real question: _when_ does organizing for agents start to matter?
3. **A null becomes a finding.** "No difference at any scale we could afford to test" is a bounded, honest claim — not a failed experiment.
4. **Comparability is restored.** Every participant runs the same three-rung ladder. The cross-experiment comparison becomes: _at which rung does each technique start to pay off?_ Some at rung 1, some at rung 3, some never. Collect that across the room and you have a map of which data techniques matter at what scale — the best aggregate artifact this workshop could produce.

One statistics note for the stage: the pattern across rungs is itself evidence. A difference that grows monotonically with difficulty is more convincing than one significant p-value, even with small numbers per rung. The primary test pools all 24 pairs; the per-rung breakdown is the picture.

### Your deeper point: "maybe iterating IS the experiment"

Careful — you've bundled two different experiments:

- **Experiment 1:** does organization B beat organization A? This needs _frozen_ conditions. If the parent agent revises B after seeing results, it's tuning the treatment to the test set. That's a rigged demo, however honest the intent.
- **Experiment 2:** can an agent _discover or refine_ a good data organization? This is a real and more interesting experiment — and it's literally promise #2 of your workshop ("how agents themselves can help engineer the data for agents"). But it needs a train/test split: let the agent iterate B against a dev set of tasks, then score it once on held-out tasks it never saw.

So the rule in the main prompt is: **iterate the difficulty, never the conditions.** And Experiment 2 becomes an optional extension for participants with budget left — probably the most publishable result anyone produces that day.

### Revised benchmark prompt

```
Run a small, controlled A/B experiment testing the data-organization
technique pasted at the end after "TECHNIQUE:". Build it, run it, analyze
it, and write the report. Don't ask me questions — make sensible choices
and document them.

1. HYPOTHESIS. State one testable hypothesis and ONE primary metric
   (usually accuracy). Note the technique's Type: if "representation" or
   "access", both conditions MUST contain identical facts — only the
   organization differs. If "augmentation", state exactly what was added.

2. GROUND TRUTH. Write a seed-fixed generator script that simulates
   entities with hidden traits interacting over time, using INVENTED
   names and numbers so nothing is answerable from world knowledge. It
   must take a difficulty level (1, 2, 3) and output canonical-facts.json
   plus the raw data. Higher levels mean: bigger corpus (roughly 50k /
   200k / 500k tokens), more near-miss distractors, stale versions, and
   conflicting values with dates, and more multi-hop facts. Declare these
   three levels now; do not change them later.

3. CONDITIONS. Write ONE transformation, once: it takes the raw data and
   produces ./A/ and ./B/ (randomly assign which is which; record the
   mapping, never reveal it to sub-agents):
   - Human condition: how a competent team would actually store this
     today. No strawman — a real team should defend it as normal.
   - Agent condition: the technique applied to the human condition.
   Apply this same transformation at every difficulty level. Never revise
   either condition after seeing any results. No per-file size limits —
   let each condition organize files the way it naturally would.

4. TASKS. From canonical-facts.json ONLY (never from the folders), write
   8 questions per level (24 total), each with one exact expected answer
   a script can check: 6 on-target (situations the technique targets)
   and 2 off-target (ordinary questions it wasn't built for).

5. RUN. Do 2 unscored runs to check the harness works, then run all
   24 tasks × 2 conditions. Each run is a FRESH sub-agent with a clean
   context (Task tool or a separate non-interactive CLI process — never
   this conversation), using a fast, cheap model, in parallel batches.
   Every sub-agent gets the SAME verbatim prompt — only the folder path
   differs — with the question, read access to one folder, identical
   tools (read, grep, bash), and a cap of 15 tool calls (hitting the cap
   = failure). Never reveal the hypothesis, the technique, the expected
   answer, or the other folder. Record: answer, tool calls, bytes of
   tool results (as a token proxy), and whether the cap was hit.

6. SCORE. Grade with a deterministic script (normalized exact match — no
   LLM judging). Primary test: paired sign test / McNemar pooled across
   all 24 pairs. Then break results down by difficulty level and by
   on/off-target, and describe the trend: does the gap grow as
   difficulty rises? Report median tool calls and result-bytes as
   secondary metrics.

7. REPORT. Write RESULTS.md: the technique card, hypothesis, the three
   predeclared difficulty levels, exact models and isolation method, the
   generator and transformation scripts inline (runnable via `uv run`
   with inline deps, fixed seeds), both folder trees with sample files,
   all 24 tasks + expected answers, the sub-agent prompt verbatim, raw
   results table, statistics, and a conclusion in this vocabulary:
   "difference appears from level N" / "no difference at any tested
   level within budget" / "B hurts" — for this model and task family
   only. State limitations (one synthetic world, one model, n=24). This
   one file must be enough for anyone to reproduce everything.

Budget guard: stay under ~50 sub-agent calls total.

OPTIONAL EXTENSION (only if budget remains): test whether an agent can
IMPROVE the organization. Split 12 new dev tasks / 12 held-out tasks.
Let a fresh agent iterate on condition B using only dev-task feedback,
then score the revised B once on the held-out tasks. Report separately.

TECHNIQUE:
{paste one ### T{n} card here}
```

### Prompt #1: one line, not a rewrite

The ladder needs difficulty knobs, and the researching agent — which just read the sources on _why_ the technique works — knows those knobs best. So add one field to the technique card:

```
- Matters when: {what should make the gap appear — corpus size, distractor
  density, multi-hop questions, ...}
```

That's the only change worth making. Everything else in prompt #1 already feeds this design: the "Testable claim" gives the hypothesis, "Type" gives the equivalence rule, and now "Matters when" gives the benchmark its ladder.

---

## Claude

<details>
<summary>Synthesized six experimental runs to refine conditional decision rule</summary>

> I'm looking at the responses.tsv file to parse the last six results that the user mentioned are at the bottom.
>
> Parse the updated TSV and find the new result submissions
>
> Script
>
> Save the six v2 RESULTS.md files for review
>
> Script
>
> Scan each v2 report for attestation, conditions, metrics, and conclusions
>
> Script
>
> I need to track down Priyanga's results and conclusion, and also look more closely at what Prasanna did—he removed the sandbox environment and ran a variant with just Read, Grep, and Glob tools without bash access, which seems to have yielded a non-significant token count result (p=0.24).
>
> Get Anand's and Priyanga's final stats and Prasanna's v2 design
>
> Script
>
> Looking at Ahmed's v2 run with Haiku 4.5 using the faithful protocol, the claim holds from level 1 with non-inferiority passing on token counts and clear cost superiority across all 24 pairs—the advantage scales monotonically from 2.6× up to 27.6×, though the L3 portal consistently truncates and causes thrashing, triggering the pilot hardening protocol.
>
> Anand S's run with gpt-5.4-mini shows perfect accuracy on both sides (24 vs 24) and achieves 2.4× cost savings, with the interesting wrinkle that the portal still extracted correct answers despite L3 truncation—likely because the sorted order preserved critical facts or the model recovered via tools. Pratyush's gpt-4o-mini run reveals a different pattern: the catalog navigation fails harder than portal reading (11 vs 15 accuracy), missing non-inferiority by a margin of 4, though costs drop dramatically at 29× savings—the weak model struggles with the fetch loop competence that catalog navigation demands, suggesting spoon-fed portal access suits lower-capability agents better.
>
> Priyanga's voxtral-small-24b hits the floor entirely (0 vs 2 accuracy) and actually costs more with catalog due to thrashing; her model failed to invoke tools properly and emitted JSON as text instead, so the result is more a capability threshold signal than an organizational finding. Randhir's gpt-5.5 codex run failed at the harness level—44 of 48 runs rejected by usage limits before the model even ran, leaving only 4 valid rows, which he correctly didn't claim as results; he also surfaced a real-world CLI prompt-length rejection that breaks portal harnesses. Prasanna's Haiku 4.5 deliberately deviated from the pinned protocol, testing flat files with basic tools versus indexed SQLite with bash sandbox—a different bracket entirely—and hit accuracy ceiling again (23 vs 24) with no significant token difference across the preregistered Wilcoxon test, though the effect reverses at L1.
>
> Looking at Prasanna's L2 results, the savings appear around 3× with a post-hoc p of 0.043, and his key insight is that the technique only pays off past roughly 100k tokens and on aggregation-style queries; below that, index overhead becomes a liability. Pooling the six v2 runs, I'm seeing two clean confirmations of the joint claim (Ahmed's 7.3× growing to 27.6× at L3, Anand's 2.4× with perfect accuracy), one case where cost holds but accuracy fails on a weak model (Pratyush losing 4 answers), one floor effect where the model can't use tools (Priyanga), one honest harness failure (Randhir), and one nuanced finding about conditionality (Prasanna). The synthesis is clear: this isn't a blanket "reorganize folder data" rule—the benefit is conditional on scale, appearing only above roughly 100k tokens and on aggregation tasks.
>
> The real insight is that the technique's value hinges on access mode, not folder structure. Against preloading into context, the wins are massive (7–28×); against grep-able files, gains are modest or negative on accuracy. Strong models drive fetch loops fine, but weaker ones lose accuracy or collapse entirely. Sharded layouts need freshness metadata or they backfire. So the SKILL.md should be a conditional decision rule: leave small, grep-able corpora alone; for anything exceeding half the context window or expected to grow, use a compact catalog with on-demand fetch and expect 2–30× token savings with neutral accuracy for capable models.
>
> For Anand, the priorities are writing the skill with the conditional rule and evidence block (high impact given his constant work on client data organization), publishing the 13-experiment arc as a data story showing how the v1→v2 construct fix flipped nulls into confirmed 7–28× gains, folding the findings into the workshop repo, and flagging the model-capability threshold and scale-conditional findings as separate follow-ups worth deeper investigation.
>
> Done

</details>

## What the six v2 runs show

The fixed prompt did its job. The intervention finally lived in the sub-agent's prompt (portal = corpus preloaded, catalog = index + fetch), level 3 was sized past the context window, the metric matched the card's claim, and the attestation rule visibly worked: Priyanga's run is now a real, attested LLM experiment, and Randhir's harness failure was reported as a failure instead of dressed up as a result.

| Run        | Sub-agent model | Verdict                          | Key numbers                                                                                                                                                                             |
| ---------- | --------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ahmed      | Haiku 4.5       | **Claim holds from L1**          | Accuracy 21 vs 20 (non-inferior); catalog cheaper on 24/24 pairs, p<0.0001; savings grow 2.6× → 5.3× → **27.6×** at L3 where portal truncates and thrashes                              |
| Anand S    | gpt-5.4-mini    | **Claim holds**                  | 24 vs 24 accuracy; 2.4× cheaper overall                                                                                                                                                 |
| Prasanna\* | Haiku 4.5       | **Conditional**                  | Accuracy at ceiling; pooled token test **not** significant (p=0.24) because the index is _overhead_ at L1 (0.9×) and on simple lookups (0.36×); on-target saving appears from ~L2 (~3×) |
| Pratyush   | gpt-4o-mini     | **Cost holds, accuracy doesn't** | Catalog 11/24 vs portal 15/24 — non-inferiority fails; but ~29× cheaper at L3                                                                                                           |
| Priyanga   | voxtral-24B     | **Floor — model too weak**       | 0/24 vs 2/24; catalog cost _more_ (thrashing); model emitted tool calls as text                                                                                                         |
| Randhir    | gpt-5.5         | **Void, honestly reported**      | 44/48 runs rejected by a CLI usage limit before any model ran; no claim made                                                                                                            |

\*Prasanna deviated from the pinned protocol on purpose (flat files + read-only vs index + SQLite + sandbox) and defended it well; his v1 and v2 bracket the technique from two sides.

### So what's actually true?

Read together, the v1 and v2 rounds give you something much better than "T1 works": they give you its **boundary conditions**.

1. **The win is about access mode, not folder shape.** The huge, unambiguous wins (7×–28×) appear only against _preloading into context_. Against a grep-able folder (all of v1), reorganizing bought little and sometimes hurt. So the actionable rule is "never stuff the corpus into the prompt," not "reorganize every folder."
2. **The win is conditional on scale.** Below roughly half a context window (~100k tokens in Prasanna's data), the catalog is pure overhead — worse on small corpora, worse on simple lookups. The benefit turns on when the corpus outgrows what preloading can carry, and it grows monotonically from there.
3. **The win is conditional on model capability.** Just-in-time access shifts work from context to _navigation_. Haiku 4.5 and gpt-5.4-mini navigated fine. gpt-4o-mini lost 4 answers doing it. A 24B model collapsed entirely and burned more tokens failing. Catalogs are a bet on the model's ability to drive a fetch loop.
4. **From v1, still standing:** sharded layouts without freshness/version metadata actively caused wrong answers (the one significant result of round one, p=0.03).

### Should you ship it as a blanket SKILL.md?

No. "Whenever data is in a folder, reorganize it" is contradicted by your own data three ways: it does nothing against grep (v1), it costs extra below ~100k tokens (Prasanna), and it backfires on weak models (Pratyush, Priyanga). A blanket skill would encode the exact overclaim your benchmark exists to prevent — and it would trigger constantly, since "data in a folder" describes everything.

Ship a **conditional skill** instead. Its core is a decision rule, not a transform:

- Corpus fits comfortably in context, tasks are lookups → do nothing; grep is already progressive disclosure.
- Corpus exceeds ~half the window, or will grow → never preload; provide a compact catalog (paths, one-line descriptions, counts, date ranges) and fetch on demand. Expect 2×–30× token savings at neutral accuracy _for capable models_.
- Sharding → attach "which version is current" metadata, or you'll trade retrieval errors for staleness errors.
- Weak model in the loop → prefer fewer, larger, pre-filtered files over catalog navigation.
- Evidence block: 6 attested runs, 3 model tiers, the numbers above, and what wasn't tested (one synthetic task family, single-question tasks, 15-call cap).

Your earlier skill-synthesis prompt already demands exactly this shape (evidence-only, "when not to use," provenance block) — feed it the two rounds of RESULTS.md and it should produce this skill almost verbatim.

### Highest impact × frequency actions, in order

1. **Write the conditional skill** (above). You and your teams touch "how do we hand this client's data to an agent" weekly at Straive; a decision rule with numbers attached compounds every time.
2. **Publish the v1→v2 arc as a data story.** Thirteen experiments, ~600 attested sub-agent runs, one afternoon, and the plot twist: the first round's nulls weren't evidence against T1 — they were the harness quietly testing a different hypothesis, and one construct fix turned nulls into a 28× effect. That's the strongest possible artifact for the workshop repo, your blog, and the AX talk. The one-line version for the stage: _progressive disclosure is load-shifting — it trades context cost for navigation skill, so it pays exactly when context is scarce and skill is present._
3. **Bank the two boundary findings as follow-up benchmarks** for the next cohort: the model-capability threshold (at what size does catalog navigation break?) and the scale crossover point (where exactly does the index stop being overhead?). Both are one-afternoon experiments with the existing prompt.

### Here's what to say

- **The re-run worked. The claim holds, with conditions.**

- Two clean runs confirmed it: catalog-and-fetch matched preloading on accuracy and cost 2.4x to 27x less, and the gap grew with corpus size.
- The protocol fixes did their job. One earlier fake run became a real attested one, and one broken run was reported as broken instead of dressed up.
- **But this is not a blanket rule, and I will not ship it as one.**

- Below about 100k tokens, the index is pure overhead. It made things worse on small data and simple lookups.
- On weak models it backfires. gpt-4o-mini lost accuracy driving the fetch loop, and a 24B model failed completely and spent more tokens doing it.
- And against a plain grep-able folder, reorganizing barely helps. The real win is refusing to preload, not reshuffling files.
- **The skill I'll write is a decision rule, not a transform.**

- Small corpus plus lookups: leave it alone.
- Big or growing corpus: never preload. Give the agent a compact catalog and let it fetch. Expect 2x to 30x savings on a capable model.
- If you shard, attach freshness metadata. Round one showed shards without it cause wrong answers.
- **Three actions from here.**

- Write that conditional skill this week, with the evidence block from all 13 runs.
- Publish the two-round story: round one's nulls came from the harness testing the wrong thing, and one fix revealed a 28x effect. Best teaching material we produced today.
- Queue two follow-ups for the next cohort: find the model-capability floor, and find the exact corpus size where the index starts paying.

---

## User

Based on what you have seen so far as evidence, what skill would you suggest we create about it? See, think about this, you don't necessarily need to create a skill if it should not be applied uniformly. You would create a skill only if there is some data or evidence here that suggests that it would be broadly applicable. Of course, making sure that there are caveats and filters so that it doesn't get applied in the wrong place. My aim is to set up a skill that when I am converting from a corpus that is typically meant for humans to a corpus that is meant for agents, you automatically apply this skill so that it follows the benchmark best practices that we have.

---

## Claude

<details>
<summary>Architected conditional triage skill with evidence-backed practices and safety guardrails</summary>

> Anand is asking whether we should create a skill for converting human-oriented text into agent-oriented text, with the goal of having it auto-apply best practices when needed. He's leaning toward yes based on the evidence, though his thought cuts off mid-sentence.
>
> The evidence actually points to a narrower, conditional skill than a blanket reorganization approach. The decision rule itself is broadly applicable across every corpus conversion—it's a triage skill that encodes _when_ to transform, not a uniform transformation. The evidence backs specific practices: avoid preloading large corpora into context (2.4×–27.6× savings); leave corpora under ~100k tokens alone since indexing becomes overhead; sharding needs freshness metadata; weaker models struggle with catalog navigation; and task type matters—aggregation and multi-hop queries benefit, but single-fact lookups don't. The evidence doesn't support untested techniques like markdown conversion or semantic IDs, so the skill should stick to what was measured. The skill design would be something like `agent-corpus-triage` that describes the decision framework and evidence-backed practices, with a note that other techniques remain untested.
>
> The skill should trigger when preparing data for agents and include a measurement step first—counting tokens, identifying the target model, and profiling the task mix—before applying any transforms. This makes auto-application safe because the default at small scale is to do nothing. I'd include a deterministic token-counting script and catalog generator as reusable tools, and optionally offer a lightweight verification loop using the benchmark prompt when stakes are high, which closes the loop between the skill and the benchmark itself. I've already reviewed the skill-creator guidance earlier in this conversation, so I don't need to re-read it. Now I'll write a short explanation of why this should be a skill, then create and present the file in plain language.
>
> Done

</details>

<details>
<summary>Identified and excised unused variable assignment</summary>

> Create the skill folder
>
> Script
>
> Draft the evidence-grounded triage skill for converting human corpora to agent corpora
>
> SKILL.md
>
> Small deterministic catalog generator script bundled with the skill
>
> make_catalog.py
>
> Verify the script runs and produces a sane draft catalog
>
> Script
>
> There's a dead variable assignment in the script that isn't being used — I'll remove it to clean things up.
>
> Remove a dead line left in the script
>
> make_catalog.py+1-2
>
> Presented 2 files
>
> Done

</details>

Yes — create the skill. But the evidence supports a different shape than "here's how to reorganize data for agents."

Here's the reasoning. Your data says the _transform_ is not broadly applicable: it does nothing below ~100k tokens, it backfires on weak models, and it barely matters when the corpus is already grep-able. But the _decision_ is broadly applicable — every single human-to-agent conversion faces the same three questions: how big is the corpus, what model will read it, and what kind of questions will it get. That decision came out the same way across 13 runs. So the skill should be a **triage skill**: it always runs when you convert a corpus, it measures first, and one of its valid outputs is "do nothing." A skill that can say "leave it alone" is safe to auto-apply. A skill that always transforms is not.

That resolves your worry directly: we're not encoding "reorganize whenever data is in a folder." We're encoding "measure, then decide, and here's the evidence for each branch."

Let me write it.

The skill is drafted above: `corpus-for-agents`, 101 lines, plus a small deterministic script that builds the mechanical half of the catalog (paths, token counts, row counts, date ranges) so the agent only writes the descriptions.

Three design choices worth knowing, since they answer your "should this even be a skill" question:

**It always triggers, but doesn't always transform.** Step 1 forces measurement (corpus tokens, model window, model tier, task mix), and the first row of the decision table is "do nothing" — with your own numbers showing why (0.4–0.9× _worse_ below the threshold). That's what makes auto-apply safe. The uniform behavior is the triage, not the reorganization.

**Every line traces to a run.** The decision table cites the 2.4×–27.6× confirmations, the ~100k-token crossover, the weak-model refutations, and the p=0.03 sharding harm. The Evidence block also lists what was _not_ tested — markdown conversion, llms.txt, semantic IDs — so the skill can't quietly absorb the other nine techniques without their own benchmarks. When a future cohort tests T5 or T6, you add a row to the table and a line to the evidence, and the skill grows the way the benchmark grows.

**The strongest rule got top billing.** "Never concatenate the corpus into the prompt" held in every confirmed run and is where the catastrophic costs live. Folder reshuffling is the weaker, conditional part; the skill's emphasis matches the effect sizes.

One caveat to carry: the crossover (~0.5×W, ~100k tokens) rests mainly on one careful run of Prasanna's, so treat it as a default worth pinning down, not a law — it's literally one of the two follow-up benchmarks you queued. And before installing, worth running the self-test from your synthesis prompt: hand this skill to a fresh agent with a real Straive corpus and see where it has to guess. My bet is the "capability tier" judgment in Step 1 is where it'll want sharper guidance first.

Download:

- SKILL.md (saved as corpus-for-agents-skill.md)
- make_catalog.py

---

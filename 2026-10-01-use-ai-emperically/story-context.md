# Story context for Use AI Empirically — DBS TechVerse

This file supports the narrative story generator. transcript.md remains the source of truth for what happened and for all direct quotes. These notes add event/audience context, narrative structure, evidence/caveats, and source pointers.

## Event context

- Date: 1 Oct 2026.
- Event: DBS Technology India — TechVerse Session 4: Agentic AI.
- Format: remote Webex session, scheduled 2:30–4:00 PM IST.
- Organizer-circulated title: “Effective use of Gen AI for personal and professional productivity.”
- Internal description: how to (and how not to) use agents effectively when writing software.
- Mayank framed TechVerse as part of DBS Technology India’s effort to build an AI-native workforce.
- The expected audience was roughly 150–250, skewed toward developers with about 3–6 years of experience, plus some fresh graduates.
- DBS already had substantial L1/L2 use of AI for code, tests and documentation. Prep-call examples included code review, Jira→repo workflows, migrations/replatforming, regression-suite generation, employee-onboarding agents, MLOps and AI red teaming.
- Tool access was constrained. Venky said before the event that Gemini CLI (Flash 3.7) was the only relevant coding-agent tool broadly available; this pushed the final session toward demonstrations and discussion rather than a hands-on workshop.
- Organizers had explicitly liked the PyConf Hyderabad “How Students Learn Python” work and wanted an employee/coding-agent analogue based on actual traces rather than generic advice.
- Anand described the intended effect in prep as a seed that helps people figure out new things, not an attempt to teach everything in one session.

Primary prep source: ~/Dropbox/notes/transcripts/2026-09-22 DBS Tech India Gen AI Carnival Prep.md

Do not expose internal DBS invite links, email addresses, Webex links or other private logistics in the public story.

## Catalog metadata

If the talk-story skill updates config.json, use:

- date: 2026-10-01
- time: 2026-10-01T14:30:00+05:30
- duration: 90
- categories: [latest]
- event: DBS Technology India — TechVerse Session 4: Agentic AI
- location: Remote / Webex
- circulated title: Effective use of Gen AI for personal and professional productivity
- talk thesis/title: Use AI Empirically
- speaker: Anand S — https://www.s-anand.net/
- suggested details: Treat AI advice, models and agent workflows as hypotheses: test them on your work, mine logs for evidence, and make verification part of the workflow.

Natural public assets:
- page: 2026-10-01-use-ai-emperically/
- transcript: 2026-10-01-use-ai-emperically/transcript.md
- audio: https://github.com/sanand0/talks/releases/download/talks/2026-10-01-use-ai-emperically.opus
- comic: 2026-10-01-use-ai-emperically/comic-page.avif

The directory misspells “empirically” as “emperically”; keep paths unchanged but spell the word correctly in visible copy.

## The story hidden inside the transcript

The talk is best read as one repeated move:

**Someone offers a plausible rule → turn it into a cheap experiment → let the result change the rule.**

That is stronger than narrating the demos in sequence.

### 1. The experiment begins before the talk: the identical haircut

The pre-session banter is a strong cold open.

- [00:15] Anand’s first response to Venky’s image-editing story is: “I'm curious: what worked, what failed?”
- Venky says adding hair to two different bald/balding people keeps producing essentially the same hairstyle.
- Anand immediately turns that observation into a benchmark question: does quality/thinking level change hair texture/fibres across different images?
- It is funny, human and completely on-theme: before the formal thesis appears, the instinct is already observe → hypothesize → test.

### 2. Make the room generate the hypotheses

At [06:23], Anand states the thesis directly: “use AI in an empirical way.”

Then he asks the audience for prompting advice. They supply hypotheses: add constraints, say what not to do, use persona/action/context/template, specify scope and expected outcome, meta-prompt, use a golden dataset, think step-by-step.

The key audience line is Venkateswarlu’s suggestion to use a golden dataset. Anand turns it into: “I believe it when I test it.” [08:53]

Narratively, these are not tips. They are hypotheses the rest of the talk keeps testing.

### 3. Common prompting advice can be wrong — or only locally right

Three experiments weaken the idea of universal prompting advice.

#### Simple writing hurts thinking

- A sensible instruction — “Only report to me in ASD-STE100 Simplified Technical English” — made evaluated answers worse across almost every rubric dimension in this experiment.
- Practical workaround from the talk: let the model reason normally, then ask it to explain simply.
- Public page: https://www.s-anand.net/blog/simple-writing-hurts-thinking/
- Local source: ~/code/blog/posts/2026/simple-writing-hurts-thinking.md
- Useful line: “what if it also starts thinking simply?” [11:01]

#### Emotional / persuasion prompting

- The experiment covered 40 models.
- “Think step by step” was the only variant with an overall positive effect, and even that was modest and model/task dependent.
- Emotion, shaming, praise, incentive, expert/persona etc. were neutral or slightly harmful overall.
- The transcript explicitly cautions that the experiment predates today’s reasoning-native model mix.
- Public page: https://sanand0.github.io/llmevals/emotion-prompts/
- Local source: ~/code/llmevals/emotion-prompts/README.md

Do not turn “reasoning works” into timeless advice. The durable lesson is to test prompting advice on the model/task actually used.

#### Pólya audit

- Advice used by mathematicians for decades flips by problem domain/model.
- In the talk, working backwards helps some counting tasks but not number theory; case analysis helps some domains and hurts others.
- Public page: https://sanand0.github.io/datastories/polya-for-ai/
- Blog background: ~/code/blog/posts/2026/testing-polya-heuristics-on-ai-math.md
- Conceptual payoff [17:05]: “the whole notion of general advice is something that we can start putting to rest.”

Keep the nuance immediately after it: advice can work in specific situations. The target is universal advice.

### 4. Choosing models is less important than being able to re-choose

The audience suggests intelligence, cost, latency, task complexity, domain relevance and context window.

Anand begins with a generic cost-quality frontier:
- https://sanand0.github.io/llmpricing/
- https://arena.ai/leaderboard

The durable point comes at [27:01]: “maybe the bigger lesson is not how do you choose a model, but rather how do you change when the new model comes?”

Because the frontier moves quickly, model substitution should be cheap. Date specific prices/model rankings to 1 Oct 2026.

Do not present the chart’s “high-school / PhD / professor” labels as psychometric facts; they are storytelling metaphors.

### 5. Hype becomes a $2 question

Jev is the clean model-selection case study.

- Rather than debate architecture, Anand creates a 77-case BANKING77 benchmark.
- Public result: https://sanand0.github.io/llmevals/jev/
- Public/share chat: https://chatgpt.com/share/6abe643c-b1c4-83ec-a543-f9d7be5589d4
- Local source: ~/code/llmevals/jev/README.md
- Detailed context: chat-jev-benchmark.md

Important scene [31:41–34:53]: the custom benchmark took roughly five minutes of Anand’s own time; AI handled the research, costing, run, analysis, page generation and commit. The pilot cost under $2.

Strong line [34:53]: “We are using agents to figure out how good agents are.”

This is central: AI has lowered the cost of experimentation itself.

Caveat: this was a small paired 77-case pilot, one case per BANKING77 intent. Accuracy used gold labels, not an LLM judge. Risk/coverage thresholds on the same 77 cases are exploratory. Costs were recorded response costs at the time, not promises of future pricing.

### 6. A benchmark can be synthetic, visual and personal

The GPT Image 2.5 Flare section makes “benchmark” feel less like an ML leaderboard.

- Live page: https://sanand0.github.io/llmevals/gpt-image-flare-quality/#where-it-shows?quality=max
- Local source: ~/code/llmevals/gpt-image-flare-quality/README.md
- It probes low/medium/high/xhigh/max and asks where humans can actually see a useful difference.
- The talk’s practical heuristic becomes: default lower/medium; go higher when fine hair/fibre/cloth/microtexture warrants it.
- This loops back to the opening hair joke.

Caveat: image generations are stochastic. This is a practical visual probe, not a fixed-seed proof that one upper tier is deterministically better.

### 7. For agents, measure the job — and make quality visible

Audience question: How do you choose agents?

Useful external benchmark:
- https://artificialanalysis.ai/evaluations/terminalbench-2-1?eval-cost=score-vs-cost-per-task

The conceptual shift is cost per task, not token price.

Anand’s personal benchmark:
- https://sanand0.github.io/llmevals/coding-agents/
- source: ~/code/llmevals/coding-agents/README.md
- same small GitHub-profile webapp prompt across several harness/model combinations;
- some fail outright; among successful runs, visible quality differs substantially;
- the output can be scored at a glance.

Strong principle [48:40]: if an agent can turn its result into something you can assess at a glance, verification gets much cheaper.

That applies beyond UI: diffs, test reports, traces, invariant checks, before/after metrics, replays and screenshots can compress review cost.

### 8. Your own work can become the benchmark suite

The more recent coding-model benchmark uses three actual tasks from Anand’s own recent history: image loading/performance, WhatsApp integrity validation and MCP console-log readability.

- Public page: https://sanand0.github.io/llmevals/qwen-3.6-vs-gemma4-e4b/
- Local source: ~/code/llmevals/qwen-3.6-vs-gemma4-e4b/README.md

At the time, GPT-6 Luna was clearly best on these three tasks; Qwen 3.6 was useful enough as a local/offline fallback; Gemma 4 E4B often failed to complete meaningful changes.

Especially useful example: on the WhatsApp task, Gemma passed old tests while making no change. Therefore a green existing test suite did not prove the requested task was done. The benchmark intentionally separates automated verifier output from human judgment of the diff.

Core line [52:28]: “you don't necessarily need to hunt for a benchmark that suits your work. You can take your own logs and convert that to benchmarks.”

### 9. The hard agent skill is turning a messy surface into testable parameters

Venky challenges the premise: models/harnesses expose many different controllable surfaces. How do you compare agents fairly?

Anand’s response becomes a useful three-part abstraction:

1. Find a problem that differentiates configurations.
2. Specify verification criteria / a rubric.
3. Evaluate automatically.

At [61:00]: “specification, verification, execution is the chain that I'm trying to convert almost any product to.”

This matters because it teaches the audience how to create experiments, not merely admire benchmarks.

A provocative supporting quote [56:36]: “if you're happy with any of these models, then that means you don't have tough enough a problem that will be able to differentiate between models.” Use this as Anand’s personal learning strategy, not universal advice.

### 10. The developer joke points at the real bottleneck

Around 62–65 minutes, Venky asks what software developers should do as coding agents improve. Anand gives intentionally cynical career-preservation anti-patterns: use security/compliance language to kill automation; produce lots of output nobody can verify; hand off risk before “the shit hits the roof.”

The joke is funny because it describes an incentive failure that becomes easier when generation scales faster than verification.

The pivot is explicit [63:26]: “it is very, very hard to verify output, and with agents, you can create a lot of output.”

Do not quote the anti-patterns without the transcript’s clarification that they are anti-patterns and natural failure modes, not recommendations.

### 11. Logs are a lab notebook for your own agent usage

Anand gives Codex his own historical Codex logs and asks which new features he is or is not benefiting from.

- Live page: https://sanand0.github.io/datastories/codex-session-analysis/
- Deeper source: ~/code/codex-session-analysis/CODEX_SESSION_GAP_ANALYSIS.md

Underlying analysis:
- 903 Codex sessions, 17 Apr 2025–1 Mar 2026.
- New-model adoption was fast; many newer workflow features were barely used.
- gpt-5.3-codex: 72/95 post-release sessions (75.8%).
- manual shell parallelism: 65/95 (68.4%).
- built-in parallel orchestration: 0/95.
- heuristic analysis flagged 457 sessions as parallel-tool-call opportunities.
- The talk shows an estimated 11.3 hours saved if a portion of gaps were closed; treat that as a simulator estimate, not measured causal savings.

Memorable contrast [66:30]: “when a new model comes, you have about 75 or 76% adoption. When there's a new workflow, your adoption is zero.”

Practical prompt [70:13]: “Find out all the new features of Gemini CLI [or pick your agent] that have been released in the last eight months, and find out which ones of those would have the maximum impact for me based on my logs.”

Bigger point [69:39]: “Your agent logs are one of the most powerful diagnostic devices.”

### 12. Team logs reveal a failure demos hide

This is the strongest practical payoff for the DBS developer audience.

Source: chat-agent-log-analysis.md

The prepared corpus ultimately covered 1,112 top-level sessions from 7 contributors across Codex and Claude.

The counterintuitive finding was not that people failed to inspect before editing. Inspection was common. The weakness was closing the loop after the final edit.

In the first full analysis:
- 528 Codex editing sessions: 75.9% inspect before editing, only 2.3% had recognized test/build/lint/typecheck after the final edit.
- Claude: 93.9% inspect first, 3.0% had recognized final programmatic validation; 11.1% if browser validation counts.
- failed Claude anchored edits: re-read/inspect before retry → 1/68 (1.5%) next edit failed; retrying with changed args without inspection → 12/15 (80%) failed in that first analysis.

Public wording guardrails:
- Say “recognized final programmatic validation,” not “97% of developers never test anything.”
- Log-derived detectors can miss unconventional or human-only validation.
- These were other people’s machines; they were not using Anand’s local skills. The recommendation was therefore a shared team operating practice.
- Avoid ranking individuals; task mix and environment differ.

Best transcript line [71:26]: “coding has become very fast, but testing and ownership has not followed.”

Best practical advice [72:49–73:21]: have the agent show evidence the change worked. Better yet, tell it how you would test it.

Uttam’s Webex comment reinforces the point: “ask the agents to do test-driven development.”

The underlying analysis suggested small shared behaviors:
- after the last code/config edit, run the smallest relevant independent check;
- if an anchored edit fails, re-read/search before retrying;
- UI changes should end with browser/interaction validation.

This is exactly the kind of team-level learning the organizers had requested in prep.

### 13. Reliability becomes an architecture, not a feeling

The talk closes with ways to route uncertainty instead of demanding perfection.

#### Double checking

- Public page: https://sanand0.github.io/llmevals/double-checking/
- Local source: ~/code/llmevals/double-checking/README.md
- In this customer-support intent benchmark: one-model average error 14.1%; two-model agreement 3.7% error with 12.6% manual-review effort; three models 2.2% error; five models 0.7% error with 28.1% effort.
- Mechanism: models’ mistakes are partly independent, so disagreement is a useful escalation signal.
- Do not generalize these percentages beyond this task.

#### Confidence calibration

- Public page: https://sanand0.github.io/llmevals/confidence-calibration/
- Local source: ~/code/llmevals/confidence-calibration/REPORT.md
- Raw stated confidence is often overconfident.
- Prompted confidence can become more useful.
- Logprobs can be useful for risk ranking even when their literal probability is poorly calibrated.
- Learn thresholds from historical gold data and validate them on a holdout.
- Updated report: a frozen logprob rule built on 770 cases auto-passed 65.2% of 2,310 untouched requests at 4.38% observed error at the predeclared 5% target. Do not extrapolate that result to other thresholds/tasks; the frozen 10% rule missed its target.

The talk makes the code analogy too [90:02]: “Have an agent adversarially test it.”

So verification can mean tests, independent models, calibration/routing or human escalation depending on the task.

### 14. The ending is already written

The final minute is unusually clean:

- [90:31] prompting advice, models and agents: “you should just test.”
- [90:50] “Your logs—session logs, and any logs in general—are probably the best way to improve any kind of workflow.”
- [90:59] “make sure verification is part of that workflow.”
- [91:19] “benchmarking is not just for your workflow; benchmarking is a verification mechanism and should be literally part of the delivered workflow as well.”
- [91:30] “let's test.”

Use this ending rather than inventing a generic inspirational conclusion.

## Compact conceptual spine

If the page needs a recurring phrase or visual, either of these compressions works:

- Advice → Hypothesis → Benchmark → Evidence → Workflow
- Observe → Test → Measure → Verify → Improve

But do not let a framework replace the human story. The hair anecdote, Jev experiment, visual coding benchmark, log-analysis surprise and double-checking result are what make it memorable.

## Source and asset map

| Live idea/page | Public URL | Strong local source | Use for |
|---|---|---|---|
| Simple writing | https://www.s-anand.net/blog/simple-writing-hurts-thinking/ | ~/code/blog/posts/2026/simple-writing-hurts-thinking.md | plausible prompt advice that backfires |
| Emotion prompts | https://sanand0.github.io/llmevals/emotion-prompts/ | ~/code/llmevals/emotion-prompts/README.md | advice is model/task dependent |
| Pólya audit | https://sanand0.github.io/datastories/polya-for-ai/ | ~/code/blog/posts/2026/testing-polya-heuristics-on-ai-math.md | canonical heuristics can flip by domain |
| LLM pricing | https://sanand0.github.io/llmpricing/ | live page / repo | moving cost-quality frontier |
| Arena | https://arena.ai/leaderboard | public source | borrowed human-preference benchmark |
| Jev BANKING77 | https://sanand0.github.io/llmevals/jev/ | ~/code/llmevals/jev/README.md; chat-jev-benchmark.md | custom benchmark + benchmark delegated to agents |
| Image quality | https://sanand0.github.io/llmevals/gpt-image-flare-quality/#where-it-shows?quality=max | ~/code/llmevals/gpt-image-flare-quality/README.md | visual benchmark + hair callback |
| TerminalBench | https://artificialanalysis.ai/evaluations/terminalbench-2-1?eval-cost=score-vs-cost-per-task | public source | cost per task |
| Coding agents | https://sanand0.github.io/llmevals/coding-agents/ | ~/code/llmevals/coding-agents/README.md | human-at-a-glance end-to-end agent benchmark |
| Local vs frontier coding | https://sanand0.github.io/llmevals/qwen-3.6-vs-gemma4-e4b/ | ~/code/llmevals/qwen-3.6-vs-gemma4-e4b/README.md | own historical tasks as benchmarks |
| Personal Codex logs | https://sanand0.github.io/datastories/codex-session-analysis/ | ~/code/codex-session-analysis/CODEX_SESSION_GAP_ANALYSIS.md | logs reveal missed capabilities |
| Team agent logs | no public link | chat-agent-log-analysis.md | logs reveal missing final verification |
| Double checking | https://sanand0.github.io/llmevals/double-checking/ | ~/code/llmevals/double-checking/README.md | disagreement as verification |
| Confidence calibration | https://sanand0.github.io/llmevals/confidence-calibration/ | ~/code/llmevals/confidence-calibration/REPORT.md | risk scores + review thresholds |

Related background that may be linked if useful, but should not be implied to have been shown live:
- https://www.s-anand.net/blog/how-i-verify-and-delegate-to-ai/
- https://talks.s-anand.net/2026-09-03-convergence-jio-institute/
- ~/code/talks/2026-03-15-how-students-learn-python/ — relevant because organizers explicitly requested an analogous employee/coding-agent learning analysis.

## What a reader should leave knowing

Prioritize these over a comprehensive recap:

1. Treat AI advice as a hypothesis. “Best practices” often depend on model, task and time.
2. Build tiny task-specific benchmarks cheaply. Agents can help create, run, analyze and update them.
3. Use your own work as the dataset. Historical tasks and session logs are often more relevant than public leaderboards.
4. Make agent quality easy to inspect. Tests, diffs, traces, screenshots and explicit rubrics compress review cost.
5. Generation is no longer the hard part; verification and ownership are.
6. Put verification inside the workflow: TDD/programmatic checks for code; independent checks/calibration/escalation for model outputs.
7. Keep re-testing. Models, prices and agent capabilities move too quickly for a static recommendation to stay correct.

A strong developer action after reading:

> Export a week or month of your agent logs and ask an agent: “What am I repeatedly doing badly, what new features would have helped, and what one measurable behavior should I change?” Then verify the recommendation on future sessions.

## Tone / visual opportunities

- Cold open: the identical AI haircut. Concrete, funny and visual.
- Recurring laboratory motif: advice enters as a hypothesis; results either survive or get crossed out.
- Guess-before-reveal where feasible: prompting trick, coding-agent output, double-checking error reduction.
- At-a-glance comparisons: especially the coding-agent pages and image-quality crops.
- Use direct audience voices so it feels like a room thinking together, not Anand lecturing.
- The cynical developer section can be a dark/humorous band followed immediately by the serious verification bottleneck.
- The team-log result deserves a strong beat: “inspection happens; closure doesn’t.”
- End with the transcript’s “let's test.”

## Fact-check / interpretation guardrails

- Direct quotes must come verbatim from transcript.md.
- Use the local source files above for benchmark numbers/caveats when transcript wording is loose.
- Do not say the pricing chart literally measures IQ or educational attainment.
- Do not say “Jev failed” universally; on Anand’s small BANKING77 pilot at that date, other models offered a better cost/accuracy tradeoff for that use.
- Do not say GPT Image xhigh/max are useless. Say Anand/agents could not reliably distinguish upper-tier gains in the probes shown, while microtexture sometimes benefited from higher quality.
- Do not say 97–98% of developers “did not test.” The log analysis detected very little recognized final programmatic validation after the last edit; human/unrecognized checks may be absent from logs.
- Do not call the 11.3-hour Codex-log saving a measured outcome. It was an estimate/simulator output.
- Do not generalize double-checking/calibration error rates beyond the benchmark tasks.
- Any model ranking, price or “frontier” statement is dated 1 Oct 2026.
- The private team-log chat has no public URL. Render a selected excerpt/result locally if useful, but do not expose its original ChatGPT conversation link.
- Internal DBS invite/mail/prep facts are for scene-setting only; do not leak internal logistics or email content.

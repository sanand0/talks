---
title: "Dharmendra Team Coding Agent Log Analysis"
date: 2026-10-01T21:49:27+08:00
source: "https://chatgpt.com/c/6aa10d58-6e58-83ec-bda5-e28eef6a1736?src=history_search"
---

# User

_2026-09-09T07:43:42.196Z_

Go through the Codex / Claude Code logs uploaded by Dharmendra's team members at [https://drive.google.com/drive/folders/1_ItCUi7LCqYkOL68MaJGYLq9UBDQjme3](https://drive.google.com/drive/folders/1_ItCUi7LCqYkOL68MaJGYLq9UBDQjme3)

Download them on to [LocalMCP](/plugins/plugin_asdk_app_69e6c604b4ec8191b8e14bb9e8d7cd52) under ~/Downloads/ai-logs/ for convenience of analysis.

Prepare the data so that it'll be easy for you to analyze the following types of questions:

* What are the most common patterns of mistakes the team is making while using agents - either based on what the agents end up doing and/or vs best practices
* What are common patterns of usage that are non-trivial that are worth creating a skill out of, e.g. someone or a few people (or even no one) doing something well that others are trying to do frequently but poorly
* ...

That sort of things - the aim being what re-usable skills and advice should we create based on this usage log.

Just prepare the data for this. Use relevant skills. Then think about the kind(s) of questions that are worth answering, and prepare an analysis plan with a prioritized list of questions. I'll ask you continue and execute the next step.

# ChatGPT

_2026-09-09T07:43:42.196Z_

The core corpus is downloaded and organized under ~/Downloads/ai-logs/. I stopped short of substantive behavioral analysis, as requested.

Preparation completed:

* Inspected the Drive folder: 18 team-member folders.
* Downloaded 992 candidate Codex/Claude log/archive artifacts, ~1.1 GB, preserving the Drive paths under ~/Downloads/ai-logs/raw/.
* Independently MD5-verified all 992 downloaded artifacts against Drive metadata: 0 missing, 0 size mismatches, 0 checksum mismatches.
* Excluded a large amount of irrelevant Cursor/Cline material. This matters especially for Dharmendra: his upload contains ~20k Cursor installation/project files that would seriously contaminate naive analysis.
* Safely expanded the useful ZIP-only uploads under ~/Downloads/ai-logs/extracted/ (~429 MB).
* Bhagyasree's Codex and Claude archives are effectively empty, so these should count as “no usable data”, not “low usage.”
* Built canonical, non-duplicating symlink trees:

* ~/Downloads/ai-logs/prepared/codex/<member>/...
* ~/Downloads/ai-logs/prepared/claude/<member>/...
* Canonical corpus: **1,425 JSONL logs: 993 Codex + 432 Claude**, from 7 contributors with usable logs.
* Parsed/probed all canonical logs: roughly **380k raw records, zero malformed JSON records**.
* Preserved provenance in prepared/canonical-files.tsv linking every canonical log back to its raw/extracted source.
* Found and inspected existing local tooling rather than reinventing it:

* ~/code/scripts/agentlog.py already supports both Codex and Claude logs.
* codextags.py has extensive Codex session metrics including tool failures, command diversity, tool/skill use, subagents, prompt properties, etc.
* skilluse.py can specifically analyze skill reads and whether the associated executions succeeded.
* Used the relevant local analysis/verification skills, especially data-analysis, expert-lens, evidence-provenance, stability-check, blind-spot, verification-gate, and failure-redteam.

The coverage currently looks like this:

| Member | Codex JSONL | Claude JSONL |
| --- | --- | --- |
| Anshu Kumar | 224 | — |
| Ayush | 122 | 12 |
| Bhanu | 313 | — |
| Rhuthuvarna | — | 103 |
| Vashist | 103 | 233 |
| Vidhya | 1 | 23 |
| dharmendra | 230 | 61 |

There are two preparation items that are not fully complete. I started materializing a prepared/agent-logs.duckdb plus Parquet tables for messages, tool calls/results, errors/signals, contexts and sessions, but that ETL exceeded the individual LocalMCP execution limit. The reproducible script is at ~/Downloads/ai-logs/prepare_corpus.py; I would rerun it from scratch before relying on any partially-created DuckDB. Also, 48 tiny optional Claude sidecar JSON files weren't byte-preserved because gws renders JSON responses instead of writing their raw bytes. These are mostly subagent metadata such as agentType; the primary JSONL logs already contain the important subagent/session information, so this doesn't block the analysis.

For the next phase, I would prioritize the questions as follows.

1. **Where is the avoidable rework?** Build a workflow-level failure taxonomy from traces: repeated command/tool failures, retries without changing hypothesis, rollbacks, aborted turns, unnecessary rewrites, failure to inspect before editing, and failed verification. Separate user-caused, agent-caused, tool/environment-caused, and ambiguous failures. This is probably the highest-yield source of concrete advice.
2. **Which missing behaviors most predict bad outcomes?** Specifically test inspect-before-edit, test/verify-after-edit, root-cause diagnosis after failure, narrow scope, incremental execution, and evidence before claiming completion. Compare matched sessions rather than merely counting examples. This should identify skill candidates such as a verification gate or failure-recovery playbook.
3. **What recurring workflows have high variance in execution quality?** Cluster session objectives plus tool-sequence patterns. The most promising skill candidates are frequent workflows where some examples are substantially cleaner/faster/more successful than others.
4. **Who has “champion examples” worth generalizing?** For each frequent task family, find unusually effective sessions: fewer failed calls/retries, less churn, good inspection/testing, appropriate delegation, strong final verification. Extract the *procedure*, not “person X is better.”
5. **What do people repeatedly struggle through that should become a skill/tool?** Look for repeated sequences such as repo exploration, debugging test failures, browser/UI verification, extracting data, modifying spreadsheets/docs, searching unfamiliar code, dependency setup, etc. A repeated 8–15-step sequence is a strong candidate for codifying.
6. **How well do people recover from failures?** After a failing tool call, classify the next move: repeat unchanged, tweak syntax, gather diagnostic information, change strategy, ask the user, abandon, or fix root cause. Good recovery sequences are especially valuable skill material.
7. **What prompt patterns cause requirement churn?** Relate first-prompt specificity, constraints, decomposition and requested verification to subsequent user corrections, number of turns, rollbacks, tool failures and session length. The output should be practical prompting advice, not generic “write better prompts.”
8. **Are people actually using available skills/playbooks, and do they help?** Use skilluse.py plus outcome metrics. More importantly, find frequently occurring workflows where an existing relevant skill is *not* used, or where users reproduce that skill manually and inconsistently.
9. **When does delegation/subagent use help?** Compare well-scoped delegation with unnecessary delegation, duplicated exploration, weak synthesis, or subagent results being ignored. Claude gives particularly good visibility into this through sidechains/subagents.
10. **What recurring environment/tool friction should be fixed once rather than coached repeatedly?** Repeated path, shell, permission, dependency, CLI, output-size, or API-interface failures may imply an agent-friendly CLI/tool improvement rather than a user skill.
11. **Where is context being wasted?** Look at repeated broad scans, giant outputs, unnecessary rereads, compactions, repeated explanations, and long debugging loops. Distinguish useful deep work from context-window inefficiency.
12. **What good practice is almost nobody doing?** This is the blind-spot analysis: identify expected best-practice actions that are systematically absent—tests, independent verification, reading project instructions, checking git state, inspecting existing implementation first, etc. These can produce skills even when there is no internal champion example.

I would treat comparisons such as “Claude vs Codex” or raw rankings of team members as lower priority. They are heavily confounded by task mix, period, experience, log coverage and agent version. The useful unit is generally the **workflow pattern**, normalized for exposure/task type, with individual sessions used as exemplars.

The highest-value next step is therefore: finish the DuckDB materialization, create intent/workflow clusters, derive retry/failure/verification features, and execute questions 1–6 first. Those are most likely to produce a short list of reusable skills backed by multiple concrete traces rather than generic agent-usage advice.

# User

Go ahead with the next step.

# ChatGPT

I completed the first substantive analysis pass over the prepared corpus: **1,112 top-level sessions from 7 contributors**, spanning August 29, 2025–September 3, 2026. The underlying 380,200 JSON records parse cleanly.

The most important finding is not what I expected: **the team generally does inspect before editing; the weak point is validating what they finally changed.**

| Priority | Finding | Evidence | What I’d do |
| --- | --- | --- | --- |
| **P0** | Final verification is usually missing | Of 528 Codex editing sessions, 75.9% inspect before editing but only **2.3%** run a recognized test/build/lint/typecheck after the final edit. Claude: 93.9% inspect first, only **3.0%** final programmatic validation; **11.1%** if browser validation counts. | Strengthen/enforce existing code + verification-gate + webapp-testing; don't create another verification skill. |
| **P0** | After a failed edit, **re-read before retrying** | Claude edit mismatches: after re-reading/inspection, the next edit failed **1/68 = 1.5%**. Changing the edit arguments and retrying without inspection failed **12/15 = 80%**. | Add this tiny explicit rule to code: failed Edit/apply_patch → re-read/search exact target → then minimal retry. |
| **P0/P1** | Lots of friction is environmental, not a user-skill problem | 82 wrong path/cwd events, 41 invalid tool inputs, 31 git-state, 29 missing command/dependency, 17 auth/permission, 15 shell quoting. Separately, **251 Codex quota errors** across 15 sessions plus model/config/Foundry connection errors. | Fix config/platform/tooling centrally rather than teaching workarounds. |
| **P1** | Running/setup/deploying apps is a recurring high-friction workflow | 71 sessions across 6 people; ~21% contain mechanical friction. | There is already a run skill. Audit and strengthen it; improve triggering rather than inventing a duplicate. |
| **P1** | Debugging is another high-friction family | 115 sessions; ~21% contain mechanical friction. | Encode reproduce → inspect evidence → one hypothesis → smallest fix → rerun failure → regression check. |
| **P1** | UI work is frequent but rarely closed with visual validation | 317 UI/frontend sessions; final validation only ~4.5% overall under the conservative definition. | Auto-trigger webapp-testing for visible UI changes. |
| Later | Very long sessions merit context-management study | 53 Codex sessions compacted; median **295 tool calls** versus 21 for all Codex sessions. | Investigate matched long sessions before creating a context-hygiene skill. |

The failed-edit result is particularly strong. I independently re-derived it after finding and correcting a feature-engineering bug. It suggests a very specific rule rather than generic “retry less” advice. In fact, exact unchanged retries were only **19 of 684** actionable failure-recovery events, so teaching “don’t blindly retry” broadly would target a relatively uncommon problem.

There are also useful champion traces—not rankings of people, but procedures worth copying. Anshu Kumar’s Codex session 01a05c8d-1933-71e1-a0d7-dbae757e227d ends with patch → targeted unit tests → rebuild derived data → inspect results → git diff. Rhuthuvarna’s Claude session ca806ccc-d30e-491c-9aed-aedb436aeccb does inspection → phase-scoped edits → targeted pytest → discovers correct venv → reruns tests → git status/diff. Dharmendra’s Claude session 9a892f8d-7395-4577-8de0-361ebef6c6e2 is a good browser-oriented loop: run locally → browser inspect → edits → browser/console checks while avoiding remote Git mutation.

A useful negative finding: I tried unsupervised clustering of the prompts and discarded it. Even the best tested clustering had silhouette ≈0.08 and was dominated by IDE boilerplate and project filenames. Transparent task categories and actual tool sequences are much more defensible here.

I also checked these conclusions against current OpenAI and Anthropic guidance. OpenAI explicitly recommends improving the development environment, persistent repo guidance, issue-like task descriptions, and verifiable test/log evidence; Anthropic describes an “explore, plan, code” workflow and emphasizes testing/verification. The corpus suggests the team has picked up much of the exploration behavior but not the verification closure. [OpenAI](https://openai.com/business/guides-and-resources/how-openai-uses-codex/?utm_source=chatgpt.com)

The detailed reproducible report is at ~/Downloads/ai-logs/analysis/findings.md. The queryable corpus is prepared/agent-logs.duckdb, with Parquet exports and all analysis scripts/results under analysis/.

The highest-value next step is to turn the first three interventions into concrete skill changes—**verification completion gate, failed-edit recovery, and improved run workflow**—then evaluate them against held-out traces/examples rather than merely writing plausible SKILL.md files.

# User

_2026-09-12T01:36:55.955Z_

Go ahead with the next step.

# ChatGPT

_2026-09-12T01:36:55.955Z_

Completed the next step. I converted the findings into concrete skill changes and tested them against a deterministic 30% stability split of the corpus.

The strongest result is the code skill patch. It adds only two bullets:

> After the **last** code/config edit, run the smallest independent check of changed behavior. An earlier test does not verify later edits.

> If an anchored edit fails because the target no longer matches, **re-read/search the current target before retrying**.

The validation split strongly supports both. Of 208 editing sessions, **201 (96.6%) had no recognized final validation**. For Claude edit mismatches, inspect-before-next-edit produced **1/40 = 2.5%** next-edit failures; non-inspection recovery produced **14/21 = 66.7%**. Across the full corpus, changed-retry without inspection fails **76.5%**, versus **1.5%** after inspection.

I also produced a one-line webapp-testing patch requiring validation after the final UI edit. In the validation split, **81/84 UI editing sessions** lacked recognized final browser/programmatic validation.

The third intervention is now clearer. Claude’s bundled run skill is already good; I recovered its actual instructions from the logs. The problem is triggering/availability. A strict filter finds **49 explicit “how to run / run this app / run locally / launch” requests**: 35 Codex and 14 Claude. Claude invoked run in only **1/14**; Codex had no equivalent invocation. In the validation split there are **14 direct run/start requests and zero run uses**. I therefore created a compact cross-agent run-app fallback rather than redesigning Claude’s skill.

The recommended rollout is:

1. Apply ~/Downloads/ai-logs/proposed-skills/code.diff.
2. Apply ~/Downloads/ai-logs/proposed-skills/webapp-testing.diff.
3. Make Claude’s run behavior available/triggerable for Codex; candidate fallback is ~/Downloads/ai-logs/proposed-skills/run-app/SKILL.md.
4. Do **not** create another generic verification skill—verification-gate is already strong. Do **not** yet create “plan first” or context-hygiene skills; the evidence is too confounded.

I could not install the first two patches into ~/code/scripts/agents/ directly because those skill files are mounted read-only here. The candidates are ready and minimal.

The reproducible evaluation is at:

~/Downloads/ai-logs/analysis/eval/heldout-evaluation.md

The rollout/pilot plan is:

~/Downloads/ai-logs/analysis/eval/adoption-plan.md

and the evaluator is:

~/Downloads/ai-logs/analysis/eval/evaluate_rules.py

One caveat: this 70/30 split is a **stability test, not a pristine holdout**, because the hypotheses were initially noticed using the full corpus. I therefore set up the more important test as a prospective two-week pilot on new logs, measuring final-validation coverage, failed-edit recovery, run triggering, and tool-call overhead.

# User

Hold on, these are logs from OTHER people's machines. They're not using my skills at all!

Given this, what would you suggest, prioritized, and why?

# ChatGPT

Yes. That changes the recommendation materially. My previous step incorrectly treated these as candidates for improving your own local skill set. They are much more valuable as evidence for a **shared Straive agent operating system**: defaults, skills, and tooling that Dharmendra’s team can adopt.

I’d prioritize these:

1. **Create a shared “finish the job” coding skill/default.** This is the clearest, broadest gap. Inspection before editing is already common: ~76% of Codex and ~94% of Claude editing sessions. But final validation is almost absent: ~2–3% programmatically, and only ~11% for Claude even counting browser checks. The skill should be tiny: after the final edit, run the smallest relevant test/build/typecheck/API/browser check; otherwise explicitly say unverified. This is probably the single highest-leverage behavioral change because it applies to nearly every coding task.
2. **Create an edit-failure recovery rule: “re-read, then retry.”** This is unusually strong evidence for a very small intervention. When Claude’s edit failed because its anchor was stale, re-reading before the next edit led to only ~1.5–2.5% immediate re-failure. Changing the edit and trying again without re-reading failed ~76%. This belongs in the common coding skill, not as a separate skill. It is specific enough that agents can reliably follow it.
3. **Give everyone a shared run-app skill.** There were 49 explicit “how do I run this app / run locally / launch this” requests. Claude’s bundled run behavior appeared only once; Codex effectively had nothing comparable. This workflow recurs enough to standardize: inspect existing project instructions → reuse current environment → launch the actual user-facing boundary → exercise one representative interaction → capture any non-obvious startup recipe for next time. This is exactly the kind of repeated rediscovery a skill should eliminate.
4. **Make UI changes automatically trigger browser verification.** UI/frontend work is huge: 317 sessions. Yet final UI validation is roughly 4–5%. A shared UI skill should say: after the last visual/interaction edit, navigate to the affected state, exercise the interaction, check console errors, and inspect a screenshot if appearance changed. I would make this an automatic companion to coding rather than something people have to remember to invoke.
5. **Fix environment friction centrally instead of teaching people to work around it.** There are dozens of wrong-path/cwd, missing-dependency, shell quoting, git-state, invalid-tool-input and permission failures. More importantly, there were 251 Codex quota errors across 15 sessions plus model/config/Foundry errors. These are not primarily “prompting mistakes.” Dharmendra’s team should get a known-good agent environment: standard shell, PATH, Git, Node/Python, model config, LLM Foundry settings, useful CLI tools, and repo-level instructions. A one-time platform fix will beat another training session.
6. **Turn recurring project-specific setup into repo-local skills.** The global run-app skill should discover and defer to .claude/skills/..., AGENTS.md, or equivalent repo instructions. Whenever an agent has to discover “install X, set Y, use port Z, run command Q,” that discovery should become an asset. This is where your proposed reusable Agent Skills Repository becomes especially useful: global skills for universal procedures, repo skills for project-specific mechanics.
7. **Only then build workflow-specific skills from repeated use cases.** The best candidates from these logs are debugging, app setup/run, UI modification/testing, LLM Foundry integration, and possibly data/demo regeneration. But I would first collect 5–10 strong and weak traces for each and extract the actual procedural difference. Don’t turn “people do this often” directly into a skill; require evidence that a repeatable procedure separates good runs from painful ones.

I would **not** prioritize generic prompting training, “plan before coding,” or “use agents better.” The data does not strongly support those. Likewise, I would not rank individuals: task mix, Claude/Codex differences, history length, and environment vary too much.

The practical rollout I’d use is very small:

* **Shared coding skill:** final verification + failed-edit recovery.
* **Shared run-app skill:** real launch + representative interaction + capture setup knowledge.
* **Shared UI-testing skill:** browser check after final UI edit.
* **Standard environment checklist/tooling:** remove avoidable platform failures.
* Instrument usage for 2–3 weeks and see whether final-validation coverage rises from ~3% toward >50%, edit retry failures fall sharply, and repeated “how to run this?” sessions become shorter.

That would also make this corpus a good **first evidence-backed contribution to Straive’s shared Agent Skills Repository**: not “skills Anand likes,” but skills derived from observed agent usage and measurable failure modes.

# User

What would be the minimal skill files for these?

# ChatGPT

I’d keep it to **three shared skills**. Don’t create separate skills for verification, edit recovery, environment setup, debugging, etc.; that fragments behavior and makes triggering harder.

### 1. code/SKILL.md

This should be the default whenever an agent edits code. Add only the two behaviors the logs strongly support.

Markdown

`--- name: code description: Use whenever modifying code or configuration. --- - Inspect the relevant code before editing. - After the **last code/config edit**, run the smallest relevant independent check: targeted test, build/typecheck/lint, API smoke test, browser check, or `git diff --check`. An earlier check does not verify a later edit. If a meaningful check cannot run, say **unverified** and why. - If an anchored edit (`Edit`, `apply_patch`, replacement) fails because the target no longer matches, **re-read/search the current target before retrying**. Then make the smallest corrected edit.`

That alone addresses the two strongest findings.

### 2. run-app/SKILL.md

Trigger on “run this”, “how do I run this?”, “launch”, “start locally”, etc.

Markdown

`--- name: run-app description: Use when asked to run, launch, start, open, or smoke-test an application. --- Running means exercising the **actual application boundary**, not merely importing code or starting a process. 1. Look for existing repo instructions or a repo-local run skill first. 2. Reuse the project's existing environment and commands; don't reconstruct dependencies unnecessarily. 3. Launch the real boundary: - CLI → run a representative command. - API/server → start it and hit a route. - Web app → start it and open it in a browser. - Desktop/TUI → launch it and perform one interaction. 4. Verify one user-visible/useful postcondition. 5. If startup required non-obvious setup, record the working recipe in the repo for next time.`

I would make this available to both Claude and Codex. Claude’s bundled version is richer, but this is probably enough for a shared baseline.

### 3. test-ui/SKILL.md

Only trigger after UI/frontend changes.

Markdown

`--- name: test-ui description: Use after modifying user-visible web UI or interactions. --- After the **final UI edit**: 1. Open the affected state in a real browser. 2. Exercise the changed interaction. 3. Check for console errors. 4. If appearance/layout changed, inspect a screenshot. A page merely loading is not sufficient verification of interactive or visual behavior.`

I would **not** create skill files for the other recommendations yet.

Environment problems such as quota, unsupported models, PATH/dependencies, and LLM Foundry configuration belong in **platform defaults / bootstrap tooling**, not a skill. Repo-specific startup knowledge belongs in each repo’s AGENTS.md or .claude/skills/..., not in the global run-app skill. And I would defer generic debugging, planning, and context-management skills until the logs show a crisp procedure with measurable benefit.

So the minimal architecture is:

Plain text

`skills/ code/SKILL.md run-app/SKILL.md test-ui/SKILL.md`

The important design choice is that code is the default baseline, while run-app and test-ui are narrow, obvious triggers. Three short files are much more likely to actually fire and be followed than a comprehensive “agent best practices” manual.

# User

Save the skills in ~/Downloads/ai-logs/skills/

Draft an email to Dharmendra summarizing the findings. I will include the skills as attachments.

Use relevant skills when writing this and make this actionable for Dharmendra. For example, knowing HOW his team is using coding agents - both effectively AND ineffectively - can help him spread good practices and curb bad ones. He can form a mental model of the team's processes. See past transcripts with Dharmendra to understand his perspective, level of understanding, and get a picture of him in your mind. Use THAT, combined with the learnings so far (and feel free to dig deeper with more analysis) to help him help his team leverage coding agents effectively.

In the light of this, the skills (which you're welcome to revise) are just one slice of the recommendation.

Use relevant skills. Back claims / suggestions with vivid examples - examples are the key to understanding.

# ChatGPT

Saved the three installable skills under ~/Downloads/ai-logs/skills/, with uniquely named attachment copies (code-SKILL.md, run-app-SKILL.md, test-ui-SKILL.md). I also created ~/Downloads/ai-logs/coding-agent-skills.zip.

I’d send Dharmendra something like this:

Email

From

What the coding-agent logs are telling us


---

Dharmendra,

I went through the Codex / Claude logs from the team. About 1,100 top-level sessions across 7 people.

Actually, these logs are more useful than I initially realized because these are from their machines. They are not using my skills or setup. So this is reasonably close to seeing how people naturally work with coding agents.

The biggest takeaway is very close to what you said in our last discussion: the coding part has become very fast, but testing and ownership have not automatically followed.

Your "tuck tuck tuck, I'm done" description is unfortunately quite visible in the logs :-)

There is quite a bit the team is doing well.

For example, before making the first edit, the agent inspected the existing code in about 76% of Codex editing sessions and 94% of Claude sessions. So people are generally not just asking AI to blindly rewrite things.

There are also some very good individual workflows.

In one Anshu session, the sequence after the final patch was roughly:

patch -> targeted unit tests -> rebuild the cache -> inspect the generated data -> git diff.

That's excellent. The agent didn't stop when the code was written. It checked whether the thing actually worked.

Rhuthuvarna has another nice example: inspect the code/tests/docs -> make a plan -> edit -> run pytest -> discover the correct environment -> rerun targeted/full tests -> inspect git status/diff.

And one of your own Claude sessions is a good UI example. It actually ran the app, used the browser after the changes, checked the interaction/state, and looked at the Git state.

I think these are worth showing in AI Builders. Not the prompts. The *process*. "Here is what a good agent session looks like."

The biggest problem is what happens at the end.

After the final edit, I could recognize a proper programmatic validation in only about 2% of Codex editing sessions and 3% of Claude sessions. Even if I count Claude browser checks, it becomes only about 11%.

This is a conservative measurement and I may miss checks people did outside the agent. But the gap is far too large to ignore.

So I think the first team habit should simply be:

**After the last edit, show me evidence that the changed behavior works.**

A targeted test is enough. Or build/typecheck. For an API, call it. For UI, open the affected state in the browser and use it.

Importantly, a test that ran *before* the last edit doesn't count.

There was another surprisingly sharp pattern.

Sometimes an Edit fails because Claude's view of the file is stale. For example:

"String to replace not found."

In a few sessions the agent then changes the edit slightly and tries again. Sometimes repeatedly. There are also examples of it repeatedly getting:

"File has not been read yet. Read it first before writing to it."

Across these edit failures, when the agent first re-read the target before trying the next edit, the next edit failed only 1 out of 68 times.

When it just changed the edit and retried without re-reading, 13 out of 17 next edits failed.

That's a wonderfully small habit to spread: **edit fails -> re-read -> edit again.**

I've attached a tiny `code` skill which mainly captures these two things.

One thing I would change slightly from our earlier discussion on ownership.

I don't think we should require the developer to understand every line AI has written. If we do that, we'll probably give back a lot of the productivity.

But I do think the developer must own four things:

1. Is this the behavior we wanted?
2. What changed in the final diff? Did AI add anything we didn't ask for?
3. What evidence says it works?
4. What is still uncertain?

This also addresses your "there are 40 extra things and nobody owns those 40 things" problem. The agent can know more than the developer. Fine. But if it has added an extra metric, tab, API, dependency, etc., somebody should either justify it or delete it.

Your "explain this to me in one page / draw me the flow" technique is useful here, especially for handoff. I would keep doing it. But I wouldn't use explanation as a substitute for testing.

Two other repeated patterns seem worth fixing.

There were 49 fairly explicit "how do I run this / run this locally / launch the app" requests. People keep rediscovering how applications start. I attached a small `run-app` skill for this.

More importantly, once somebody has discovered that "this repo needs this environment variable, this command and this port", we should save that in the repo. The global skill should be generic. The project-specific knowledge should compound.

UI work is also very common: 300+ sessions. But browser validation after the final UI change is rare. So I've attached a tiny `test-ui` skill: go to the affected state, actually exercise the changed interaction, check console errors, inspect a screenshot if visual appearance changed.

There is also some stuff I would *not* solve with skills.

For example, I found 251 Codex "quota exceeded" errors, plus model/config errors and stream disconnects. There are also repeated path/cwd, missing dependency, Git-state and tool-input errors.

Some of those are user/agent discipline. But quota, model defaults and connectivity should be fixed centrally. We shouldn't train 20 people to work around a broken default.

What I suggest we do:

Pick 3-4 active users and give them these three skills for two weeks.

In the AI Builders meeting, spend maybe 15 minutes each week on one real trace:

* one that worked particularly well;
* one where the agent got into an avoidable loop.

No ranking of people. Just "this procedure works; this one wastes time."

Then collect their logs again. We can measure whether:

* final verification has gone up;
* failed edits are re-read before retrying;
* run/setup knowledge is being reused;
* the skills themselves are actually getting invoked.

If these move, put the skills into the central repository. Then we have both the asset and proof that it changes behaviour, which is what we were discussing earlier.

The three attached skills are deliberately very small. I wouldn't create 20 skills from these logs yet. Better to change three frequent behaviours first and see what happens.

Anand

The draft is deliberately framed as “here is how your team actually works, and how to improve the operating model,” rather than as an audit of individual people. I can also compress it to roughly half this length if you want a quicker email.

# User

Removed the "Actually, these logs are " para as irrelevant.
Simplified next to "You're right: coding part has become very fast, but testing and ownership have not followed."
Broke sections a bit, reworded / reformatted a little bit, but mostly sent this as-is after review.
FYI - no response required.

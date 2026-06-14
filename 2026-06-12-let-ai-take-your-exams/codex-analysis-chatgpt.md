---
title: "Codex Exam Performance Analysis"
date: 2026-06-14T15:33:38+05:30
source: "https://chatgpt.com/c/6a2e7ab3-e340-83ec-9420-04b9cfc3e20b"
---

## User

Analyze how Codex solved https://exam.sanand.workers.dev/2026-06-test Use Local MCP bash to look at: - ~/r2/files/blog/2026-06-12-let-ai-take-your-exams/ - which has Jaideep's solution using Codex on his ChatGPT Pro account. It got 10/10 - ~/.codex/sessions/2026/06/12/rollout-2026-06-12T14-48-26-019ebb20-24f9-7ea2-b13c-17c49fd40308.jsonl - which has my Codex solution my ChatGPT Plus account. I interrupted it after 9/10 because I was eating into my credits. - ~/code/exam/src/exam-2026-06-test.js - which has the source of the exam questions. Inspect the q-\*.js in the same folder for the question details and solutions. How did Codex solve the questions? Did it make mistakes? If so, how did it recover? Based on the transcript at ~/code/talks/2026-06-12-let-ai-take-your-exams/transcript.md what are the questions / hesitations students have in their minds about using AI coding agents like Codex to solve the problem, and what do the session logs reveal in response to those questions / hesitations? Analyze exhaustively and share a detailed report in simple concise language.

---

## ChatGPT

Worked for 5m 23s

## Executive summary

Codex did not solve the exam like a student reading questions and reasoning aloud. It solved it like a forward-deployed engineer.

It found the question source, read the validators, generated local solvers, used browser automation to fill answers, used the live “Check” buttons as feedback, and recovered from errors until the page accepted the answers.

Jaideep’s Codex run got **10/10**. Your Codex run got **9/10** before interruption, with the only remaining point blocked by an **invalid AIPipe bearer token**, not by inability to solve the rubric.

The biggest finding: this exam tests not just “knowledge,” but whether a human or agent can operate a verifiable environment. Codex was strong because the exam exposed feedback loops: source code, validators, error messages, external APIs, downloadable files, and check buttons.

---

## Files inspected

I inspected:

`~/code/exam/src/exam-2026-06-test.js` and the ten `q-*.js` modules.

`~/r2/files/blog/2026-06-12-let-ai-take-your-exams/`, especially Jaideep’s Codex rollout, redacted report, and markdown transcript.

`~/.codex/sessions/2026/06/12/rollout-2026-06-12T14-48-26-019ebb20-24f9-7ea2-b13c-17c49fd40308.jsonl`, your interrupted Codex run.

`~/code/talks/2026-06-12-let-ai-take-your-exams/transcript.md`.

Sensitive tokens and email-bound JWTs were treated as credentials and not reproduced here.

---

## What the exam actually tested

The exam had 10 questions, totaling 10 marks. The source file explicitly labels the capability behind each question:

1. Verify and fix AI-generated code.
2. Build binary evaluation rubrics.
3. Repair missing context in a prompt.
4. Reconcile numbers in a data narrative.
5. Detect chart-axis manipulation.
6. Find hallucinated APIs across 1,000 Python files.
7. Write property-based tests to expose hidden bugs.
8. Solve a limited-query network investigation game.
9. Optimize a prompt across multiple model profiles.
10. Fix a color-encoding mismatch.

This matters because Codex used the exam’s own structure. The source defines seeded per-user variants, validators, weights, and feedback behavior. For example, the manifest labels Q6 as “Detecting hallucinations at scale,” Q8 as “Problem breakdown and efficient experimentation,” and Q9 as “Robust optimization and model-aware prompting” in `exam-2026-06-test.js`.

---

## How Codex solved the exam overall

Codex used this loop:

First, it inspected the page. It realized the exam was a client-side assessment shell, not a static page. It then inspected DOM, network traffic, bundled JavaScript, and source files.

Second, it read validators. For many questions, the key was not “what sounds right?” but “what exact input will the checker accept?” This is why Codex looked for functions, error messages, expected phrases, seeded random choices, and tolerance checks.

Third, it generated small scripts. It wrote Node/Python snippets to evaluate seeded questions, search combinations, parse ZIP files, score graph nodes, and fill browser fields.

Fourth, it used the live Check buttons. This was critical. When an answer failed, Codex read the validator feedback and repaired the answer. The exam rewarded iterative correction.

Fifth, it saved only after validation. Jaideep’s run reached `Score: 10 / 10` and submitted. Your run reached `Score: 9 / 10`; Q2’s rubric text was completed, but the AIPipe judge rejected the bearer token with a signature verification error.

---

## Question-by-question analysis

### Q1. Verify and fix AI-generated code

The question source randomly generates buggy JavaScript scenarios. Examples include “most frequent element,” “validate email,” “flatten array,” “group by,” “compound interest,” and similar tasks. The validator requires JSON with `bugs`, `fixedCode`, and `testStrategy`, then executes the submitted function against hidden/generated test cases.

Codex solved this by identifying the actual bug, writing corrected JavaScript, and adding a test strategy mentioning edge cases. In Jaideep’s run, the visible scenario was “most frequently occurring element,” where the bad code returned the maximum value instead of the most frequent value. In your earlier visible field, the email-validation variant appeared.

Mistakes: none significant. This is the kind of question chat models can often solve directly, and Codex passed it early.

What this reveals: simple AI-output verification is close to free marks if the student gives the whole question and uses the checker.

---

### Q2. Build a binary eval rubric

This question asks for exactly N yes/no checks that distinguish GOOD, MEDIOCRE, and POOR outputs. The validator then uses AIPipe to call an LLM judge many times. The source shows it requires a token and makes many judge calls concurrently.

Jaideep’s variant was about SQL query quality. Codex wrote checks like whether the SQL uses CTEs, null handling, joins, filtering, grouping, and so on. It initially could not validate because no AIPipe token was available. After the user provided a token, Codex tried to inject it into the page, failed because the page global was locked, then recovered by using the browser prompt the page opened. Q2 passed and the score became 10/10.

Your variant was about API endpoint documentation quality. Codex wrote six checks covering method/path, content type, authentication, concrete request payload, success status/response, and multiple error status codes. The page showed “Correct” feedback for the rubric content, but the external judge rejected the bearer token with `JWSSignatureVerificationFailed`. The score stayed 9/10.

Mistakes and recovery: Jaideep’s Codex first tried setting `globalThis.aiPipeToken`, then `window.aiPipeToken`; both failed. It recovered by interacting with the native prompt. Your run hit an authentication blocker, not a reasoning blocker.

What this reveals: the hardest part was not designing the rubric. It was credential handling, external cost, and validator execution. This directly matches student worries about paid access, token budgets, and setup friction.

---

### Q3. Presentation prompt structural repair

The source defines six load-bearing prompt components: audience, output format, data grounding, tone/style, length, and action recommendation. Each user gets a prompt missing exactly three components. The validator searches for both the missing component labels and concrete detection phrases.

Codex solved this by reading the component validator rather than guessing. It identified which three components were missing, preserved existing requirements, and inserted the exact missing constraints.

Jaideep’s run needed to add items such as the primary metric `forecast_error_pct`, an NYT graphics team style, and a numeric length constraint. Your run initially used semantically plausible phrasing but had to tighten wording to satisfy the validator.

Mistakes and recovery: generic “good prompt” repairs were not enough. Codex recovered by inspecting the source and adding validator-detectable phrases, such as “between 110 and 160 words” or the seeded target metric.

What this reveals: context engineering questions are not only about writing well. They are about preserving constraints exactly.

---

### Q4. Data-narrative number reconciliation

This question provides a table and a paragraph with some planted wrong quantitative claims. The instruction is to fix only the wrong values and leave correct claims unchanged.

Codex solved it by extracting/generated the seeded data, computing the correct values, and identifying the planted wrong indices.

In Jaideep’s run, Codex found these planted errors: April units sold, February average revenue per unit, May-to-June return-rate direction, and July online order share. It also correctly left a decoy Q4 revenue claim unchanged.

Mistakes and recovery: Jaideep’s answer initially failed because the checker searched numeric fingerprints. The value `$105,128` contained `512`, which confused the July share fingerprint check. Codex recovered by reordering the paragraph so the July online share appeared before the Q4 revenue value.

What this reveals: even when the reasoning is right, validators can be brittle. A coding agent can still adapt if it reads the feedback precisely.

---

### Q5. Axis scale manipulation repair

This question gives broken Chart.js HTML and asks for corrected chart HTML plus an explanation of the manipulation and distortion.

The source has several manipulation families: truncated axes, dual-axis scaling, inverted axes, and log-scale compression. The validator checks for a corrected chart, a distortion value within tolerance, and specific manipulation phrases.

Codex solved it by reading the generated scenario and the accepted phrase set. In your run, the manipulation was an inverted y-axis: the chart visually made satisfaction look like it was rising even though the series declined. The accepted phrase included “inverted axis flips decline narrative.” In Jaideep’s run, the issue was a log-scale compression case, and the corrected chart needed a linear scale.

Mistakes and recovery: Codex initially wrote semantically correct explanations but missed exact validator phrases and syntax. In Jaideep’s run, the validator wanted literal `type: "linear"` rather than JSON-escaped syntax. In your run, it needed the exact accepted phrase for inverted axis manipulation. Codex recovered by reading the source phrase matcher.

What this reveals: visual judgment was solvable, but the grader rewarded exact evidence and exact repair language.

---

### Q6. LLM hallucination trap matrix

This question asks the student to download a ZIP of 1,000 Python files and identify the one file that contains only real API calls. The generator creates one correct script and 999 scripts with one to three hallucinated API calls. The source shows the correct script ID is seeded by user email.

Jaideep’s Codex found the answer by evaluating the exam source/generator locally. Its answer was `script_152.py`.

Your Codex run downloaded and extracted the ZIP, then built an analysis pipeline. The first naive AST allow-list produced many false candidates because some scripts had only “plausible-looking” calls but still contained subtle fake APIs like `response.code`, `json.ParseError`, or `timedelta(weeks_days=7)`. Codex then improved the method: group scripts by template, compare line positions across many variants, ignore randomized dummy lines, and find the modal real API choices. That isolated `script_666.py`, which the live validator accepted.

Mistakes and recovery: the early filter was too permissive. Codex recovered by using the structure of the generator: only the true script uses the first, real option at every mutable API position.

What this reveals: the agent did not “read 1,000 files.” It built a cheap static-analysis pipeline. This is exactly the scalable behavior the question was testing.

---

### Q7. Bug hunter property-based testing

This question asks for a Hypothesis property test that fails on a seeded buggy implementation but passes on the correct implementation. The source runs the submitted Python test in Pyodide and checks whether Hypothesis discovers the bug within 1,000 generated examples.

Codex solved it by reading the seeded bug scenario and designing a generator that hits the risky region. In your run, the important failure region was “any window that contains exactly one zero value.” Codex wrote a property test that forces the counterexample instead of hoping random generation finds it.

Mistakes: none major in the logs. It passed in both runs.

What this reveals: property-based testing is a good AI-agent task because the agent can turn a vague “find edge cases” instruction into executable randomized tests.

---

### Q8. Network game: Graph Detective

This was the most agentic question. The external game gives an anchor node, a limited query budget, clues, and requires the compromised node plus a shortest path from the anchor. The exam accepts only a completion JWT from the game server.

Both runs converged on the same solution: compromised node `91`, shortest path `13 → 72 → 91`.

Codex solved it by opening the game, reading its inline JavaScript, discovering API endpoints such as `/detective/start`, `/detective/node/{id}`, `/detective/sample`, `/detective/submit`, and `/detective/clear`, then querying nodes programmatically. It scored nodes against the clues: enormous outgoing volume, very low transaction count, very low in/out ratio, few counterparties, and high average transaction size. Node 91 was unambiguous: volume 24,000, transaction count 3, in/out ratio 0.03, counterparty count 5, and average transaction size 9,480.

Mistakes and recovery were important here. Jaideep’s Codex guessed nodes 5, 49, and 22 too early. The game rejected them and ended the session after three wrong guesses. Codex then learned that the failed state persisted by email/week. It discovered a `/detective/clear` endpoint, first called it without the week, then without the token, then finally with both week `2026-W24` and the session token. That reset the game. After that, it mapped the graph using resettable sessions, computed the shortest path, and submitted only once on a clean session.

Your run was more efficient on the final game path. It mapped enough frontier nodes, restarted with a fresh query budget, submitted node 91 with path `13,72,91`, and the server confirmed `correct_node`, `path_valid`, and `path_is_shortest`.

What this reveals: the game exposed the biggest difference between chat AI and coding agents. A chat model might reason vaguely. Codex used APIs, state, graph search, scoring, and server feedback.

---

### Q9. Multi-model robustness audit

This question gives 21 prompt fragments, model-specific contribution scores, word counts, and target thresholds. The answer must be the shortest set of fragment IDs that meets Macro-Mean and Model Floor thresholds across four models. The source applies a sigmoid to raw scores, checks exact word count, exact mean/floor, and also verifies optimality.

Jaideep’s Codex evaluated the seeded source and found: `I7, I9, I10, I14, I15, I19; 40; 97.23; 94.53`.

Your Codex initially made a subtle mistake: it treated model scores as percentages rather than logits passed through a sigmoid. The validator rejected the mean. Codex inspected the source, found `sigmoid = 1 / (1 + Math.exp(-x))`, reran the exhaustive search, and found: `I8, I11, I13, I17, I20; 59; 97.01; 96.68`.

Mistakes and recovery: this is the cleanest example of why source/validator inspection matters. The first solver was plausible but wrong. The corrected solver used the exact scoring function and passed.

What this reveals: optimization questions are where AI is strongest when it can write code, but weakest if it guesses the math.

---

### Q10. Color encoding mismatch

This question gives broken chart HTML with an inappropriate color palette. The answer must explain the mismatch in an HTML comment and submit corrected HTML using the right palette family: sequential, categorical, or diverging. The source checks perceptual properties like monotonic lightness, CIEDE2000 distances, diverging midpoint lightness, and no rainbow palette.

Jaideep’s variant involved elevation around sea level, where the correct encoding was diverging: negative and positive values should be visually separated around a midpoint.

Your variant involved hospital wait times. The broken categorical palette implied each hospital’s wait time was an independent category, rather than a position on a continuum from fast to slow. Codex initially gave a generic explanation, failed, read the validator’s expected mismatch phrase, inserted the specific continuum explanation, and passed.

Mistakes and recovery: the color fix was not enough. The explanation had to name the exact false implication.

What this reveals: AI can do perceptual design repair if the task is made checkable. It still needs precise language aligned to the rubric.

---

## Mistake taxonomy across both runs

The mistakes were not random hallucinations. They clustered into repeatable types.

First, Codex made **semantic-but-not-validator-compliant answers**. Examples: Q3 length phrasing, Q5 manipulation phrase, Q10 mismatch phrase. These were correct in spirit but failed exact checks.

Second, Codex made **formula/interpretation mistakes**. The Q9 sigmoid error is the best example. It used the right search shape but the wrong score transformation.

Third, Codex made **premature action mistakes**. In the network game, Jaideep’s Codex guessed too early and burned all three wrong guesses. It recovered only after finding the clear endpoint.

Fourth, Codex hit **tooling and browser-state mistakes**. Duplicate DOM IDs, wrong tab, timeouts, locked globals, failed text extraction, and command errors all appeared.

Fifth, Codex hit **credential and budget issues**. Q2 required AIPipe. Jaideep got through after token entry. Your run did not because the token was invalid, and you stopped at 9/10 because the remaining work was eating credits.

The key point: Codex usually recovered when there was feedback. It struggled when the failure was external authentication or budget.

---

## Pro account vs Plus account: what can and cannot be concluded

Jaideep’s Pro run got 10/10. Your Plus run got 9/10.

But the logs do not prove “Pro is smarter than Plus.” The outcome difference is mostly explained by environment and credentials:

Jaideep had a working Chrome flow and eventually a valid AIPipe token. Your run had stricter `rtk`/sandbox friction, more CDP/tooling overhead, and Q2’s token failed with 401.

Your run actually solved the hard technical questions: Q6, Q8, Q9, Q10. The missing point was not conceptual.

So the fair conclusion is: **agent environment quality and credential readiness mattered at least as much as model tier.**

---

## What students were worried about in the session

The transcript shows students were not simply asking “Can AI solve exams?” Their hesitations were more practical and psychological.

They worried that AI hallucinates. They specifically mentioned hallucination on Excel sheets, calculus, multiple tables, and data interpretation.

They worried about missing context. Students said they do not always know what context the model needs.

They worried about input limits and formats: images, multiple images, Markdown, unreadable text, and free-version limits.

They worried about recency: if the model’s training cutoff is old, it may not know new subject updates.

They worried about cost: whether ₹2,000/month or paid tools are worth it.

They worried that using AI feels wrong even when allowed.

They worried that exams might be AI-proof, so trying AI may be wasted effort.

They worried that if AI makes the question and AI answers the question, the human role becomes pointless.

They worried about overconfidence: AI may solve some questions, fail others, and leave too little time.

They worried about privacy: whether giving AI course material, personal data, or private questions is dangerous.

They worried about effort: connecting AI to a URL, copy-pasting, and managing context can itself be work.

They worried about skill loss: if they delegate everything, will they become dumber?

They worried about jobs: if AI writes code, what should they learn?

---

## What the session logs reveal in response to those worries

### “AI hallucinates.”

Yes. But coding agents can be forced into verification loops.

Codex hallucinated or made wrong assumptions several times: wrong Q9 score transform, premature network-game guesses, generic visual explanations, brittle Q4 wording. But because the environment had validators, it recovered.

The lesson is not “trust AI.” The lesson is “give AI a checker.”

---

### “AI needs context, and I don’t know what context to give.”

Correct. Codex’s strongest move was to fetch context itself.

It did not wait for the user to paste all ten questions. It inspected the DOM, downloaded scripts, read source modules, parsed validators, opened the game, and read network APIs.

This suggests a better student prompt is not “answer this question,” but:

“Here is the exam URL. Inspect the page, source, network calls, and validators. Build a manifest of question IDs, constraints, and checkers before solving.”

---

### “Formatting and exact wording cause failures.”

Correct. Many failures were formatting/wording failures.

Q3, Q5, and Q10 were not blocked by reasoning. They were blocked by exact validator expectations. Codex recovered by reading feedback and source.

This is a strong argument for passing error messages back to the agent.

---

### “What if the exam is AI-proof?”

This exam was designed for AI-era skills, but it was not agent-proof.

In fact, the more verifiable and tool-rich the exam was, the more it favored agents. The live checkers, source scripts, downloadable ZIP, and external game API all became affordances.

A truly AI-resistant question would need to restrict feedback, personalize context more deeply, require human taste without an executable oracle, or require live human judgment. But then it may also become harder to grade fairly.

---

### “Will AI waste time in a timed exam?”

Yes, if used naively.

The logs show both speed and danger. Jaideep’s run took long enough to include multiple recovery loops. Your run was still at 9/10 when you stopped because of credits/budget. The transcript also records the concern that a 45-minute exam could be a problem if Codex takes an hour.

The answer is parallelization and triage: run multiple agents, solve low-cost deterministic questions first, defer expensive AIPipe questions, and do not let one hard question consume the exam.

---

### “Is the cost worth it?”

The logs show where cost appears: AIPipe judge calls, model thinking time, browser-agent time, and repeated retries.

But they also show that one successful agent can recover many marks. Jaideep’s 10/10 and your 9/10 make the ROI argument stronger for high-stakes graded work, but only if the student learns to manage token-heavy questions and stop loops early.

---

### “Can I trust AI with private data?”

The logs show both risk and guardrails.

Your Codex run attempted to inspect browser/session state in a way that touched `localStorage`; it was rejected as unsafe. Tokens were redacted in the stored artifacts. But the run still required a user-provided AIPipe token and generated email-bound JWTs.

The practical answer is: agents need credentials to act. Students need explicit trust boundaries and should avoid giving secrets unless necessary.

---

### “Will AI make me less skilled?”

The logs suggest a sharper answer: AI reduces the value of some skills and increases the value of others.

Codex did not remove the need for skill. It shifted the skill from hand-solving to supervising: knowing when to inspect source, when to test, when a validator is brittle, when a result is plausible but wrong, when to stop, and how to recover.

The student skill becomes “catch wrong ones,” not “produce every answer manually.”

---

### “Do I still need programming?”

Yes, but maybe not language memorization.

Codex used JavaScript, Python, shell, DOM automation, CDP, API calls, AST analysis, exhaustive search, graph search, and browser manipulation. The human did not need to hand-code all of that, but the human needs enough programming judgment to understand what the agent is doing and whether its plan is safe.

This supports the transcript’s distinction: programming experience matters more than memorizing a specific language.

---

## The most important non-obvious insight

The exam was not won by “better prompting.” It was won by **better instrumentation**.

The winning behavior was:

Read the source.
Extract the validator contract.
Write small solvers.
Use feedback.
Repair precisely.
Save only after verification.

That is closer to software engineering than prompting.

---

## What a better future prompt should say

A much stronger prompt than “Solve this” would be:

“Open the exam URL and solve it end to end. First inspect the page, source files, network calls, validators, scoring weights, seeded variants, and external dependencies. Build a table of all question IDs, expected answer formats, validator rules, costs, and credentials needed. Solve deterministic/local questions first. For each answer, fill it, run the Check button, read feedback, and iterate until correct. Defer expensive token-gated checks until the end. For downloadable archives, write reproducible scripts instead of manual inspection. For games, inspect the API and maintain state carefully before submitting. Do not guess on limited-attempt tasks. Save only after the page confirms the score. Redact all tokens in logs.”

That prompt directly addresses the mistakes seen in both runs.

---

## Final assessment

Codex solved the exam because the exam was highly verifiable. It made mistakes, but the mistakes were recoverable because the system exposed feedback.

Jaideep’s run demonstrates the upper bound: a coding agent with browser access, source inspection, live validation, and a valid token can get 10/10.

Your run demonstrates the realistic bound: even with tooling friction and token issues, Codex solved 9/10 and the remaining failure was external authentication, not exam reasoning.

The strongest message for students is not “AI will take your exams.” It is:

AI can attempt the exam.
The human’s job is to build, choose, and supervise the verification loop.

---

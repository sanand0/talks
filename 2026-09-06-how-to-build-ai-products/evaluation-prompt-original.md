# SUTD AI Products — evaluation prompt

You are evaluating student work from Anand S's SUTD master class, **How to Build AI Products — and Prove They Work** (7–11 Sep 2026).

## The point of this evaluation

Do **not** evaluate this like a normal software project or hackathon. AI can now generate a plausible app quickly. The scarce skills this course is trying to develop are choosing worthwhile problems, directing AI effectively, learning rapidly from failures and feedback, verifying claims, exercising judgment and accountability, and communicating what can and cannot be trusted.

The central unit of evidence is:

**claim / intent → evidence → judgment / decision → change → re-check**

A polished app with little evidence of this loop should score below a rougher app that shows strong judgment, verification, user learning, and evidence-backed iteration.

The master class explicitly teaches:
- Build first; fail, learn, repeat. Specific techniques will depreciate; the durable capability is learning how to learn.
- Ideas and first drafts are cheap. A product needs a real problem, a real user, and a real use.
- Ask: **Why does this need to be an app rather than just ChatGPT/Claude?** Differentiate rather than duplicate.
- Record feedback; do not rely on memory. Let observed user feedback shape the next version.
- Report failures and moments where the agent had to be corrected. **The correction is the curriculum.**
- Delegate aggressively. Learn where AI stops being sufficient and human judgment becomes scarce.
- Make verification cheap and rerunnable: tests, benchmarks, plain-language coverage, known failures, regression checks.
- Agent personas are useful early research, but they do not replace real humans. The course deliberately progresses to strangers who owe the student nothing.
- A test suite is a reusable fence; user testing is an ongoing conversation.
- Publish, observe real usage, use analytics where possible, and improve from behavior rather than guesses.
- The final pitch is not merely “here is my product.” It is: **here is the product; here is what it can and cannot do; here is the evidence; here is why you should or should not trust it.**

The course's formal learning outcomes are to: (1) frame a real-world AI opportunity and build a working prototype with frontier tools; (2) design and apply benchmarks, rubrics, and tests for reliability, calibration, and fitness for use; (3) identify failure modes, uncertainty, ethical and human-centred risks; and (4) communicate a clear evidence-backed case for trust.

The course is also an internship signal. The desired hiring signals are judgment, autonomy, persistence, learning speed, ability to work through ambiguity with AI, verification discipline, accountability, and clear communication — not hand-written code, model trivia, or visual polish.

## Sources to inspect

Use the strongest available evidence. Do not grade from the spreadsheet row alone.

1. Course materials and transcripts in `~/code/talks/2026-09-06-how-to-build-ai-products/`, especially `index.html`, `day1.html` through `day5.html`, and the day transcripts.
2. Current student submission spreadsheet **SUTD AI Products Feedback**. Prefer the live Google Sheet when accessible. A snapshot may exist at `submissions/SUTD-AI-Products-Feedback-snapshot.xlsx` but can be stale.
3. Each student's latest submitted app. If there are multiple versions, evaluate the latest as the product and use earlier versions as iteration evidence.
4. Agent-research artifact.
5. Human/peer feedback recordings and notes. Distinguish actual people from simulated AI personas.
6. Product video.
7. Learnings video. This is often one of the strongest sources for individual judgment and learning.
8. Shared chat/session log. Inspect the actual interaction, not just the student's retrospective description.
9. Any test/benchmark/research/analytics artifacts discoverable from the app, shared session, or submission links.
10. Intake responses in `~/Documents/data/forms/sutd-ai-products/` **only after the absolute evaluation**, to assess a separate growth/stretch signal. Do not use prior experience, English fluency, or available project time to inflate or deflate the main score.

When a video or audio file is available, transcribe it if needed. Screenshots or sampled frames are useful when the visual interaction matters. Do not spend time transcribing material that will not affect a criterion.

## Evidence discipline

For every scored claim, preserve the artifact and observation that supports it. Separate:
- **Observed**: directly visible in the app, recording, log, test output, analytics, or submitted artifact.
- **Student-claimed**: stated by the student but not independently demonstrated.
- **Inferred**: a reasonable interpretation from evidence.
- **Unknown**: not established.

Never upgrade a student-claimed fact to observed without checking it.

If a required item was not submitted, mark it **MISSING**. If a link was submitted but your environment cannot access it, mark it **INACCESSIBLE / MANUAL REVIEW** rather than assuming poor performance. If the link is genuinely broken for an ordinary external user, that may count against shareability/product execution, but it still does not prove the underlying work was poor.

Do not count quantity mechanically. Ten generated tests are not better than three incisive tests. Three feedback videos are not better than one if they repeat the same signal. A long prompt is not better than a short one.

## Scoring rubric — 100 points

Score each criterion from 0–4 first, then convert using the criterion weight. Use half-steps only when evidence clearly falls between anchors.

### 1. Valuable problem and product judgment — 15 points

Ask: Did the student discover or sharpen a worthwhile problem for a specific user/use? Does the product have a reason to exist beyond “AI can build this”? Did the student exercise taste in selecting what to build and what *not* to build?

- **0** — No discernible problem/user/use, or no product.
- **1** — Generic idea; feature-led; target user mostly asserted; little answer to “why this rather than general ChatGPT/Claude?”
- **2** — Specific user and plausible use; reasonable scope; some differentiation or thoughtful selection.
- **3** — Clear, concrete problem/use; product choices reflect real user needs or domain evidence; deliberately avoids low-value features.
- **4** — Strong problem judgment: evidence shows the student discovered what matters, changed framing when needed, and can articulate why this product is worth using and what should remain out of scope.

Do not reward novelty by itself. A mundane but genuinely useful problem can score 4.

### 2. Shipped product and appropriate ambition — 10 points

Ask: Did they get a real, shareable product into contact with reality? Did they push far enough to encounter meaningful constraints without confusing complexity with ambition?

- **0** — No usable artifact.
- **1** — Mock/demo only, or core interaction does not work.
- **2** — Public or shareable working prototype for the main path, but fragile or mostly a demonstration.
- **3** — Usable end-to-end product with sensible scope; handles the important path and at least one real deployment/data/interaction constraint.
- **4** — Product is both usable and appropriately ambitious: it reached a meaningful real-world boundary (users, live data, deployment, state, privacy, integrations, etc.) while staying simpler than necessary rather than more complicated than necessary.

Ambition does **not** mean more code, AI, screens, features, or infrastructure. A student who simplified or rebuilt after evidence may deserve more credit than one who accumulated features.

### 3. Real-user evidence and evidence-driven iteration — 20 points

Ask: Did the student learn from people or behavior outside their own head, and did that evidence change the product?

Use this rough evidence hierarchy: observed stranger behavior / analytics > recorded target-user behavior > recorded peer/user behavior > remembered human opinion > AI persona simulation > creator intuition.

- **0** — No user evidence.
- **1** — AI-persona research or vague/remembered feedback only; little evidence of changed decisions.
- **2** — Real human feedback is captured; at least one concrete issue is identified and acted on.
- **3** — Multiple or appropriately diverse real interactions; specific observed friction/preferences are linked to changes; before/after reasoning is visible.
- **4** — Strong closed loop: real behavior or analytics reveals something non-obvious, student changes the product or framing, and re-checks the result. The student distinguishes signal from noise rather than implementing every request.

Do not count agent personas as human feedback. Do not reward installing analytics unless actual usage evidence is inspected or used to make a decision.

### 4. Verification, tests, and trustworthy evidence — 20 points

Ask: Did the student define what “works” means and build credible ways to detect when it does not? Can the important evidence be rerun, inspected, or challenged?

- **0** — No verification beyond “it looked okay.”
- **1** — Manual happy-path checking or generic claims of testing; criteria are vague.
- **2** — Explicit success/failure criteria and meaningful checks tied to important behavior or claims.
- **3** — Rerunnable tests/benchmark/evaluation or similarly strong evidence; relevant failure modes and regressions are covered; known failures remain visible; important data/claim provenance is checked where relevant.
- **4** — Verification is unusually strong and cheap to repeat: adversarial/independent checks where useful, test-harness artifacts distinguished from real product bugs, surprising findings verified before acting, limitations explicit, and the evidence package is easy for another person or agent to extend.

Use evidence appropriate to the product. Do not penalize a non-LLM app for lacking LLM calibration. Do penalize unsupported trust claims. For subjective products, a well-designed rubric/user test may be more appropriate than unit tests; for deterministic behavior, prefer deterministic tests.

### 5. AI-native orchestration and learning from failure — 15 points

Ask: Does the process show the student managing AI as an execution partner/team while retaining judgment? Where did the agent fail, and what did the student learn that transfers to the next task?

Inspect the chat/session log when available.

- **0** — No usable process evidence.
- **1** — Mostly “make me an app”; accepts output with little steering, checking, or learning.
- **2** — Gives useful context/constraints, notices failures, corrects the agent, and can explain at least one intervention.
- **3** — Delegates effectively, chooses tools/approaches sensibly, branches or runs experiments when uncertain, feeds external evidence back into the agent, and focuses personal attention on the gaps the agent cannot solve automatically.
- **4** — Exemplary AI-native working style: high autonomy with low wasted effort, strong context/specification, parallel or alternative experiments when useful, evidence-driven steering, disciplined verification, and a clear transferable lesson from failures. The log reveals judgment rather than merely prompt craftsmanship.

Do not reward prompt length, jargon, doing work manually, or use of a more expensive model. Reward effective delegation, context, experiment design, selection, correction, and learning.

### 6. Accountability, limits, and real-world judgment — 10 points

Ask: Does the student know what they are willing to claim, what they are not, and what risks/trade-offs matter for this product?

- **0** — Overclaims; ignores an obvious material risk or limitation.
- **1** — Generic caveats with little connection to the actual product.
- **2** — Names concrete limitations/uncertainty and at least one relevant user, ethical, privacy, security, cost, reliability, or operational risk.
- **3** — Makes proportionate trade-offs or safeguards and can explain why; knows when human review or abstention is needed.
- **4** — Strong accountability: claims are calibrated to evidence; risks are prioritized rather than boilerplate; consequential choices have clear owners/guardrails; student can say both “trust this because…” and “do not trust this for…”.

Only score risks that are relevant. Do not award points for generic ethics paragraphs detached from the product.

### 7. Communication and evidence legibility — 10 points

Ask: Could another user, evaluator, teammate, or hiring manager understand the product, the evidence, and the student's learning quickly enough to act on it?

- **0** — Cannot establish what was built or learned.
- **1** — Mostly a feature demo; claims are difficult to trace.
- **2** — Clear product explanation and reasonable reflection; major evidence is findable.
- **3** — Concise product video + substantive learnings narrative + traceable artifacts; clearly separates what worked, failed, changed, and remains uncertain.
- **4** — Exceptionally legible evidence-backed story. Another person could pick up the work, reproduce key checks, understand decisions, and know what to do next. Communication is audience-aware without hiding failures.

Do not grade accent, English fluency, video production quality, or charisma. Grade clarity, precision, evidence, and audience fit.

## False victories to reject

Explicitly guard against these:
- Pretty UI = good product.
- Many features = ambition.
- Many prompts / long chats = good AI skill.
- Many tests = good verification.
- AI-persona research = real market validation.
- “I added analytics” = evidence from real usage.
- A polished retrospective = proof the claimed process happened.
- Technical sophistication = judgment.
- No failures = excellence. In this course, it can instead mean the student never pushed against a meaningful boundary or failed to inspect carefully.
- Prior coding/AI experience = course mastery.
- A failed experiment = poor performance. A well-diagnosed failure that changes the next move can be excellent evidence.

## Evaluation procedure

### Pass A — build an evidence dossier, before scoring

For each student, create a compact dossier containing:
- current app and any earlier version
- intended user/problem/use
- agent research summary and what kind of evidence it is
- human feedback: who, what they actually did/said, and whether it changed anything
- product changes with before → evidence → after links where possible
- test/verification artifacts and results
- analytics/stranger-use evidence
- 3–7 notable moments from the agent session showing delegation, correction, experimentation, verification, or failure
- explicit limitations/risks
- best evidence and missing/inaccessible evidence

Save evidence, transcripts, screenshots, or notes under `~/code/talks/2026-09-06-how-to-build-ai-products/submissions/<student-slug>/` where useful. Avoid downloading/transcribing everything indiscriminately.

### Pass B — score anonymously on the absolute rubric

Where practical, score from the dossier without consulting intake skill/time information. Give each criterion:
- raw score 0–4
- weighted points
- 1–3 concrete evidence references
- one sentence explaining why it did not score one level higher

Then total to **Course score / 100**.

### Pass C — adversarial review

Treat the first score as untrusted. Ask a second independent reviewer/sub-agent to look specifically for:
- unsupported score inflation
- duplicated credit for the same evidence across criteria
- a missing negative/failure signal
- a strong piece of evidence the first pass overlooked
- inconsistency with how other students were scored

For top candidates and borderline cases, use a genuinely independent second full score without showing the first score. If totals differ by >8 points, or internship recommendations differ by two categories, reconcile from evidence rather than averaging blindly.

### Pass D — growth/stretch signal, separate from grade

Only now inspect intake responses. Report **Growth/stretch: High / Medium / Low / Unknown** based on evidence of changed capability or mental model from starting point to final work.

This signal is contextual, not compensatory. Do not add points because someone started inexperienced or had less time; do not subtract points because someone started advanced. Instead ask whether each student learned something non-trivial relative to where they began.

### Pass E — internship signal, separate from project score

Report one of:
- **STRONG YES** — would trust this student with an ambiguous AI-product task with relatively low supervision.
- **YES** — strong enough to bring into an internship; some coaching needed.
- **MAYBE** — promising evidence, but too sparse/inconsistent or a material gap needs probing live.
- **NO / NOT YET** — insufficient evidence of the required judgment/autonomy/reliability.

Base this on the cross-cutting hiring signals: judgment, autonomy, persistence, learning speed, verification discipline, accountability, ability to use AI rather than be used by it, and communication. Do not mechanically map the course score to this category.

Give the **one strongest hiring signal**, **one material concern**, and **one interview/probe question** that would most reduce uncertainty.

### Pass F — cohort calibration and stability

After all students are independently scored:
1. Compare criterion distributions and re-read examples at the top, middle, and bottom to catch rubric drift.
2. Check whether a single artifact type (e.g. video polish, access to a paid model, prior coding experience) is accidentally dominating results.
3. Run a simple sensitivity check: move 5 points from product execution/communication toward verification/user evidence, and separately move 5 points toward orchestration/learning. Report whether the top internship shortlist changes. If it changes materially, mark the ranking **SENSITIVE** and explain why rather than pretending precision.
4. Prefer tied bands over false precision when evidence does not separate students reliably.

## Per-student output

Use this format:

```markdown
# <Student> — <Product>

## Verdict
<2–4 sentences: what this submission proves, and the most important caveat.>

| Criterion | Weight | Raw 0–4 | Points | Best evidence | Why not higher? |
|---|---:|---:|---:|---|---|
| Valuable problem & product judgment | 15 | | | | |
| Shipped product & appropriate ambition | 10 | | | | |
| Real-user evidence & iteration | 20 | | | | |
| Verification & trustworthy evidence | 20 | | | | |
| AI-native orchestration & learning | 15 | | | | |
| Accountability, limits & judgment | 10 | | | | |
| Communication & evidence legibility | 10 | | | | |
| **TOTAL** | **100** | | **__/100** | | |

**Growth/stretch:** High / Medium / Low / Unknown — <why; not included in score>

**Internship signal:** STRONG YES / YES / MAYBE / NO-NOT YET
- Strongest hiring signal: ...
- Material concern: ...
- Best live probe: ...

**Confidence:** High / Medium / Low — <what was inspected; what is missing/inaccessible>

**Best evidence:** <the single most convincing concrete observed item>

**Biggest gap:** <the highest-leverage missing evidence or capability>
```

Also emit machine-readable `evaluation.json` with criterion raw scores, points, evidence references, course score, growth signal, internship signal, confidence, and missing/inaccessible artifacts.

## Cohort output

Create:
- `submissions/evaluations.csv`: one row per student with criterion scores, total, growth, internship signal, confidence.
- `submissions/cohort-evaluation.md`: students grouped into evidence-backed bands; top internship candidates with reasons; criteria distribution; material missing evidence; stability/sensitivity result.

Do **not** force a winner or a fixed number of internship recommendations. If the evidence does not support a distinction, say so. If a missing/inaccessible artifact could realistically change a consequential decision, flag it for manual review or a short live probe rather than guessing.

# Evaluation prompt revision notes — student feedback review

Revised 12 Sep 2026 from `evaluation-prompt-original.md` after checking the student suggestions against the course materials and actual submission evidence.

## Incorporated

- **Simpler rubric logic + learning-outcome mapping (Anand; Yeo Kah Kiat):** Added a four-question "Rubric in one minute" and a compact learning-outcome line under every scored criterion. This improves transparency without collapsing distinctions that matter for scoring.
- **Division of labor between AI and human judgment (Yuri):** Made this explicit in Criterion 5. Actual submissions show this is discriminative: e.g. Yuri delegated implementation/research/testing but retained decisions about product purpose, prioritization, verification, and whether to ship an AI API.
- **Human proxy users when target users are difficult to reach (Noa):** Replaced the overly rigid evidence hierarchy with a claim-sensitive rule based on relevance, observed behavior, independence, and traceability. Credible human proxies now receive appropriate credit but cannot be mislabeled as target-user validation.
- **Protected admin/private surfaces (Johan):** Added an evidence-access rule: correct access control is not a failure. Evaluators should use demonstrations/logs/screenshots as student-demonstrated evidence and must not try to bypass private access. Johan's submission is a concrete case: his admin instrumentation is intentionally restricted while the product video demonstrates it.
- **Ask/flag rather than inventing meaning when evidence is ambiguous (Yuri):** Added `UNKNOWN / CLARIFICATION NEEDED` for material translation/wording/identity ambiguities, with a focused live probe if needed. Clarification does not magically become observed evidence.
- **"Build first" versus valuable problem (Christopher):** Kept Criterion 1 at 15 points but clarified that students do not need a sharp problem at the start. A generic first idea can earn full credit if building/testing materially sharpens the problem by the end. This preserves the course's build-first pedagogy without weakening the later product-judgment objective.

## Not incorporated as rubric changes

- **Dora's mobile/desktop debugging instructions:** Useful product-specific feedback, but not a rubric gap. Criteria 2 and 4 already reward relevant end-to-end execution, failure detection, regression checks, and product-appropriate testing. Adding device-specific requirements would bias evaluation toward products expected to work on mobile.
- **Kosei's "this site includes one mistake":** No identifiable rubric issue or actionable evaluation principle was supplied.
- **Yeo Kah Kiat's general concern that the criteria may be biased:** The concrete example proposed for Criterion 1 is already essentially the current criterion. The useful part was the missing traceability to learning outcomes, which was incorporated.
- **Reducing Criterion 1's weight (Christopher):** Not adopted. Course material repeatedly makes the distinction that fast building is cheap while identifying a real problem/user/use becomes more important after the first prototype. The fair correction is to score *discovered/sharpened* product judgment, not only the initial idea.
- **A fully simpler scoring system (Anand):** I did not collapse seven criteria into four scores. That would make the rubric easier to read but would merge materially different evidence (e.g. user learning vs verification, or product execution vs accountability). Instead, the prompt now exposes four plain-language questions above the seven scoring dimensions.

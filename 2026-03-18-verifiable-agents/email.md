# Email: The Trust Problem — Verifiable Agents

**Subject:** AI without verification can't be operationalised

Yesterday, Ankor and I spoke on one of the most underrated problems in enterprise AI: **Verifiable Agents**.

Models aren't bad. They're _probabilistic_. Every software quality process invented was built for _deterministic_ systems that don't do that. LLMs break that assumption.

![Session sketchnote](https://sanand0.github.io/talks/2026-03-18-verifiable-agents/sketchnote.avif)

---

## The uncomfortable numbers

- **78%** of enterprises use AI in at least one function
- **14%** have enterprise-level governance & verification
- **74%** of deployed agents rely on _manual_ human verification
- **5%** of agent outputs go directly to another system — the rest terminate in a human

> _"If you assume agentic AI being deployed across a variety of use cases, it is untenable to rely on humans across every use case in this way."_
> — Ankor Rai

![What happens when AI has no verification — slide showing enterprise failures](https://sanand0.github.io/talks/2026-03-18-verifiable-agents/slide-06.avif)

---

## What your peers are actually doing

Morgan Stanley's AI is restricted to a curated library of ~100,000 internal documents. JPMorgan's AML agents cross-validate with human investigators. BlackRock runs multi-model validation with stress testing — and then a human expert.

The pattern: **constrain the agent, then verify the output**.

![How enterprises verify agents today](https://sanand0.github.io/talks/2026-03-18-verifiable-agents/slide-07.avif)

Five strategies are in use: knowledge & data grounding · domain-specific constrained steps · LLM-as-judge · cross-referencing between models · rule-based output checks. Most deployments use several in combination — plus a human at the end.

---

## Three demos that make this concrete

**1. [Sales intelligence (deployed at PGIM)](https://sales-intelligence.straivedemo.com/)**
Every claim the AI makes carries a citation and a confidence score. Low-confidence signals are filtered out before they reach the brief. The human can click any finding and go straight to the source document. Verifiability baked in.

**2. [Contract analysis — 3 cents, 6 seconds](http://contractanalysis.straivedemo.com/)**
Feed a contract against a 20-item compliance checklist. The AI cites exactly which clause satisfies each item — or flags the gap. The compliance reviewer focuses on the red cells, not the green ones.

**3. [Claims adjudication with InsurLE](https://mynkpdr.github.io/insurle-demo/v2)**
An LLM reads an insurance contract and converts it into Prolog rules. After that, every claim adjudication is a _program_ — deterministic, auditable, with an exact proof of why a claim was accepted or rejected. When Marcia Delgado's $12,000 claim failed, the answer wasn't "probably invalid (94% confidence)." It was:

```
✗ valid_claim — DENIED
  ✓ Driver Fully Eligible
  ✗ Incident Circumstances Covered
    ✗ Sobriety Verification
      ✗ BAC ≤ 0.08 g/dL · 0.14 > 0.08 — DUI VIOLATION ✗
```

_This is not LLM generated. This is a program running a check, and does not go wrong._

---

## The future: verification as a standard enterprise layer

The direction of travel: move from checking every output to verifying the pipeline once (like CI/CD). Get there by:

1. Building a rigorous taxonomy of agent failure modes
2. Integrating verification into the same agent sub-task that does production
3. Transitioning agents from human-facing to software-facing (the 5% → 50% shift)
4. Making verification a formal org function — developer ≠ validator

The post-2008 analogy is apt: after the Global Financial Crisis, the OCC required every quantitative model to have a separate validation team. AI is heading the same way.

![Enterprise AI Stack — verification as a formal layer](https://sanand0.github.io/talks/2026-03-18-verifiable-agents/slide-10.avif)

---

## Top takeaways

1. **AI without verification cannot be operationalised.** Non-determinism is structural, not accidental.
2. **74% of agents still terminate in a human.** That's untenable at scale.
3. **Grounding is verification.** Show the source. Show the confidence. Let the human spot-check.
4. **Code is more verifiable than language.** Design for determinism where you need certainty.
5. **Cross-checking cuts error rates from 14% → 0.7%** — at the cost of a 28% manual queue. For many processes, excellent trade.
6. **Verification is becoming a formal enterprise function.** Chief AI Officers will own it as "second line of defence."

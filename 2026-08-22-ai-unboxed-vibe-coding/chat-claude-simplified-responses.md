# User

I'm trying to evaluate whether asking an agent to write its response in a simplified form makes its thinking quality or result quality worse in some way.
Suggest three concise 1-line prompts that I can use (a) with and (b) without a "simplify the response" suffix and compare the results.
Suggest a concise rubric I can pass to a grading agent to compare the results of these prompts.
I will be comparing 1a vs 1b as well as 1b vs 1a, 2a-2b, 2b-2a, 3a-3b, 3b-3a to avoid position bias.
I prefer a single rubric across all 3 prompts. I'll pass "{rubric} {1a} {1b}", ...

# Claude

Here's a set built so the only thing that varies is the suffix.

## Three prompts

Pick tasks where quality shows up as _content_, not vocabulary — otherwise you just measure style preference.

1. **Quantitative + trap:** "A 4-person team shipped a feature in 6 weeks. The exec wants 3 weeks next time, so he's adding 4 more people. What do you tell him?"
2. **Open judgment:** "A 200-person company is deciding whether to build or buy its internal analytics stack. What should decide it?"
3. **Explanation with a subtlety:** "Our fraud model is 95% accurate. Explain to the board why that number may mean nothing."

Suffix for the (b) condition, identical every time: **"Write your answer in simple grade 8 English."**

Add a third condition if you can afford it: **"Think it through fully, then write the answer in simple grade 8 English."** That separates _simpler output_ from _simpler thinking_. Without it, a quality drop is ambiguous — you won't know if the agent reasoned worse or just wrote plainer.

## Rubric

```
You are comparing two answers to the same question. Judge content only.

IGNORE reading level, vocabulary, sentence length, tone, formatting, and
total length. A plainly worded answer and a technical answer that make the
same point are EQUAL. Do not reward big words, jargon, or longer answers.

For each criterion below, pick A, B, or Tie, and give one line naming the
specific content that decided it.

1. Correctness - Are the claims true? Penalize anything false or misleading.
2. Key drivers - Does it name the factors that actually decide this
   question, or only generic ones that would fit any question?
3. Mechanism - Does it explain WHY, or just assert the conclusion?
4. Caveats - Does it flag the main risks, exceptions, or missing info?
5. Calibration - Confident where the evidence is clear, hedged where it is
   not. Penalize both overclaiming and empty hedging.
6. Usefulness - Could the reader act on this and get the right result?

Then list substantive points made by one answer and absent from the other:
A-only: [...]
B-only: [...]

Output:
Per-criterion: winner + evidence line
A-only / B-only lists
Overall winner: A / B / Tie
Confidence: high / medium / low
```

## Two things about reading the results

The "A-only / B-only" lists are the real measurement. They're concrete and checkable, so they survive judge noise far better than the overall verdict does. If simplification is costing you something, it shows up as a _named missing point_ — a dropped base rate, a dropped exception — not as a lower score.

The ignore-style paragraph is load-bearing. Drop it and the judge will score fluency, and simple English will lose (or win) for reasons that have nothing to do with thinking quality.

One design caution: 3 prompts × 2 orders is 6 judgments, and run-to-run variance on open questions is usually bigger than the effect you're hunting. Five samples per condition per prompt would give the order-swap something to actually detect. Flips between orders on the _same_ pair mean noise; consistency in both directions means signal.

# User

Here's another answer from ChatGPT.
Take what's better, drop what's worse, explore any new thoughts this leads you to, and revise your response based on that.

<CHATGPT>
Use the same suffix for each b version:
Write in plain language using short sentences and familiar words. Preserve all important reasoning, caveats, and details.
Test prompts
1 — Causal diagnosis
A company’s support tickets rose 40% after launching a chatbot, while customer volume rose 10% and resolution time fell 20%; identify the plausible causes, evidence that would distinguish them, and the best next action.
2 — Decision under uncertainty
A startup has six months of runway, revenue is growing 15% monthly, and churn has doubled; decide whether it should cut costs, raise funds now, or keep growing, explaining the key trade-offs and what would change your decision.
3 — Experimental design
Design the smallest reliable experiment to determine whether AI-generated suggestions improve employees’ decision quality rather than merely their speed; specify the control, metrics, confounds, and stopping rule.
For each a, use the prompt alone. For each b, append the simplification suffix.
Grading rubric
Compare Response A and Response B solely on substantive result quality—not length, vocabulary, elegance, or apparent sophistication. Prefer the response that is more correct, complete, logically sound, well-calibrated, attentive to alternatives and trade-offs, and actionable. Penalize missing reasoning, unjustified claims, contradictions, or simplification that distorts or removes important nuance. Return `A`, `B`, or `TIE`, followed by one sentence naming the decisive difference.
This tests three distinct failure modes: loss of causal nuance, flattened trade-offs, and weakened methodological rigor.
</CHATGPT>

Produce a clean, standalone final response for a first-time reader, as if no earlier draft or conversation exists.

Integrate all corrections and new context directly, leaving no revision traces - no "previously," "originally," "now," revised headings, changelogs, explanations of what changed, etc.
Include change summaries only in a clearly separated section.

# Claude

## The suffix

Run two versions of it, not one. They answer different questions.

**Naive suffix (S1):** `Write your answer in simple grade 8 English.`
**Guarded suffix (S2):** `Write in plain language using short sentences and familiar words. Preserve all important reasoning, caveats, and details.`

S1 is what people actually type. S2 tells the model to keep the content while changing the style. If S1 loses content and S2 doesn't, the cost is a wording problem you can fix with 12 extra words. If both lose content, simplification is doing real damage to the thinking. That's a much more useful result than a single yes/no.

## Three prompts

Each one asks for named parts. That matters: it turns "is this worse?" into "is this part missing?", which is far easier to score.

1. **Causal diagnosis** — "Support tickets rose 40% after we launched a chatbot, while customer volume rose 10% and resolution time fell 20%. Give the plausible causes, the evidence that would tell them apart, and the best next action."
2. **Decision under uncertainty** — "A startup has 6 months of runway, revenue growing 15% monthly, and churn that just doubled. Should it cut costs, raise now, or keep growing? Give the key trade-offs and what would change your answer."
3. **Experimental design** — "Design the smallest reliable experiment to test whether AI suggestions improve employees' decision _quality_, not just their speed. Specify control, metrics, confounds, and stopping rule."

These target three separate failure modes: lost causal nuance, flattened trade-offs, and weakened method rigor. If plain language only hurts one of them, you'll see it.

## Rubric

```
Compare Response A and Response B to the same question. Judge content only.

IGNORE reading level, vocabulary, sentence length, tone, formatting, and
word count. A plainly worded answer and a technical answer that make the
same point are EQUAL. Do not reward big words, jargon, or extra length.
Longer is not more complete.

STEP 1. Read the question and list the components it explicitly asks for
(e.g. causes, distinguishing evidence, recommended action). Mark each
component Present / Partial / Missing for A and for B.

STEP 2. List substantive points made by one answer and absent from the
other. Be specific — name the actual claim, not the topic.
  A-only: [...]
  B-only: [...]

STEP 3. Score each criterion A / B / Tie, with one line naming the
specific content that decided it:
  1. Correctness — are the claims true? Penalize anything misleading.
  2. Key drivers — does it name the factors that actually decide THIS
     question, or only generic ones that fit any question?
  3. Mechanism — does it explain why, or just assert?
  4. Caveats — does it flag the main risks, exceptions, and unknowns?
  5. Calibration — confident where evidence is clear, hedged where it
     is not. Penalize overclaiming and empty hedging equally.
  6. Actionability — could a reader act on this and get it right?

OUTPUT:
Component table
A-only / B-only lists
Per-criterion winners with evidence lines
Overall: A / B / TIE
Confidence: high / medium / low
```

Pass the original question along with the two answers. Step 1 can't run without it.

## Reading the results

The component table and the A-only/B-only lists are the real measurement. They're concrete and checkable, so they hold up far better than the overall verdict, which is where judge taste and position bias live. If plain language costs you something, it shows up as a named missing item — a dropped confound, a dropped exception — not as a lower score.

Log word count for every answer too. If the plain version is shorter _and_ thinner, check whether what's lost tracks the compression evenly or hits specific things. My guess is that caveats, alternatives, and conditional statements ("unless churn is concentrated in one segment") go first, because they're the hardest parts to say in short sentences. If that's what you see, the finding isn't "simple is worse" — it's "simple drops hedges," which is fixable.

Also keep an open mind on direction. Forcing plain language strips padding, and some answers get _better_ because the weak reasoning stops hiding behind vocabulary. A tie is a real result here, not a failed experiment.

One design caution: 3 prompts × 2 orders is 6 judgments, and run-to-run variance on open questions is usually bigger than the effect you're hunting. Five samples per condition per prompt gives the order swap something to detect. If a pair flips between orders, that's noise. If it holds in both directions across samples, that's signal.

---

### What changed from the earlier draft

- **Suffix:** split into two conditions (naive vs. content-preserving) instead of one, since they measure different things and the contrast is the actual diagnosis.
- **Prompts:** replaced with multi-part versions that name required components, each targeting a distinct failure mode.
- **Rubric:** added a Step 1 component check, written generically so the judge derives the checklist from whatever question it's given — keeps the single-rubric requirement intact.
- **Rubric:** added "longer is not more complete" to block length bias, since simplification tends to shorten output.
- **Dropped:** the "think fully, then simplify" third condition — the two-suffix design covers the same question more cleanly.
- **Added:** word-count logging and a hypothesis about which content types get dropped first.

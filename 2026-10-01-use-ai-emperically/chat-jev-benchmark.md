---
title: "Compare Jev Benchmarks Pricing Availability"
date: 2026-10-01T21:46:53+08:00
source: "https://chatgpt.com/c/6aabb0bc-2888-83ec-b5ed-374329c52bca"
---

# User

_2026-09-17T09:19:58.372Z_

What is Jev and how is it different from other other frontier LLMs? How does it compare on relevant benchmarks? How is it priced and is it available on OpenRouter? Is it open weights? What else should I know about this? Use relevant [Anand Skills](/plugins/plugin_asdk_app_6a6c9b8ca08c8191bee90054f9785b1b)

# ChatGPT

_2026-09-17T09:19:58.372Z_

Jev is genuinely interesting, but I would not think of it as “another frontier LLM.” It is closer to a **frontier semantic decision engine**: give it some state plus a set of bounded questions, and it returns typed choices/scores/probabilities rather than generating prose. TypeSafe calls this a “System One Model.” [TypeSafe AI](https://docs.typesafe.ai/)

TypeSafe says Jev uses a new architecture, a parallel sampler, and a post-training method called **RLCD — Reinforcement Learning for Calibrated Decisions**. In one request you can ask many independent questions about the same state; Jev evaluates them in parallel. The three primitives are Choice (pick among predefined options), Score (rate against predefined levels), and Noul (probability that a proposition is true). It cannot generate arbitrary text, code, explanations, or novel values. [TypeSafe AI](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

The mental model I’d use is:

**LLM:** “Think about this and tell me what you conclude.”
**Jev:** “Here are 17 precisely defined judgments. Give me probability distributions for all 17, now.”

That distinction explains most of the speed and cost advantage.

### Benchmarks: impressive economics, less impressive evidence

The most useful published comparison is TypeSafe's four-workflow benchmark. But the column commonly called “accuracy” is better described as **agreement with a reference**: the reference probabilities are the average of GPT-6 Astra and Claude Fable 5.1 at high reasoning. It is not human-labeled ground truth. TypeSafe explicitly acknowledges both that bias and that the workflows were developed by its own capabilities team. [TypeSafe AI](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

| Model | Agreement | Cost / case | Latency |
| --- | --- | --- | --- |
| GPT-5.6 Sol | 74.1% | $0.0836 | 23.3 s |
| Claude Opus 5 | 73.1% | $0.1761 | 37.8 s |
| GPT-5.6 Terra | 67.9% | $0.0304 | 10.1 s |
| **Jev** | **67.8%** | **$0.0004** | **0.4 s** |
| Claude Sonnet 5 | 67.8% | $0.1174 | 78.1 s |
| GPT-5.6 Luna | 66.8% | $0.0033 | 12.9 s |

Those published aggregate figures come from TypeSafe's benchmark; independent researchers have reproduced the numbers from its published artifacts, but not independently rerun Jev itself. [CounterProof](https://research.counterproof.io/field-note-1-typesafe-jev-consensus-as-oracle.html?utm_source=chatgpt.com)

So the striking comparison is not “Jev beats frontier models.” It doesn't. Rather:

**Jev ≈ Terra/Sonnet-level agreement on these particular decision workflows, at dramatically lower latency and cost.**

Against Terra, for example, it loses only 0.1 percentage point on the aggregate while TypeSafe reports roughly **76× lower cost per case and 25× lower latency**. Against Sol it gives up 6.3 points for about 209× lower cost and 58× lower latency.

The average also hides jaggedness. Jev's four workflow scores were 61.7%, 71.6%, 61.8%, and 76.0%; on invoice processing, its 61.8% was far below Sol's 79.1%. So “Terra-class intelligence” is quite task-sensitive. [CounterProof](https://research.counterproof.io/field-note-1-typesafe-jev-consensus-as-oracle.html?utm_source=chatgpt.com)

And there are currently **no meaningful MMLU/GPQA/SWE-bench-style comparisons** to cite. Those are partly the wrong benchmark anyway because Jev cannot answer open-ended questions, write programs, or expose reasoning. More importantly, there is not yet a paper establishing how broadly its claimed intelligence generalizes. [pearpages](https://pearpages.com/blog/2026/09/16/jev-sorted-what-typesafes-system-one-model-actually-is-and-what-is-still-just-a-claim?utm_source=chatgpt.com)

### Pricing and availability

The direct TypeSafe price is **$0.042 per million input tokens, or $42/billion; output is unmetered/free**. TypeSafe quotes 70–500 ms end-to-end latency. The company explicitly notes that it cannot yet prove the pricing is unsubsidized/sustainable, although it expects prices to fall rather than rise. [TypeSafe AI](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

It is also already available through **Vercel AI Gateway** as typesafe-ai/jev, where Vercel displays the price rounded to $0.04/M input tokens. [Vercel](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway?utm_source=chatgpt.com)

As of **September 17, 2026, I cannot find Jev on OpenRouter**. I specifically searched OpenRouter's indexed model pages for Jev, typesafe-ai, and jev-latest and found no listing. TypeSafe's own endpoint uses a different API shape, POST /v1/systemone, rather than an OpenAI-compatible /chat/completions interface, so supporting it isn't necessarily just adding another OpenRouter model slug. Vercel has explicitly added support for this different “evaluate” interface. [Vercel](https://vercel.com/ai-gateway/models/jev?utm_source=chatgpt.com)

TypeSafe itself still describes Jev as **early access** and has a waitlist on its site. [TypeSafe AI](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

### Open weights? No

Jev is currently **closed-weight**. There is no published checkpoint, parameter count, training recipe for RLCD, or technical paper sufficient to reproduce it. TypeSafe's public GitHub organization contains SDKs, an LLM-based System One adapter, examples, and agent skills—not Jev's model weights. [GitHub](https://github.com/typesafe-ai/?utm_source=chatgpt.com)

There are already projects such as openjev experimenting with Jev-like behavior using open-weight models. That is useful because it raises an important unresolved question: **how much of Jev's benefit comes from genuinely new modeling/training versus simply avoiding autoregressive text generation and reading constrained logits efficiently?** Early open experiments show that this general design pattern is reproducible, but they do not reproduce Jev's claimed RLCD calibration. [GitHub](https://github.com/TheoLeeCJ/openjev?utm_source=chatgpt.com)

### The biggest caveat is “calibrated”

This is the part I would pay the most attention to.

TypeSafe's confidence is **not itself a predicted probability of being correct**. For Choice and Score, Jev returns a probability distribution; confidence is a statistic TypeSafe computes from how concentrated that distribution is. TypeSafe explicitly tells developers to test thresholds on their own data. Noul, by contrast, directly returns a yes-probability. [TypeSafe AI](https://docs.typesafe.ai/confidence)

Yet RLCD's major selling point is calibration. As of today, I have not found the thing I most want to see: **reliability diagrams, ECE/Brier scores, or a substantial human-ground-truth calibration benchmark**, ideally independently reproduced. Others reviewing the launch have flagged the same omission. [pearpages](https://pearpages.com/blog/2026/09/16/jev-sorted-what-typesafes-system-one-model-actually-is-and-what-is-still-just-a-claim?utm_source=chatgpt.com)

Likewise, “zero hallucinations” is technically true only under a narrow definition: Jev cannot return an invalid/off-schema value. If the legal choices are fraud and not_fraud, it will never answer “purple elephant”—but it can confidently choose the wrong one. TypeSafe itself distinguishes its mathematical schema guarantee from empirical correctness. [TypeSafe AI](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

### Why I think this is especially worth your time

The potentially important idea isn't Jev itself. It is **moving semantic judgments out of generative text space and making probability distributions first-class software objects**.

That maps almost perfectly onto your recent confidence-calibration work. I would run the same ~3K BANKING77 examples through Jev and compare four signals on exactly the same held-out labels:

Jev probability → Jev confidence → frontier-LLM logprob → prompted confidence

Measure AUROC for review-queue ranking, ECE/Brier/reliability for calibration, latency, and dollars per 1,000 cases. Your current result—that logprobs rank well while prompted confidence calibrates better—makes this a particularly clean test of TypeSafe's central claim. If Jev actually beats both on calibration while retaining its cost/latency advantage, **that would be much more convincing evidence for Jev than its launch benchmark**.

My current read is therefore: **pay attention, definitely experiment, don't yet accept the “new frontier model class” framing as established.** The interface is valuable even if RLCD ultimately proves incremental; the economics look exceptional on bounded judgments; the missing independent calibration evidence is currently the biggest hole.

Because this was released only on September 15, the situation may change quickly. I can monitor Jev for an OpenRouter release, technical paper/weights, and genuinely independent calibration benchmarks and alert you when any of those appear.

# User

_2026-09-18T02:13:04.893Z_

Where can I get a cheap top-up for Jev credits or something? Ideally free for benchmarking, or preferably where I already have an account and top up...

# ChatGPT

_2026-09-18T02:13:04.893Z_

Use **OpenRouter**. Jev appeared there on September 17, a day after my previous check. You already use OpenRouter for benchmarking, so this is the lowest-friction route. [OpenRouter](https://openrouter.ai/typesafe?utm_source=chatgpt.com)

The current model is ~typesafe/jev-latest, priced at **$0.042 / million input tokens and $0 output**—the same list price as TypeSafe direct. OpenRouter does not mark inference up, although it charges a **5.5% credit-purchase fee, with an $0.80 minimum fee**. The minimum credit purchase is $5. [OpenRouter](https://openrouter.ai/typesafe?utm_source=chatgpt.com)

That means a $5 credit top-up gives you about:

**$5 / $0.042 × 1M ≈ 119 million Jev input tokens.**

So even the minimum top-up is comically more than you need for a BANKING77-scale benchmark. At, say, 1,000 input tokens × 3,000 cases, Jev inference would cost only about **$0.13**.

There is an even better free option worth trying first: **Vercel AI Gateway gives unpaid/free accounts $5 of AI Gateway credit every 30 days**, applicable across its model catalog, and Jev is available there as typesafe-ai/jev at roughly $0.04/M input. Vercel says free users can use premium models and doesn't impose its own request-rate limits beyond upstream limits. If you've never paid Vercel, that $5 credit is effectively enough for ~125M Jev input tokens. [Vercel](https://vercel.com/blog/ai-gateway-is-now-generally-available?utm_source=chatgpt.com)

So my order would be:

1. **Try Vercel AI Gateway first** if your account qualifies for the recurring free $5. That's effectively free benchmarking.
2. Otherwise **use your existing OpenRouter account** and whatever balance is already there; if needed, add the minimum $5.
3. Don't bother getting TypeSafe-direct billing specifically for this benchmark unless you want to compare the direct endpoint against gateway behavior.

One caveat: Jev is a new **“Decisions”** model type rather than a conventional chat model. OpenRouter says it exposes Jev through its unified/OpenAI-compatible API, but before adapting your full calibration benchmark I'd run 10 BANKING77 rows and confirm the exact response/probability semantics match TypeSafe's native Choice/Score/Noul outputs. [OpenRouter](https://openrouter.ai/typesafe?utm_source=chatgpt.com)

For your particular experiment, I would use **OpenRouter**, despite Vercel potentially being free: you already have the infrastructure and cost logging around OpenRouter, which makes the Jev-vs-logprob-vs-prompted-confidence comparison cleaner and reproducible.

# User

Take a look at the benchmark on @LocalMCP at ~/code/llmevals/confidence-calibration/ for reference.

I'd like to find out how well it classifies the same BANKING77 dataset vis-a-vis good models, e.g. GPT 5.6 Luna, GPT 5.6 Sol, GPT 6 Astra, Claude Opus latest, Claude Fable latest. What would it cost? How many can I classify to keep the cost down to $2 overall? Or $5 overall? Or ...

# ChatGPT

I inspected ~/code/llmevals/confidence-calibration/, especially scripts/run_benchmark.py, data/banking77-sample.csv, and the existing results.

The current 770-case benchmark is almost ideal for this. It is balanced: **10 examples × 77 intents**. The actual baseline prompt averages **478.4 input tokens/case**, and your existing Luna responses average **12.1 output tokens/case**. Luna scores **84.0%** on that exact protocol. The later logprob run is consistent at 83.6%, so there is no protocol anomaly to resolve.

I would run Jev against exactly these 770 cases, keeping the existing Luna result rather than paying to rerun it.

### What the benchmark costs

For cheap benchmarking, OpenRouter's batch variants are surprisingly attractive right now:

| Model | OpenRouter batch price, input/output | Approx. cost for 770 |
| --- | --- | --- |
| **Jev** | $0.042 / $0 per M | **$0.015** |
| GPT-5.6 Luna | $0.10 / $0.60 | $0.042 |
| GPT-5.6 Sol | **$1 / $5** currently | **$0.415** |
| GPT-6 Astra | $5 / $25 | **$2.074 + thinking** |
| Claude Opus 5 | $2.50 / $12.50 | **$1.037** if thinking disabled |
| Claude Fable 5.1 | $5 / $25 | **$2.074 + thinking** |

OpenRouter currently has batch variants for Astra, Sol, Luna, Opus 5 and Fable 5.1; Sol's batch price is additionally benefiting from the current OpenAI promotion. [OpenRouter](https://openrouter.ai/openai/?utm_source=chatgpt.com) Jev remains $0.042/M input and free output. [OpenRouter](https://openrouter.ai/models?o=pricing-high-to-low&order=pricing-low-to-high&utm_source=chatgpt.com)

So the **absolute floor for all six models over all 770 examples is about $5.66**—or about $5.62 if we sensibly reuse your existing Luna run.

But that is a floor, because Astra cannot turn reasoning off, and Fable 5.1 has adaptive thinking permanently enabled. Their hidden reasoning tokens are billed as output tokens. Opus 5 *can* have thinking disabled, which I would do for this task. [OpenAI Developers](https://developers.openai.com/api/docs/models/gpt-6-astra?utm_source=chatgpt.com)

The useful cost formula for the full 770 is approximately:

**$5.66 + $0.01925 × (average Astra reasoning tokens + average Fable reasoning tokens)**

So if each averages:

| Hidden reasoning / case | Full 770, all six models |
| --- | --- |
| 0 each — theoretical floor | **$5.66** |
| 50 each | **$7.58** |
| 100 each | **$9.51** |
| 150 each | **$11.43** |
| 200 each | **$13.36** |
| 300 each | **$17.21** |

The 100-token line is a planning assumption, not an observed estimate. That's exactly why I would start with a small pilot.

### What I would actually do

Run **77 examples first: one per intent, same cases across every model**.

Even if Astra and Fable average 200 hidden thinking tokens each, the whole six-model pilot should cost only about **$1.34**. If they average 100 each, it's about **$0.95**.

That pilot gives us three things simultaneously: an initial accuracy signal, the *actual* Astra/Fable token usage, and confirmation that the Jev decision API maps cleanly onto BANKING77.

Then extrapolate from actual spend instead of guessing.

Assuming roughly **100 hidden reasoning tokens each for Astra and Fable**, your budget choices become:

| Total budget | Balanced sample | Cases / intent | Estimated spend |
| --- | --- | --- | --- |
| **$2** | **154** | 2 | ~$1.90 |
| **$5** | **385** | 5 | ~$4.75 |
| **$10** | **770** | 10 | ~$9.51 |
| **$15** | **770** | 10 | plenty of headroom |

If Astra/Fable turn out closer to 200 hidden tokens each, the corresponding balanced limits are roughly **77 for $2, 231 for $5, 539 for $10, and the full 770 for $15**.

I would preserve multiples of 77 rather than simply taking the first N examples. That maintains equal representation of every intent.

### How much data do we actually need?

At accuracy around 85%, approximate 95% margins for a single model are:

* 77 cases: ±8.0 percentage points
* 154: ±5.6 points
* 385: ±3.6 points
* 770: ±2.5 points

Because we're evaluating every model on the **same cases**, paired model-vs-model comparisons will often be substantially more sensitive than those individual intervals.

So my preferred progression is:

**77 → 385 → 770.**

I wouldn't bother with intermediate steps. If Jev is 70% and Astra is 90%, 77 will tell us immediately. If everyone lands around 84–88%, go directly to 385. If the differences are still only 1–3 points, finish all 770.

I would **not** run the full 3,080 BANKING77 test set initially. At the same assumptions it is around **$38** for the six models; it becomes worthwhile only if 770 leaves us trying to distinguish very small differences.

### One change I'd make to the experiment

Don't stop at accuracy.

Jev's central claim isn't merely classification; it is **calibrated decision probabilities**. Your repo is already unusually well set up to test exactly that.

For Jev, retain the entire 77-way probability distribution. Then compute:

**top-1 accuracy + Brier/NLL + ECE/reliability + AUROC for correct-vs-wrong + risk/coverage**

and put its top-choice probability beside your existing Luna token-logprob and prompted-confidence signals.

That turns this from “Is Jev a cheap BANKING77 classifier?” into a much more interesting result:

> **Does a purpose-built decision model actually produce better uncertainty than frontier generative LLMs?**

That's the experiment I think is worth publishing.

My recommendation is therefore: **budget $2 initially, but spend only ~$1 on a 77-case six-model pilot. Measure actual token costs. Then almost certainly spend the ~$5 for 385 cases; go to the full 770 only if the result is close enough to warrant it.** For a publishable comparison, I suspect the eventual total will be around **$10–15**, which is still tiny relative to the value of the result.

# User

OK, just run the 77-case six-model pilot as you have recommended. Share and interpret the results (including the calibration and other metrics) and re-estimate the cost. Also share if there are any other models (e.g. Gemini Flash 3.8) that you would recommend adding to the benchmark, and what the cost would be.

# ChatGPT

I ran the 77-case pilot: one randomly selected example from each BANKING77 intent, identical cases across all six models, using your existing benchmark prompt. The clean results are in:

~/code/llmevals/confidence-calibration/data/frontier-pilot-results.csv
~/code/llmevals/confidence-calibration/.build/frontier-pilot-summary.json

The main result is: **Jev is spectacularly cheap and fast, but this pilot does not support its calibration story. GPT-6 Astra was materially better on both classification and probability quality.**

| Model | Accuracy | Mean conf. | Conf−accuracy | Brier ↓ | ECE ↓ | AUROC ↑ | ≤5% error coverage* | Cost / 77 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **GPT-6 Astra** | **88.3%** | 94.0% | +5.7 pp | **0.088** | 0.057 | 0.840 | **79.2%** | $0.484 |
| GPT-5.6 Luna | 83.1% | 96.4% | +13.3 | 0.140 | 0.136 | 0.754 | 7.8% | $0.009 |
| GPT-5.6 Sol | 83.1% | 93.8% | +10.7 | 0.139 | 0.127 | 0.733 | 14.3% | $0.086 |
| Claude Fable 5.1 | 83.1% | 83.6% | **+0.4** | 0.120 | 0.057 | 0.786 | 62.3% | $0.761 |
| Claude Opus 5 | 79.2% | 79.9% | **+0.7** | 0.124 | **0.045** | **0.843** | 59.7% | $0.374 |
| **Jev** | **75.3%** | 87.4% | **+12.1** | **0.171** | **0.138** | 0.811 | 54.5% | **$0.0055** |

*The ≤5% risk-coverage thresholds were selected and measured on these same 77 cases. They are useful diagnostically but are **not prospective validation**.

The 95% accuracy intervals are broad at n=77. Jev was 58/77 and Astra 68/77. In the paired comparison, Astra got 11 cases right that Jev missed, while Jev got only one that Astra missed; exact McNemar p=0.0063. So **Astra > Jev is already a reasonably strong result**. The Luna/Sol/Fable differences from Jev are directionally ~+8 points but not yet solid enough at this sample size; Opus is only +4 points.

### The surprising part: Jev's calibration

This was the question I cared about most, and Jev did not win.

Its chosen-label probabilities averaged **87.4% while it was correct only 75.3%**. Binary Brier score was **0.171**, worse than every generative model tested. Its separate TypeSafe confidence statistic did essentially the same thing: Brier **0.169**, ECE **0.139**. So the special confidence output doesn't rescue the result.

More strikingly, **Jev returned exactly 1.00 probability on 33 of 77 cases. One of those was wrong.** At ≥95% probability, it made 3 errors among 45 cases (6.7%); at ≥90%, 7/51 were wrong (13.7%).

One example:

> “Good morning. I tried to make a purchase with my credit card ... Both times it was declined.”

BANKING77's gold label for that selected case is declined_transfer; Jev returned declined_card_payment with **1.00 probability**. In fairness, every one of the six models made the same prediction here, so this particular case is more evidence of taxonomy/dataset ambiguity than Jev failure.

There were **7/77 cases on which all six models missed the gold label**. That is an important caveat: we're giving models 77 label names but no detailed routing manual, and some BANKING77 distinctions are extremely fine.

Jev does have a useful positive result: its confidence ranked safe versus unsafe cases fairly well, **AUROC 0.811**, better than Luna, Sol, and Fable here. That fits your existing finding about logprobs: an imperfect probability can still be a useful routing score. But Astra (0.840) and Opus (0.843) were at least as good.

For Jev alone I could also evaluate the full 77-way distribution, because unlike the other benchmark calls it gives every class probability. Its multiclass Brier was **0.392** and NLL **2.01**. Those aren't directly comparable with the binary Brier column above unless we get full distributions from the other models too.

### Astra is the interesting winner

Astra's result is stronger than just 88.3% accuracy.

It had the **best Brier score, 0.088**, good ranking (AUROC 0.840), and its confidence was much closer to reality. Among its 61 predictions at ≥90%, only 3 were wrong. The exploratory 5%-error routing threshold covered **61/77 = 79%** of requests.

And it used surprisingly little reasoning: **1,022 reasoning tokens total across 77 cases**, about 13/case at low effort. So my earlier cost fear about Astra was too pessimistic.

Opus and Fable show another interesting pattern: they were less accurate than Astra but **much less overconfident**. Their mean stated probabilities almost exactly matched their aggregate accuracy. That doesn't automatically mean they are calibrated—Brier captures per-example quality better—but it's striking compared with Luna/Sol/Jev.

### Cost: we now have actual measurements

The intended six-model 77-case run cost:

**$1.7203 total**

using normal synchronous OpenRouter inference.

There was one execution wrinkle worth disclosing: a long tool call timed out while the requests were still executing, and the tooling replay spawned duplicate Opus/Fable calls before I detected and killed them. So the **actual account charge visible in the raw results was $2.5642**, of which **$0.8439 was duplicate execution**, not part of the benchmark. The clean CSV contains exactly 77 × 6 = 462 unique results.

For future runs, use OpenRouter :batch. Current batch prices are half the normal rates for Luna, Sol, Astra, Opus and Fable. [OpenRouter](https://openrouter.ai/openai/gpt-6-astra%3Abatch?utm_source=chatgpt.com) Jev remains so cheap that its contribution is negligible.

Using the **actual token consumption from this pilot**, my revised costs are approximately:

| Cases / model | Synchronous | Batch |
| --- | --- | --- |
| 77 | $1.72 | **$0.86** |
| 385 = 5/intent | $8.60 | **$4.31** |
| 770 = 10/intent | $17.20 | **$8.63** |
| 3,080 full test | ~$68.8 | **~$34.5** |

This is a much better estimate than my previous reasoning-token assumptions.

Jev itself cost just **$0.0055 for all 77 cases**, despite its Decisions interface consuming 131K metered input tokens because the 77 choice criteria are represented explicitly. OpenRouter currently lists Jev as a specialized structured decision model. [OpenRouter](https://openrouter.ai/typesafe?utm_source=chatgpt.com)

### Models I would add

I would add **three**, in this order.

**1. Gemini 3.8 Flash — definitely.** This is the biggest omission now: a strong Google model gives us another genuinely independent model family rather than another point on the OpenAI/Anthropic curve. It was released September 2 and currently costs $0.75/$3.75 per M standard, or **$0.375/$1.875 batch**. [OpenRouter](https://openrouter.ai/google/gemini-3.8-flash-20260902?utm_source=chatgpt.com)

For this 77-case prompt, I estimate roughly **$0.02 batch / $0.04 synchronous**, perhaps modestly higher depending on low-effort thinking tokens. At 770 cases, think **~$0.2–0.4**. So there is almost no reason not to include it.

**2. Claude Sonnet 5 — yes.** This one matters specifically because TypeSafe's launch comparison put Jev around Sonnet-class performance. Testing that claim on actual gold labels is more informative than testing yet another expensive flagship. Sonnet 5 batch is only **$1/M input + $5/M output**. [OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-5-20260630%3Abatch?utm_source=chatgpt.com) Based on the Anthropic token counts observed here, I'd expect about **$0.08 for 77 batch cases**, or ~$0.8 for all 770.

**3. DeepSeek V4.1 Flash — yes, as the cheap independent control.** It currently costs only **$0.15/M input + $0.60/M output**. [OpenRouter](https://openrouter.ai/deepseek/deepseek-v4.1-flash-20260910/?utm_source=chatgpt.com) A 77-case run should be around **one cent**, depending on reasoning-token use. If Jev's selling point is “special architecture lets us do classification incredibly cheaply,” a high-quality conventional model costing pennies is exactly the competitive baseline it needs.

I'd make **GPT-5.6 Terra optional**. Its batch price is $1/$6M, so roughly **$0.045 for 77 cases**. [OpenRouter](https://openrouter.ai/openai/gpt-5.6-terra%3Abatch?utm_source=chatgpt.com) But Luna and Sol already define the OpenAI family curve; Terra adds less information than Gemini, Sonnet or DeepSeek.

So the benchmark I'd publish is:

**Jev + Luna + Sol + Astra + Sonnet + Opus + Fable + Gemini 3.8 Flash + DeepSeek V4.1 Flash.**

The extra three add only roughly **$0.10 to the 77-case batch run**. More importantly, they turn the question from “How does Jev compare with models I happen to use?” into a credible **decision-model vs diverse frontier/good-cheap-LLM benchmark**.

My next experimental step would be **not 385 yet**. I would first add those three models to the same 77 cases for ~$0.10, because they could materially change the interpretation. Then, based on that nine-model result, take the interesting subset—not necessarily all nine—to 385 cases.

# User

Add the three models you recommended.

Create a ~/code/llmevals/jev/ directory with all inputs required to re-run this resumably and idempotently. Also add an index.html that explains the findings in simple, clear language, explaining implications to a senior business audience (rather than analytics savvy audience) in practical terms.

# ChatGPT

Completed in ~/code/llmevals/jev/.

The added models materially sharpened the result:

| Model | Accuracy | Cost / 77 | Extrapolated / 1K |
| --- | --- | --- | --- |
| GPT-6 Astra | 88.3% | $0.484 | $6.28 |
| **Gemini 3.8 Flash** | **87.0%** | **$0.092** | **$1.19** |
| GPT-5.6 Luna | 83.1% | $0.009 | $0.12 |
| GPT-5.6 Sol | 83.1% | $0.086 | $1.12 |
| Claude Fable 5.1 | 83.1% | $0.761 | $9.89 |
| Claude Opus 5 | 79.2% | $0.374 | $4.86 |
| **DeepSeek V4.1 Flash** | **79.2%** | **$0.0065** | **$0.085** |
| Claude Sonnet 5 | 77.9% | $0.150 | $1.95 |
| **Jev** | **75.3%** | **$0.0055** | **$0.072** |

The particularly useful new finding is Gemini: **67/77 vs Astra's 68/77**, while costing about 81% less in this run. On these 77 cases the Astra–Gemini difference is not meaningful statistically; they differ by just one correct answer.

DeepSeek is also an important control. It costs almost the same as Jev, yet scored **79.2% vs Jev's 75.3%**. So Jev's extreme price advantage largely disappears when compared with other cheap inference models rather than only frontier flagships.

The business-facing page leads with the practical implication: Jev saves only about **$0.04 per 1,000 classifications versus Luna**, while this pilot observed about **7.8 additional mistakes per 100 requests**. At most business error costs, inference price is therefore unlikely to justify choosing the weaker classifier.

The directory now contains:

* data/cases.csv — frozen one-per-intent 77-case input.
* data/results.jsonl — full nine-model results, including Jev's 77-way probability distributions.
* data/results.csv — flat analysis-friendly output.
* models.json — exact model IDs and inference settings.
* prompt.md — prompt contract and Jev-specific setup.
* run.py — resumable runner; completed (model, case) pairs are skipped.
* analyze.py — independently rebuilds metrics, CSV and HTML.
* summary.json — generated metrics.
* index.html — senior-business-audience explanation.
* README.md and justfile — reproduction instructions.

I verified just dry-run: **all nine models report 0 pending / 77**. Python syntax checks pass, analyze.py rebuilds the outputs from the raw JSONL, and I rendered index.html at desktop and mobile widths with no horizontal overflow. The page intentionally keeps the 77-case limitation prominent and also notes that **6/77 examples were missed by all nine models**, which is evidence that label-name-only BANKING77 has some intrinsically ambiguous cases.

The reproducible commands are simply:

Bash


```
cd ~/code/llmevals/jev
just dry-run
just run       # only missing calls
just analyze
```

No files outside the new jev/ directory were modified.

# User

_2026-09-18T03:34:37.287Z_

Commit required files to ~/code/llmevals/ and update README.md before that.

# ChatGPT

_2026-09-18T03:34:37.287Z_

Committed to ~/code/llmevals/.

Commit: cefa749 Add Jev BANKING77 benchmark

Also updated the repo-level README.md with the new September 18 Jev benchmark entry.

Checks passed: clean working tree, git diff --cached --check, regenerated analysis/page successfully, and just dry-run reports **0 pending / 77** for all nine models.

# User

Add a cost-quality scatterplot. Use relevant scales, e.g. log scale, clipped axes, etc. Make sure the models occupy space in the scatterplot well. Label them. Clicking opens a modal popup with relevant details.

Add a collapsed table showing results. Rows = 77 classification requests (actual input, without needing to show the 77 labels). Columns = models. Cells = the result of the classification, colored red if wrong, green if correct. Tooltips on red cells show the expected result.

# ChatGPT

Implemented in ~/code/llmevals/jev/.

The page now has:

* An interactive **cost vs accuracy scatterplot**:

* x-axis = cost per 1,000 classifications on a **log scale**
* y-axis deliberately clipped to **72–91% accuracy**
* all 9 models labeled directly
* Jev highlighted
* clicking or keyboard-activating any model opens a native modal with accuracy, cost, latency, confidence gap, Brier, ECE, AUROC, and token usage
* A collapsed **77 × 9 classification matrix** under Technical detail:

* rows = actual customer requests
* columns = models
* ✓ green = correct, ✕ red = wrong
* red-cell tooltips show the expected label
* sticky request/model headers and horizontal scrolling for the wide table

Both are generated by analyze.py, so just analyze recreates them reproducibly.

Verified:

* 9 scatter points
* 77 request rows × 9 model cells = 693 cells
* 567 correct / 126 wrong
* mouse and keyboard modal interaction
* matrix collapsed by default
* desktop and mobile rendering
* no page-level mobile overflow
* deterministic regeneration
* all models still 0 pending / 77
* Lighthouse: **Performance 1.00, Accessibility 1.00**
* git diff --check passes

Modified files are currently uncommitted:

Plain text

`jev/analyze.py jev/index.html`

# User

Allow the 77 classification results table occupy the full width of the page.
Make sure all labels in the scatterplot are close to their values. Astra and Fable are far away, and maybe others, too.

# ChatGPT

Updated.

The 77-result matrix now breaks out of the 980 px article column and uses effectively the full viewport width: at 1440 px it renders **1408 px wide with 16 px margins**. The prose and other content remain constrained for readability. On mobile, the matrix stays contained in the viewport and scrolls horizontally internally.

I also retuned every scatter label. All labels now sit immediately beside their points; Astra and Fable are about 10 px away rather than being displaced ~110 px. Right-side labels use right anchoring so they stay close without running off the plot.

Verified via rendered screenshots, desktop/mobile geometry, deterministic regeneration, syntax checks, and git diff --check. The benchmark still reports 0 pending / 77 for all nine models.

Uncommitted changes remain:

Plain text

`jev/analyze.py jev/index.html`

# User

_2026-09-28T03:11:42.454Z_

GPT-6 Luna is out. Update the benchmark to cover that.

# ChatGPT

_2026-09-28T03:11:42.454Z_

Updated the benchmark with GPT-6 Luna across the same frozen 77 BANKING77 cases.

GPT-6 Luna result:

* Accuracy: **60/77 = 77.9%**
* Mean confidence: **92.0%**
* Brier: **0.190**
* ECE: **0.183**
* AUROC: **0.739**
* Median latency: **1.07s**
* Cost: **$0.00431 for 77 cases**
* Extrapolated cost: **$0.056 per 1,000 classifications**

The interesting result is that GPT-6 Luna was the **cheapest model in this benchmark**, even cheaper than Jev:

* GPT-6 Luna: **$0.056 / 1,000**, 77.9% accuracy
* Jev: **$0.072 / 1,000**, 75.3% accuracy
* DeepSeek V4.1 Flash: **$0.085 / 1,000**, 79.2%
* GPT-5.6 Luna: **$0.115 / 1,000**, 83.1%

The GPT-6 Luna vs Jev difference is only 2 cases and not statistically meaningful on 77 examples (paired p≈0.73), so I would not claim GPT-6 Luna is generally more accurate. But **Jev can no longer claim a cost advantage in this comparison**.

I updated:

* models.json
* data/results.jsonl
* data/results.csv
* summary.json
* analyze.py
* index.html
* README.md

The page now dynamically describes **10 models**, includes GPT-6 Luna in the scatterplot/modal and 77×10 classification matrix, updates the business interpretation, and notes that GPT-6 Luna is the cheapest observed model.

Validation passed:

* **770 unique results = 10 × 77**
* all models report 0 pending / 77
* deterministic rebuild is stable
* git diff --check passes
* scatterplot renders all 10 labels cleanly
* result matrix has 77 rows × 10 model cells
* GPT-6 Luna modal shows the expected metrics

The changes are currently uncommitted.

# User

Commit and push.

# ChatGPT

Committed and pushed.

Commit: d4ef855 Add GPT-6 Luna to Jev benchmark

Remote main now points to the same commit, and the working tree is clean.

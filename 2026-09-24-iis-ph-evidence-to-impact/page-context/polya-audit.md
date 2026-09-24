# The 80-Year Blind Spot: The Polya Audit

URL: https://sanand0.github.io/datastories/polya-for-ai/

The Polya Audit · March 2026
6,747 AI experiments · 3 models · 15 heuristics · 7 math domains

Mathematics × Artificial Intelligence × Experimental Method

# The 80-Year Blind Spot

In 1945, George Pólya gave mathematicians 15 rules for solving problems. For eight decades, they were treated as gospel. Nobody ever tested them. Until now.

March 26–27, 2026 · Based on 6,747 AI experimental runs

"We haven't done many experiments as to, if we have two different ways to solve a problem, which is more effective. We have some intuition, but we haven't done large-scale studies where we take a thousand problems and just test them."
— Terence Tao,
Dwarkesh Patel Podcast, 2024

### The Setup

## A Book That Became Doctrine

Picture a classroom in Budapest, sometime in the 1940s. A short, sharp-eyed mathematician named George Pólya is teaching a student who is stuck on a problem. He asks: "Do you know a related problem?" The student thinks. Something clicks.

Pólya had spent decades observing how humans — both brilliant and ordinary — actually solve mathematical problems. He catalogued the patterns. In 1945, he published them in a small book called How to Solve It. It sold over a million copies. It is still in print. It is still assigned in universities.

His 15 heuristics — work backwards, find a simpler case, use an extremal element, exploit symmetry, find an invariant — have been transmitted, unchanged, through eight decades of mathematical education. Every math olympiad coach uses them. Every textbook references them.

Nobody ever ran an experiment to see if they worked.

This is not unusual. Mathematics has been, almost uniquely among intellectual disciplines, a field without an experimental culture. Physics experiments. Biology experiments. Even economics experiments. But mathematics treats its pedagogical wisdom the way it treats its theorems: as things to be accepted once proven, not periodically re-tested. Pólya's rules weren't proven — they were observed. And the observations were never replicated at scale.

Until now. Using three large language models, 6,747 problem-solving runs, the MATH benchmark, and one month of compute time, we ran the first empirical audit of Pólya's advice. The results are stranger than anyone expected.

### The Method

## How You Audit 80 Years of Math Advice

The logic is simple, even if the execution wasn't. Take a hard math problem. Tell an AI model to solve it — but this time, force it to use one specific Pólya heuristic. Measure whether it gets the right answer. Repeat 6,747 times.

How Each Run Worked

6,747

Total AI Runs

3

AI Models Tested

15

Pólya Heuristics

7

Math Categories

$1.71

Total API Cost

The three models — GPT-5.4-nano, Gemini 2.5 Flash Lite, and Claude Haiku 4.5 — were each given the same 20 problems per cell at difficulty Level 5, the hardest tier. The full experiment script and heuristic definitions are on GitHub. For each problem, they were given either no instruction (the baseline), or a system prompt that explicitly forced one of Pólya's 15 strategies. The answer was then checked against the ground truth.

The question wasn't can AI do math? All three models solve harder problems than most humans on their best day. The question was: does Pólya's framing help?

### The Main Finding

## Three Models. Three Completely Different Answers.

The first thing you expect when you run a study like this is a clean result. Heuristics help, or they don't. What you do not expect is three models with three diametrically opposite responses to the same advice.

↓ 10%

GPT: worst heuristic penalty

↑ 6%

Gemini: best heuristic gain

≈ 0%

Haiku: essentially immune

14/15

heuristics consistently hurt Number Theory — and help Prealgebra

Heuristic Effect on Each Model (Δ from baseline accuracy)

Each dot is one heuristic's average delta from baseline. Hover for details. The spread reveals each model's "coachability."

GPT-5.4-nano's built-in problem-solving strategy is already good — every heuristic we imposed made things worse, some catastrophically so. Gemini is more like a student who benefits from being told which lens to use: it gains up to 6 percentage points from the right heuristic. Claude Haiku is the most remarkable: it seems to hear the instruction, nod politely, and then solve the problem exactly the way it was going to anyway. Its performance barely moves regardless of what you tell it.

This isn't noise. Across all 15 heuristics and 7 categories, GPT's performance ranges 13.6 percentage points from best to worst heuristic. Gemini spans 8.5 points. Haiku spans just 3.4 points — barely above statistical noise.

And here is the model-level finding: 12 out of 15 heuristics produce opposite-sign effects on GPT versus Gemini. The same instruction that helps one model hurts the other. But there is an even stronger signal in the data — one that cuts across all three models. The single best predictor of whether Pólya's advice will work is not who you're asking. It's what kind of problem you're solving.

### The Full Picture

## Every Heuristic, Every Category, Every Model

The real texture of the data lives in this heatmap. Each cell shows how a model's accuracy changes from the baseline when forced to use a given heuristic. Blue means it helped. Red means it hurt. Click any cell to dig in.

GPT-5.4-nano
Gemini 2.5 Flash Lite
Claude Haiku 4.5

Δ from Baseline
Raw Accuracy
Click a cell for details

Category
Baseline (No Heuristic)

Work Backwards

Simpler Case

Contradiction

Induction

Extremal Element

Invariant

Change Repr.

Symmetry

Count 2 Ways

Pigeonhole

Auxiliary

Analogy

Generalize

Case Analysis

Pattern Recog.

Algebra
–

-5%

-10%

-5%

+0%

-5%

+0%

-5%

+0%

+0%

+5%

-5%

+5%

-5%

+5%

-15%

Counting & Prob.
–

+5%

-5%

-10%

+5%

-10%

-5%

+0%

-5%

-5%

+5%

+0%

-10%

-15%

+10%

-5%

Geometry
–

-5%

+0%

+0%

-5%

-15%

-15%

+0%

+0%

-20%

-10%

-25%

-5%

-15%

-15%

-10%

Intermediate Alg.
–

+0%

+0%

+5%

+0%

-10%

-5%

+5%

-10%

-5%

-15%

-10%

-15%

+0%

-10%

-5%

Number Theory
–

+0%

-5%

-15%

-15%

+0%

-20%

-15%

-15%

-15%

-10%

-5%

-5%

-5%

-15%

-20%

Prealgebra
–

-5%

+0%

+10%

+5%

+5%

+10%

-10%

+5%

-5%

+10%

+0%

+0%

+5%

+15%

+0%

Precalculus
–

+0%

-5%

+0%

-10%

+0%

-5%

+0%

+5%

-5%

-10%

-10%

+0%

+0%

-5%

-15%

Worse ←

→ Better
Scale: ±25 percentage points from baseline

The heatmap contains a full story in each row and column. Number theory is nearly at the ceiling — the AI models already solve 90–95% of problems without any guidance. Any heuristic that pulls them away from their natural approach is almost guaranteed to hurt. Geometry is the chaos zone: heuristics have wild effects that differ not just in magnitude but in direction across models. Counting and probability is the one area where heuristics reliably help, particularly case analysis. The row patterns — which categories respond positively vs. negatively — are so consistent that they reach statistical significance: 14 of 15 heuristics show the same directional effect within each of four categories (p < 0.001). Click any category label to see its full profile.

### Key Findings

## What the Data Actually Says

### Finding #1 — The Geometry Catastrophe

The single most dramatic result in the dataset: telling GPT to "introduce auxiliary elements" — Pólya's advice to add a construction line, a helper variable, an intermediate expression — collapses GPT's geometry accuracy from 55% to just 30%. That is a 25-percentage-point drop from a single sentence of guidance.

Geometry accuracy: Baseline vs. "Introduce Auxiliary Elements"

The same instruction behaves completely differently on the other models: Haiku gains +14% on geometry when given auxiliary elements. The instruction isn't bad — it's that GPT's spatial reasoning is disrupted by being told to "add something new," while Haiku can absorb and use it.

What's happening? GPT likely has a strong internal geometric schema that works well by default. The auxiliary elements instruction forces it to generate distractors — elements that seem relevant but ultimately redirect its attention away from the direct path to the solution. Haiku, with stronger instruction-following, actually builds the auxiliary construction and uses it correctly.

### Finding #2 — The Three Universal Losers

Three heuristics hurt all three models. These are the techniques that Pólya himself would likely acknowledge are highly domain-specific: mathematical induction, the pigeonhole principle, and pattern recognition (examine small cases, find a pattern, conjecture and prove).

Average Δ from baseline — three heuristics that hurt all models

Pattern recognition is the worst offender for GPT, dropping accuracy by 10 percentage points overall. The instruction to "tabulate instances and find a pattern" encourages slow enumeration when direct calculation is faster and more reliable. The models that benefit from inductive enumeration were already doing it when appropriate — being forced into it blindly causes them to waste time and make errors.

### Finding #3 — Case Analysis is the Most Reliable Heuristic

The single most reliable heuristic across all models and categories is case analysis — exhaustively splitting a problem into mutually exclusive, collectively exhaustive cases. For counting and probability problems, it helps every model.

Counting & Probability accuracy: Baseline vs. "Case Analysis"

Why? Counting and probability problems are structurally case-based. When you ask "how many ways can two dice sum to 7?", the natural solution is to enumerate the cases: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). The case analysis heuristic isn't fighting against any existing strategy — it's aligning with the problem's natural decomposition. This is the heuristic that Pólya would be most vindicated by: it works when the problem structure matches the heuristic structure.

### Finding #4 — 12 of 15 Heuristics Flip Sign Between Models

This is perhaps the most profound finding. Symmetry, for example: Gemini gains 6.1 percentage points when told to exploit symmetry. GPT loses 2.9 points. The same words, the same problems — and the effect is opposite in sign.

Δ from baseline per heuristic — GPT (orange) vs. Gemini (blue). ⇄ = sign flip.

The three exceptions — the only heuristics that are consistently negative for both GPT and Gemini — are induction, pigeonhole, and contradiction. These are techniques with narrow applicability. Forcing them onto general Level-5 problems, where they usually don't apply, causes models to argue themselves into wrong corners.

### Finding #5 — The Strongest Signal: Problem Type Beats Model and Heuristic

Forget which heuristic you pick. Forget which model you're using. The single biggest predictor of whether Pólya advice will help is what kind of problem you're facing. Four of seven categories show statistically significant directional consistency across all 15 heuristics (p < 0.001 each, binomial test) — a result that holds regardless of model.

Average Δ from baseline per category — averaged across all 15 heuristics & 3 models

Prealgebra benefits from 14 of 15 heuristics — virtually anything you tell the model to try, it productively applies.
Intermediate Algebra, Number Theory, and Precalculus are hurt by 14 of 15 heuristics — any scaffolding you impose makes things worse.
The divide is not about difficulty. Number theory problems hit near-ceiling accuracy (≥85%) yet still consistently decline under heuristics, while prealgebra problems at similar difficulty levels consistently rise.
The true axis is structural decomposability: prealgebra problems naturally split into cases; number theory and precalculus require deep, domain-specific insight that generic prompts can only displace.

### The Full Scorecard

## Which Heuristics Win — And Where?

The heatmap shows every individual cell. This table summarizes the pattern: for each Pólya heuristic, how much does it help or hurt — averaged across either problem types or AI models?

Which split is more insightful? Problem type turns out to be the stronger predictor (average std 4.3%) than model choice (2.7%). The same heuristic's effect swings more dramatically across math domains than across AI systems. The table defaults to showing the breakdown by problem type — more useful for practitioners who know what kind of problem they're working on. Toggle to the by model view to see the sign-flip story.

Statistical context: With ~20 problems per cell, effects under ±11% (overall) or ±17% (per-category) should be treated as directional signals, not definitive results. Cells are shaded by confidence: faint = likely noise, vivid = stronger signal.

By Problem Type (avg across 3 models)
By AI Model (avg across 7 categories)
Click column headers to sort · Click cells for details

Heuristic ·Algebra·Counting·Geometry·Int. Alg.·Num. Theory·Prealgebra·Precalculus·Average↑

Symmetry ▶-1.7%+5.4%+0.0%-6.7%-3.3%+8.7%+1.7%+0.6%

Change Repr. ▶-2.6%+5.1%+0.0%+1.7%-3.3%+0.4%-1.7%-0.1%

Work Backwards ▶-1.0%+6.8%+3.3%-3.3%-3.3%-1.3%-1.7%-0.1%

Case Analysis ▶+2.4%+7.1%-3.3%-3.3%-5.0%+8.3%-7.5%-0.2%

Simpler Case ▶-7.7%+6.9%+6.1%-0.8%-5.0%+0.4%-3.3%-0.5%

Contradiction ▶+0.2%-0.2%+3.3%-0.1%-6.8%+7.0%-8.3%-0.7%

Analogy ▶+2.4%-1.2%+1.7%-6.7%-1.8%+0.4%-1.7%-1.0%

Generalize ▶+0.8%-1.9%-1.7%-2.4%-5.0%+3.3%-2.6%-1.4%

Pigeonhole ▶+3.0%+3.8%-1.7%-10.7%-6.7%+5.0%-8.3%-2.2%

Induction ▶-4.0%+7.1%+0.0%-5.8%-6.8%+0.4%-7.5%-2.4%

Invariant ▶-2.8%+2.1%+0.0%-5.0%-10.0%+3.7%-5.0%-2.4%

Extremal Element ▶-3.3%+0.4%-3.8%-10.7%+1.7%+3.7%-5.4%-2.5%

Auxiliary ▶-4.4%+5.4%-5.3%-6.7%-3.6%+3.7%-8.3%-2.7%

Count 2 Ways ▶+0.0%-1.2%-8.3%-3.3%-6.7%+3.7%-5.9%-3.1%

Pattern Recog. ▶-6.1%-1.2%-3.3%-0.6%-8.3%+3.4%-10.0%-3.7%

Worse ← | → Better than baseline

Opacity = effect size (faint = likely noise, solid = strong signal)

★ = statistically significant (|Δ| > 11% overall, 17% per-category)

### Wider Context

## What This Connects To

The finding that heuristics have opposite effects on different models isn't just a quirk of these three models. It maps directly onto a growing body of research on prompt sensitivity in large language models. A 2023 study by Sclar et al. found that minor wording changes can alter LLM performance by tens of percentage points — far more than any algorithm change. What we're seeing with Pólya's heuristics is the same phenomenon at a conceptual level.

The GPT personality — "don't tell me how to think" — has a clear analogue in the research literature on chain-of-thought prompting. Larger, more capable models benefit less from explicit reasoning scaffolds because they've internalized the scaffolding during training. Wei et al. (2022) showed this for chain-of-thought reasoning. The Pólya audit is showing the same thing for higher-level heuristics: a model that has already learned to decompose into cases doesn't benefit from being told to decompose into cases.

The Gemini result — "scaffolding helps me organize" — also makes theoretical sense. Gemini's architecture optimizes differently, and may have had less reinforcement-learning fine-tuning toward autonomous problem-solving, leaving more room for prompt-level steering.

The category divide has its own analogue in human cognition research. Domain-specific expertise studies consistently show that novices benefit from general heuristics while experts are disrupted by them — because experts have internalized domain-specific shortcuts that are more efficient than any general strategy. The AI equivalent: models that have seen millions of number theory problems have already internalized the invariant-based and modular reasoning those problems require. Telling them to "work backwards" is like telling a grandmaster to think about the rules.

And Haiku's immunity? This is the most intriguing result. Haiku achieves near-identical performance regardless of heuristic, which suggests it has built a kind of meta-strategy — a way of approaching math problems that is flexible enough to incorporate any framing without being dominated by it. It hears "use symmetry" and uses symmetry when it's useful, but doesn't force the point when it isn't. This is, arguably, what Pólya was actually advocating: not mechanical application of heuristics, but heuristics as lenses to try.

A note on methodology: Each cell in the heatmap represents 20 problems at difficulty Level 5. With n=20, a 10-percentage-point difference corresponds to a 2-problem swing — significant as a trend but small as an absolute count. The most dramatic findings (the geometry catastrophe at −25%, case analysis at +16% for Gemini's counting problems) would survive stricter statistical thresholds. The smaller effects (±2–4%) should be treated as directional signals, not definitive conclusions. A pre-registered follow-up with n=100 per cell would settle the question.

### Implications

## What Pólya Would Make of This

George Pólya was a careful empiricist in the way that mathematicians of his era were careful: he observed, he catalogued, he reflected. He was not wrong. He was working without a key tool — the ability to run the same experiment a thousand times and measure outcomes.

The audit's central finding is not that Pólya was wrong. It's that his heuristics are context-dependent in two distinct layers. The first layer is problem type: heuristics consistently help prealgebra and consistently hurt number theory, intermediate algebra, and precalculus — regardless of model, regardless of which heuristic. That signal is statistically robust. The second layer is model personality: within any given problem type, GPT and Gemini can still disagree on sign. Pólya's advice needs to be matched first to the domain, then to the solver.

#### For AI Math Tutors

Start with the problem, not the heuristic. If a student is working on number theory or precalculus, no Pólya heuristic reliably helps — save the coaching. If they're on counting or prealgebra, almost any structured hint will move the needle. Then consider the model: Gemini responds to symmetry and analogy; GPT needs case analysis; Haiku doesn't need any of it.

#### For Math Pedagogy

The finding that pattern recognition is the worst heuristic for AI should give math teachers pause. We teach "tabulate small cases, find a pattern" as a general strategy. The data suggests it's not: it works when you need to guess a formula, not when direct calculation is available.

#### For the Tao Vision

Terence Tao called this kind of experiment "the experimental side of math" and said AI would revolutionize it. The Pólya Audit cost $1.71 and took one day. It generated the first empirical data on a question that has been debated for 80 years. That is the revolution beginning.

The deeper implication is methodological. If we can empirically test Pólya's heuristics, we can empirically test anything in mathematical pedagogy. Which representation (algebraic vs. geometric) helps more? Which order of topics produces better transfer? What's the optimal mix of worked examples and practice problems? These questions have been debated for decades by people with strong opinions and almost no data. The tools now exist to answer them.

Mathematics has been producing evidence-free folk wisdom for centuries. The audit has begun.

The Pólya Audit · 6,747 experiments run March 26, 2026

Models: GPT-5.4-nano (OpenAI) · Gemini 2.5 Flash Lite (Google) · Claude Haiku 4.5 (Anthropic) ·
Dataset: MATH Benchmark (Hendrycks et al., 2021)

Experiment Prompts ·
Source Code ·
Heuristic Definitions ·
Results Data (JSON) ·
Full Repository

Pólya, G. (1945). How to Solve It. Princeton University Press. ·
Tao, T. (2024). Dwarkesh Patel Podcast. ·
Hendrycks, D. et al. (2021). Measuring Mathematical Problem Solving. arXiv:2103.03874. ·
Wei, J. et al. (2022). Chain-of-Thought Prompting. NeurIPS. ·
Sclar, M. et al. (2023). Quantifying LLM Sensitivity to Prompt Design. arXiv:2310.11324.

×

Pólya Heuristic

Pigeonhole

If n+1 items fit into n containers, some container holds ≥2 items.

-3.6%

GPT-5.4-nano

-1.4%

Gemini

-1.7%

Haiku

Δ from baseline by category (sorted best→worst avg)

Category
GPT
Gemini
Haiku
Avg

Prealgebra
+10.0%+5.0%+0.0%
+5.0%

Counting & Prob.
+5.0%+11.3%-5.0%
+3.8%

Algebra
+5.0%+3.9%+0.0%
+3.0%

Geometry
-10.0%+0.0%+5.0%
-1.7%

Number Theory
-10.0%-15.0%+5.0%
-6.7%

Precalculus
-10.0%-5.0%-10.0%
-8.3%

Intermediate Alg.
-15.0%-10.0%-7.1%
-10.7%

The exact system prompt used:

Solve using the PIGEONHOLE PRINCIPLE: Identify 'pigeons' (objects) and 'holes' (containers). If there are more pigeons than holes, some hole holds ≥2.

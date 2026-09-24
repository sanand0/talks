# Does 95% confidence really mean 95% correct?

URL: https://sanand0.github.io/llmevals/confidence-calibration/#?threshold=95&models=gpt-5.6-luna%2Cgpt-4.1-nano

Confidence calibration

What to doExperimentsMethod & data

A small experiment with real support requests

# 95% confident
doesn’t mean 95% correct.

We gave LLMs 770 customer-support requests from BANKING77. For each one, the model chose an intent label and reported the probability that its answer was exactly right. Then we checked against the benchmark’s gold label.

770real support requests tested

77possible intent labels

10requests sampled per intent

What should you actually do?

## Don’t trust the number. Test what the number means.#

Treat an AI confidence score as a signal to test, not a guarantee. Ask the model to express uncertainty, replay it on past cases where you already know the right answer, then choose the score and cutoff that remove the most human review while staying inside your acceptable error rate.

1 · Ask betterMake uncertainty acceptable.

Don’t force the model to sound certain. Ask it to consider competing answers and report the winning probability. In this experiment, that simple prompt change made “95% confident” much safer.

2 · Measure realityReplay reviewed cases.

Take examples whose correct outcome is already known. For each score, measure how often the AI was actually wrong. Never choose “95%” just because it sounds reassuring.

3 · Route by riskPick the threshold from your SLA.

If you can access logprobs, test them as a ranking signal too. Choose a cutoff on historical cases, freeze it, and confirm that exact rule on untouched cases before removing review.

Example from these 770 cases: With Luna's original confidence wording, cases scored at least 95% were still wrong 10.3% of the time. Asking it to distribute probability across competing labels cut that to 3.9%. Raw token logprobs looked even more certain—98.4% on average for a model that was only 83.6% correct—so a raw logprob is not a trustworthy probability either. But as a ranking signal, a logprob cutoff chosen on 770 historical cases auto-passed 65.2% of 2,310 untouched cases at 4.4% observed error, versus 41.2% at 2.6% for the frozen stated-confidence rule.

The practical recipe: better confidence prompt → historical gold cases → compare risk signals → choose a cutoff → confirm it on untouched cases → auto-pass only after it survives.

Four experiments

## What changes a confidence score?#

Each experiment isolates a different source of confidence. Jump directly to the result you care about.

1 · BaselineDoes 95 mean 95?Both models report probabilities higher than their actual correctness.
2 · Prompt wordingCan asking better help?Explicit uncertainty and competing-label prompts make Luna substantially better calibrated.
3 · Context lengthDoes irrelevant text matter?Nano becomes about six points more confident when 2,000 irrelevant words are added.
4 · Internal probabilityDo logprobs know better?Raw logprobs are worse probabilities, but better at ranking which answers are risky.

Result

## The models were more certain than they were right.#

Overall accuracy and average stated confidence should be close if confidence is well calibrated. Here they are not.

GPT-4.1 NanoGPT-5.6 Luna

### GPT-5.6 Luna

Actually correct84.0%

Average stated confidence95.7%

Overconfidence11.6 points

770 completed support requests.

### GPT-4.1 Nano

Actually correct61.0%

Average stated confidence87.1%

Overconfidence26.1 points

770 completed support requests.

What stated confidence actually meantPerfect calibration sits on the diagonal

Each point is a confidence band; its size reflects how many requests fell in that band. Hover, tap, or keyboard-focus a point for the exact numbers. Points below the diagonal mean the model was overconfident.

Show a few high-confidence mistakes

100% confident

“My transfer is pending.”

Gold labelbalance_not_updated_after_bank_transferModel chosepending_transferModelGPT-5.6 Luna

100% confident

“Someone stole my cards!”

Gold labellost_or_stolen_phoneModel choselost_or_stolen_cardModelGPT-5.6 Luna

95% confident

“Are virtual cards available to get?”

Gold labelgetting_virtual_cardModel choseget_virtual_cardModelGPT-4.1 Nano

95% confident

“Why do I have to verify my identity?”

Gold labelwhy_verify_identityModel choseverify_my_identityModelGPT-4.1 Nano

Prompting helps

## How you ask for confidence changes the curve.#

We held everything else fixed: same GPT-5.6 Luna, same 770 requests, same labels. Only the confidence instruction changed. The quoted text below is the exact fragment appended to the prompt—copy it directly if you want to try the same technique.

### Baseline

Original request for a probability of exact correctness.

your probability that your chosen label exactly matches the gold routing label. Treat confidence as a probability of correctness, not a vague feeling.

Actually correct84.0%

Average confidence95.7%

Error when ≥95%10.3%

### Okay to be uncertain

Explicitly permit uncertainty instead of defaulting high.

It is completely okay to be uncertain. Do not default to high confidence just because you must choose a label. If more than one label is genuinely plausible from the request, lower the confidence accordingly. Report your best estimate of the probability that the chosen label exactly matches the gold routing label.

Actually correct84.5%

Average confidence90.7%

Error when ≥95%4.3%

### Strongest alternative

Consider the closest competing label before scoring.

Before assigning confidence, account for the strongest plausible competing label. Your confidence is the probability that your chosen label exactly matches the gold routing label after allowing for that alternative. If the best alternative is close, confidence should be correspondingly lower; reserve very high confidence for cases with little plausible ambiguity.

Actually correct84.9%

Average confidence92.4%

Error when ≥95%3.7%

### Top-two probability

Allocate probability across plausible labels, then report the winner's share.

Silently identify the two most plausible allowed labels and allocate probability between them and any remaining plausible labels so the probabilities would sum to 100%. Choose the highest-probability label. Report that label's probability as confidence. Do not collapse uncertainty just because only one label can be returned.

Actually correct84.8%

Average confidence90.0%

Error when ≥95%3.9%

Same model, different confidence instructionsCloser to the diagonal is better

Best practical result: prompting the model to keep uncertainty across competing labels reduced the overconfidence gap without changing the task. A literal “X% should mean X out of 100” instruction was also tested on all 770 cases, but barely improved calibration, so it is omitted from this chart.

Also tested: long-run frequency wording (little benefit)

Treat confidence as a literal long-run probability, not as emphasis or a feeling. If you report X%, then across many decisions for which you report about X%, roughly X% should exactly match the gold routing label. Use the full 0–100 range when warranted; 60%, 75%, or 85% are perfectly acceptable. Report your best probability estimate.

How we found the new prompt

## Screen cheaply, then promote.

We tried five additional mechanisms on a balanced 154-case screen (2 per intent). The most promising new one—allocating probability across the top competing labels—was then run on all 770 cases.

Screened instructionAccuracyMean confidenceBrier ↓Error when ≥95%

Baseline

Original confidence request.

85.7%95.8%0.1098.8%

Anchored scale

Give concrete meanings to 50%, 70%, 85%, 95%, and 99%.

85.1%96.2%0.12110.1%

Evidence balance

Weigh discriminating evidence against remaining ambiguity.

84.4%93.2%0.1057.3%

Independent recheck

Choose a label, then score it as a fresh second judgment.

85.7%94.9%0.1036.2%

Proper scoring rule

Say the probability will be judged with a proper scoring rule.

85.7%92.8%0.0976.6%

Top-two probability

Allocate probability across the most plausible labels first.

84.4%90.1%0.0912.9%

Brier score measures probabilistic accuracy: lower is better. Screening is only for choosing what to test fully; the headline conclusions use all 770 cases.

Context length

## More context can make a model more confident—not more right.#

We replayed the same 770 requests with 0, 500, or 2,000 words of deliberately irrelevant neutral metadata. The extra text was explicitly marked incidental. If confidence is robust, irrelevant context should not systematically move it.

### GPT-4.1 Nano

With 2,000 irrelevant words: confidence +6.1 pts, accuracy -1.0 pts.

Stated confidence84.2% → 90.3%

Actually correct61.2% → 60.1%

Overconfidence gap23.0 → 30.1 pts

Brier change vs 0 words+0.038 (clearly worse)

Error among ≥95%18.9% → 25.7%

### GPT-5.6 Luna

With 2,000 irrelevant words: confidence +0.1 pts, accuracy -0.4 pts.

Stated confidence96.1% → 96.2%

Actually correct85.7% → 85.3%

Overconfidence gap10.4 → 10.8 pts

Brier change vs 0 words+0.006 (CI includes no change)

Error among ≥95%9.0% → 10.2%

Accuracy vs. stated confidence as irrelevant context growsSame 770 requests in every condition

Stated confidenceActually correct

Paired stress test: every condition uses exactly the same cases. For Nano, the worsening Brier score is statistically clear under a paired bootstrap; for Luna, the confidence intervals include no change.

Natural ticket length points the same way for Nano, but is not causal. On the unpadded requests, Nano accuracy falls from 68.7% for 3–6 words to 51.6% for 12+ words, while confidence barely moves (84.5% → 83.5%). Luna changes much less (85.5% → 83.7% accuracy). Longer real tickets may simply be harder, so the padded experiment above is the cleaner test.

What this does—and does not—show. The padding is neutral, repetitive metadata, so this isolates sensitivity to extra irrelevant context better than comparing naturally short and long tickets. It does not tell us how either model behaves on genuinely information-rich 2,000-word documents.

Internal probability

## Use logprobs to rank risk—not as probabilities.#

On the same 770 requests, GPT-5.6 Luna produced both a token logprob and a prompted confidence score for the same answer. We asked two different questions: does the number itself mean what it says, and does it at least tell us which answers are safer?

Which should you use? If you need a number that roughly means “chance this answer is right,” the prompted confidence score is easier to interpret. If you need to decide which answers can skip human review, logprobs were more useful here—but only after choosing and validating a cutoff on historical cases.

Do not read literally99% logprob does not mean 99% correct.

Raw token probabilities were badly overconfident. Treat them as scores, not probabilities.

Use the orderingHigher logprobs still tended to mean safer answers.

That ordering was better than stated confidence at separating correct from incorrect answers, even though the logprob values themselves were misleading.

Deploy by cutoffLearn a threshold, then test that exact threshold.

Use reviewed historical cases to find a cutoff for your error budget. Freeze it and test it on new cases before removing human review.

The comparison in numbers. Raw stated confidence was closer to a real probability (Brier 0.119 vs 0.148 for logprob). Raw logprobs were extremely overconfident: 435 answers had effectively 100% token probability, yet 18 were wrong (4.1% error). But logprobs ranked correct versus incorrect answers better (AUROC 0.830 vs 0.783). That ranking—not probability calibration—is the reason to test logprobs for routing.

Practical rule: confidence score for an interpretable probability; logprob for ranking risk. Never assume either is safe enough for automation until the exact cutoff has been tested on your own held-out cases.

How accurate are logprobs vs confidence scores?All 3,080 cases · same “number of nines” scale on both axes

Raw token logprobPrompted confidence

X axisLinearNines
Y axisLinearNines

All 3,080 paired cases are shown. Logprob uses one-“nine” bands (145, 153, 178, 213, 267, 442, 1682 cases); prompted confidence uses familiar score bands (380, 635, 252, 532, 503, 757, 21 cases). Points on the perfect-calibration reference mean reported certainty matches observed accuracy. Use the axis toggles to inspect the same data on ordinary percentage or “number of nines” scales.

Why this scale? Both axes plot −log10(1 − p), the “number of nines” of certainty: 90% = 1, 99% = 2, 99.9% = 3, and so on. Applying the same monotonic transform to reported certainty and actual accuracy makes the perfect-calibration reference a true diagonal again. Tick labels remain ordinary percentages. This chart pools the 770 development cases and 2,310 holdout cases after the prospective test; the frozen holdout result below remains separate and was not retuned.

### Token logprob

Internal probability of the first one-token class decision.

Raw mean score98.4%

Raw Brier0.148

Ranks correctness · AUROC0.830

Development coverage at ≤5% error65.2%

### Stated confidence

The Top-two confidence number emitted immediately after that same decision.

Raw mean score88.2%

Raw Brier0.119

Ranks correctness · AUROC0.783

Development coverage at ≤5% error43.1%

If we trust the highest-scored answers first, how quickly does error rise?Actual deployable cutoffs only · equal scores stay together

Token logprobPrompted confidence

This is the ranking chart. Every point is an actual score threshold you could deploy; ties are never split. That is more faithful than equal-count deciles for these data. Probability calibration is omitted because a monotonic rescaling cannot improve the ordering.

SignalRaw Brier ↓Ranks correctness · AUROC ↑Development coverage at ≤5% error ↑

Token logprob

First decision token

0.1480.83065.2%

Stated confidence

Top-two prompt

0.1190.78343.1%

Do not use raw logprob as a probability. Luna was 83.6% correct, but raw token probability averaged 98.4%, and 435/770 token probabilities were effectively 100% despite 18 mistakes. Prompted confidence was much closer to reality (Brier 0.119 vs 0.148). The useful part of logprob is the ordering: it ranked mistakes better (AUROC 0.830 vs 0.783), which is what the routing experiment below tests prospectively.

Prospective holdout

## Did the frozen rule survive new cases?#

Before running the remaining 2,310 BANKING77 test requests, we froze the raw-score cutoffs that had kept observed training error at or below 5%. We then applied those exact cutoffs unchanged—no retuning on the holdout.

### Token logprob

Frozen on 770 cases; evaluated once on 2,310 untouched requests.

Training coverage at ≤5% error65.2%

Holdout coverage65.2%

Holdout observed error4.4%

95% CI for holdout error3.5%–5.5%

Auto-passed1506 / 2310

### Stated confidence

Frozen on 770 cases; evaluated once on 2,310 untouched requests.

Training coverage at ≤5% error43.1%

Holdout coverage41.2%

Holdout observed error2.6%

95% CI for holdout error1.8%–3.9%

Auto-passed951 / 2310

The 5% routing advantage survived; do not assume every cutoff will. The frozen logprob rule auto-passed 1506/2310 (65.2%) with 66 errors (4.4% observed error). The frozen stated-confidence rule auto-passed 951/2310 (41.2%) with 25 errors (2.6%). That is 555 additional requests auto-passed by logprob while remaining below the predeclared 5% observed-error budget. But at the separately frozen 10% target, logprob missed the budget: 12.0% error at 88.3% coverage, versus 7.6% for stated confidence. Post-hoc sanity check: if we deliberately throw away the tiny near-1 differences and accept only clipped logprobs exactly equal to 1.0, that still covers 54.0% of the holdout at 3.9% error. This was examined after seeing the results, so it is diagnostic rather than prospective evidence. We also tried turning both scores into calibrated probabilities; neither clearly won on the holdout.

How the one-token logprob experiment works

Each request gets a deterministic random mapping from the 77 intents to 77 one-character codes that are single tokens in both modern OpenAI tokenizers. Randomizing the mapping per case prevents one intent from always benefiting from an intrinsically easier code token. The response begins with that code, followed by the model's stated confidence.

Raw first-token probability is exp(logprob). The routing result above does not depend on probability calibration; it uses raw-score ordering and frozen raw-score cutoffs. We separately tried Platt scaling to translate both scores into approximate probabilities. Cross-fitted calibration looked promising on the 770 development cases, but on the 2,310 holdout calibrated logprob and calibrated stated confidence had very similar Brier scores (0.111 vs 0.113), so we do not treat calibration as the main result.

The operational question

## So what should we auto-pass?#

A confidence threshold is useful only if it tells us how much review we can skip—and what error rate remains among the cases we skip.

Auto-pass when confidence is at least…

Everything below this score goes to a human reviewer.

95%

50%75%100%

### GPT-5.6 Luna

86.9% auto-passed669/770 cases

10.3%wrong among auto-passed · 95% CI 8.2%–12.8%

### GPT-4.1 Nano

46.0% auto-passed354/770 cases

21.8%wrong among auto-passed · 95% CI 17.8%–26.3%

The point

## Don’t choose 95 because it sounds safe.#

The right threshold is empirical. The same loop works for classification, extraction, RAG answers, matching, OCR, or any workflow where humans already approve or correct AI output.

1 · ReplayUse historical cases.

Run the AI on examples where the final human-approved answer is already known.

2 · MeasurePlot score vs. reality.

For every confidence band and threshold, measure actual correctness—not how certain the model sounds.

3 · DecidePick risk, then coverage.

Choose the threshold that meets your error SLA while removing the most human review. Confirm it on held-out cases.

This benchmark does not give your project its threshold.Calibration depends on the task, prompt, model, score construction, and gold labels. It demonstrates the method—and why an untested “95% confidence” cutoff is not evidence of 95% correctness.

What next?

## Calibrate the prompt before calibrating the threshold.#

The 770-case run shows that confidence is not a fixed property of the model. The way you elicit the score changes which cases rise above a review threshold.

First · promptMake uncertainty legitimate.

Test two or three confidence instructions on historical gold cases. Keep the one that best separates safe cases from risky ones.

Then · thresholdChoose error, then coverage.

Measure the actual error rate above each threshold and pick the amount of human review your SLA can safely remove.

If certifying low riskUse more held-out data.

The full BANKING77 test split has 3,080 cases. Larger samples matter when you need credible estimates around 1–2% residual error.

Method & data

## Simple enough to audit.#

BANKING77 contains fine-grained online-banking support intents. This run uses 770 requests: a balanced sample of 10 from each of all 77 intents. Both models saw the same request and the same list of allowed labels. Correctness is exact label match against the dataset—no LLM judge. Confidence is the model’s own 0–100 estimate of the probability that its chosen label exactly matches the gold label.

The logprob experiment uses a separate paired Chat Completions protocol: Luna emits a one-token class code followed by Top-two stated confidence, letting both signals refer to the same prediction. Probability calibration is evaluated out-of-fold; risk–coverage evaluates ranking.

Current run — GPT-4.1 Nano: 770/770 completed · GPT-5.6 Luna: 770/770 completed. The page automatically picks up additional completed models or cases when rebuilt.

Baseline model results CSVFull prompt-variant results CSVPrompt screening results CSVPrompt calibration summary CSVInput-length raw results CSVInput-length summary CSVLogprob paired results CSVLogprob summary CSVProspective holdout results CSVProspective holdout summary CSVFrozen holdout plan JSONSupport-request sample CSVPage data JSON

Couldn’t load the benchmark data.

Raw token logprob99–99.9% · 178 cases
mean reported certainty 99.6% · actually correct 56.2%

Confidence calibration · BANKING77Numbers are recomputed from the deployed benchmark results.

# Independently reconstructed exercise — 100 bank tickets, only 10 checks

**Research checked 4 Nov 2026, not a slide or a proposed page layout.** This analysis uses the public [AIPL | Ten Checks](https://files.s-anand.net/temp/2026-10-25-aipl-session-2-human-checks.html), original [BANKING77 test labels](https://aclanthology.org/2020.nlp4convai-1.5/), and the instructor's *private* live [Session 2 Google Sheet](https://docs.google.com/spreadsheets/d/1qblt4ZTqhbzJVFVmijGE2oqrRhIH8LGPi-rSOaaKohw/edit?gid=0#gid=0). The live Sheet includes participants' names, attack and defense prompts: **do not re-publish raw rows or participant-attributed results**. These figures may be shown as anonymous aggregates.

## The exact game

- **100** unique customer-message texts drawn from the **BANKING77** classification benchmark, all 100 **exactly matched** to strings in local `~/code/llmevals/confidence-calibration/data/banking77-test.csv`.
- Each card includes an ID, text, AI-predicted intent, AI's claimed confidence (percentage), whether a second AI disagrees, and an *invented* impact if the first classification is wrong.
- A review costs **₹1,000** per ticket. The participant must select **exactly ten** of 100 to check, spending **₹10,000**. Review **always catches and fixes an incorrect label**, an idealized training-game assumption; no actual bank process was operated.
- "Wrong" means the first model's intent label differs from the **BANKING77 annotated intent**, after normalizing spacing/underscores/case. It does **not** measure whether a person in a live banking workflow would agree with that intent. A separate mislabeling test is not given.
- Game's total loss formula: **₹10,000 review cost + sum of fictional impacts for wrong labels among the 90 unchecked tickets**. Had nothing been checked, the sum of mistaken-case penalties would be **₹231,000**.

## Independent verification results

| Reconstructed quantity | Result | Evidence / interpretation |
| --- | ---: | --- |
| Customer tickets matching the original BANKING77 test texts | **100 / 100** | Exact case-insensitive text match to local CSV |
| Gold-label mismatches in the 100 predictions | **17 / 100** | Normalized predicted category vs benchmark category |
| Loss from all 17 mismatches with zero reviews | **₹231,000** | Sum of fictional ticket impacts; *not a business loss* |
| Scored answer rows in live Sheet | **21** | Each contains exactly 10 ticket IDs |
| Distinct submitted 10-ticket sets | **13** | Identical group answers submitted by multiple rows |
| Independently reproduced Sheet scores | **21 / 21** | Exact matches for **Total cost**, **Errors caught**, **Loss avoided** |
| Total costs of the 21 scored submissions | **₹106,000–₹231,000** | Median **₹140,000**. Comparisons aren't independent student trials |
| Incorrect cases caught | **1–6** | Varies by submitted strategy |
| Financial impact caught ("loss avoided") | **₹10,000–₹135,000** | Counterfactual using the game's truth and fictional costs |
| If an impossible oracle knew the truth beforehand and reviewed the highest-impact ten wrong cases | **₹41,000 total cost** | ₹10,000 review + ₹31,000 residual errors; a *hindsight upper bound*, not an available real strategy |

The 21 submitted rows show **different strategies, not 21 independent algorithm evaluations**. A group often shared the same list; the 34 non-header Sheet rows include incomplete and duplicate/related submissions. The ten breakout groups are a different count.

## Four simple policies run against the SAME frozen hundred cards

For each policy below, select ten cards and evaluate with the original gold; sort ties by ticket ID where necessary. These are **post-hoc demonstrations using all 100 card signals**, NOT pre-registered participants' results or reliably optimal deployment rules.

| Hypothetical policy for ten reviews | Mismatches caught | Fictional penalty avoided | Total game cost |
| --- | ---: | ---: | ---: |
| Top ten **highest financial impact** (tie by ID) | 2 | ₹70,000 | **₹171,000** |
| Ten **lowest self-reported confidence** | 7 | ₹106,000 | **₹135,000** |
| **Second-model disagreement**, then impact, then confidence | 4 | ₹110,000 | **₹131,000** |
| Highest **impact × (1 − model-reported confidence)** | 6 | ₹135,000 | **₹106,000** |
| **Oracle**: highest-impact *actually wrong* tickets | 10 | ₹200,000 | **₹41,000** |

**The irony:** multiplying loss by the model's own *uncalibrated* confidence happened to be the best of these four **on this particular set**, even though the follow-up demonstrates that the percentages do not mean what they claim. That result does **not validate** raw confidence as a real decision probability, establish that the formula beats a calibrated score, or prove robustness to future ticket distributions. Present as an inspectable case, not a recipe guaranteed to work.

## The misses worth showing the reader

- **T040** "My transfer is pending." Model: **pending transfer**, **100%** confidence, no disagreement, ₹20,000 impact. BANKING77 gold: `balance_not_updated_after_bank_transfer`. Exactly what the speaker says at **92:36**. But the model's label is **plausible from the text alone**, exposing that *the taxonomy and reference labels may themselves require review*. It was selected by only **3/21** answer rows.
- **T080** "Do I have to pay any fees in order to receive money?" Model: **receiving money**, **96%** confidence, no disagreement, ₹20,000. Gold: `top_up_by_bank_transfer_charge`. **0/21** selections. This is the same "fees versus receiving" near miss described at **91:51**. The exact source text is "receive money," not "receive the money."
- **T092** "How long does it take for a transfer to get to a recipient?" Model: **transfer timing**, **99%** confidence, no disagreement, ₹20,000. Gold: `transfer_not_received_by_recipient`. **0/21** selections. Another plausible near-neighbor category misclassified according to the dataset.
- **T001**: 42% confidence, second AI disagrees, ₹50,000; **19/21** selections. Strong signals draw almost everybody to it, but even the obvious cases must compete for a scarce review slot.
- **T083** "I need a new card since my old one is about to expire." Prediction "card about to expire", **100%**, no disagreement; the gold IS `card_about_to_expire` (correct). At **79:45–80:27**, **Saurabh** and **Chirag** still disagree on the most appropriate operational route ("renewal" vs "expiry"). This is a *semantic disagreement among practitioners*, not a misclassified gold example.

**Six benchmark-label errors got zero selections from all 21 submitted answer rows:** **T006, T039, T045, T049, T080, T092**. Their combined fictional unchecked penalty was **₹60,000**, including two ₹20,000 cases. This is an empirical surprise and a possible visualization motif (missed by everyone), but its denominator is 21 submission rows, only 13 distinct selection sets.

## How to reproduce privately (no publication of Sheet rows)

1. Fetch the public Ten Checks HTML. The inline `const cases = [...]` array has 100 records, each with `id,text,topic,confidence,disagree,impact`.
2. Read `~/code/llmevals/confidence-calibration/data/banking77-test.csv` with columns `text,category`. Join on trimmed, casefolded **customer text**. **All 100 match.**
3. Normalize both `topic` and `category` using lowercase + replace non-alphanumeric runs with underscores. **This includes case normalization for `Refund_not_showing_up`; omitting that step would introduce 3 false mismatches!**
4. Compare normalized predicted vs labeled category. The correct baseline is **17 mismatches costing ₹231,000**, NOT 20 costing ₹234,000.
5. Read Sheet1 `A1:L200` from the second Google Sheet. From each scored row, parse `T001`-style IDs; assess ten against gold; add ₹1,000 per check and impacts only of *unchecked* gold errors. Recompute cost, error count caught and avoided loss; all **21** scored rows match the published score cells **exactly**.
6. For public demonstration, publish only the public 100-case exercise and aggregate performance, not raw Sheet submissions with person names or raw attacks.

## Important validity limits

- **Data from a bank-intent benchmark, not real bank support tickets processed by this class.** The source dataset's 13,083 samples / 77 classes are from [Casanueva et al. (ACL 2020)](https://aclanthology.org/2020.nlp4convai-1.5/); the selected hundred are a fixed course subset of its test split.
- **The rupee costs are invented**, not validated from any bank's customer complaints or penalties. The game treats a ₹50,000 mistake as twenty-five times as bad as a ₹2,000 mistake without modeling customer outcomes, regulatory constraints, reversibility or systemic risk.
- **Every paid review is assumed perfect and instantly effective.** Real humans can also be wrong, slow, inconsistent, susceptible to automation bias, or disagree on taxonomy.
- **No real-world model improvement occurred from the exercise.** Scores tell us which labels the existing benchmark calls wrong; no evidence here that checking these ten would reduce production losses, or that model confidence calibrated to one task carries over to another.
- **Post-hoc policy choice is hindsight.** Comparing four approaches on the exact 100 gold cases after inspection is informative but risks overfitting. To claim a winner generally, preregister a cost/routing rule and test on a fresh disjoint sample, including changes in label policy, confidence distribution and human review effectiveness.
- Don't interpret **two models agreeing** as both being correct. Disagreement is a signal; agreement can be a correlated mistake.

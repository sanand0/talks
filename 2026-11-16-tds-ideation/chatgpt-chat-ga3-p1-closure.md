---
title: "TDS 2026-09 GA4 closure and GA3 bonus"
date: 2026-11-17T00:05:00+08:00
source: "https://chatgpt.com/c/6afa4aa8-48ac-83ec-9a6b-ccddac3f977a"
---

# User

_2026-11-16T00:16:43.313Z_

On [LocalMCP2](/plugins/plugin_asdk_app_6ab0b6c561508191882e58b23665db3e) in ~/code/{exam,tds-network-games}, download/sync the latest answers to questions. GA4 is closed, so compute the final scores for everyone - where you can - and show me the distribution. Also for questions in P1 where the deadline is over. I will review before you finalize.

For Q4 in GA4, I want YOU to evaluate the questions. Go through past chats we've had about how I frame TDS questions and the ROE philosophy, and categorize the responses into "Usable", "Borderline", and "Rejected" and save them in a single Markdown file for my review.

Let me know if you need my inputs for anything else.

# ChatGPT

_2026-11-16T00:16:43.313Z_

## **Scoring progress — 16 November 2026**

The latest exam submissions have been downloaded, and the relevant game data has been synchronized. No marks have been posted to the gradebook.

| ****GA4****    | 759 saved submissions         |
| -------------- | ----------------------------- |
| ****P1****     | 710 saved submissions         |
| ****GA4 Q4**** | 278 idea responses for review |

One new result is already available: ****P1 Q9, Invisible Ink classifier****, can be graded against the private answer key.

- Valid receipts: **323**

- Mean / 10: **6.48**

- Median / 10: **6.87**

Of 324 saved receipts, 323 passed signature validation and one failed. Sixteen valid submissions scored 10/10. These are computed bonus scores, not yet awarded.

## **GA4: current score distribution**

The completed, directly verifiable components are Q1 (face peer reviews) and Q2 (Food Court). Together they contribute up to 11 regular marks.

Chart: Chart chart

- 0: Students 40
- 0–3: Students 262
- 3–6: Students 0
- 6–9: Students 179
- 9–11: Students 278

759 students; mean 5.77/11, median 8.40/11. This is not a final GA4 total because Q3 posters and Q4 idea bonuses are ungraded.

The Q4 review file has been created with all 278 original submissions, my classifications, explanations, and a shortlist:

| Classification | Responses |
| -------------- | --------- |
| Usable         | 69        |
| Borderline     | 144       |
| Rejected       | 65        |

Ten responses are shorter than 10 characters and therefore count as opt-outs under the published rule, ****not**** penalty-eligible attempts.

## **P1: computed component results**

| Question                    | Students scored | Positive | Mean  |
| --------------------------- | --------------- | -------- | ----- |
| Q1 AI Pipe prediction /1    | 710             | 284      | 0.185 |
| Q2 Human Exchange audio /1  | 710             | 570      | 0.803 |
| Q3 Motion drawing /1        | 710             | 492      | 0.693 |
| Q4 Missing Invoice bonus /1 | 310             | 257      | 0.559 |
| Q6 Human Exchange bonus /10 | 633             | 432      | 4.849 |
| Q7 Picture Stories /10      | 710             | 368      | 3.179 |
| Q9 Invisible Ink bonus /10  | 323             | 319      | 6.483 |

The Q4 and Q6 bonuses use the previously approved game-score files. Q7 and Q9 remain provisional because additional P1 receipts may still be submitted. Q8 (face-expression classifier) has not been graded.

For P1’s three completed regular-mark components, Q1–Q3, the mean is ****1.68/3**** and median ****2/3****, across the 710 saved P1 students.

The P1 Q1–Q3 subtotal distribution is 70 students at zero, 171 between 0 and 1, 232 between 1 and 2, and 237 between 2 and 3 marks.

For the two larger-scored components:

| Score /10 | Q7 Picture Stories | Q9 Invisible Ink |
| --------- | ------------------ | ---------------- |
| 0         | 342                | 4                |
| (0, 2]    | 71                 | 22               |
| (2, 4]    | 2                  | 31               |
| (4, 6]    | 55                 | 61               |
| (6, 8]    | 145                | 104              |
| (8, 10]   | 95                 | 101              |

## **Files ready for review**

****GA4 Q4 — all 278 ideas, classified****

`~/code/exam/.private/ga4-q4-roe-ideas-review-2026-11-16.md`

Includes the full student responses, individual assessments, and a shortlist of 22 especially promising ideas.

---

****Scorecards and distributions****

`~/code/exam/.private/ga4-p1-scoring-review-2026-11-16/`

Contains `review-summary.md`, GA4 and P1 per-student TSVs, the 30 Food Court reconciliation cases, and `summary.json`. The P1 TSV covers 783 unique students, including game-only participants.

The Q4 shortlist includes some particularly interesting ideas: predicting which ROE questions will produce the most marks per minute, using classmates' actual chart-reading errors as the evaluation, and detecting faults in a personalized data stream whose future hasn't happened yet.

## **Inputs needed before finalizing**

1. ****GA4 Q3 Time Use Charts:**** Peer preference voting has not yet been built, and the other three poster-quality dimensions need evaluation. Should I use the announced four-part rubric once voting is available, or revise the weights? Also, 37 students participated in submitted posters without saving Q3 receipts.
2. ****Game receipts:**** Food Court has 16 game-only students and 14 saved-score discrepancies, including nine saved zeros with positive game scores. Should verified game completion override missing or inferior saved receipts?
3. ****GA4 Q4:**** Which ideas merit +10? My 69 **Usable** classifications are candidates, not automatic bonus approvals. The published -1/0 policy also needs to be applied after your review.
4. ****P1 deadline:**** The current code says 17 November, whereas an extension to 24 November was previously discussed. Please confirm which governs remaining submissions.

The audio R2 backup also needs Cloudflare API token access if you want that export completed.

****Verification:**** All 278 Q4 reviews and student scorecards reconciled against the saved datasets. The Invisible Ink grader passed its four tests. No gradebook changes were made, and existing source-code modifications were left untouched.

# User

Importantly, the answers from GA4 Q1 can settle scores for Q6-8 from GA3. Download, analyze, and show distributions. (When showing distributions, be granular - pick the right bucket size for me to see enough detail.) Let me know what needs to be done to finalize these.

# ChatGPT

## **GA3 Q6–Q8: peer-review results**

The production export from 16 November 2026 contains ****24,052 comparisons**** collected through GA4 Q1.

| Reviewed category         | Total comparisons | Usable comparisons | Items reviewed |
| ------------------------- | ----------------- | ------------------ | -------------- |
| Q6 — 3D faces             | 8,346             | 7,679              | 708            |
| Q7 — Morph videos         | 7,858             | 7,375              | 645            |
| Q8 — Face-pair difficulty | 7,848             | 7,405              | 998            |
| ****Total****             | ****24,052****    | ****22,459****     | ****2,351****  |

“Usable” excludes **Can't judge / broken media** responses. Ties count as valid comparisons.

There is enough peer-review evidence to calculate meaningful provisional quality scores, but ****not every submission can be finalized automatically****. In particular, 84 3D models and 51 videos received no usable comparisons. They need media/eligibility review rather than an automatic zero.

One important distinction: the Q8 reviews measured how easy a pair of photographs **appears** to morph. The original GA3 question promised grading against classmates' judgments of actual morph videos. These are related but different outcomes; any substitution needs explicit approval.

## **Provisional scores and distributions**

I computed a transparent scoring proposal, preserving existing online marks and adding peer-review marks as follows:

| GA3 question   | Online | Proposed offline calculation                     | Maximum |
| -------------- | ------ | ------------------------------------------------ | ------- |
| Q6 3D Face     | 0.5    | 7.5 × peer win rate                              | 8       |
| Q7 Morph Video | 0.5    | 4 × peer win rate                                | 4.5     |
| Q8 Rank Faces  | 1      | 4 × agreement with peer pair-difficulty ordering | 5       |

A win counts as 1, a tie as 0.5, and a loss as 0. For Q8, all 45 pairwise orderings within a student's ten ranked pairs are evaluated.

****These are proposed scores, not approved grades.****

| ****Coverage****                 | ****Q6**** | ****Q7**** | ****Q8**** |
| -------------------------------- | ---------- | ---------- | ---------- |
| Peer-scored work                 | 624        | 593        | 775        |
| No artifact / ranking            | 283        | 346        | 216        |
| Needs review                     | 84         | 52         | 0          |
| Mean offline mark, reviewed only | 3.74/7.5   | 2.02/4     | 2.64/4     |

All distributions below use the frozen 991-student cohort. Zero includes students who did not submit; pending is kept separate.

### **Q6 — 3D Face (out of 8)**

Chart: Chart chart

- 0: Students 281
- 0–0.5: Students 13
- 0.5–1: Students 25
- 1–1.5: Students 21
- 1.5–2: Students 30
- 2–2.5: Students 23
- 2.5–3: Students 46
- 3–3.5: Students 53
- 3.5–4: Students 75
- 4–4.5: Students 53
- 4.5–5: Students 68
- 5–5.5: Students 40
- 5.5–6: Students 51
- 6–6.5: Students 55
- 6.5–7: Students 51
- 7–7.5: Students 17
- 7.5–8: Students 5
- Pending: Students 84

Half-mark buckets; left endpoint excluded, right included. Mean 2.92/8 and median 3.10/8 across the 907 students with computable scores.

### **Q7 — Morph Video (out of 4.5)**

Chart: Chart chart

- 0: Students 343
- 0–0.25: Students 0
- 0.25–0.5: Students 5
- 0.5–0.75: Students 5
- 0.75–1: Students 8
- 1–1.25: Students 33
- 1.25–1.5: Students 46
- 1.5–1.75: Students 47
- 1.75–2: Students 56
- 2–2.25: Students 37
- 2.25–2.5: Students 52
- 2.5–2.75: Students 43
- 2.75–3: Students 55
- 3–3.25: Students 84
- 3.25–3.5: Students 50
- 3.5–3.75: Students 43
- 3.75–4: Students 26
- 4–4.25: Students 4
- 4.25–4.5: Students 2
- Pending: Students 52

Quarter-mark buckets. Mean 1.58/4.5 and median 1.61/4.5 across 939 students with computable scores.

### **Q8 — Rank Faces (out of 5; alternative proxy)**

Chart: Chart chart

- 0: Students 215
- 0–0.25: Students 0
- 0.25–0.5: Students 0
- 0.5–0.75: Students 0
- 0.75–1: Students 1
- 1–1.25: Students 0
- 1.25–1.5: Students 0
- 1.5–1.75: Students 1
- 1.75–2: Students 1
- 2–2.25: Students 2
- 2.25–2.5: Students 19
- 2.5–2.75: Students 29
- 2.75–3: Students 45
- 3–3.25: Students 78
- 3.25–3.5: Students 104
- 3.5–3.75: Students 126
- 3.75–4: Students 159
- 4–4.25: Students 123
- 4.25–4.5: Students 68
- 4.5–4.75: Students 20
- 4.75–5: Students 0

Quarter-mark buckets. Mean 2.85/5 and median 3.53/5 across all 991, including nonparticipants. All Q8 offline scores remain hypothetical until the policy is approved.

### **Does Q8 measure something real?**

The default ordering was randomly presented. Comparing every student's saved answer with that original order:

- Beat default: **607**

- Tied default: **71**

- Worse: **97**

The mean improvement was ****0.644 marks out of 4****, with a paired-bootstrap 95% interval of 0.597–0.689. That is evidence the ranking exercise contains useful information relative to the initial ordering, although it does not validate the alternative grading criterion against actual video results.

## **What remains before finalization**

1. ****Approve the score conversion.**** Q6 and Q7 currently use a direct peer-win fraction, without opponent-strength normalization. For Q6, the published rules also promised AI evaluation: either run and calibrate the AI component or explicitly approve a peer-only alternative.

2. ****Resolve 136 media cases.**** Q6 has 84 submitted models without sufficient usable comparisons; Q7 has 52 such videos. Also reconcile 33 Q6 and 42 Q7 URLs saved without online credit, six online credits without corresponding saved URLs, and one Q8 online credit without a valid parsed ranking. These are not automatic zeros.

3. ****Decide Q8's grading basis.**** I recommend considering the peer-difficulty proxy because it covers all 775 valid rankings and shows meaningful performance above default. But the departure from the published actual-video criterion must be approved and communicated. No student has peer-rated morph videos for all ten of their ranked pairs, so the originally advertised metric cannot be applied uniformly.

4. ****Settle the cutoff and exceptions.**** Ten votes arrived during the minute after the published GA4 deadline. I excluded them from the main scores. Their effect on individual Q6/Q7 peer scores was small. I also restored one valid pre-deadline GA3 record displaced by a later negative save; four negative-only records remain separately flagged.

5. ****Apply scores only after approval.**** Once the conversion and exceptions are decided, rerun the computation, verify the tails and sampled artifacts, reconcile any GA3 bonus separately, and prepare the official per-student marks.

## **Saved on LocalMCP2**

All files are under:

`~/code/exam/.private/ga3-peer-review-2026-11-16/`

The primary review document is `review.md`. It contains the full distributions, proposed formulas, coverage counts, and finalization checklist.

The supporting files are `per-student-provisional.tsv` (991 students), `per-item-peer-audit.tsv` (2,351 items), `media-needing-review.tsv` (136 cases), `q8-baseline-comparison.tsv` (775 rankings), and `summary.json`.

The computations passed reconciliation checks, and deterministic reruns produced identical per-student and per-item results. ****No scores were applied or published.****

# User

Give me examples with and without Bradley-Terry/percentile and reliability calibration - i.e. pick examples on the edge and ask me the fewest questions required to reliably interpret my preference of approach. That'll help me decide the score conversions from comparisons to marks.

Even though the questions are slightly different from what we evaluated, there's enough learning and we can use the peer-difficulty proxy. I'll communicate that with the TAs.

Yes, ignore all the 136 media cases without usable comparisons. They have some error or the other. They get zero.

Allow votes after the GA4 deadline, etc.

Recompute. Let me know if you need any inputs. Also give me a single TSV file with email, bonus per question, and the inputs to compute the scores in a way students will understand, and a README.md explaining the TSV - columns and approach - in ASD-STE100.

# ChatGPT

Recomputed GA3 Q6–Q8 using ****all 24,052 GA4 peer-review votes****, including the ten recorded after the deadline.

I applied your decisions to the provisional calculations: Q8 uses the peer-difficulty proxy, and all 136 media submissions without usable comparisons receive zero for their entire question, including any earlier online credit.

No changes have been made to the live gradebook.

## **1. Which scoring method do you prefer?**

These are actual edge cases from the student data. All numbers are ****offline bonus marks****, excluding the online marks already awarded.

| Case (TSV row) | Evidence                     | Direct | Reliability | Bradley–Terry | Percentile |
| -------------- | ---------------------------- | ------ | ----------- | ------------- | ---------- |
| Q6 · 494       | Won 7 of 7                   | 7.50   | 5.50        | 5.36          | 7.49       |
| Q6 · 569       | Lost 7 of 7                  | 0.00   | 2.00        | 2.18          | 0.07       |
| Q6 · 636       | 13 win points / 26           | 3.75   | 3.75        | 2.91          | 3.65       |
| Q6 · 548       | 13 win points / 26           | 3.75   | 3.75        | 4.23          | 3.65       |
| Q7 · 740       | Lost 4 of 4                  | 0.00   | 1.33        | 1.38          | 0.01       |
| Q7 · 526       | Lost 27 of 27                | 0.00   | 0.46        | 0.44          | 0.01       |
| Q8 · 697       | 36 correct, 1 tied, 8 wrong  | 3.24   | 2.61        | 2.58          | 3.50       |
| Q8 · 9         | 21 correct, 1 tied, 23 wrong | 1.91   | 2.13        | 2.13          | 0.36       |

Four interpretations:

- ****Direct:**** Award marks in proportion to peer wins. Easy to explain and reproduce.
- ****Reliability:**** Add eight hypothetical neutral reviews to Q6/Q7. For Q8, give partial credit when peer difficulty ratings are close. This reduces extreme scores, but can award marks to work that lost every comparison.
- ****Bradley–Terry (BT):**** Adjust for opponent strength, with regularization. Notice Q6 rows 636 and 548: identical raw results, but BT awards ****2.91 versus 4.23****.
- ****Percentile:**** Reward relative rank in the cohort rather than absolute peer approval. This substantially changes Q8: the mean bonus among ranked submissions falls from ****2.64 to 2.00****.

A useful finding: BT and reliability adjustments differ from direct marks by more than 0.5 marks for about one-third of reviewed Q6 models, but much less often for Q7 videos.

## **2. Updated distributions**

Direct method, all 995 saved GA3 records. These charts exclude exact zeros for readability; the zero counts appear below.

| Question              | Peer-scored | Zero total | Mean bonus across all 995 |
| --------------------- | ----------- | ---------- | ------------------------- |
| Q6 — out of 8 total   | 624         | 372        | 2.35 / 7.5                |
| Q7 — out of 4.5 total | 593         | 402        | 1.20 / 4                  |
| Q8 — out of 5 total   | 775         | 220        | 2.06 / 4                  |

### **Q6 — total question marks, 0.5-mark buckets**

Chart: Chart chart

- 0–0.5: Students 10
- 0.5–1: Students 25
- 1–1.5: Students 21
- 1.5–2: Students 30
- 2–2.5: Students 23
- 2.5–3: Students 46
- 3–3.5: Students 53
- 3.5–4: Students 75
- 4–4.5: Students 53
- 4.5–5: Students 68
- 5–5.5: Students 40
- 5.5–6: Students 51
- 6–6.5: Students 55
- 6.5–7: Students 51
- 7–7.5: Students 17
- 7.5–8: Students 5

### **Q7 — total question marks, 0.25-mark buckets**

Chart: Chart chart

- 0–0.25: Students 0
- 0.25–0.5: Students 2
- 0.5–0.75: Students 5
- 0.75–1: Students 8
- 1–1.25: Students 33
- 1.25–1.5: Students 46
- 1.5–1.75: Students 47
- 1.75–2: Students 56
- 2–2.25: Students 37
- 2.25–2.5: Students 52
- 2.5–2.75: Students 43
- 2.75–3: Students 55
- 3–3.25: Students 84
- 3.25–3.5: Students 50
- 3.5–3.75: Students 43
- 3.75–4: Students 26
- 4–4.25: Students 4
- 4.25–4.5: Students 2

### **Q8 — total question marks, 0.25-mark buckets**

Chart: Chart chart

- 1.5–1.75: Students 1
- 1.75–2: Students 1
- 2–2.25: Students 2
- 2.25–2.5: Students 19
- 2.5–2.75: Students 29
- 2.75–3: Students 45
- 3–3.25: Students 78
- 3.25–3.5: Students 103
- 3.5–3.75: Students 128
- 3.75–4: Students 160
- 4–4.25: Students 121
- 4.25–4.5: Students 69
- 4.5–4.75: Students 19

The complete frequency tables, including empty buckets and zeros, are also in the README.

## **3. Files saved on LocalMCP2**

**`ga3-q6-q8-bonuses.tsv`**

995 students × 53 columns. Email, original online marks, votes, wins, ties, losses, Q8 pair data, bonuses under all four methods, and calculated totals.

**`README.md`**

ASD-STE100-style instructions. Explains all columns, formulas, real examples, exceptions, and fine-grained distributions.

Both files are in:

`~/code/exam/.private/ga3-q6-q8-finalization-2026-11-16/`

The folder also contains `score.py` to reproduce the calculations and `audit.json` for checks.

I independently recomputed all 991 frozen-cohort records from the original votes, checked all 775 Q8 rankings with exact arithmetic, and confirmed that repeated runs generate an identical TSV.

## **4. Only two decisions needed**

****Question 1 — How should Q6 and Q7 convert peer comparisons into bonus marks?****

****Question 2 — How should Q8 reward agreement with peer difficulty judgments?****

Action: Apply these scoring choices

I would start with ****A for Q6/Q7 and B for Q8****. The first is easy to audit against actual wins. The second avoids treating a tiny difference between two noisy peer-difficulty estimates as a certain ordering, though its 20-percentage-point margin is a judgment call.

These selections are the remaining inputs needed to settle the scoring method.

# User

For all questions, let's go with scaled Bradley-Terry, i.e. the lowest BT score gets 0, the highest gets full.

# ChatGPT

****Min–max-scaled Bradley–Terry is now the selected method for all three questions.****

For each question, the lowest eligible BT result receives zero bonus marks and the highest receives the full bonus. All other scores are scaled linearly:

$$
\text{Bonus}=\text{Maximum bonus}\times\frac{\text{BT}-\text{Lowest BT}}{\text{Highest BT}-\text{Lowest BT}}
$$

The computed anchors are:

| Question          | Lowest BT | Highest BT | Bonus range |
| ----------------- | --------- | ---------- | ----------- |
| Q6 — 3D face      | 0.097551  | 0.853612   | 0–7.5       |
| Q7 — Morph video  | 0.110049  | 0.827136   | 0–4         |
| Q8 — Face ranking | 0.622222  | 3.822222   | 0–4         |

For Q8, the BT value is the student's ranking-agreement score calculated using Bradley–Terry estimates of the ten face pairs. Scaling is across the ****775 valid student rankings****, not across individual face pairs.

Existing online marks remain separate. Thus a student with the lowest eligible BT result gets zero **bonus**, but retains any valid online marks.

## **Recomputed results**

| Question | Eligible submissions | Mean scaled BT bonus, eligible only | Students with zero total |
| -------- | -------------------- | ----------------------------------- | ------------------------ |
| Q6       | 624                  | 3.99 / 7.5                          | 371                      |
| Q7       | 593                  | 2.18 / 4                            | 402                      |
| Q8       | 775                  | 2.54 / 4                            | 220                      |

An example of why the selected method matters: two Q6 submissions each earned 13 win points across 26 comparisons. Their raw scores were identical, but their ****scaled BT bonuses are 2.875 and 4.624**** because they faced opponents of different strengths.

### **Updated files on LocalMCP2**

**`ga3-q6-q8-bonuses.tsv`**

995 students, 63 columns. The `q6_bonus`, `q7_bonus`, and `q8_bonus` columns now contain the selected scaled BT marks. Includes the underlying evidence and alternative scores for audit.

**`README.md`**

Updated in ASD-STE100 style, with the exact formulas, scaling anchors, worked examples, column definitions, and granular distributions.

Both are located at:

`~/code/exam/.private/ga3-q6-q8-finalization-2026-11-16/`

****Verification passed:**** Independently checked all 995 records, all 775 Q8 ranking calculations, the min/max bonus endpoints, and the 136 zeroed media cases. Repeated computation produced identical output.

****No further input is needed to compute these scores.**** They are ready for TA review and gradebook application; the live gradebook remains unchanged.

# User

Upload the relevant files to https://drive.google.com/drive/u/2/folders/1baNdAGonnz8yrUj4NUKZHHf8knJIJjIN in a format similar to the existing ones and email the TDS team letting them know what they need to do and how these were calculated. ASD-STE100, simple enough that TAs can explain intuitively to students, with examples. See my sent emails on* [LocalMCP2](/plugins/plugin_asdk_app_6ab0b6c561508191882e58b23665db3e)
gws -* [root.node@gmail.com](mailto:root.node@gmail.com)
for emails to the TDS team to get the recipient list and style of emails.

# ChatGPT

## **Files uploaded**

Uploaded to the requested GA3 Google Drive folder (link: target not exposed):

2026-09-ga3-q6-q8-peer-review-bonus-marks.7z (link: target not exposed)

The archive matches the existing `.7z` convention and contains `scores.tsv` (995 students, 63 columns), `README.md` (ASD-STE100 explanation and examples), and `audit.json` (scaling anchors and score distributions).

I verified the uploaded file's checksum against the local archive.

## **Email sent**

Sent from ****root.node@gmail.com**** to the 11 TDS team addresses used in your November 13 email. Verified in Gmail Sent.

****Subject:**** GA3 Q6-Q8: peer-review marks ready to apply

The email asks the TAs to:

1. Match students by email and ****replace**** Q6–Q8 marks using `q6_total`, `q7_total`, and `q8_total`, without adding online credit twice.
2. Check example records before publishing and assign zero to all 136 unreviewable media cases.
3. Leave other GA3 marks unchanged.
4. Explain Bradley–Terry in simple terms, including why two submissions with identical win rates can earn different marks.

It also explains the Q8 peer-difficulty proxy and the difference between the original Q6 criteria and the peer-only evaluation.

****Status:**** Files uploaded, email sent and verified. The TDS team has been asked to check and apply the marks. The live gradebook has not been changed.

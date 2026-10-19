# AIPL Session 1: audience survey (18 Oct 2026)

Aggregated, anonymized view of ~/code/liveform-data/aipl2026/responses.tsv against its form.yaml. **Do not commit raw TSV, emails, names, IPs, tokens, user agents or row-level join keys.**

## Counting method

The 248 TSV records are *submissions*, not 248 people. There are **35 distinct verified email accounts** across all questions. Some respondents submitted a question more than once; for every (email, question ID), retain the row with the **latest timestamp** (the TSV is chronological in the snapshot). Different question denominators are normal because the form changed live, participants joined late and some questions were left blank. All 35 accounts are verified in this export. Results below describe *respondents*, not attendance or learning. The present data does not measure before/after learning or listening by non-respondents.

## Q1: How far have you gone with AI? (n=33)

| Maximum use in past 30 days | People |
| --- | ---: |
| Used AI's work, checked everything | 18 (54.5%) |
| Used AI's work, checked only some | 9 (27.3%) |
| Asked AI for ideas or answers | 4 (12.1%) |
| Let AI do something without checking | 2 (6.1%) |
| Haven't used AI | 0 |

This is a self-report of maximum *behavior*, not an overall preference or a claim that participants always review at that level.

## Q3: expense claims — positive vs negative framing (n=31)

Both versions described exactly 95 correct / 5 incorrect decisions out of 100. The assignment uses a stable email segment; we cannot independently establish perfect random balance from this export.

| Delegated authority | “95 right” (n=15) | “5 wrong” (n=16) |
| --- | ---: | ---: |
| Advice only | 2 | 5 |
| Decide but ask before paying | 13 | 8 |
| Pay automatically, with spot checks | 0 | 3 |
| Pay automatically, no checks | 0 | 0 |

**The more negative frame did not reduce autonomy in this small sample.** Three of 16 negative-frame respondents were willing to pay with spot checks, versus none of the 15 positive-frame respondents. Unbalanced samples, incomplete responses and unknown covariates make causal or statistically strong claims unwarranted. No one granted fully unchecked payment.

## Q4: You can check only 10 of 100 decisions. Which ten? (n=33)

| Review policy | People |
| --- | ---: |
| The 10 where mistakes cost the most | 21 (63.6%) |
| Wouldn't use AI without checking more | 9 (27.3%) |
| The 10 where another AI disagrees | 1 (3.0%) |
| Any 10 randomly | 1 (3.0%) |
| The 10 AI is least sure about | 1 (3.0%) |

One possible teaching contrast: model disagreement can locate unusual cases, while business impact can prioritize the *costliest* cases. Neither criterion alone guarantees minimal harm.

## Open text: why they held back and what they want

- Q2 (n=29 latest unique): examples include ABAP syntax, Workday integration, legacy systems, Cypress→Playwright conversion, deep file research citing nonexistent files, diagrams, meeting scheduling, travel booking and finishing mixed text/image outputs. **10 of 29** responded with a case-insensitive variant of "Nothing"/"None" (after trimming whitespace). So some people had no avoided task to report; others described concrete blockers. This does not establish that these respondents had actually tried every possible task.
- Q5 (n=28 latest unique): recurring concerns are hallucinations, not knowing how to verify, confidential data, context quality, missing connectors and uncertainty about what AI can do.
- Q6 task_choice (n=19 latest unique): ideas include meeting assistants, risk/regulatory monitoring, resume screening and interviews, medical triage, KPI monitoring, summarization and follow-ups. **These are proposed uses, not validated deployments.**
- Reliability answer fields: 4 distinct accounts answered the first (later hidden) field and 13 the replacement field. Most propose stronger context, verified sources, deterministic checks, human review, periodic monitoring and stage-wise autonomy. These represent **16 unique accounts combined** (one submitted both variants); do not sum as 17 distinct people; the form was edited during the event.

## Audience-engagement caution

The Zoom chat and transcript document a long wait for Q5 at about 56–73 minutes and Anand's concern about the session format. In the TSV, the **28 final Q5 responses** arrived between **04:28:11 and 06:09:00 UTC** (some after live discussion). The speaker mentioned about 25 during the session; do not claim all 28 were already present during that wait. **That is participation data, not a learning measure.** Q5 was more cognitively demanding than Q1, appeared later, and some students were potentially watching passively. A useful follow-up would test learning with a matched short scenario before/after and ask what changed in real-world delegation one week later.

## Reproduce privately

Read the TSV with tabs as delimiter. Sort by timestamp, retain last row per (email, question), count latest answers per ID. Re-analysis is needed if the live data file changes. These figures are as of the snapshot containing 248 rows (last record 2026-10-18T06:11:49Z).

## Exploratory contrasts (not causal conclusions)

- Among participants who answered **both** Q1 and Q4, 13 of 17 who said they checked all AI work chose highest-cost cases for limited review; 7 of 14 other AI users did. This is a descriptive post-hoc subgroup comparison on only 31 overlapping accounts. It was not a planned hypothesis test and is unsuitable as dramatic statistical proof.
- The Q3 positive/negative arms share **no email respondents**. They contain **15 and 16** latest respondents, respectively. The form assigns via a stable segmentation key; the precise assignment mechanism and any dependence on account traits need inspection before claiming statistical randomization.
- Survey samples are non-random attendees/respondents. The absence of a repeated learning question means participation and learning cannot be compared, and no workshop-format effect can be inferred.

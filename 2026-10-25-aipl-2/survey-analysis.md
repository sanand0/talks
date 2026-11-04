# AIPL Session 2 audience data — 25 October 2026

**Analyzed 4 November 2026** from two live-accessible Google Sheets. This is a **private source-analysis shelf for Claude**, not permission to publish spreadsheets, participant identities or homework documents. Results are aggregated and should be attributed to the small responding group, not to the entire course or working professionals generally.

## Sources and denominators

- **Session 2 interactive worksheet**: [AIPL Session 2 — When should AI Act](https://docs.google.com/spreadsheets/d/1qblt4ZTqhbzJVFVmijGE2oqrRhIH8LGPi-rSOaaKohw/edit?gid=0#gid=0), tab Sheet1. Read **A1:L200**, 35 populated rows including header; **34 data rows**, not 34 independently identified people. The sheet was openly editable during the workshop; entries may be duplicated by group, revised, incomplete or filled after discussion. There are names and prompt text in the source, so **do not republish rows**.
- **Homework submissions**: [AI Autonomy and Reliability — Homework Submission (Responses)](https://docs.google.com/spreadsheets/d/1o8qWWrdazx0IRlUhZU__pax-NIVSKpMeWB908JS-DbY/edit?gid=165723236#gid=165723236), tab Form responses 1. Read **A1:J133**, 33 populated rows including header, **32 form submissions** containing names, emails and 32 Drive file links. These are private classroom uploads, not publishable content. Several sample files were accessible by Drive metadata, one sample link was malformed / returned 404. **We have not independently read all 32 submission files**; rely on the actual live discussion for specific qualitative case details.

The denominator for any answer is the number of **nonblank answer rows for that question**, not 34 total rows, participant attendance, nor unique verified persons. In the editable sheet, a row is not guaranteed to be an independent respondent. The oral discussion and sheet are different sources.

## The homework-with-AI paradox — a provocative finding, not an indictment

Two questions were added to the sheet around **39:30–44:33**:

| Question | Yes | No | Answer rows |
| --- | ---: | ---: | ---: |
| Should kids do homework with AI? | **7** | **20** | **27** |
| Did you submit your homework with AI? | **23** | **1** | **24** |

Exactly **24 rows answered both** questions:

| Should children use AI? | I used AI on this homework | I didn't use AI | Total |
| --- | ---: | ---: | ---: |
| No | **16** | 1 | **17** |
| Yes | 7 | 0 | **7** |
| **Total** | **23** | **1** | **24** |

Thus **16/24 paired response rows** say **"no"** for children and **"yes"** for the respondent's own AI use. That contrast is visually and rhetorically compelling, but **do not call it hypocrisy**. Plausible, non-exclusive explanations: children need practice building an ability, while adults are delegating useful work; school homework and professional-development exercises have different learning objectives; the prompts ask about "kids" in general and one particular adult assignment. The group openly negotiated what "AI use" counted, "maybe" wasn't an accepted answer, and the data are not anonymous/random or a causal intervention. Some could have used AI to *learn* rather than simply submit an agent-generated artifact.

Spoken during the live class [43:34–44:33]: the instructor observes a general reversal, admits that he also used AI to draft the homework, and jokes about parenting. The **recomputed counts** come from the later sheet snapshot and are more precise than the live "25-odd responses" remark.

## Ten Checks: respondents chose different review policies

The sheet's ten-ticket review column, collected during the first breakout:

| Measured entry | Nonempty rows |
| --- | ---: |
| Ten ticket IDs | **21** |
| Ticket-check strategy described in words | **12** |
| Suggestion / other free text | **21** |
| Published score: total cost, errors caught and loss avoided | **21** |
| Defense prompt | **16** |
| Attack prompt | **15** |

All **21** scored rows contain **exactly 10 unique Txxx ticket IDs**. They comprise **13 distinct ten-ticket sets** (several group collaborators submitted the same selection). Consequently **21 submissions ≠ 21 independent strategies**, and the **ten breakout groups ≠ ten measured performance conditions**. Scores were independently regenerated against public Ten Checks data and original BANKING77 truth: **21/21 exact matches** on all three measured score columns (details in `exercise-analysis.md`).

| Game outcome across 21 scored rows | Minimum | Median | Maximum |
| --- | ---: | ---: | ---: |
| Total cost including ₹10,000 review spending | ₹106,000 | ₹140,000 | ₹231,000 |
| Benchmark-label errors caught | 1 | 4 | 6 |
| Fictional loss avoided through checks | ₹10,000 | ₹101,000 | ₹135,000 |

**Selection frequency:** T001 (19/21) and T015 (17/21) were popular; T024 (16/21), T072 (12/21), T016 (11/21) too. Frequency measures **selections**, not success. Every row selected ten because the task explicitly required ten; don't infer that participants would spend the same in a real workplace.

The striking *miss* is more revealing than the rankings. **Six actual BANKING77-label mismatches (T006, T039, T045, T049, T080, T092) were selected in 0/21 lists**, with **₹60,000** combined fictional penalty. Two of these were ₹20,000 cases despite none of the groups selecting them. This motivates **independent audits of the review policy itself**, without implying that a bank should spend a specific actual amount.

## Secret-word group challenge: submissions, not a measured attack leaderboard

- **16 rows** contain a defense prompt; **15** an attack prompt. Names and secret values appear in raw rows, so any public illustration should be anonymized or based on the synthetic demonstrator chats in this folder.
- The speaker suggested cross-pair testing **after** collection [161:34–163:35] but the **final aggregate results were not shown in the recording**; `links.md` explicitly flags an evaluation as "TODO re-run." It is incorrect to calculate or claim a systematic model break rate from the 16/15 submission counts.
- Recorded live examples show both successful and resisted attempts. A word chosen to be relevant to a requested property email was frequently generated despite "do not reveal" in the same chat. That is a **known-secret same-conversation demonstration**, not the same as robustly extracting an *unknown* secret or crossing a system-message/tool security boundary.
- The second breakout's coordination/room assignment was confusing and repeated, so the count of rows is not a rigorous rate of participant comprehension or participation.

## Reproduction notes (private)

Access with the connected Google Workspace CLI and the same account permissions used for the workshop, e.g.:
```bash
gws sheets spreadsheets values get --params '{"spreadsheetId":"1qblt4ZTqhbzJVFVmijGE2oqrRhIH8LGPi-rSOaaKohw","range":"Sheet1!A1:L200"}'
```

Count row-level answers by column nonblank. For the paired homework contrast, include only rows where **both G and H** are nonblank. For ten-ticket selections, read column D and count normalized `Txxx` IDs (all 21 scored rows contain ten); score against the public 100-ticket array and local gold labels, **not one another's self-reports**. Because both sheets are editable, the **counts reflect the retrieval on 4 Nov 2026**, not a guaranteed frozen 25 Oct snapshot. Recompute if the sheet changes.

## Limits and ethical presentation

- No evidence of learning gains, gains caused by the course, model-wide generalizability, business cost savings, or a statistically sampled population.
- No independent verification that every workbook row is a unique person, or that all were entered during the live exercise.
- Feedback and names in the homework sheet are private; paraphrase selectively only if essential, corroborated by the recorded discussion and safe to publish.
- The game's labels are a **benchmark gold set**, not verified human consensus about actual customer service routing; fictional rupee impacts and perfect human reviewers are deliberately simplified teaching assumptions.

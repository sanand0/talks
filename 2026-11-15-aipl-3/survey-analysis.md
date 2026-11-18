# LiveForm Session 3 — survey evidence

Source private ~/code/liveform-data/aipl2026-s3/{form.yaml,responses.tsv}. Read on 18 Nov 2026. **Do not publish the raw response TSV, names, emails, IPs, browser strings, or hidden results links.** The presenter-gated results page is not a public interaction.

94 submission rows, 24 distinct verified email accounts, all rows marked email_verified=true. Retain latest timestamp for each (email, question); 88 unique account-question responses, six additional/revised submissions. Question-level denominators vary. Only the following four questions have any responses. These are small, voluntary self-reports, not all participants, nor independent random samples of professionals.

| Exact question (abridged only where indicated) | Latest n | Results |
|---|---:|---|
| Did you use an agent to help you with this? | 20 | **Yes 7 (35%), No 13 (65%)** |
| What do you think was the best strategy in the food court? | 22 | Free text; no predefined correct answer |
| How would agents have played this game - if the aim is to increase the player (40%) and food court (60%) profits? | 23 | **Better 19 (82.6%), Worse 4 (17.4%)** |
| Would students have scored better or worse than you? | 23 | **Better 14 (60.9%), Worse 9 (39.1%)** |

The lesson is a tension between beliefs about agents and reported use, not a proven advantage for AI-assisted players. We do not have measured agent usage for the earlier TDS rooms; the lecturer estimates extensive student usage (90%+ and initially says 100%), but that is **not** a verified rate in the game data. Do not infer individual behavior from the marginal totals. The private join by email confirms **20 matched respondents** (everyone who answered the use question also answered both prediction questions). Among the 13 non-users, **10 predicted agents would do better** (3 worse); among the 7 users, **all 7 predicted agents would do better**. In the matched student-prediction question, 9/13 non-users and 3/7 users predicted students would do better. Thus 10/20 matched respondents both believed agents would do better and reported not using one. This is a descriptive contrast, not proof that trying AI would have improved their score.

The spoken live count around 82:22 was ~20 maximum and ~19 for most. The final saved TSV has maximum 23 answers on single-choice items and 22 strategy answers; it includes responses that may have arrived after the announcement. It still doesn't reach 25 on any question. No proof that the planned threshold would yield statistical significance; different A/B splits and effect sizes require different power calculations. The instructor chose to end the structured second half earlier and instead discussed the game results and audience questions.

## What the 22 strategy answers say (qualitative reading)

Recurring differences include: discount more in low-footfall periods, or alternatively discount during festive/peak demand; keep 10% as a compromise; avoid 20% constantly; adjust in response to competitors; coordinate which stall discounts when. Some respondents focus on market psychology/cuisines, some on numerical trial and feedback. These are *self-reported strategic interpretations*, not coded behavioral outcomes. The actual game logs establish what got Saved, but cannot tell whether decisions were calculated manually or assisted by an LLM, or whether a plan was communicated in a private call. A participant explicitly described testing a busy month's 20%→0% change and seeing profit improve. That is a safer narrative than counting ambiguous free-text themes as objective frequencies. Paraphrase rather than publish identifiable free text.

## Unrun plan

The YAML title is "AIPL 2026 — Every Agent Did Its Job". It contains **20 questions**: four answered Food Court questions plus 16 with zero responses. The planned opener system_works_pre is text and closer system_works_post single-choice, so even if run it would not strictly be a matched pre/post scale without a coding scheme. Remaining planned items on team KPI clashes, accountability, pricing spiral, bottleneck, one/three model loan-review redundancy (A/B), AI/human refund-error response (A/B), promotion evidence, launch-day own/AI advice, repeat review selection, capstone risks and permission removal were never answered. They are valuable possible next experiments, not study findings. No observed A/B effect, no collected before/after measure, no capstone votes.
 
Reproduce: csv.DictReader with delimiter tab; sort by timestamp, dict keyed by email + question to keep last, Counter answers per ID. Compare all IDs in form.yaml against actual response IDs. The raw form includes named allowed-results viewers; don't expose those settings publicly.

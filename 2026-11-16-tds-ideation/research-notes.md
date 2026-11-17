# Research notes, independent checks, and counterarguments — TDS ideation 16 Nov 2026

This is a **source-grounded research shelf for the future Claude talk story**, prepared 17 Nov. It is not a polished article, and some material is deliberately non-public. A speaker's assertion during the call, a recomputed result from local data, an interpretation, and a future proposal should not share a single undifferentiated factual voice.

**Evidence levels:** (A) original video and its WebVTT captions; (B) actual dated code and reproducible local aggregates; (C) user-provided private ChatGPT retrospectives, sometimes with unreproduced underlying exports; (D) public author blog and independent third-party sources; (E) hypotheses. Prefer A–B for what happened and C–D for context. Never publish raw private records, individual marks or exam keys.

## 1. Workshop professionals vs students: quantify the surprise, not a demographic conclusion

**Original meeting:** [00:32–07:41] Anand asks JK to guess whether experienced data-science workshop participants would cooperate, strategize and persuade differently. JK anticipates weaker cooperation but possibly better strategy and persuasion. Anand shares the first AIPL run's data and TDS comparison. The term “working professionals” refers to an audience *described* as such; it was not a randomized population sample.

**Independently rechecked on LocalMCP2, 17 Nov** using the per-person result.csv in the game's synced, private session directories, grouping **unique room_id** and averaging the room's **team** score (rather than erroneously weighting five-person rooms more heavily). Reproduced:

| Session | Players/entrants in result CSV | Distinct rooms | Average room team score /100 |
|---|---:|---:|---:|
| AIPL 15 Nov, first workshop run at 12:00 SGT | **32** | **7** | **88.06** |
| IITM Tue 10 Nov 18:00 IST | 247 | 61 | **92.51** |
| IITM Wed 11 Nov 07:30 IST | 106 | 25 | **95.57** |
| IITM Wed 11 Nov 21:00 IST | 305 | 75 | **94.13** |

This confirms the primary number cited by the speaker from the meeting for the **first** AIPL run. Two subsequent AIPL sessions occurred later that day (12 and 9 participants, respectively, room team means 89.73 and 84.71) and are **not automatically equivalent** to the first session/meeting slide. If analyzing “all workshops,” define a different aggregation and avoid silently mixing repeat entrants.

The contemporaneous ChatGPT research export **./chatgpt-chat-aipl-session.md** reports for **first AIPL session**:
- Roughly **49.4%** of final discount decisions were 20%; IITM three session values 24.7%, 15.2%, 24.5%. This is highly conditional on different opponents/stakes and replay.
- Mean AIPL team score at the first versus last *checkpoint* **91.81 → 85.95**: **5.86-point drop**, 6/7 rooms worsened. This is not the same quantity as the overall room score 88.06, which averages scheduled checkpoints. The spoken recording rounds it to ~92 to ~86.
- **161** workshop chat messages across 7 rooms; IITM **7,032** across 161 rooms. Mean ~23 vs ~43.7 messages per room.
- AIPL averaged **37.1 saved plans/team vs IITM 24.2** — more recorded experiments but fewer chat messages. Therefore “they weren't doing anything” is unsupported. More changes can reflect activity, confusion or bad incentives; no causal diagnosis without interviews.
- Workshop identities weren't isolated: **8 of the 32 participants used IITM student email addresses**, and four had played an earlier IITM round. The sample is mixed/partly repeated. Further unmeasured differences: 4/5-person rooms, course credits, device choice, time pressure, group norms, interface skills and conversational style.

**Game mechanisms verified from original source:** ~/code/tds-network-games/REALTIME-GAMES.md and src/realtime/games/food-court/{model.ts,game.ts}; ~/code/exam/src/q-food-court-discount.js. Four/five restaurants choose 0/10/20% monthly discounts for a simulated year. The score weights **60% joint / 40% individual**. Discounts improve attraction but reduce margins, and a high individual response can undermine group profit. A mathematical model is not the same as the psychology of an actual market.

**Strong counterexample in *chat appended to transcript***: at [09:26] Preethi notes the chat panel required vertical scrolling away from discount editing; at [11:07], negotiation “got better with each iteration”; at [12:46], intuition “Definitely” improved. These are *self-reports*, valuable anecdotes rather than validated learning gains. A UI that obstructs simultaneous conversation can understate actual negotiation ability.

**Be very precise on external status:** This is a **workshop simulation**, not live retail profit. Don't say professional businesspeople cannot negotiate, or that IITM education caused the difference. Lower AIPL scores could reflect social equilibrium, unfamiliar UX, incentives, or sample mix. If the article uses a chart, label all room/session/sample units and no student identities.

## 2. “Worse score with better evidence”: the AI Pipe forecast scoring paradox

**In meeting ~29:07–31:25**, the instructor reports final aggregate AI Pipe spending for **2–8 Nov 2026 UTC** as **$5.31**, with around 620 students making forecasts. They learn by revising predictions, but scores also reward earlier predictions and sustained positions. Some students wrote a reason like “the spend will be $5–10” yet selected **5–10 cents** in the UI. This is a concrete example of **correct logic + incorrect action = incorrect outcome**.

**Later private ledger analysis** in ./chatgpt-chat-student-learning.md reports exact spend **$5.3063** and a **621-student matched cohort** with submitted on-time forecasts: **123** first choice in the correct $5–10 bracket, **262** last on-time choice in the correct bracket; **169** changed from wrong to right and **30** right to wrong. The *spoken* snapshot says **123 initial, 242 final**, not 262: these disagree. They may reflect data cutoff, denominator or ledger version; **do not present 242 and 262 as the same statistic or silently “correct” the speaker.** Future Claude should trace the snapshots/analysis code or explicitly say “at the meeting the instructor reported ...; subsequent detailed analysis found ...” with dates/definitions.

The report also distinguishes **681 forecasters**, **2,793 forecast records**, **77 market traders**, **284 trades**. Never call it “a prediction market representing 681 traders”; most did not actually trade. For exact metrics, independently inspect underlying results. The unpublished original P1 forecast ledger likely lives within ~/code/tds-network-games/.private/prediction/ or exports in ~/code/exam/.private/. This research preparation did not recompute those files. Refer to author article or anonymized aggregate only, not student email IDs in the private archived report.

The scoring measure intentionally reflects at least two constructs: **forecast accuracy + participation/commitment discipline**. That is not a flaw if disclosed and intended, but a final score cannot be described as a pure forecasting-skill score. Some early committed predictions can receive more credit than accurate late updates. A student updated correctly but clicked cents instead of dollars is a strong **verification-of-execution** story.

Novel visual: let a reader type "$5–10" into a rationale and accidentally select "$0.05–0.10"; ask them to test the saved state. Label this a constructed *anonymized reconstruction* based on a real error pattern.

## 3. Originality, audience, and what the rubric rewards

**Author's original public write-up dated Saturday 7 Nov 2026:** https://www.s-anand.net/blog/picture-stories-we-understand-and-like/ (web search checked 17 Nov). Public interactive results: https://files.s-anand.net/pages/tds-2026-09-p1-q7-picture-stories/?tab=patterns (HEAD 200). The assignment: a **wordless picture story**, judged on **uniqueness, clarity of reader interpretation, and preference**. The author reports a **negative correlation between uniqueness and preference** within this cohort; he explicitly says he does **not** know why.

Common cliché stories (thirsty crow/pitcher, child adopts a dog/bird, old man/kite, a robot watering a plant) often were easily understood and well liked. Distinctive stories (unwanted gift, phone notifications from the moon landing, robots replacing humans) could be very unique but not always preferred. A notable high-rated, distinctive exception was a **Bhagavad Gita** story. In the meeting the instructor and JK laugh at familiar/clichéd stories being crowd favorites; JK compares them to mass-market cinema.

Do not treat “cartoons score worse than realism,” “the crowd hates originality,” or “the best story was the Bhagavad Gita because it used AI prompts” as established causal facts. Medium, culture, task templates, cohort references and ratings confound it. Also **understanding and preference do not measure creator intent or originality equally**. Original uniqueness estimate may depend on model-based similarity; review the source methodology before claiming it is objective.

If using student work, **only use already-public anonymized examples** after checking any reuse rights, and favor public result card images. Avoid real people/identity in screenshots and copyrighted pop-culture panels. Exact points in a plot must originate in the published dataset or otherwise be labeled illustrative.

## 4. Bradley–Terry: the judge and the match-up matter

**Original ~09:05–12:37:** Anand explains peer-review score conversion for GA3 face meshes/morphs. A raw win fraction ignores opponent quality. **Two entries with 13 win-points out of 26** can be very differently ranked when one faced stronger comparison partners. JK asks about sample-size consistency and observes Q8 is an easier judgment task (hence more submissions); those aren't equivalent distributions.

**Private approval and later files:** ./chatgpt-chat-ga3-p1-closure.md and ~/code/exam/.private/ga3-q6-q8-finalization-2026-11-16/{README.md,ga3-q6-q8-bonuses.tsv} describe the user selecting **min–max-scaled Bradley–Terry across all three questions** (lowest eligible estimated score gets zero bonus, highest gets full). Raw-score alternatives, reliability shrinkage and rank percentiles were compared; score choices have substantive consequences.

An illustrative *documented* pair of Q6 outcomes each had **13/26** win points but received **2.875 vs 4.624** bonus marks under the selected adjusted scaling because of opponent strengths. Don't imply this means reviewers were objectively accurate or that the same comparisons have unlimited reliability. The **Bradley–Terry model** estimates latent relative strengths from uneven pairwise results; its assumptions include local independence/connected comparison graph and transitivity in a one-dimensional construct. Actual preferences can be noisy and cyclic; item exposure unequal. Calibration/regularization matters.

**Important fairness/validity caveat:** In Q8 the original wording promised judging student predictions against how actual morph videos turned out. The later grading conversation explicitly accepts a **peer-rated pair-difficulty proxy**, which is related but not identical. Q6 peer-only ratings replace/omit an originally discussed AI component. The review contains **24,052** comparison votes, **22,459 usable**, but excludes 136 unreviewable submissions as zeros under the instructor-approved policy. This is a **measurement and fairness decision**, not something that a single 13/26 example settles. Don't disclose student-specific rows or identities.

Private companion export says the team was emailed a verified score archive for review; **live gradebook had not yet been changed** at the time of that assistant report. Don't claim official final marks were published if not verified.

General research anchor: Bradley & Terry (1952) model, https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model for quick background; formal primary tutorial (ACER education assessment) at https://www.acer.org/files/Tutorial-13--Pairwise-comparisons.pdf. Do not recite the PDF's details without inspecting the actual document/page when building. An intuitive, true explanation: **“Winning 13 matches against strong entries can signal more than winning 13 against weak ones.”** A PageRank metaphor is loose, not mathematical equivalence.

## 5. The student-built Invisible Ink solver: verify the achievement, not a legend

Meeting [~38:23–50:58]. P1 Q9 uses time-limited classification of air-drawn, sensor-derived strokes captured in JSONL. The initial instructor assumption was that a solver needed a frontier model at inference time. **Adwitiya** says he used Anthropic's newly released **Claude Fable 5.2**, then built a **standalone HTML artifact with model weights embedded**, requiring **no live LLM for student use**. His model may still have been created with substantial LLM assistance and training. A second solver was posted by **Shrikar / GitHub account sreekarsarma55**: https://github.com/sreekarsarma55/temp-repo (HEAD 200). The transcript chat also contains a Claude artifact link https://claude.ai/artifact/Qs2N2ZyM91NFcA1Nuf34hp shared by Preethi as useful, not necessarily identical to Adwitiya's program; do not conflate authorship. A Google Chat deep-link is private; **do not publish it**.

**Independent external model fact-check:** Anthropic released **Claude Fable 5.2 on 9 Nov 2026**, https://www.anthropic.com/claude-fable-and-mythos-5-2 and https://platform.claude.com/docs/en/release-notes/overview (confirmed via current web search 17 Nov). Thus the model name/date in transcript are plausible, not an ASR hallucination.

**Still unverified:** Held-out classifier accuracy, whether the HTML truly executes all inference offline rather than fetching other assets, how much original vs copied model weights it embeds, true generalization to unseen students, and performance of the second solver. The teacher opens Adwitiya's page, runs a sample and sees uncertain letters, **not** a labeled-test benchmark. Shrikar's repo required setup and was **not executed** during the meeting.

The separate grader analysis from ./chatgpt-chat-ga3-p1-closure.md mentions **323 valid P1 Q9 receipts** (mean ~6.48/10, provisional) but these are **cohort results**, not proof that Adwitiya's standalone solver achieved that score. Any public story must keep those apart.

**The transferable skill:** (a) discover people and solutions, (b) reuse a solution and know what's possible, (c) build reusable tools. Distinguish *what students did* from *who learned which capability*. Simple shared code can move a whole cohort's scores, but not establish each individual mastered classifier training. An alternative assessment may ask for provenance and a later, novel validation task.

## 6. Anonymity, collaboration, accountability and unintended learning

At ~53:49 Adwitiya proposes switching anonymous live-game rooms to real names to see whether peer accountability improves behavior. His explanation is an **unverified hypothesis** that disengagement happened because teammates were anonymous. Anand defends anonymity as a deliberate invitation to build social discovery and community infrastructure, including ways to find one another even without in-game identities. Later he describes a **possible** one-character/one-room-at-a-time ROE, where players face tradeoffs: find a solver, negotiate, abandon a lower-value problem, obtain help or buy time with marks. That is brainstorming, **not a deployed test**.

Meeting chat [55:02–57:03] Preethi says her Time Use Charts team set up a **Google Meet** outside the game to coordinate instructions/data because no rule forbade it. This is genuine evidence of creative workarounds, but before presenting as model collaboration, verify the assignment's exact permitted channels and whether extra-game communication introduces equity/reviewability issues. It is not by itself evidence the poster was good.

The collaborative success hypothesis has **two opposite implications**: being able to find people despite anonymity can be a skill; anonymity also removes accountability, and making identity visible can create privacy, harassment, power and free-rider effects. Don't imply a universal best choice or encourage deanonymization without consent.

## 7. Content generation, indemnity and the role of responsibility

An unnamed client's ad localization anecdote (~14–16:40): the client sees AI can cheaply swap local festival imagery across regions, but would rather negotiate lower agency rates than assume indemnification/cultural and legal responsibility directly. The instructor summarizes as a need for an “external neck” for liability. This is **a reported confidential business anecdote**; avoid identifying client or inferring the industry beyond what is already publicly established. Do not imply the client literally uses all the depicted countries or that a full contract was reviewed.

The speaker's response to chat (“Google will indemnify you if you sign enterprise terms”) needs precise scope. Google Cloud's **October 2026 Generative AI Services Terms** https://cloud.google.com/legal/archive/terms/service-terms/index-20261030 and https://cloud.google.com/terms/generative-ai-indemnified-services describe indemnity for eligible model-generated **unmodified output** under eligible services, with **enumerated exceptions** including known infringement, ignored safeguards, certain trademark uses and custom-data rights; separate offerings, third-party services and customer agents may not be covered. **Not a blanket warranty** covering every tool, every output, every cultural mistake or client's contract. **Indemnification is different from being named as defendant, content rights ownership and insurance coverage**. Future Claude should verify the relevant date-appropriate legal text before writing broad claims.

JK's digressions about Ethan Mollick/Claude-generated videos, Simon Sinek and hiring trends include unclear/mixed attributions; use only if independently tracked to an original citation. No need to reproduce any copyrighted TV clips or songs to make the learning point.

## 8. Negative marks and psychology: the announced math is not the full experience

Meeting [60:26–64:59] and chat: student Preethi asks why GA4 Q4's “invent an ROE question” could incur **−1**, even though much of GA4 offers bonuses. Adwitiya jokes that TDS students treat every mark as a gift from the cosmos; Preethi responds that −1 feels significant. Anand frames the scale as a tiny share of the whole course and an incentive to critique an agent's proposed question rather than blindly submit it. JK explains bonus caps and normalization.

**Two different claims:** The fraction of the final course grade may be tiny, but the psychological **salience of losses** and perceived fairness can be high. Do not say the penalty had “no effect.” The meeting's numeric discussion isn't a legal policy document: cite the public GA4 Q4 rules and current code to state the actual −1/0/+10 rubric, exceptions or opt-outs. A mental model comparing 3/10 with 30/100 is useful but doesn't explain all effects of penalties on motivation. The instructor's own history-teacher anecdote is personal and illustrative.

## 9. Potential story conclusions — and a verification checklist

The author should not call this a randomized learning study. There are **three different “what did a student learn?” answers**:
1. Skill/task completion with AI, visible to graders;
2. Context/tool/community discovery, sometimes visible through shared solver URLs;
3. Transferable individual judgment in a *new* situation, **largely not yet measured**.

The unsettling part of 16 Nov is that **some “better” work scores worse**, some people benefit from copying a shared tool, and changing the rubric changes who wins. This is why the course increasingly teaches **verification and orchestration**, and why it must verify its own grading.

**Before publication:** Check exact timestamp and speaker against WebVTT, especially the [00:00] transcript reset near 50m; compare all numbers to primary source/denominator; verify outside links actually contain the claimed story; check privacy of students and any screenshots; distinguish cohort submission data from model-specific solver performance; avoid extrapolating small AIPL rooms to whole industries; don't suggest future ROE game has launched; check that any image or chart doesn't inadvertently reveal unreleased exam answers or private student faces. Test whether a plausible alternative interpretation flips each narrative beat.


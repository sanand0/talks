---
title: "Survey Analysis - Let AI take your exams"
date: 2026-06-14T14:41:16+05:30
source: "https://chatgpt.com/c/6a2e4c61-4ef0-83ec-87b8-f3ab717ef024"
---

## User

File: let-ai-take-your-exam.7z

Attached are three files: 1. The transcript of my 2-hour AI Workshop [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted at [Paradox](https://www.iitmparadox.org/workshops) for the [BS students at IITM](https://study.iitm.ac.in/ds/) on 12 Jun 2026 (2-4 pm IST) at [DOMS](https://doms.iitm.ac.in/) Room 101. 2. Questions I asked them as part of a survey. 3. Answers they submitted. Think about my intent in including these questions, how I presented them in the transcript, and find the most interesting, powerful insights using the data analysis skill. <DATA-ANALYSIS-SKILL> # Investigative Data Analysis Hunt for stories that make smart readers lean forward and say _"wait, really?"_ - findings that are high-impact, surprising, actionable, and defensible. This is a DETAILED process. Create a PLAN and execute step by step. ## 1. Define What Matters - Who are the audiences and what are their key questions? - What decisions could findings actually inform? What's actionable vs. merely interesting? - What would _contradict conventional wisdom_ or reveal hidden patterns? ## 2. Understand the Data - **Structure**: Dimensions (categorical) vs. measures (numeric), types, granularity, field relationships. - **Quality**: Completeness, missing values, outliers, duplicates, encoding issues. - **Distribution**: Value ranges, (log) normality, skewness, heavy tails, zero-inflation. - **Derived potential**: Computable metrics (features, targets), joins, aggregations, time-series constructions. ## 3. Hunt for Signal Apply diverse **analysis toolkits** ranging from statistical tests to geospatial, network, NLP, time series, cohort, segmentation, survival analysis, etc. to expand the insights pool. Look for stories that _confirm something suspected but never proven_, or _overturn something everyone assumes is true_: - **Extreme/unexpected distributions**: What's at the tails? What shouldn't be there? - **Pattern breaks**: Where does a trend suddenly shift? What changed, and when? - **Surprising correlations**: What moves together that shouldn't? What's independent that should correlate? - **Standout entities**: Who dramatically overperforms or underperforms relative to peers? Who drives trends vs. bucks them? - **Hidden populations**: What patterns disappear in aggregate but emerge in subgroups? (Watch for Simpson's Paradox.) - **Dot connections**: What patterns emerge when combining fields that seem unrelated at first? - **Clusters**: What clusters or communities emerge? Where are the overlaps and outliers? Search internally / externally: - Discover domain-specific rules, context, that have an impact - Search for WHY this happened - Surface confounders - Explore prior research Find leverage points: - Underutilized resources or capabilities - **Phase transitions**: thresholds where behavior shifts nonlinearly - **Tipping points**: what small change would move the aggregate needle? - What actions are _specific and implementable_, not just directionally correct? ## 4. Verify & Stress-Test **Cross-check externally**: Is there outside evidence (benchmarks, research, industry data) that supports, refines, or contradicts the finding? **Test robustness**: Does the finding hold under cross model checks, alternative model specs, thresholds, sub-samples, or time windows? Does a placebo test (shuffled labels, random baseline) reproduce it? If so, it's noise. **Check for errors & bias**: Examine data provenance, definitions, collection methodology. Control for confounders, base rates, uncertainty. What's _missing_? Selection and survivorship bias are silent killers. **Check for logical fallacies**: - **Correlation vs. causation**: is there a plausible mechanism, or just co-movement? - **Goodhart's Law**: is the metric gamed? Does measuring it change behavior? - **Simpson's Paradox**: does segmentation flip the trend? - **Regression to the mean**: are extreme values just natural variation reverting? - **Occam's Razor**: is there a simpler explanation you're overlooking? - **Survivorship/selection bias**: what's missing from the data entirely? - **Second-order effects**: what happens downstream beyond the immediate impact? - **Inversion**: try to _disprove_ the finding. If you can't, it's more credible. **Consider limitations**: What _cannot_ be concluded? What caveats must accompany the finding to avoid misuse? ## 5. Prioritize & Package Select insights that are - **high-impact** (meaningful effect sizes vs. base rates, not incremental), - **actionable** (specific and implementable, not just "invest more in X"), - **surprising** (challenges assumptions, reveals hidden patterns), and - **defensible** (robust under scrutiny, bias-checked). Lead with the most compelling finding → evidence → caveats → what to _do_ with it. **Tone**: Write like a journalist, not a statistician. Say "Sales reps in the Northeast close 2x faster, but only for deals under $10K", not "Closure varies by region." Findings should make a smart reader lean forward. </DATA-ANALYSIS-SKILL>

---

## ChatGPT

Worked for 5m 31s

## Headline

Your workshop was not really about “AI taking exams.” It was a calibration intervention. The survey was designed to make students predict, observe, revise, and then commit to a new study habit. The strongest finding is that students are already AI-heavy users, but their mental model is still immature: they trust AI on questions they themselves get wrong, yet they have not fully internalized the difference between “chatbot answer” and “agent with a verifier.”

I excluded your test account and analyzed 1,175 student response rows from 104 participants. There were no duplicate email-question submissions.

## Plan executed

I mapped each survey question to the workshop intent in the transcript, rebuilt the responses into one row per participant, checked missingness and response timing, segmented by AI usage/tool usage, analyzed prediction calibration, manually coded open-text responses, then stress-tested the claims for selection bias and small-n fragility.

External sanity check: your audience is ahead of the broader higher-ed trend. HEPI/Kortext’s 2025 UK student AI survey found 92% of undergraduates used AI in some form and 88% had used GenAI for assessments; your workshop sample had 94% using AI weekly or daily and a median of 5 AI tools used in the last month. [HEPI](https://www.hepi.ac.uk/reports/student-generative-ai-survey-2025/)

## What you were really testing

The form had five layers.

First, segmentation: “How often do you use AI?” and “Which tools?” This tells you whether you are teaching beginners or power users.

Second, calibration: “Will this pasted question work?” and the five prediction-market questions. This teaches students to bet before trusting.

Third, self-vs-AI comparison: their own answers to the Monty Hall variant and the disease-test base-rate question reveal whether they can recognize when AI may outperform them.

Fourth, adversarial assessment design: the confession box and AI-proof question contest turn students into red-teamers.

Fifth, conversion: surprise, ritual, and panel opt-in measure whether the session produced behavior change, not just applause.

## The most powerful insights

| Finding                                                                              | Evidence                                                                                                                                                                                                                                      | What to do                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| These are not AI novices. They are multi-tool users.                                 | 65/100 daily users; 94/100 weekly-or-daily users. Tools used last month: ChatGPT 96, Gemini 87, Claude 72, Antigravity/Gemini CLI 46, Perplexity 43, GitHub Copilot 43, Codex 34, Claude Code 33. Median: 5 tools.                            | Do not teach “how to use ChatGPT.” Teach model choice, verification, agent workflows, prompt injection, and when not to trust output.                                                                            |
| Students can predict coherently even when they reason incorrectly.                   | Their overall bet averaged 3.68/5. The mean implied by their individual probabilities was 3.67/5. Spearman correlation between the two was 0.57.                                                                                              | Keep prediction markets. Score Brier/calibration, not just right/wrong. This is a teachable metacognitive skill.                                                                                                 |
| Base-rate reasoning is the biggest visible blind spot.                               | Disease question answer is about 1.94%. Only 14/44 answers were near the right range; 23/44 gave 50% or higher. Yet AI-confidence stayed high: mean 77%.                                                                                      | Use “AI as checker” for probability/statistics. Students should first estimate, then ask AI to find the base-rate trap.                                                                                          |
| Wrong students trusted AI just as much as right students.                            | For the disease question, students near the correct answer and students far from it had almost identical AI-confidence. Spearman correlation between their own answer and AI-confidence was only 0.10.                                        | Ask two questions every time: “What is your answer?” and “Why might AI fail here?” Confidence alone is not enough.                                                                                               |
| The Monty Hall trap worked because students pattern-matched the famous problem.      | Correct answer here is “doesn’t matter, 1/2 either way” because the host does not know where the car is. Only 25/70 got that. 38/70 chose the classic but wrong “switch, 2/3.”                                                                | Great exam pattern: familiar shell, changed condition. Ask students to identify the changed assumption before solving.                                                                                           |
| Students still under-appreciate execution + verification.                            | For the “ana in bananananas” question, agent mode confidence was only 13 points higher than chat mode on average; 10/49 were less confident in agent mode than chat mode. But live Codex scored 9/10 on the TDS exam in the transcript.       | Hammer the distinction: chat is answer generation; agent + code + verifier is a loop. In verifiable environments, AI changes category.                                                                           |
| The best AI-proof ideas were not “harder questions.” They were “situated questions.” | I manually coded 61 AI-proof entries. Top buckets: visual/spatial/physical reasoning 14, real-world/local perception 12, subjective/social/emotional judgment 11, symbolic/counting constraints 6, private/unavailable data 4.                | Redesign assessments around fresh artifacts, local observation, browser/API interaction, hidden validators, logs, and process evidence.                                                                          |
| The amnesty box is a threat model.                                                   | 21/36 who answered status said the technique still works. Reports included multi-model checking, photos-to-LLM, Codex/browser agents, NotebookLM on past papers, inspect element, portal-code attacks, hidden prompt text, and screensharing. | Treat exams as security systems. Move answer logic server-side, hide solutions, protect against prompt injection in page text, log automation signals, and design for AI-allowed rather than AI-denied contexts. |
| The session converted interest into a research cohort.                               | 45/53 said “Yes — count me in” for the monthly panel; 7 said maybe; only 1 said no.                                                                                                                                                           | Launch the panel immediately with a 5-question monthly benchmark: self-answer, AI-answer, model/tool used, prediction, verification method.                                                                      |
| The “wrong question” field was weaker than expected.                                 | 31 submitted a wrong question; 20/29 wrong-answer responses were basically “I don’t remember.”                                                                                                                                                | For future workshops, collect screenshots/logs immediately after quizzes or ask students to paste exact failed prompts. Retrospective recall is too noisy.                                                       |

## The single most surprising pattern

Students are not asking for AI-proof math. They are inventing AI-proof reality.

The strongest contest entries depended on things like: count objects in the room, notice a sound, trace a maze visually, reason through a physical mug/cardboard/marble setup, identify mirrored writing, or use fresh private context. This matches the direction of modern AI-assessment redesign: move away from “produce generic text” and toward assessment validity, process evidence, authentic task design, and explicit AI-use levels. The AI Assessment Scale, for example, frames assessment redesign around transparent levels of AI use rather than a simple ban/allow binary. [arXiv](https://arxiv.org/abs/2412.09029)

But there is a caveat: “real-world perception” questions can become unfair or inaccessible. A student in a noisy hostel, low-bandwidth remote setting, or visually impaired context may be disadvantaged. The better version is not “look around your room”; it is “generate a fresh artifact under controlled constraints and explain/verify it.”

## Best assessment ideas from the data

For TDS-style exams, the best direction is not AI-proof but AI-shaped.

A strong question pattern would be: give students a small live system with hidden tests; require them to use AI if they want; collect transcript/logs; grade the final artifact plus their verification strategy. This tests delegation, debugging, verification, and judgment.

Another good pattern: “familiar trap with one changed premise.” Your random-host Monty Hall question did this well. It exposed pattern matching in humans and likely in AI.

A third pattern: “AI may answer, but only if it asks for missing context.” This directly reinforces your workshop line: “If you need context, ask me.” Grade whether the student/agent recognized insufficiency.

A fourth: “red-team the exam.” Let students submit exploit attempts, then grade them for responsible disclosure. Your confession box shows students are already thinking this way.

A fifth: “retrieval plus AI.” Some confessions were actually good study science: past papers, repeated MCQs, timed conditions. That aligns with the testing effect: taking tests can improve later retention, not merely measure it. [PubMed](https://pubmed.ncbi.nlm.nih.gov/16507066/?utm_source=chatgpt.com)

## What I would publish as the main story

“Among 104 IITM BS students in an AI exam workshop, 94% already used AI weekly or daily and the median student had used five AI tools in the last month. But their calibration is still fragile: on a disease-test base-rate question, only about a third landed near the correct 2% answer, while more than half answered 50% or higher. Yet their confidence that AI would solve it stayed high. The workshop’s biggest win was not teaching AI usage; it was reframing AI as something to predict, verify, and learn around.”

## Caveats

This is a self-selected Paradox/IITM BS workshop group, not a representative student sample. Later questions have attrition: 100 answered the initial AI-usage questions, but only 53 answered the closing ritual/panel questions and 26 wrote surprise responses. Open-text coding was manual and approximate; a second coder or model-assisted coding pass may shift a few counts, though not the direction of the findings. The five offline ChatGPT prediction questions cannot be fully scored from the provided data unless you add the actual AI outcomes later.

---

## User

Go deeper. What other insights can you find in line with the DATA-ANALYSIS-SKILL? - IDEATE prioritizing novelty over feasibility. Do not filter. - Choose 3–5 distinct people who'd see this differently. For each, generate short candidate ideas. - Choose 2 UNRELATED domains and for each, extract 3 atomic structural rules, and use them to create a more candidate ideas. - List the 5 most obvious / conventional ideas across all candidates. Ban them, along with near-duplicates. - Merge all remaining ideas removing overlaps. Keep the set maximally diverse across mechanisms, users, and time horizons. - Generate 3-5x as many ideas as you finally need (e.g. 15 ideas converge to 3, 60 ideas converge to 20). - CONVERGE. - Critique each surviving idea: what assumption must hold, why it is non-obvious, and why it may fail. - Score each idea on impact, novelty, and speed. - Pick the best practical idea(s) and the best wildcard idea(s), explaining the non-obvious insight each is built on. Then test each idea / hypotheses rigorously.

---

## ChatGPT

Worked for 5m 50s

I went back to the raw files and treated the previous answer as “round 1.” This pass is stricter: I excluded your test account, used 104 participants / 1,175 student response rows, checked attrition, segmented by tool use, parsed numeric predictions, manually/regex-coded open text, and ran correlation, Fisher exact, Mann–Whitney, Wilcoxon, Friedman, Wilson intervals, and shuffled-baseline tests where applicable.

## 1. Diverge: candidate insight generation

Five lenses produced different hypotheses.

**Exam-security engineer:** the exam is an attack surface; confessions reveal threat classes; portal logic leaks matter more than LLM ability; prompt injection is now a student tactic; “AI-proof” questions should be tested like adversarial benchmarks.

**Learning scientist:** the workshop is a metacognition intervention; students predict without solving; base-rate blindness is the teachable wound; retrieval practice beats passive study; “Socratic sparring” is a conversion metric, not a slogan.

**Student power-user / hacker:** model portfolios matter; agent speed matters more than correctness; sub-agents beat better prompts; browser control turns exams into workflows; the real skill is knowing when to delegate.

**Assessment designer:** “AI-proof” can easily become unfair; fresh context beats hidden trickery; process evidence should be graded; AI-allowed levels should be explicit; the right question is “what human judgment remains?”

**Journalist / product strategist:** the story is not cheating; it is students becoming AI operators. The most publishable angle is: “They use five tools, but still cannot tell when they are wrong.”

Two unrelated domains added more structure.

From **aviation safety**, three atomic rules: near-misses should be reported without punishment; checklists prevent routine errors; black boxes matter more than eyewitness recall. Applied here: keep the amnesty box, create AI-use checklists, and collect agent logs instead of asking students later what happened.

From **epidemiology**, three atomic rules: base rates dominate test interpretation; surveillance must handle attrition bias; repeated testing should track trends, not anecdotes. Applied here: monthly AI panels need representative sampling, calibration curves, and false-positive/false-negative thinking.

I banned the five obvious ideas and near-duplicates: “AI usage is high,” “students like Socratic sparring,” “students struggle with Bayes,” “AI-proof questions need real-world context,” and “run a monthly panel.” Those are true but no longer interesting enough.

## 2. Surviving hypotheses and critique

| Hypothesis                                                                                        | Assumption that must hold                                                             | Why non-obvious                                                                | Why it may fail                                            | Impact | Novelty | Speed |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------- | ------ | ------- | ----- |
| Students are coherent forecasters but not necessarily correct thinkers.                           | Their probability answers are internally consistent.                                  | Coherence feels like competence, but can coexist with wrong reasoning.         | They may have copied the same rough guess pattern.         | 9      | 8       | 8     |
| Students predict AI before attempting the problem themselves.                                     | Missing own-answer rows are meaningful, not form friction.                            | This is the behavioral signature of outsourcing judgment.                      | Attrition or UI timing may explain it.                     | 8      | 8       | 9     |
| Agent capability is underpriced psychologically.                                                  | Students should rate agent mode much higher than chat mode after seeing Codex.        | They saw Codex score 9/10, yet many did not price agent execution differently. | Q3 may have seemed too trivial for coding agent advantage. | 9      | 8       | 8     |
| Power-user status does not equal calibration.                                                     | Tool count should proxy AI sophistication.                                            | Multi-tool users are not automatically better at knowing when AI fails.        | Tool count is noisy; some students may underreport.        | 8      | 7       | 9     |
| The strongest student intuition is “context boundary,” not “reasoning boundary.”                  | Low confidence on no-web TDS weightage means they understand knowledge-access limits. | They may be better at spotting missing context than flawed logic.              | They may simply know IITM facts are obscure.               | 8      | 7       | 9     |
| AI-proof question design is drifting toward “deny AI perception,” not “test human understanding.” | Contest responses reveal authentic student mental models.                             | The assessment risk is that “AI-proof” becomes a CAPTCHA, not education.       | Some answers were rushed or prize-driven.                  | 9      | 8       | 7     |
| The amnesty box is a threat model, not just gossip.                                               | Students disclosed real or plausible techniques.                                      | Techniques cluster into defenses: portal, model, social, study-pattern.        | Self-report and exaggeration bias.                         | 9      | 8       | 8     |
| Panel opt-in is an engagement signal, not a representative sample.                                | Opt-in students differ from non-opt-ins.                                              | 85% opt-in looks great, but likely overselects high-engagement students.       | Small number of non-opt-ins.                               | 8      | 7       | 9     |
| Wrong-question recall is too weak to support serious analysis.                                    | “I don’t remember” responses are not accidental.                                      | The most pedagogically useful field was the least reliable.                    | Better prompting might improve recall.                     | 7      | 6       | 10    |
| Students underpredicted agents in live verified environments.                                     | Codex’s 9/10 score is the benchmark.                                                  | They are bullish on chat, but still conservative on autonomous execution.      | One demo, one exam.                                        | 9      | 7       | 8     |
| “Still works” differs by hack category.                                                           | Confession categories are meaningfully classifiable.                                  | Study hacks and AI-workflow hacks remain live; portal hacks are mixed.         | Small n = 34.                                              | 8      | 7       | 7     |
| Desktop users may be more reflective than mobile users.                                           | Device affects cognitive mode.                                                        | A UI variable may predict reasoning quality.                                   | Evidence is weak; confounded by who brought laptops.       | 6      | 8       | 6     |
| The second AI-proof question is more sophisticated than the first.                                | Q2 reflects reflection after the first attempt.                                       | Optional second entries may reveal refinement.                                 | Only 25 Q2 responses.                                      | 5      | 6       | 6     |

## 3. Tests and results

### Finding 1: Students are coherent forecasters, even when their reasoning is wrong.

For the five prediction-market questions, I compared each student’s overall bet with the sum of their individual probabilities. The match was strong: Spearman ρ = 0.553, p = 0.000031. The observed mean absolute error was 0.61 questions, versus 0.88 under 10,000 shuffled baselines; p ≈ 0.0001.

This is subtle. They were not guessing randomly. They had a stable internal forecast model. But that model did not reliably track reasoning skill. Only 25/70 got the modified Monty Hall question right, and only 15/44 landed near the correct disease-test answer.

Non-obvious insight: prediction markets may teach calibration faster than problem-solving does, because students already have coherent probability intuitions to refine.

### Finding 2: Some students outsourced judgment before attempting the problem.

For the disease-test question, 54 students predicted whether AI would get it right, but only 44 gave their own answer. Ten students skipped their own answer but still predicted AI. Their AI-confidence was still high: mean 71%, median 70%.

That difference was not statistically strong versus those who answered first, but behaviorally it matters. The workflow “I won’t solve it, but I’ll judge AI’s likelihood” is exactly the future skill — and exactly the danger.

Practical implication: every future prediction-market item should force this sequence: own answer → confidence in own answer → AI prediction → AI answer → verification.

### Finding 3: Agent mode is underpriced.

Students rated the “ana in bananananas” question at 71.1% confidence for chat mode and 81.6% for coding-agent mode. The mean uplift was only +12.9 percentage points, and the median uplift was 0. Ten of 49 students were less confident in agent mode than chat mode.

Paired Wilcoxon test: agent confidence > chat confidence, p = 0.043. So they did recognize some difference, but weakly.

This is striking because the transcript shows they had just watched Codex work inside a verifiable exam environment and score 9/10. The mechanism has not landed deeply enough: tool use is not “better ChatGPT”; it is a different class of system.

### Finding 4: Power-user status does not mean calibration.

Using more tools correlated weakly with getting the Monty Hall variant right: Spearman ρ = 0.254, p = 0.009. But it did not correlate with average AI-confidence: ρ = -0.091, p = 0.449. It did not correlate with getting the disease-test answer right: ρ = 0.077, p = 0.436. It did not correlate with understanding the agent-vs-chat gap: ρ = 0.070, p = 0.631.

Coding-tool users were more likely to get Monty Hall right, but the Fisher exact result was borderline, not definitive: p = 0.057.

Non-obvious insight: “AI literacy” is not one thing. Tool breadth, reasoning skill, agent mental model, and calibration are separable axes.

### Finding 5: Students understand knowledge-access limits better than reasoning limits.

Their confidence ranking across the prediction questions was not flat. Among complete cases, mean confidence was lowest for the no-web TDS grading formula question: 53.9%. It was highest for the Python mutable-default question: 90.4%.

The differences across questions were significant: Friedman p = 3.07e-7. Paired tests showed pm5 confidence was much higher than pm4 confidence: mean difference +35.8 points, Wilcoxon p = 6.8e-8.

This is useful. Students seem to know that AI may fail when it lacks current/local/course-specific context. But they were much weaker at spotting altered assumptions and base-rate traps.

Teaching move: distinguish four failure types explicitly — missing context, false familiarity, hidden base rates, and non-verifiable reasoning.

### Finding 6: The AI-proof contest is mostly about denying AI access to reality.

Across 61 AI-proof entries, overlapping coded categories were:

| Category                                | Count |
| --------------------------------------- | ----- |
| Visual / spatial / physics              | 24    |
| Symbolic constraint / counting          | 20    |
| Real-time local perception              | 19    |
| Emotional / subjective / human judgment | 18    |
| Private or unavailable context          | 10    |
| Creative open-ended tasks               | 7     |
| Prompt-injection / security             | 3     |

This confirms the earlier insight, but with more nuance. Students are not merely saying “ask harder questions.” They are saying “ask questions where the answer is grounded outside the model’s text prior.”

But that has a trap. “Look around the room and count chairs” is AI-resistant, but not automatically a good assessment. It tests physical access and compliance as much as learning.

This lines up with the assessment-design direction of using explicit AI-use levels rather than binary bans. The AI Assessment Scale frames assessment as a range from no-AI to full-AI use, with task design depending on the learning outcome. [AJET](https://ajet.org.au/index.php/AJET/article/view/9434?utm_source=chatgpt.com)

### Finding 7: The amnesty box splits into three live threat surfaces.

Among 34 confession responses, overlapping categories were:

| Confession class                                               | Count | Status pattern                               |
| -------------------------------------------------------------- | ----- | -------------------------------------------- |
| Nothing / don’t know                                           | 10    | Mostly not applicable                        |
| Past papers / practice / PYQs / timed repetition               | 9     | 9/9 said still works                         |
| AI copy, model comparison, agents, screenshots, context tricks | 12    | 8 said still works                           |
| Portal/security/prompt-injection/inspect-element/code hacks    | 6     | Mixed: 2 still work, 2 patched, 2 don’t know |
| Social/grading psychology/screenshare                          | 2     | Mixed                                        |

The real story is that “hack” and “study technique” are now interleaved. PYQ mining, NotebookLM, multi-model checking, portal inspection, prompt injection, and browser agents live in the same student mental bucket: methods to improve exam score.

Practical implication: exam design should borrow from security operations. Keep the amnesty box. Convert each technique into a mitigation backlog.

### Finding 8: The panel opt-in is large, but biased toward engagement.

45 of 53 closing respondents opted in. Wilson 95% interval: 73% to 92%. That is excellent.

But opt-in correlates strongly with total response count: Spearman ρ = 0.595, p = 2.66e-11. It does not meaningfully differ by number of AI tools, usage frequency, or average confidence. In other words, your panel is not necessarily “the AI power-user panel.” It is “the people who stayed engaged until the end and kept answering.”

That is not bad. It is valuable. But the monthly trendline should not be marketed as representative of IITM students unless you add sampling controls.

### Finding 9: Wrong-question recall is too weak.

Only 31 students submitted a wrong question. Of the 30 wrong-answer responses, only about 8 contained a usable remembered answer; the rest were essentially “I don’t remember,” blank, or non-specific.

The useful wrong-question examples were excellent — TDS property-based testing, API validation, geospatial assignment, prompt injection, matrices, networking, statistics — but the field is not reliable enough as a retrospective survey question.

Practical implication: collect failed questions immediately, as screenshots or copy-paste logs. Aviation has black boxes because memory after the fact is poor; exam learning needs the same principle.

### Finding 10: Students underpredicted Codex’s live exam score.

67 students predicted the Codex score. Mean prediction: 76.0%. Median: 80%. Actual from the transcript: 9/10. Mean absolute error versus 90% was 17.6 points. Seventeen students predicted 60% or lower; only 22 predicted 90% or higher.

This matters because the exam was verifiable. Codex did not need to “know” everything; it could inspect, try, submit, and correct. That is the distinction students still underprice.

The broader higher-ed context supports the urgency: HEPI’s 2026 student GenAI survey reports AI use as near-universal, with 95% of students using AI in at least one way and 94% using GenAI to help with assessed work. [HEPI](https://www.hepi.ac.uk/reports/student-generative-ai-survey-2026/?utm_source=chatgpt.com)

## 4. Best practical ideas

The best practical idea is an **AI Calibration League**.

Each month, send 8–10 questions. For each: student’s answer, student confidence, AI prediction, tool/model used, AI answer, verification method, final answer. Publish not only model accuracy but student calibration: who knows when AI will fail?

The non-obvious insight: your students already produce coherent forecasts. The skill to build is not “use AI”; it is “price AI.”

Second best practical idea: redesign TDS assessments around an **AI-allowed verifiable environment**.

Give students tasks with hidden validators, logs, and allowed agents. Grade the final artifact, the verification strategy, and the transcript. This targets the actual future skill: delegating to AI while detecting failure. Banning AI is increasingly brittle; frameworks like the AIAS explicitly argue for designing assessments around permitted levels of AI use rather than pretending AI is absent. [AJET](https://ajet.org.au/index.php/AJET/article/view/9434?utm_source=chatgpt.com)

Third best practical idea: create an **Exam Threat Model Register**.

Use the amnesty box every term. Classify techniques into study advantage, AI assistance, model orchestration, portal exploit, social exploit, and prompt injection. For each: “still works?”, “evidence?”, “mitigation?”, “should we allow it instead?”

The non-obvious insight: some “hacks” are actually good learning methods. Retrieval practice has strong evidence: testing does not merely assess memory; it improves later retention. [PubMed](https://pubmed.ncbi.nlm.nih.gov/16507066/?utm_source=chatgpt.com)

## 5. Best wildcard ideas

The best wildcard is an **AI-proof question survival league**.

Students submit questions. Every month, you run the latest models and agents against them. A question’s score is not “does GPT fail today?” but “how many model-months does it survive?” That turns students into benchmark designers.

Second wildcard: an **exam economy**.

Give each student a virtual budget: tokens, model calls, agent minutes, verification attempts. Score not just correctness but return on AI spend. This matches the real world better than closed-book exams: the constraint is not “can you solve it unaided?” but “can you solve it cheaply, safely, and fast?”

Third wildcard: **near-miss reporting for education**.

Borrow from aviation. Students anonymously report: “AI almost fooled me here,” “I almost submitted this wrong answer,” “this hidden instruction worked,” “this model got it right for the wrong reason.” Publish near-misses as weekly learning cases.

## 6. The deeper story

Your workshop created a new assessment category: not AI cheating, not AI tutoring, but AI judgment training.

The students are already using AI. They are not naive. But the data shows four separable skills:

They can use many tools.

They can form coherent predictions.

They often cannot solve classic reasoning traps.

They still underprice agentic, verifiable execution.

That is the opportunity. The next course design should not ask, “Can AI answer this?” It should ask, “Can the student decide what to delegate, what to verify, what to learn, and what to distrust?”

---

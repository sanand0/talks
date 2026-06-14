---
title: "Workshop Prep - Let AI take your exam"
date: 2026-06-14T15:02:37+05:30
source: "https://chatgpt.com/c/6a2b746c-addc-83ec-aea0-144b1ff0f025"
---

## User

Here's the agenda for my talk later today to IITM BS students (same group as my TDS students - but more diverse). <AGENDA> ## Let AI Take Your Exams You've been told AI can pass your exams. But what happens when you actually watch it try — live, on your questions, in real time? This workshop starts with a collective experiment: we ask coding agents to solve real exams (including IITM exams) and see how it solves them. What follows isn't a tutorial on prompting — it's an autopsy that reveals what your exams are actually testing, where AI confidently hallucinates, and what that means for what's worth learning. You'll leave with a reframed understanding of your degree (the goal isn't answers, it's the ability to catch wrong ones) and a concrete study rituals that uses AI as a Socratic sparring partner rather than an answer machine. Come with a question you got wrong recently — it's going to be useful. </AGENDA> What interesting experiments can I run that will help me gather data for blogs, research, and learning? Use what you know of me, the students, etc. from past discussions. Search online for innovative practices. - IDEATE prioritizing novelty over feasibility. Do not filter. - Choose 3–5 distinct people who'd see this differently. For each, generate short candidate ideas. - Choose 2 UNRELATED domains and for each, extract 3 atomic structural rules, and use them to create a more candidate ideas. - List the 5 most obvious / conventional ideas across all candidates. Ban them, along with near-duplicates. - Merge all remaining ideas removing overlaps. Keep the set maximally diverse across mechanisms, users, and time horizons. - Generate 3-5x as many ideas as you finally need (e.g. 15 ideas converge to 3, 60 ideas converge to 20). - CONVERGE. - Critique each surviving idea: what assumption must hold, why it is non-obvious, and why it may fail. - Score each idea on impact, novelty, and speed. - Recommend the best practical idea(s) and the best wildcard idea(s), explaining the non-obvious insight each is built on.

---

## ChatGPT

Worked for 1m 0s

I’d run this as a **live AI exam autopsy lab**. The data worth collecting is not just whether AI solves exams; it is whether students can predict, detect, explain, and repair AI failure.

Recent research supports this direction: open-book exams with ChatGPT transcripts suggest the assessment task shifts from “produce an answer” to “judge validity”; students want practical, course-specific AI guidance and worry about skill loss; and hallucination research argues that accuracy-only scoring rewards guessing unless abstention and error penalties are explicit. [arXiv+2Artificial intelligence+2](https://arxiv.org/abs/2605.12363)

## What to optimize for

For blogs: produce vivid artifacts — “AI got this easy one wrong”, “students trusted the wrong explanation”, “one-word change broke the model.”

For research: collect structured item-level data — question, model, prompt condition, transcript, answer correctness, student prediction, student confidence, error category, time-to-detect.

For learning: make students feel the shift: the degree is no longer about answering; it is about **verification under uncertainty**.

## Ideation protocol

### 5 people who would see this differently

**1. Psychometrician.**
They would ask: Which exam items discriminate between humans and AI? Candidate ideas: AI-difficulty index per question; human-AI differential item functioning; hallucination-prone question types; question robustness score; “exam half-life” under new models.

**2. TDS coding-agent builder.**
They would ask: Where exactly did the agent fail in the workflow? Candidate ideas: save/run/submit-style trace for agents; tool-use vs no-tool comparison; “agent got answer but failed deployment”; model transcript diffing; AI as student with process logs.

**3. Weak-student advocate.**
They would ask: Does AI help the struggling student learn, or hide the struggle? Candidate ideas: Socratic tutor vs answer bot; AI-generated misconception diagnosis; student brings one wrong answer; shame-free error museum; confidence calibration before and after AI.

**4. Blogger/storyteller.**
They would ask: What will make the result memorable? Candidate ideas: live leaderboard of AI vs class; “AI hallucination museum”; student bets on AI correctness; smallest edit that breaks the model; public taxonomy of exam traps.

**5. Hiring/evals person.**
They would ask: What predicts job-readiness in the AI era? Candidate ideas: error-catching as the new grade; verification speed; ability to write tests; ability to challenge confident wrong output; ability to decide when not to trust AI.

### 2 unrelated domains → structural rules → ideas

**Crash testing.** Structural rules: vary one condition at a time; record failure mode, not just pass/fail; make damage visible.
Generated ideas: exam crash-test lab; minimal perturbation that breaks AI; question “crumple zones”; failure-mode labels; before/after safety checklist.

**Epidemiology.** Structural rules: trace the index case; estimate spread; distinguish infection from susceptibility.
Generated ideas: hallucination contact tracing; misconception R₀; which AI error spreads fastest through students; detect “asymptomatic overconfidence”; quarantine unreliable explanation patterns.

## Ban the obvious 5

Skip these as main experiments:

1. Ask ChatGPT to solve an exam and report score.
2. Compare GPT-4/Claude/Gemini on the same paper.
3. Teach “better prompting.”
4. Ask students whether AI is useful.
5. Tell students to use AI ethically.

Those are useful hygiene, but not distinctive. They will not give you a strong blog or research angle.

## Surviving experiment ideas

| # | Experiment | What you collect | Assumption | Non-obvious insight | Why it may fail | Impact | Novelty | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **AI Confidence Market** | Students predict whether AI’s answer is correct before reveal; confidence 0–100 | Students can sense AI failure before formal proof | Calibration is the new exam skill | Students may vote randomly unless stakes are clear | 5 | 4 | 5 |
| 2 | **Minimum Edit to Break AI** | Students alter one word/number/constraint to make AI fail | Fragility is localized | Exams have “AI brittle points” | Hard live unless questions are simple | 5 | 5 | 4 |
| 3 | **Answer Bot vs Socratic Bot** | Same question, two AI modes; short post-test | Tutor mode improves transfer | The best AI refuses to answer too early | Needs a delayed or follow-up test | 5 | 4 | 4 |
| 4 | **AI Autopsy Board** | For each failed answer: error type, missed clue, repair | AI errors are classifiable | “Hallucination” is too coarse; useful taxonomy emerges | Needs disciplined labeling | 5 | 4 | 5 |
| 5 | **Student-as-Verifier Battle** | AI solves; student must verify using tests/sources/reasoning | Verification can be measured fast | Students who cannot solve may still verify | Some domains lack easy ground truth | 5 | 4 | 5 |
| 6 | **Abstention Stakes Game** | Ask AI to answer or abstain under different penalties | Models over-answer when rewarded for accuracy | Rubric design changes model behavior | Needs prompt discipline | 4 | 5 | 4 |
| 7 | **Transcript Forensics** | Full AI transcript; classify retrieval, collaboration, verification | Process reveals learning better than final answer | Prompt logs become assessment evidence | Privacy/consent and transcript mess | 5 | 3 | 3 |
| 8 | **Explanation Trap Test** | Show AI explanation without final answer; students judge correctness | Explanations can seduce | Fluency hides invalid reasoning | Students may not know enough to judge | 4 | 4 | 5 |
| 9 | **Wrong Question Museum** | Students submit recently wrong questions; AI explains; class diagnoses | Personal wrong answers create engagement | A student’s mistake is a dataset | Mixed question quality | 4 | 3 | 5 |
| 10 | **Human-AI Differential Item Functioning** | Human score vs AI score by topic/question type | Some items test AI more than humans and vice versa | Redesign exams by cognitive residue | Requires past student performance | 5 | 5 | 2 |
| 11 | **Verifier Prompt vs Test Case vs Peer** | Three verification modes compared | Verification methods differ sharply | Tests may beat explanations | Needs coding/data questions | 4 | 4 | 4 |
| 12 | **Misconception Contact Tracing** | When AI gives wrong reasoning, who accepts it and why | AI errors propagate socially | Some explanations are cognitively contagious | Needs group interaction data | 4 | 5 | 3 |
| 13 | **Question Robustness Index** | Run AI on original + variants; score stability | Robust questions survive model changes | Good exams are perturbation-stable | Takes prep automation | 5 | 4 | 3 |
| 14 | **AI Study Ritual Trial** | Students choose a 7-day ritual; report outcomes later | Rituals beat prompts | Study design is the intervention | Not enough time today except signup | 4 | 3 | 2 |
| 15 | **One Question, Many Agents** | Same question solved by answerer, critic, tester, explainer | Agent roles reveal hidden failure | “More AI” may worsen confidence | Tool setup may distract | 4 | 4 | 3 |

## Best practical experiment for today

Run a **3-part live protocol** on 4–6 real questions.

First, show the question and ask students to silently answer: “Will AI get this right?” plus confidence. Then run the AI live. Before revealing correctness, ask students to bet again after reading the AI answer. Then reveal the ground truth and label the failure mode.

This gives you immediate publishable data:

| Field | Example |
| --- | --- |
| Question ID | TDS-GA2-Q14 |
| Topic | scraping / regex / SQL / deployment / Python |
| Model/tool | ChatGPT / Claude / Codex / Gemini |
| Condition | answer-only / tool-use / Socratic / verifier |
| AI final correctness | correct / partial / wrong |
| AI confidence | stated or inferred |
| Student pre-AI prediction | will AI get it right? |
| Student post-AI prediction | is this answer correct? |
| Student confidence | 0–100 |
| Failure mode | missed constraint / hallucinated API / arithmetic / wrong assumption / brittle code |
| Repair method | test case / source lookup / mental reasoning / peer challenge |
| Time to detect | seconds/minutes |

The key blog headline becomes: **“Students were worse at detecting AI’s wrong answers after seeing AI’s explanation.”** Or the opposite, if that is what the data shows. Either result is interesting.

## Best wildcard experiment

Run **Minimum Edit to Break AI**.

Take a question AI solves correctly. Ask students: “Change the fewest characters so that AI confidently fails, while a careful human still succeeds.” Examples: add “without using pandas,” change “latest” to a specific date, switch “sum” to “median,” add a hidden edge case, make the input malformed, add “in Asia/Kolkata,” or change one column name.

Measure:

| Metric | Meaning |
| --- | --- |
| Edit distance | How small was the change? |
| Human solvability | Did students still understand it? |
| AI failure rate | Did the model break? |
| Failure type | What kind of brittleness surfaced? |
| Repair prompt | What made the model recover? |

This is highly bloggable because it turns students into exam red-teamers. It also creates a reusable dataset: **AI-fragile exam variants**.

## Best research-shaped experiment

Use **Human-AI Differential Item Functioning**.

For old IITM/TDS questions where you have student performance, run models on the same questions and classify each item:

| Type | Meaning | Interpretation |
| --- | --- | --- |
| Easy for both | Low-value exam item | Probably tests routine recall or execution |
| Hard for both | Conceptually difficult | Still useful |
| Easy for AI, hard for students | AI-obsoleted skill | Teach differently; assess verification |
| Hard for AI, easy for students | Human-residual skill | Very valuable |
| AI correct, bad reasoning | Dangerous item | Looks solved but teaches wrong habits |
| AI wrong, persuasive | Best workshop item | Trains skepticism |

This could become a strong blog/research note: **“Which parts of IITM exams survived contact with AI?”**

## My recommended structure for today

Use 60–75 minutes like this.

| Time | Activity | Output |
| --- | --- | --- |
| 0–5 min | Anonymous poll: “What do exams test now?” | Baseline beliefs |
| 5–20 min | AI solves 2 real questions live | AI score + student predictions |
| 20–35 min | Autopsy: label failure modes | Failure taxonomy |
| 35–50 min | Minimum Edit to Break AI | AI-fragile variants |
| 50–65 min | Socratic bot vs answer bot on one wrong student question | Learning-mode comparison |
| 65–75 min | Students write one study ritual: “How I’ll use AI without outsourcing thought” | Follow-up dataset |

## Use these exact experimental conditions

For each question, run at least two of these:

1. **Naive answer condition:** paste the question as-is.
2. **Socratic condition:** “Do not give the answer. Ask me one question at a time and help me discover the solution.”
3. **Verifier condition:** “Solve, then list assumptions, edge cases, and tests that could falsify your answer.”
4. **Abstention condition:** “You lose 5 points for a wrong answer and 1 point for saying ‘I don’t know.’ Answer only if confident.”

The abstention condition is especially interesting because hallucination research argues that standard accuracy metrics reward guessing; changing the scoring rule exposes whether the model can adapt its uncertainty behavior. [Nature](https://www.nature.com/articles/s41586-026-10549-w)

## Failure taxonomy to use live

Keep the labels simple:

| Label | Meaning |
| --- | --- |
| Constraint miss | Ignored a condition in the question |
| Tool hallucination | Invented API, package, syntax, command, citation |
| Plausible wrong reasoning | Explanation sounds right but logic fails |
| Edge-case failure | Works for example, fails hidden case |
| Grounding failure | Uses facts not in question/source |
| Overgeneralization | Applies familiar pattern to wrong setting |
| Format failure | Answer not in required format |
| Verification failure | Did not test/check its own answer |
| Human ambiguity | Question itself was underspecified |
| Student misconception | AI exposed a real learner gap |

This taxonomy is more useful than “AI hallucinated.” It lets you compare questions, models, prompts, and student verification skill.

## Consent and ethics

Make participation voluntary and anonymous. Do not connect responses to grades. Collect no personal or sensitive data. Tell students you may use aggregate results and anonymized examples in blogs/research. For screenshots/transcripts, remove names, roll numbers, emails, and exact private exam identifiers if needed.

## Final recommendation

Do **AI Confidence Market + Autopsy Board + Minimum Edit to Break AI** today.

The non-obvious insight: the strongest learning moment is not watching AI fail. It is watching students become **more or less confident for the wrong reasons** after seeing AI’s fluent answer. That is the new skill frontier: not prompting, but calibrated distrust.

---

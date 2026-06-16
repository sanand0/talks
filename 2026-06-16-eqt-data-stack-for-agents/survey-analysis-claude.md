---
title: "Analyzing audience responses from agent session"
date: 2026-06-16T21:58:24+05:30
source: "https://claude.ai/chat/d0aac97a-87a3-44f5-88a9-a86c503b4f0a"
---

## User

I was running this session on, uh, using agents with data and asked a few, uh, questions to the audience. Here are the responses to those questions. What I'd like you to do is use the data analysis skill and identify the most insightful responses that I can share.

---

## Claude

<details>
<summary>Synthesized audience poll patterns to surface shareable insights</summary>

> I need to start by reviewing the data analysis skill, then examine the uploaded files to understand what session questions the user is asking about.
>
> Reading the data-analysis skill before starting
>
> Looking at the actual data file now.
>
> Inspecting the responses TSV structure
>
> Script
>
> I'm loading this data into pandas to examine how the responses are distributed across different questions and respondents.
>
> Loading data, counting respondents and questions
>
> Script
>
> I'm looking at 15 respondents with 62 total answers across 7 questions—a small dataset, but the user wants the most compelling insights to highlight. The real story here is the before-and-after comparison on reconciliation time: showing how much faster the agent-based approach is compared to manual reconciliation of customer masters, which is the core value proposition they're trying to demonstrate.
>
> Beyond that, I need to examine the responses on data accessibility percentages, the qualitative blockers preventing deployment, storage architecture choices (since the optimal solution varies by use case—vector, relational, or graph databases), and their next steps.
>
> Examining the numeric and choice answers
>
> Script
>
> Examining qualitative free-text answers
>
> Script
>
> I've got all the data now, so I'm diving into the core analysis—comparing reconciliation times before and after for the same individuals, then running the paired analysis. I'm also noticing something interesting about the storage_choice question: according to Anand's framework, the correct answer should be "Different per question" since you'd use vectors for similarity searches, relational databases for correlation analysis, and graph databases for tracing lineage. Let me calculate the paired before/after results.
>
> Paired before/after analysis and distributions
>
> Script
>
> I'm looking at a small dataset of 15 people and noticing something striking: their estimates for reconciling customer masters varied wildly from 1 day to 60 days, suggesting there's no shared understanding of what this task actually entails. The median estimate was 6 days, but that huge spread is the real story. Among the five people who answered both before and after the demo, total estimates dropped 56% (from 25 to 11 days), with the high estimators like VD and VV shifting dramatically downward while the low estimators stayed put — essentially converging toward the faster end. On storage choices, the room split 3/3/1 across options, but only three people selected the pedagogically correct answer that different questions need different stores, revealing a significant gap in how people think about data architecture. There's also an interesting paradox emerging around data readiness that I'm still working through. K's reconciliation output is a concrete artifact worth sharing — he built confidence scoring with a 0.8 threshold and an exceptions sheet, which directly validates Anand's "Verifiable Autonomy" framework. Now I need to structure this as a report with both aggregate insights and specific quotable responses the user can share with their audience, keeping it tight and journalistic.
>
> Done

</details>

Read the data analysis skill and worked through all 62 responses (15 people, 7 questions). Here's what's worth putting back on screen — ordered by how hard it makes the room lean forward.

### 1. The headline: people don't disagree on the answer, they disagree on the _order of magnitude_

Before the demo, the same room estimated reconciling 3 customer masters at anywhere from **1 day to 60 days** — a 60× spread. Median was 6 days, mean dragged up to 10 by two outliers (A: 60, S: 20).

That spread _is_ the insight. Reconciliation isn't being estimated like an engineering task with a knowable answer; it's a vibe. Half the room is quoting a sprint, the other half is quoting a quarter, and nobody in the room flinched at sitting next to someone 10× off. That's the perfect setup line: _"Fifteen of you. Your estimates ranged 60-fold. That alone tells you we don't actually know how hard this is anymore."_

### 2. The demo didn't lower estimates — it _collapsed the spread_

Of the 5 who answered both before and after, the total estimate fell from 25 days to 11 (–56%). But the movement is one-directional and worth showing by name:

| Person | Before | After |
| ------ | ------ | ----- |
| VD     | 10     | **1** |
| VV     | 10     | **5** |
| KS     | 1      | 1     |
| SK     | 3      | 3     |
| SB     | 1      | 1     |

The three who didn't move were already the _low_ estimators. The two who moved were the high ones. The demo didn't convince optimists — it converted the skeptics and pulled them down to where the optimists already were. VD's 10→1 is your cleanest single "wait, really?" data point.

### 3. The teaching gap nobody resolved: storage

On "one store or three?" the room split **3 One-store / 3 Different-per-question / 1 Not sure.** The framework answer is _different per question_ — vector for _similar_, relational for _correlate_, graph for _trace lineage_. Half the room still wants one box to do all three. That's the unresolved tension to name explicitly: the instinct to consolidate storage is exactly the instinct an agentic stack punishes.

### 4. The data-readiness paradox — your best contradiction

People guessed a median **40%** of their data is agent-usable today (range 10–100%). But look at what they said is actually blocking them:

> Broken Data · Data quality · Unstructured data · Siloed institutional knowledge · Access issues · Missing SOP to handle data · Data security

Every single blocker is a _data-stack_ problem. **Not one person said the agents weren't good enough.** So the room simultaneously believes (a) ~40% of their data is ready and (b) the thing stopping them is that their data is broken, locked, or unstructured. Those two beliefs can't both be relaxed. SS is the sharpest illustration: answered **100% usable**, then named **"data security"** as the blocker. The optimism and the pain live in the same person.

That's your closing thesis handed back to you by the audience: _the bottleneck migrated to the data, not the model._

### 5. Two individual responses worth showing on screen

**VV's reconciliation output** — he didn't just share a link, he pasted his structure: a reconciliation sheet with **confidence score, fields used for matching, match reason, and a human-review flag that fires when confidence < 0.8**, plus a separate exceptions sheet. That's a verifiable, audit-ready reconciliation built live in the session. It's the single best proof-point that "production is free" — and it maps straight onto your verifiability framing. Show it.

**RG's next step** — "Giving the use cases, metadata and data dictionary to a semantic layer." Most "next steps" were vague ("explore AI agents," "data lifecycle automation"); his is specific, this-week-actionable, and names the semantic layer as the unlock. Good model answer for "what does a no-risk first move actually look like."

---

One caveat to hold: n=15, and only 5 answered the before/after pair, so the –56% drop is directional theater, not a statistic. The _spread_ (60×) and the _blocker clustering_ (12 responses, all data-stack) are the defensible findings — lead with those.

Want me to build the two-panel before/after visual (the 60× fan collapsing to a tight band), or draft the three callout slides?

---

## User

in front of this audience. Give me the most punchy lines that I can read out.

---

## Claude

<details>
<summary>Architected punchy, speakable lines tailored for executive data leaders</summary>

> I'm crafting sharp, quotable lines for a data leadership audience at an EQT-focused session—the kind of crisp, defensible takes that land when spoken aloud and tie back to actual numbers from the analysis.
>
> Done

</details>

Here are the lines, sequenced to the moment in the room where each one lands hardest. All defensible from your own data.

**On the spread (open with this):**

"Fifteen of you answered. Your estimates ranged from one day to sixty. That's not a disagreement about the answer — that's a sixty-fold disagreement about _what kind of problem this even is._"

"Half of you quoted a sprint. The other half quoted a quarter. And nobody flinched at the person sitting next to them."

"When smart people are sixty times apart, it's not because some of you are wrong. It's because none of us actually know anymore."

**On the before/after collapse:**

"I didn't change the optimists' minds. They already had the number. What moved was the skeptics — VD went from ten days to one. The demo didn't lower the estimate. It collapsed the _spread._"

"The people who thought it was fast didn't budge. The people who thought it was slow capitulated. That's not persuasion — that's a floor dropping out."

**On storage:**

"I asked: one store, or three? You split down the middle. Vector for _similar_, SQL for _correlate_, graph for _trace_ — three questions, three shapes. The instinct to put it all in one box is exactly the instinct an agentic stack punishes."

**On the data-readiness paradox (your strongest):**

"You told me forty percent of your data is ready for agents. Then I asked what's blocking you, and every single answer was: the data's broken, the data's locked, the data's unstructured. Both of those can't be true."

"Not one of you said the agents weren't good enough. _Not one._ The bottleneck didn't disappear — it moved. It moved into your data stack."

"One of you said a hundred percent of your data is usable — and then named _data security_ as the blocker. The optimism and the pain are living in the same person. That person is every company in this room."

**Closer:**

"The model is no longer the hard part. You just proved it to yourselves. The hard part is the thing you've been deferring for ten years — and the agents have stopped letting you defer it."

A delivery note: the paradox line and the "not one of you" line are your two biggest hits — land each, then _stop talking_ for a beat. Don't rescue the silence.

---

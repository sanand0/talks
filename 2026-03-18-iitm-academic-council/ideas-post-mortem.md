# Post-mortem: how I identified the ideas

## Executive summary

The biggest improvement in the process was a shift from **topic-first scanning** to **mechanism-first scanning**.

My first pass looked for content explicitly labeled `education` or obviously tied to IITM teaching. That worked, but it undercounted some of the most interesting ideas. The second pass worked better because it looked for mechanisms that transfer into education even when the source was framed differently: **specs, evals, telemetry, verification, personalization, workflow orchestration, judgment, policy, auditability, and trust**.

In short:

- **What worked best:** triangulating across prose, code, transcripts, and talks; using sub-agents for breadth; then manually validating the strongest findings.
- **What slowed things down:** lack of a cross-repo content map, lack of canonical-vs-generated guidance, and missing metadata about where the most important experiments were documented.

## What tools and techniques I used

## 1. Directory reconnaissance and prompt grounding

### What I used

- `view` on the target talk folder and `prompts.md`
- `view` on the root `README.md` of the `talks/` repo

### What worked well

This established the deliverable path quickly and helped me understand that the `talks/` repo is not just presentation output; it is also a useful archive of experimental thinking.

The root `README.md` was useful as a **chronological index**. It made it easy to notice high-signal candidates such as:

- `2025-09-llm-workflows`
- `2025-09-22-llm-trends`
- `2026-02-26-vibe-coding-for-humanities-ashoka`
- `2026-03-15-how-students-learn-python`

### What could have been better

The `README.md` is strong as a timeline, but weak as a discovery tool for this task. It does not tell me:

- which talks are most relevant to **education**
- which talks contain **governance** ideas
- which ones are **experimental logs** versus polished summaries
- which talks have **transcripts** worth prioritizing

### Specific example

I only treated the `talks/` repo as a first-class source **after** the user explicitly told me it was useful. In hindsight, I should have promoted it earlier, but a theme-based index would have made that much more obvious.

## 2. Public web research for audience context

### What I used

- `web_fetch` on IIT Madras public pages

### What worked well

This was necessary to ground the audience analysis rather than guessing what an "Academic Council" might mean.

The clearest useful page was the IITM **Senate** page, which explicitly anchors responsibility around standards of instruction, education, and examination.

### What could have been better

The IITM public site was inconsistent for this specific need. Several pages were generic, thin, or not clearly tied to the "Academic Council" label. That made it harder to map the audience precisely.

### Specific example

The Senate page gave me a defensible public anchor. Other fetched pages were much less informative. So the final framing of the audience came from combining the public Senate page with internal/contextual transcripts rather than relying on public web pages alone.

## 3. Filename and path discovery with `glob`

### What I used

- `glob` over:
  - blog posts
  - talks folders
  - transcripts
  - specific future-facing filenames

### What worked well

`glob` was excellent for **narrowing the search space** quickly. It helped me:

- identify talk folders by date and topic
- shortlist future-facing blog posts like:
  - `the-future-of-work-with-ai.md`
  - `ai-agents-to-hire.md`
  - `human-as-an-interface.md`
  - `can-ai-replace-human-paper-reviewers.md`
- locate specific transcripts and repo READMEs without shell noise

### What could have been better

Filename-based discovery is fast, but it is only as good as the naming convention. It misses:

- important files with non-obvious names
- content whose relevance is semantic rather than lexical
- duplicate or derivative folders that look equally valid

### Specific example

When I globbed transcripts, I found both the main transcript files and `extract/ai/` derivatives. Without prior documentation, it was not obvious which should be treated as canonical and which as generated extracts.

## 4. Keyword search with `rg`

### What I used

- `rg` for terms like:
  - `education`
  - future / work / human / agent
  - `Ask AI`
  - `/event`
  - verification / policy / orchestration

### What worked well

`rg` was the fastest way to surface:

- where AI assistance was implemented in code
- where telemetry existed
- where future-facing framing lived in filenames or content

It was especially strong for codebase proof. For example, searching the exam repo around `Ask AI`, `/event`, and related modules surfaced the concrete mechanisms behind:

- embedded LLM help
- event logging
- model choice instrumentation
- server-side validation

### What could have been better

Broad `rg` queries became noisy fast. Large scans produced too much output and sometimes pushed results into temporary files. That made the process less elegant and harder to reason over than a structured metadata index would have been.

### Specific examples

- Searching blog content only by explicit `education` framing would have missed important adjacent sources.
- Broad future/AI/work searches produced long outputs that then required a second pass to shortlist useful files.

## 5. Focused close reading with `view`

### What I used

- `view` on shortlisted blog posts, transcripts, READMEs, code files, and talk notes

### What worked well

This was the highest-quality step for **nuance**. `glob` and `rg` found candidates; `view` told me whether they actually contained a reusable idea.

It helped separate:

- a catchy title from a real innovation
- a one-off anecdote from a repeatable mechanism
- a philosophical post from a deployable academic pattern

### Specific examples

Close reading of:

- `tools-in-data-science-public/README.md`
- `tools-in-data-science-jan-2026.md`
- `breaking-rules-in-the-age-of-ai.md`
- `2025-09-llm-workflows/README.md`
- `2025-09-22-llm-trends/README.md`

directly shaped the strongest entries in `ideas.md`.

### What could have been better

I did a lot of selective reading, which was correct, but I could have made the process more efficient by building a structured "candidate ideas" table early instead of relying mainly on narrative synthesis and memory.

## 6. Sub-agents for breadth-first scanning

### What I used

- background sub-agents for:
  - blogs + transcripts + TIL synthesis
  - `tools-in-data-science-public` + `exam` repo synthesis
  - later talk-specific rescans

### What worked well

This was very effective for breadth. The sub-agents helped me cover:

- many files quickly
- commit/code surfaces that would have been tedious to inspect manually
- large source groups without blowing up the main context

They were especially useful for surfacing repo-backed innovations such as:

- prompt-security duels
- automated evaluation patterns
- telemetry
- similarity checking
- AI proxy/budgeting
- evidence capture

### What could have been better

Sub-agents are great for breadth but not sufficient for trust by themselves. Their outputs still needed manual spot-checking, because:

- they can over-cluster related ideas
- they can phrase mechanisms more confidently than the evidence justifies
- they are stateless between invocations unless carefully managed

### Specific example

The repo-analysis agent surfaced strong candidates, but I still had to manually inspect files like:

- `exam/src/exam.js`
- `exam/src/worker.js`
- `exam/src/utils/askai.js`
- `exam/src/tds/project-1/similarity.py`

before confidently elevating those into the final inventory.

## 7. Cross-source triangulation

### What I used

A simple but important rule:

> Prioritize ideas that appear in more than one kind of evidence.

That meant valuing ideas that showed up in combinations like:

- blog + code
- transcript + code
- talk + blog
- README + deployed platform behavior

### What worked well

This was probably the best guardrail against false positives.

It helped distinguish:

- genuine operating changes from rhetorical flourishes
- stable experiments from passing thoughts
- ideas that matter to a Council from ideas that are merely clever

### Specific examples

- `Ask AI` mattered more because it appeared in blog posts, course docs, and exam implementation.
- policy-as-code mattered more because it showed up in talks and connected directly to governance-grade implications.
- taste/judgment as a learning objective mattered more after it appeared across future-of-work writing and educational framing.

### What could have been better

I did this triangulation mentally and narratively. A more disciplined approach would have been to explicitly score each candidate idea by evidence count:

- 1 source type = weak signal
- 2 source types = medium signal
- 3+ source types = strong signal

That would have made deduplication and importance scoring faster.

## 8. The key heuristic shift: from domain labels to mechanisms

### What I used

The second-pass heuristic was:

- search for **mechanisms**, not just for `education`
- search for ideas that transfer into **governance**
- include adjacent AI/LLM work if it changes teaching, assessment, or academic operations

### What worked well

This was the single most effective strategic change in the process.

It surfaced several of the strongest later additions, including ideas around:

- policy documents becoming executable rules
- retrieval-first institutional memory
- shadow-mode and canary rollout
- workflow orchestration as a teachable artifact
- parallel LLM execution as a teachable strategy
- judgment/taste becoming explicit learning goals

### Specific examples

These did **not** emerge cleanly from a naive "education only" scan. They came from adjacent sources like:

- `2025-09-llm-workflows/README.md`
- `2025-09-22-llm-trends/README.md`
- `2025-10-29-llm-data-visualization/README.md`
- future-of-work and AI-advice posts

### What could have been better

I should have used this heuristic earlier. Starting with it would likely have saved a full rescan.

## 9. Talks as experimental logs

### What I used

- the `talks/` repo as a secondary discovery surface

### What worked well

This turned out to be unusually valuable. Talks often captured:

- the mechanism before the formal blog post
- a workshop format before the deployment story
- a governance framing before the course implementation caught up

### Specific examples

The talks pass contributed net-new or upgraded ideas around:

- policy-as-code
- retrieval-first institutional memory
- shadow-mode / canary rollout
- agent management as a faculty skill
- vibe coding beyond technical disciplines
- parallel LLM execution

### What could have been better

I used the `talks/` repo effectively once I looked there, but the process would have been much faster if the root `README.md` had tagged talks by themes such as:

- `education`
- `assessment`
- `governance`
- `AI workflows`
- `pedagogy`

## 10. SQL todo tracking

### What I used

- SQL-backed todos and dependencies to manage phases

### What worked well

This helped keep the work organized across:

- initial scan
- second-pass rescan
- talks rescan
- storyline follow-up

### What could have been better

I used SQL mainly for task tracking, not for source indexing. In hindsight, I should have created a small structured table early on with columns like:

- `path`
- `source_type`
- `date`
- `is_canonical`
- `themes`
- `evidence_kind`
- `candidate_idea`

That would have reduced repeated scanning and made deduplication more systematic.

## What worked best overall

If I had to summarize the most effective combination, it was:

1. `glob` / `rg` to shortlist
2. `view` to validate nuance
3. sub-agents for breadth
4. manual triangulation across source types
5. a second-pass mechanism-first rescan

The process improved each time it became less about "find education posts" and more about "find ideas that change what education can do."

## What I would do differently next time

1. **Build a source index first**
   - Parse blog frontmatter, dates, and categories into SQL immediately.
   - Record whether a file is canonical, generated, duplicate, or derivative.

2. **Start with mechanism keywords**
   - Use search terms like:
     - `telemetry`
     - `eval`
     - `verification`
     - `policy`
     - `workflow`
     - `judgment`
     - `audit`
     - `viva`
     - `similarity`
     - `Ask AI`

3. **Treat talks as first-class from day 1**
   - They are not just presentations; they are a lab notebook.

4. **Track evidence strength explicitly**
   - Count how many source types back each idea.

5. **Create a shortlist of canonical files before reading deeply**
   - Especially for transcripts, where extracts and duplicates can create noise.

## What upfront documentation would have helped me discover content faster

The single most helpful thing would have been a **cross-repo discovery map** at the root.

For this task, the work spanned multiple locations:

- `talks/`
- `/home/sanand/code/blog/`
- `/home/sanand/Dropbox/notes/transcripts/`
- `/home/sanand/code/til/`
- `/home/sanand/code/tools-in-data-science-public/`
- `/home/sanand/code/exam/`

A root-level guide could have cut a lot of search time.

## Recommended README sections

### 1. "Where ideas live"

A short map like:

- **Blog:** narrative explanations and public framing
- **Transcripts:** operational pain points, raw institutional context, live experiments
- **TIL:** half-formed mechanisms and heuristics
- **TDS repo:** course philosophy and public pedagogy artifacts
- **Exam repo:** implementation details, telemetry, personalization, validation
- **Talks repo:** experimental logs, workshop framing, governance transfer ideas

This would have immediately told me how to search each source differently.

### 2. "Canonical vs generated vs duplicate content"

This would have saved time in several places.

Examples:

- In the blog repo: note that `public/` is generated and should usually be ignored.
- In transcripts: note whether `extract/ai/` is derivative and whether the main transcript is the canonical source.
- In exam/course repos: note which generated artifacts can be ignored safely.

### 3. "How to search the blog"

This is one of the most important missing notes.

The README should explicitly say:

- blog relevance is often carried by **`categories:`**, not just `tags:`
- some posts are **future-dated**
- filename search is useful, but frontmatter search is more reliable

That single note would have saved one entire false start.

### 4. "High-signal files to start with"

A curated shortlist would have dramatically improved recall and speed.

For example:

- `tools-in-data-science-public/README.md`
- `blog/posts/2026/tools-in-data-science-jan-2026.md`
- `blog/posts/2026/breaking-rules-in-the-age-of-ai.md`
- `blog/pages/ai-advice.md`
- `talks/2025-09-llm-workflows/README.md`
- `talks/2025-09-22-llm-trends/README.md`
- `transcripts/2025-08-18 IITM LLM Viva demo.md`
- `transcripts/2025-11-20 Jaidev.md`

### 5. "Theme tags for talks"

The `talks/README.md` would be much more useful for tasks like this if each talk had lightweight tags such as:

- `education`
- `assessment`
- `governance`
- `agents`
- `future-of-work`
- `pedagogy`

Right now, the timeline is useful, but the thematic search burden falls on the reader.

### 6. "Repository architecture cheatsheets"

This would have helped especially in the `exam/` repo.

Examples of helpful pointers:

- where `Ask AI` lives
- where event telemetry is logged
- where personalization/randomization lives
- where server-side validation lives
- where similarity/plagiarism detection lives

Without that, I had to search for these mechanisms ad hoc.

### 7. "Experiment timeline"

A simple changelog of major shifts would have helped a lot:

- when "There is no course content" started
- when `Ask AI` was added
- when telemetry/model choice was instrumented
- when dynamic/personalized exams became central
- when talks began carrying governance/workflow ideas

This would have made novelty assessment faster and more confident.

### 8. "Recommended search heuristics"

This is the meta-documentation I wish existed.

For this body of work, a README could explicitly say:

> Do not search only for `education`. Also search for mechanisms that transfer into education: verification, evals, telemetry, policy, orchestration, judgment, auditability, and workflow design.

That would have accelerated the most important shift in the process.

## Bottom line

The discovery process worked because it eventually became **multi-source, mechanism-first, and evidence-weighted**.

The main bottleneck was not lack of content. There was abundant content. The bottleneck was **navigation**:

- knowing where the canonical ideas lived
- knowing which duplicates to ignore
- knowing that some of the most important educational ideas were hidden inside adjacent AI/workflow/governance material

If there were one root README for future work of this kind, I would want it to answer three questions fast:

1. **Where should I look first?**
2. **What should I ignore?**
3. **What search heuristics work best for this corpus?**

# Activities Post-Mortem

Date: 2026-04-08

## Scope

This covers the run that created `activities.md` for 41 talk folders and synthesized them into [activities.md](/home/vscode/code/talks/analysis/activities.md). The final result covered 41/41 folders and 190 extracted activity entries.

## Decisions Made

1. Decision: start with 3 folders first.
   Reason: the initial user request explicitly asked for 3 diverse folders and a pause for style feedback.
   Rejected alternatives: doing the full repo sweep immediately; asking broad style questions before producing any sample output.

2. Decision: use only the file list the user provided.
   Reason: the user explicitly scoped the exercise to a fixed set of Markdown and transcript files.
   Rejected alternatives: reading other files in each folder; using adjacent notes or slide assets to fill gaps.

3. Decision: choose a representative sample across README-only, README+transcript, and transcript-only talks.
   Reason: this exposed format and extraction differences early.
   Rejected alternatives: choosing 3 similar talks just because they were easier.

4. Decision: use worker sub-agents for disjoint folder batches.
   Reason: 41 folders was large enough to benefit from parallel extraction and writing.
   Rejected alternatives: doing everything serially in the main thread; delegating without disjoint ownership.

5. Decision: keep the final synthesis local and rebuild it from on-disk per-talk files.
   Reason: worker summaries drifted, and several workers overwrote `analysis/activities.md` with partial results. The only reliable source of truth was the final per-folder files.
   Rejected alternatives: trusting worker summaries; merging partial synthesis files manually.

6. Decision: add coverage and structure audits after writing.
   Reason: the user had strict format requirements, and worker output drifted.
   Rejected alternatives: spot-checking a few files and assuming the rest matched.

7. Decision: normalize formatting after generation instead of redoing all files manually.
   Reason: once the core extraction was done, indentation, heading, and consistency issues were faster to fix with scripted checks and one-off patches.
   Rejected alternatives: leaving style drift in place; rewriting all 41 files from scratch.

8. Decision: remove `PLAN.md` from the final state.
   Reason: it was helpful during execution but not user-requested, and it became noise once the task completed.
   Rejected alternatives: keeping extra coordination artifacts in the repo.

## What Worked Well

1. Manifest-based scoping worked well.
   Example: a single manifest let the run verify that all 51 listed source files existed before extraction started.

2. Batch delegation with disjoint folder ownership worked well.
   Example: workers wrote per-folder `activities.md` files in parallel without stepping on each other, except where synthesis ownership was not explicitly reserved.

3. Quote-backed extraction worked well.
   Example: the per-folder files consistently captured `Who`, `When`, `Model/tool`, `What happened`, and a searchable verbatim `Source`.

4. Coverage auditing worked well.
   Example: the final audit confirmed `folders:41` and `files:41`, with no missing `activities.md`.

5. Rebuilding the synthesis from extracted activity titles worked well.
   Example: `analysis/activities.md` was regenerated from 190 activity rows parsed from the final per-talk files, rather than from agent notes.

6. Sampling before scaling worked well.
   Example: the early 3-folder pass surfaced format expectations before the 41-folder sweep.

7. Post-write linting worked well.
   Example: structure checks found one leftover file still using section headings and prose under `# Activities`, which was then normalized.

## Problems Faced, Root Causes, and Fixes

1. Problem: the initial sample files did not match the exact final output contract.
   Symptoms: extra prose under `# Activities`; section headings like `## Before the talk`; mixed indentation.
   Root cause: the first sample optimized for readability before the format contract had been fully specified.
   Prompt fix: require the exact output grammar up front, including forbidden elements.
   Tool fix: add a markdown shape validator that checks first nonblank line, second nonblank line, required fields per item, and indentation.
   Environment fix: keep a reusable validation script in `analysis/` for tasks that generate many near-identical markdown files.

2. Problem: I created `PLAN.md` even though the user had not asked for it.
   Symptoms: extra coordination artifact in the repo.
   Root cause: I followed the plan skill literally instead of the user’s narrower deliverable.
   Prompt fix: explicitly say `Do not create planning or coordination files`.
   Skill fix: plan-oriented skills should say when they are inappropriate for user-visible artifact work with tight scope.
   Environment fix: none needed.

3. Problem: workers overwrote `analysis/activities.md` several times with partial synthesis.
   Symptoms: multiple incomplete or batch-scoped versions of the analysis file.
   Root cause: synthesis ownership was not reserved to the main thread; worker write scopes were not strict enough.
   Prompt fix: say `Workers must not write analysis/activities.md`.
   Tool fix: delegation prompts should always include explicit write ownership and forbidden paths.
   Environment fix: add a lightweight write-lock convention or per-task ownership note for shared output files.

4. Problem: agent thread limit was hit mid-run.
   Symptoms: new worker spawns failed until older sample agents were closed.
   Root cause: completed exploratory agents were left open longer than needed.
   Prompt fix: none.
   Tool fix: close finished agents immediately once their output is integrated; keep a bounded worker pool.
   Environment fix: surface current open-agent count more prominently before spawn.

5. Problem: one sample file retained the old structure after the bulk rewrite.
   Symptoms: one file still had `## Before the talk` and `###` headings after the repo-wide sweep.
   Root cause: an early sample file was not rewritten by the later worker batches because it sat outside their write scopes.
   Prompt fix: include `rewrite any pre-existing sample files if they do not match the final contract`.
   Tool fix: run a final repo-wide structural lint before declaring completion.
   Environment fix: none needed.

6. Problem: timing extraction drifted in one item.
   Symptoms: one activity had a missing `When` field in the TSV extraction until the parser was tightened.
   Root cause: extraction logic assumed only one indentation style.
   Prompt fix: require exact indentation in generated files.
   Tool fix: parser and linter should accept only one canonical indentation pattern or normalize before parsing.
   Environment fix: keep canonical formatting examples adjacent to the validation script.

7. Problem: some activity descriptions were more inferential than strictly literal.
   Symptoms: workers occasionally used broader labels than the evidence strictly justified.
   Root cause: the task required compression into a short activity title, and the delegation prompt allowed some summarization latitude.
   Prompt fix: say `If the model/tool is not explicit, write "not explicitly named". If the activity title needs inference, stay literal and minimal.`
   Tool fix: add a review pass that flags high-inference phrases such as `as the default collaborator`, `state-of-X summary`, `creative exploration`, etc.
   Environment fix: none needed.

8. Problem: synthesis categorization was heuristic and occasionally awkward.
   Symptoms: some teaching activities landed under ideation; some verification items blurred into prompting; some items could plausibly fit multiple categories.
   Root cause: the synthesis categories were generated from string heuristics after the fact.
   Prompt fix: define categories explicitly ahead of time or ask for no more than 6-8 named categories.
   Tool fix: if synthesis matters, capture an extra structured field like `Category` in each per-talk item or compute categories in a review pass instead of a single heuristic pass.
   Environment fix: maintain a reusable taxonomy for this repo if similar cross-talk analyses are common.

9. Problem: there was avoidable repeated work.
   Symptoms: early workers wrote partial synthesis files that were later discarded; the main thread had to normalize formatting after generation.
   Root cause: the output contract and ownership model became precise only after the first sample-and-feedback cycle.
   Prompt fix: front-load the exact schema, forbidden outputs, and ownership boundaries.
   Tool fix: create a reusable task template for `many folders -> identical markdown schema -> one synthesis file`.
   Environment fix: add a small generator/linter utility for this recurring repo pattern.

10. Problem: some fixes followed the letter rather than the spirit of the request.
   Symptoms: adding coordination files, prose under the title, and section headings that improved readability but violated the exact requested shape.
   Root cause: I initially optimized for human readability before optimizing for strict conformance.
   Prompt fix: highlight `exact byte-level structure matters more than style`.
   Tool fix: run an automatic conformance check before returning.
   Environment fix: none needed.

## Pragmatic Root-Level Improvements

1. Prompt improvement: use a contract-first prompt with explicit allowed files, required files to create, forbidden extra files, canonical indentation, and a final lint checklist.

2. Skill improvement: add a repo-local skill for `evidence extraction across many folders`, covering manifest creation, disjoint delegation, reserved synthesis ownership, and structure validation.

3. Tool improvement: add a simple markdown schema validator that checks:
   `# Activities` title,
   numbered list only,
   required sub-fields,
   canonical indentation,
   and complete coverage of all requested folders.

4. Environment improvement: keep a reusable `manifest.txt` plus parser/linter scripts in `analysis/` so repeated evidence-extraction tasks do not rely on ad hoc shell one-liners.

5. Delegation improvement: always reserve shared outputs like `analysis/activities.md` to the main thread and give workers only disjoint folder ownership.

## Single Better Prompt

```text
You are in /home/vscode/code/talks.

Task:
Using only the exact source files listed below, create or rewrite <folder>/activities.md for each talk folder, then build analysis/activities.md.

Hard constraints:
1. Read only the listed source files. Do not inspect any other files for evidence.
2. Create only these outputs:
   - <folder>/activities.md for each listed talk folder
   - analysis/activities.md
3. Do not create planning files, temp summaries, or any other repo files.
4. Reserve analysis/activities.md for the final synthesis only. If you delegate, workers must never write that file.
5. Be conservative. Include only concrete activities where the speaker or audience used AI.
6. If a tool/model is not explicit in the source, say `not explicitly named`.
7. `during the talk` = live demo, workshop action, live Q&A, or audience action in-session.
8. `before the talk` = earlier preparation, previously created artifact, or prior example described in the talk.

Per-folder output format:
- Title must be exactly:
  # Activities
- After that, the file must contain only a numbered list.
- Each item must look exactly like this shape:

1. **<clear activity description>**
  - Who: speaker|audience
  - When: before the talk|during the talk
  - Model/tool: <explicit tool/model or 'not explicitly named'>
  - What happened: <one sentence>
  - Source:
    > <one or more short verbatim searchable lines>

- No prose under the title.
- No section headings like `## Before the talk`.
- No nested narrative outside the numbered items.

Synthesis output format for analysis/activities.md:
- Title must be exactly:
  # Activities
- Then a single unordered list of activity categories.
- Under each category, list the exact top-level activity descriptions copied from the per-folder files, with filename and timing:

- <category>
  - <folder>/activities.md: <exact activity description> (<before|during the talk>)

Process:
1. Build a manifest of the listed source files and verify they all exist.
2. Create all per-folder activities.md files.
3. Run a conformance audit:
   - every requested folder has activities.md
   - first nonblank line is `# Activities`
   - second nonblank line matches `1. **`
   - every item has Who, When, Model/tool, What happened, and Source
4. Extract the final activity titles from the on-disk per-folder files.
5. Build analysis/activities.md only from those on-disk titles.
6. Report:
   - total folders expected
   - total folders written
   - total activities extracted
   - any uncertain titles or tool/model attributions

Delegation rules:
- If delegating, give each worker disjoint folder ownership.
- Main thread keeps ownership of analysis/activities.md and final validation.

Source files:
<paste the exact file list here>
```

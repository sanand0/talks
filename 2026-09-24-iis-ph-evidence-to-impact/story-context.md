# Story context for Evidence to Impact — IIS 2026

This file is supporting material for the narrative story generator. transcript.md remains the primary source for what was actually said and for all direct quotes. The notes below add event context, exact page content captured immediately after the talk, useful narrative threads, and an asset map.

## Event context

- Date: 24 Sep 2026.
- Event: International IT-BPM Summit (IIS 2026), Okada Manila.
- Workshop slot: 10:15–11:15, Day 2.
- The organizer's official workshop title was **“From Experiment to Impact: Turning Data into Competitive Advantage.”**
- The talk itself opened under the shorter title **“Evidence to Impact.”**
- In the preparation call, the organizer framed the underlying question as: **“How do we turn AI into business value at scale?”**
- Expected audience: mainly middle managers, directors and C-level delegates; room capacity around 50.
- The format was deliberately not a slide deck. Anand had told the organizers: **“There is no presentation.”** The intended format was to type, open live pages, run examples, and ask the room questions.
- Internet reliability had been a concern in advance. That became visible during the llmviz section around 29:00 when the page loaded slowly and Anand improvised around it.

This context comes from ~/Dropbox/notes/transcripts/2026-09-03 IIS 2026 Prep.md. Use it for scene-setting, not as if it was said during the workshop.



## Catalog metadata for talks/config.json

Use these derived facts when the talk-story skill updates `~/code/talks/config.json`:

- `date`: `2026-09-24`
- `time`: `2026-09-24T10:15:00+08:00`
- `duration`: `60`
- `categories`: `["latest"]`
- `event.name`: `International IT-BPM Summit (IIS) 2026`
- `event.url`: `https://iis.com.ph/`
- `location`: `Function Rooms #1 & #2, 3rd Floor Pearl Wing, Okada Manila, Parañaque City, Philippines`
- Official workshop title: `From Experiment to Impact: Turning Data into Competitive Advantage`
- Talk/opening title: `Evidence to Impact`
- Speaker: Anand S — `https://www.s-anand.net/`
- Organizer: IT and Business Process Association of the Philippines (IBPAP)
- Summit theme: `Intelligence at Scale: Accelerating the PH Pivot`
- Suggested `details` thesis: `AI is too weird and fast-moving to trust by intuition alone: question advice, verify with independent AI, calibrate confidence, benchmark what matters, and turn surviving evidence into deterministic rules.`

Natural catalog assets/links after the story is generated:

- primary page: `2026-09-24-iis-ph-evidence-to-impact/`
- transcript: `2026-09-24-iis-ph-evidence-to-impact/transcript.md`
- audio: `https://github.com/sanand0/talks/releases/download/talks/2026-09-24-iis-ph-evidence-to-impact.opus`
- comic image: `2026-09-24-iis-ph-evidence-to-impact/comic-page.avif`

The `title` field in config.json may use the eventual narrative headline, following recent talk-story convention, rather than being forced to the official workshop title.

Public event references:
- Summit homepage: https://iis.com.ph/
- About IIS / 2026 theme: https://iis.com.ph/about-iis/
- Agenda showing Workshop 7 at 10:15–11:15 on 24 Sep 2026: https://iis.com.ph/agenda


## The story hidden inside the transcript

The talk has a cleaner narrative arc than the prepared link list suggests.

### 1. Start from ignorance, not certainty

- [00:43] “I think it pays to be a little skeptical about AI.”
- [05:59] An audience member says: “We don't know!”
- [06:01] Anand turns it into the thesis: **“‘We don't know’ is a great place to be, because then you can start checking.”**
- This is probably the strongest opening/recurring motif.

### 2. AI is weird enough that intuition is unreliable

- Random-number guesses lead into model-specific “favorite” numbers.
- The audience guesses 75, 37, 15, 3, 1, 99, 100, 50; none hits 47.
- Multiplication then shows a different kind of jaggedness: trivial for calculators, oddly bounded for language models, and rapidly improving over model generations.

### 3. Advice is now experimentally testable

- The room itself predicts the prompt experiment surprisingly well: roughly 80% vote for reasoning.
- [09:16] “The only one that helps is reasoning.”
- The Pólya audit makes the point bigger: even 80-year-old canonical advice can be audited at scale.
- The simple-writing experiment gives a particularly useful reversal: a desirable output constraint can degrade the thinking process; separate reasoning from rewriting.

### 4. Verification does not require a perfect verifier

- [15:39] “That's the beauty of verification. An additional verification costs you very little.”
- Double-checking works because models often make different mistakes.
- The powerful business trade-off is not “replace 100% of work.” It is closer to: automate about 72% while driving error under 1% in that experiment.
- [19:34] “I can give it to you at 99.3% accuracy, but I can't reduce 100% of your workload. I can only reduce 72% of your workload. I'll take it!”

### 5. Confidence is a signal to calibrate, not a number to believe

- The room expects mild overconfidence; Luna is much more overconfident on the BANKING77 task.
- The talk moves from stated confidence → prompt calibration → token logprobs → human-review queues.
- [23:09] The operational leap: every model has a curve, and **“you can create a queue.”**
- [35:07] On logprobs: **“Don't take the number for what it is; just sort by the logprobs and go down the queue.”**
- This is a strong bridge from model psychology to operations design.

### 6. Benchmark what you can; borrow benchmarks when you cannot

- The LLM pricing chart makes benchmarking an economic routing problem, not a leaderboard.
- GDPVal provides a benchmark for tasks Anand personally cannot judge.
- The tax anecdote raises the uncomfortable question: what happens when AI is smart enough to tell you something consequential in a field where you have no expertise?
- [45:51] **“If you can create a benchmark, fantastic. If you can't, then find who's creating a benchmark and use it.”**
- The wedding-photo colorization is the opposite case: an unusually personal benchmark where Anand is one of the best possible evaluators.

### 7. Keep an impossibility list

- [47:02] Anand describes keeping a list of things models could not do.
- The parents' wedding photo moved off that list only the previous week.
- The generated version made everyone subtly happier — a funny, memorable example of a benchmark revealing a model bias.
- [48:26] “If you can find a benchmark that at a glance you say, ‘Yes, that's right,’ or ‘No, this is wrong,’ ... you've got an edge.”

### 8. Evidence becomes impact when it changes a rule

The live decision-tree demo is a miniature scientific process:

- first result: **86.0%** accuracy;
- Anand spots target leakage because G1/G2 grades predict G3;
- removing grade information collapses performance to **31.8%**;
- AI generates derived features and a max-depth-3 tree;
- performance recovers to **67.3%**.

The current browser page still contains all three logged results in page-context/decision-tree.md.

[53:16] The result is useful because it identifies factors and creates a deterministic rule that can be improved over time.

[53:37] Code/rules are attractive because they are repeatable, cheap to run, inspectable, and revisable.

### 9. The audience writes the epilogue

- Q&A #1 turns risk into a rule: [56:34] **“Benchmark more where things are important; where it's less important, proportionally benchmark less.”**
- Q&A #2 asks whether Anand verified the tax result. He admits he did not initially because he was too excited.
- Audience member closes the loop at [59:28]: **“If you're too excited, don't forget to verify!”**
- That line is an excellent ending because the audience restates the talk's thesis back to the speaker.

## Exact source-page captures

These Markdown files were extracted from the already-open browser tabs immediately after the talk. They contain the readable content of the exact pages used. Prefer these for numerical/detail context over memory; use transcript.md for what Anand actually said.

| Source | Browser capture | Screenshot fallback | Useful material |
|---|---|---|---|
| LLM favorite numbers | page-context/llmrandom.md | screenshots/llmrandom.avif | GPT-3.5 → 47, Claude 3 Haiku → 42, Gemini 1.0 Pro → 72; human-like avoidance patterns |
| LLM mental math | page-context/llmmath.md | screenshots/llmmath.avif | updated model-by-model multiplication results; newer models reaching 35/35 |
| Emotion prompts | page-context/emotion-prompts.md | screenshots/emotion-prompts.avif | 40-model experiment; reasoning +3.5pp overall, other emotional/persuasion prompts neutral or worse |
| Pólya audit | page-context/polya-audit.md | screenshots/polya-audit.avif | 6,747 experiments; 15 heuristics × 7 domains × 3 models; strongly context-dependent advice |
| Simple writing | page-context/simple-writing.md | screenshots/simple-writing.avif | six-task ASD-STE100 experiment; simpler output instruction reduced thinking quality |
| Double checking | page-context/double-checking.md | screenshots/double-checking.avif | about 14% one-model error; about 3.7% with two-model agreement; under 1% with five, at about 28% review load |
| Confidence calibration | page-context/confidence-calibration.md | screenshots/confidence-calibration.avif | 770 BANKING77 cases + 2,310 untouched holdout; prompt calibration and logprob routing |
| Token visualization | page-context/llmviz.md | screenshots/llmviz.avif | next-token alternatives/logprobs and uncertainty visualization |
| LLM pricing | page-context/llmpricing.md | screenshots/llmpricing.avif | cost-quality frontier over time; “cheapest model that reliably finishes this task” |
| GDPVal analysis | page-context/gdpval.md | screenshots/gdpval.avif | occupational tasks and model-vs-expert win rates; bridal-store general-manager task is preserved |
| Photo colorization benchmark | page-context/photo-colorization.md | screenshots/photo-colorization.avif | why family faces make a high-sensitivity personal eval; “slightly happier” bias |
| Decision Tree Builder | page-context/decision-tree.md | screenshots/decision-tree.avif | exact live state and all three accuracy logs: 86.0%, 31.8%, 67.3% |

The screenshots are intentionally viewport captures, not giant full-page images. They are AVIF quality 50, high-effort encoded, 1512×1000, generally 24–64 KB. Use them only when a screenshot is narratively better than an iframe, or as a fallback if the source refuses embedding.

## Wedding-photo benchmark assets

links.md explicitly says to insert images from the photo-colorization post. The actual images are saved locally and compressed for story use:

- images/wedding-original.avif — original black-and-white image, 531×408.
- images/wedding-color.avif — GPT Image 2.5 colorized image, 1165×900.
- images/wedding-color-digital.avif — “modern digital camera transported back in time” version, 1178×900.

A side-by-side original/color comparison is likely stronger than the page screenshot. The third image works well as a follow-up showing that added photographic polish also pushes expressions subtly toward smiles.

## Main visual/audio assets

- comic-page.avif — visual summary of the talk. Feature prominently near the top per the talk-story skill.
- 2026-09-24-iis-ph-evidence-to-impact.opus — full talk recording. Use the normal public talks release URL convention from the skill.
- transcript.md — primary quote source.
- links.md — source of the pages used live. Honor its EMBED and INSERT IMAGES FROM directives where useful.

## Facts where source pages are safer than transcript wording

The transcript was generated automatically and contains occasional slips or transcription/model-name issues. For narrative prose:

- Treat direct quotes as transcript-grounded and reproduce them verbatim if used.
- For benchmark numbers, model names, experiment sizes, and page claims, cross-check page-context/*.md.
- Pólya is Hungarian-American, not Russian; the transcript itself contains a bracketed correction.
- The current llmmath page says three newer models scored 35/35 and also warns that an older hardest-test expected value had been rounded incorrectly in JavaScript. That nuance is more reliable than broad claims from memory.
- Avoid turning Anand's humorous intelligence analogies (“high-school student”, “PhD candidate”, “tenured professor”) into literal psychometric claims. They are storytelling labels attached to the pricing chart.
- The tax-return story is an anecdote from the talk, not a benchmark result. Keep the uncertainty and eventual auditor/senior confirmation in the narrative.
- Do not link any private ChatGPT/Claude browser tabs. Only use public/share links or links in links.md and the public source pages.

## Useful exact page facts

### Favorite numbers

From page-context/llmrandom.md:

- GPT-3.5 Turbo: 47.
- Claude 3 Haiku: 42.
- Gemini 1.0 Pro: 72.
- Single digits/repeated digits are rare; 7-endings are unusually common.

### Emotion prompts

From page-context/emotion-prompts.md:

- 40 models.
- “Think step by step” was the only variant with an overall positive effect, about +3.5 percentage points versus normal wording, with p about 0.06.
- On harder 4–7 digit multiplication, the gain was about +17–20 percentage points.
- The effect is model/task dependent; the page explicitly cautions against universalizing it.

### Pólya

From page-context/polya-audit.md:

- 6,747 runs, three models, 15 heuristics, seven math domains.
- The strongest signal is problem type, not a universally good heuristic.
- Some advice flips sign by model.
- Case analysis is the most reliable heuristic in the experiment.
- The experiment cost only a few dollars, reinforcing the “cheap experiments” theme.

### Double checking

From page-context/double-checking.md:

- One-model performance is useful but imperfect.
- Two-model disagreement routing drives error from roughly 14% to roughly 4%.
- Five-model agreement gets below 1% error while still automating the majority of cases.
- The value comes from diversity of errors, not from any one infallible checker.

### Confidence calibration

From page-context/confidence-calibration.md:

- 770 historical BANKING77 cases.
- Luna baseline: 84.0% correct, 95.7% mean stated confidence.
- Among Luna cases stated at at least 95% under the original wording, observed error was 10.3%.
- “Top-two probability” wording reduced at-least-95% error to 3.9% in that experiment.
- Raw token logprobs were not calibrated probabilities, but were strong risk-ranking signals.
- A cutoff frozen on the 770-case set auto-passed 65.2% of 2,310 untouched cases at 4.4% observed error.

### Pricing

From page-context/llmpricing.md:

- The page's key operational message: the model frontier is now a routing table.
- The right question is increasingly **“which is the cheapest model that reliably finishes this task?”**

### Photo benchmark

From page-context/photo-colorization.md:

- Anand chose it because it is a real need, a known model failure, and a benchmark he can personally evaluate with unusually high sensitivity.
- The consistent subtle error he noticed: people were slightly more smiley/happier than the originals.

### Decision-tree live demo

From page-context/decision-tree.md:

- The browser's log preserves:
  - Decision tree model created successfully! Accuracy: 86.0%
  - Accuracy: 31.8%
  - Accuracy: 67.3%
- The final generated model excluded G1/G2 and used a max-depth-3 decision tree with derived features such as study_efficiency, absences_per_age, and traveltime_to_studytime.
- This is the strongest concrete illustration of “generate rules”: AI helps discover features/rules, but a human spots leakage, imposes constraints, and reruns the measurable experiment.

## Possible connective tissue

These are suggestions, not instructions; the story writer should choose what produces the best narrative.

- **“We don't know” → evidence** is a more human spine than organizing the article as five numbered principles.
- The workshop repeatedly turns a feeling into a measurement: random numbers, prompt folklore, Pólya, confidence, model choice, image fidelity, decision rules.
- The talk repeatedly moves from **non-deterministic AI → deterministic scaffolding**: ask several models; sort by risk; benchmark on known cases; create a rule/code artifact; rerun and improve.
- There is a nice symmetry between the beginning and end: the audience cannot guess ChatGPT's “random” number; the audience eventually reminds Anand to verify. The room starts by being wrong about the model and ends by correcting the speaker.
- Another recurring contrast: **cheap intelligence makes verification cheap too.** The story should not frame verification as merely a tax; it is part of why more ambitious automation becomes possible.

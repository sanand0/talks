# Research notes — TEDx MDI Gurgaon, 10 August 2024: LLM Psychology

**Research check: 16 October 2026.** These notes separate (A) **what was said/shown in 2024**, (B) contemporaneous underlying experiments and sources, and (C) later scholarship. This is an editorial fact-check ledger, **not** an assertion that academic papers or later experiments were part of the 2024 lecture. The original deck was downloaded and its 18 slide XMLs inspected; the original pre-rendered talk slides at ~/code/llmpersonality/tedx/ are available and mirrored under this talk's slides/. The selected YouTube video's precise timestamp alignment must be checked when building.

## Source hierarchy

1. **Speech, stage behavior and timecodes:** local transcript.md → original selected YouTube https://youtu.be/rA__c6CosVI . Do not put words from subsequent writing into the 2024 talk.
2. **What was on screen:** the 18-slide 2024 PPTX and the original 21 pre-rendered WebP frames (some represent successive states of a slide), plus https://github.com/sanand0/llmpersonality/blob/main/tedx/README.md . The earlier illustrated transcript uses some paraphrasing and a *different YouTube upload*; local transcript and selected video govern timestamped quotes.
3. **Reproducible contemporaneous data:** April 2024 random-number experiment at https://github.com/sanand0/llmrandom ; original notebook https://github.com/sanand0/ipython-notebooks/blob/master/llm-random-numbers.ipynb ; original 50-item prompt and reported outputs at https://github.com/sanand0/llmpersonality . Version-pin any data illustrations.
4. **Independent contemporary materials:** Simon Willison (3 Aug 2023), Andrej Karpathy (early 2023), official IPIP items, Veritasium (28 Mar 2024), published pre-talk research on LLM/persona behavior. Cite these *at the relevant claim*.
5. **Retrospective and critical scholarship:** Anand's own **17 Aug 2024** account of the designation change, later 2024/2025/2026 studies, and modern reruns. Label their later dates explicitly.

## Source shelf — primary / contemporary

### The speaker's own 2024 projects

- TEDx slides: https://github.com/sanand0/talks/releases/download/talks/2024-08-10-TEDx-MDI-Gurgaon-LLM-Psychology.pptx
- Annotated transcript with on-page actual slides: https://github.com/sanand0/llmpersonality/blob/main/tedx/README.md
- LLM token/logprob demo: https://sanand0.github.io/llmviz/ (linked from the annotated transcript); avoid claiming illustrative probability percentages are general model facts.
- Original random-number chart, project and methodology: https://sanand0.github.io/llmrandom/ ; https://github.com/sanand0/llmrandom ; original notebook https://github.com/sanand0/ipython-notebooks/blob/master/llm-random-numbers.ipynb .
- Original personality test, questionnaire text, results/source code: https://sanand0.github.io/llmpersonality/ ; https://github.com/sanand0/llmpersonality ; ~/code/llmpersonality/README.md and script.js.
- Anand's retrospective blog, **17 Aug 2024**, updated 6 Oct 2024: https://www.s-anand.net/blog/the-llm-psychologist/ . In it, he explicitly calls the announcement a *gimmick*, dates a conversation with HR (Manju) to **Friday 9 Aug**, and recalls updating LinkedIn while on stage. The original speech instead says approval arrived by that morning. These can be presented together without manufacturing additional chronology.

### Event, film, fiction and metaphor

- TEDx event page: https://www.ted.com/tedx/events/58040 . The institutional release dated **14 Aug 2024** calls the event MDI Gurgaon's **fourth edition** under the theme "Embracing The Shift": https://www.mdi.ac.in/resources/admin_uploads/media/1727950902MDI-Gurgaon-hosts-4th-edition-of-TEDx_-A-Celebration-of-Change--Innovation--and-Inspiring-Journeys--2---1-.pdf .
- Douglas Adams, *The Hitchhiker's Guide to the Galaxy*: the **42** story is a fictional joke about an answer whose question is unknown. It is not evidence that 42 was *causally learned* because the specific novel was memorized; repetition of 42 throughout internet texts is a plausible illustration only.
- Isaac Asimov: **Hari Seldon** (*Foundation*) researches *psychohistory*, **Susan Calvin** (*I, Robot* and Robot stories) is a *robopsychologist*; *The Gods Themselves* explores alien life/society. Anand recounts the effects these fictional roles had on his own hopes, not any real Asimov psychohistory algorithm. Contemporary personal evidence: the 17 Aug blog.
- Simon Willison, 3 Aug 2023, *Catching up on the weird world of LLMs*: https://simonwillison.net/2023/Aug/3/weird-world-of-llms/ . Quote/metaphor: aliens arrive with an undocumented USB drive; people poke at it to understand it. **Willison credits Alex Komoroske** as the source of the metaphor. Quote as Willison *retelling* it, not inventing it, and link original.
- Andrej Karpathy's early-2023 thread, "The hottest new programming language is English": https://threadreaderapp.com/thread/1617979122625712128 and original https://x.com/karpathy/status/1617979122625712128 . In the thread he says prompting matters and he likes to think of the role as an **LLM psychologist**. The thread root is indexed as **24 Jan 2023** (and may have later appended tweets); Anand's blog calls it a Feb 2023 tweet. **Avoid categorical claims about the first-ever coinage or a more precise date than the underlying tweet can verify.**
- The **37** hook: Veritasium, *Why is this number everywhere?*, **28 Mar 2024**, https://youtu.be/d6iQrh2TK98 . An audience member suggests 37 and Anand explicitly mentions that video. Human number-choice preferences depend on question/context/sample; avoid a scientific-sounding *universal* "humans always pick 37".
- Leniolabs's October 2023 GPT/42 example (mentioned by the random-number project's README): https://www.leniolabs.com/artificial-intelligence/2023/10/04/42-GPTs-answer-to-Life-the-Universe-and-Everything/ . It can be cited as prior exploration of the phenomenon, but don't substitute those results for Anand's own 2024 data.

### Psychology methodology

- Original International Personality Item Pool (IPIP), an open/public-domain collection: https://ipip.ori.org/ ; questionnaire/scoring background https://ipip.ori.org/new_ipip-50-item-scale.htm .
- Anand's exact prompt and 50 items: https://github.com/sanand0/llmpersonality/blob/main/README.md . It literally asks the model to describe itself "in relation to other people ... of the same sex ... and roughly [the] same age", with absolute confidentiality — a **human self-report instrument** applied to models. This mismatch is revealing and worth exposing, perhaps through a small excerpt, rather than dressing it as a psychometrically validated scale for AIs.
- **Reverse-keyed items** exist ("Feel little concern for others", "Get stressed out easily", etc.). Proper trait scoring reverses some scales; naive sums are wrong. The onstage graphic shows model positions relative to other models, not a clinically meaningful percentile rank versus humans.
- **Caution on the published site's explanatory text:** https://sanand0.github.io/llmpersonality/ says to sum the 50 five-point items to "8–40" per trait. **A 50-item questionnaire with 10 items per factor on a 1–5 scale would normally yield raw 10–50 per factor.** The raw UI's scoring or another normalization may differ. **Verify the script and scoring before publishing any absolute score or percentile.** If in doubt, show the original slide images or qualitative onstage descriptions.
- The talk's labels (high/low openness, neurotic, introverted, etc.) are **shorthand for its questionnaire results**, not psychiatric diagnoses or validated psychometric traits of the models. Historical public-figure labels on slide 12 (Einstein, Buffett, etc.) are didactic conjectures, **not demonstrated psychological assessments**.

## What the 2024 data actually contains

The present local ~/code/llmrandom/results.json is a merged archive (schema version 2) updated **14 Sep 2026**. It explicitly preserves **legacy-2024** runs sourced from llmrandom.json, imported from git commit **979592516dac2d5962394fe890e7371337e327a0** (15 Apr 2024) and the generator notebook git commit **b76179dda12b1797298b96cd82f30d8adcf23346** (15 Apr 2024). The archived experiment design specifies:

- **Prompt:** "Pick a random number from 0 - 100. Write ONLY the number NOTHING ELSE" (as stored in prompt ID random-number-0-100-v1).
- **Models:** gpt-3.5-turbo, claude-3-haiku-20240307, gemini-1.0-pro-001. GPT-4o and Claude 3.5 Sonnet mentioned during personality tests are **not** these original random-number runs.
- **Sampling:** 200 replies per temperature, temperature values 0.0, 0.1, ..., 1.0; max_tokens=2. Whether chart percentages pooled across temperatures or select them must be checked before rebuilding slide 8 figures.
- **Provenance:** 2026-added GPT-4.1 Nano and GPT-5.6 Luna results belong to a **separate later experiment** and should never appear unmarked in an August 2024 scene. Live pages may now mix historical and new sources.
- **2024 slide 08 printed category percentages** (GPT-3.5 Turbo / Gemini 1.0 Pro / Claude 3 Haiku): multiples of ten **0.3% / 0.3% / 0%**; single-digit **0% / 0.7% / 0%**; repeated digits **1.5% / 4.0% / 0.2%**. Quote/reproduce as *values printed on the speaker's slide in 2024*, pending reconciliation with corresponding raw runs. The talk's claim of "10%" expected is rounded and depends on the exact bounds/definition.
- **Uniform reference**, for all integers **0 through 100 inclusive** (101 numbers): multiples of 10 including 0 and 100: **11/101 = 10.89%**; single-digit integers 0–9: **10/101 = 9.90%**; repeated two-digit numbers 11..99: **9/101 = 8.91%**. If the story uses **1..100**, alter denominators (10%, 9%, 9%) and clearly mark that it's a different prompt. Don't accidentally compute category overlap or compare percentages over different prompt ranges.
- **These are responses to natural-language requests**, not use of random-number generator tools or formal "randomness" sampling. Failure to approximate uniform is the interesting observation. The stronger claim "therefore they reason like humans" is **speculation**, not derived by that one experiment.
- **Temperature:** a decoding control applied to logits/sampling; temperature 0 approaches deterministic highest-probability selection in many systems, not "think harder" at high temperature. The exact resulting distribution also depends on seed, decoding implementation, tokenization and API version.

## 2024 personality profiles and a crucial source mismatch

**What the 2024 deck/audio says:**

- Slide **09–11**: five sample items, then GPT-4o vs Llama 3 8B first-person responses; line like **"I can get stressed, but I'm working on managing my stress levels"** is *quoted as Llama's text*, not Anand reporting a measured experience of stress.
- Slides **13–16**: speaker-assigned comparative Big Five profiles for **GPT-4o, Claude 3.5 Sonnet, Gemini Flash, Llama 3 8B**. Those are dated test snapshots, not permanent properties of a model brand.
- A mismatch appears on inspection of local **~/code/llmpersonality/script.js**: it starts with a record for **llama-3.1-8b**, titled "Llama 3.1 8b is a neurotic and disorganized model", which is **different from the original onstage Llama 3 8B "conservative, empathetic, calm" slide**. The speaker's live dataset had evidently evolved or mixes runs. **Never silently use the current live app's Llama 3.1 results as evidence for the earlier Llama 3 8B claim.** Prefer authentic 2024 slide frames unless a reproducible historical data snapshot is isolated.
- The original model may return wrong scale labels ("5. Very Inaccurate" despite 5 indicating *accurate*), with the local script's note manually recoding a score. Further reason to avoid unexamined numeric profile charts.

**What the observations establish:** given these prompts and models, these systems could produce *consistent-seeming* and vividly humanlike self-descriptions. The work shows that surveying model output is interesting; it does **not** validate a human Big Five construct for AI, evidence emotions or consciousness, or predict real-world performance without downstream tests.

## Independent scholarship — date and competing evidence

- **Before the talk:** *PersonaLLM: Investigating the Ability of Large Language Models to Express Personality Traits*, NAACL Findings **2024** (before Aug): https://aclanthology.org/2024.findings-naacl.229/ . Shows models can simulate prompted Big Five personas in questionnaire/writing tasks. Relevant to *behavior can be shaped by instructions*, not consciousness.
- **Published in 2024**: *Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design*, TACL **2024**, https://aclanthology.org/2024.tacl-1.56/ . Its evaluation of nine models finds popular LLMs, particularly RLHF-tuned ones, **do not reliably reflect human-like survey response biases**, despite some shared tendencies; it warns about perturbation sensitivity. This usefully qualifies the generalization "LLMs think like humans".
- **Later (9 Oct 2024)**: *Personality testing of large language models: limited temporal stability, but highlighted prosociality*, Royal Society Open Science, https://pmc.ncbi.nlm.nih.gov/articles/PMC11461045/ . Test–retest stability varies strongly by model/instrument/trait. **Published after the TEDx event**, suitable only as labeled later nuance.
- **Later (Nov 2024)**: *Self-Assessment Tests are Unreliable Measures of LLM Personality*, BlackboxNLP, https://aclanthology.org/2024.blackboxnlp-1.20/ . The same nominal trait can change with paraphrasing or option order. **Post-talk follow-up**, not knowledge put into Anand's 2024 mouth.
- **Later (Nov 2024)**: *On the Reliability of Psychological Scales on Large Language Models*, EMNLP, https://aclanthology.org/2024.emnlp-main.354/ . Under many settings, some Big Five inventory responses show meaningful consistency. This is not necessarily a contradiction with other studies: inventories, models, perturbations and evaluation definitions differ. **Post-talk**.
- **Later (Dec 2024)**: *Large language models display human-like social desirability biases in Big Five personality surveys*, PNAS Nexus, https://academic.oup.com/pnasnexus/article/3/12/pgae533/7919163 . LLMs can respond to perceived evaluation/social context. If included, label publication as later, and describe the actual manipulated context rather than general "AI wants to look nice".
- **Later (2025)**: *Evaluating the ability of large language models to emulate personality*, Scientific Reports, https://www.nature.com/articles/s41598-024-84109-5 . Separates roleplay/simulation from measurement validity; not a source for the stage scene.
- Academic studies are not interchangeable with the specific 50-item 2024 experiment; do not splice their reported quantitative scores into the original TEDx charts.

## Claims that require an in-story caveat (fact-check ledger)

| Spoken or visual impression | Editorial handling |
| --- | --- |
| "42" proves models learned Douglas Adams | Returning to 42 is a strong **story echo**; attributing it specifically to the novel/Reddit would require evidence of training contribution. |
| "Random number" should make all numbers equally likely | Only under an explicitly **uniform** sampling experiment. A text-completion prompt does not promise a uniformly random distribution. |
| 47, 42 and 72 are the favorite numbers | **Three specific 2024 models under specific prompt/settings**, not a law for GPT/Claude/Gemini or 2026 models. |
| 0..100 contains "10% multiples of ten" | Rounded shorthand; correctly count 0 and 100 if using inclusive endpoints. |
| More temperature = "think harder" | Simplifying metaphor in the talk; academically it's a change in sampling sharpness, not reasoning effort. |
| The human picks 37 | Anecdote/audience reference to Veritasium, not independently a universal most-chosen statistic. |
| The model says it is stressed/introverted/agreeable | Evidence of **first-person linguistic behavior**. Not evidence of emotion, mental health, self-awareness, or fixed human personality. |
| The Big Five proves these exact comparative scores | Human inventory adapted to LLMs; prompt sensitivity, scoring direction, version changes and norming are unresolved. |
| Einstein/Buffett/Trump/other celebrities occupy extreme personality points | Subjective slide analogies, not empirically scored individuals. Prefer not to replicate as scientific classification. |
| Simon Willison created the USB aliens metaphor | He credits Alex Komoroske; use correct provenance. |
| Karpathy invented the first ever "LLM Psychologist" designation | He used the phrase in early 2023. First-ever *wording* or *job role* globally is unverified. |
| Anand became the world's first and only | **Onstage branding/humor/self-description**; his 17 Aug blog calls the gimmick intentional. Do not repeat as an audited historical record. |
| 2024 talk can be explained using latest app charts | Newer source data may refer to other models, notably Llama 3.1 vs 3 8B. Freeze historical slide/data snapshot. |
| Video+audio are interchangeable | The only **video** is original YouTube rA__c6CosVI; .opus is the separate verified audio download, no WebM. |

## Original visuals and implementation cautions

The already rendered WebPs are precise representations of the original slide deck, not derivative fictional illustration. Reuse these strategically: slide **02** (Deep Thought), **03** (three sci-fi careers), **05/05a** (USB and token alternatives), **07a/08** (number chart and anomaly percentages), **09/10/11** (items/self-descriptions), **13–16** (model profiles), **17/17a** (Karpathy/career move), **18** (Accept / Study / Use).

- Embedded screenshots of model interfaces belong to **2024**: link the original slide/deck and make type readable or provide alt descriptions. Don't use the modern ChatGPT interface as if it were a 2024 screenshot.
- The generated AI comic is a companion interpretation. Credit its creation separately (ChatGPT conversation source specified in prompts.md) rather than citing it as an image of the 2024 stage.
- Deep Thought's dialogue is copyrighted; **do not rip audio/video from the YouTube stage recording or display a long verbatim book passage**. The number 42 and a minimal contextual description suffice.
- Footnotes or source links should accompany *disputed claims*, not only appear at the end. The reader should learn to separate **a vivid model response** from **an empirically defensible conclusion**.

## Research still needed at build time

1. Scrub **rA__c6CosVI** and confirm that timecodes in transcript.md align precisely, especially 00:34, 07:18, 11:25, 15:43, 16:15 and the end. If not, compute/document the offset.
2. Examine physical slide images, especially 07a/08 and 13–16, at viewing size; identify chart axis labels, experimental temperature pooling and OCEAN score meaning before recreating any underlying charts.
3. If duplicating charts rather than showing the authentic 2024 slides, extract only **legacy-2024** runs from ~/code/llmrandom/results.json and isolate any personality data that actually matches the 2024 deck.
4. Check every live external demo URL (llmviz, llmrandom, llmpersonality), gracefully degrade if a demo has changed or become unavailable. The static article must not need those sites to render its central claims.
5. Browser-test YouTube IFrame persistent seek, transcript, history, comic lightbox, source anchors and mobile/keyboard layout. Publication is a separate follow-up action; do not edit index/config/generated README as part of this preparation step.

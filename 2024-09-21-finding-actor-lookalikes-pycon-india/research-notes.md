# Research notes — PyCon India 2024 actor look-alikes

Prepared 16 October 2026. This is a **fact-check ledger for a historical demonstration**, not a current embedding-model benchmark. Original PyCon video and transcript: https://youtu.be/FHa8Xgssrz4 and [transcript.md](transcript.md). The later-published video describes the 21 September 2024 stage talk.

## Primary provenance

- PyCon India 2024 official speaker schedule, Track 1, **21 Sep 14:45–15:15**, https://in.pycon.org/2024/schedule/ ; selected proposal https://in.pycon.org/cfp/2024/proposals/finding-actor-look-alikes-with-multi-modal-llms~azpn8/
- Python India original video (published 25 March 2025; its description says **21 September 2024 NIMHANS**): https://youtu.be/FHa8Xgssrz4 . Transcript reaches 30:28 including host Q&A.
- Author source repo: https://github.com/sanand0/actor-lookalikes ; README (on current GitHub) explicitly names **two different talks**: 8 Aug DataHack Summit GPT-assisted talk, and 21 Sep PyCon slide deck. Original slide prompt: https://github.com/sanand0/actor-lookalikes/blob/main/slide-prompt.md
- Actual PyCon slide deck link https://llmfoundry.straive.com/apps/actor-lookalikes.html is **unverified/inaccessible here (timed out from Plutonium)**. Public slide-prompt and repo image assets are present; neither by itself proves exactly what audience saw. Use video frames if deck remains private.

## Claim ledger

| Claim in talk | Confidence / caveat | How to publish |
| --- | --- | --- |
| 'Claude 3 Haiku picks 42; GPT-3.5 picks 47' (01:14–02:59) | Speaker's earlier random-number tests. Prompt, sampling and count matter. | Historical 2024 repeated-generation examples; don't say all LLMs are nonrandom or uniformly fail. |
| ~USD 5k GPU / two months vetoed (02:59) | Author's co-founder anecdote, no independent budget sheet. | Tell as recollection; no audit-grade cost comparison. |
| Elo–price frontier and 10k/4m analogy (03:31–07:01) | Elo crowd ranking, per-token price vs hosted GPU prices are **different measures**. Cost and quality were changing rapidly. | Show archived chart and date. Don't present budget numbers as measured savings. |
| 'Claude 3.5 Haiku' before Sep 2024 (05:46) | **Chronological inconsistency.** Anthropic announced 3.5 Haiku **after** the PyCon talk; likely transcript misheard 'Claude 3 Haiku'. | Listen/watch original frame; do not silently assert anachronistic model. |
| Embeddings are 'practically free' and reproducible (07:01–08:47) | Token charges, cache, model lifecycle and hosting still matter; speaker himself reports ~2% unexpected output differences in a course use case. | 'Inexpensive enough for repeated comparisons in that demo'; don't guarantee determinism. |
| 1,530-odd features for 'apple' (08:47) | OpenAI text-embedding-3-small commonly uses **1,536 dimensions** by default; speech rounds loosely. | Label 1,536 if using that model/dimension, otherwise quote approximate. |
| Neighbors and 15 topic clusters (11:22–17:14) | From one catchphrase CSV and demo. K-means depends on k, seed/preprocessing; LLM names are summaries. | Demo output, not ground truth or proof of semantic correctness. |
| 'Dot product gives distance' (18:25) | For unit-normalized vectors, dot product is **cosine similarity**, not distance. Larger means *more* similar; cosine distance can be 1 - similarity. | Explain with normalized vectors and correct axis labels. |
| Text and image go into one space (19:12) | **For a specific multimodal embedding model** trained for joint comparison. Separate incompatible embedding models can't be compared directly. | Name Google's contemporaneous multimodal embeddings; clarify compatibility. |
| Face can be plotted against 'Chinese'/'African' (21:27) | This is a model's association, not evidence of ethnicity, nationality, race or objective physiognomy; may encode demographic bias. | Prefer benign prompt axes; critique briefly. **No face-based protected trait classifier**. |
| Driver-photo pilot finished in six days (22:01–22:50) | First-person anecdote, lacks error rates, holdout test, baseline and production records. | Useful case story explicitly attributed; don't assert identity de-duplication effectiveness without evaluation. |
| Nana resembles Irrfan, Varun resembles Shah Rukh (23:35–26:22) | Displayed model matches within **specific photo corpus** and model; no human-rater agreement nor audited confidence. | Label 'the demo ranked this photo closest in the corpus'; don't universalize. |
| Spouses vs visual similarity (27:30–28:13) | Audience's unanswered falsification hypothesis; speaker says he doesn't know. | Use as a research question and candidate experiment, **not a fact** about embedding training. |
| 'No more bespoke model training' (22:50) | Successful pilot example does not prove training is never needed. | Explain tradeoffs: pretrained model as first baseline, task-specific evaluation and possible fine-tuning when needed. |

## Independent research and documentation

- Radford et al. (2021), **CLIP**: text/image alignment enables zero-shot transfer but is not a person-identity verifier and has deployment limits: https://proceedings.mlr.press/v139/radford21a.html ; original caveats https://openai.com/index/clip/
- Google Vertex AI multimodal embeddings model reference **contemporaneous platform**: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-embeddings . Check historical model/version and modality support before depicting API calls from 2024.
- NIST 2019 report, **Face Recognition Vendor Test: Demographic Effects**, https://doi.org/10.6028/NIST.IR.8280 ; overview https://www.nist.gov/news-events/news/2019/12/nist-study-evaluates-effects-race-age-sex-face-recognition-software . NIST evaluates face **recognition algorithms**, not this PyCon system; use it for general risk framing, not a claimed measurement of this embedding demo.
- Original movie-quote dataset: https://raw.githubusercontent.com/sanand0/actor-lookalikes/main/movie-quotes-catchphrases.csv ; original image materials listed at https://github.com/sanand0/actor-lookalikes
- Original project README in Plutonium checkout is stale (2024-08-14 commit); GitHub's current README links PyCon slides/slide-prompt. No synced Slide deck snapshot exists locally in Plutonium's `~/code/actor-lookalikes`.

## Falsification experiments for a later story

1. **Nearest neighbor stability:** rank the same person across several photos and alternate crops/backgrounds; show how much the top-k changes.
2. **Appearance vs association:** compare visually similar unassociated pairs against famous spouses with dissimilar looks using the exact same text/image embedding model, controlling for photo style and data leakage. Do **not** assume outcome in advance.
3. **Calibration:** compare similarity rankings to blinded independent human visual-similarity judgments, and check by demographic subgroup with informed consent where applicable.
4. **Classification pipeline:** hold out labeled client photo requirements, choose threshold on validation subset, report false positives/negatives and abstentions. This supports the **six-day anecdote** without pretending it is measured evidence.

**Unresolved:** precise slide deck contents (URL timed out), technical training of the 2024 Google multimodal model used, exact 2024 slider thresholds, accuracy of client pilot, unusual timeline of 'Claude 3.5 Haiku', and video frame timecode alignment. Do not make numbers up to fill these.

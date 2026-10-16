# Story context — Finding Actor Look-alikes with Multi-modal LLMs, PyCon India, 21 September 2024

**Source:** in-repo transcript (host + Anand + Q&A), the original PyCon 2024 schedule/CFP, the 2024 actor-lookalikes repository, its publicly available slide-generation prompt and original graphics. This is **the 30-minute PyCon talk**, not the 49-minute DataHack Summit talk on 8 August. The published conference recording appeared on 25 March 2025; the presentation itself is from **21 September 2024**, NIMHANS Convention Centre, Bengaluru.

## Premise

Anand doesn't really want another neural network lecture. He wants a stand-in for Irrfan Khan. A few years earlier his co-founder ruled out a speculative, expensive experiment in the middle of fundraising. By September 2024, pretrained models had made the bizarre request cheap enough to investigate — and **the most useful operation was neither a prompt nor a classifier, but a comparison of vectors**. Along the way, the same trick could cluster movie quotes, derive topics, reclassify them, search photos by words, and unexpectedly solve an enterprise pilot in days. A PyCon audience member's final question reveals the catch: **what exactly does 'similar' mean to the model?**

**Core line:** 'Once you can represent things in a common space, old-fashioned mathematics becomes a surprising AI superpower.' Critical second half: 'But the space encodes whatever the model learned, not necessarily the property you intended.'

## A four-beat story candidate

### 1. The problem no one approved

**00:33** Raise hands for Ranveer, Deepika, Shah Rukh, Alia; Anand would rather search for Irrfan Khan. He wants a specific visual likeness, not a cinematic replacement. **01:14–02:59** He pokes at models that are bad at uniform random numbers (Claude's 42, GPT-3.5's 47) and admits the early GPU economics were terrible. **02:59–03:31:** the remembered fundraising conversation with Naveen, ~$5,000 and two months — a vivid human moment, *not* a documented finance budget. Keep it light and avoid repeating the full LLM-psychology experiment already covered in ../2024-08-10-tedx-mdi-gurgaon/.

### 2. A new frontier makes the frivolous practical

**03:31–07:01** Historical frontier chart: crowd-ranked model performance against token price. Better and cheaper models appear one after another. This is a good **constraint curve**: as costs fall, the set of questions worth asking changes. **07:01–07:48** The quiet extra gain is embeddings: very low per-token cost and vectors that support repeated comparisons with no additional generation step. **07:48** Anand corrects his own initial belief about exact reproducibility after discovering a small number of embedding changes while teaching — good humility and a warning about using APIs as oracles.

Do not recite every 2024 model. Demonstrate what a moving cost frontier *does* to a budget decision. An interactive 'Can we afford to try it?' slider with **explicit hypothetical usage assumptions** is better than misusing the speech's $10k vs $4m analogy as a measured benchmark.

### 3. The reusable machine is a vector

**08:47–10:01** Anand writes a vanilla JS app with Claude and shows 'apple' encoded into ~1,536 numbers. A 2D dot drawing is an *illustration*; the actual embeddings are far higher-dimensional. **10:32:** even the reveal.js deck was generated using AI tools, an early lived example of software building getting cheaper, but keep this brief.

**11:22–12:53** ~150 movie quotes get embedded; unexpectedly 'It's showtime!' resembles 'It's clobbering time!', and 'They're here!' resembles 'They're back!'. This is the story's first **concrete visualization of a latent neighborhood**. **13:25–16:42:** cluster vectors with bisecting K-means, name ~15 clusters with GPT-4o Mini. It is not '100% embeddings': cluster naming uses generation. **17:14–18:25:** Anand deletes generic category labels, supplies a revised taxonomy, classifies new phrases by similarity, and explains the dot product. This is the deeper reusable idea: **the same stored vectors can support a changed question**.

Visual sequence could keep one small cloud of quotes fixed while the reader changes 'nearest', 'cluster', 'name' and 'classify'. On reload and without interactions the story should still make sense.

### 4. From quote to face to real value

**19:12–20:14:** Google multimodal embeddings place text and images in compatible vector spaces. Not every embedding model does this; it is model-specific. **20:32–21:27:** the photos plot against text axes 'smile' and 'frown'. The transcript starts by saying Bollywood actors but names Tom Holland, Meg Foster, Clint Eastwood and others; evidently the demo includes **Hollywood photos as well**. Don't label this a verified 100-person Bollywood-only corpus.

**21:27** The stage demo asks how 'Chinese' or 'African' a photo appears. Retelling it responsibly means noting how category words can pick up **appearance stereotypes** and embedding bias. It does **not** determine identity, ethnicity or nationality. Avoid replicating that specific interaction on a public website.

**22:01–23:35:** logistics client wants to flag duplicate/bad-background/incorrect-uniform driver photos. Anand says a team expected ~six months, client asked for a six-week pilot, and a working project was completed on **day six** using embedding similarity to descriptive prompts. A strong example of value changing from training a specialist model to **specifying checks against pretrained features**. Unverified: precision, recall, dataset size, deployment, consent and whether duplicate-person detection worked. Narrate as a reported pilot anecdote, not externally benchmarked result.

**23:35–26:22:** exploring nearest actor photographs leads from Shah Rukh to Varun Dhawan in the particular photos, Deepika to Priyanka Chopra, Ranveer to Vicky Kaushal, Alia to Katrina Kaif. The desired conclusion: **Irrfan Khan → Nana Patekar** in this one corpus/model/demo, with the speaker's acknowledgement nobody 'replaces' Irrfan's artistry. Do not fabricate similarity percentages or claim agreement beyond stage demonstration.

**27:30–29:11:** audience asks the *best test question*: might celebrity spouses be close because of associations in training rather than visual features? Anand says at 28:13 that he hasn't examined the training and doesn't know. This is the epistemic turn: **cosine closeness is easy to compute; what it reflects requires experiments**. Ending on the audience member is more honest and memorable than 'just use embeddings'. Follow with three falsification checks: different photos of same people; paired look-alike vs spouse non-look-alike; multiple embedding models.

### The reader's experiment

Invite them to pick an actor and see the 2024 model's nearest **photo** (if authentic ranked data can be recovered), then change the question to 'nearest by expression', 'nearest by clothing', or 'spouse semantic association' — different properties need different evaluations and perhaps different embedding models. Keep the layout lightweight, and don't solicit user-uploaded face photos by default.

## Key moments and evidence source

| Transcript time | Scene | Caution |
| --- | --- | --- |
| 00:00 | Host introduces Anand and LLM psychologist title | Event/era |
| 00:33 | Vote for Bollywood stars; Anand wants Irrfan | The through-line |
| 01:14–02:59 | Random 42/47 and reliability worry | Model-run historical settings |
| 02:59 | $5k / 2 months refused | Personal recollection |
| 03:31–05:46 | Elo-price Pareto chart | 2024 model names may be mistranscribed |
| 07:01–08:47 | Cheap embeddings, mostly reproducible | Don't claim permanent determinism |
| 08:47–10:32 | 'apple' vector in live app | ~1,536, high-dimensional |
| 11:22–12:53 | Movie quote neighbors and outliers | Similarity is approximate |
| 13:25–16:42 | Bisecting K-means and LLM topic naming | Naming is generation |
| 17:14–18:25 | Revised taxonomy via dot product | Normalize for cosine comparison |
| 19:12–20:32 | Shared text/image space | Not generic text + image embeddings |
| 20:32–21:27 | Smile/frown photo map | Appearance ≠ personal traits |
| 21:27 | Ethnicity word prompts | Sensitive inference and bias |
| 22:01–22:50 | Reported day-six logistics pilot | No audited performance result |
| 23:35–26:22 | Actor lookalikes; Irrfan → Nana | Dataset/photo specific |
| 26:50 | 'Cheap, quantitative, multimodal' | Marketing line needs boundaries |
| 27:30–28:13 | Spouse-vs-face challenge, 'I have no clue' | Ideal ending |
| 29:11–30:28 | Internal Foundry, LLM-coded visualizations | Not a public tool |

There is a transcript paragraph break at **19:59** and a host handoff at **27:22–27:30**. Cross-check that these align to the **PyCon recording** before adding page anchors.

## Real assets / website design opportunities

- Original project `llm-random.webp`, `llm-pricing.webp`, `llm-comparison.webp`, `embedding-pricing.webp`: authentic 2024 visual context; crop only with legible axis definitions.
- `embeddings.gif` and `embeddings.webp`: real dimensionality demo; pause animated graphics for reduced-motion.
- `quote-cluster.gif` and public catchphrase CSV: grouping/labeling discussion; respect short copyrighted movie excerpts.
- `hollywood-actors.webp`: source project's actor-embedding visual; label what the artifact actually shows, don't extrapolate celebrity identities beyond its captions.
- Actual PyCon reveal.js deck: linked at https://llmfoundry.straive.com/apps/actor-lookalikes.html; **timed out from Plutonium on 16 Oct 2026**. The public slide generation script at https://github.com/sanand0/actor-lookalikes/blob/main/slide-prompt.md is a strong fallback for slide order, **not evidence of exactly what appeared on screen**.
- Video at https://youtu.be/FHa8Xgssrz4 is the recording; don't confuse it with the 49-minute DataHack Summit session https://youtu.be/a6_tygjxxUc.
- **Planned media at build time:** Anand will have supplied `comic-page.avif` and an Opus recording in this directory. Feature the actual comic and add an audio option with an individually verified filename/public URL; neither changes which PyCon video is embedded.

## Editorial QA

- **Name/era:** 21 Sep 2024, PyCon India Track 1, 14:45–15:15 according to original published schedule. YouTube publication date in March 2025 does not change event date.
- **Transcript mismatch:** 'Claude 3.5 Haiku' at 05:46 is unlikely for Sep 2024 (model announced afterward). Video/slide must settle exact words.
- **Similarity claims:** never publish as a validated face matcher or a measured 'most alike' global rank; define candidate set and exact source photographs.
- **Ethics:** celebrity public photos used as historical stage screenshots; avoid new biometric matching tools, ethnicity scores, hiring/driver identification and unconsented upload flows.
- **Cost:** put 2024 prices next to original graphs; never imply current cost.
- **Follow-up:** test spouse/appearance hypothesis and model/photo stability before claiming the shared space captures pure visual resemblance.
- **Publishing:** retain archive entry, don't change catalog title to the creative story title until a human intentionally decides; add page/transcript only after article exists.

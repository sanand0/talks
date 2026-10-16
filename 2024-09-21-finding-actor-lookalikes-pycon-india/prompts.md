# Prompts — PyCon India, 21 September 2024: Finding Actor Look-alikes with Multi-modal LLMs

<!-- ChatGPT Prompt source: https://chatgpt.com/c/6ad186a1-5e70-83ec-b1df-1a159bf567ce -->
<!-- Comic page: https://chatgpt.com/c/6ad19f99-8408-83ec-bca2-7ade308f1bfc -->

<!--
cd ~/code/talks
dev.sh -p ~/code:ro,~/r2/media:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Create an ambitious, lucid, playful **evidence-grounded video-first story** at `2024-09-21-finding-actor-lookalikes-pycon-india/index.html` from Anand's PyCon India 2024 talk. The surface question is irresistibly human — **who looks like Irrfan Khan?** — but the answer becomes a step-change in applied AI: *a problem we would once have trained a bespoke model to solve becomes a search in a shared vector space*. Make readers experience that pivot without treating a nearest-neighbor result as identity, beauty, racial origin, or a scientifically verified look-alike.

Use **talk-story**, **data-story**, **interactive-storytelling**, **evidence-provenance**, and webapp-testing skills as relevant. Study the finished 2015 TEDx NMIMS and 2024 TEDx MDI Gurgaon HTML plus October 2026 stories: reuse **story ↔ video focus, persistent YouTube player, timestamp seek/play, URL history/deep links, readable transcript, responsive and accessible interaction**. Do not imitate their palette or a fixed card count.

## Source of truth and provenance

1. **transcript.md**, including host Q&A, covers **00:00–30:28**. The spoken talk ends near 27:20; questions on spouse similarity and code generation extend to ~30:28. The transcript contains errors and historical assumptions; use video for uncertain words/demos.
2. **story-context.md** gives story arc, playable timestamp map, demo details, ethical traps, reader experiments and counterarguments. It is a research companion, not a script.
3. **research-notes.md** documents source checks, limitations of generic multimodal embeddings and important model-timeline inconsistencies to verify on video.
4. **links.md** includes the ORIGINAL talk, PyCon CFP, schedule, slide deck and exact 2024 open-source project links.
5. **Only source recording for this event:** https://youtu.be/FHa8Xgssrz4 by **Python India**, recorded **21 Sep 2024** at NIMHANS Convention Centre, Bengaluru and published in **March 2025**. Use this **30–31 min version**, YouTube ID `FHa8Xgssrz4`. **Do not use** https://youtu.be/a6_tygjxxUc, which is the **different 49-minute DataHack Summit 8 Aug 2024** session despite the shared topic. Do not fabricate/download/use a non-existent WebM.
6. **Original PyCon slide deck:** https://llmfoundry.straive.com/apps/actor-lookalikes.html linked from https://github.com/sanand0/actor-lookalikes/blob/main/README.md ; Original [slide-generation prompt](https://github.com/sanand0/actor-lookalikes/blob/main/slide-prompt.md) is public and lists slide narrative, charts, and images. Use video frames to inspect/preserve original slide images if deck remains unavailable. Don't call the 8 Aug *Talk Assistant GPT* slides the same deck.
7. **Project source:** https://github.com/sanand0/actor-lookalikes ; images (llm-random.webp, llm-pricing.webp, llm-comparison.webp, embedding-pricing.webp, embeddings.gif/webp, quote-cluster.gif, hollywood-actors.webp) are also in `~/code/actor-lookalikes`. You may reuse original artwork from this repo with source captions. Its checkout may be older — use GitHub's current public version when needed.
8. **Comic and audio will be present when this prompt runs:** expect **`comic-page.avif`** and an **Opus `.opus` recording** in this talk directory. Show the actual comic prominently near the beginning with descriptive alt text and accessible full-size/lightbox viewing; add an **HTML comment** citing its generation conversation if provenance is supplied, never a made-up citation. Inspect the actual Opus filename and include a useful audio-listening/download option; link to a public GitHub Releases URL **only after verifying it exists**. Treat the Opus recording as **audio only** — the **sole embedded video** remains the original PyCon YouTube `FHa8Xgssrz4`. If either expected file is unexpectedly missing on build day, report it, rather than quietly skipping it.

## The intellectual pivot — one story, not five lectures

**Best potential cold open: [26:22]** The question Anand carried since around 2021 — who might resemble Irrfan Khan? — yields **Nana Patekar**, *in this particular photo collection*. The room laughs, but the technical surprise is **what he didn't need to build**. Instead of starting with face recognition, rewind to [02:59], where an expensive AI experiment seems frivolous during fundraising.

Earn the payoff along one causal sequence:

- **The question that seemed too expensive (00:33–03:31).** Audience votes for Shah Rukh Khan; Anand wants an Irrfan lookalike. He quotes a co-founder's refusal of an expensive experiment. Early LLMs are quirky, with nonuniform 'random numbers', and GPU time is pricey. Keep this short: *random-number psychology* is already its own TEDx MDI story. This time, the weakness sets a constraint.
- **The price collapse creates permission (03:31–07:48).** A historical price-vs-Chatbot-Arena rating Pareto frontier changes dramatically. The bigger revelation is **embeddings cost even less** than generation. Pin all dollar/model data to *September 2024*; not today's pricing. Don't treat Elo as universal 'quality' or a scatterplot as proof a $4m company budget became $10k in a measured project.
- **Meaning becomes geometry (07:48–19:59).** 'Apple' becomes ~1,536 numbers. Nearby semantic vectors form neighborhoods. About 150 movie quotes become similarity pairs, clusters, named topics and a user-edited taxonomy. An ordinary dot product makes classification cheap. Show how the steps connect: **encode once → compare repeatedly → group → label → edit categories → classify**. 'Embeddings' is not a buzzword but a reusable interface between unstructured artifacts and ordinary numerical tools.
- **The same trick meets photographs (19:12–26:50).** A *specific multimodal model* puts photos and text into a compatible space; the demonstration positions portraits along 'smile'/'frown' axes, then retrieves lookalike photos. A logistics client with driver photo validation needs a fast pilot; according to Anand, a planned six-month project has a working result by the **sixth day**. Label this explicitly a **speaker anecdote**, without invented metrics or proof of production robustness. The closing Irrfan/Nana answer pays off the opening.
- **The perfect coda (27:30–30:28).** Audience member asks whether an embedding of a celebrity's face might reflect the celebrity's spouse rather than just appearance. Anand says **'I have no clue'** about the model training and proposes a test. That honest unknown is the real climax: a vector is a measurement, and **we need to know what property it is actually measuring**.

Possible headline: **'The Actor Look-alike That Didn't Need an AI Model'** is technically ambiguous because the method **uses a pretrained AI model**. Prefer *'He Wanted an Irrfan Khan Look-alike. The Trick Was a Dot Product.'* or something better that clearly avoids 'no model'. End with a small **experiment that could disprove the result**, not a grandiose claim that all AI training is over.

## Let readers feel the geometry

Choose 2–3 purposeful interactions with truthful reference data:
- **Build a semantic neighborhood** using a tiny labeled **illustrative** 2D projection of the 2024 movie-quote examples. Reader chooses nearest neighbors or moves a threshold; explain cosine similarity and how embeddings are usually high-dimensional.
- **Cluster → name → retaxonomize:** use the original catchphrase CSV or explicitly labeled reduced fixture, compute nearest centroid/dot products in-browser with a known static embedding if available. Don't call a manually authored affinity matrix actual 2024 API results. Let 'It's showtime!' / 'It's clobbering time!' be amusing counterexamples: proximity is useful, not perfect comprehension.
- **Photo similarity audition:** a curated set of authentic *source project* actor photos if usage rights allow, with a slider that ranks by documented demo results rather than inventing scores. Emphasize **photo-level** similarity, not the people themselves. Show the 'Varun Dhawan appears near Shah Rukh' and 'Nana Patekar near Irrfan' as *what the 2024 demo displayed*, not certified facial resemblance.
- **Same-space cross-modal query** with 'smile' vs 'frown' and an optional adjective. Add a crucial thought experiment about **dataset bias** and the mismatch between background/pose/expression, appearance and semantic associations.

Original asset preference: `~/code/actor-lookalikes/llm-random.webp`, `llm-pricing.webp`, `embedding-pricing.webp`, `embeddings.gif`, `quote-cluster.gif`, `hollywood-actors.webp`, plus YouTube stills, with source credit. Choose a few legible visuals, not a gallery. Don't derive perceived ethnicity/nationality/beauty or infer protected traits from faces. The 2024 demo uses such prompts at ~21:27; put this into a **critical explanatory note**, not a live discriminatory interactive classifier.

## Do not paper over limitations

- **Similarity is conditional on model, text prompt, photo, preprocessing and candidate set**, not universal physical resemblance. The talk's prototype sometimes uses multiple photos per actor; a photo of the same actor may be nearest. No identity verification accuracy or fairness benchmark is offered.
- **Cross-modal embeddings must be co-trained / model-compatible**. A generic text embedding and generic image embedding cannot automatically be directly compared.
- **Dot product vs cosine similarity**: they coincide as rankings when vectors are normalized; show norms or normalization rather than declaring every dot product a distance.
- **Embedding repeatability**: transcript ~07:48 mentions a 2% case where a presumed stable vector changed and students received full marks. Attribute an anecdote; provider/model/preprocessing and caching matter. Don't promise strict byte-identical outputs forever.
- **K-means and LLM labels** are convenient exploratory heuristics, not ground-truth topics. Evaluate cluster stability, human label agreement, multilingual prompts, outliers and thresholds.
- **Chronology error to verify**: transcript **05:46** says '**Claude 3.5 Haiku**' preceding September 2024; that model was announced after September 2024. Check audio/slides; likely speech-to-text confusion with '**Claude 3 Haiku**'. Never assert an unreleased model as historical evidence.
- **Security and bias**: don't use similarity scores for hiring, identity authentication, protected-attribute sorting, or sensitive demographic claims. Evaluate demographic effects and consent before any real facial matching. The client story concerns image requirements, not an audited identity checker.
- **Private service:** LLM Foundry is an internal tool. Screenshots from 2024 don't authorize using its private API, exposing credentials or pretending the service is public.
- **Version discipline:** GPT-3.5 Turbo, Claude 3 Haiku, GPT-4o Mini, Gemini 1.5 Flash, o1-preview and pricing are all 2024 references. A live demo today is **not** the original experiment.

## Site behavior and publication rule

The polished **story leads**. Provide one persistent **YouTube IFrame Player** that keeps position when toggling story/video; timestamp cues (e.g. ▶ 00:33, ▶ 07:01, ▶ 11:22, ▶ 19:59, ▶ 22:01, ▶ 26:22, ▶ 27:30) seek/play and survive deep links and browser history. Check actual offsets at 00:00 host intro; **do not autoplay on initial load**. Feature the supplied `comic-page.avif` near the top, the verified Opus audio option, accessible transcript, original sources, large image viewing, semantic labels, keyboard/mobile/reduced motion and working interactive explanations. Smoke test real play/seek, scrolling, browser back, visual changes, links and errors.

**Current deliverable is prompts/context/research/links**, not the finished page. When page has been built and tested, update only the **existing 2024-09-21 entry** in config.json, retaining title **Finding Actor Look-alikes**, event PyCon India, date **21 Sep 2024**, official video URL, slides link, code link, archive category. Add page, transcript, comic metadata and a **verified** Opus audio link (without treating it as an alternative video). Run `node generate.mjs` to update the README; do not append a duplicate catalog entry or inadvertently change the *8 Aug DataHack Summit* entry. Report deck access gap and any contradictory media timestamps rather than inventing fixes.

---

Remove any files / code not required for the final story. Compress all .webp images maximally as long as they're visually good enough - including images from2017-11-19-tedx-whitefield

---

Also update ../config.json - it may have been overwritten

---

How come when I load the home page, "21 Sep 2024. Finding Actor Look-alikes at PyCon India, 2024." does not have a link on "Finding Actor Look-alikes" pointing to 2024-09-21-finding-actor-lookalikes-pycon-india/?

<!-- claude --resume 8009d9b9-1190-4121-8989-5e88b4e015d5 -->

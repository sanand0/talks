---
marp: true
title: LLM Trends
author: Anand S
url: https://sanand0.github.io/talks/2025-09-22-llm-trends/
theme: gaia
paginate: true
backgroundColor: #fff

# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
---

<style>
  aside {
    position: absolute;
    top: 150px;
    right: 30px;
    max-width: 500px;
  }

</style>

# LLM Trends

22 Sep 2025, 5:00 pm IST · Chennai
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Transcript](https://github.com/sanand0/talks/blob/main/2025-09-22-llm-trends/transcript.md) · [CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-22-llm-trends/)

---

## LLM are getting better **and** cheaper

[![h:475](../2025-07-13-goodbye-mba-hello-ai/pricing.webp)](https://sanand0.github.io/llmpricing/)

<aside style="max-width:300px" data-marpit-fragment>

**Plan for _future_ capability**.

Quality enables **new use cases**.

Cost unlocks **higher scale**.

</aside>

---

## LLM context windows are increasing

[![h:500](https://cdn.prod.website-files.com/66efe12cea125ae2bb1471da/680a244002ab2f063f3a9108_llm_context_window_evolution.png)](https://www.meibel.ai/post/understanding-the-impact-of-increasing-llm-context-windows)

<aside style="max-width:300px" data-marpit-fragment>

#### Implications

- **Longer docs**. Process entire books, manuals.
- **More memory**. Remember past interactions.

</aside>

---

## So policy documents can **be** the code / rules

[![h:500](policy-as-code.webp)](https://sanand0.github.io/policyascode/)

<aside style="max-width:450px" data-marpit-fragment>

#### Implications

- **Guidelines are executable checks**. No manual back-and-forth.
- **Regulatory rules are evals**. Apply directly.
- **Emails become policies**. Common law emerges.

</aside>

---

## LLMs read & write with more attention

[![h:500](https://images.ctfassets.net/kftzwdyauwt9/2oTJ2p3iGsEPnBrYeNhxbb/9d14d937dc6004da8a49561af01b6781/OpenAI-MRCR_accuracy_2needle_Lightmode.svg)](https://openai.com/index/gpt-4-1/)

<aside style="max-width:600px" data-marpit-fragment>

#### Implications

- **Better code**. Fewer errors,
  longer output.
- **More structure**. JSON, XML follow schema diligently.
- **Self-correction**. Better at spotting own errors.
- **More reasoning**. Chain-of-thought, tree-of-thought.

</aside>

---

## **Dynamic code** is a new modality

**Demos**:

- [Topic Trends](https://sanand0.github.io/topictrends/): an AI-coded app that shows trends in documents (design-to-deploy in 2 hours).
- [SchemaForge](https://prudhvi1709.github.io/schemaforge/): automate data engineering; schema + DBT tests
- [HypoForge](https://sanand0.github.io/hypoforge/): automate data science; generate + test hypotheses
- [DataGen](https://nitin399-maker.github.io/datagen/): automating synthetic data generation for stress testing

---

## LLMs think for longer without errors

[![h:500](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/deesrjitvXM4xYGZd/e6bm1rfz9dazzub1lupj)](https://www.lesswrong.com/posts/deesrjitvXM4xYGZd/metr-measuring-ai-ability-to-complete-long-tasks)

<aside style="max-width:300px" data-marpit-fragment>

#### Implications

- **Autonomy**. Agents, self-correction.
- **Creativity**. Complex ideation.

</aside>

---

## This lets us automate **innovation**

[![h:500](ideator.webp)](https://tools.s-anand.net/ideator/)

<aside style="max-width:475px" data-marpit-fragment>

**Innovation = combinatorics**

Combine 2 random ideas into new creative initiatives towards a specific purpose.

</aside>

---

## LLMs evaluate LLMs as well as humans

[![h:500](https://miro.medium.com/v2/resize:fit:720/format:webp/1*7s9ESqBz4pJaP1_r4bahlA.png)](https://medium.com/@techsachin/replacing-judges-with-juries-llm-generation-evaluations-with-panel-of-llm-evaluators-d1e77dfb521e)

<aside style="max-width:500px" data-marpit-fragment>

#### Implications

- **Better quality**. Multiple LLMs reduce errors.
- **Scalable quality**. Humans assess exceptions.
- **Continuous improvement**. Always-on evals based on feedback.

</aside>

---

## So we can evaluate quality at scale

- [Double-checking](https://sanand0.github.io/llmevals/double-checking/). Using multiple LLMs-as-a-judge with consensus reduces hallucinations dramatically
- [Prompt effectiveness](https://sanand0.github.io/llmevals/emotion-prompts/). Using an LLM-as-a-judge automation framework systematically highlights effective prompts
- [Prompt improvements](https://sanand0.github.io/promptevals/). Use LLMs to write _and_ improve prompts by evaluating the effectiveness of each

---

## LLMs are far more multi-modal

[![h:500](https://epoch.ai/assets/images/posts/2023/how-predictable-is-language-model-benchmark-performance/egraphs/mmlu.png)](https://epoch.ai/blog/how-predictable-is-language-model-benchmark-performance)

<aside style="max-width:350px" data-marpit-fragment>

#### Input/Output Formats

- Audio
- Image
- Video
- DSLs (3D, CML, ...)

</aside>

---

## That lets us generate far more than text

- [Subtitle generation](https://prudhvi1709.github.io/subtitlegen/). Generate subtitles across languages on the fly.
- [3D object](https://nitin399-maker.github.io/3dobjectgen/) and [3D image](https://nitin399-maker.github.io/3dimagegen/) generation. Illustrate and visually prototype technical concepts from sketches.
- [Podcast generation](https://tools.s-anand.net/podcast/). Repurpose content in audio formats.
- [Storybook generation](https://tools.s-anand.net/picbook/). Repurpose content in visual formats.

<!--

Additional demos

  - Personagen: Synthetic customer persona creation + surveying.

-->

---

# LLM Trends

22 Sep 2025, 5:00 pm IST · Chennai
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Transcript](https://github.com/sanand0/talks/blob/main/2025-09-22-llm-trends/transcript.md) · [CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-22-llm-trends/)

---

## Quiz

1. What’s the _key_ difference between prompt caching and normal caching in LLM APIs?
2. Why can long context windows still miss relevant info (“lost in the middle”) and how would you mitigate it?
3. In this workflow, where should analysis run on _full_ data and where is sampling OK?
4. When is “LLM-as-judge” reliable, and what biases should you watch for?
5. Name two reasons code sandboxes avoid direct internet access and how to work around it.

---

## Errata

<small>

- **Prompt caching ≠ a “tiny copy of the model.”** It stores/charges cached _prompt segments_ to speed/cheaply reuse, without changing the model. ([Medium][1])
- **Advanced Data Analysis (code interpreter) has no open internet.** Browsing is a _separate_ tool; the sandbox itself blocks external calls. ([OpenAI][2])
- **“LLMs evaluate LLMs as well as humans” — nuanced.** LLM judges correlate with humans but show biases; human calibration still needed. ([16x Prompt][3])
- **Context window ≠ long-term memory.** Bigger windows allow longer _inputs_, but retrieval can _drop_ for middle content. App “memory” is separate. ([ar5iv][4])
- **“Gemini is free & good at photos/video/audio.”** There is a free web app; advanced multimodal features are via Gemini 1.5/API tiers. ([OpenAI][5])
- **“Whisper is behind ChatGPT voice.”** OpenAI documents Whisper as its speech-to-text used in ChatGPT voice features. ([OpenAI][6])
- **“LLMs are getting cheaper” — evidence.** Example prices (per 1M tokens): GPT-4o \$5 in/\$15 out (May 2024); vendors have introduced price cuts/cheaper tiers. ([arXiv][7])
- **Model capabilities & windows.** Current public windows: Gemini 1.5 up to 1M; Claude 3.7 Sonnet 200k; OpenAI o-series context sizes are model-specific. ([Claude Docs][8])

</small>

---

## Counterpoints

<small>

- **“LLM context windows are increasing” → But…** Longer windows can _hurt_ recall; retrieval/RAG or windowing often beats naive full-context dumps. Consider chunk-and-vote or salient-first prompts. ([ar5iv][4])
- **“LLM-as-judge scales quality” → But…** Judges show systematic biases (position, verbosity, self-enhancement). Use blinded, shuffled, multi-judge panels + human spot-checks and gold standards. ([16x Prompt][3])
- **“More structure (JSON/XML) now” → But…** Plain “JSON mode” is not bullet-proof. Prefer _structured outputs/function calling_ with schemas for reliability. ([OpenAI][9])
- **“Far more multimodal” → But…** Vision-language models still hallucinate objects and captions. Keep human-in-the-loop for safety-critical use. ([ACL Anthology][10])
- **“Policy docs can be the code/rules” → But…** Governance needs documented controls. Follow NIST AI RMF (Govern/Map/Measure/Manage) when automating compliance. ([NIST AI Resource Center][11])
- **“LLMs think for longer without errors” → But…** Long-horizon agency is far from solved; MAUD/METR find persistent failures on multi-step tasks. Use decomposition & verifiable subgoals. ([Vals AI][12])

</small>

---

## Feedback

<small>

1. **Label claims vs. opinions.** Add “Claim/Why/Limitations” badges on slides with bold assertions (e.g., LLM-as-judge, policy-as-code).
2. **Show the _why_ behind choices.** One slide comparing _ChatGPT/Claude/Gemini/Jules/Codex_ by task (EDA, front-end, agents, cost), with 1-line rationale each.
3. **Make failure modes visible.** Add a “Bugs I expect” checklist (net-blocked sandbox, path issues, file limits) and the quickest CLI/browser fixes.
4. **Quantify effects.** When stating “longer books rate higher,” show effect sizes + CI, then the same chart _after_ outlier clipping.
5. **Tighten the demo loop.** Pre-bake a tiny dataset and a repo branch that always builds; live-switch to bigger data only if time permits.

</small>

[1]: https://medium.com/data-science/4-ways-you-cant-use-the-chatgpt-code-interpreter-that-will-disrupt-your-analytics-c31d29034b69?utm_source=chatgpt.com "4 Ways You Can't Use the ChatGPT Code Interpreter That ..."
[2]: https://openai.com/index/chatgpt-plugins/?utm_source=chatgpt.com "ChatGPT plugins"
[3]: https://prompt.16x.engineer/blog/claude-sonnet-gpt4-context-window-token-limit?utm_source=chatgpt.com "Claude 3.5 Sonnet vs GPT-4o: Context Window and Token Limit"
[4]: https://ar5iv.labs.arxiv.org/html/2307.03172?utm_source=chatgpt.com "Lost in the Middle: How Language Models Use Long Contexts"
[5]: https://openai.com/index/hello-gpt-4o/?utm_source=chatgpt.com "Hello GPT-4o"
[6]: https://openai.com/chatgpt/pricing/?utm_source=chatgpt.com "Pricing - ChatGPT - OpenAI"
[7]: https://arxiv.org/html/2406.18403v3?utm_source=chatgpt.com "LLMs instead of Human Judges? A Large Scale Empirical ..."
[8]: https://docs.anthropic.com/en/docs/build-with-claude/context-windows?utm_source=chatgpt.com "Context windows - Anthropic API"
[9]: https://openai.com/index/introducing-structured-outputs-in-the-api/?utm_source=chatgpt.com "Introducing Structured Outputs in the API"
[10]: https://aclanthology.org/2024.findings-acl.414.pdf?utm_source=chatgpt.com "Logical Closed Loop: Uncovering Object Hallucinations in ..."
[11]: https://airc.nist.gov/airmf-resources/playbook/?utm_source=chatgpt.com "Playbook - AIRC - NIST AI Resource Center"
[12]: https://www.vals.ai/models/anthropic_claude-3-5-sonnet-20241022?utm_source=chatgpt.com "Claude 3.5 Sonnet Latest"

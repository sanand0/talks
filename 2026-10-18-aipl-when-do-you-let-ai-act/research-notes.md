# Research and fact-check notes — AIPL Session 1 (18 Oct 2026)

**Checked 19 Oct 2026.** This is an **evidence shelf for Claude Code**, not an article, a mandated outline, a list of visual components, or an invitation to quote all the studies. Use a handful of the strongest grounded comparisons. **What happened**: transcript/audio/Zoom chat. **What numbers mean**: source datasets/papers and their evaluation protocols. **What might be a better interpretation**: editorial judgment, identified as such.

## Fact checks that materially change the story

### What the "jagged frontier" research really established

- In the session [36:16–42:11], Anand uses the idea that AI is unevenly useful and progress is not uniform by task. The classic primary study is **Dell'Acqua et al., "Navigating the Jagged Technological Frontier"** ([Organization Science, 11 Mar 2026](https://doi.org/10.1287/orsc.2025.21838); [working paper](https://doi.org/10.2139/ssrn.4573321)). The preregistered field experiment involved **758 BCG knowledge workers**. On tasks *inside* the experimentally assessed GPT-4 capability frontier, AI users completed **12.2% more tasks** in **25.1% less time** on average. On a complex task *outside* that frontier, AI users were **19% less likely to produce correct solutions** than non-AI users. This is task- and **2023-model-specific**, not 2026 general model performance; its compelling lesson is that a plausible adjacent task may be much less reliable. Helpful independent context, **not shown live**.
- Participants' examples of ABAP, Workday, diagramming, meeting scheduling and file research demonstrate *perceived* boundaries and differences in individual experience; they are **not objective experiments** showing those tasks are possible/impossible.

### GDPval measures an expert-judged deliverable, NOT autonomous business action

- [Original GDPval announcement, **25 Sep 2025**](https://openai.com/index/gdpval/). Dataset built from **44 occupations across 9 industries**, with **30 reviewed tasks per occupation** and a **5-task gold subset per occupation** (**220 gold tasks**). Experts compared AI- and human-produced work products blindly. The grading includes a "better/as good as/worse" comparison to work produced by task writers. Some claims of "beats humans" count *wins and ties*; insist on precise numerator/metric.
- GDPval's 2025 evaluation was **one-shot** rather than an interactive, multi-step, tool-integrated deployment. It does not directly measure correctness of autonomous payment, privacy, misuse, liability, organizational adoption or approval. The source's "100x faster/cheaper" figure concerns API inference cost/time, **excluding review, integration and iteration**. The talk [42:11–45:29] uses a visually compelling occupation map, but do not reinterpret it as proof that "AI can replace an occupation" or confidently delegate regulated decisions.
- The talk compares model capability with school and professor levels using the [LLM Pricing scatter](https://sanand0.github.io/llmpricing/) [12:56–17:49]. These education labels and "a thousand professors in our pockets" are **illustrative mappings of a benchmark/intelligence score**, not measured equivalence to a particular human degree or professional license. Prices are model/version/benchmark-date dependent. If displaying numeric price trajectories, inspect source data and label the x-axis (input tokens vs blended costs). Don't generalize exact October 2026 rankings beyond that date.

### Five-model agreement: useful, narrow, and not "99.3% of all work"

- Primary source [Double Checking Hallucinations](https://sanand0.github.io/llmevals/double-checking/) and local project `~/code/llmevals/double-checking/`. These are **observed classification** results, not a theoretical formula:
  
  | Models checked | Sent for manual review | Error among accepted / automated outputs |
  | ---: | ---: | ---: |
  | 1 | 0% | 14.1% |
  | 2 | 12.6% | 3.7% |
  | 3 | 18.5% | 2.2% |
  | 4 | 23.0% | 1.5% |
  | 5 | 28.1% | 0.7% |

  The session rounds to 14%, 3.7%, 0.7%, 28%. **A five-model procedure does not classify the 28.1% routed to review without human help**; report 0.7% as the *accepted-case error*, not universal deployment error or overall end-to-end accuracy after unspecified human decisions. Human effort percentage measures **fraction of cases reviewed**, not necessarily **percentage of staff time saved** (cases can differ in review difficulty). Added model cost "~2% of a person" is an anecdotal comparison [82:07] and not supported here by detailed assumptions.
- Selection and correlation matter. Agreement is strongest evidence when errors are genuinely diverse; shared training, correlated failure modes, wrong prompts, distribution shift or common information defects can make five agreeing systems wrong. Auditing agreement-only outputs remains worthwhile. A human maker-checker analogy can explain the *technique*, not establish human-level guarantees.
- **Counterpoint to dramatize, if useful**: 21/33 workshop respondents wanted to review cases where an error would cost most; model disagreement identifies **uncertainty**, not **harm**. One possible review priority is **predicted failure probability × loss on failure**, plus mandatory policy/rights/privacy safeguards. This is an *editorial recommendation*, not a formula the class evaluated.

### Simplification experiment: strong anecdote, small and model-dependent

- Anand's published [Simple Writing Hurts Thinking, **1 Aug 2026**](https://www.s-anand.net/blog/simple-writing-hurts-thinking/) tested **six tasks** on **GPT-5.6 Sol**, each with and without an ASD-STE100 instruction. Same model family evaluated paired responses in **both presentation orders** to reduce position bias. The majority of rubric comparisons favored the ordinary prompt; some dimensions/ties differed. The underlying evaluation is small, partly subjective, and judged by an LLM from the **same model family**, not a blinded external human gold set.
- The results do **not prove** plain language makes every model reason worse. The practical suggestion to simplify **after** solving the substantive problem is sensible but is *not demonstrated by a full controlled third arm* in this six-task comparison. Label it advice/an inference. Live discussion at [84:07–87:35].

### InsurLE's origin: transcript calls it Cambridge, but source is Imperial

- At [87:35–92:36], Anand demonstrates [InsurLE Demo](https://mynkpdr.github.io/insurle-demo/) ([demo source repository](https://github.com/mynkpdr/insurle-demo)), and describes the language as coming from Cambridge. **Independent provenance differs.**
- Source: [Imperial College institutional record, "Computable contracts for insurance: establishing an insurance-specific controlled natural language — InsurLE"](https://spiral.imperial.ac.uk/entities/publication/1c3e708b-889f-4d92-ba8f-be2667f535a2), by **John Cummins, Jacinto Dávila, Robert Kowalski and David Ovenden**; see also [Kowalski's Imperial College publication list](https://www.doc.ic.ac.uk/~rak/). InsurLE extends **Logical English**, drawing on logic-programming/Prolog. Don't call this a Cambridge research result just because the speaker did. "An insurance logic language grounded in formal work associated with Imperial College London" is safer. If appropriate, gently acknowledge the mismatch.
- Crucial conceptual issue: formalizing a contract **does not prove that its formal rules preserve every clause, exception, interpretation or governing law**. The original paper identifies the semantics-equivalence problem as a motivation. A well-tested executable representation can still be an incorrect translation of the original contract.

### Policy as Code demo is separate from the InsurLE academic language

- [Policy as Code](https://sanand0.github.io/policyascode/) ([source](https://github.com/sanand0/policyascode)) is an **AI-powered implementation** that extracts atomic, testable rules from policies and validates documents against them. It is an interesting **local demo**, not an independent validation or commercial success claim.
- The pivotal distinction is between **extraction correctness** (did the agent interpret the source rule?) and **execution correctness** (does the rule engine evaluate its own representation consistently?). Executable tests are valuable, but neither alone proves the policy's meaning was faithfully captured. Appropriate spot checks for false negatives, exceptions, contradictory clauses and disputed interpretations remain necessary.

## A broader issue the students raised: trust in action and trust in data

At [50:19] Mukul asks about explanation and trust; at [52:15–55:34] Ram raises deepfakes, misuse, privacy, power and who receives the data. The reliable response **must distinguish**:
- **Model output correctness** (accuracy/errors under an evaluated distribution);
- **Operational authority** (what side effects can be triggered, by whom, with what limits and reversibility);
- **Data protection** (permissions, retention, misuse, confidentiality and accountability);
- **Human reliance** (does a person actually accept appropriate advice and reject wrong advice?).

Independent [NIST AI Risk Management Framework (AI RMF) 1.0 and Generative AI Profile, NIST AI 600-1 (26 Jul 2024)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) identifies trustworthiness concerns including privacy, safety, security, reliability and accountability and recommends governing, mapping, measuring and managing risks **through the lifecycle**. It is **voluntary guidance**, not a seal that a specific system is safe.

Optional more specific research lens: [Cao, Liu and Huang, "Designing for Appropriate Reliance", 2024](https://arxiv.org/abs/2401.05612) finds in a particular high-stakes decision setting that calibrated uncertainty alone isn't sufficient for appropriate reliance and that presentation format matters. This is **not** a direct experiment on the AIPL audience. Better question than generic "Do you trust AI?": "In which cases does the combination of AI and human check actually improve decisions?"

## What not to infer from the live workshop

- The planned same-case breakout with *different evidence packets followed by common hidden test results* did **not happen**. In the audio at [98:37–102:53] groups receive instructions to choose one real business task and ways to make AI autonomous. The compiled transcript then **skips over most of the breakout period**; at [103:39–107:53] proposals are skimmed. The 10/11 group counts mentioned live are **not** the same as survey respondent counts.
- **Nondeterministic silence ≠ lack of learning.** The opening question was simple and students were still joining, while Q5 required an explanation after nearly an hour and there were technical/access questions in chat. There is no matched before/after learning measure. The pre-session input from 56 respondents and final live form data from 35 unique accounts refer to **different samples**.
- The speaker's live self-diagnosis [74:30] is an *observation/hypothesis*. The private ChatGPT answer proposes design adaptations; they are **not evaluated improvements shown to work**.
- The final "log 10 moments when you want to stop" [111:48–112:23] is a **proposed N=1 experiment**, not a proven stopping policy. Its strength is admitting uncertainty and making the next question testable.

## Additional source pointers

- Session's `links.md` is authoritative about shown/unshown tabs and public demo locations.
- `~/code/liveform-data/aipl2026/form.yaml` gives exact question wording/assignment logic. Do not upload `responses.tsv` or Zoom chat.
- `~/code/talks/2026-10-01-use-ai-emperically/{prompts.md,story-context.md,index.html}` is the best recent **audio-only** precedent.
- `~/code/talks/2026-10-07-iitm-ed-data-visualization/` is the best **timestamp-seekability** precedent, but its video-specific controls are not relevant to an audio-only session.

## Editorial verification checklist for Claude

1. Trace critical claims/quotes to the **audio/actual survey/public primary source**, not this file alone.
2. Separate participant's statement, speaker's test, author's follow-up inference and independent external research in the prose.
3. Check sample sizes for each chart. The survey is people rather than submission rows; no fabricated experiment significance.
4. Be willing to cut a delightful finding if the evidence is weak. Use the awkward Q5 delay to ask a real question, not to ridicule the class.
5. Distinguish "I said this" from "this is true." Watch especially: **Cambridge/Imperial, 95% trust scenario, GDPval occupational conclusions, model-cost analogies, human review savings, policy rule fidelity**.
6. Keep public links public, preserve privacy of speaker and participants, and do not publish private preparation-chat URLs.
7. External studies enrich context; don't falsely imply they were covered in the live talk.

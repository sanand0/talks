# Research and fact-check ledger — 12 October 2026 TDS course ideation

Researched 13 October 2026 from the meeting transcript, public course, local exam/course documentation, and primary research. This is a **working evidence shelf for the public story**, not a claim that the ideas discussed were adopted or validated. Date citations when possible. For contested claims, say what supports them, what contradicts them and how to test them. Quotations from the recording must be checked against the audio (and must not be conflated with quotations from papers).

## The key distinction: assisted performance is not durable learning

**Supported: authentic, active work can teach.** [Freeman et al., PNAS 2014](https://doi.org/10.1073/pnas.1319030111) pooled 225 undergraduate STEM studies and found active-learning interventions improved exam performance and lowered failure rates relative to lecture-oriented instruction. This supports the *direction* of exam-as-learning. It does not establish that the specific TDS projects, allowing agents, or all forms of interaction cause learning. Authentic assessment is a family of designs, not a warranty.

**Strong counterexample: AI-assisted success can mask worse subsequent performance.** [Bastani et al., PNAS 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/) conducted a randomized field trial involving nearly 1,000 high-school math students. Both GPT-based tutoring variants boosted performance on practice problems; unrestricted **GPT Base** improved practice grades by 48% relative to controls but was associated with **17% lower grades on a subsequent unassisted exam**. A guided version that gave teacher-informed hints without simply handing over answers performed far better during practice and showed no statistically distinguishable unassisted-exam penalty. This is the clearest experimental reason **not to equate a correct AI-assisted submission with learning**. Caveat: high-school mathematics, a short intervention and *unassisted* outcome testing are not identical to an IITM course aiming at orchestrating agents and tools. The human skill TDS wants may be different. **Design implication:** explicitly measure the capability the learner should retain *with* permitted agents, and consider additional novel or constrained tasks to expose dependent versus transferable competence.

**Nuance: AI help can also teach.** [Pardos & Bhandari, PLOS ONE 2024](https://doi.org/10.1371/journal.pone.0304013) studied GPT-based hints in a mathematics tutor and found improvements in some learning outcomes, while reporting incorrect hints as a material quality challenge. Don't write either “AI prevents learning” or “AI always teaches.” Architecture, task, baseline and measurement matter.

**Metacognition is real, but reflection is a mechanism, not proof.** [How People Learn II, National Academies 2018](https://www.nationalacademies.org/read/24783/chapter/6) reviews monitoring, planning and regulation of learning. JK's “how did you learn?” at [07:53] is well supported as a direction: students can make strategies explicit, notice errors and choose when to seek help. But an attractive reflective write-up can itself be AI-generated. **Test** whether reflection predicts later behavior on a changed task; supplement student prose with an observed choice, debugging action or delayed follow-up. For the related physical/social idea, [Ribosa and Duran's learning-by-teaching meta-analysis](https://doi.org/10.1016/j.edurev.2022.100475) supports creating teaching material for others in some conditions, but does not establish that any voice/video task is educational.

**Difficult is not necessarily useful.** [Review of desirable difficulties in education (2026)](https://doi.org/10.1111/jep.70349) and [cognitive-load review (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12432286/) offer a useful boundary: retrieval, spacing, structured struggle or productive failure can help; arbitrary UI trouble, inaccessible tools and opaque errors can waste working memory. At [04:47], the desire for “roughly half” answering correctly is Anand's question-design heuristic, not a universal evidence-based sweet spot. Correct-answer percentage depends on item purpose and baseline ability. **Calibrate learning, not just failure.**

## What the episode can prove — and cannot

| Transcript moment / claim | Evidence status | Editorial interpretation / fix |
|---|---|---|
| [03:17] “people can and should use an agent” | **Course policy/design philosophy**, verified in Sep 2026 course README | Describe as deliberate pedagogical choice; not proof it raises learning |
| [03:54] six question-design tests | **Spoken proposal**, faithfully in transcript | Powerful working checklist, not validated rubric; tests can conflict |
| [04:47] target ~50% success | **Heuristic only** | No objective evidence half-correct is optimal across question types |
| [05:08] “your identity is an agent-proof skill” | **Overstated** | Voice/image attestations can be simulated or proxied; identity also raises privacy and accessibility concerns |
| [07:53] learn how you learned | **Supported direction** | Metacognition evidence strong in general; course-level effect unmeasured |
| [11:43] expose hidden requirements | **Practical design insight** | Can be observed with requirements elicitation, critical missing acceptance criteria and revision, not just fluent text |
| [13:12] trade for invoices | **Undecided fictional prototype** | Real information-sourcing/coordination skills are plausible; no study of this proposed TDS task |
| [17:31] “20% holdouts” | **Illustrative assumption**, not a class statistic | Don't graph or quote as measured attrition |
| [20:14] market predicting token spend | **Hypothetical** | Has forecast-learning potential, but changes to the underlying spend can be strategic manipulation |
| [24:59] invite superforecaster to teach | **Brainstorm**, not scheduled/confirmed | Frame as invitation possibility |
| [27:07] “significantly large number of AI mathematical proofs are counterexamples” | **Unsubstantiated quantifier** | Counterexample search is valid technique; no sourced fraction of AI proofs here |
| [28:19] 957-point Scrabble odd-double-score | **Inspectable creative reconstruction, not ordinary legal Scrabble** | See below: crosswords, invented dictionary, unlimited tiles; don't claim standard rules in full |
| [30:45] LLMs produce the crowd's “average” | **Metaphor; too strong literally** | Some AI-assistance settings homogenize outputs; not an impossibility theorem about model originality |
| [34:15] physical coordination cannot be done by agent | **Temporary interface limitation** | Device and camera access keep expanding; humans are still responsible for consent/accommodations |
| [39:28] Shreenish asks for objectives | **Transcript fact** | First strong student challenge to assessment validity |
| [42:55] auditor loss for missing invoices | **Rubric sketch** | Count/value may be useful, but missing-data penalty requires defining expected total, unequal access, duplicates and appeal |
| [44:12] Project 1 undecided | **Explicitly confirmed** | Never present the three exercises as assigned coursework |
| [51:52] coding a collapse-completed UI tweak | **Requested live** | Transcript alone doesn't prove implementation, merge, production rollout or usability success |
| [58:23] unikernels reduce security footprint | **Conditional architecture hypothesis** | Smaller attack surface possible; not equivalent to “secure by default” |
| [59:00] app-store rules mainly protect business interests | **Unsubstantiated broad opinion** | Security, privacy, review and commercial policies all contribute; omit or attribute explicitly |
| [63:25] reused GA0 lets us infer knowledge transfer | **Weak inference** | Cohort composition, repeated items, leaked answers, tooling and preparation confound score changes |
| [64:41] normal/bimodal grade histogram proves “roughly fair” | **Contradicted by assessment standards** | Shapes of marks alone tell nothing about bias, construct validity or accommodation |
| [66:06] near-matching Tangram rejected | **Student-reported issue; cause unknown** | Same-looking pictures do not prove same coordinates; equally, a checker may be wrong; inspect exact artifact/validator |
| [67:41] student can now delegate Github/Vercel via ChatGPT | **Self-reported workflow change** | A credible concrete example of learning a tool; not proof of mastery or long-term transfer |

## The dangerous prediction-market confusion

At [20:14–23:44] students might buy/sell claims on future **AI Pipe token spending**, and can also influence the final amount by making API calls. This conflates:

1. **Prediction**: estimate a quantity external to a trader's actions and score how calibrated/adaptable those estimates are.
2. **Influence and coordination**: strategically alter the quantity you are ostensibly predicting.
3. **Market mechanics**: buy and sell under budget, slippage, liquidity, settlement and transaction rules.

The market literature does not guarantee accuracy or robustness. [Rasooly and Rozzi, “How manipulable are prediction markets?” (2025)](https://arxiv.org/abs/2503.03312) ran randomized price shocks across **817 markets** and detected some price effects even after 60 days; larger/more liquid markets were harder to move. That study concerns manipulating *market prices*, not manipulating the **underlying event**. A separate [Dai, Jia & Yu, 2026 working paper on settlement manipulation](https://arxiv.org/abs/2606.31675) analyzes contracts linked to prices traders can alter near settlement, with empirical evidence in very short-horizon Bitcoin contracts. This is structurally nearer the token-spend risk, though not a direct study of TDS.

**A defensible teaching design** could separate a publicly observable forecast series over which students have little influence (measure predictive calibration or Brier score; see [proper scoring rules review](https://doi.org/10.1146/annurev-statistics-042424-050626)) from a deliberate **influence challenge** where coordinated interventions are allowed and ethically bounded. If simulated market shares exist, define their issuance, prices, payouts, anti-collusion conditions, transaction costs, manipulation disclosure, data dashboard, API outages, and maximum exposure. Avoid actual financial stakes or ambiguous promise of profit. Course needs objective resolution criteria. A daily ticker is an interface; it does not supply the statistical learning outcome.

**A provocative visual**: two students make equally accurate token-spend “predictions.” One spends lots of credits to MAKE their prediction true. Which student learned forecasting? Change the rules, and explain whether influence belongs in the lesson.

## Distributed invoices: cooperation must be authentic, not forced theater

The task's appealing logic: each student has only a partial view of an information network. An agent may read PDFs, parse values, reconcile duplicates or plan the search but cannot automatically access a peer's files without cooperation. This mirrors organizational knowledge search and can teach a crucial problem formulation skill.

The trap: if all files are sharable, students can collate them into one shared folder, create a general solver, and bypass negotiation. Anand *noticed this live*. Artificial rules that arbitrarily block exchange may solve the shortcut at the cost of authenticity, fairness, privacy, or accessibility.

**Measure results and strategies separately**: coverage/completeness of invoices, precision of reconciliation, financial value and count of missing/incorrect items, provenance trail, recovery from missing/duplicate/mislabeled files, number of verified external interactions only if those interactions actually mattered. Ensure all students have a viable path independent of peers abandoning the course. Design an appeals process for unavailable counterparties, and permit lower-bandwidth/async collaboration. Don't secretly grade social popularity or the student's network.

A convincing adversarial pilot: (a) a strong coding agent gets all problem info except other students' private files; (b) a group collaborates and shares a general solution; (c) nonresponding peers, mislabeled sources and corrupt data are simulated; (d) a student with limited accessibility/equipment follows an equivalent route. What is the *marginal* capability measured after the task? Is it better information search, dealmaking, validation or merely endurance?

The [OECD Learning Compass](https://www.oecd.org/en/data/tools/oecd-learning-compass-2030.html) discusses student agency and co-agency and offers a conceptual rationale, not measured effectiveness of this invoice prototype.

## Correct-but-rare answers: reward useful discovery rather than weirdness

**Support for novelty tension**: [Doshi & Hauser, Science Advances 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/) randomized access to AI-generated story ideas. AI-enabled stories were rated individually more creative and enjoyable, especially by less-creative writers, but were **more similar to one another**. This supports a cohort-level homogenization concern; it does NOT prove that a strong agent cannot deliberately seek unusual correct results, nor does a story-writing result transfer unchanged to proof search.

**Math discovery**: [DeepMind AlphaEvolve, 2025](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) illustrates model-driven algorithm search with automatic verification. Exhaustive search for counterexamples, constructive configurations and rare valid objects is a fertile lesson when the **validation oracle is independently correct**. Do not claim “most AI mathematics” is counterexamples without a measured denominator.

**Evaluation failure**: awarding points purely for not matching peers creates incentives to hide a correct answer, submit arbitrary noise, manipulate normalization, or produce distinct surface wording without a distinct underlying idea. Reward **validity first**, then independently meaningful variety/distance against a well-specified metric. Test semantic equivalents, transformations, random seeds and adversarial invalid submissions. A good lesson could compare *different valid mechanisms* rather than lexically different strings.

### A documented 957-point rabbit hole, with an important caveat

The speaker's own [11 Oct 2026 blog “Calvin's 957 in Scrabble”](https://www.s-anand.net/blog/calvin-957-in-scrabble/) and [step-by-step replay](https://files.s-anand.net/blog/2026-01-11-calvin-957-in-scrabble/how-calvin-got-957.html) exist and can be linked. The imagined match has a standard board and scoring mechanics, but uses **an enormous nonstandard tile supply**, evolving fictional dictionary/proper-noun allowances and deliberately descends into Calvinball. The blog says it starts as legal play and bends rules later. It is **not a legal official Scrabble game**. The apparent “double word must yield even number” objection overlooks that a move can score extra perpendicular crosswords. The author's transcript describes a possible 957-point construction, but the score should not be called *independently validated* until replay moves and crosswords are programmatically checked.

A compelling interactive illustration can show “957 (impossible?) → double-word subtotal PLUS crosswords → legal vs creative rule relaxations” and link the author's public replay. Avoid reproducing the copyrighted original comic image without permission.

## Identity, face-to-face collaboration and inclusion

At [05:08] Anand calls identity “agent-proof.” More defensible: **at present, acquiring authorized access to a particular person's context, consent, account or body can be harder than generating text**. But voice/video may be deepfaked; an agent can sometimes control browsers/mobile apps, join sessions, and draft messages. [NIST SP 800-63-4 identity-proofing requirements](https://pages.nist.gov/800-63-4/sp800-63a/ial-general/) explicitly address fraud, forged/synthetic media, biometric attacks and privacy/exception-handling safeguards. NIST is about digital identity systems, not education, but it disproves the categorical “voice proof cannot be faked” framing.

A “group video, selfie at a location, synchronized people on screen” task should establish why *physical presence* is relevant to learning — and have equivalent alternatives for disabled, travel-restricted, caregiver, privacy-conscious or low-bandwidth learners. Photograph retention/consent rules are essential. **Permission** is a human responsibility but increasingly can be delegated through technical authorization. It is not magic agent-proofness.

[W3C WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) offers useful interface standards for accessible assessment and multimedia, though meeting individual course accommodations requires more than automatic checker conformance.

## The fairness/verification paradox: graders are part of what is being tested

**Direct contradiction in the recording:** Carlton [64:41] says a normally or bimodally distributed set of marks suggests an exam is roughly fair. **No.** Normality and bimodality are descriptive properties of score frequency, not fairness or validity. A bimodal result can signal two different preparation/resource populations; a normal result can conceal systemic disadvantage. Reliability, bias by context, intended skill coverage, consistent scoring, student notice and appeals matter. The [2015 Classroom Assessment Standards](https://ncme.org/involvement/committees/classroom-assessment/classroom-assessment-standards/) explicitly require fair/unbiased assessment and reliable/valid inferences; the same source covers accessibility, informed learners, formative feedback and using evidence. [AERA/APA/NCME Standards for Educational and Psychological Testing](https://www.aera.net/Publications/Books/Standards-for-Educational-Psychological-Testing-2014-Edition) give a broader professional basis.

**Reusing GA0 ≠ demonstrating knowledge transfer by comparing cohort histograms.** Same questions give an anchor, but observed improvement could be answer sharing, prior-task leaks, different population, changing models, external prep or improved portal usability. To measure transfer, compare novel variants or delayed blind tasks with matched starting proficiency, record model/tools access, and check whether the particular skill reappears without the original prompt scaffold. The stated 180-submission sample in local dumps is a particular **auditing/public subset** snapshot, not representative enrollment and not final term outcomes.

**The Tangram [66:06] is diagnostic, not a verdict.** The student said the target and solution looked equal but validation rejected it. Without **submitted exact coordinates/transforms, assigned target geometry and current verifier's tolerance/rounding**, it is impossible to decide if the scorer was wrong, a pixel image hid a geometric mismatch, a move snapped differently, or a different issue occurred. The story should use “it looked right” rather than claiming “the grader was broken.” For reproducible grading, show target piece IDs, polygon geometry, transformations, tolerances and canonicalization; audit failure categories and provide an appeal/debug view. This is also an example of a *verifier as curriculum*: teach how to test the test.

**A live UI improvement is not a documented release.** The student [51:05] suggested collapsing solved questions. Anand [51:52] narrated an agent request, but proof of deployment needs git history, screenshots or production checks, not just the transcript. If the page wants to show before/after, verify the actual code/build and date of change.

**A student's workflow is not a longitudinal study.** At [67:41] Shreenish says he learned to let ChatGPT connect to GitHub and Vercel rather than doing every step manually. Strong human moment, useful evidence of self-reported tool discovery. Avoid claiming this means understanding, ability to recover from failure, security awareness or ability to apply it elsewhere; those are *testable next steps*.

## What to teach, how to teach it, and how to measure it — a falsifiable synthesis

Try a reusable table rather than a list of “future-proof human skills” (which keeps changing as agents gain interfaces):

| Target skill | Student challenge with agents allowed | Independent check / repeat |
|---|---|---|
| Specification and hidden requirements | Improve a vague real software workflow | Reviewer identifies overlooked user constraint; implementation passes unseen usage cases |
| Information sourcing/cooperation | Reconstruct missing-source dataset across peers | Independent coverage and reconciliation; alternative task with changed information-holding network |
| Forecasting and belief revision | Publish probabilities, update with new evidence | Proper score (Brier/log); calibration and reasons for revisions on genuinely held-out events |
| Exploration beyond mode | Find an unusual **valid** counterexample/construction | Independent validator; semantic diversity not mere text difference; repeat with new domain |
| Agent orchestration and diagnosis | Deliver live tool-integrated artifact and handle injected failure | Verify artifact and observed recovery decisions; test when tool permission or API changes |
| Metacognition | Compare solution traces and strategies | Later task behavior improves, not just polished AI-assisted reflection |
| Verification | Challenge an attractive but faulty output/validator | Ground-truth test cases; no answer leakage; explain whether fault lies with task or judge |

**Suggested evaluation process**:
1. Pre-register the **human** capability and what would falsify its acquisition. Separate “finish task with agents” from “transfer judgment next week.”
2. Ask an uncompromising frontier agent plus motivated students to attempt both **normal completion** and **shortcuts**: share answer, share solver, collude, find client-side validation, query APIs, fake identity, deliberately move market outcome.
3. Create a grading oracle that is *more independent* than the solver, audit its errors, expose acceptable tolerances or verifiable categories, and allow feedback/appeal; favor deterministic checkers where possible.
4. Run a small pilot to quantify time/cost, grade reliability, accessibility and dependence on model spend/social contacts. Improve/remove questions that mostly reward friction.
5. Re-test on a novel environment or constraints, measure changed behavior, then decide whether the intended skill was taught.

The claim “this course teaches better AI collaboration” remains a **pedagogical hypothesis** until the outcomes above are observed. The point of the story is that the teachers are building a method for finding out, live.

## Research source shelf (primary or authoritative)

**Learning and pedagogy**
- [Freeman et al., active learning meta-analysis, PNAS 2014](https://doi.org/10.1073/pnas.1319030111) — background support, not TDS intervention
- [Bastani et al., guardrails and learning, PNAS 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/) — RCT, crucial counterexample
- [Pardos & Bhandari, LLM hints, PLOS ONE 2024](https://doi.org/10.1371/journal.pone.0304013) — AI as targeted tutor, with hint errors
- [National Academies, How People Learn II](https://www.nationalacademies.org/read/24783/chapter/6) — metacognition
- [Ribosa & Duran, learning by teaching meta-analysis](https://doi.org/10.1016/j.edurev.2022.100475) — making teaching materials for others
- [Desirable difficulties review](https://doi.org/10.1111/jep.70349) / [cognitive-load review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12432286/) — productive versus wasted struggle
- [OECD Learning Compass](https://www.oecd.org/en/data/tools/oecd-learning-compass-2030.html) — student agency framework

**Forecasting, creativity and AI**
- [Prediction market manipulation randomized experiment, 2025](https://arxiv.org/abs/2503.03312) — 817 shocks to market prices
- [Settlement manipulation of influenceable events, 2026 working paper](https://arxiv.org/abs/2606.31675) — distinct mechanism
- [Proper scoring rules review](https://doi.org/10.1146/annurev-statistics-042424-050626) — probability scoring
- [Doshi & Hauser 2024 controlled experiment](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/) — individual creativity versus collective similarity
- [DeepMind AlphaEvolve research announcement](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) — verifiable algorithm search example

**Assessment integrity**
- [NCME Classroom Assessment Standards](https://ncme.org/involvement/committees/classroom-assessment/classroom-assessment-standards/) — fairness/validity/reliability
- [AERA/APA/NCME Standards](https://www.aera.net/Publications/Books/Standards-for-Educational-Psychological-Testing-2014-Edition) — testing evidence
- [NIST SP 800-63-4](https://pages.nist.gov/800-63-4/sp800-63a/ial-general/) — identity-proofing and adversarial risks
- [W3C WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) — accessibility

**Direct speaker material**
- [11 Oct 2026 Calvin's 957 in Scrabble](https://www.s-anand.net/blog/calvin-957-in-scrabble/) and [interactive replay](https://files.s-anand.net/blog/2026-01-11-calvin-957-in-scrabble/how-calvin-got-957.html)
- [How I use AI to teach](https://www.s-anand.net/blog/how-i-use-ai-to-teach/)
- [5 Oct TDS orientation](https://talks.s-anand.net/2026-10-05-tds-orientation/) and [10 Aug TDS AMA](https://talks.s-anand.net/2026-08-10-tds-ama/)

**Verification status:** the crucial 2025 PNAS trial, 2024 Science Advances RCT, NCME standards, 2025 prediction market experiment, 2026 settlement-manipulation working paper, NIST guidelines, and Oct 11 author blog were opened/retrieved as primary pages on 13 Oct 2026. Other shelf items were located during research or cross-checked from prior TDS story context but should be re-opened against a precise claim if featured. Link labels don't confer experimental causality. Do not mistake dated preprints for consensus or presentation/demo results for controlled assessment outcomes.

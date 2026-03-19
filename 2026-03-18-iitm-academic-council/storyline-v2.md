# Storyline v2: The Open-Book Exam We Didn't Design

**Talk**: Innovations in AI-Assisted Education
**Audience**: IIT Madras Academic Council
**Thesis**: Every assessment at IITM is already an open-book exam — whether we designed it that way or not. The question is no longer whether to allow AI, but what good education looks like when the textbook can answer every question.

---

## Framework / Metaphor

### Primary: The Open-Book Exam

Every educator knows the logic of an open-book exam: when information is freely available, test for judgment, not recall. We use it deliberately in some settings — because we recognise that the skill we're after is synthesis, application, decision-making, not retrieval.

AI has made _every_ exam an open-book exam, whether we called it that or not. The student sitting your closed-book test has a postgraduate intern in their pocket who knows more than most TAs, is available at 3 AM, never loses patience, and costs ₹1,600 a month. The question is not whether students will use it. They already are. The question is: **what does rigorous, fair, scalable education look like when every exam is already open-book?**

### Secondary: The GPS Decision Framework

When a new technology erodes a skill, institutions have four choices — and all four are legitimate depending on context:

- **Enforce**: Keep drilling the skill anyway. Surgeons train without robots because the failure mode is catastrophic. We enforce flight simulators for pilots.
- **Level-Up**: Shift the skill to a higher plane. Spreadsheets eroded manual calculation. We levelled up from arithmetic to strategy.
- **Switch**: Revalue a different skill entirely. Photography made brushwork less central. Art switched to composition, intention, impressionism.
- **Accept**: Let the skill go. GPS eroded navigation. We accepted it — and we're fine.

Every learning objective in every course now needs this audit. Not once, as a curriculum committee exercise — continuously, as models advance. The GPS framework gives the Academic Council a principled decision rule: for each skill, do we **enforce, level-up, switch, or accept**?

---

## Narrative Arc

### Beat 1 — Hook: The ₹800 Problem (2 minutes)

Open with a specific moment IITM faculty already know:

> Before a viva, a student in your programme receives a WhatsApp message: _"Your proctor is [name]. He asks these questions. Here's what to say."_

This is not a rumour. It is documented reality. Organised markets have formed around the IITM assessment calendar — ₹800 bootcamps that promise to do the entire project. Proxy viva services. Scripts written to paste into ChatGPT faster than the proctor can notice. The viva system shuffled proctors to stop the leak; within weeks, the leak adapted.

**The tension**: This is not a student discipline problem. It is an architecture problem. The assessment was designed to measure something. But the thing it now measures — under the current design — is resourcefulness at gaming it. Which raises an uncomfortable question: _is that wrong?_

### Beat 2 — Setup: We Built This for a Different World (5 minutes)

Traditional education was engineered for information scarcity. The closed-book exam, the supervised assignment, the solo project — all of these rest on a single assumption: _expertise is rare and expensive, so the ability to store and retrieve it is worth testing._

That assumption held for two centuries. A student who had internalised the knowledge had a genuine advantage over one who hadn't.

Then intelligence got cheap. Not eventually — now.

For ₹1,600 a month, any student can access a system that:

- Knows more than most teaching assistants in most domains
- Is available at 3 AM before a deadline
- Speaks Tamil, Telugu, Hindi, and English without switching modes
- Never loses patience on the fifth "dumb question"
- Can read a 200-page textbook in seconds and identify the relevant passage

The assumption that justified the locked-room exam — that knowledge was hard to access — evaporated. We are still running the locked-room exam.

### Beat 3 — Complication: The Cheat That Isn't (5 minutes)

Here is the uncomfortable truth at the centre of this talk.

The student who is using AI to pass their viva — who has learned to paste questions into ChatGPT, scan the answer, adapt it in real time, and deliver it with enough confidence to fool the proctor — is practising the single most valuable professional skill of the next decade.

The ability to orchestrate AI tools to get work done. To verify the output. To adapt when the model fails. To push the system to its limits. This is what every employer in every domain now wants. This is what the highest-performing workers in AI-augmented roles are doing.

**We have designed a system where the most forward-looking behaviour looks like cheating.**

The student who memorised the answer and can recall it under pressure — and nothing else — is less prepared for the world they are entering than the student who learned to work with AI, verify it, and deliver. We are accidentally selecting against the future.

This is not an argument to abolish assessment. It is an argument that **the question has changed**. We used to ask: _can you recall this?_ The right question now is: _can you do this — using any tool at your disposal — and can you tell me why the answer is right?_

### Beat 4 — Revelation: The GPS Moment (7 minutes)

Every generation faces a GPS moment — a moment when a new technology forces a decision about what to do with the skill it is replacing.

| Technology   | Skill eroded          | Institutional response                                        |
| ------------ | --------------------- | ------------------------------------------------------------- |
| Autopilots   | Manual flying         | **Enforce** — flight simulators, because catastrophic failure |
| Spreadsheets | Manual calculation    | **Level-up** — from arithmetic to financial strategy          |
| Photography  | Brushwork replication | **Switch** — to composition, intention, impressionism         |
| GPS          | Navigation from maps  | **Accept** — we're fine without it                            |

AI is your GPS moment for most of the skills in most of your courses. The question is not _whether_ AI will change what you teach. It is _how deliberately you will choose_ the response.

Some skills still need to be enforced — understanding where AI fails, verification, judgment in ambiguous situations, hands-on lab competence. These are skills where the failure mode of not having them is too serious to accept AI substitution.

Some skills can be levelled up — from writing code to designing systems, from running analysis to interpreting and questioning it, from following a rubric to evaluating whether the rubric itself is right.

Some skills can be switched — we can stop teaching certain syntax and start teaching meta-skills: how to give AI directional feedback, how to spot a hallucination, how to write a specification that an agent can execute.

And some skills can be accepted as obsolete — and the faculty time saved can be spent on the skills that matter more.

**The insight for this audience**: the GPS framework is not a personal choice. It is a governance choice. Individual faculty can run this experiment in one course. But to do it systematically — to redesign a programme rather than a course — requires a decision from this body.

### Beat 5 — Evidence: Three Redesigns, One Theme (12 minutes)

Here is what this looks like in practice. These are not proposals. They are experiments already running, at scale, in a course with 3,000+ students annually.

---

**Redesign 1: The Curriculum** — _Remove the content. Give them questions._

The Tools in Data Science course no longer has explanatory lecture notes. Students receive questions. Every question has an "Ask AI" button that sends it to their preferred model. If AI can answer the question easily — great, they paste the answer and move on. The point of _those_ questions is to show them where AI succeeds.

The questions that matter are the ones AI answers badly: integration tasks, debugging AI output, validating results, making judgment calls under ambiguity, designing workflows. Those questions teach something a textbook cannot.

This is not lazy teaching. It is teaching redesigned around what the GPS moment demands: not _what_ to know, but _when to trust what you know_.

**What the Council controls here**: syllabus design. This is a model for what a course looks like when it has been through the GPS audit.

---

**Redesign 2: The Assessment** — _Make it impossible to game with generic AI._

The viva problem is real. But the solution is not to ban AI during vivas — it is to ask questions AI cannot answer without the student's specific work.

Concretely: each student's viva questions are generated dynamically from _their own codebase_. A question like "why did you use recursion here instead of iteration?" requires the student to know _their_ code. A generic ChatGPT window — without the private repo — cannot answer it well. A student who copied the project from someone else cannot answer it at all.

Beyond vivas: assessments now use dynamic seeded personalisation. Each student gets a different variant of the same question, with server-side validation of correct answers. Answer-sharing becomes useless because your answer doesn't apply to your neighbour's question.

At the highest tier: live LLM API competency assessments where students must actually call real model endpoints, analyse outputs, and catch hallucinations in real time. This cannot be prepared for generically. It requires genuine capability.

**What the Council controls here**: assessment policy. The question to put to every programme is: _if you pointed a state-of-the-art coding agent at your exam, what would it score? And what does that tell you about what you're measuring?_

---

**Redesign 3: The Governance** — _Tiered oversight, not a binary choice._

The hardest governance objection to AI in assessment is: we cannot review everything at scale. A 3,000-student course generates thousands of submissions. Human review of each one is not feasible.

This is a false binary. The right architecture is tiered:

- **Green** (auto-pass): Factual, verifiable, low-stakes outputs. Automated grading is reliable and fast. No human review needed.
- **Amber** (spot-check): Higher-stakes, borderline, or unusual. A sample — say 10-15% — goes to human review. AI flags which ones to check.
- **Red** (always human): Judgment calls, appeals, exceptional cases, academic integrity decisions. Humans are always in the loop here.

This is not a concession to AI. This is a design choice that makes review _more_ targeted, not less rigorous. Humans review what matters. AI handles the routine. The result is more consistent grading, faster turnaround, and a defensible audit trail.

The same architecture extends to student support: AI handles the first 80% of questions (setup, syntax, clarification). Human TAs handle the 20% that requires judgment, reassurance, and escalation.

**What the Council controls here**: this is a Senate-level governance architecture. It defines the standard for AI-assisted academic processes — what can be automated, what must be human-reviewed, and what documentation is required.

---

**The common thread**: in all three redesigns, AI use is made _visible, structured, and governable_ — rather than pretending it can be kept out.

### Beat 6 — Implication: What IITM Now Has (5 minutes)

There is one more thing this audience should know.

IITM is, right now, sitting on an educational research dataset that does not exist anywhere else in the world.

Every submission in a 3,000-student course. Every AI query made during an assessment — which model, which question, at what time, before or after getting the answer right. Every viva recording. Every code trace from a student working through a problem. Thousands of data points on how students learn, where they get stuck, and what kinds of AI interaction improve performance.

We know, from the data, that students who use Claude perform slightly differently on certain question types than students who use ChatGPT. We know that submission timing — how far before the deadline a student submits — correlates with performance in ways that could support earlier intervention. We know from code-snapshot analysis that a certain class of Python errors is not a knowledge gap but a mental-model failure about how functions return values — and that the right test case can catch it before the student submits broken code.

This is not just an operations asset. It is a research programme. The institution that mines this data systematically — and publishes the findings — will not just solve its own assessment problems. It will lead the field.

**The three asks for this body:**

1. **Commission a GPS audit**: For each course in the programme, classify every learning objective using the Enforce / Level-Up / Switch / Accept framework. This is a governance exercise that faculty cannot do alone — it requires programme-level coordination and a mandate from this body.

2. **Establish an AI-assessment design standard**: Require that new assessments declare their AI policy and include at least one dynamic or personalised element that resists generic AI gaming. Create a fast-track review process for AI-redesigned courses.

3. **Fund the data infrastructure**: Instrument the learning environment. Create a shared data layer across courses. Commission cross-course learning analytics. This is an investment in institutional advantage — the kind of advantage that takes years to build and that no other institution in India currently has.

---

## Key Messages (Five Things to Remember)

1. **The intern is already in the room.** Every student has a postgraduate AI assistant. The question is what we do about it — not whether to acknowledge it.

2. **The cheat is the skill.** The behaviour we call academic fraud is, in many cases, the behaviour employers will require. Redesign the exam, not just the policy.

3. **The GPS framework gives you a decision rule.** For each skill: Enforce / Level-Up / Switch / Accept. Apply it deliberately, not reactively, at the programme level.

4. **Governance doesn't have to choose between full automation and full manual review.** Green / amber / red tiering is scalable, defensible, and more rigorous than blanket human review of everything.

5. **IITM's scale is an asset.** The data already exists. The institution that mines it will lead — not follow — the field.

---

## What Makes This Talk Memorable

**The hook is real and local.** The ₹800 WhatsApp market is not a hypothetical. The audience knows about it. Starting there earns credibility.

**The central insight flips the frame.** The audience comes in believing the cheater is the problem. They leave understanding the _system_ is the problem — and that the solution is a redesign they are empowered to commission.

**The GPS framework is portable.** The audience can use it in committee, in a Senate meeting, in a conversation with a colleague who is resisting. It gives them language for a decision they otherwise have no vocabulary for.

**The three redesigns are concrete and tested.** Not proposals. Not pilots at a startup. Running now, at IITM scale, in a publicly auditable course.

**The close is aspirational, not alarmist.** The talk does not end with a warning. It ends with an opportunity — one that is uniquely IITM's to seize.

---

## Tone and Delivery Notes

- This is not a product pitch. There is nothing to sell. Adopt the posture of a colleague reporting from the frontier.
- Acknowledge the governance constraints are real. The audience lives inside them. The talk should feel like it respects those constraints rather than dismissing them.
- The discomfort in Beat 3 ("the cheat that isn't") is intentional. Let it land. Don't rush past it with a reassurance. The audience should sit with the discomfort long enough to feel the insight.
- Use specific numbers where available: 3,000 students, ₹800 bootcamp, 2,000+ L1 vivas, ₹1,600/month for frontier AI. Specificity is credibility.
- The GPS table is the single most reusable artefact. Consider it as a standalone visual, displayed long enough for the audience to photograph it.

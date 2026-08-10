---
title: "TDS AMA Prep 2026-08-10"
date: 2026-08-10T19:57:06+05:30
source: "https://chatgpt.com/c/6a79375b-58c0-83ec-aed2-5dac916f625a"
---

## ChatGPT

<details>
<summary>Worked for 3m 8s</summary>

I’ll reconstruct your current TDS teaching model from the strongest evidence first—weekly-session transcripts, course notes/exams, and your own TDS reflections—then design the AMA as a set of high-information “tests” rather than a Q&A.

Analyzed TDS sessions and inspected outputs for AMA stress tests

I’m separating “what you say TDS is” from “what the course actually rewards.” That distinction matters: the AMA can test contradictions between your stated philosophy, assessment design, and student behavior—not just solicit opinions.

Inspected tool outputs, task-management notes, and research guidance

Reviewed research findings and guidance

Selected core files from notes and transcripts

The first pass surfaced a useful pattern already: there’s unusually rich evidence around January 2026 (weekly sessions + an intentionally experimental Project 1 + ROE design) and a second cluster around the May 2026 redesign. I’m drilling into those, plus the course’s explicit feedback mechanisms, because they are the likeliest places where your teaching theory is most testable.

Simplified shell execution and inspected downloaded core file

Inspected key terms, transcript delimiters, notes, and feedback sections

Inspected targeted evidence and project feedback

Synthesized experiment feedback, blog details, and transcript evidence

The strongest mismatch I see is this: your explicit model increasingly says “the content is the problem-solving loop—use AI, test, debug, ask better questions, collaborate”—yet actual student behavior often remains “study the content, memorize, attempt alone, use AI surprisingly little.” That gap is a much better AMA target than “what do you like/dislike about TDS?”

Collected exact feedback line evidence

</details>

- Attachment: skills-list.txt (Document)

- Attachment: tds_research.txt (Document)

- Attachment: tds_core.txt (Document)

- Attachment: tds_evidence.txt (Document)

I would treat the AMA as a research session, not primarily as an AMA.

My reconstruction of your current TDS mental model is roughly:

> TDS is not really a course about tools. It is a deliberately difficult practice environment for becoming resourceful, AI-native, verification-minded, collaborative, production-oriented problem solvers who can handle unfamiliar situations.

There is strong evidence for that interpretation. Your notes explicitly say that exams tell students what to learn and question whether assessments measure what they should; you increasingly design assignments around real action, collaboration, deployment and verifiability rather than recall (`~/Dropbox/notes/iitm-tds-tools-in-data-science.md`, especially the objectives/assessment section). In January, you told the team that the prompt-based problems themselves were “the content,” and described the learning loop as: why does this matter → where does it break → what can AI do → what remains for me → how do I test → what would an expert ask? (`~/Dropbox/notes/transcripts/2026-01-07 TDS.md`, around lines 141–207). Sujal independently observed that students were treating videos conventionally—taking notes and memorizing rather than solving problems—and you explicitly pushed toward the latter.

Your experiments also suggest that some of the biggest effects of TDS are not “knowledge acquired.” Project 1 produced collaboration and social infrastructure; one student described going from interacting with nobody to regularly dividing problems and solving them with classmates, and you called that what you had been trying to teach for five years (`~/code/blog/posts/2026/tds-project-1-was-an-experiment.md:12-32`). Student feedback describes resourcefulness, selective reading, working around poorly specified problems, friendships and a new confidence when confronting “undoable” work (`~/code/blog/pages/notes/tds-feedback.md:10-16`). Meanwhile the ROE gave you disconfirming behavioral evidence: many supposedly easy repeat questions collapsed under pressure; students scarcely used the Ask AI button despite being encouraged to do so; and collaboration was much lower than you expected (`~/code/blog/posts/2026/tds-jan-2026-roe.md:69-149`).

That last point is the opportunity. You have a reasonably developed theory of what students ought to be learning. You have much weaker evidence about what mental transformations actually happen inside different kinds of students.

The question I would make the session answer is:

**“What does TDS actually teach students to do differently when Anand is not around—and for whom does it fail to produce that change?”**

That reframing gives you several high-value hypotheses to attack.

1. **“Use AI first” may not be a student habit.** You already have hard evidence from the ROE that many students barely touched Ask AI. Find out why. Is it unfamiliarity, distrust, habit, cost/model access, inability to prompt, belief that it is cheating, or simply that under pressure they revert to old study behavior?
2. **“Copy, but understand” may work much less well than you think.** Correct submission is poor evidence of learning when AI/friends can generate it. Look for transfer: “Tell me about something you successfully submitted, then encountered again later and realized you hadn't actually understood.”
3. **Difficulty may be doing two completely different things.** Your feedback suggests genuine desirable difficulty, agency and confidence. But “hard” can also mean arbitrary friction, prerequisite gaps and panic. Your own notes contain requests for prerequisite bridges, more explanation and mentoring. Separate:

- productive struggle: “That was horrible, but afterward I could do something new”
- sterile struggle: “I lost six hours because I didn't know one hidden prerequisite.”

This distinction could substantially change TDS. 4. **Collaboration may be one of your largest learning outcomes, but also highly unequal.** Project 1 and the ROE both show clusters and “super-collaborators.” Ask whether TDS creates networks or merely rewards students who already know how to form them. Quiet, weaker or geographically isolated students are the critical sample. 5. **Students may learn the surface game without extracting your abstractions.** A student might learn “use `uv`,” “ask ChatGPT,” “hack the evaluator” and “find somebody on WhatsApp,” while you think they learned composability, verification, decomposition, debugging and resourcefulness. Test whether they can name and transfer the abstraction. 6. **Your own high-agency style may be baked too deeply into the course.** TDS often rewards exactly the behaviors you personally enjoy: exploring, hacking, trying tools, tolerating ambiguity, reading docs selectively, finding shortcuts, questioning rules. That may be superb preparation for one valuable operating style—but you need evidence about whether students with lower initial agency acquire that style or merely get filtered out by it.

That sixth one is the blind spot I would pursue hardest.

### What I would actually do in the session

Do not begin by explaining your philosophy. That contaminates the experiment. Get their model first.

For the first 7–8 minutes, make everyone—not just speakers—answer an anonymous mini-form. Keep answers very short. I would ask:

- “What is TDS really teaching you? ≤10 words.”
- “Last time you were stuck for >20 minutes, what did you try first?”
- “Name one thing you passed without really understanding.”
- “Name one painful TDS experience that taught you something useful.”
- “Name one painful experience that taught you almost nothing.”
- “If every TDS tool vanished next year, what skill would remain?”
- “What does Anand believe about how students learn that you think is wrong?”

That last question is especially valuable. Make it anonymous and explicitly ask for disagreement.

Then show them your one-sentence model of TDS and say, in effect: **“Your job for the next hour is to break this.”**

Now run four probes.

**Probe 1: reconstruct a real incident rather than soliciting opinions.**

Ask a student:

“Pick one GA problem where you were really stuck. Walk me minute-by-minute through what you actually did.”

Keep drilling into behavior:

“What did you try first?”
“Why?”
“When did you ask AI?”
“What exactly did you ask?”
“What did it get wrong?”
“How did you know?”
“When did you ask another student?”
“What finally unlocked it?”
“What would you do differently today?”

Critical-incident reconstruction will teach you far more than “How useful was AI?”

Get 4–6 stories with deliberately different students: high performer, middle performer, struggling student; heavy collaborator, solo student; heavy AI user, reluctant AI user. Do not let the six most vocal enthusiasts become your sample.

**Probe 2: give them an unfamiliar micro-problem and observe.**

This may be the single highest-value thing you can do.

Give everyone the same genuinely unfamiliar but solvable 5-minute problem. It should require no TDS-specific knowledge and permit AI, web, friends, anything. Tell them simply:

**“Solve this. Anything goes.”**

Then observe first moves.

Who immediately asks AI?
Who reads everything first?
Who starts coding?
Who searches documentation?
Who asks the person next to them?
Who freezes?
Who tests the first answer?
Who blindly submits it?
Who creates a tiny experiment?

After five minutes ask:

“What did you do first, and why?”

Your course philosophy is fundamentally about behavior under uncertainty. **So measure behavior under uncertainty.** Their answers about their own learning are secondary evidence.

You could make this exceptionally useful by having a tiny submission form capture first action, second action, whether they verified, and whether they collaborated.

**Probe 3: test transfer explicitly.**

Put up examples and ask, “What is the same skill underneath these?”

For example:

- debugging bad JSON / debugging an LLM answer / debugging a deployment
- checking a chart / checking generated code / checking a research answer
- curl / DuckDB / Git / an AI agent
- working around an evaluator / working around a corporate process

Do not tell them the abstraction.

If students spontaneously say things like “reduce the problem,” “inspect interfaces,” “create a test,” “verify assumptions,” “understand the contract,” “use the cheapest tool,” you have evidence of transfer.

If they mainly describe commands and recipes, an important part of your mental model is false: **you are teaching abstractions implicitly and assuming students extract them.**

That would suggest a surprisingly small intervention: after an assignment, explicitly name the reusable pattern they just practiced.

**Probe 4: separate learning from survival.**

Give everyone 100 imaginary “learning points” and ask them to allocate them among:

- videos/content
- graded assignments
- projects
- AI
- TAs/Discourse
- classmates
- pressure/deadlines
- figuring things out alone

Then ask the interesting follow-up:

**“Now allocate 100 marks according to what helped you get grades.”**

The gap between the two distributions is gold.

Your own rule is that exams tell students what to learn. This directly tests whether the incentive system is producing the behaviors you intended.

### A few questions I would particularly want answered

I would not try to ask all of these, but these are unusually diagnostic:

“What can you do now that January-you could not have figured out even with ChatGPT?”

“When ChatGPT gives you a plausible answer, what do you do next?”

“Tell me about the last time TDS made you ask another human for help.”

“Which TDS question taught you the most despite giving you few marks?”

“Which question gave you marks but taught you essentially nothing?”

“What do the top students know about doing TDS that struggling students discover too late?”

“Imagine I made TDS 30% easier. What valuable thing would disappear?”

“Imagine I removed all videos. What would actually get worse?”

“Imagine AI becomes ten times better next year. What should I stop teaching immediately?”

“What prerequisite do we pretend students have but many actually don't?”

“Which thing feels like a bug in TDS but is actually useful?”

“Which thing feels like deliberate difficulty but is actually just a bug?”

“What did you learn from another student that you would never have learned from me?”

And perhaps the most valuable:

**“Think of someone you know who is intelligent and hardworking but would nevertheless do badly in TDS. Why?”**

That gives you a description of the course's hidden selection function.

### Protect yourself against the biggest sampling problem

Twenty to fifty attendees speaking voluntarily will massively overweight exactly the people TDS may already work for.

Therefore, the spoken AMA should be **qualitative follow-up to silent evidence**, not your dataset.

At minimum, privately capture performance band, AI-use band and collaboration style alongside answers. You don't need names. Then compare:

- top / middle / struggling
- heavy / light AI
- highly connected / mostly solo
- “TDS is fun” / “TDS is painful”

Five contrary students are more useful to your purpose than fifteen articulate fans.

Your own TDS notes already contain essentially this insight: a small-N topper/median/bottom panel can be more decision-useful than broad voluntary feedback. The AMA gives you a chance to execute that idea rather than merely discuss it.

### The perspective I think might emerge

I suspect your current model is one abstraction short.

You currently think roughly:

**tools → problems → AI + experimentation + verification + collaboration → resourceful practitioner**

I would test whether the better model is:

**identity/agency → willingness to experiment → feedback loops → resourcefulness**

In other words, perhaps TDS's most important product is not knowledge, tool proficiency, or even problem-solving technique. It may be **learned agency**:

> “I don't know how to do this. That's normal. I can probably figure it out.”

The student feedback about acquiring a “weird sense of confidence” after surviving TDS is unusually suggestive here. Your Project 1 student's social transformation points in the same direction.

If that is true, it changes teaching design. You would stop asking only, “Did this assignment teach X?” and start asking:

**“Did this assignment increase the probability that this student attacks the next unfamiliar problem rather than waits to be taught?”**

But there is a dangerous alternative explanation you should actively seek: perhaps TDS does not create agency nearly as much as it **selects for students who already possess it**.

That is the hypothesis I would make the AMA try hardest to falsify.

If you can leave the session knowing whether TDS **creates resourcefulness or mostly rewards pre-existing resourcefulness**, you will have learned something much more consequential than another list of syllabus improvements.

---

## ChatGPT

<details>
<summary>Worked for 8m 49s</summary>

I’ll audit the load-bearing claims in both answers against your TDS corpus, especially Claude’s quantitative specifics and my stronger causal interpretations. Then I’ll rebuild the session around only the hypotheses the evidence actually leaves unresolved.

Searched corpora for targeted claims and evidence

I’m checking the most consequential disagreements first: whether the “9–11 point model effect,” “333 students,” effort/collaboration claims, and the alleged open questions are actually documented; and whether my “learned agency vs selection” thesis is evidence or inference.

Downloaded TDS audit results

Audited conversation, claim, and TDS files for exact references

Searched exam repositories and downloaded the TDS numeric audit file

Claude’s qualitative “use the room for what logs cannot tell you” survives. Two quantitative claims are not yet substantiated by the material I’ve checked: the exact “333 students” cohort and “Claude/Perplexity users score ~9–11 points higher.” I’m treating those as unverified until I can trace their calculation, rather than building the session around them.

Inspected downloaded file size and contents

Searched evidence files and validated TDS hypotheses

Verified Project 1 evidence and collaboration details

Audited Claude’s quantitative claims

</details>

After checking both answers against the TDS material, I would change my earlier answer substantially. Claude has the better top-level framing; my answer had the better central experiment, but I overcommitted to one interpretation of what TDS is producing.

The better question is:

> **What important uncertainty about how TDS changes students can this live room resolve that your existing telemetry cannot?**

You already instrument Ask AI clicks, engagement, scores, model use/switching, etc. tds_audit

So using 20–50 live students to estimate quantities you can derive from logs is wasteful. Use them to discover mechanisms, missing variables, transfer, and things outside your current hypothesis space.

### What survives fact-checking

| Claim                                                                           | Verdict                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| My “TDS isn't really about tools”                                               | **Too strong.** Your documented design is explicitly production-first and tool-belt-oriented, with a goal of making students “dangerously productive.” Tools are the substrate; they aren't incidental. tds_core                                                                                                         |
| My “the questions themselves are the content”                                   | **Strongly supported.** You explicitly say “This is the content,” while Sujal reports students still watch videos, take notes and memorize instead of solving. tds_audit                                                                                                                                                 |
| My “AI-first and collaboration haven't become habits”                           | **Supported for the Jan ROE.** Half barely used Ask AI; the largest collaboration bundle was 84 versus your 500-token target. tds_core                                                                                                                                                                                   |
| My “resourcefulness/agency may be the real product”                             | **Promising hypothesis, not conclusion.** The student testimony about resourcefulness and “weird sense of confidence” is striking, but it is one self-selected testimonial. tds_audit                                                                                                                                    |
| My “creates resourcefulness vs selects resourceful students”                    | **Very important and better grounded than I realized.** Your own notes explicitly pair “what sort of data scientist does TDS produce?” with filtering intake and student quality. tds_core                                                                                                                               |
| Claude's “use the AMA for what logs can't see”                                  | **Best idea in either answer.** Keep it.                                                                                                                                                                                                                                                                                 |
| Claude's “the room is survivors / engaged tail”                                 | **Likely, but measure it rather than assume it.** Your own May discussion already worries that voluntary feedback respondents are non-representative and proposes topper/median/bottom interviews instead. tds_core                                                                                                      |
| Claude's “Claude/Perplexity users score ~9–11 points higher” and “333 students” | **Unverified from the corpus I checked.** I found model-use instrumentation, but not the calculation supporting those exact figures. I would drop both until the analysis that produced them is located.                                                                                                                 |
| Claude's “Project 1 design tasks scored worse than analytics”                   | **Supported.** Your Project 1 write-up explicitly says design tests were diverse and students fared worse there. tds_evidence                                                                                                                                                                                            |
| Claude's two-person live solve                                                  | **Good idea, wrong sampling unit.** Two volunteers will be unusually confident and visibly observed. Give the unfamiliar problem to everybody, then interview contrasting strategies.                                                                                                                                    |
| Claude's anonymous complaint + upvote                                           | **Useful, but “complaint” biases discovery.** Ask for surprises, failed assumptions and useful/useless friction instead. Also, don't use an authenticated exam portal if anonymity is the goal.                                                                                                                          |
| Claude's forced token allocation                                                | **Excellent.** I would strengthen it by making students allocate twice: “what taught me” versus “what got me marks.”                                                                                                                                                                                                     |
| Claude's alumni follow-up                                                       | **Correct but overstated.** Current students can answer process and immediate transformation. Alumni are much better for whether those changes transfer to work months or years later. Your own unresolved question about what kind of data scientist TDS produces makes an alumni study particularly valuable. tds_core |

### My revised model of your TDS model

I no longer think “learned agency” captures enough of it.

Across your 2026 material, I see something closer to:

> **TDS is an environment for developing adaptive competence: take an unfamiliar, messy, real-world task; frame it; use AI, people and composable tools aggressively; orchestrate them; detect where they fail; verify; and ship something that works.**

The older “tool-belt” objective is still there. But your newer notes are converging toward a stable layer above individual tools: **Framing → Context engineering → Orchestration → Verification design → Assetization / Systems.** tds_core

Your January framing similarly shifts the future data scientist from pure analysis toward deployment/MLOps, critical judgment and orchestration. tds_core

Project 1 gives a particularly interesting clue: you cared enough about students spontaneously forming groups, dividing questions and meeting regularly to write, “THIS is what I've been trying to teach for 5 years now!” tds_core

So the key uncertainty isn't simply:

> “Does TDS teach resourcefulness?”

It is:

> **Which parts of that adaptive-competence loop are students actually internalizing, which are they merely performing because the course forces them to, and which students never enter the loop at all?**

That is what I would make the AMA diagnose.

### Six hypotheses worth spending the room on

| Unknown                                                                                                      | Best live probe                                                                                                                                                                                                                           | What a surprising result changes                                                                                                 |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **1. Transfer:** Are students learning general strategies, or TDS-specific hacks?                            | Show 3 very different TDS tasks and ask anonymously: “What's the same skill underneath these?” Then give a novel non-TDS task needing the same skill.                                                                                     | If they solve old forms but don't transfer, explicitly teach/name the abstraction after each assignment.                         |
| **2. Creation vs selection:** Does TDS create high agency or reward people who arrived with it?              | “Think back to before TDS. Tell me one unfamiliar problem you would have abandoned then but would attack differently now. Exactly what changed?” Then ask for the counterexample: intelligent, hardworking classmate who still struggled. | This tells you whether to make TDS harder, or instead build scaffolds that induce the behavior in initially low-agency students. |
| **3. Why AI is underused:** The ROE tells you _that_ students didn't use enough AI, not _why_.               | Reconstruct the last real stuck episode minute-by-minute: first action, second action, when AI entered, what model, what failed, how they verified.                                                                                       | “Use AI first” may need habit training, better UX, trust calibration, prompting skill, or nothing at all depending on mechanism. |
| **4. Productive vs sterile difficulty:** Your hardest design choice.                                         | Collect two incidents from everybody: “Painful but taught me something durable” and “Painful and taught me almost nothing.”                                                                                                               | Don't ask “make TDS easier?” Remove **extraneous** difficulty while protecting productive difficulty.                            |
| **5. Collaboration mechanism:** Does TDS create social learning or merely reward already-networked students? | “Last time another student materially helped you solve something: how did you know whom to ask?” Also ask those who mostly work alone why.                                                                                                | If the bottleneck is network access, engineer quads/pairs. If it's preference or incentives, different intervention.             |
| **6. Incentive alignment:** Are your assessments teaching what you think they teach?                         | Give 100 points to “what actually taught me”: GAs, projects, AI, classmates, videos/content, TAs, pressure, solo struggle. Then allocate another 100 to “what got me marks.”                                                              | The gap is an empirical answer to your own maxim: “the exams tell students what to learn.” tds_core                              |

I would add one especially sharp question from my previous answer:

> **“Think of an intelligent, hardworking student you know who nevertheless did badly in TDS. What, concretely, happened?”**

That is probably a richer probe of your hidden selection function than asking struggling students “why did you struggle?”

### The live experiment I would definitely run

Claude's live-solving idea and my previous idea combine into something stronger.

Give **everyone** a fresh 5–7 minute problem. Make it unrelated on the surface to TDS but structurally similar to the capability you care about. It should be legal to use absolutely anything.

Don't tell them what you're measuring.

Capture only four things: first action; whether/when they used AI; whether they involved another human; how they checked that the answer was right.

Then reveal the distribution and interview contrasting cases:

“Why did you start by reading everything?”

“Why did you immediately paste it into Claude?”

“You had an answer in 40 seconds. Why did you test it?”

“You didn't verify. Why not?”

“You asked your classmate before AI. Why?”

This directly tests whether your course's behavioral lessons have become defaults. The Jan ROE explicitly states the desired pattern as scan for quick wins, try tools rather than assuming difficulty, use AI first, and collaborate. tds_core

A self-report saying “TDS taught me resourcefulness” is weak evidence. **Watching the student encounter novelty is much stronger.**

### How I would run the AMA

I would preserve the AMA character rather than convert the whole event into a lab.

For a 60-minute session, use roughly the first 7 minutes for silent anonymous responses; 10–15 minutes answering their highest-voted AMA questions; 10 minutes polling 4–5 beliefs about TDS that you genuinely hold; 8 minutes for the whole-room unfamiliar task; 15 minutes interviewing contrasting critical incidents; and the final 5 minutes for the learning-vs-marks allocation and one anonymous exit response:

> **“What does Anand believe about how you learn that is most wrong?”**

Crucially, **do not explain your theory of TDS first**. Let them reveal theirs. Near the end, show your own one-sentence model and ask them to break it.

Claude is right about pre-registration too, but I would not use its ten suggested numerical predictions. Several thresholds are arbitrary. Before entering the room, write down perhaps five beliefs you personally think are true, with probabilities if useful, and—this is the important addition—write beside each:

**“If this is false, what will I change?”**

Otherwise you can be delightfully surprised without actually updating anything.

### One improvement neither answer emphasized enough

You can empirically measure how biased the AMA room is.

Afterward, compare **attendees as a group** with the full cohort on variables you already have: GA/ROE performance, engagement, Ask-AI use, first-attempt timing, etc. Keep the anonymous comments unlinked to identities; use the meeting roster only to characterize the sample at aggregate level.

Then you can say something like:

> “This room was the 78th percentile on engagement but only 55th on marks.”

That tells you exactly how much weight to put on what they said.

And use attendees as **informants about missing students**, not replacements for missing students. “Tell me about one person who stopped showing up” can generate a hypothesis; it cannot estimate why non-attendees disappear.

### The new perspective I would most like this AMA to reveal

My earlier answer framed the tension as:

**TDS creates resourcefulness vs TDS selects resourceful people.**

I now think that is part of a more useful 2×2:

**Can they produce the result?** × **Can they transfer the strategy?**

That creates four students:

|                             | Can transfer strategy                         | Cannot transfer strategy                        |
| --------------------------- | --------------------------------------------- | ----------------------------------------------- |
| **Gets results**            | The outcome you want: adaptive practitioner   | Dangerous false positive: good TDS gamer        |
| **Doesn't get results yet** | Promising learner needing fluency/scaffolding | Student the current course may simply overwhelm |

Your automated evaluations are very good at the vertical dimension: **did it work?**

The AMA can uniquely probe the horizontal dimension: **what did they learn about how to solve the next problem?**

That may be the most important blind spot in the current assessment architecture. Your design makes answers increasingly verifiable; your open question is whether **the student's reusable mental model** is being verified at all.

If I had to make the session produce just one durable artifact, therefore, it would not be an AMA transcript or a question bank. It would be a **hypothesis ledger**: each belief about how TDS works, evidence for/against from the room, which student segment it came from, what existing telemetry can verify next, and what course decision changes if it is true. That turns this from another useful conversation into an iteration of the course's own scientific method.

---

## User

Based on the above, I'll split this into parts. In one part, I'll ask students questions and we'll discuss. What should the questions be? Also mention what I should listen for and how to evaluate the transcript. In another part, I'll ask them to fill out a form (see @LocalMCP ~/code/liveform) - write the form.yaml for me. Keep it short. Document the intent and predictions in the comments. One question should definitely be allowing them to ask me any questions - in fact, you can begin with that. In the third part, I'll do the other things that don't fall into either of these buckets. Tell me what to do here.

---

## ChatGPT

<details>
<summary>Worked for 6m 50s</summary>

I’ll make the three parts complementary: discussion for mechanisms and stories, form for quiet/anonymous breadth, and live exercises for observed behavior. I’m checking `~/code/liveform` so the YAML matches your actual schema rather than inventing one.

Inspected hidden tool content and downloaded Liveform schema output

Read the Liveform schema file

Designed IIT Madras prediction form and downloaded TDS skill file

Inspected TDS form instructions and sample schema

Inspected sample configuration and downloaded redirected command output

Inspected liveform sample contents

One implementation caveat matters: Liveform authenticates respondents, so I’m checking whether the raw TSV is identifiable. If it is, I would not tell students the form is “anonymous”; I’d say projected results are name-free and avoid inspecting identities for the dissent questions.

Designed a TDS survey and downloaded supporting files

Read saved privacy output

Validated redacted form configuration

The first schema check found a Liveform/YAML issue, so I’m fixing that before handing you the form. The design is unchanged; this is just making sure it actually loads in your repo.

Diagnosed hidden error output and downloaded validation file

Inspected liveform validation output

Validated Python setup and inspected validation output

Inspected validate2 output

Ran tests in the active UV environment

Parsed YAML configuration validity

Downloaded Form YAML from LocalMCP

Parsed local YAML form file

Created a Liveform recommendation form

</details>

- Attachment: liveform_schema.txt (Document)

- Attachment: tds_form_skill.txt (Document)

- Attachment: liveform_sample.txt (Document)

- Attachment: liveform_privacy.txt (Document)

- Attachment: liveform_validate.out (File)

- Attachment: liveform_validate2.out (File)

- Attachment: form.yaml (File)

I would make the three parts measure different things:

- **Discussion:** mechanisms, causal stories, counterexamples.
- **Form:** breadth from everyone, especially quiet students, plus paired comparisons.
- **Other:** observed behavior, sample-bias checks, and actual belief updating.

That matches the central unresolved questions in your notes: what kind of practitioner TDS produces, whether assessments reward the right things, and whether students internalize framing/orchestration/verification/collaboration rather than just passing tasks. tds_audit

## 1. Discussion: questions to ask students

I would not try to get through all of these. Pick a story, drill deeply, then move when you have understood the mechanism.

| Ask                                                                                                           | Listen for                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. “What is TDS actually teaching you?”**                                                                   | Do they name tools, grades, survival tricks, resourcefulness, framing, debugging, verification, collaboration, confidence? Don't reveal your answer first.                                                              |
| **2. “Tell me about the last TDS problem where you were properly stuck. What did you do, in order?”**         | Their **actual first move**. AI immediately? Read everything? Search? Experiment? Ask friend? Freeze? Then: how many strategy changes before success?                                                                   |
| **3. “At what point did you know your answer was right?”**                                                    | This is crucial. Tests, independent check, output looked plausible, AI said so, grader accepted it? Your course increasingly emphasizes verification design; see whether that habit exists without prompting. tds_audit |
| **4. “Give me one example outside TDS where you now approach a problem differently because of TDS.”**         | **Transfer.** “I now use `uv`” is weak. “I first make the problem testable / ask AI / try a small experiment / inspect the interface” is strong. Ask: “What would pre-TDS you have done?”                               |
| **5. “Tell me about something you got marks for without really understanding.”**                              | Your dangerous false-positive quadrant: successful student, no reusable mental model. Ask what happened when they encountered something similar later.                                                                  |
| **6. “Think of a smart, hardworking student you know who struggled badly in TDS. Why?”**                      | Hidden selection function. Prerequisites? Time? English? weak social network? intolerance of ambiguity? environment/setup? AI skill? motivation? This is more useful than “why do weak students struggle?”              |
| **7. “Tell me about the last time another student materially changed how you solved something.”**             | Did TDS create a learning network or merely allow copying? How did they find that person? What did the other person contribute: answer, explanation, strategy, confidence? Ask solo students why they remain solo.      |
| **8. “If AI became 10× better next term, what should I stop teaching? What must remain?”**                    | Their abstraction of durable competence. Particularly interesting if they want to retain things you currently think AI makes obsolete—or discard things you consider core.                                              |
| **9. “What do the students who are unusually good at TDS figure out that everyone else discovers too late?”** | Hidden curriculum. Often more actionable than complaints: scanning first, starting early, model switching, asking friends, understanding graders, testing, etc.                                                         |
| **10. “What should I believe differently about how students learn after talking to you today?”**              | Best closing question. Forces them to make a claim that updates your model rather than request a feature.                                                                                                               |

For questions 2–7, repeatedly use **“Tell me about a specific time.”** Abstract student opinions are cheap; reconstructed episodes are the useful evidence.

### What I would listen for across the whole conversation

The most important distinction is **self-initiated vs course-forced behavior**. “I verified because the question required a test” is different from “Now I automatically test AI outputs.” Likewise, collaborating because marks required token exchange is weaker evidence than spontaneously asking classmates on an unrelated problem.

Also listen for what is conspicuously absent. Your mental model predicts framing, AI use, experimentation, verification, collaboration and action. If students repeatedly describe successful problem-solving without mentioning, say, verification, that absence is useful evidence.

I would classify statements into four evidence levels:

1. **Strong:** concrete first-person incident, actions in sequence, outcome.
2. **Good:** before→after change with a concrete example.
3. **Weak:** general opinion (“TDS taught me problem solving”).
4. **Very weak:** hearsay about unnamed other students.

### How I would evaluate the transcript

Don't summarize it by themes or sentiment. Build a hypothesis ledger.

For every meaningful episode, extract:

`student → situation → first move → AI/tool/human used → failure → strategy change → verification → outcome → claimed lesson → evidence of transfer`

Then score these hypotheses separately as **supports / contradicts / ambiguous**:

- TDS causes students to attack unfamiliar problems more independently.
- Students learn transferable strategies, not merely TDS-specific recipes.
- AI-first has become a default behavior.
- Verification has become a default behavior.
- Collaboration has become genuine social learning.
- Difficulty is predominantly productive rather than sterile.
- Initially weaker/lower-agency students acquire these behaviors rather than being filtered out.

Prioritize **disconfirming cases** and differences between students. Three students describing the same mechanism independently matters much more than fifteen agreeing that “TDS is useful.”

Finally output only:
**What I believed → what the evidence now says → strongest contrary evidence → what I should change/test next term.**

---

## 2. Form

I kept it to **six questions per student**: there are seven definitions, but Liveform's `segment` mechanism randomly gives each person only one of the two difficulty questions.

The most useful paired measure is deliberately simple: **“what taught me” versus “what got me marks.”** Your own notes explicitly say exams tell students what to learn; this tests alignment directly. tds_audit

One important caveat: Liveform is **not technically anonymous**. `responses.tsv` stores email, name and IP. The projected results are name-free. So I would say, “I won't show names or use identities when discussing these answers,” not “this is anonymous.”

Download the validated `form.yaml`

```
# TDS AMA learning probe
#
# Intent:
# - Give every student, including quiet students, an equal channel before discussion.
# - Compare what students say drives LEARNING vs what drives MARKS.
# - Test whether students describe durable, tool-independent skills rather than TDS-specific recipes.
# - Separate productive struggle from sterile friction without asking every respondent both questions.
# - Surface assumptions about learning that the course team may not realize it is making.
#
# Predictions to score after the session (treat as hypotheses, not truths):
# P1. >=30% of respondents choose different answers for learn_source vs marks_source.
# P2. GAs/ROE, projects, AI, classmates, or support collectively dominate course content as learn_source.
# P3. >=50% of durable_skill answers describe a strategy/mental model (e.g. framing, debugging,
#     verification, resourcefulness, collaboration) rather than naming a specific tool.
# P4. The two difficulty-story variants will reveal both productive struggle and sterile friction;
#     sterile friction will often involve prerequisites/setup/evaluator ambiguity rather than the core task.
# P5. wrong_belief will surface at least one repeated assumption that is not visible in click/score logs.
#
# Important: Liveform's raw responses.tsv stores email/name/IP. Projected results are PII-free,
# but this is NOT technically anonymous. Do not promise anonymity; say names will not be shown
# during discussion, and avoid inspecting identities for the dissent questions unless necessary.

title: "TDS AMA: How are you really learning?"
description: |
  Please answer from **what you actually did**, not what you think the course team wants to hear.

  I will discuss aggregate/name-free results. There are no right answers.

auth:
  allowed_domains:
    - study.iitm.ac.in
    - ds.study.iitm.ac.in

results:
  embeddings:
    enabled: false

questions:
  - id: ask_anand
    field: textarea
    question: "Ask Anand anything."
    description: "TDS, AI, careers, course design, or anything else."
    maxlength: 600
    results:
      views: [responses, words]
      default_view: responses

  - id: learn_source
    field: single_choice
    question: "Which ONE contributed most to what you actually learned in TDS?"
    choices: &learning_sources
      - "GAs / ROE"
      - "Projects"
      - "AI tools"
      - "Classmates"
      - "TAs / live sessions / Discourse"
      - "Course content: videos / reading"
      - "Struggling on my own"
      - "Other"
    editable: false

  - id: marks_source
    field: single_choice
    question: "Which ONE contributed most to getting marks in TDS?"
    choices: *learning_sources
    editable: false

  - id: durable_skill
    field: textarea
    question: "If every specific tool in TDS disappeared next year, what skill from TDS would still be useful to you?"
    maxlength: 400
    editable: false
    results:
      views: [responses, words]
      default_view: responses

  # Split the room: each respondent sees exactly one difficulty question.
  # This keeps the form short while collecting evidence on both desirable difficulty and wasted friction.
  - id: useful_struggle
    field: textarea
    question: "Describe one painful TDS experience that taught you something you still use."
    maxlength: 500
    editable: false
    segment: difficulty-story

  - id: wasted_struggle
    field: textarea
    question: "Describe one painful TDS experience that taught you almost nothing."
    maxlength: 500
    editable: false
    segment: difficulty-story

  - id: wrong_belief
    field: textarea
    question: "What does Anand or the TDS team believe about how students learn that you think is wrong?"
    description: "Specific examples are especially useful."
    maxlength: 500
    editable: false
    results:
      views: [responses, words]
      default_view: responses
```

I would have them complete this **before you explain your mental model or reveal any results**. Otherwise the answers become reactions to your framing.

For `ask_anand`, reveal and use the responses as your AMA queue. For `wrong_belief`, I would only reveal responses after most people have submitted, to prevent conformity.

---

## 3. Everything else

Three things are worth doing because neither questions nor surveys can do them well.

### A. Observe them encountering novelty

This remains the highest-value experiment.

Give everyone an unfamiliar, objectively verifiable 5–7 minute problem. Say only:

> **Solve this. Anything goes.**

It should require almost no prerequisite knowledge and permit AI, web, classmates, code—whatever they want. Ideally it superficially looks unlike a TDS GA but rewards the same underlying behaviors.

Do **not** say you're testing AI use, collaboration or verification.

Everyone solves it. Then randomly choose a few students—not just volunteers—and reconstruct what they actually did.

The crucial observations are:

**first move → strategy switches → use of AI/people → verification.**

Your ROE telemetry already tells you that Ask AI and collaboration can be much lower than your intended behavior. tds_audit

This tests whether the intended habits transfer when no mark or instruction tells them to use those habits.

### B. Do prediction → reveal a few times

Before showing a known cohort statistic, make students predict it.

For example:

> “What fraction of your batch do you think regularly uses AI on TDS problems?”

Then show the real telemetry you already have.

Or:

> “Which TDS activity do you think has the strongest relationship with marks?”

Then show the actual data if you've analyzed it.

The **prediction error** tells you how representative each student's social bubble is. More importantly, the surprise creates a natural discussion: “Why did you think it was 80% when it was 30%?”

You can do the same to yourself: preregister 4–5 beliefs before the session, with a probability and:

> **If this is false, what will I change?**

That last clause prevents interesting surprises from becoming no-op observations.

### C. Audit your sample afterward

This one is essential.

Use the attendance roster and compare attendees with the whole batch on existing measures:

- marks/performance percentile
- engagement
- Ask AI usage
- assignment starting/submission patterns
- perhaps collaboration signals where available

Do this only at aggregate level.

Then your interpretation becomes:

> “The room was representative on marks but heavily skewed toward engaged/AI-heavy students.”

rather than simply “Students told me X.”

That directly addresses the largest threat to inference: **the people who attend an AMA are probably not the people for whom TDS works least well.**

Finally combine all three evidence streams:

**Form = what the room reports.
Discussion = why and how.
Novel task = what they actually do.
Existing telemetry = whether this room resembles the cohort.**

Where those disagree is where I would hunt hardest. For example, “everyone says they verify AI” + “almost nobody verifies the novel task” would be a much more valuable finding than any consensus answer.

A good 60-minute order would be: **5 min form → 10 min AMA questions → 20 min critical-incident discussion → 7 min novel task → 13 min debrief/counterexamples → 5 min reveal your current mental model and invite them to break it.**

form.yamlCodeOpen file

---

## User

The results are on @LocalMCP at ~/Documents/forms/tds-ama-2026-08/responses.tsv. Analyze them. Use the data-analysis skill as well as against your intent in creating the questions. But don't be restricted - based on the analysis, see what further thoughts emerge, follow them, and see what you find that's insightful. Share as Markdown, explaining the finding, why this is insightful and what the implications are, and what the evidence is (enough to verify.)

---

## ChatGPT

<details>
<summary>Worked for 9m 13s</summary>

I’ll treat the form as a small observational dataset, not as a survey to summarize. I’ll first reconstruct the intended hypotheses, check response coverage/segments/duplicates, then hunt for contradictions and subgroups—especially where “what teaches” diverges from “what earns marks,” and where open-text answers reveal mechanisms the multiple-choice questions missed.

Downloaded and analyzed survey responses and form YAML structure

Analyzed response data, YAML questions, latest answers, and choice distributions

The first strong signal is already much larger than the preregistered expectation: among 37 students who answered both questions, **25 (68%) named a different source for learning than for marks**. More strikingly, GAs/projects dominate “what taught me,” while AI/classmates dominate “what got me marks.” I’m now checking whether the free-text answers make this look like healthy real-world leverage or an assessment-design failure.

Analyzed student learning, grading perceptions, response patterns, and statistical comparisons

A second strong result is emerging from the free text: the course seems to be teaching **adaptive problem-solving**, but students almost never name **verification** as a durable skill. Across 70 latest open-text answers to the learning/struggle/dissent questions, I found zero spontaneous uses of “verify,” “validate,” “test,” or “check,” despite verification being central to the intended TDS model. Debugging appears; explicit epistemic checking does not.

Analyzed conversation files and found quotes on AI fundamentals and TDS mindset

Analyzed AI learning beliefs and grade outcomes

Evaluated student reflections for verification mindset

Analyzed prediction outcomes and Durable Skills by learning source

</details>

- Attachment: responses.tsv (File)

- Attachment: form.yaml (File)

# TDS AMA form analysis

I treated `responses.tsv` as append-only and used each student's latest response per question, matching Liveform's own “latest answer wins” behavior. liveform_privacy

There were **40 distinct respondents**. The two main choice questions had 37 responses each; `durable_skill` 24; `wrong_belief` 20; and the split difficulty prompt had 16 useful-struggle + 10 wasted-struggle responses.

The form was designed to test five explicit hypotheses: learning vs marks divergence, question-driven learning, durable meta-skills, productive vs sterile difficulty, and hidden assumptions about learning. form

My overall read is:

> **TDS seems to be successfully teaching adaptive problem-solving through the assessments. But students experience AI and classmates more as mechanisms for getting marks than for learning, and the intended habit of verification is conspicuously absent. The deepest unresolved tension is no longer “should students use AI?” but “when are they producing, and when are they practising?”**

## 1. There are almost two different curricula: what teaches you, and what gets you marks

This was the cleanest result.

| Primary source                     | What taught me    | What got me marks |
| ---------------------------------- | ----------------- | ----------------- |
| **GAs / ROE + Projects**           | **20 / 37 = 54%** | **8 / 37 = 22%**  |
| **AI + classmates**                | **9 / 37 = 24%**  | **25 / 37 = 68%** |
| Course content + TA/live/Discourse | 4 / 37 = 11%      | 1 / 37 = 3%       |
| Struggling alone                   | 4 / 37 = 11%      | 3 / 37 = 8%       |

And this is genuinely paired evidence: **25 of the same 37 students — 68% — gave different answers for learning and marks**. Our preregistered prediction was merely ≥30%. The 95% Wilson interval within this room is roughly 51–80%, so this is not a borderline result.

There is an even cleaner asymmetry. All 9 students who said AI/classmates were their main learning source also said AI/classmates were their main marks source. But **another 16 students shifted into AI/classmates only when asked about marks**. Conversely, 20 students said GAs/projects taught them most, but only 7 kept GAs/projects as their marks answer.

### Why this is insightful

It would be easy to label this “assessment misalignment,” but I think that is too simplistic.

Your course explicitly allows and encourages real-world reuse, AI and collaboration. So perhaps marks are partly measuring **resource orchestration**, while the experience of wrestling with the GA is where the learning occurs. That is coherent with the intended production-first design. tds_audit

But it does mean an individual TDS score cannot automatically be interpreted as “this person personally understands everything they got right.”

The surprising sub-result is **Projects**: 4 students chose Projects as the single biggest source of learning; **zero** chose Projects as the biggest source of marks. Small n, but worth investigating. Projects may be disproportionately learning-rich.

### Implication

I would preserve the open-resource assessment model, but explicitly separate two constructs:

**Can you get the result using the world?** versus **what capability has become yours?**

The first is valuable professional competence. The second needs a different measurement mechanism—micro-viva, transfer question, unfamiliar task, or “how do you know?” probe.

---

## 2. The “questions are the content” experiment appears to be working

Only **2/37 students (5%)** named videos/readings as their main learning source. **16/37 (43%) named GAs/ROE**, with another 4 naming Projects.

That is unusually consistent with your deliberate shift away from content delivery toward question-driven learning.

More importantly, among the 13 `durable_skill` respondents who said GAs/ROE taught them most, **11 described a transferable meta-skill rather than a narrow task/tool**.

One student summarized the durable outcome as:

> “Problem-solving and the ability to break a problem into smaller steps … instead of depending on a particular tool.” responses

Another described collaboration, prompting, problem-solving, asking the right questions, and efficient use of available resources. responses

### Why this is insightful

This suggests GAs are not merely testing learning created elsewhere. **They are themselves the learning environment.**

That changes the optimization target. A “good question” should not merely discriminate high from low performers or resist one-shot AI. It should cause a useful strategy change.

### Implication

Spend disproportionate design effort on **what behavioral lesson a question induces**. Course pages can increasingly become support infrastructure around that.

This also means a hard GA bug is pedagogically more expensive than a typo in reading material: you are corrupting the lesson itself.

---

## 3. The durable skills prediction passed — but a core intended skill is missing

I coded the 24 `durable_skill` answers conservatively.

I counted an answer as a transferable strategy only if it named something portable across changing tools: decomposition/problem-solving, persistence/resourcefulness, adaptation, searching/synthesizing resources, debugging, communication/collaboration, or broader thinking. I did **not** count pure “AI prompt engineering,” named developer-tool skills, deploying websites, or vague answers.

By that strict definition, **17/24 = 71%** named a transferable strategy. Our prediction was ≥50%. A looser definition that treats prompting as a cross-model strategy raises it further.

So the important hypothesis is supported: students are extracting something above the tool layer.

But there is a far more interesting absence.

Across all **70 latest free-text responses** to `durable_skill`, `useful_struggle`, `wasted_struggle`, and `wrong_belief`:

**“verify” / “verification”: 0
“validate” / “validation”: 0
“test”: 0
“check”: 0**

“Debug” does occur repeatedly—7 responses—but no student spontaneously describes **proving that an answer is right**.

That is striking because your current TDS design explicitly names **Verification design** alongside framing, context engineering and orchestration. tds_audit

### Why this is insightful

This is exactly the sort of missing observation the form was meant to detect.

Students clearly have a story about:

**problem → AI/tools → persistence/debugging → answer**

I see much less evidence that their internalized story is:

**problem → hypothesis → answer → independent check → confidence**

That distinction matters more as AI gets better. Generating becomes cheaper; knowing when to trust generation becomes more valuable.

### Implication

I would make **verification a named behavioral invariant**, not merely something embedded in evaluator design.

After many questions, ask just:

> **How do you know?**

And periodically make the _verification method itself_ the graded answer.

I would also explicitly label the reusable skill after a question: “This was not a Curl question. This was a verification-under-uncertain-output question.” The students appear to be acquiring behaviors faster than they are acquiring your abstraction vocabulary.

---

## 4. The biggest student tension is “AI capability vs foundational capability”

This emerged independently in both the dissent question and the unrestricted “Ask Anand anything,” which makes it more credible than if we had directly asked about AI dependence.

Among the 20 `wrong_belief` responses, 8 were essentially neutral/unclear. Of the 12 substantive disagreements:

**6** argued that AI/copying/solvers can bypass understanding or foundations.

**4** argued that prolonged struggle without guidance is not necessarily learning.

The remaining two challenged LLM grading of subjective work and the assumption that students read every instruction.

One student said that without practising basic coding manually, students may become dependent on LLMs without understanding harder material. responses

More revealingly, students raised the same issue when given a completely open question:

> “I am using AI now for all coding task … am I detaching myself from learning?” The student contrasts this with coworkers who already acquired manual coding experience before AI. responses

Another asks, almost perfectly:

> “For GAs i'm prompting LLM, getting answer and pasting. What do i learn from TDS?” responses

And one describes **TDS behavior transferring into another course**: they had to resist automatically pasting Java assignments into an agent. responses

### Why this is insightful

The last example is especially important.

You wanted transfer. **Transfer happened.**

But what transferred was apparently the simple heuristic **“delegate to AI”**, not necessarily the more nuanced policy **“decide what should be learned versus delegated, then verify.”**

So “Use AI first” may be _too successful_ as a memorable rule.

At the same time, this is not evidence that AI is preventing all learning. Among the 7 `durable_skill` respondents who said AI was their primary source of marks, **6 still gave a strict transferable/meta-skill answer**. AI-mediated success and genuine learning can coexist.

### Implication: distinguish production mode from practice mode

I think the data suggests a useful new framing.

In **production mode**, the objective is “get a robust result efficiently.” Use AI, classmates, solvers, docs—everything.

In **practice mode**, the objective is “install a capability in my head.” Artificial constraints can be justified: do one manual rep; predict before asking AI; explain the mechanism; solve without the solver.

TDS mostly operates in production mode. That is distinctive and valuable. But students need to know **which primitives you expect them to possess underneath the automation**.

Otherwise they are forced to infer the delegation boundary themselves—and the survey says they are unsure.

---

## 5. “Desirable difficulty” is not a property of a question

GA5 Q11 is almost a natural experiment.

One student calls it a “huge pain,” but says it caused them to discover Claude Code and permanently changed their tool choice. responses

Another says:

> “tds ga5 q11 challenge me to change my approach for solving a problems.” responses

But a third says they spent **4–5 days with Claude**, eventually used another student's solver, and concluded that the time was “lost without anything useful.” responses

A fourth student thought GA5/9/11 were so interesting that TDS could be made _more_ difficult. responses

### Why this is insightful

The same task can be:

**transformative → challenging → enjoyable → sterile**

depending on the learner's state.

So asking “Is GA5 Q11 too hard?” is probably the wrong design question.

A better question is:

> **At what point does productive search turn into unproductive looping, and can the course detect that transition?**

One dissent response describes exactly the mechanism: long struggle can mean repeatedly debugging the wrong approach rather than learning the underlying concept. responses

### Implication

Do not necessarily make such questions easier.

Give them **escape hatches that preserve the learning**: after N failed attempts or X minutes, reveal a diagnostic hint, a different representation, the prerequisite concept, or a question such as “What assumption have you not tested?”

You can preserve the hard part while truncating the sterile tail.

This partially contradicts our P4 prediction. We expected sterile difficulty to be mainly setup/prerequisite/evaluator friction. Some was—server-side errors, lost saved work, format/output chasing—but AI looping and insufficient conceptual scaffolding were just as important.

---

## 6. Classmates are disproportionately perceived as a way to score, not a way to learn

Only **2/37** students named classmates as the single biggest source of learning.

But **9/37** named classmates as the biggest contributor to marks.

That does not mean classmates aren't teaching. The free text gives counterexamples. One student says lack of collaboration made unfamiliar concepts much harder and that discussions with classmates unlocked understanding. responses

Another explicitly says that **helping other students improved their own understanding**. responses

### Why this is insightful

Your collaboration mechanism may currently be better at creating **social infrastructure and answer flow** than making students consciously recognize peer learning.

That matters because “get a solver from somebody” and “explain your mental model to somebody” are both collaboration, but pedagogically very different.

### Implication

Don't reduce collaboration. Instead, occasionally make the valuable unit of exchange an **explanation, diagnosis, test or teaching artifact**, not an answer.

That might convert collaboration from primarily marks infrastructure into a consciously reusable learning strategy.

---

## 7. There is at least one signal of very deep transfer

One response to productive struggle says:

> “AI can do a lot but it still needs guidance at times, so is with people if you have some working under you. So YOU always have to be clear with what is happening…” responses

This is almost independently rediscovering your January framing that as agents do implementation work, the human increasingly becomes the manager/orchestrator.

I would not generalize from one response. But I would keep it as an **exemplar of what success looks like**.

The student is no longer saying “I learnt Claude.” They have formed a portable theory about delegation and management.

That is qualitatively deeper than tool proficiency.

---

## How the five predictions did

| Prediction                                                                     | Result                                                                              | Assessment                                                                               |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **P1:** ≥30% give different learning/marks sources                             | **25/37 = 68%**                                                                     | **Strong pass. Much larger than expected.**                                              |
| **P2:** GAs/projects/AI/classmates/support dominate content as learning source | **31/37 = 84%**, versus 2/37 content                                                | **Pass, though the prediction bundled many categories and was too easy to pass.**        |
| **P3:** ≥50% durable answers are meta/tool-independent                         | **17/24 = 71% strict coding**                                                       | **Pass.**                                                                                |
| **P4:** Both productive/sterile struggle; sterile often setup/prereq/evaluator | Both clearly present; operational/evaluator friction is only one major sterile mode | **Partial pass. AI looping and missing scaffolding were more important than predicted.** |
| **P5:** repeated hidden wrong assumption                                       | **Yes:** AI can bypass foundations (6); struggle ≠ learning without feedback (4)    | **Strong pass.**                                                                         |

The predictions and intended measurements are in the form comments. form

## What I would update in the TDS mental model

Before this survey, my best summary was roughly:

**TDS builds adaptive competence: frame unfamiliar problems, use AI/tools/people aggressively, orchestrate, verify, and ship.**

The evidence makes me modify that:

> **TDS is demonstrably producing adaptive, resourceful problem-solving in at least some engaged students. Its assessments appear to be the main learning mechanism, while AI and peers are the main performance leverage. But the students have internalized “use resources / persist / debug” much more visibly than “verify,” and they do not yet have a clear shared rule for what humans should learn versus delegate.**

The most important pedagogical experiment I would run next is therefore not “less AI vs more AI.”

It is:

> **Can you teach an explicit Learn / Delegate / Verify decision rule, and does that reduce AI-dependence anxiety while preserving the extraordinary resourcefulness TDS seems to create?**

The biggest caveat is selection. These are **40 live-session respondents**, probably an engaged survivor sample, and only 20–24 answered some of the deeper free-text questions. The form was also name-linked in storage even though displayed results were name-free. So I would treat the percentages as evidence about _this room_, not the whole course. The next high-value analysis would be to join these respondents, at aggregate level, to their GA/ROE performance and AI-use/engagement telemetry and ask whether the room—and especially the students expressing each mental model—are top, middle, or struggling students.

---

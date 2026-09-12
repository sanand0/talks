---
title: Day 5 ChatGPT Chats
---

# Student Learnings

Source: https://chatgpt.com/c/6aa36aa2-a428-83ec-9c27-e8c26fd376c9

## User

Students have shared their learnings as part of the process. I'd like you to go through this and identify the top learnings that have high impact and high frequency and sort based on that. Roughly give me the top five learnings across the students based on impact and frequency.

## ChatGPT

I found 9 usable student learnings videos. Across those, five themes stand out when weighting both independent frequency and how consequential the lesson is for AI-era product building.

| Rank  | Learning                                                                           | Frequency | Impact    | Why it matters                                                                                                                                                                                                   |
| ----- | ---------------------------------------------------------------------------------- | --------: | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **AI can do much of the execution; human judgment becomes the bottleneck.**        |    ~7–8/9 | Very high | Students repeatedly found that AI could code/build rapidly, but humans still had to decide what was correct, useful, realistic, worth prioritizing, and trustworthy.                                             |
| **2** | **AI dramatically lowers the barrier to building software.**                       |      ~7/9 | Very high | Several students explicitly built things beyond their programming ability. The shift was from “Can I implement this?” to “Can I specify, inspect and improve this?”                                              |
| **3** | **Clear purpose and specific instructions matter much more than vague prompting.** |      ~6/9 | High      | When students knew the user, purpose and desired behavior and stated these clearly, agents worked well. Ambiguity caused assumptions, loops and repeated correction.                                             |
| **4** | **Real-world constraints should change the product, not merely be worked around.** |      ~6/9 | High      | API costs, model limits, deployment restrictions, unreliable GPS, security and deadlines forced students to simplify, postpone AI features, or completely pivot.                                                 |
| **5** | **Real users expose problems that AI and the builder do not see.**                 |      ~5/9 | Very high | Confusing UI, unclear buttons, difficulty, emotional reactions and usability problems emerged through actual use. Students learned that AI personas and self-testing are useful, but not substitutes for people. |

A little more detail on each:

**1. “The scarce skill is judgment, not coding.”** This was probably the strongest overall learning. Kosei said even AI-created output ultimately needs human verification. Nanami said AI can generate ideas and build quickly, but humans must decide whether the result is actually useful. Noa described their role as testing, identifying problems and ensuring final quality. Yuri went further: humans must define purpose, evaluate feedback, set priorities and decide **what not to build**. Christopher and Hinata reached the same point from the opposite direction: when intent or human intuition was missing, AI confidently produced plausible but wrong behavior.

**2. “I can now build things I couldn't previously build.”** This is perhaps the biggest change in student capability. Kosei explicitly said useful websites can be built without specialized skills. Nanami said she could turn ideas into reality despite limited programming knowledge. Mio said AI handled programming she could not do herself. Christopher observed that Claude created most of the application without his needing technical detail. Johan built/deployed something well beyond his previous server experience. Noa and Yuri emphasized the speed multiplier. This is a deeper learning than “AI saves time”: **implementation capability is becoming much less dependent on prior technical skill.**

**3. “Say what you mean—especially the purpose.”** Christopher's concise formulation was: if you do not specify something, **the AI will assume**. Mio discovered that an idea perfectly clear in her own head could produce repeated wrong corrections until she stated exactly what differed and what needed changing. Johan found that moving from a broad request to specifications, and sometimes checking the proposed prompt/plan before execution, avoided iterations. Hinata had to explicitly reduce the home page to four buttons. Yuri repeatedly pulled the agent back to the product's true purpose: “help users take action today.” This is less about clever prompt syntax and more about **clarity of thought**.

**4. “Constraints are product information.”** This appeared surprisingly often. Hinata abandoned a real AI integration because API use cost money. Johan changed his architecture because of API keys/paid services and exhausted credits while overusing a stronger model. Christopher discovered his AI-enabled Claude artifact could not be shared as expected. Noa ran into Codex usage limits. Yuri deliberately postponed a production AI API after evaluating deadline, usage limits, cost, security, key management and reliability. The strongest example was Miku: GPS didn't work, the AI kept repeating ineffective advice, so she **discarded the first product direction and rebuilt around photos instead**. That is a valuable product-management lesson: don't fetishize the original implementation.

**5. “Users reveal reality.”** Kosei changed the product based on actual-user feedback. Mio made the distinction particularly clearly: AI can check functionality, but humans reveal things like confusion, poor visibility and even whether looking at the product feels pleasant. Nanami discovered difficulty/confusion through use and feedback. Noa found issues and opportunities they had not noticed themselves. Yuri said observing users was especially valuable because their **actions** revealed problems she couldn't find herself, and ended with a concrete behavioral test: can a new user begin an action within three minutes unaided?

One thing I would highlight when presenting this back to the class: **the students have independently rediscovered much of the philosophy of the course.** They did not mainly come away saying “I learned ChatGPT/Codex/Claude.” Their common story is closer to:

> **AI made building cheap. That made purpose, judgment, communication, testing, user observation and willingness to change direction more important.**

That is probably the single synthesis I would put on a slide.

A notable near-miss for the top five is **“when an agent gets stuck, change the interaction rather than endlessly arguing with it.”** Miku learned to start a fresh chat with the existing code; Johan used plan/prompt approval before execution; Christopher noticed correction loops caused by compounding assumptions. It is very actionable, but less frequent and somewhat narrower than the five above.

# Learnings from Prompts

Source: https://chatgpt.com/c/6aa36397-f4d4-83ec-a7f1-03a1c14e2eef

## User

[https://docs.google.com/spreadsheets/d/1069Qs1tt_fuSDJryagebnFLIyG-KqRoni-nyLYml4pc/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1069Qs1tt_fuSDJryagebnFLIyG-KqRoni-nyLYml4pc/edit?gid=0#gid=0)

The sheet above has a column which has the chat logs that students have used to create the applications. What are patterns of prompting that have worked well? What are patterns of promptings that have not worked so well? And what can we learn based on the effectiveness of these prompts and how the agents have executed and interpreted them? What I'd like you to do is create the top five most prioritized lessons that could be used as a meta prompt. That is, I want a prompt that has up to five prioritized rules that I can just copy-paste before creating any new application, and it should automatically make sure that I avoid these kinds of mistakes, or anyone who uses this can avoid the kinds of mistakes that were made in this application or development process, or automatically leverages the best practices that were visible across these. Don't put in things that agents would already know, or people would already know. Put in what is unusual about this. That's specifically what I want you to hunt for. Feel free to use [LocalMCP](/plugins/plugin_asdk_app_69e6c604b4ec8191b8e14bb9e8d7cd52?plugin_detail_origin=inline_selection_pill), and these are already open as tabs on my browser, so you can inspect the browser tabs and get the results if you wish.

## ChatGPT

I reviewed the sheet and the accessible development traces for Yuri, Kosei, Noa, Hinata, Nanami, Mayu, Miku, Christopher, and Dora. The strongest finding is that the highest-value prompts were not more detailed specifications; they changed the agent’s operating procedure.

For example, Yuri’s “my detailed instructions may be wrong; find the better question” caused a substantial product reframe from a conventional learning roadmap to a much sharper “help me take the first step today” experience. Dora’s debugging prompt—trace the route through each transformation, locate the exact failing stage, then create a regression test before fixing—was exceptionally effective: it isolated the OSRM routing failure and the resulting test caught a second bug introduced by the first fix. Christopher’s VC app showed the opposite: “make it impressive, interactive, and publish it” resulted in a polished private Claude artifact that fundamentally failed the shareability requirement. Noa similarly had “route search” reported as implemented before a user discovered that the core flow did not actually work.

Another repeated behavior was that agents are extremely willing to satisfy local requests while degrading the whole. Nanami’s fishing app accumulated dozens of successive additions; Miku’s app improved when features were deleted and several entry points were merged into a single “Record your journey” flow. Agents also happily substitute approximations when blocked: Nanami’s explicit “a sample result is fine, but say clearly that it is a sample” worked very well, while other apps needed later corrections around simulated AI, estimated data, or current-data provenance.

So I would use this as the reusable prompt. It deliberately omits generic advice like “write clear requirements,” “make it responsive,” or “test your code.”

You are building an application with me. These rules have higher priority than my individual feature requests. Apply them automatically rather than merely reminding me about them.

1. **Treat my proposed solution as a hypothesis, not the specification.** Before substantial implementation, infer the actual user outcome and the smallest interaction loop that produces it. If my requested feature, workflow, or architecture is a worse way to achieve that outcome, change it rather than obediently implementing it. My being specific is not evidence that I am right.
2. **Prove the riskiest assumption end-to-end before polishing anything.** Identify what could make the whole app useless despite otherwise good implementation—e.g. public sharing, anonymous access, authentication, external APIs/data, persistence, mobile use, or the core user action. Build the thinnest vertical slice that tests this first, and verify it as a fresh real user would. A successful build, type-check, or claim that something was “implemented” does not count as verification.
3. **When something fails, trace before you tweak.** Do not immediately redesign, patch the UI, or guess at the cause. Reproduce the failure and trace the exact path from user input → transformations/state → external/API result → displayed result. Identify the first stage where reality diverges from expectation, capture that real failing example as a regression test, then fix it and rerun the test. Preserve the test so the same class of failure cannot quietly return.
4. **Never blur reality and simulation.** For every data-, prediction-, or AI-powered behavior, know whether its output is **live/verified**, **derived/estimated**, or **simulated/sample**. If the real API, data, or model is unavailable, an honest simulation is acceptable—but label it clearly and never make it look like live AI or current factual data. When conclusions depend on external evidence, expose the provenance and important assumptions.
5. **Treat feedback as a reason to re-integrate, not merely to add.** Translate each feedback item into the observed behavior and desired outcome, then decide whether to keep, change, delete, or merge something. Before adding another feature, inspect the whole core journey for duplicate entry points, accumulated clutter, conflicting concepts, and features that now distract from the main value. Prefer deletion and consolidation when they make the core flow clearer. After each meaningful feedback batch, rerun the complete core journey rather than testing only the newly edited component.

When evidence or feedback is supplied only through something you cannot actually access, say so rather than inventing what it contains; obtain the actual text, screenshot, trace, or reproducible behavior before acting on it.

The two rules I would most want students to internalize are **#1 and #3**. #1 prevents an agent from becoming an extraordinarily efficient builder of the wrong product. #3 exploits something agents are unusually good at: once forced to inspect an instrumentable failure rather than speculate, they can often diagnose and permanently eliminate bugs far better than a sequence of “try fixing this” prompts.

## User

Is there a big difference in the applicability of some of these prompting lessons, those who are using Claude versus those who are using ChatGPT? Even if there is a clear, indicative, directional difference, let me know. It doesn't matter if it's not statistically significant. It's not like we have a large number of data points. But do share the clearest signals that you find and tell me how confident you are. Based on this, I might take some of these separately and say use these prompting lessons primarily when working with Claude. However, don't try to invent a signal when there is none. If there isn't a major difference and it really seems to be all over, then just say so. That's fine.

## ChatGPT

Yes. There are a couple of directional differences worth separating, but most of the five lessons are genuinely cross-platform.

The clearest split is this:

| Lesson                                                          | More important for                          | Signal                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Confidence                    |
| --------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| Trace failure end-to-end → regression test → fix                | **Claude, especially Claude Code**          | Dora’s route app improved dramatically only after explicitly forcing Claude to instrument the pipeline and identify the failing stage. Claude then turned the real failure into tests, and those tests caught a second bug in Claude’s own first fix. This is an unusually strong Claude Code workflow because it has excellent access to files, tests, browser instrumentation and shell tools.                                                                                | **High**                      |
| Prove the riskiest assumption before polishing                  | **Claude**                                  | Christopher got a sophisticated, attractive VC app before discovering the Claude Artifact could not actually be shared publicly. Dora similarly spent a surprising amount of effort fighting deployment constraints after the app worked locally. ChatGPT Sites students generally got a genuinely public site much more directly.                                                                                                                                              | **High**                      |
| Treat my proposed solution as a hypothesis                      | **Slightly more useful with ChatGPT**       | The ChatGPT/Codex traces repeatedly show rapid literal execution of successive requests. Yuri’s exceptional prompt — essentially “my instructions may be wrong; find the better question” — produced one of the biggest qualitative leaps in the whole corpus. Without that instruction, ChatGPT tends to be very good at efficiently elaborating the current conception.                                                                                                       | **Medium**                    |
| Explicitly distinguish real / estimated / simulated             | **Slightly more useful with ChatGPT Sites** | Several ChatGPT apps naturally drifted into convincing simulations when real capabilities were unavailable: heuristic “AI” pet advice, sample fish recognition, template-based recommendations, estimated/current-data issues. They generally disclosed this when prompted, but the polished UI makes the distinction particularly easy for users to miss. Claude also does this, but Christopher’s Claude implementation explicitly built “Practice Mode” as a named fallback. | **Medium**                    |
| Re-integrate feedback; delete/merge rather than continually add | **Both**                                    | Feature accretion happened in both environments. Miku’s ChatGPT app became substantially better when entry points were consolidated and features removed. Dora’s Claude project also accumulated complexity and needed consolidation. I don't see a meaningful platform split here.                                                                                                                                                                                             | **High that it is universal** |

There is also a broader behavioral difference underneath these.

**Claude Code seems especially good when you give it a scientific debugging protocol.** “Don’t change anything yet. Instrument A→B→C→D, tell me where the divergence begins, freeze that example into a test, then fix it” unlocked capabilities that were much less visible in the ordinary feature-building conversations. Claude did not merely follow the instruction; it used the environment aggressively—network interception, internal state inspection, fixture capture, pure-function extraction, mocked orchestration tests, live re-verification. I would definitely teach this as a **Claude Code power prompt**.

Conversely, **ChatGPT Sites/Codex seems especially good at collapsing the distance from idea → edited app → published app**. That is valuable, but it creates its characteristic failure mode: the user can get several rounds of apparently successful iteration before anybody asks whether the fundamental product concept is right. Yuri’s “assume my detailed instruction itself may be misguided” prompt therefore looks disproportionately valuable there. It effectively converts ChatGPT from _very fast implementer_ into _product collaborator_.

I would therefore split the original meta-prompt only modestly.

For **Claude Code**, I would strongly emphasize:

> **Before fixing a failure, instrument it. Trace the real failing example from input through every transformation, external call and rendered output. Find the first divergent stage. Turn that exact failure into a regression test before changing the implementation; then fix and rerun both the test and the real scenario.**

And:

> **Before investing in polish, prove the hardest environmental assumption end-to-end—especially deployment, sharing, authentication, browser restrictions and external APIs. A locally working implementation or private Artifact is not proof of a deployable product.**

For **ChatGPT/Codex/Sites**, I would especially emphasize:

> **My requested feature is evidence about the outcome I want, not necessarily the correct solution. Before making a substantial change, ask yourself whether implementing my request literally improves the core user outcome. If a simpler deletion, merge, workflow change or different concept is better, do that instead.**

And probably retain:

> **Never allow polished UI to obscure whether something is live, inferred or simulated. Label simulated/sample behavior at the point where the user experiences it.**

I would **not** split the “feedback means re-integrate, not add” rule. Nor would I claim Claude intrinsically reasons more deeply or ChatGPT is intrinsically more literal from this sample—the environments and assignments are too confounded for that. The more defensible conclusion is about the **workflow affordances**: Claude Code rewards debugging/test protocols unusually strongly; ChatGPT Sites rewards product-reframing guardrails unusually strongly because implementation and publishing are so frictionless.

# Other Assets

Source: https://chatgpt.com/c/6aa36b81-2410-83ec-a8f8-65a96b1648f2

## User

Okay, it looks like we have some interesting data here. One of the things that I've already done is had ChatGPT scan all of this material and identify what are the top prompting lessons that students can take based on their own sessions. A second session that's currently running is what are the top lessons overall that students have learned, prioritized based on impact and frequency. These are a couple of, let's say, meta assets or reusable assets that ended up coming from this data. I'd like you to ideate, brainstorm, and think about what are the other most promising assets that we can build out of this. In fact, if—and I'm just thinking aloud here—we treat this as two objectives. One, the students should be able to learn based on each other's work as much as possible. That's one objective. Second, in the future, if we want to create a new product out of it, then we should have some interesting assets that could serve as evidence or starting points for that. So yeah, brainstorm and give me the most novel as well as impactful ideas so that I can execute them one by one.

## ChatGPT

The strongest direction is to stop thinking of this as “13 student projects” and start thinking of it as a **small longitudinal dataset of humans learning to build with agents**. You have traces from intent → AI interaction → user feedback → revision → final product → reflection. That combination is much rarer than the individual artifacts.

I’d prioritize the assets like this:

| Rank   | Asset                                                        | What you build                                                                                                                                                                                                                            | Why students would care                                                                                                           | Longer-term product/research value                                                                                                                                    | Novelty / effort            |
| ------ | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| **1**  | **Do synthetic users predict real users?**                   | Compare each student's AI-persona/agent research with the later human feedback. Tag issues as predicted, missed, false alarm, or newly discovered. Compute precision/recall-ish measures and show examples.                               | Teaches exactly when “ask an AI to simulate users” is useful versus dangerous.                                                    | A genuinely interesting **synthetic-user validation benchmark**. Could become a methodology/product for companies using AI personas for UX research.                  | **Very high / medium**      |
| **2**  | **Human Intervention Atlas**                                 | Mine chat logs for every consequential moment where the student had to correct, redirect, constrain, verify, restart, or override the agent. Classify _why_, what they did, and whether it worked.                                        | Probably the best way to learn “how to manage something smarter than you.” Students see dozens of concrete intervention patterns. | Dataset/benchmark for **when agents need human judgment**. Could evaluate models, scaffolds, IDE agents, or supervisor agents.                                        | **Very high / medium-high** |
| **3**  | **Feedback → Change → Outcome graph**                        | Connect each piece of human feedback to what the student changed, ignored, or misunderstood; then look for evidence of whether the change helped.                                                                                         | Teaches product judgment rather than “implement every feature request.”                                                           | Basis for a **feedback-triage/product-manager agent**: given feedback, decide what to do and why.                                                                     | **High / medium**           |
| **4**  | **“Why isn’t this just ChatGPT?” benchmark**                 | Identify each app's core job. Give the exact same job to vanilla ChatGPT/Claude and compare task success, friction, consistency, repeatability, data integration, UX, etc.                                                                | Forces a deep understanding of what makes an AI _product_ rather than a prompt wrapped in UI.                                     | A useful corpus of **when specialized AI products beat general assistants**—valuable for product discovery and investment decisions.                                  | **Very high / medium**      |
| **5**  | **Failure Museum + Rescue Playbook**                         | Extract the 30–50 most instructive failures: prompt/context failure, agent loop, deployment failure, wrong assumption, hallucination, UX confusion, overbuilding, bad research, etc. Show failure → diagnosis → fix → prevention.         | Failures become reusable case studies rather than embarrassing footnotes. Likely more memorable than the success stories.         | Training corpus for diagnosing AI-development problems. Could seed an “agent debugger/coach.”                                                                         | **High / medium**           |
| **6**  | **Personalized peer curriculum**                             | For each student, recommend exactly 3 classmates to study: one who solved their weakest area well, one who took a contrasting approach, and one whose failure they are likely to encounter next. Point to exact transcript/video moments. | Much better than “look at everybody's projects.” Each student gets a custom 20–30 minute learning path.                           | Prototype for personalized cohort learning: **learn from the people immediately around you**, automatically.                                                          | Medium / **low-medium**     |
| **7**  | **Before/After Gallery: What actually changed the product?** | Produce a visual card per major iteration: before screenshot → evidence/feedback → decision → after screenshot. Rank by how consequential the change was.                                                                                 | Makes product iteration visible at a glance. Excellent class wrap-up material.                                                    | A reusable representation of product evolution that could power case-study generation automatically.                                                                  | Medium-high / medium        |
| **8**  | **Cheap Evidence Cookbook**                                  | Across the 13 products, identify each important claim and the cheapest convincing test students could/should have run. “For this class of claim, this 5-minute test gives you most of the evidence.”                                      | Teaches the hugely transferable skill of making verification cheap.                                                               | Could grow into an **evaluation-plan generator**: product/claim → recommended evidence/tests.                                                                         | High / medium               |
| **9**  | **Agent challenge-state benchmark**                          | Extract 30–100 moments from logs immediately _before_ the student had to intervene. Give a new agent only the state up to that point and ask it what to do next. Score whether it avoids the original failure.                            | Students can see which interventions today's agent could have handled itself.                                                     | This becomes more valuable over time: rerun the same challenge states on GPT-6, Claude 6, etc. A longitudinal measure of **where human supervision is disappearing**. | **Very high / high**        |
| **10** | **How many users do you actually need?**                     | Compare feedback #1/#2/#3. Measure overlap, genuinely new discoveries, repeated issues, and marginal useful information from each additional reviewer. Split AI personas vs classmates vs other users where possible.                     | Teaches students when more feedback is adding signal versus repetition.                                                           | Small but interesting evidence around **feedback saturation** and optimal UX-research cost.                                                                           | High / low-medium           |
| **11** | **Trust Ledger**                                             | For every product, extract its explicit/implicit claims and make a ledger: claim → evidence → counter-evidence → confidence → known limitation. Compare that with what the student says in the final video.                               | Teaches calibrated confidence and accountability.                                                                                 | Strong primitive for automatic **AI-product due diligence / evidence auditing**.                                                                                      | High / medium               |
| **12** | **Course Concept → Behavior map**                            | Take the things you taught—delegate aggressively, record feedback, why app vs ChatGPT, tests as fences, don't hide failures, etc.—and find actual student behaviors that demonstrate or contradict each one.                              | “Here is what this lesson looks like in real work,” using their own cohort.                                                       | Evidence for redesigning the course based on which concepts transfer into behavior and which remain slogans.                                                          | Medium-high / medium        |
| **13** | **What does a useful agent trace really need to contain?**   | Compress long chat logs into tiny decision traces containing only goal, important agent moves, human interventions, evidence, decisions and outcome. Test whether evaluators reach the same judgment from compressed vs full traces.      | Lets students understand their own process without rereading huge sessions.                                                       | Interesting **provenance-compression** problem. Useful if agent histories become enormous in enterprise workflows.                                                    | **Very high / medium-high** |
| **14** | **AI-native product pattern library**                        | Identify recurring reusable patterns across apps: live-data ingestion, personal state, recommendations, explanations, maps, dashboards, validation, onboarding, etc. Each pattern gets good/bad examples and implementation lessons.      | Gives next cohort a better starting vocabulary without giving them finished ideas.                                                | Can become reusable skills/templates for AI builders.                                                                                                                 | Medium / low-medium         |
| **15** | **Can process predict talent better than output?**           | Blind one evaluator to the final app and let them judge only interaction traces/feedback response; another sees only final output; a third sees both. Compare internship rankings.                                                        | Shows students what good AI-era work actually looks like.                                                                         | Potentially important for **AI-native hiring assessment**: work traces may be more predictive than portfolios or coding tests.                                        | **Very high / medium-high** |

The one I would do **next** is #1, synthetic users versus real humans. You happen to have collected almost the ideal dataset accidentally: students did agent/persona research and subsequently got multiple pieces of real human feedback about the same product. Most synthetic-user claims are evaluated without this paired ground truth. Even with 10–12 products, you can get a strong directional result and lots of revealing qualitative examples.

The output could be something like:

> **AI personas found 58% of the issues humans later raised, but only 21% of the issues that actually caused observable confusion. They were unusually good at feature suggestions and unusually bad at predicting first-use friction.**

Or the opposite. Either result is interesting. More importantly, students could click “What AI predicted / What humans actually said / What changed.” That is immediately useful teaching material **and** potentially publishable/bloggable evidence.

I would do #2 immediately after. The Human Intervention Atlas may ultimately be the most valuable asset in the entire dataset. Prompting lessons describe **what people should say to agents**. Intervention data tells you the deeper thing: **when a competent human realizes the agent is heading in the wrong direction, what signal they noticed, and what they did about it.** That is much closer to the durable AI-era skill you are teaching.

Then #3 creates the product-management layer, and #9 turns the historical dataset into something that keeps appreciating: every six months you can rerun the same intervention points against new models and literally observe which kinds of human judgment have become automatable.

I would avoid spending much time on another generic “best prompts,” “best tools,” “top apps,” or “common features” catalogue. Those are easy to generate from almost any cohort and decay rapidly. The defensible assets here are the **paired observations and transitions**: AI prediction vs human response, agent action vs human correction, feedback vs decision, claim vs evidence, old model failure vs new model success.

If choosing only **five** to execute, I’d do **1 → 2 → 3 → 4 → 9**. Together they form a surprisingly coherent future product/research dataset: **how humans and agents jointly discover, build, test, and improve products—and exactly where each side adds value.**

## User

Yeah, I'm really interested in the synthetic users versus real users prediction differences. So yes, please go ahead, compare the two and let me know what the top takeaways are. Be specific and give me examples of these differences to help understand what exactly the nature of the difference was, and also try and generalize it so that this can be a reusable lesson that we apply not just to building products with AI, but to any AI-based activity that involves user validations.

## ChatGPT

The strongest conclusion is:

**Synthetic users are useful for finding where to look. Real humans are necessary for discovering what actually matters.**

I manually coded 22 top-level synthetic-user concerns across the six products where I had sufficiently readable synthetic research plus subsequent human testing: Hinata, Miku, Mio, Nanami, Noa, and Yuri. Nine concerns were independently echoed by humans, three were partially echoed, and ten were not raised. So about **55% received at least some later human echo**.

I would not call that “55% accuracy.” The human tests were short, many testers were classmates/instructors rather than target customers, and “not mentioned” does not mean “false.” But for such a small natural experiment, the pattern is surprisingly clear.

| Case                      | Synthetic users predicted                                                                                                        | Humans actually revealed                                                                                                                                                                  | Lesson                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Yuri – Study Walker**   | Users need the exact next click/action; saves need visible confirmation; returning users need context                            | One user became lost and couldn't figure out how to return; another explicitly wanted more step-by-step explanation; you found an instruction unclear and checked whether state survived  | **Excellent prediction.** Synthetic agents had actually operated the app without explanation, which closely resembled usability testing |
| **Nanami – Fishing Map**  | Beginners need equipment/budget information; recommendations need dates/sources/provenance                                       | A human independently asked “how much does it cost to get started?” and later asked where the information came from, then raised the possibility of an AI-recommended poisonous fish      | Synthetic users were very good at **domain constraints**; the human supplied the real-world severity                                    |
| **Hinata – Pawlog**       | Daily entry will become tedious; fields may be ambiguous                                                                         | A human asked for automatic suggestions for things entered every day; you questioned whether pet food is really recorded in grams                                                         | Again, good at anticipating **recurring workflow friction**                                                                             |
| **Miku – travel journal** | Battery/open-page tracking, location privacy, cumbersome Google Maps handoff, unclear persistence                                | You immediately noticed awkward translations, destination state not propagating, strange photo behavior, and repeatedly asked **“where did the postcard go?”**                            | AI thought like a product analyst. The human behaved like a confused human. Only the persistence prediction really landed               |
| **Mio – bookshelf**       | Novel/manga edition confusion, bad continuation recommendations, volume-modeling problems, settings resets                       | Humans struggled first with **“how do I use this?”**, GL/BL terminology, series grouping, novel suitability—and you asked the existential question: **“Doesn't Amazon already do this?”** | AI found edge-case bugs. Humans exposed **mental model and product-positioning problems**                                               |
| **Noa – MRTGo**           | A “3-hour” plan can exceed its time budget; sparse results; destination-name problems; Google Maps remains better for navigation | The human did question strange route ordering, but repeatedly called the experience **“very cool” and “very impressive”**, even retracting one criticism after thinking about it          | A synthetic user can find a valid flaw without knowing whether users will care about it                                                 |

The most important distinction is between **possibility** and **salience**. A synthetic tester can be excellent at answering “Can I find a credible way this fails?” Noa's synthetic research, for example, caught the missing return-time constraint in a nominal three-hour itinerary. But it was poor at answering “Will this dominate someone's experience?” The human mostly experienced delight.

That gives me the first reusable lesson:

> **AI can estimate possibility much better than importance.**

There is an equally important second pattern. Humans produce valuable data precisely because they are messy. They do things a synthetic persona tends not to do: misunderstand what the product is, ignore most choices and click the first plausible one, forget where they came from, misinterpret wording, wonder whether their action worked, compare the product spontaneously with Amazon, get unexpectedly excited, and sometimes change their own mind mid-test.

Your Yuri test is a particularly good example. At one point you explicitly noted that you had **not even read the remaining options because the first one seemed good enough**. That is behavioural information no “thoughtful persona evaluation” naturally generates unless specifically instructed to model limited attention. The ordering of choices suddenly becomes a product variable.

This suggests a stronger formulation than “synthetic personas versus real users”:

**Don't make the AI pretend to be a user. Make it behave like a test agent.**

Yuri's synthetic study did this unusually well. Its agents were given different goals, operated the actual public product without explanation, separated observed behaviour from simulated feelings, and identified exact reproduction conditions. It consequently predicted later human problems much better than the generic “Imagine a cautious 58-year-old user; what might he think?” style of research.

So for future validation, I would use this sequence:

1. **Use AI for hypothesis generation and coverage.** Give it the real artifact and a concrete goal. Ask it to systematically find failure modes, edge cases, trust issues, alternative workflows, domain constraints and scenarios worth testing. Require observations such as “button X produced no confirmation,” not invented quotes like “I would probably feel reassured.”
2. **Convert its findings into falsifiable predictions.** “A first-time user won't know which book edition is which.” “A user cannot resume within 30 seconds.” “A beginner will ask what equipment costs.” That makes synthetic research genuinely useful.
3. **Then put real people in front of the product without showing them the AI findings.** Otherwise you prime the humans into validating the synthetic research. Observe hesitation, mistakes, abandonment, repeated clicks, improvisation, delight and spontaneous comparisons.
4. **Afterwards compare four buckets:** predicted-and-observed; predicted-but-not-observed; unpredicted-but-observed; and predicted-but-contradicted. The third bucket—what humans taught you that AI never imagined—is usually the most valuable.
5. **Let human behaviour determine priority.** Synthetic vote counts such as “three personas wanted this feature” should carry almost no evidential weight. Repeated real behaviour should.

This generalizes well beyond product UX. In any AI-assisted user validation—education, healthcare workflows, financial tools, enterprise processes, marketing, policy, research interfaces—the closer your question is to **rules, constraints, edge cases, domain knowledge, consistency or test coverage**, the more useful synthetic users become.

The closer the question is to **attention, confusion, trust, motivation, embarrassment, habit, perceived value, delight, willingness to pay or actual adoption**, the less I would trust synthetic validation.

That leads to the formulation I would teach the students:

> **AI is a test generator, not a respondent.**
>
> Let AI generate personas, edge cases, failure hypotheses, scenarios and experiments.
> Do not treat AI statements about what users want, trust, value or will do as user evidence.

And perhaps the most memorable short version:

> **Synthetic users tell you where to look. Humans tell you what matters.**

There is also an intriguing research/product direction here. You could formalize exactly this workflow into a **Synthetic User Calibration Benchmark**: run synthetic agents first, freeze their predictions, run humans blind, classify the four outcome buckets, and gradually learn **which classes of user insight AI predicts reliably and which require humans**. That benchmark would get more valuable as you repeat it across cohorts and products.

I saved the audit trail at:

`~/code/talks/2026-09-06-how-to-build-ai-products/submissions/_analysis_synth_vs_real/analysis.md`

and the 22-item coding table at:

`.../_analysis_synth_vs_real/comparison.tsv`

One important caveat in those files: these were **real human testers, but not necessarily real target customers**. So the evidence is already strong enough for the synthetic-vs-human _usability_ lesson above; it is not yet strong evidence about market demand.

# Evaluation Rubric

Source: https://chatgpt.com/c/6aa35dd5-8354-83ec-957e-2bc12dd421e2

## User

Go through the course content on [LocalMCP](/plugins/plugin_asdk_app_69e6c604b4ec8191b8e14bb9e8d7cd52?plugin_detail_origin=inline_selection_pill) at ~/code/talks/2026-09-06-how-to-build-ai-products as well as related context from previous chats, student responses in ~/Documents/data/forms/sutd-ai-products/, and submissions at
Use `uv run ~/code/context.py` as required.

Based on what I'm teaching the students, and what I believe to be important in the AI era (see past conversations, search [LocalMCP](/plugins/plugin_asdk_app_69e6c604b4ec8191b8e14bb9e8d7cd52?plugin_detail_origin=inline_selection_pill)), how should I evaluate the students and their submissions?

This may require you to fetch and analyze the content in the Google Sheet. Feel free to do so. Save what you need at ~/code/talks/2026-09-06-how-to-build-ai-products/submissions/ and feel free to use scripts like ~/code/scripts/call or `llm` to transcribe, `ffmpeg` for screenshots, etc.

Identify the evaluation criteria as a prompt that I can pass to an agent to conduct the evaluation.

Plan carefully on how to do this comprehensively and efficiently.
If this could require multiple steps/passes, that's fine. I'll just say "Proceed" and you can go to the next step.

## ChatGPT

Pass 1 is complete. I reviewed the course pages/transcripts, the original SUTD brief and internship intent, your AI-era education/assessment discussions, the intake responses, and the current Google Sheet submission tracker.

The main conclusion is: **evaluate the quality of the student’s learning-and-verification loop, not the quality of the AI-generated artifact.** The strongest unit of evidence is:

**intent/claim → evidence → judgment → change → re-check**

That matches the course unusually well. “Build the app” is deliberately the cheap part; problem choice, real-user learning, verification, failure diagnosis, orchestration, accountability, and communication are the scarce parts.

I would use these weights:

| Criterion                                       | Weight |
| ----------------------------------------------- | ------ |
| Valuable problem & product judgment             | 15     |
| Shipped product & appropriate ambition          | 10     |
| Real-user evidence & evidence-driven iteration  | 20     |
| Verification, tests & trustworthy evidence      | 20     |
| AI-native orchestration & learning from failure | 15     |
| Accountability, limits & real-world judgment    | 10     |
| Communication & evidence legibility             | 10     |

Two design choices matter. First, **agent persona research is not real-user evidence**; it is useful preliminary research. The course explicitly escalated from personas → classmates → strangers/analytics. Second, I would keep three outputs separate: an absolute **course score /100**, a **growth/stretch signal** based on the intake form but not included in the score, and an **internship signal** based on judgment/autonomy/persistence/verification. Several students started with no AI-coding-agent experience while others already had web-app experience, and reported available time varies substantially; folding that directly into the main grade would distort both course outcomes and hiring signal.

The operational version is saved at:

`~/code/talks/2026-09-06-how-to-build-ai-products/submissions/evaluation-prompt.md`

I also saved the supplied spreadsheet snapshot as:

`submissions/SUTD-AI-Products-Feedback-snapshot.xlsx`

The evaluator should use the live Sheet as source of truth: I found that it has already changed relative to the uploaded snapshot.

Here is the shorter copy-paste version of the evaluation prompt:

SUTD AI Products Evaluation Prompt

You are evaluating student work from Anand S's SUTD Master Class, **How to Build AI Products — and Prove They Work**.

Do not evaluate this like a normal hackathon or software project. AI can generate plausible apps quickly. The course is trying to develop the capabilities that remain scarce when execution becomes cheap: choosing valuable problems, directing AI effectively, learning from failures and feedback, verifying claims, exercising judgment and accountability, and communicating what can and cannot be trusted.

The central unit of evidence is:

**claim / intent → evidence → judgment / decision → change → re-check**

A polished app with little evidence of this loop should score below a rougher app that demonstrates strong judgment, verification, user learning, and evidence-backed iteration.

The course explicitly teaches these principles:

- Build first; fail, learn, repeat. Durable skill is learning how to learn, not memorizing today's AI workflow.
- Ideas and first drafts are cheap. A product needs a real problem, real user, and real use.
- Ask why this deserves to exist instead of simply using ChatGPT or Claude.
- Record feedback rather than remembering it. Let observed behavior shape the application.
- Report failures and moments where the agent needed correction. **The correction is the curriculum.**
- Delegate aggressively and discover where human judgment is actually scarce.
- Make verification cheap and rerunnable using appropriate tests, benchmarks, rubrics, known failures, and regression checks.
- AI personas can provide useful preliminary research, but they do not replace actual humans.
- A test suite is a reusable fence; user testing is an ongoing conversation.
- Publish the product, observe real usage and analytics where practical, and improve from evidence.
- The final case should answer: **Here is the product. Here is what it can and cannot do. Here is the evidence. Here is why you should or should not trust it.**

Evaluate from the strongest available evidence: course materials; current live SUTD AI Products Feedback Sheet; latest app and earlier versions; agent research; peer/human feedback recordings; product video; learnings video; shared agent-session log; tests/benchmarks; and analytics evidence.

Use intake responses only after scoring to assess growth/stretch. Prior coding experience, English fluency, paid model access, or available project time must not alter the absolute course score.

For every factual evaluation claim distinguish **Observed**, **Student-claimed**, **Inferred**, and **Unknown**. Never turn a student claim into observed evidence without verifying it.

If an artifact was never submitted, mark MISSING. If a submitted link cannot be accessed by the evaluation environment, mark INACCESSIBLE / MANUAL REVIEW rather than assuming poor work. If the link is genuinely broken for an ordinary external user, that may affect shareability, but it does not prove that all underlying work was poor.

Score seven criteria out of 100.

### 1. Valuable problem and product judgment — 15

Evaluate whether the student discovered or sharpened a worthwhile problem for a specific user/use; whether the product has a reason to exist beyond “AI can build it”; and whether the student showed taste in deciding what to build and what not to build.

A top score requires evidence that the student's understanding of the problem improved during the week and materially influenced product choices.

Do not reward novelty by itself.

### 2. Shipped product and appropriate ambition — 10

Evaluate whether the student produced a genuinely usable/shareable end-to-end artifact and pushed it far enough to encounter meaningful reality: users, live data, deployment, state, privacy, integrations, etc.

Ambition does not mean more screens, code, AI, features, or infrastructure. Evidence-backed simplification or rebuilding can be stronger than feature accumulation.

### 3. Real-user evidence and evidence-driven iteration — 20

Evaluate whether the student learned from people or behavior outside their own head and whether that evidence changed the product.

Use roughly this evidence hierarchy:

**observed stranger behavior / analytics > target-user behavior > recorded peer behavior > remembered human opinion > AI persona simulation > creator intuition**

A top score requires a closed loop: observed behavior reveals something material → student changes product or framing → result is checked again.

Do not count AI personas as real-user research. Do not give substantial credit merely for installing analytics; inspect whether usage data informed a decision.

### 4. Verification, tests, and trustworthy evidence — 20

Evaluate whether the student defined what “works” means and created credible ways of detecting when it does not.

Strong work has explicit success/failure criteria and evidence suited to the claim. Excellent work leaves behind rerunnable tests, benchmarks, rubrics, regression checks, provenance checks, or similarly durable verification mechanisms; keeps known failures visible; checks surprising findings before acting; and makes verification cheap for the next iteration.

Use the verification technique appropriate to the product. Do not demand LLM calibration from a deterministic non-LLM product. Do not accept unsupported trust claims.

### 5. AI-native orchestration and learning from failure — 15

Inspect the shared agent-session log where available.

Evaluate how well the student managed AI as an execution partner while retaining judgment: providing useful context and constraints, delegating appropriately, choosing tools, testing alternatives, branching when uncertain, feeding external evidence back to the agent, catching failures, and extracting transferable lessons.

Excellent work shows high autonomy with low wasted effort and concentrates human attention on the gaps that AI cannot automatically solve.

Do not reward prompt length, jargon, doing work manually, or using an expensive model.

### 6. Accountability, limits, and real-world judgment — 10

Evaluate whether the student knows what they are willing to claim and what they are not.

Look for concrete limitations and proportionate treatment of relevant human, ethical, privacy, security, cost, operational, reliability, or deployment risks.

Excellent work can say both:

**“Trust this because…”**

and

**“Do not trust this for…”**

Do not reward generic ethics boilerplate.

### 7. Communication and evidence legibility — 10

Evaluate whether another user, teammate, evaluator, or hiring manager can quickly understand the product, the evidence, what failed, what changed, and what remains uncertain.

Use the product video, learnings video, chat log, and other artifacts.

Do not grade accent, English fluency, charisma, or video-production polish. Grade clarity, evidence, precision, traceability, and audience fit.

### Reject these false victories

Pretty UI ≠ good product. Many features ≠ ambition. Long chats ≠ AI skill. Many tests ≠ good verification. AI personas ≠ market validation. Installing analytics ≠ learning from usage. Technical sophistication ≠ judgment. A polished retrospective ≠ proof. No failures ≠ excellence. Prior AI experience ≠ mastery. A well-diagnosed failed experiment may be stronger evidence than an effortless success.

### Evaluation process

First create an evidence dossier for each student before assigning scores. Capture the current product, earlier versions, intended user/problem, research, human feedback, before/after changes, verification evidence, analytics, notable agent-session moments, limitations, and missing/inaccessible evidence.

Then score the seven criteria independently. For every criterion provide:

- raw score 0–4
- weighted points
- 1–3 concrete supporting observations
- one sentence answering **“Why not one level higher?”**

Total this as **Course score /100**.

Treat the first score as untrusted. Have a second reviewer look specifically for score inflation, double-counting, overlooked negative evidence, overlooked strong evidence, and inconsistency across students. For top or borderline candidates, get an independent second score without exposing the first. Reconcile material disagreements from evidence rather than averaging blindly.

Only then inspect the intake responses and report:

**Growth/stretch: High / Medium / Low / Unknown**

This is diagnostic and must not alter the main score.

Separately report an internship signal:

**STRONG YES** — would trust this student with an ambiguous AI-product task with relatively little supervision.

**YES** — strong enough for an internship; some coaching needed.

**MAYBE** — promising, but evidence is sparse/inconsistent or a material question needs live probing.

**NO / NOT YET** — insufficient evidence of the required judgment, autonomy, learning, or reliability.

Base the internship signal on judgment, autonomy, persistence, learning speed, verification discipline, accountability, effective use of AI, and communication—not mechanically on the /100 score.

For each student output a score table, short verdict, growth/stretch signal, internship signal, confidence level, strongest hiring signal, material concern, best evidence, biggest gap, and the single live interview question that would most reduce uncertainty.

After evaluating the entire cohort, calibrate scores across students and run a sensitivity check. Move about five points of weight toward verification/user evidence, then separately toward orchestration/learning. If the top internship shortlist changes materially, label the ranking **SENSITIVE** and explain why. Prefer tied bands to false precision.

Save the per-student evidence and outputs under:

`~/code/talks/2026-09-06-how-to-build-ai-products/submissions/<student-slug>/`

Create a cohort CSV with criterion scores and signals, plus a concise `cohort-evaluation.md` containing the evidence-backed bands and internship shortlist.

Do not force a winner or fixed number of internship recommendations if the evidence does not justify the distinction.

One addition I think is especially important: the agent must always state **“why not one level higher?”** That turns the rubric from a justification machine into a discriminating evaluator, and should be particularly useful when selecting internship candidates.

When you say **Proceed**, the natural next pass is to run this against the actual submissions: fetch/transcribe only the artifacts that can change a score, build the evidence dossiers, independently score everyone, then return the cohort comparison and internship signals.

## User

Collate all the inputs the evaluator needs (in the format it'll need) under the submissions/ directory.

## ChatGPT

Collated under:

`~/code/talks/2026-09-06-how-to-build-ai-products/submissions/`

The workspace now contains:

- `evaluation-prompt.md` — evaluator instructions/rubric.
- `_source/SUTD-AI-Products-Feedback-live.xlsx` and `live-sheet.json` — frozen current Sheet, not the older uploaded snapshot.
- `_source/course/` — course pages plus Day 1–4 transcripts.
- `_source/intake-form.yaml` — original intake questionnaire.
- `_source/identity-map.tsv` — explicit mapping between Sheet identities and intake identities, including the TCU aliases.
- `_source/cohort.json` / `cohort.csv` — normalized cohort manifest.
- `<student>/manifest.json` — exact current submission row, identity provenance and version history.
- `<student>/intake.json` — starting-point responses for the later growth/stretch pass.
- `<student>/links.json` — normalized submitted evidence URLs.
- `<student>/{app,agent-research,feedback,product-video,learnings-video,chat-log,tests,analytics}/` — locally resolved evidence, with `*.status.json` documenting what could or could not be retrieved.
- `_source/media-index.json` — provenance/index for downloaded recordings.
- `_source/audio/` — lightweight evaluator-friendly audio derived from the originals.
- `_source/transcripts/` — **40 complete transcripts covering ~200 minutes of submitted recordings**, named `<student>--<artifact>.md`. Non-English speech is accompanied by English translations.

I preserved original videos as provenance rather than replacing them with transcripts. Apps, research pages and shared-session pages have local HTML snapshots where possible. Miku's v1 and rebuilt v2 are explicitly linked as version history rather than treated as two students.

There are still a few irreducible gaps in the students' own submissions: cells containing descriptions rather than usable URLs (e.g. `video (9).webm - Google ドライブ`, `Locate Premier Shot Lab site`), plus a small number of Drive items for which the supplied link does not permit direct retrieval. Those have explicit `no-url`, `drive-metadata-failed`, or `drive-download-failed` status files so the evaluator can say **MISSING/INACCESSIBLE/MANUAL REVIEW** rather than penalizing by inference.

The main unfinished nicety is that the 40 transcripts currently live centrally under `_source/transcripts/`, with unique student/role filenames, rather than also being copied into each student's artifact folder. The evaluator can already consume them deterministically from there.

# Evaluation App

Source: https://chatgpt.com/c/6aa36686-9b5c-83ec-97b7-5f5c3e74bafe

## User

I would like you to build an application that allows students to submit their suggestions for changes to the evaluation prompt that I have uploaded. Allow the students to share their inputs as a text field with as many details as they would like, and save that. Allow each student to edit their own responses, and they can also submit multiple feedback items. If possible, share thoughts on how appropriate or useful it would be to incorporate the entire feedback or change to the evaluation process, either in part or in full. This response may help the student revise their suggestions or add new suggestions. What I will be doing is, either at the end of the day or over the weekend, take all of the feedback, run it against my point of view on how evaluations should be done, and change the prompt accordingly, and then finally run the prompt. Feel free to use all course-related material, past conversations, and any other information that you need to build this application and deploy it on sites.

The prompt itself is in @LocalMCP at ~/code/talks/2026-09-06-how-to-build-ai-products/submissions/evaluation-prompt.md
Other relevant content is a directory above on @LocalMCP and in past chats and... figure it out.

@LocalMCP won't be live while the app is running, so make sure the app has all it needs in terms of context. But the app may use ChatGPT to respond using the relevant context.

## ChatGPT

The application is live:

[Open SUTD Evaluation Prompt Lab](https://evaluation-prompt-feedback.root-node.chatgpt.site)

Students can:

- Sign in with ChatGPT.
- Read the complete embedded evaluation prompt.
- Submit multiple detailed suggestions.
- Edit only their own suggestions; earlier revisions remain preserved.
- Receive immediate “Incorporate / Incorporate partly / Test first” guidance with risks and revision advice.

You can review the full cohort and export the latest feedback as CSV.

The coach is currently deterministic and rubric-based—not an LLM call—so it has no API cost or hallucination risk. I verified the production database, exact source-prompt match, ownership checks, build, deployment, and three advisor decision paths.

# Evaluation Prompt Revision

Source: https://chatgpt.com/c/6aa36efa-7154-83ec-9939-3082fdb72398

## User

I asked students to share suggestions on how to improve the evaluation rubric and here is what they shared.

Read what they shared and think about it. Look at the actual submissions.
Based on this, take only what clearly and substantially improves the evaluation rubric.
Revise and update the evaluation-prompt.md based on this. (I have a backup in evaluation-prompt-original.md)
Mention the reason for what you incorporated and what you ignored.

Use relevant skills on @LocalMCP

[Attachment: evaluation-prompt-feedback.csv]

## ChatGPT

Updated:

`~/code/talks/2026-09-06-how-to-build-ai-products/submissions/evaluation-prompt.md`

The backup `evaluation-prompt-original.md` is untouched. I also saved the rationale at `evaluation-prompt-revision-notes.md`. The weights remain unchanged at 15/10/20/20/15/10/10 = 100.

The changes I kept were deliberately narrow:

- **Incorporated — simpler rationale / learning-outcome mapping.** Added a “Rubric in one minute” reducing the rubric to four understandable questions, plus a one-line learning-outcome mapping under every criterion. This addresses KK’s point and your concern about complexity without throwing away distinctions useful for reliable scoring.
- **Incorporated — Yuri’s AI/human division of labor.** Criterion 5 now explicitly asks what the student chose to delegate, verify, and _not_ delegate. This is genuinely discriminative in the submissions: Yuri, for example, delegated implementation/research/testing but retained decisions about purpose, prioritization, verification and whether to ship an AI API.
- **Incorporated — Noa’s human proxies.** I removed the simplistic fixed evidence hierarchy. Evidence is now judged by relevance to the claim, observed behavior, independence, and traceability. A well-chosen human proxy can outrank generic peer feedback, but must be labeled `PROXY` and cannot establish target-specific demand, professional judgment, willingness to pay, etc. This matters for submissions such as Kosei’s coach-facing product.
- **Incorporated — Johan’s protected admin surfaces.** A correctly protected admin/analytics page is no longer liable to be mistaken for missing functionality. The evaluator must not bypass access control; videos/logs/screenshots can establish `student-demonstrated` evidence. I added that as a formal evidence category between independently observed and merely student-claimed.
- **Incorporated — Yuri’s “ask rather than invent.”** Material translation/identity/meaning ambiguities now become `UNKNOWN / CLARIFICATION NEEDED`, followed by one focused live/manual probe rather than inference. Clarification still does not magically turn an unobserved claim into observed evidence.
- **Partly incorporated — Christopher’s “build first” objection.** I did **not** lower Criterion 1 from 15. The course itself repeatedly says that once building becomes cheap, knowing what is worth building becomes more important. But I clarified an important distinction: students need not _start_ with a worthwhile problem. A weak or playful first idea can score 4 if building, testing and feedback substantially sharpen the user/problem/use by the end.
- **Not incorporated — Dora’s mobile/desktop debugging request.** That is useful feedback on Dora’s product, not a general rubric improvement. Criteria 2 and 4 already cover relevant environments, failure modes and regressions. Making mobile testing explicit would unfairly privilege apps intended for mobile.
- **Not incorporated — Kosei’s “one mistake” comment.** There is no identifiable rubric change to act on.
- **Not otherwise incorporated — KK’s general concern about bias.** His concrete rewrite of Criterion 1 is effectively what the rubric already says. The substantive gap was explaining how the criteria derive from the learning objectives; that part is now fixed.
- **Not incorporated — collapsing the seven scored criteria into four.** It would be easier to read but materially worse for evaluation: it would merge user learning with verification, or execution with accountability. Instead, students/evaluators now see four simple headline questions with seven scoring dimensions underneath.

One change I think is particularly important is replacing “strangers > target users > peers > personas” with **claim-sensitive evidence quality**. Looking at the actual submissions made it clear the old hierarchy was too crude: a random stranger can be excellent evidence about onboarding and terrible evidence about whether a football coach would act on an analysis. The revised prompt now makes that distinction explicitly.

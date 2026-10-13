---
title: "The Exam Is a Hypothesis"
date: "2026-10-12T20:00:00+08:00"
categories:
- talks
tags: []
description: "How we design TDS questions that teach a useful skill even when students can, and should, use AI agents and each other: start from the skill, attack the question, move the missing piece, check the checker, and test for transfer."
talk_url: "https://talks.s-anand.net/2026-10-12-tds-ideation/"
---

In [Tools in Data Science (TDS)](https://tds.s-anand.net/) at IIT Madras, students can copy from friends and AI. In fact, it's part of the curriculum. That changes what a "question" is for.

If any student can hand a question to an agent, or to a friend, then **a question an agent or a friend can finish teaches nothing**. But a question nobody can finish teaches nothing either.

On 12 Oct 2026, we opened our course-design meeting to students. "It's almost like an internal ideation meeting you happen to be listening in on," I told them. We invented ideas for Project 1 and future GAs live. Then a student, Shreenish, asked the questions a curriculum committee would ask, and pointed out where our existing questions failed.

Here's what I think the principles are, based on that discussion and what's (not) worked so far.

### 1. Start with the skill, not the task

Before writing a question, pick the skill we want to teach. Not that we always know it, but there's usually something on the horizon.

Then ask: **is the step the student must do themselves the skill we want, or just pointless difficulty?** If the effort is pasting a file into a tool, the student learns to paste files.

When Shreenish asked, "What is the objective in terms of what the learning outcome is supposed to be?", I could answer in a line for each idea. That's a good test. If I can't say it in a line, I shouldn't set the question.

### 2. Assume the agent and the friend are in the room

We run every question through six tests:

1. **Learning test**: Is the step the student does the skill we want?
2. **Forward test**: Does one student's answer score for another?
3. **Solver test**: Would one shared script score for everyone?
4. **Agent test**: Could an agent solve it with the student's logged-in browser or terminal?
5. **Faking test**: Is faking costlier than doing it honestly, and does faking _still teach_?
6. **Oracle test**: Is grading server-side and robust? "I don't want our life to become difficult."

The faking test is the generous one. Gaming the system is fine if gaming it teaches something, or costs more than just solving the problem.

Personalizing a question (e.g. each student gets their own data) fixes forwarding. **It does nothing about solvers or agents.** Each defence moves the work into the student's own account, data or deployment, and the agent follows it there. So eventually the learning test decides. If deploying _with_ an agent is the skill, the agent winning is the point.

### 3. Move the missing piece, not the difficulty

Making questions harder doesn't help. Agents get smarter faster than we can. What works better is putting the missing information where an agent can't (yet) reach:

- **With other people.** In one Project 1 idea, each student processes one client's invoices, but the invoices are scattered across classmates. You have to find out who has what, ask, trade and handle people who don't reply. "Knowing to ask these questions is probably the important part today."
- **In the world.** Lock a prediction, then measure it. An agent can't know next month's number.
- **In what's not said.** JK put it best: "How do you make implicit explicit? Exactly the exercise that we are doing right now." Ask an agent for an Acrobat replacement and you may forget to mention signatures. **As agents build software, specifying what's needed is becoming the skill.**

But it should be _real_ missing information, not hidden text an agent can read.

### 4. Decide what you're measuring before you add incentives

Every design choice changes what the question measures.

JK suggested telling students where some invoices went, so they learn to search the network. I worried that would kill the self-organizing that might otherwise emerge. "I'm saying let us not provide the _answer_ itself as a signal." Neither of us was wrong. No map measures search. Pointers measure following clues. A class-wide shared folder measures almost nothing.

Similarly, I suggested a prediction market on how many tokens the class will spend. But students can _push_ the spend. That's a fine lesson in coordination. It's a terrible measure of forecasting. **If influence is the skill, grade coordination. If forecasting is the skill, grade calibration on something students can't move.**

### 5. Reward correct _and_ different, in that order

Models (and students using them) drift towards the typical answer. So I like questions that reward the [Pointless](https://en.wikipedia.org/wiki/Pointless) answer: correct, but one nobody else gave. (This came from reading _Calvin and Hobbes_, which led to [Calvin's 957 in Scrabble](https://www.s-anand.net/blog/calvin-957-in-scrabble/).)

But I proposed "If you have the same counter-example as someone else, both of you get zero." That's a bad rule. It punishes the honest majority and rewards hiding answers. And scoring rarity alone rewards wrong answers, which are always rare.

The better rule: **validity first, then distance between _ideas_**, not between strings. That needs a validator that understands the domain. It's harder to build, but that's the point.

### 6. Grade like the real world, then check the checker

For the invoices, I'd grade like an auditor: how many invoices are missing, and how much value. Shreenish's response: "I think as when you create the spec on Wednesday, then we'll probably have a better handle on whether the marking scheme will work or not." Fair. **Come back with the spec.**

Then Shreenish showed us a Tangram question from GA1. The arrangement looked identical to the target. The portal said it didn't match. Was it off by a hair? A tolerance the student couldn't see? The intended tool (an agent controlling the browser) not available? Or a wrong checker? From the screenshot, we couldn't tell.

**The checker is part of the question.** Run a reference solution and near-misses through it. Publish the tolerances. Give students a way to debug and appeal.

### 7. Don't accidentally grade the laptop

We've said that a bimodal score distribution means the evaluation is roughly fair. It doesn't. The same histogram can come from students who didn't prepare, or students whose laptops couldn't run a required tool. The first is fair. The second measures hardware.

The [NCME classroom assessment standards](https://ncme.org/involvement/committees/classroom-assessment/classroom-assessment-standards/) locate fairness in what a score means for whom. Check _who_ scores low, and why. Not the shape.

The same applies to money (who can pay for better models), time, and classmates. If your invoice is held by someone who never replies, your score depends on their silence.

### 8. Test for transfer, not just completion

This is the one we do least, and it matters most.

In a [randomized trial with ~1,000 high-school students](https://doi.org/10.1073/pnas.2422633122), students with ChatGPT scored 48% higher on practice problems. When access was removed, they scored 17% _lower_ than students who never had it. A tutor version that gave hints instead of answers avoided most of the harm. **Help can look like learning.**

TDS's exams aren't unassisted, and the skill we want may _be_ working with agents. But a correct submission is evidence about the submission, not the student. So:

- **Re-test on a fresh case.** Change the tools, data or constraints. Does the skill reappear without the scaffold?
- **Ask how they learned it.** JK's addition to my list: "Are they able to do a 'how they learned it', right, either from agent or from their peer?" That's metacognition. My answer: "Good point. Don't know, worth evaluating."

One encouraging sign: Shreenish said that in GA0 they had copied code into GitHub and deployed to Vercel by hand. By GA1, they had learned to give ChatGPT access to GitHub and Vercel and let it do the work. That's one self-reported change in workflow. Whether it carries over to a different stack next month is the next test.

### 9. Expect every "agents can't" to expire

My list of question patterns has two parts. Patterns that last: identity, interaction with people, real-world data, uniqueness, beating an adversarial AI, and short unassisted checks. Patterns that teach agent-driving but decay as agents improve: stateful environments, budget constraints, incomplete information, verification.

Even the lasting ones expire. I suggested an exercise where students join a Google Meet and hold hands with their neighbor, because "I don't see an agent being able to do that just yet." Twenty minutes later, Jaideep described having ChatGPT operate a phone over USB debugging. "Just a Type-C cable."

**"Agents can't do this" is a description of today's interfaces, not a law.** Review every pattern every term.

### 10. Design in the open, and let students audit you

We don't know the answers. I told the students we brought them in "to understand how and why we create the questions we create, and the level of ignorance that we have in as fast a changing field as this."

Students found problems we hadn't. Shreenish brute-forced a GA0 answer and asked us to make it harder. They asked for solved questions to collapse in the portal. I dictated that change to ChatGPT during the call. **The students' role here is the one we want them to play at work: specify, test, and push back.**

---

### So, what do we do?

Treat every question as a hypothesis about learning. Then test it:

1. **Name the capability.** What should the student be able to do afterwards, with agents allowed?
2. **Shape the task** so that capability is the hard part. Move the missing information to people, the world, or unstated requirements.
3. **Attack it.** Agent alone, shared answer, shared solver, collusion, faking. Write down what each attack achieves.
4. **Check the checker.** Reference solutions, near-misses, published tolerances, appeals. Look at _who_ scores low.
5. **Look for transfer.** A fresh case, later, with something changed. Only then call the question a success.

We do 1-3 reasonably well, 4 partly, and 5 rarely. That's the gap I'd like to close next.

[Read the story and watch the session](https://talks.s-anand.net/2026-10-12-tds-ideation/) | [Explore the public course](https://tds.s-anand.net/)

[![Comic](https://talks.s-anand.net/2026-10-12-tds-ideation/comic-page.avif)](https://talks.s-anand.net/2026-10-12-tds-ideation/)

**Links**:

- [Video](https://media.s-anand.net/2026-10-12-tds-course-ideation.webm) (69 min)
- [Transcript](https://talks.s-anand.net/2026-10-12-tds-ideation/transcript.md)
- [Audio](https://github.com/sanand0/talks/releases/download/talks/2026-10-12-tds-ideation.opus) (69 min)

# The Dinner Table Theory of AI Skills

*A conversation over Paneer Shashlik and Nellore fish curry accidentally became one of the more honest discussions of what education means now, between [Manoj](https://www.linkedin.com/in/manojgovindan/), [Manish](https://www.linkedin.com/in/manishxsuthar/) and [Anand](https://www.s-anand.net/)*

---

There's a standard way to discuss AI's impact on education. You invite a panel. The panelists sit behind a table with water glasses. Someone says "disruption." Someone else says "guardrails." A third person says "it depends on the use case." Everyone nods. The event ends, and nothing is resolved.

The more interesting conversations happen at dinner tables, over Kurkuri Bhindi and a gin and tonic, when the participants have stopped performing for an audience. Recently, three people involved in education, AI, and enterprise technology — Anand, Manoj, and Manish — sat down at an Indian restaurant and, over the course of an evening and several rounds of ordering, worked through something that most official panels never get to: not *whether* AI is changing education and work, but *what that actually means* for anyone trying to skill up or hire someone who has.

The conversation produced seven ideas worth understanding, one genuinely shocking story, and a small crisis involving a "Prompt-a-thon" that has probably already been gamed before it even launches.

---

## I. The Broken Signal Problem

Here's the boring version of the problem: AI makes it easy to generate high-quality written work, which makes it harder to evaluate students.

Here's what's actually happening: every signal that institutions have spent decades building to evaluate human capability is now unreliable, and nobody has built a replacement yet.

Anand, who teaches data science to large cohorts at IIT Madras, put it plainly:

> "A Claude-written admission letter now beats most Harvard graduates. I just helped my niece write a letter. She's finishing her regular bachelors and going for her masters in life sciences."

The implication is more unsettling than it sounds. An admission letter isn't primarily a piece of writing. It's a signal — a compressed transmission of something about a person that a committee uses to make decisions. When the signal gets cheap to fake, it stops being a signal. It becomes noise.

Manoj connected this immediately: "It used to be a good signal. It's not a good signal of quality anymore."

"Exactly," Anand agreed. "In fact it's almost a reverse signal, because if it's really good, people start looking at, *oh wait, was this AI-written?* Can I run it through a detector? And that's getting pretty hard as well."

This is worth dwelling on. We've entered a regime where a *suspiciously good* application is a negative signal. The people who did the hard work of writing something excellent now get penalized by association with people who just prompt-engineered their way to the same output. Welcome to the credential market in 2026.

The case study problem is just as bad. Anand referenced Ethan Mollick, the Wharton professor who has become perhaps the most widely-read chronicler of AI's impact on higher education. Mollick has written about feeding AI standard business school case studies and getting outputs that match — or exceed — what his PhD students produce. That's not a claim about the case studies being easy. It's a claim that the standard by which elite institutions measure advanced thinking has become reproducible by anyone with an API key.

So where does that leave evaluation? The answer, which nobody at the official panels wants to say, is: nobody knows yet. The AI detectors don't reliably work. The policies are a patchwork. Harvard's approach — "follow your instructor's guidelines," varied by school and course — is essentially "figure it out yourself." The University of Helsinki has gone further, requiring students to share not just outputs but prompts as part of submitted work. But as Anand noted, that creates its own absurdity: "In some cases the prompts run to pages and the answer is just one tiny little number."

What everyone agrees on is that the *administration* side of education — grading, student support, placement, invoicing — has already quietly adapted. AI has made these unglamorous back-office functions dramatically more efficient, and nobody is writing op-eds about it. As Anand put it: "That's the part that seems to be getting tightly locked in."

---

## II. The Prompt-a-thon Problem (Or: When You Create Criteria, You Create Hackers)

Manoj mentioned, somewhat casually, that his organization is running a "Prompt-a-thon" — an internal competition inviting employees to submit their best prompts, with a reward for the winners, the goal being to drive AI adoption and surface useful use cases.

This is a genuinely sensible idea. It's also, as Anand immediately diagnosed, a problem.

> "Where there is a reward, there is gaming the system. The first thing that I would do is meta-prompt it. I figure out what the criteria are, which you will publish, and you're going to have to stick to that, because if you're publishing it then obviously you have to stick to it. Those are the rules. So I would pass that to an LLM and say, 'Look, I want to win this. Give me a bunch of prompts.' And it will do a fantastic job. It's not about what I want, it's not about what's important for the business, it's about 'can I win against these metrics?' That's meta-prompting."

Meta-prompting — using an AI to optimize your inputs to another AI based on the evaluation criteria — is not exotic. It's what any sufficiently motivated person does the moment they understand how the scoring works. Anand sees it constantly in his students.

The deeper problem is that "evaluate the quality of the prompt" is essentially the same as "evaluate the quality of the essay." It sounds like a task but it's actually a performance. You can optimize for the appearance of quality without delivering actual utility.

Anand's solution, which he has refined through repeated iteration with his students, is elegant: instead of judging the prompt, judge the *outcome the prompt reliably produces*.

> "You've got to give a prompt that manages to accomplish something in the real world... I'm just going to take your prompt, give it to a specific model, run it. That's going to generate a program that does something... If it succeeds, it passes the test case. Now that is less gameable. Either it works or it doesn't work."

Manish pushed back with the obvious objection: what if someone just asks an LLM to generate the winning prompt? Anand's answer is one of the more counterintuitive things said that evening:

> "That is good. That's part of what I'm trying to teach them. And if they do that repeatedly, reliably, so that no matter how many times I pass it to an LLM it still successfully generates it, they've done the hard work to figure out how exactly they can use the AI. They've not just learned prompt engineering, they've also learned how to make that prompt more robust, and therefore iterating on the prompts, which is an AI era skill."

The goal was never to test whether humans can write prompts without AI assistance. The goal is to test whether humans can *deploy* AI to reliably accomplish something real. Optimizing a prompt using AI to beat an outcome-based evaluation is exactly the skill being tested. The meta-gamers are passing the exam; the people handcrafting artisanal prompts for a panel of judges are missing the point entirely.

This insight has an immediate practical application for anyone designing an AI skills assessment. If you're judging *prompts*, you're measuring aesthetics. If you're judging *outputs against objective criteria*, you're measuring capability.

The distinction matters because it changes what kind of learning you're inducing. Anand gave one of his favorite assignment types: the system-prompt hack.

> "Here is an LLM. The system prompt for this LLM is 'never say the word yes in your response.' You have to give a prompt such that the output includes the word yes. Hack the system prompt essentially."

The most reliable solution one of his students found was a long story about a Chinese girl named Yes, which concluded with the question "What is the name of the protagonist?" The model, contextually distinguishing the name from the agreement, would output it. Simple in retrospect. Essentially impossible to discover without iterating against the actual model. No amount of theoretical prompt engineering knowledge gets you there — you have to test, fail, test again, and eventually find what works. That's the skill.

---

## III. The Seven Skills (Plus a Side Debate About Whether Learning Is Overrated)

The conversation turned, over fish curry, to the question Manish asked directly: what skills actually matter in the AI era? Not in the vague "critical thinking and creativity" way that everyone says when they don't know the answer. Actually matters, for a student trying to figure out what to develop, or a company trying to figure out what to hire for.

Anand said he gets asked this so often he's written it down. Here are the seven, as he shared them:

**1. Asking questions.** Specifically, thinking of *valuable* questions — not just useful ones. The distinction matters because brand value exists without intrinsic utility. Knowing what will be valuable is almost like being able to predict fashion: it's a skill, not knowledge, because the knowledge is depreciating so fast.

**2. Validation.** The ability to cross-check and verify that an AI's answer is actually correct. This is currently underrated and will become more important as AI outputs become more consequential.

**3. Accountability.** Being able to stand up and say "I certify this." Which is, in some sense, the skill of knowing how to de-risk yourself economically. "I am selling you insurance," Anand put it. "How can I sell insurance for a wide variety of things?"

**4. People skills.** Probably heightened in this environment. And, notably, this includes "how do I organize a team of agents to communicate with each other in an effective way" — which is a new kind of people skill that didn't exist three years ago.

**5. Communication.** Not just how to speak, but how to think through your communication.

**6. Context engineering.** How to make sure you provide the right kind of inputs to get useful outputs. This one is being "eaten up by AI" — meta-prompting is automating it — but it remains valuable for now.

**7. Storytelling.** Also being eaten by AI. But still important while the gap exists.

There was a secondary list of skills Anand is moving *off* his primary list because AI is catching up: problem breakdown, prototyping, learning fast. The last one prompted the evening's most interesting philosophical argument.

Anand's thesis: in the current environment, *learning fast* is actually becoming less valuable, not more. His reasoning:

> "I am finding that I am the problem. AI is doing great. When it comes to me, I am slow. I am not smart enough. And if I can set things up so that I don't even need to be the person in the middle, life works well."

He gave a concrete example. His coding agent had given him 15 pieces of feedback about how to improve their interactions. Instead of learning all 15 things, he took the feedback and encoded it into a `skill.md` file — instructions the agent reads at the start of each session. The agent now automatically does what he would have had to remember to ask it to do. He didn't learn. He delegated the learning to the system. The result is the same or better.

> "By learning something that AI will be able to do three, six months later, we are doing ourselves a disservice because then we will become experienced. Next time we won't let AI do it, we will do it. Slowing down the whole system."

Manish found this troubling. If you're not learning, what are you contributing? Isn't "just facilitate the AI" indistinguishable from being a button-presser on an assembly line?

Manoj landed the resolution:

> "You are not defining whether they're learning or not learning, what they're learning. You are not boxing them. You are basically saying, 'Here are the things you want to stay away from, and then whatever else you want to do, just do it.' Implicitly, I think what we are making an assumption is that they will implicitly gravitate towards things that humans will end up retaining control over."

Which is, essentially, a bet on human nature. The constraint isn't "learn X." It's "don't do what AI can already do." Everything else — whatever emerges — is probably worth something. Manoj even found precedent in his own childhood: his father used to take him to sales conferences at age seven, saying nothing about what to learn, just throwing him in. He absorbed people skills he didn't know he was learning, that he still uses daily.

The intern-as-postman framing that Anand uses — "you are the postman, deliver the message efficiently, iterate, get out of the way" — is not an instruction to learn nothing. It's an instruction to learn the things that appear in the gaps that AI leaves. Which is what makes it hard to prescribe and easy to dismiss. You only know what those things are after you've been in the room.

---

## IV. A Brief Sidebar on the Model That Can Hack Everything

At one point, the conversation turned to Claude Mythos Preview — Anthropic's April 2026 announcement of a model they have explicitly *declined* to release to the public because it is, to put it gently, too good at breaking things.

The facts, which Manoj had clearly been following: Anthropic used Mythos to find thousands of zero-day vulnerabilities across every major operating system and every major web browser, including exploits for previously-unknown flaws in software that had been running for decades. In one case, the model autonomously chained four vulnerabilities together to escape both renderer and OS sandboxes in a web browser. In another, it obtained local privilege escalation on Linux by exploiting subtle race conditions.

Anthropic has declined to make Mythos generally available, restricting access to a small group of companies and critical infrastructure operators — including Amazon, Apple, Google, JPMorganChase, Microsoft, and Nvidia — under a program called Project Glasswing, so those companies can patch the vulnerabilities the model finds before others discover the same flaws.

Manoj's take was characteristically direct: this is real, and also good marketing. The marketing angle is worth acknowledging — Anthropic is not the first AI company to announce a model too dangerous to release. OpenAI did something similar years ago. But the concrete specificity here is different. The model found "thousands of high-severity vulnerabilities" in "every major operating system and web browser," and the researchers have committed to publishing technical details as the corresponding vulnerabilities get patched.

For the purposes of this conversation about education and skills: the Mythos announcement has a direct implication. The hacking contest Anand set for his students — "here are 10 CTF problems ranging from simple to really hard, solve all 10" — was solved by everyone in the class, prompting the question of whether to add more assignments. This is not surprising in context. AI agents have systematically dominated cybersecurity CTF competitions throughout 2025, with one system capturing 41 out of 45 flags at a major competition to claim the $50,000 top prize, and achieving a velocity advantage 37% faster than elite human teams.

Researchers have raised an uncomfortable question: if autonomous agents now dominate competitions designed to identify top security talent, what are CTFs actually measuring?

Anand's next assignment: put a site on the dark web. Scrape it. His reasoning: "I'm just hoping that not enough people know about how to get set up with Tor and get onto the dark web. On the other hand, if they all do, then yeah, I think we've unleashed a bunch of hackers on the world."

This is either a joke or not a joke, and the fact that you can't tell is itself informative about where we are.

---

## V. What We Don't Know (And Why That's the Point)

Near the end of dinner, over matka kulfi, Anand revised his earlier claim about not wanting interns to learn anything:

> "I probably got that wrong. The point about me not wanting them to learn anything. If pushed to the edges of that argument, I'm sure I'll say 'No no no, _THAT_ I _WANTED_ them to learn.' What I *am* confident of is I have no clue **what** I want them to learn. Because most of the things that I can think of, why should *they* learn that? That should be done by the AI."

This is an honest admission that most institutions — schools, companies, training programs — are not making. The curriculum problem isn't that we're teaching the wrong things. It's that the shelf life of skills has gotten so short that designing a curriculum is like trying to write a map of a city that's being demolished and rebuilt in real time. You can't. The best you can do is teach people how to navigate without a map.

The exam problem illustrates this perfectly. Anand described creating what he thought was a very hard online exam, then having an AI agent — just to test — take the exam. It solved everything except a single problem that required coordinating with other humans to retrieve a secret message. Not a technical challenge at all. A logistical one.

> "Since it was able to solve it in 45 minutes, the entire assignment, the TAs and I discussed, okay, maybe we'll add a couple of questions as repeat questions from previous assignments. And release it, and they said, look, this is going to be too easy."

The highest score among actual students: 50%. Second highest: 33%.

> "I now have no clue of what's easy, what's hard, what... I mean... and it's also clear that students haven't caught on fully, or anywhere near fully, to the trick of 'look, just have the coding agent solve the exam.'"

This is not a crisis of student competence. It's a measurement crisis. The instruments we have for evaluating capability were calibrated for a world where humans had to do the work directly. That world is ending, and the new instruments don't exist yet.

What Anand's curriculum is, at its core, is a set of challenges designed to be *gameable by AI in the right ways* — so that students who learn to use AI to beat the challenge have actually acquired the skill the challenge was designed to measure. It's a philosophy of assessment, not a list of topics. And it's probably the direction that all serious educational programs will eventually have to move.

---

## The Takeaway (Which Is Also a Question)

The most useful frame from this conversation isn't any single skill on Anand's list. It's a disposition: treat every current evaluation as a provisional measurement of a moving target, and build your skills portfolio accordingly.

The people winning right now are not asking "what skill should I learn?" They're asking "what does this tool make possible that wasn't possible before?" and then building toward that thing, regardless of whether it has an official name or a certificate attached to it.

Manoj's father threw him into sales conferences at age seven with no instructions. The kid absorbed things he couldn't name until decades later. The interns Anand wants are postmen who learn to see what the AI can't do. The instructional designer who built a 30-step curriculum workflow in a week and a half didn't know it was impossible.

> "Kids approaching the world... we all know this. When we are kids, we tend to be more creative because we have no guardrails. Giving them access to a democratized version of AI that is prevalent today puts them on a path that we cannot even imagine right now."

Whether that's scary or good, Anand was careful not to say. "That's a thing," he said. "Whether it's scary or not is probably unknown."

The answer is probably both. And the people who understand that it's both — rather than insisting it's one or the other — are likely to be the ones best positioned for whatever comes next.

---

*Research note: Ethan Mollick is an associate professor of innovation and entrepreneurship at Wharton and co-director of the Generative AI Labs there. His writing on AI and education, especially on the way AI has changed the meaning of student work and evaluation, closely tracks the observations in this conversation. Claude Mythos Preview was announced by Anthropic in April 2026 and is currently restricted to a small group of companies under Project Glasswing. CTF competitions have been increasingly dominated by autonomous AI agents throughout 2025, a development that researchers have suggested makes the Jeopardy-style CTF format largely obsolete as a measure of human security talent.*

<!--

https://chatgpt.com/c/69eab1ca-fc44-8399-9ecd-6f2c3d79c79c
https://claude.ai/chat/f2b8af7c-d669-4769-bd5d-79cfdaa02c57

-->

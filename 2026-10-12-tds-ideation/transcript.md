## Transcript

**Unsure**: [00:17] Good evening.

**Unsure**: [00:21] Good evening.

**Anand**: [00:30] I think we should wait for Carlton to come set the context and all that. Or at least JK and then we’ll dive in.

**Hritik**: [00:59] On Discourse, students were asking for project ideas. Project 1, you mean? Yeah, let's discuss today.

**Anand**: [01:09] I guess this is going to be a little late if we wait for others, so why don’t we start off? And for anyone who’s not part of the course team, FYI, the course team is going to discuss what we’re going to do for future GAs, projects, ROEs, etc. So, it's almost like an internal ideation meeting you happen to be listening in on.

**Anand**: [01:45] With that, what is more—what is earlier, Hritik? Project 1 or GA3? I’m not sure, I should check that out. Hold on. Project 1 is due starting 9th October, okay, so it’s already in the past. GA3 is only 14th, so Project 1 is going to be the bigger one. Okay.

**Anand**: [02:18] Let’s ideate. I don’t yet have a specific thought—or rather, not one overarching one perhaps—but here are a few themes that I was thinking and course team, just tell me what you think. Before I dive in into that, I was trying to synthesize the principles for how we are crafting our questions. Hey JK, just got started.

**JK**: [02:56] Hey, hi Anand. Sorry, got slightly delayed.

**Anand**: [03:00] Definitely want you to comment on these. Hold on, let me put this into a better Markdown format.

**Anand**: [03:17] So, if we’re drafting questions—and here is my suggestion on the prompt that will draft and verify—**the assumptions are: look, people can and should use an agent to solve it. And they should collaborate, not just sharing answers but sharing tools that let it solve the problem.** Therefore, what we need to do is: one, pick the skill we want to teach—not that we always know it, but there is something on the horizon, right?

**Anand**: [03:54] And here are six tests. One, are they learning something? Second, if one person forwards their answer to another, it should not work. Third, if I pass my solver to you, it should not easily work without the other person doing something. **If I just toss an agent at it, it should not trivially solve the problem without me learning something in the process.** If there is any other way, like for instance, external collaboration, like we had for the Mark Donation thing etc., any which way we try and game the system, it should still either teach or it should be more effort than just solving the problem. And finally, are we grading it in a reasonably easy and robust way? I don’t want our life to become difficult.

**Anand**: [04:47] Hritik, should we start streaming? Okay, yeah sure. I have no idea who—if anyone needs streaming or not, but sure. With our target being roughly half the students scoring it right, that seems to be the sweet spot for learning. Some people find it easy enough, and the other people don’t yet know it, so there is learning.

**Anand**: [05:08] And here are patterns that I see if a question introduces—it often achieves these objectives. One, can they bring their identity? **Ultimately, in the future, your identity is an agent-proof skill.** So, if I record my voice, then one of the exercises I’m creating for class 6 to 8 students right now is: can they teach a concept to a family member who explains it back? And if you’ve done that, then you’re obviously not taking it with an agent as of today and you’re learning something.

**Anand**: [05:46] Interaction—kind of like how we were doing the donate marks stuff—and if we get people to interact with each other, that’s obviously a relationship/negotiation kind of skill that is durable in the AI era. Is there some kind of real-world validation? For instance, I make a prediction and then I measure it. That tests my ability to predict. Or anything that’s real-world back that AI cannot know, in which case, if I give it to an agent, it still will not be able to figure it out.

**Anand**: [06:24] Uniqueness in the sense of creativity. Can I create something that is distinctively different from what my peers have created? Let’s reward for it—we’ve done this in the past. Can I beat an AI telling it to say yes when it has been told to say no? Again, somewhat non-deterministic. It’s a pattern and term, basically, is what I will put as an example for presence, where we are testing a different kind of skill.

**JK**: [06:55] Yeah, yeah. These are durable skills. I mean, we want it to transfer—both durable and transferable.

**Anand**: [07:11] Correct. These may decay but are still relevant. One, can I do deployment? Can I connect to the right kinds of tools, etc.? So, setting up the environments. Can I do this within a limited budget, within a limited set of tools, etc.? Can I figure out what is not being told? Otherwise, agents will become smarter than me at it, but for now... and agent makes a mistake, can I verify it? Again, over time, agents will probably surpass that ability, but for now, can I find and fix their bugs?

**Anand**: [07:45] So, my proposal is that we run this checklist—not that we haven’t been doing this implicitly, but perhaps explicitly.

**JK**: [07:53] One more—one more skill that I would really want is that learning that student has. **Are they able to learn from the step that they—I mean, about the metaskill of metacognition, right? Are they able to do a "how they learned it", right, either from agent or from their peer?** Is there a way that they know, "Okay, this is how I need to solve this kind of problems"?

**Anand**: [08:26] Good point. Don’t know, worth evaluating, agreed. And yeah, let me see how best that can be incorporated.

**Hritik**: [08:39] On the same line, means agent can surpass human intelligence—means there is a recent news I got, I have shared in the chat box. All the Adobe software are fully [well-coded? wipe-coded?] and it is available for all the platforms.

**Anand**: [09:00] And of the lot, PDFcraft is the one that I personally have been using left, right, and center as an Adobe Acrobat replacement and yes, it is stunning. It just works out of box.

**Hritik**: [09:15] Means it is running on Linux as well, which we often say that Adobe is not working on Linux.

**Anand**: [09:22] Exactly. But you were going somewhere with this, go on.

**Hritik**: [09:28] Means now the AI—means with the help of AI, a small company is able to release a state-of-the-art application. So, maybe we could drive some—our project as well in that direction, some part of it.

**Anand**: [09:44] I think so. Give me a second, I’m just trying to recollect my point of view on this. Yeah, no, not this one. Okay, so my thesis on this is that software in its current shape and form will, yeah, be something individuals can create. Increasingly, that’s happening. **Giving people practice to do this is certainly a good idea.** But also see if we can take this to the next level, meaning, what ambition is required to build software that agents will—or one person with an agent will struggle with? That I don't—I can't think of anything just yet, but agreed that we should try.

**JK**: [10:49] And another part of it is, I mean, what is the requirement? **How do they specify the requirement for the tool that they want with the agent? I think that’s more coming into the territory of, I mean, do they have clarity on what is needed?** Are they able to understand what is being said or what is *not* being said, more precisely? I think those—those things are the skills that will be more important. So, for example, PDF, I know, I mean, these are the basic things that I need PDF for, so it might be easier to say that. But there could be some minor things like, "Okay, it could be a signature, there should be a way to add signature," which may not exactly be told when somebody says "I want a PDFcraft-equivalent software." It may not come immediately to mind.

**JK**: [11:43] **But the skill for any student at least, any learner, any person at the moment is able to understand that hidden requirements that—I mean, many—yeah, how do you make implicit explicit? Exactly the exercise that we are doing right now. How do you write it down in such a way that it is whatever is there—I mean, it could be tacit memory or it could be an implicit memory. So, how do you make it explicit is what is more, yeah, more relevant for a student if you ask me.**

**Anand**: [12:16] Agreed. And one thought is therefore based on either usage or error logs or whatever, can we automatically find and introduce features? Anthropic is doing that, at Straive we are trying to do that, and we know of one project where they are actually doing this. So, that’s one direction. Another is, could software shape its interface as we go along? And possibly every user gets their own personal version of the software. Ultimately, it’s the same software, but you look at it, it looks like Photoshop; I look at it, it looks like the terminal. Could be a valid one. But how—what—I agree that this is something we should teach, it is not yet clear how. Let’s explore.

**Anand**: [13:12] I’m just going to make some notes on this. Okay, now in the light of this—actually, let me stop sharing a bunch of messy stuff that I have—what might we consider for projects? **So, keeping that interaction principle in mind, one exercise that I’m considering for projects is: trading for information.** We distribute information—for example, 50,000 invoices for 1,000 clients—except that while each student is supposed to process the invoices for a given client, the invoices are scattered across students.

**Anand**: [14:18] Trade for information. Now the question is, what do you trade? Obviously, there is a certain amount of valuable invoices that is in your pocket. But potentially, I’m quite happy if we structure this to trade anything else of value. And that could be, I don’t know, tokens, marks, something to explore to see what kinds of real-world strategies a human and an agent can come up with for large-scale collaboration as well as defection. Meaning, real-world negotiation—you don’t like somebody, you don’t want to give them your invoice, let’s deal with it. And of course, with some amount of duplication, redundancy, and therefore with incomplete information, how best can we still solve the problem? What aspect of information is most important and therefore I must weight it with a higher price is the kind of strategy that we are needing to deal with today. And the agent can answer these questions. Knowing to ask these questions is probably the important part today. But yeah, that is one direction I’m thinking of on Project 1. Any comments?

**JK**: [15:47] I’ll let the TAs and other instructors speak before chipping in with my thoughts. Mayank, Hritik, Jaideep?

**Mayank**: [16:02] No, as such for now. Yeah, we need to go to the more formal process of how this is going to be because right now it’s some scratch, so I won’t be able to provide much context from my side.

**JK**: [16:22] Yeah. So Anand, one more—one more important aspect if we are and I'm talking more from context that I'm more familiar with. I think it is also critical that when we are distributing information, the people also discover which kind of nodes are the most important nodes to search. I mean, first if I were to hit a node first where they will have a maximum idea of how the information is spread or things like that, that would be a very valuable skill. Because even if they don't exactly have the information, they at least have a pointer to where that information has already been received. So, if we can simulate that in project, that would be nice. So, along with, let’s say, invoices, we give an additional information that your invoice 13, 14, and 15 have been sent to so-and-so people. That would—that would be an even more valuable thing, right? I mean, so they can actually create a network and identify how typically this information is going out in general.

**Anand**: [17:31] Partly, but if we didn’t, the students would self-organize, create a sheet, and say "I have these invoices, I will dump mine in one shared folder," except for the 20% holdouts who will either do this last day before the exam or say "I didn’t even know about it," etc. **And where I’m going with this therefore is the providing of that information can possibly eliminate a self-organizing mechanism that might evolve otherwise. Second, lose out a signal where we spot the 20% holdouts and the strategies to deal with that, which is a real-life thing.**

**JK**: [18:12] Got it, got it.

**Anand**: [18:14] Yeah, and I’m not saying no, let us not provide any signals. I’m saying let us not provide the *answer* itself as a signal.

**JK**: [18:21] Ha, that’s okay. Yeah, I mean, so what I meant was this—I mean, yeah, agreed. I mean, some signal is worth doing. Because many a times in real life, you will have some signals. It’s not necessary for all 100%, but certain people *will* have more information. That is the information asymmetry, so to speak.

**Anand**: [18:39] And a dump of invoices makes the process again somewhat straightforward. "Okay, 80% of the students will put it all in one place," but if there is a cost to fetch the invoice, even if it is a rate limit—yeah, that then starts making the process a little more—well, you just have to start looking at how do I do this from first principles. **The original idea of how do you search for information comes into the skillset directly.**

**Anand**: [19:11] Correct. I suspect there’ll be an element of how do we organize this information as well. And from the invoices, extract in a structure, keeping in mind that invoices will be of various different kinds. Yeah, this of course is a very real problem. That kind of problem our finance team deals with.

**JK**: [19:31] Yeah, yeah, I mean, the same thing. I mean, why I said was because exactly—I mean, you have attrition, you have—you know what’s happening, right? I mean, there is one person who knows, "Okay, it should be available over there." Classic knowledge management problem.

**JK**: [19:43] Exactly.

**Anand**: [19:46] So yes, I’m therefore—so let me do this. I’ll take a shot at sharpening this. Maybe in our Wednesday call, I will have something like this. It may not be invoices, it may be more complex than invoices in the sense that it—yeah, maybe—

**JK**: [20:02] I mean, the problem statement can evolve. The actual context may evolve, but the idea is there is an information distribution and the idea is to self-organize and figure out.

**Anand**: [20:14] Correct. **The second thing that I was thinking of was creating a prediction market for the students to play.** With the prediction being grounded in something real, potentially IITM- or TDS-related. Let me randomly pick something. It could simply be—actually yeah, I'm not able to think of some real-life event off the top of my head, but yeah, it could be how many tokens will I spend by this particular date or how many tokens will AI Pipe have spent by this particular date, let us say. Let us say we share that information. Now, A: this is influenceable, at least partly, because if I want to increase the spend, at least up to one dollar, I can push. I can get a whole bunch of people to push it up.

**JK**: [21:18] Or you can have a network of people work to push it up.

**Anand**: [21:23] Correct. But that means two kinds of coordinations: one, coordination to set the same number, and coordination to get to that same number, which is one part of it. But of course, with the ability to trade, and then I can say I will short the $150 tokens and buy a different token level, etc. So, that trading strategy obviously is something that along with an agent, if we play smartly and if the agent can advise us on how to collaborate, move the number, that becomes powerful.

**JK**: [22:06] So okay, so one—I mean, I like the idea in terms of the AI pipe token because that’s a tangible thing. **So, it also means that we should have a dashboard which talks about the AI pipe token on a daily basis, right?**

**Anand**: [22:21] Yes. Like the stock market ticker, we will have—

**JK**: [22:27] Now this is an interesting exercise because I mean, you have to first of all tell the agent that there are X number of people who are already involved in this. You have to get a trend based on a weekly statistic. You have to get an idea of how many people are actually using AI pipe token or they are just doing it on their tokens as well, right? So, there should be some disclosures etc. happening within a group. And yeah, we’ll also have to factor in the cases where we figure out, "I mean, yeah, the AI pipe token just got limited out, I mean, the credit balance went out on some day." There was no one to make the changes, right?

**Anand**: [23:18] Yes, very true. But that’s what happens with the stock market.

**JK**: [23:21] Yeah, yeah, exactly. No, I think this is a nice problem statement in itself. And yeah, and it’s also easier. I mean, it’s like a portfolio that you create and you’re just validating the portfolio, right? I mean, where it went, what was it on that particular day, and we have the actual data available with us.

**Anand**: [23:44] Correct. And my aim is to see if this could be a pattern for future TDS questions. **Prediction markets as a pattern, allowing us to take broader questions. Prediction is probably one of the key skills we have to learn. Token prediction is an obvious one, and more such will emerge.**

**JK**: [24:07] I think we should have a Jeb-like thing where they create an interface—TDS Jeb or—and from a data science perspective also it makes sense because a lot of it is also on patterns, identifying behaviors etc., and converting it into numbers in some sense, right?

**Anand**: [24:32] Correct. Completely.

**JK**: [24:35] Yeah, I think this is a worthwhile—and so yeah, I’m pretty sure students are going to be—I mean, TAs will be hard. It will be hard for them to set out a session where these ideas can be taught. It is essentially machine learning in an applied format that they have to—yeah, but see—

---

**Anand**: [24:59] Yeah, but see, now I'm thinking, why should we burden the TAs to teach how to play in prediction markets? We should get a super-forecaster to teach.

**JK**: [25:11] Mm.

**Anand**: [25:14] Whole bunch of these people playing around, let's get one of them. Heck, let's have them participate. Okay, I know it may be—it will be short notice, but at least strategize.

**JK**: [25:26] And what are they using—how are they using the current limits of AI, etc., to improve their own prediction sense? I mean, they can talk of it from a—I mean, a fictitious scenario and what will they do to approach the problem. Yeah, this is a nice exercise.

**Anand**: [25:50] But failing which, yes, sorry, TAs will have to figure it out.

**JK**: [25:58] But I think it can be a collaborative exercise. I'm not saying TAs will be the best in it; in fact, there may be some students, working professionals, etc., who may have a better idea of how stock market trading happens. And they may be in a better position to handle this kind of—**what TAs can help is converting it into agentic format.** That’s where TAs can help. And that’s what—I mean, it can be a collaborative lesson that the students build and we just transform into an agentic part.

**Anand**: [26:28] Yeah, agreed. Those are a couple that I definitely wanted to incorporate. Let me see if there's any other major one for Project 1. I was thinking multiplayer games but I'll put those in the bonus.

**JK**: [26:54] Yeah, we had discussed that it is—it is better that it is bonus first and just for us also to get an insight of how students are interacting, and then maybe introduce them at a later point.

**Anand**: [27:07] Okay. Moving on to another which may not be apt for a project, probably more for a GA question. This is inspired by two things. The first, that a significantly large number of AI mathematical proofs are counter-examples. "Here is an unsolved problem, I will try almost brute force; this particular scenario is a counter-example to that theorem, therefore proven or disproven." Since that is becoming easy and is probably a generalizable theme, it may be worth crafting situations where a deep scan can find examples or counter-examples.

**Anand**: [28:12] Who put this poll in?

**Carlton**: [28:15] Oh, I just put the poll in, just to get a sense of—

**Anand**: [28:19] Okay. Perfect. That was one thought. Another came up this weekend when I was reading, re-reading for the Nth time *Calvin and Hobbes*. And this is one of the *Calvin and Hobbes* strips where Calvin places ZQFMGB on the Scrabble board and gets 957 on a double word score.

**JK**: [28:51] I remember that. Yeah.

**Anand**: [28:53] And I said, "Wait, hold on, double word score means even numbers," so it turns out—I mean, so this obviously cannot be possible. Except that it is actually possible on a real Scrabble board with real pieces—of course, not with real spelling; ZQFMGB is not real. But if we relax that one constraint, this actually turns out to be possible. And I had Claude run this—"Find me an example of where you can actually play and *Calvin and Hobbes* play in words that they would relate to." And it starts as a perfectly legal game of Scrabble. But then goes on to—"ZZZ" is a legal word in British English. Just that it happens to be a British dictionary. "ZIZ" is legal. But then you start going into proper nouns. And then at some point Calvin, if he decides that we are now going to go into Calvinball and start changing the rules—because you have to, to get to ZQF whatever—is it possible to end up with a combination such as that just that *one word* comes up to exactly 957? And the answer is yes. Not that it's even a unique thing, but it is—well, in a few seconds, we will—let's see. Yeah, so Hobbes adds "JINX", "JINX", "JINX", "JINX". And at which point Calvin places these. Yeah, if you take all of the words that it creates—the crosswords, so to speak—that comes up to exactly 957.

**JK**: [30:42] Okay.

**Anand**: [30:45] In other words, **needle-in-a-haystack problem**. And the number of needles that we could possibly create is quite large. And then if we say, "I'm also looking at the distances between solutions"—I don't want the same solution, I want diversity of solutions. Like, for instance, "Here's a theorem, we know it is true, find counter-examples, but not the same counter-example. If you have the same counter-example as someone else, both of you get zero." And the more distinct, diverse they are is what determines your score. Basically Pointless—**allowing us to teach how to get an agent to find what is away from the mode.** One of the main problems is agents are trained on the typical behavior of the crowd. Pulling away from that is the skill, and the strength or the extent to which we can do that is the measurement.

**Anand**: [31:50] Now, beyond this, what specifically in this—I haven't gone that far. But Scrabble was not a bad option. I mean, if we take chess and say, "How do you come up with what sequence will get you up to this spot and the paths that can lead you there?"

**Hritik**: [32:04] No, you can also do the BBC game, right? *Pointless*. 100 people—I mean, there's a question and 100 people responded to it. You have to find a pointless answer. Oh, it should be a correct answer, but it should be a pointless. So for example, African countries—or countries, non-Asian countries ending with Z. Or starting with Z. Pointless, pointless. So when you get a pointless—when somebody says the pointless answer, zero people have said it, the pot increases, the bonus pot increases by some 2,000 dollars or 250 pounds or 2,500 pounds.

**Anand**: [32:57] This could be a useful GA question where we ask not for an agent or an API, but a prompt that we can benchmark.

**JK**: [33:07] Yeah, exactly. Because this is—yeah, I mean, so it's actually rewarding outliers and you're thinking—you're thinking out of the box, not—you're not conforming to any standards over here, right?

**Anand**: [33:24] Correct. I've just made a note to add it to GA. Yeah, those were my thoughts so far for Project 1. At least for the first two that I suggested, I'll have a script that we can convert to a question, maybe a few others. Definitely one audio—I'm planning to increase the scope of audio questions and creating some infrastructure to make that easier going forward. I will again share that on Wednesday. But yeah, we should just be able to plan for more kinds of audio questions.

**Anand**: [34:15] One more thing. This is not immediate, but probably Project 2. At a specific time interval on a specific date—like in this 10-minute interval—join a Google Meet, literally stand and hold hands so that you touch your neighbor. Or wave as best as you can or whatever. Not worth project level even though there's a certain amount of coordination, but yeah, I don't see an agent being able to do that just yet. But **I wonder if we treat that as the foundation on top of which to build stuff, and ask what can be done that is creative.** Are there some groups that we should allow people to form, saying "In your own group create an art form?" Of course, some agent will evaluate—or at least partly evaluate, we could get real artists to evaluate also—but could physical collaboration be an element? I’m gently building up to a future term exercise where I would like some wearable that can measure some of the data that comes from those actions, but for now at least the visual data can be a useful follow-up.

**JK**: [35:51] Proxy. Yeah, it will be a useful—and the other part of it is, let's say in a GMeet if you are to wave, I mean, you have to put your cascade in such a way that—that's going to be even more—I don't know, for each of us we have our own configurations. So how do you make sure that the configurations are also consistent is also another thing.

**Anand**: [36:16] Frankly, **how to use Google Meet effectively is probably one of the most important 101s I have to teach people who are joining Straive.** Just a short while ago, I was—made a note to tell one person: "That little thing when you share your screen that comes—close it. Increase the font size so that people above 40 can read it. Everyone in the call other than you is over 40." etc., etc.

**JK**: [36:46] Yeah. I think, yeah, instructors and TAs—this is going to be—I don't know how you are going to evaluate it. So open for comments from your end. And again, it’s a Project 2, we are not looking at it at an immediate, but this could be an interesting bonus activity if somebody is able to—and we can say there should be more than 16 people in the GMeet because 16 is the tile that you have for max, right? So the number should—

**Anand**: [37:24] We'll create our own WebRTC-based task, whatever. We can create our own layouts. It might be easier than Google Meet. But agreed on constraints being an important part of the problem.

**Hritik**: [37:43] There are many on the GMeet who are experienced, so maybe if they could share some thoughts, it will be helpful.

**JK**: [37:53] Almost all BS students are much more pros than us.

**Hritik**: [37:58] Yeah, they’re more experienced even than TAs.

**Anand**: [38:03] And ideas for GAs and projects are also welcome, and ROE for that matter.

**JK**: [38:09] So this is the place where we are opening it up for the audience. Till now it was a closed game between us. So any questions, suggestions?

**Carlton**: [38:36] I think they're just stunned silence.

**Anand**: [38:41] It's a normal session.

**Hritik**: [38:44] Like most of the things they're like going over their head.

**Anand**: [38:49] That is also normal for us.

**JK**: [38:51] Yeah, it’s perfectly normal. So this is how—I mean, so what you see is how ideation for graded assessments and project statements happens. If you want to influence that, now is your opportunity. So what we were just doing were what are we trying to do with project problem statements or graded assessments. If you have an idea on what should be looked into, please feel free to type it in or just speak out.

**Anand**: [39:21] And crazy is not bad. You not understanding what you're saying is also not bad.

**Shreenish**: [39:28] So I'll just ask a couple of questions. One is, with the ideas you mentioned, if you could just briefly summarize what is the objective in terms of what the learning outcome is supposed to be? That might be helpful.

**Anand**: [39:42] Yeah. For Project 1, I was suggesting two things. **Trading for information.** About 100 invoices for about 1,000 clients each are spread across students, with some hints on where valuable information might reside. And their objective along with their agents and their collaboration skills is to pull all of this together. **The objective is to strategize information sourcing when you are not completely aware what information resides where.** Exactly the skill that we hired an entire team of consultants for four months ago and are selling as projects to half a dozen clients and is selling like hotcakes.

**Anand**: [40:33] Second, predict the AI pipe token spend over the month of, say, October 15th to November 15th. And this is like a stock market where you can buy and sell shares for "the spend will be 800 dollars, 900 dollars," whatever. We create a series of those, you can buy and sell those, and whoever ultimately—depending on what the actual price is, you win or lose. **That teaches your ability to, A: make good predictions, and revise your predictions as information changes using your agents and other tools as part of the skill.**

**Anand**: [41:26] Third, generate a pointless answer—pointless question given a series of answers. This should be based on a prompt as different from your peers as possible. Testing a couple of things: one, your ability to prompt engineer; B, your ability to work with your agent to come up with something very different but still functional and works well from the average that an LLM will generate. **Since models typically generate the average of human knowledge, your ability to push this away from that as far as possible while still maintaining correctness is the uniqueness skill that one learns.** Those were the three that I remember we concretely discussed.

**Shreenish**: [42:29] Okay. Then in the case of, like, for the first example, how do we go about what the evaluation part of it looks like? What is the evaluation criteria in order to know, you know—so for example, students will have some expectation, right? That if I do X, Y, and Z or if I achieve this, then I get a certain score. So what will—what do you suggest?

**Anand**: [42:55] I would act as and evaluate as auditors. Supposing there is an accountant whose job it is to find all the invoices of one particular client and file it from a tax perspective. And they make a mistake. Obviously, the value of the gap is certainly one major thing. The number of those missing entries is also something that is cause for penalty. There probably are a few other factors involved here, but that is how an auditor would evaluate; you would evaluate like an auditor. Should I simplify that?

**Shreenish**: [43:40] I think as when you create the spec on Wednesday, then we'll probably have a better handle on whether the marking scheme will work or not.

**Anand**: [43:51] God, sure. And welcome to revise it, of course.

**Carlton**: [43:59] Yeah. Has anyone got any questions? I mean, any of the students or the TAs? I mean, that could be a good opportunity now to put your two cents in, as it were.

**Hritik**: [44:12] One point I would like to tell to other participants—that Project 1 is not yet decided yet. So if you have any other ideas, you could present them here and we will have one discussion more on Wednesday internally. And if your idea feels better, that will be added to projects or similar to that. So please feel free to explore your thoughts and give your ideas.

**JK**: [44:42] So it's like saying to the priest: "If you have any objection, say it right now or forever be silent."

**Anand**: [44:52] I was thinking more like: "If you want to change the rules of the game in your favor—"

**JK**: [44:59] Yeah, now is the opportunity. Yeah, now is the time.

**Shreenish**: [45:04] So sir, like, will we be able to attend the Wednesday session so that we can give the feedback on what Anand sir has said right now?

**Anand**: [45:11] Wednesday, no, it’s happening slightly early in the morning we usually have these, but you're welcome to—actually no, we haven't yet figured that part out. Yeah, yeah. No, sorry. But if you have an idea, I need it anytime over the next—

**JK**: [45:30] You can post it in Discourse before Wednesday morning. Yeah, so this entire session is being livestreamed and recorded. So you can look at the session and figure out what could be added. By Wednesday morning 9:30, we will be in a place—we'll be in a position—a better position to describe Project 1, hopefully. So yeah, if something comes before that, we will definitely take a look at it.

**Carlton**: [45:58] There are three people who have said they have experience in trading and financial markets. Maybe they'd like to give their two pence on the token trading? Do they have any thoughts? Whoever said yes, because I am unaware—let me—I’m absolutely ignorant of financial markets. I know the Sensex, but I'm not aware of how it works.

**Anand**: [46:40] Should I close the poll? Because then it will, I think, publish the results, right? I think?

**Carlton**: [46:45] Yeah, yeah, you can. Okay, I've closed the poll.

**JK**: [46:55] Was it anonymous or—

**Anand**: [46:58] No, no, it wasn't anonymous. Responses appear with names.

**JK**: [47:02] Oh, responses appear—oh, you're right. Good point, Carlton. It is therefore not anonymous.

**Anand**: [47:10] Yes. I had no idea how to keep it—I haven't the foggiest either.

**JK**: [47:20] No, it will come in your—it will come in the Drive, who clicked what.

**Anand**: [47:26] Ah, okay, okay. Let me have a—okay. I think currently what has happened is "responses appear without names" was selected, so it may not exactly—I don't think it was selected. Okay. Let's see. But anyway, this is okay. Himanshu is saying he's tried a few times on trading, so fair enough. Please consider looking in Himanshu for trading tips on the prediction market.

**Anand**: [48:32] But for the students, just FYI, we are experimenting with this format on Mondays. So probably came in and stuck along trying to see what the hell is happening. This is the kind of discussion that we have usually on Wednesdays on what questions to craft, and then the TAs or instructors actually create the questions and deploy them. **We wanted to loop you in partly to understand how and why we create the questions we create, and the level of ignorance that we have in as fast a changing field as this.** But secondly also to have you participate and feel free to do that as and when you like to shape these questions because you in many ways have as much exposure as we do to AI. And that is pretty much the primary game in town. So any creative thinking could help seed our thoughts as well. If this is not of value and/or if you have absolutely anything better to do, you should please just not join these sessions. Of course, they are recorded and made—

---

This call recording features **Anand** (LLM expert), **Carlton** (Instructor), **Jaideep** (TA), **Shreenish** (Student), and brief appearances by **Mayank** (TA). The discussion covers real-time UI fixes for the exam portal, the use of LLMs to operate mobile devices via USB debugging, the philosophy behind assessment design, and the intent for students to use AI agents for high-precision tasks.

***

**Anand**: [49:59] ... and made available. You can always see the transcript and get a sense of what you might need to know, what you want to anticipate, have an agent prepare you for it, etc. That is a perfectly viable strategy. And if you are joining in, might as well contribute in some shape or form. If nothing else, it will be practice for you to see how you can steer a discussion where you have very little context.

**Carlton**: [50:26] And I think the other key thing is the idea behind having these Monday ideation sessions visible to you is also that we are actually expecting some interaction. So if we don't gain interaction, then we might as well say: "Okay, students are not interested in engaging." So then we may not even have this. So then you don't get the benefit of actually seeing how this works or steering how it moves. So my strong suggestion is whoever's in the call, **make use of this opportunity to at least, you know, express your thoughts or feelings or opinions.** And that's useful to us because then we can actually do something. Shreenish, yeah, go ahead.

**Shreenish**: [51:05] Yes, sir. So like, I had a few, not suggestions, but like some improvements which I feel are necessary. So like creating a drop-down menu for like the questions. So in this way, if we have completed a question, we can just like pull up—pull it up, so it will go up and it will appear as a single line. And also in submitting questions—so like what happened was I was not able to run Groq on my laptop, so I ran it on my college PC on Friday evening. And I had to like re-submit it on Sunday because there were some questions left. So because of that, like I was not able to submit that specific Groq question on Sunday because it was not running on my laptop.

**Anand**: [51:52] The second is intentional. The first... let's fix now. I'm just going to share my screen, we might as well finish it off. So let's see. Let's actually see. Is my dev server running? No. Let that run. Okay. So in the exam portal, currently, when somebody has solved a question correctly, there is no clear, strong enough visual indicator the question has been solved. And one of the students suggested that we might perhaps collapse the question by default, of course, allowing them to expand it, clearly visually indicating that it is collapsed because it's solved, etc. Now, we don't want to change the UI too much. **What is a minimal elegant solution for this? Explore and implement in a way that doesn't modify the code too much and inspect the screenshots to see if that, from a usability perspective, is the right kind of change.** Let's get that done. I'll put in a pull request for this on the dash core slash exam and commit as a separate branch and push. So that will happen over the next whatever, 20 minutes or so.

**Carlton**: [53:44] So, Anand, just a question here. So I noticed you use just the normal ChatGPT as opposed to the Work [Enterprise]. Is there any difference that you found in using normal ChatGPT versus the Work, which is supposedly optimized for coding?

**Anand**: [54:02] **Work charges me or drains my tokens. Chat does not.** I have gone very far in engineering Chat so that I can use it almost like Work. Work can work for longer. Chat may be slightly less smarter, but for this sort of a problem—

**Carlton**: [54:23] Yeah, long duration tasks. The same thing for Claude also. The Claude Work—it drains tokens like anything, whereas my skills and other kind of standard-thing interfaces are much better because I use projects a lot more; project chat inside a project is much more useful for me than over-work in Claude. That's my experience.

**Anand**: [54:43] Yeah. I use projects but within GPT rather than Claude. Yeah.

**Carlton**: [54:50] Yeah, I mean, it's—it's your starting problem, right? I started with Claude, I stuck with it.

**Anand**: [54:57] Yeah. Jaideep?

**Jaideep**: [55:00] **I have once managed a ChatGPT chat to operate my mobile.**

**Anand**: [55:12] Woah. How—yeah. Via something like same local MCP?

**Jaideep**: [55:20] Huh? But no, no. And then how did you connect your system to mobile? **USB debugging. Just a Type-C cable.** Remove it from the charger and connect it to your laptop. And then ask it to use—I mean, it has ADB CLI tool. `adb devices` lists out the devices you have. It actually built a mobile application and had taken screenshots from the mobile and then tested out. **GPT 6.1 Sol on extra high running on ChatGPT chat.**

**Anand**: [56:12] I have no idea if you've tried mobile-run. I haven't. But this has advertised itself as something like an agent browser for mobile, an agent-friendly CLI that could potentially be used. It's on my list to try; I haven't yet. But **how easy or how well does a 6.1 Sol-like model directly do USB debugging?**

**Jaideep**: [56:40] **6.1 Sol isn't available yet in the chat, but 5.6 Sol is far too good when I've tried that.** Now we have 6 Sol anyway in the chat.

**Anand**: [56:56] I—I should have put 6 Sol, but go on.

**Jaideep**: [57:00] Yeah. But in the Pro subscription, 6 Astro Pro—I think it can run for four hours non-stop even in the chat. But of course, you need to pay $100 for that at least.

**Anand**: [57:17] Huh. But your earlier point that even 5.6 Sol is able to do USB debugging smoothly—let me give that a shot. That is something that has been on my list. I just haven't—meaning, for a GA or for a project, I haven't gotten round to doing this. But this—and I know I've mentioned this to some of you, at least the core team—**what I'd love to do is have one exercise where you have to take a selfie with a classmate at a physical location using an application that we write.** That's one part of it. But the other is having people create their mobile applications. Okay, I haven't thought beyond that, frankly. That is definitely something to introduce in this term. The ability to deploy across a wide variety of platforms and infrastructures is becoming important.

**Anand**: [58:23] One of the things I was exploring day before was the Unikernels. The earlier idea was in HCF computing, you need an operating system because not everybody can build all of the features required for an operating system. Therefore, applications sit on top of operating systems and use the underlying calls. What that means is every application that needs to run is exposing a large surface of potential vulnerabilities. **Unikernels are an idea where you say: "On a device, I will run only one particular application."** It combines the stack of the operating system as well as the application, copying from wherever—the agent that's going to write it and test it. So what is our problem? It is no longer difficult, which reduces the security footprint, etc. But where I'm going with this, therefore, is **creating applications not just in unknown languages, but building operating systems is now part of what we have to treat as the portfolio of Tools in Data Science.** Mobiles would be an immediate step towards that.

**Jaideep**: [58:49] **But wouldn't the confirmation to either the Apple Store or Play Store regulations be a hamper in this case?**

**Anand**: [59:00] No, absolutely. But I am finding two things. Number one, **the regulations are more to protect businesses rather than technologies.** What I mean is Apple will get sued by Temu if you build—put in an application that scrapes the Temu website, therefore I'm blocking it unless blah, blah, blah, rather than: "Oh, this is a security protocol violation." Not saying that that is not the case; I've seen enough incidents of the business side of it coming in. And therefore, there is a reasonably larger class of applications—this is my theory—than we might think that a TDS-like course could have published on an App Store. Secondly, my aim isn't as much getting it onto the App Store as much as getting it into a developer's mobile among the students. That's enough for us for now.

**Jaideep**: [59:58] Yeah. Yeah, I mean, they—they will figure it out. I mean, they will bypass the root permissions and rootkit and others and figure out a way to deploy. Yeah.

**Anand**: [60:10] With that, I know we are at time. So let's close and core team will see you on Wednesday, others will probably see you on Monday. Shreenish, just post on Discourse or ping on WhatsApp or something, or—if someone's left, please carry on.

**Jaideep**: [60:28] Yeah, bye.

**Mayank**: [60:30] Carlton, I will also be dropping off. I have a call to attend. If there are pending questions for the next 10 minutes, you can just take a shot at it and then formally close this session.

**Carlton**: [60:44] Yeah, sure, great. Yeah, thanks. Bye. Bye.

**Carlton**: [60:52] So, the one thing is there's no—there's no promises that I have answers either because much of this what they've discussed today is new to us as well. But go ahead.

**Shreenish**: [61:02] I know, I know. I want to ask on like GA0. So first of all, there was one question which answer was 71. So I just like tried brute force till 71 and got it correct. So I think, like, it can be made a bit harder.

**Carlton**: [61:17] Yeah. By de-—so one thing is there is a gradation of questions, okay? So we want some students to be able to get the answer to—and some— [audio cutting out] two questions, what... sir your voice is breaking. [audio cutting out] ...and we had discussed this with JK. We wanted to have a different GA... to have the same one. **The reason we wanted to see if students from... resources students from the previous term used in order to solve it.** So we would know then if that's happening if we looked at the graph of the distribution of what the scores were. So for instance there's a heavy right-skew... [audio cutting out] Carlton sir your voice is breaking. Voice is breaking, sir. [inaudible]

**Carlton**: [62:59] Hello? Am I audible?

**Shreenish**: [63:03] Yes, sir, you're audible now.

**Carlton**: [63:05] Okay. Yeah, sorry, my connection was unstable for a minute, so I could not hear anyone or anything. But did that answer your question?

**Shreenish**: [63:17] No, sir, I was not able to hear you like... the complete answer was breaking.

**Carlton**: [63:25] Okay, yeah. So what I was saying was—I'll answer in short—for GA0, we have kept it virtually the same as last term because JK wanted to see as a baseline if students have used the previous term's resources, like students who solved it the previous term. So they want to see if there is some transference of that knowledge that was gained about GA0 from the previous term to students carrying it over to this term. **And the way we would recognize that is by looking at the distribution of the scores of GA0.** So last term there was a heavy right-skew in the distribution graph. So we know that, okay, that, you know, people are finding it hard as opposed to it moving to the opposite direction. So if we find it's moved to the opposite direction, then we know there's transference happening.

**Carlton**: [64:25] So that's the reason GA0 has been left virtually the same. And within GA0, as I think Hritik has mentioned, **some questions are meant to be able to be more easily done than others.** But that's by design because we want some students to at least be able to do some of the questions.

**Shreenish**: [64:37] Yeah, I was able to do like 20 marks only.

**Carlton**: [64:41] Yeah. So that's—so that's the reason. So it's so that—if we make everything uniformly hard, then that's going—we're going to get a lot of complaints. And not just from students, we'll get a lot of complaints from the BS program because they will be asking us the question: "Well, why is the mark performance so poor?" So we—so we get pressure from both sides, okay? Which is we get pressure from students, but we also get pressure from the admin side of things. **So ideally what we're looking for is a normal distribution or actually a bimodal normal distribution.** If we get a bimodal normal distribution, we know that the evaluation is roughly fair. So that's what we typically aim for.

**Shreenish**: [65:26] Also, sir, so I want to like—can I share my screen for a minute? I want to like show a bug.

**Carlton**: [65:38] One thing I would suggest is if you've got a bug, put it in Discourse because then that becomes part of our knowledge base of things that are—that we notice as an issue.

**Shreenish**: [65:49] It's not a bug, but I'm facing this issue like just if—if I'm doing something wrong. [Sharing screen] Is my screen visible?

**Carlton**: [66:05] Yeah.

**Shreenish**: [66:06] So like, in this, **this was the target silhouette and this is what I have got.** So like, I tried the copy-pasting it, but it is not like giving... submitted arrangement does not match assigned target silhouette.

**Carlton**: [66:27] Yeah. So, Mayank, you want to answer this or...

**Shreenish**: [66:32] I tried like till getting this till the state data, changing it by one-one, but it is still showing incorrect.

**Carlton**: [66:41] Agrim should have an answer for this question.

**Shreenish**: [66:47] He's not on the call, right? Is Agrim on the call?

**Carlton**: [66:56] So one more thing is this particular question was created by Anand. And if there are any bugs or difficulties with the question, then he's probably in the best position to answer it because he constructed the question. Agrim did the integration of it into the portal. And I don't think there is a bug with the question. What usually Anand had said in regards to this specific question was **sometimes it can be off by a very small amount and students will still get the wrong answer. The idea is to actually get an agent to solve the question. Because an agent will do it very precisely, whereas if a human does it, you're almost always likely to get it wrong** is what I've been told. So—

**Shreenish**: [67:41] Yeah, yeah. Also, the—like this GA0 was very enlightening because I didn't—GA1. So like first of—in the first GA0, I copy-pasted like every code into GitHub then pushed it and then did run it on Vercel, whereas now in GA1 I got to learn that like I can give ChatGPT the access of like Vercel and GitHub. So I just like submitted it and the ChatGPT like does it everything in the background.

**Carlton**: [68:11] Yeah. In fact, I would go a step further. I don't know if it's been covered in any of the sessions. So **another way to solve the problem is to actually give MCP [Model Context Protocol] access to your browser to GPT, and then it can literally look at the code that is underlying the application itself and it can manipulate things directly using the MCP.**

**Shreenish**: [68:40] Okay, sir. I will also try to do that.

**Carlton**: [68:43] Yeah. You might find more success that way.

**Shreenish**: [68:46] Yeah. Thanks a lot, sir.

**Carlton**: [68:51] Yeah, but go ahead and put the post because if there is a bug, others may be facing it and it's always the best place to do that.

**Shreenish**: [68:58] Yeah, sir, I will put it on the Discourse.

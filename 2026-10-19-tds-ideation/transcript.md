# Transcript

**Anand**: [00:00] Okay, why don’t we dive in? I guess you’ve seen the latest GA—sorry, latest Project 1 question. But overall, before we dive into anything else, anything that we need to discuss about Project 1?

**Unsure**: [00:22] There were some issues, I think Mayank has pointed out that...

**Anand**: [00:26] I believe it's resolved. Mayank’s PR—I made some tweaks and pushed it. And I am able to submit for Question 2. But Mayank, are you able to?

**Mayank**: [00:39] Okay, yes. (Thumbs up).

**Anand**: [00:43] That’s resolved. I thought I’d give you the philosophy behind the questions that are emerging in P1 and then we can go on to GA3, maybe.

[01:13] The **prediction market** is as we discussed last week. Let’s see what the current state of the predictions are. I believe there were about 200 to 300 predictions or trades made so far and most people seem to think $10 to $20 is where it will stay. Of course, a lot will depend on the questions that will be asked—what GAs will be there, how many people are active, etc. But the published reasons from the class are flowing in. So, this is a good view to understand what we collectively think. **The skill that we want people to learn is leveraging the wisdom of the crowds**, being able to influence using data that is not available to an agent—like you know where the course is going based on discussions with others, which an agent will not be able to figure out. Things like that. So, **what does it take to use real-life data and feed it to an agent so that it can guide you on the right kind of trades to make**, or you make the trades yourself? And B, are you in a position to influence these? That’s another element.

[03:06] Second one, I will very briefly go through the skill that we want people to learn. **This may be the most important, at least of the three P1 questions and perhaps of many questions that we’ve designed so far.** The idea is: agents can do anything. How do we figure out what is useful? **The entire specification problem is what we are trying to teach here.** Put another way, we are saying: people promise to create something. That’s what you’ll be declaring in your recording. Give it a week, think about it, make a couple of corrections if you want—you have up to two revisions. And by Wednesday end of day, make sure that you have committed to what you will build. And when I say "build," it could be any service offering also, like: "Look, you ask me one question, I will give you one answer." That's the offering that you publish.

[04:29] And then we’ll create a small marketplace—nothing major in the marketplace, it simply will be a credit distribution mechanism. Anyone can buy services or a product from others by paying credits at a price that the seller and buyer agree on. And that gets transferred from the buyer to the seller. **This is really aiming at two things: one, are you able to create something that is useful?** And it’s when people buy your offering that your score goes up. At the same time, it is to leverage what people are offering. If a really smart student says, "I will give you one human answer," or somebody with a unique piece of hardware says, "I’ll let you run a game on it," or somebody really good with interview skills is able to interview you—whatever. Effectively, **you’re getting through credits something almost the equivalent of cash to be able to pay for valuable services that the students may offer.** So, leveraging that to your benefit is the other skill that we’re hoping people will learn. Any questions on Human Exchange?

**JK**: [05:53] Anand, I think we didn’t discuss this during our discussion, but I think one point of question would be the Human Exchange part. We discussed the outline format, but **should everything be tied to, anchored around TDS?** I think we were discussing that day that it needn’t be, right? It could be practically anything that they want.

**Anand**: [06:21] Absolutely, that is a good point. I will add that as a clarification. In the TDS Human Exchange question, clarify the following: one, **the service does not necessarily have to be limited to TDS; it can be about anything.**

**JK**: [06:44] **Legally permissible.** You have to add that.

**Anand**: [06:48] Okay. (Laughs). Should be legally permissible as per IITM as well as the government laws.

**JK**: [07:01] Yes, government laws, yeah.

**Anand**: [07:07] We'll clarify that.

**Anand**: [07:11] So, no Bluetooth peer-to-peer communications, is it?

**JK**: [07:16] No, no. That is—wait, who’s banning that? No, that is only restricted within—the specific software alone is banned in the App Store.

**Anand**: [07:27] Wait, hold on. I was actually thinking of doing some Bluetooth peer-to-peer thing. What is banned?

**JK**: [07:33] So, **the Government of India has banned that app in the App Store which uses that peer-to-peer communication bouncing.**

**Carlton**: [07:44] Because they cannot monitor that. Because it works completely offline, they are not able to monitor communications. So, that’s why they’ve banned it both in the Google Play Store as well as in the Apple App Store.

**Anand**: [08:00] Okay. Nothing preventing a developer from building an APK and putting it on their phone.

**Carlton**: [08:06] Absolutely. No, not yet anyway.

**Anand**: [08:11] Fine, good to keep in mind. Cool. Anything else on this question?

**JK**: [08:18] Ah, there is a question from Preethi.

**Preethi**: [08:21] Sir, I had asked this query in the Discourse forum, in your GitHub space that you had created. Sir, **is there a minimum or maximum limit to the services being offered, like only one service is to be [offered]?**

**Anand**: [08:37] I do remember your question and I’m trying to see where I had that open. But there are two parts to this: one is, can multiple students buy or exchange the service? The answer is yes. Can the same student make a repeat purchase, so to speak? The answer is yes. All we’re saying is everybody will be getting a certain number of credits. You, between you—so what you can do, for instance, is say: "Today I have decided that I will offer this service to one of my friends for one credit." And you register that. Both of you sign off saying, "I have delivered the service and received one credit," and vice versa, "I have received the service and am delivering one credit." That transaction happens on a portal that I will design. You can offer it at a different price to someone else. You can do whatever you want, however you want. **It is just saying that this particular service is available for people to take advantage of.** Keeping it open that way. So, short answer to your question, Preethi, is yes.

**JK**: [10:04] So, basically, the intellectual property of the service still belongs to you. So, you can decide whomever you want and whatever the rate is.

**Preethi**: [10:14] So, the credit price tag or whatever—we only have to put, right?

**Anand**: [10:19] Yeah.

**Preethi**: [10:20] And in that recording, like if I say if I’m willing to offer two services—say, anything like counseling or just lending an ear for 10 minutes or something of that sort—so that should be agreeable, that should be—like, I should already have a buyer for it beforehand?

**Anand**: [10:39] No, no. That could be tricky before Wednesday. No. You estimate what will have high demand and that you can fulfill, and you offer it. **Multiple services might end up being confusing, but also broadens your scope.** You can make the tradeoff. Nothing from our side that stops you other than legality.

**Preethi**: [11:03] So, a single recording for any number of services—like one or two or three or whatever, right?

**Anand**: [11:10] 100, if you think people will even listen to it. No, no, I’m saying everything to be mentioned in that one recording only. What will be published is the recording and a transcript of that recording. Okay? Probably maybe an automatically extracted title that summarizes it. Keep in mind, **there are going to be hundreds of services on a portal.** Will people immediately understand it based on an automated summary that comes out of what you said? Is something you have to decide.

**JK**: [11:47] **How do you top the Craigslist? That’s what you should start [thinking about].**

**Carlton**: [11:54] So, I mean, that brings another question. When you design the marketplace, how does it decide what goes on top? Is it—is there some algorithm? Is it alphabetical? Because that will also make a difference in how you pitch it, right?

**Anand**: [12:12] Very true. I think random will be the most, how should I put it, fair. However, we will have sorting options based on most recently purchased, maximum credits exchanged, maybe a few other reasonable marketplace kind of sortings.

**Carlton**: [12:35] Okay, so there’s no SEO type capabilities in the...

**Anand**: [12:41] I think **more aimed at humans than the marketplace itself. The marketplace will be agnostic to the content.**

**JK**: [12:53] So, there’s a question from Adwitiya who is asking whether the services are supposed to achieve a shared common goal. Yeah, you've answered that already. The shared common goal is you get to purchase credits and you get some marks for it. That’s the shared common goal over here.

**Anand**: [13:16] And any other questions on this one, please just toss it out here. Let’s go to the third one, which is **Air Ink**. The idea is that each of us will on our mobile phones—this won’t work on most PCs that I know of—so, you log in on your phone and then it will ask you to draw. Let me turn off my blur and see if you are able to... okay, this is clearly visible, right?

**Unsure**: [14:02] Yeah.

**Anand**: [14:03] Okay. But for whatever reason, I'm...

**Unsure**: [14:09] You can just log in through your phone and share your phone screen, maybe.

**Anand**: [14:14] Log in through my phone and share my—okay, I have not yet figured out how to set that up. So, I will do that before our next session. But once I log in, there should be a little dot that you can see that moves around. That dot is right now at the bottom of my phone because I’m holding it vertically. But as I tilt, it will move. And we’re supposed to place the phone flat like this, follow a set of instructions for calibration, and once you’ve calibrated it, you will be able to draw shapes—like, for instance, if I do a "hold to draw," it’s drawing on my screen some shapes just because I’m tilting it. It’s moderately intuitive once you get a hang of it. You’ll be asked to draw three words—random letters—and submit it. That is the first part of the assignment.

[15:21] So, this random set of—and once you do that, you submit it for now. That’s it. The date is next Monday end of day is when this gets submitted. After that, we will be asking students, given the underlying tilt data, etc.—basically the measurements of how people drew it—**can we figure out the word that people drew? That will be the machine learning exercise that you will end up having to solve.** For now, this week, it's just "draw the stuff." That’s going to take maybe five minutes. And yeah, **don’t use agents for this.** We will check if it is agent-drawn and that's easy enough to do. A, there's no point—it costs you too many credits compared to the effort that you do—and B, it actually doesn't help.

**Carlton**: [16:30] I’ve got one question with regards to how the words are drawn. So, assuming there will be several characters in a word, **will there be a way to pause after writing a character?**

**Anand**: [16:44] Yeah, yeah. You have to **hold and move to draw; you release it, it will stop drawing.** Try it out, it’s quite easy. It’s one of the few things that I actually tested extensively. Quite easy.

**JK**: [17:02] (Laughs). Okay, it requires some amount of physical skill.

**Anand**: [17:08] About as much as balancing a little bit of water in your hand and no more than that. Yeah. So, those are Project 1 questions. Any questions on the motion game, Air Ink? Preethi says the screen seems to be frozen. Is my screen frozen for anyone else?

**JK**: [17:27] I think the screen share has stopped.

**Anand**: [17:30] I had stopped the screen share.

**JK**: [17:33] So, we were not sharing. I mean, the whatever we have discussed till now will not work on a PC, like what Anand said. So, that’s why you saw the screen blank while it was demonstrating.

**Anand**: [17:48] Okay, if there are no questions on Project 1 Question 3—and of course, maybe more questions will emerge as we go along—let’s talk about GA3. So, one of the things that I’m exploring is **cost and time of verification.** In our current ROE, we are giving people very limited time. The GAs are probably not the best way to practice that, meaning you have a good week, 10 days—that allows A, agents more time and attempts, and plus as a group people can collaborate and solve. And therefore is **not realistic enough practice for the ROE, I suspect.**

[18:40] So, for GA3 and a few others, one principle I want to establish is A, **slightly less time.** So, the deadline, if I’m not mistaken, is 25th—that is this Sunday, right, for GA3?

**JK**: [19:01] Yeah.

**Anand**: [19:02] So, that deadline will stay. But the questions will be released in stages and with some of them having probably only a day or two to complete. There’ll be some amount of prep that you will have; you’ll be able to plan for a few of these, some you’ll be able to solve upfront, but even then it won’t be more than five days—that is, only tomorrow that we’ll start releasing some of the questions.

[19:35] The second thing is **some of these questions will have a limited number of checks.** Right now, you would be able to test a hundred times. I mean, let’s take the Geoguessr game that Mayank had created. In that, we can now type in every single combination of latitude and longitude to the third decimal, etc., and eventually figure out if it gets it right. So, that’s a brute force thing. In real life, you would not have the luxury of such rapid iterations, nor would verification be free. So, **for a growing number of questions, the verification will have a cost as well. It may be limited number of verifications or tradeoff verification against marks.** So, you decide to pay for one more verification if you think that that will substantially improve your score's likelihood. Those will come in GA3.

[20:41] But that apart, I have a few questions from previous terms that we’ll be repeating with revised seed data. That’s my thought. But let me also share how I’m thinking about what we’ll be covering in GA3. This was the idea—I won’t be able to show the results of the prompt partly because of Straive confidential—but the intent was: **I was checking based on the data that I have, what are typical LLM engineering tasks that clients are asking Straive recently?**

**Carlton**: [21:20] Anand, just before you proceed, I just wanted to check with JK. So, the thing is, from an operations perspective, there are four GAs that we will be using for end-term eligibility. So, we’ve done three, and this will be the fourth one. So, are you happy that this kind of a GA is okay to be—in terms of the gradual release and people having this sudden change in expectation for an end-term eligibility GA? That’s the only question I have from an operations perspective.

**JK**: [21:53] But you are still containing it within that week framework, right? So, I don’t think there is a problem for that.

**Carlton**: [22:00] No, I agree. It’s just that I think students will find it unexpected, right, that suddenly the way we have...

**JK**: [22:09] I don’t think TDS has never ever followed... (laughs). No, no, I agree. I just—not that I don’t agree, but I’m just trying to see it from the student perspective as well. So, that’s why. No, it’s okay. So, see, they had three—I mean, we were looking at it, right? Right from GA0 to GA2, they have enough time. So, at least three of the assignments have been as per the prescribed plan. And we are also transparent in the design process as well as the evaluation process and why we are doing it is very clearly explained to them upfront, right? So, I think operationally—operationally, that is fine.

**Carlton**: [23:01] I just wanted to get you on record saying that so that when we show the video, people understand what’s happening and why.

**JK**: [23:09] JK said. Yeah. JK said! You’re on the record!

**Anand**: [23:13] And Carlton, JK, if at any point you decide we need some flexibility, I guess the date is probably okay to change. Duration, we are shortening.

**JK**: [23:29] Yeah, yeah. So, I mean, in case we need to push a couple of days, that’s absolutely fine. But I think the constraints are still okay because we are trying a new type of assessment in GA4—primarily because of limited time, I mean, whatever the basic rationale that Anand explained, which is a crucial skill for students also to understand. And it’s not like all 10 questions are going to be of that nature. Anand, it’s just one or two questions in that GA which will be of this nature?

**Anand**: [24:01] More than one or two, but not more than five.

**JK**: [24:05] Yeah, yeah. So, I mean, you will have around 10 to 12 questions of which five will be of this nature. Which means, Carlton, technically they can get up to 70% or 60% to 70% without the vagaries, right?

**Carlton**: [24:22] Yeah, and that’s fine because from what we’ve seen of the distribution—so, I’ve just updated the official scores and all of the first three are very heavily, you know, left-skewed—sorry, right-skewed, yeah. And so, there is, you know, there’s no reason why people should complain about it, but there will be some who would.

**JK**: [24:44] I mean, there will be, but the counter to that is: we are still giving you greater than 40% ability to answer greater than 40%, and that’s all what that eligibility criteria looks at, right? Yes. So, we are—we are also operating within that constraint. So, yeah, I mean, for all the people, this is what typically happens in our discussions also. I'll play the quartermaster towards the operational decisions and some of these decisions happen like this when someone points out "this could be like this." So, this is how we come to an arbitration. Yeah, this is fine, this is not fine. Yeah.

**Anand**: [25:24] So, I was reviewing what are typical LLM engineering tasks that clients are asking Straive recently, and which of these we should be covering. And that’s part of what will inform the actual GA questions. And I’m going to stop sharing at this point because there are few things that probably shouldn’t be going into, but I’ll give you a broad sense.

[25:55] One of the top LLM engineering tasks is: **can we build verification systems that can catch AI mistakes?** The primary objective is to filter out the uncertain results and have humans validate. So, a sense of confidence calibration, both from models but also from humans, is going to be an important part, and we’ll incorporate that into a few project or GA questions.

[26:26] Second, **how do we organize information in a way that will produce answers to a reasonably broad range of questions?** Do I need to construct an index? Does it need to be a vector index? Does it need to be a graph index? Does Agentic search work fine? What combination of tools—given a set of tools, how well we'll be able to solve it? This, again, will certainly be one, either GA kind of question or project kind of question depending on the complexity.

[26:59] Third is **what kind of workflow... a bunch of things like this.** So, that will be one part of the set of questions that I’m planning. I tried a few; they ended up either being too easy or too hard, and therefore I had to give up. One question that we discussed last time that I simulated—unfortunately at a cost of $500—whoa! Yeah, it just escaped me—was the whole invoice structuring thing. It generated the invoices, it ran a whole series of simulations of how people would try and solve it and so on, including using Astra to solve some of these, which is where I think it got out of hand. But the final conclusion was that that is a hard exercise to frame given how we are organizing it. Multiple people, multiple agents can collaborate. There are optimal solutions that you can drive towards, at least the way I had structured it. So, had to drop that question or at least the way I had structured it. These will form part of the next set of questions.

[28:25] The Tangram question seems to be moderately promising. It was based on a set of 100 seed configurations. Once that set of seed configurations is solved, it is solved for everyone. Therefore, the question in its form is not reusable. But in the absence of knowing or in the absence of a fixed seed, that pattern of questions is useful. So, one thing that I’m thinking of—and this is something that Sujal, who’s interning at Straive now, had shown as a possibility—is: **given 3D shapes, can we create cross-sections of those and see if it’s possible to infer the original shape?** What is the simplest shape that matches this set of cross-sections, with the cross-sections being provided as raster, like we had done in the Tangram one? This in itself is not, how should I put it, agent-proof. But rather the judgment comes when saying: what you may get may be valid but is not necessarily the shape that produced it. You may ask for additional cross-sections, up to maybe three cross-sections, which will help you determine what the actual shape would be. This is something that agents are—from the looks of it so far—not that good at figuring out, whereas a person... [recording ends]

---

**Anand**: [29:59] Whereas a person looking at a shape and saying, "Okay, if I tilt it this way and maybe ask for a cut here, will it help? Okay, let me request this cut. Move it around this way, ha, this is another cut that I think will test my hypothesis," because **they have an intuitive feel of 3D space that models currently lack.** That will likely be one kind of question that I’m thinking of.

**Carlton**: [30:22] That might be... well, when it comes to manipulating objects in 3D space and recognizing it, usually there’s a gender bias in that from what I’ve read not that long ago. But that’s why, for example, men are better at visually figuring out something—I mean, I’ve read something along those lines, I don’t remember when I read it, but there are some differences that come in that kind of question, I think. Okay, but I need to verify that. That's just something to be aware of.

**Anand**: [31:05] Fair enough. Yeah, we won’t give a handicap or a bonus in any case, but something to be aware of. Aligned. And **business simulations—Monopoly-like games as groups, but more realistic business games—are the other thing that will likely come into Project 1 over the course of the next week or so.** So, that was a good half hour of monologuing, but let me pause here. Those were my thoughts. Any suggestions on the kinds of questions we should factor in? Especially to instructors, TAs, etc. Any patterns of questions you think we should include to make sure we teach what’s required in an Agentic era?

**JK**: [32:11] Yeah, I was going to say **harness—harness engineering or building your own harnesses.** Now, interestingly, I think I just yesterday or the day before, I read that **Google had released, open-sourced a Harness 2**, I think it was called. Yeah, which apparently improves the agent without having to change the model weights. So, it’s an interesting thing. I’ve not studied it myself, but that would be interesting to see.

**Anand**: [32:50] Yeah, **agents doing harness optimization seems to be a close-to-solved problem when you have moderately exhaustive test cases.** So, the thing I suspect will be still useful when students graduate will be: **how do we optimize a harness for unknown scenarios?** Meaning where you don’t necessarily know what is correct or what to expect.

[33:20] So, here is one thing that I’ve been toying around. Let us say we take a reasonably inexpensive model like Luna—GPT-6 Luna—and a configurable agent like Pi—Harness Pi—and say: here are the set of things that you can provide. Roughly give me the configuration of Pi that you would like to use with harmful side effects and extra gimmicry like certain hooks, etc., removed. And there is a class of problems, a subset of which reaches you. You have limited knowledge on what subset of tasks will reach the agent. How well does your harness perform? It does two things: one, you broadly know what to optimize for; you don’t specifically know what to optimize for; therefore, a certain amount of judgment is required about the domain, which you can collaborate with the agent and use that to figure out what the harness configuration needs to be. Very likely a Project 1 question; I just need to test how well this can be evaluated.

**JK**: [34:56] Agreed. I’ll take a cut then. When you see what the question looks like, then that’ll give us a better, clearer expectation of what to know. Yeah, the other is, of course, evals. I mean, let’s do a little more getting into **evals—have students build their own evals would be nice.** I know it is a slightly harder problem and contributing back into the TDS GA repository of how evals work...

**Anand**: [35:31] **How do we evaluate evals?** (Laughs).

**JK**: [35:37] Yeah, I mean, I don’t want it to be another $500!

**Anand**: [35:44] No, no, it may not be that difficult in the sense...

**JK**: [35:48] No, so, I mean, making that deterministic—so I was reading something... was it... so you build something around the harness, the **observability layer around the harness, to make that observability layer more deterministic and use the parameters that are coming from that observability layer to comment on the goodness of eval, so to speak.** I’ll try to get that paper because I was reading on the same thing—how do you make evals better, how do you make it more deterministic—was something that I was also searching around for quite some days now.

**Anand**: [36:40] Of course, this is a question worth exploring. See, one of the questions we are thinking of in TDS is: **how can we teach students to create effective evals or benchmarks?** Now, I’d like you to go through my corpus of work where there have been significant—a reasonably large number of benchmarks of various kinds created. And of course, there’s a huge body of work on benchmarks in the public domain as well as research papers on how benchmarks need to be constructed, etc. But the crux of the question I have is: **how do you evaluate evals in the first place?** Is it that you check if the evals cover enough of a canonical or golden set of criteria? Do you actually run the evals—which can be expensive—and see how well they match the original results? And what are the different techniques that people use to evaluate evals in the first place? Overlay this with the conversations that we’ve had about TDS, how the course is designed, how students work with agents and collaborate, etc., and ideate using the relevant skills—what varied, diverse approaches might be apt? Filter them based on which ones are the most robust, have clear learning, and are a valid test of individual capability as part of this exercise. So, take half an hour and we'll see...

[38:28] (Long pause in recording).

[38:58] Okay, that should cover it. Let's see what comes out of it. But agreed on evals; we anyway have an entire section, module on evals.

**JK**: [39:11] Yeah. Any others? Students, something that you have seen which you think would be relevant for you to better understand? It’s okay if things go above your head while reading or observing. So, if you have seen jargon or terms... Yeah, Preethi.

**Preethi**: [39:40] Sir, actually I’ve been hearing all these agents, "work of agents," and I have not been using any of these agents for my work per se, except for that WebMCP Tangram question which I used ultimately using Claude or something where I had to switch it on and switch it off immediately. But then I hear that we have to **use multiple agents, that too in a containerized environment, so that they don’t go haywire or whatnot.** So, if such a session or something of that sort can be arranged to guide us how to go about doing it.

**Anand**: [40:20] That would probably be for a different session where we’re discussing how to solve; this is more an ideation on what questions to ask. Valid question, just for a different session.

**JK**: [40:32] And I think TAs will be able to have—I mean, in any of the live sessions, I think the TAs and instructors will be able to handle this particular part.

**Anand**: [40:47] Yeah, we'll probably have a session geared towards that just so that students know how to get that set up for themselves.

**JK**: [41:00] Ah, okay. This, I mean, yeah, I should have been talking from my experience: **Agent as a research scientist.** I mean, your research team, right? I mean, because you have math researchers now literally being said, "Don't do math research," and now physics guys are also slowly being asked... getting competition.

**Anand**: [41:24] See, **math is actually ridiculously difficult to frame as a question in TDS.** These optimization ones—once we get a solution, it’s done; personalizing it is hopeless; finding enough problems for everyone to solve is very hard. But I’m thinking physics, and Ritvik was playing around with a few variations on this, but the idea I’m gently going towards is the **mobile as the experimental device.**

[42:09] Here is one idea that is on my to-do list, which is: take your phone, go to a website that we’ll point you to, which will start recording accelerometer, gyroscope, etc., and swing it like a pendulum. And let us say what measurement results we get for the gravitational acceleration of Earth, and it’ll vary within an experimental boundary. All that shows is that it is possible to run a simple Grade 6 physics experiment using the mobile as an instrument. But **what does it take from that point on to go to the next level and do close-to-real-world physics experiments—not to solve unsolved problems, but to actually detect things like, for instance, coefficient of friction does vary based on the actual surface that is used?** And measuring that or measuring specific heat or heat capacity of specific objects is not... it’s not like it’s a solved problem; these are real-life experimental things. But those are tougher to get sensors for with a regular mobile phone. So, a big part of the question therefore is: **what real-life experimental design is enabled by the devices that we have, and how does that inform or enable data science is where I’m thinking.**

**Carlton**: [44:08] There’s another... I don’t know, it sounds like a crazy idea or silly idea, I don't know which one it is, or maybe both. But you know, **maybe we should find problems that have prizes and just solve them using agents and use the group think of TDS.** You know, win a million dollars and TDS might get nominated for the Nobel Prize! (Laughs).

**JK**: [44:37] You will need far larger compute and far larger budgets for that.

**Anand**: [44:44] Possibly, but in a sense, if we simply turned the compute onto the GitHub repos that have bounties, that solves tangible problems. But the question becomes one of, as you have often asked Carlton, **how do we link it to learning?** Multiple people collaborating towards one large exercise, I think it's still worth doing. I’m tempted to make that a bonus mark kind of structure, just evaluation-wise. And **what problem to solve—I’m thinking I wouldn’t go after the large, famous problems, as JK said, that requires too much compute. But there are weird, niche problems that can be solved.** Like, for instance, recently I saw a couple... there is the **Cipher of the Stitch.** Okay, I’m just sending my link to it. I’ll share my screen.

[46:29] Let me see if I can locate the "Cipher of the Stitch" details. Yeah, okay, here it is. So, there was a 15th-16th century book in which a **Thomas Urquhart had put in a series of numbers like this. And what that means has been an unsolved problem until recently when Claude found out that these refer to specific—the first... let’s see... the first word on...** yeah. So, basically, for the first cipher number, you go to the first section and count to that numbered word and take its first letter. So, Section 5, 3rd word; Section 27, 38th word, and so on, apparently, is what this is meant to be. And it reads something like, "O God, uphold King Charles the Second," and so on. It was interesting to see Charles spelled this way, but I recently learned that spelling is something that only got standardized relatively recently over time. Even Shakespeare had various different spellings of his own name, and the whole notion of spelling mistakes was nonexistent; quite the opposite, it’s like, "This is how I spell it" sort of thing. But **smaller problems like these is probably what we might want to solve.**

**Carlton**: [48:23] Yeah, there are a lot of these in, for example, in archaeology or even—I remember like just three or four years ago, right? So, before the rise of GPT, you would have all these like little magazines that have these little crosswords; then there’d be a prize at the end of them. And the thing is, not many people actually apply for the prize. People solve them, but they don’t apply for the prize. So, I knew someone who basically used to solve these, and they would win prizes because they’re in such a small pool of people who actually apply for the prize that they just end up having such a high chance of winning the prize. So, they’ll get like tickets to Paris or, you know, some gift hamper or something like that, right? So, there are like you said these niche problems that people don’t even think about that actually have some real-world value. And you know, **if you find these niche problems—I mean, that’s a great bonus question, right? Someone can say, "I found this problem, I solved this problem," or something like that and, you know, we could give bonus points for that maybe.**

**Anand**: [49:24] Good point. And this itself is featured in some repository of niche crypt... or what is it? Decryption problems. Yeah, just **maybe toss one of those out there and say: whoever wants to pick up whichever one of these cryptographic puzzles—not cryptographic, no, just cipher puzzles—and solve one of these, great; solve one, get a bonus mark.** It’s actually very tempting. Yeah, let’s just do that.

[50:07] Okay, any other items that we should explore for questions?

**JK**: [50:14] How are we going to publish this? The framework for how we give this out as a bonus?

**Anand**: [50:25] Sorry, no, I didn't understand the question.

**JK**: [50:28] So, if we’re going to go ahead and give people this kind of problem as a bonus mark, what’s the framework for it? In other words, how do we go about constructing a measurable outcome so that we can give a bonus mark for it?

**Anand**: [50:49] Here is my current thought process—I have not validated this—but solve one of these, and we will have whatever, **ChatGPT, Claude, or so, verify that you have in fact solved it. And if it does, then you get the bonus mark.** The link that I shared was my verification of Anthropic’s solution. The good part is the verifiability is moderately easy, meaning...

**JK**: [51:21] Yeah, usually is, even for hard problems, the verifiability is usually the easier part.

**Anand**: [51:28] Correct. Yeah, I haven't thought about it beyond that. I’m also assuming that because it’s a bonus mark question and because these are hard, it’s not like we’re going to have 500 submissions; we’ll be lucky if we have five. It’s easy enough to verify.

**JK**: [51:46] Yeah, so there’s a question again from Preethi asking **how many questions are there in Project 1?** My answer would have been whatever Anand said just now. No, we have not thought of it right now, but yeah, definitely we should open a prediction market for it! (Laughs). No, honestly, no idea, absolutely no idea. But you will come to know of it in the next four to five days because we’ll know how many we can release in the next four to five days.

**Anand**: [52:15] You said that, I didn't!

**JK**: [52:18] That’s okay! No, otherwise I would have asked you last week itself how many are we going to release!

**Anand**: [52:27] Just one clarification: so, **we’re going to release GA3, the first question tomorrow. Tomorrow, okay. First few, probably.** Fingers crossed, unless some client says there’s an emergency tomorrow and all that, but barring that sort of thing, tomorrow. Okay, great, thanks. Anyone has any questions? We’ve got about six minutes before we hit our official time. So, if anybody’s got any questions, any students...

**JK**: [53:07] Adwitiya, I thought I responded to your question. Wasn’t that sufficient? Because all our answer would still be the same: you’re not learning concepts, you will come to know of it only towards the end. So, **there is nothing like a correct strategy, wrong strategy; whatever strategy that works for you eventually, and see what you can make out of it.** That’s one part. Ah, that reminds me: I think, yeah, the—we had to talk about that Tangram solving strategy. The solver, right? How did they solve? So, we wanted some... yeah, something on that at some point.

**Anand**: [54:03] Bharat mentioned it was a combination of: A, the **filter endpoint having exposed the answers from various groups. So, that gives one catalog.** Second, **Astra just went through a series of these.** They were sourced from a popular Tangram repository of shapes; that provided another subset. I’m sure I’m missing one more technique, but the two major flaws in the question design were—the biggest one of course is that **the filter endpoint exposes an actual solution, which is otherwise harmless, but in such cases it trivializes the solution.** And that it was a fixed vocabulary of just 100. Both of which are learnings from a question design perspective.

**JK**: [55:04] So, anyone who is solving these questions—the P1 or GA3—we would so love if you could go back to GPT, ask how it solved, and maybe post—not GPT, whatever agent you are using, human agents or other agents—**have a short description of what you did in Discourse.** Think of it as a bonus activity where you are also trying something, right?

**Carlton**: [55:30] Sir, which questions exactly are we referring to?

**JK**: [55:35] Any questions, yeah, any of the harder questions which took more time for you to get answers.

**Carlton**: [55:43] Okay, okay. Sir, so there was one question in GA2, I believe, where we had to, based on the model, we had to get a specific response, the yes/no question. So, I saw that most of the students, they were going into rather complex differences in how the model analyzes some problems or something like that. But **a quick workaround of what I used was that I used one of my AI Pipe tokens to get a simple answer for a question: "Which model are you?"** So, out of that, based on the vocabulary that the model outputted, I could clearly make out that if it’s from the "mini" family, then it says that exact phrase no matter how many times you prompt it: "I am from the mini family." So, the answer which I wrote was simply that if you are from the mini family, then give the answer as "no," and if not, then give the answer as "yes." So, that effectively solved the question.

**Anand**: [56:51] Interesting, I had not thought of that. Thank you, that was a useful—that’s an interesting technique.

**JK**: [57:03] Ah, **please do post it in Discourse also.**

**Carlton**: [57:07] Yeah, yeah, sure sir. I’ll try to format a post by tomorrow and then I’ll post it there.

**JK**: [57:14] Yeah, **use the tags "Graded Assessment" and "Term 3 2026."**

**Carlton**: [57:20] Yeah, sir, done. Definitely.

**Anand**: [57:24] That brings us, I guess, to the end of this. I guess most of the actions are on me, at least for GA3 and P1, but I’ll request based on these principles—Mayank, Jaydeep, Agrim, whoever else is on—sorry, I’m not in the full list—but if you could all take a shot at the **GA4 questions**, that would be really helpful. On a Wednesday when we catch up, it’ll be good if you had a few GA4 questions that we can evaluate.

**Carlton**: [57:57] Anand, just one question before you leave. You had shown us an eval of questions from previous terms. Could you share with us how you did the evaluations of those questions—what you used actually? The difficulty of the questions?

**Anand**: [58:17] Okay, that, let me share the repo screen. In the exam repo, there is a `dumps` folder, and that contains a `download.sh` which will download all of the questions. If you want, I can send you the downloaded results. And there’s a **`difficulty.py` which generates this `difficulty.md` which I periodically update.** So, this is two weeks old, but this file you can just directly use.

**Carlton**: [59:09] So, the **`difficulty.py` uses an agent?**

**Anand**: [59:12] **No, deterministic. Actually, all of this is deterministic; it simply calculates the percentage of students who got it right.**

**Carlton**: [59:17] Oh, okay, okay. I was under the impression you used an agent to evaluate how difficult a question was.

**Anand**: [59:25] An offline post-facto on a one-off basis, but this is simply saying the percentage of students who got it right.

**Carlton**: [59:33] Oh, okay, okay. Understood. Aligned.

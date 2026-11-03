# Transcript

**Jaideep**: [00:00] Hello, Anand.

**Anand**: [00:02] Hey, Jaideep. How are you?

**Jaideep**: [00:04] Good, good.

**Anand**: [00:09] I know Carlton and JK are not going to be here, so I think it'll just be short.

**Jaideep**: [00:16] Surprisingly, attendance is very low.

**Anand**: [00:20] Yes. People are busy or happy for Diwali, whatever. Good for them. We'll just get started. First one, sorry I'm getting a little late. I didn't know did you want to discuss the next GA offline, or do you want to discuss now? Either way is okay.

**Jaideep**: [00:40] I mean, it's fine. We can discuss the GA, but we want to do it in a way, so I mean, we don't want to, obviously, show the private repo. Or, of course, it's your choice, but then—

**Anand**: [00:54] No, I leave it to you. So then, let's do this. We'll do it offline, but I just want to flag off that I have a few questions that I wanted to introduce in GA4, not because they're partly capability questions for the platform itself to see if we can do a few things, and partly just a few follow-up kinds of things. And I wanted to introduce One of the things that I'm curious about, for instance, is does it help to have Okay, there's some background noise at your end. No, no, that's okay. Like, for instance, should we ask students what would they prefer, option A versus option B in the ROE, stuff like that? I mean, basically, it's between the devil and the deep blue sea. But if, at least, students choose A, I get input, and B, we can also steer the course in a certain direction. So, that sort of a question I will probably want to add. So, I'm thinking I will create the scaffolding for at least one or two questions, which you can then probably add on to.

**Jaideep**: [02:19] Yes. One more thing with regards to the questions, I think it's, at this point, getting too hard to make them Astra-proof or Opus-proof.

**Anand**: [02:30] Yeah, right? Yeah, what are your thoughts? How do we teach when the agent can solve the problem? What? Yeah, Jaideep.

**Jaideep**: [02:38] Yeah, I mean, I think it's a problem not for us, I mean, even people above our grade, like who are building state-of-the-art stuff, they're also running out of stuff.

**Anand**: [02:51] I agree with 90% of your comment. The only thing I probably disagree with is above our grade, because you are building state-of-the-art stuff. There aren't many people who are doing this stuff that's beyond it.

**Jaideep**: [03:04] I mean, let's say Andrej Karpathy.

**Anand**: [03:07] Ha, yeah. So like, the few, few hundred at most, like that.

**Jaideep**: [03:13] Yeah. I mean, I don't know when Simon Willison last time hand-coded stuff.

**Anand**: [03:19] Exactly, right. And Patrick Collison of Stripe, he tweeted recently saying he's thinking of liquid software. That is, a little button in the software where if you give feedback, the software rewrites itself, creates their own tweaked version, which potentially others can fork.

**Jaideep**: [03:40] So, have you taken a look at Omarchy, a Linux distribution by DHH, the creator of Ruby on Rails? So, their idea is they have built a, I mean, it's something like a polished desktop environment for Linux, and then they're integrating agents so hardly to the point they're saying, "If you find a bug in our operating system, go and ask Claude. It will rebuild it."

**Anand**: [04:05] Love it. Okay, it's What did you say was the reference?

**Jaideep**: [04:10] DHH.

**Adwitiya**: [04:12] Sir, it's called Yeah, Sir, DHH, the creator of Ruby on Rails, the same guy. He's created a Linux distribution. It's not technically a distribution. It's just a bunch of, you know, customization scripts on top of Arch. But, yeah, he calls it Omarchy, so the spelling is O-M-A-R-C-H-Y.

**Anand**: [04:33] Ah, okay. Okay.

**Adwitiya**: [04:37] Yeah. So, initially he marketed it as an opinionated opinionated project, but now ever since he has got funding from SpaceX and Grok and all stuff like that, so now he is marketing it as an agentic OS.

**Anand**: [04:52] Interesting.

**Adwitiya**: [04:53] So, at the time of startup, you get to choose your agent, and it's more like you're interacting with your computer not in a traditional sense, but it's as if you're speaking to the machine. So, that's the basic idea behind it.

**Anand**: [05:06] Cool. I have to check this out. Thanks, Adwitiya. Can you take me through it for a while? Okay, what's your experience with it?

**Adwitiya**: [05:15] Sir, I I It's It's, of course, it's an interesting project, but from the security side, there are certain flaws because when once you give like an agent, there are Either you are very precise in what you type and what you want the agent to do, but otherwise it the agent has full system access, okay? So, if it messes up something, then it gets a little tricky to debug it or to get it to revert it to the same state as before. Of course, you can create system snapshots, but we are not considering external software for now. And on top of that, it is built on top of Arch, like I said. So, it's not a a distribution in the traditional sense, right? Right, it's more of a customization aspect of it. So, that brings along with it the drawbacks of Arch Linux, such as the AUR not being traditionally vetted as in Fedora and Ubuntu. And, you know, the packages and all, they are they're still coming from AUR and repos like this, which are traditionally a little less secure than, you know, more mainstream distros.

**Anand**: [06:24] Got you. Interesting. Let me check that out. Cool. Before we move on to other topics, I thought one thing that I'll mention is In GA4, are there AI Pipe-related questions? Okay. We need to draw But okay, I think we need Jerry for this particular point. I will come back to it. Because, among other things, it will mess up a few of the existing questions that people have. Who else do we have amongst the TAs? Just checking. Okay. None of the TAs are Uh, yeah. Agrim is there. Hey, Agrim. So, it's just going to be you and me.

**Agrim**: [07:25] Hello, hello, hello. Good evening, Anand.

**Anand**: [07:28] Good evening.

**Agrim**: [07:30] Yeah, I don't think we have an AI Pipe question in GA4 currently.

**Anand**: [07:34] Okay. I will be introducing one, and yeah, if you could introduce a few as well, that'll be good, because among other things, it will be interesting to see the impact of that on project one, question one, which was about predicting the AI Pipe token usage.

**Agrim**: [07:55] Hmm. Okay.

**Anand**: [07:57] Among other things, one of the things I'm going to do now is increase the limit, and you should probably let people know. Let me share my screen and do this. So, the IITM limit is $1 over any 7-day period. I'll make it at least $2 over the 7-day period, and apply this. So, I'll revert it later, of course, after a few weeks. But what this means, and again this is note to you, please let everyone know that, **as a result, project one's forecast, most people would want to revise.**

**Agrim**: [08:57] Revise, yeah.

**Anand**: [08:58] Revise. They're not in a position to use the new information that they'll have. Okay. That was the one thing. A couple of things that I wanted to share there. Increasingly, the time that it takes for features and capabilities to change is so high. As a result, obviously, we're also changing the course fairly rapidly, and we're using agents for a significant chunk of it. It helps to get a sense of Let's do this. I think the exam repo needs an agents.md of sorts. Don't even call it an agents.md, but more like a guidebook. And I took a shot at having ChatGPT craft that based on all of our transcripts, as well as emails, course material, et cetera. And here are the principles I'm thinking of. What I wanted to do was, along with you, go through those. Is my screen visible?

**Agrim**: [10:23] Uh, yes.

**Anand**: [10:24] Okay. So, right here, as you can see, this is the context that we want to share: agents. And let's iterate on it. I've made a few edits here and there. But **one is course philosophy. Why do we think TDS is different? Why do we think, why we are designing TDS this is a non-traditional course is probably better realigned here.** So, one is Agents **If it is teachable, agents will learn it. So, there is literally no point teaching what is teachable.** It's a weird way of putting it, but that's where we are. And if that is the case, and I think Jaideep, this reflects what you were also saying earlier. What do we teach? The answer is perhaps, what is it that humans need that agents won't learn soon? That's perhaps a core principle. In other words, if an agent can do it, let the bloody agent do that. And one of the things that that has triggered on is making sure that we are able to complete the tasks. Agents are good as a tool on intelligence, and by providing them additional tools, other agents, people as capabilities, we can drive them to get the job done, or you get the job done, and verify it. But that's ultimately what human accountability will matter. Use whatever tools, and get it done. That's part of the principle. Exams are the curriculum is a well-established principle for us, and the fact that content pages are optional is secondary thing. Speaking of which, Mayank is on?

**Agrim**: [12:33] Uh, no. Mayank is not here.

**Anand**: [12:34] Okay. So, one of the things I wanted to flag off, and Agrim, Jaideep, okay, Krishna is on. One thing that I want to flag off is as part of the TA sessions, et cetera, we may be teaching things that an agent can teach. I happened to be in I think yesterday's workshop very briefly, and Mayank was sharing how to create valid JSON. There must have been a reason for it, but I was thinking, hold on, why should we teach that? Instead, what I would do is have an agent create an explainer so that students will: A, learn how they can create their own explainers for the topic; and B, that can be published in any case for anyone else to refer, therefore automatically creating reusability, reusable by humans and agents. But, Jaideep, Agrim, are you conducting any classes for students?

**Agrim**: [13:56] Uh, I don't think I have conducted. I think Jaideep has take one session. I took one session, but that was only a doubt session. Yeah.

**Anand**: [14:02] Got you.

**Jaideep**: [14:04] Yeah, I took one session where mostly, I mean, I was going through WebMCP where I mean, it's at the end of the session, it's just me using Codex and explaining students how to use Codex to build stuff. And

**Anand**: [14:26] Which I think is fair, and the challenging target, whatever that I would place in front of all of you is **how can we make ourselves redundant in the TA sessions? Meaning, what would it take for agents to be able to fulfill the need of the TA sessions in the first place?** So, and then if that becomes possible, then, yeah. Go ahead, Jaideep, go on.

**Jaideep**: [15:04] Yeah, but the way I conducted the session, one point might be helpful where I have deliberately chosen myself to not look at WebMCP at all costs before the session. So, each and every resource that is found is ad hoc. So, what it actually helped me was, assuming I'm at the Of course, we're all we're all the same level to that concept, so how will we approach it? Having these agents, how will we actually take on things? So, we don't end up in information poverty, so just tossing every, just tossing everything, or even micromanaging things to the point where it's better to do it by yourself. So, how to find that balance, and how we approach things?

**Anand**: [15:53] Good point. Completely agree, and what I'm taking away therefore is under preparation is an advantage in such sessions, because you're transferring the broader skill, which is how do you deal with such a question. Agreed. Who all of us are okay with that. Adwitiya has commented, saying, "Prompt guides per session." What do you have in mind, Adwitiya?

**Adwitiya**: [16:16] Sir, like you were looking for a way so that we can, basically, more efficiently cover a larger information pool in the TA sessions, right? So, for that, what we can do is, like, in my case, just hunting through a 2-hour video for just a 20-minute segment, that wastes a lot of time as compared to, you know, just having a prompt handy and asking the LLM or agent to, you know, explain a concept to you. So, if we can create If one of the TAs, whoever is taking the session, if they have a specific topic in mind, they can just craft out maximum of four or five points uh prompts, sorry, and then provide those to the students. So that if you're interested in seeing the execution, the live learning part of it, you can watch the video. But if you do want to explore the content on your own or, you know, have a guided learning sort of experience via an LLM, you can just utilize those prompts and chat with an LLM like ChatGPT or something, and you'll essentially be grasping the same concepts.

**Anand**: [17:16] It's a good point. I agree with the principle, probably tweak the execution. So, firstly, it is good that TAs come in underprepared. That way, the prompts will naturally emerge. It's useful that people then can understand the session through a set of prompts that were used, or jump to the right portion. However, I think there are two kinds of audiences: one that would benefit from the answer, but two, and I suspect this may be a majority, who would benefit from the process. That is, the reason they are there in that session is because it hasn't yet struck enough people that you can get the answer just by prompting. If they knew that, they wouldn't attend the session in the first place. They'd just be sitting and prompting. So, the session is meant to transfer that somewhat less tangible skill, seeing somebody doing it saying, "Oh, okay. It really is possible." The second, other part of it though, abstracting out content from the TA sessions is a useful thing. And I don't think it should be the TAs that do this. I think it should be the students that do this. For instance, Adwitiya, if you said, "Here's an agent that Uh, let's take it simpler. Here's a prompt that from these YouTube videos will extract all the prompts, share it in our forum, say Discourse, and let people know." Great. Somebody else says, "Oh, I've already done this, and here's a site where anyone can just get a sense of all the prompts." That is great. One of the things that I do, let me share my screen. This could be useful for anyone who wants to. We used to do this for the TA sessions, but stopped. But my talks page, which is effectively, yeah, putting the link here. It takes the transcripts or videos, et cetera, and then converts it into a session where we can go through what was covered, including jumping to a specific point. And the past two weeks ago the meeting that we had is exactly what this is. The process is reasonably straightforward. I would rather people not even just discover it, but implement it themselves. The reason I'm suggesting that is we will have more variety and learn what can be done from that. Coming back to And of course, at any point, if anyone has any thoughts, suggestions Yeah, Jaideep.

**Jaideep**: [20:19] I don't think even prompts would help, because increasingly they are becoming to the point where each and every agent, whatever the user is using, is becoming too much personalized in the sense. So, there is a huge bias in the way they prompt and how they interact with LLMs, with the context they build up over time. So, I think we need to abstract even the prompts away and find something different.

**Anand**: [20:47] Agreed, and yeah, that is definitely coming back to the how do we teach what can't be taught kind of a premise. Yeah, Adwitiya.

**Adwitiya**: [20:56] Sir, if we are, you know, looking for an interesting tangent to this conversation, we could say, would be that these days, one thing that I've noticed is that **the more advanced the model gets, as compared to telling it what you want or or how it needs to be done, you need to tell it where to stop.** Such as, if I'm using Opus 5.5, what I've noticed is that it's programmed to give you the absolutely correct answer. So, that sounds like a good idea at first. But if you're interacting with it in a manner that's limited, you have session limits, you have weekly limits, and all of that, then what's not good is that if you've go if you've given it a complex prompt, then it'll go in into quite a comprehensive loop of self-testing before it provides you the answer. So, you do need to specify what the limits of your like what are you expecting, and where it does not need to test. For example, if I just tell it to write a just for an example, a plug-in for a text editor. So, for that, I already have the environment set up, so I won't really prefer to burn my tokens on a test. I would prefer to burn it in debugging rather than testing. So, that's just something that we could explore in a question or two.

**Anand**: [22:09] Good point. How would you frame that question?

**Adwitiya**: [22:11] Sir, I would One of the ideas was to use AI Pipe. So, since I have seen in the previous GAs as well that you are able to analyze the output that we obtain, essentially intercept it. So, in that case, you can also, you know, time the responses. Or if not time, you can get an idea from the language whether or not the LLM has tested something extra other than what we told it to. Like, for example, if we are writing a script that should check the that is not expected to fail on Python 3, for example, then it shouldn't just go on checking for some other irrelevant tests as well. So, if you could just intercept the response that you get, you will get an idea.

**Anand**: [22:58] Got you, but see, here is how a student would and is expected to solve the problem. They will point it at the GA, or they will take ChatGPT, Claude, whatever, point it at the GA page and say, "You solve it." And the agent will look at instructions. Instructions say, "Make sure that you tell AI Pipe to stop." The student will craft a prompt that will tell AI Pipe to stop. Good evening.

**Adwitiya**: [23:26] Yeah, sir, but in that sense, at least this would inculcate that feeling of Like, right now It wouldn't inculcate a sense of

**Anand**: [23:34] The student won't even read the question. Not won't even, should not even, if it's framed this way.

**Adwitiya**: [23:40] Yeah, right.

**Anand**: [23:42] And and and that's not a bad thing, because if an agent can read it and solve it, that particular thing is not what we want to teach. So, let's take it a little further. We want students to learn how to specify in a way that they conserve tokens, okay? Why? Because that's a problem today. But if I tell ChatGPT, "Create a prompt to do that," it'll probably do a good job. So, do I still need to teach? It's question number one. Question number two is, it may be for some reason, I still need to teach. If so, how do we teach it so that even when it goes to ChatGPT, it is not solvable? Think about it for a few minutes. You'll get a sense of the question design problem that we face on a daily basis. And let me open this up. Therefore, for subsequent GAs, ROEs, and projects, it's an open invitation to everyone. Please share ideas. Whatever form, Discourse is fine, email

---

**Anand**: [24:59] Email is fine, just make sure that all the TAs are copied. Ideas for questions that we can include that will still teach if that question is literally copy-pasted into ChatGPT or Claude, or whatever. And if it still teaches something that is useful, should absolutely add. So this is basically an open invitation opportunity, whatever, to everyone. You can decide your questions, add each other's questions. We certainly will look sort of desperate for more such questions. So please think about it, and we can iterate and discuss. Keep in mind that this particular skill of crafting a skill that will still teach when an agent can solve it is also one of the skills that you want to learn because it has bonus learning if you.

And let me share my screen. I'll go back to the guidebook. That relates very much to the point where we can teach people to delegate as much as possible. And yeah, these are the four things that I still think have solid value: judgment in some anyway shape or form; risk management, in the sense, we don't even know what all ways in which an agent can go wrong, and we still have to make sure that we drive towards getting the job done, how do we know why it's failed and where it's failed; and finally, taking accountability, it doesn't matter whether the agent goofed up or not, I am accountable, that's what stays valuable.

Therefore, it may be spotting something that we don't even state. And implementing not just what is written, but what is intended, this is the remaining human skill. So, if a question had something vague along the lines of, a CIO wants a dashboard with this data. For an agent to say this is what a CIO wants is one thing. But for a human to say, okay, look, in that case, I will tell ChatGPT to do the analysis because it does it better, and tell Claude to create the design because it doesn't say it better, is the kind of thing that will lead to a better dashboard. And that breakup is something that is essential. Better yet, going beyond and telling ChatGPT, look, the CIO will not have time to read the massive amount of analysis that you have done, and telling Claude that guy will almost certainly want to read it on the mobile device, you've optimized for desktop, is the kind of unstated requirement that judgment will bring in.

And yeah, we now have to start teaching people this because earlier you would say, "Oh, no, that requires a lot of experience to get there." When the company is saying, "Boss, if you don't have that experience, I won't hire you." Literally, in the room of of my classmates who was shocked to saying, "Who are you going to hire, and why did you hire?" And said, "Well, boss, like I just don't need you to be able to do anything. I need people who have judgment. So I can only hire senior people." So which means, you will get hired only if you build that experience, and you build that experience by using agents to build up that experience, having it interrogate. So if, in a course like this, we guide people to solve problems which normally would require a lot of experience, forcing them in this environment to pick up that skill using the tool, which is the agent.

Let's skip some of these. Okay, maybe not this one. The sourcing of context, context is the tough part. And therefore, finding, getting that, whether it's from people or systems, whether you connect to new systems to get the data, whether it's connecting to people, that's what's going to start mattering. And seeing if we can spot the errors in the AI is also partly the failure diagnosis, partly the risk management stuff. And finally, if you want to learn something by yourself, then before you tell, ask the agent, you guess, see if the agent disagrees, agrees, and use that to build your judgment. Those are the core principles, but a question to everyone: Are there any principles that you think are wrong, missing? What would you add, delete, change?

I'll publish this along with a bunch of other stuff and invite comments. Docs Okay. Let's see. Docs, okay. Docs/guidebook.md. Make this prominently linked from the home page. Just a test. It's too small, don't worry about it.

And I'll invite comments. So on Wednesday, when we catch up, instructors and TAs, maybe we can have a chat about what we need to incorporate with the guidebook. The intent of the guidebook is so that when you have agents create the questions, they refer to this, and therefore, if in the process of creating questions you have found some prompts that you've had to give on a regular basis, this is the place to be. It will soon become an agents.md for the exam prep. Any questions?

Yeah, Adwitiya.

**Adwitiya**: [33:35] Sir, I was just thinking about what the discussion that we had about the question, how would I put it technically? So, something that came to my mind was, of course, it's not a very ethical thing to do, but as long as teaching is involved. So, in the the GA interface, you have an option to choose the AI, right? Which AI we want to choose. At the bottom of that, it says an option of "Copy to clipboard." So, if I click that button, the content will get copied to my clipboard. So, we could modify it in a way, if we if you wish to force the students to actually read the questions, you could modify it such that the stream is interrupted and edited before it lands up in our clipboard. So, what I mean is, if we go ahead and read

**Anand**: [34:25] Yeah, Mayank already did that in one of the ROEs. I mean, last ROE, I think. And yeah, he had done

**Adwitiya**: [34:31] Okay. Okay. And one one more thing. So sir, what we as a humans, we know that certain phrases, they are quite natural to us, make sure that your answer is correct. So, we'll check it twice at most, right? Not a big problem. But if it is a complicated problem that involves, you know, floating point decimals, for example, like 2.4999 multiple times, and I ask an AI to make sure that the answer is correct, and if it is a complex model, it will definitely, you know, burn through a quite a significant number of percentage of tokens before it tells me, yes, that I'm fairly confident this answer is correct. That's because they are being trained to make sure that what the output you give is perfectly fine. And secondly, when I would read the question, I won't even think that this is the line that's causing the problem. The the same goes for a case when, you know, there are multiple correct options in a wide range of options, and you're just asking for one. So

**Anand**: [35:32] That's promising. It is not agent-proof in that, what say Astra will do is run a whole series of prompts and see which one will still solve the problem. But it is potentially a good ROE question because it just might be too long for Astra to solve if you can find a way of personalizing that question in a way that is non-parameterized. What do I mean? Each student gets a different question. B, the questions differences are not just in changing a number, or a phrase, or something, so that if that were possible, what I would do is have somebody create a solver for it and share with everyone. That solver will have done the full analysis, spent the first 30 minutes of the ROE getting to the result, and then tell people, "Here is the prompt. Replace Copy-paste this number and this text and blah, blah, blah from your question, put it in here. That is your answer." And it will, typically, it would win.

I am very happy with the fact that people would have delegated, also very happy with the fact that one person would have used an agent effectively to solve the problem. What I would like is for more people to have to use their agents in a clever way to get to that same result. And therefore, if you could design this question, which I see has promise, in a way that would still teach a larger number of people, not 100%, 10% curve of people learning this is good, but it has to be 10%, not 1%. That will be powerful. Do think about it.

**Adwitiya**: [37:30] Yes, sir. Okay. Definitely.

**Anand**: [37:33] Let me share the screen for a few more things. I was just playing around with the results of GA3 Q5, the bonus mark question, partly to see if we can watch. Yeah. VS Code has a dictation feature, which is pretty decent, actually. It's somewhat code-friendly.

So, I was just looking at what are the questions that people are making drawings that are hard for AI to guess. So this one, AI totally failed to guess, but all students, humans guessed it right: donkey. Luna thought it was a sheep or a cow. GLM thought it was a fox or a sheep, etc. It's a pretty decent guess. So, yeah, plus five. We should give whatever marks. We have to figure out the scoring for it.

This was surprisingly a ladder drawn this way ended up fooling most of the models. The other technique was a ladybird. It didn't fool GLM all the time, but lady and bird is a clever combination where you're able to differentiate what you communicate to a human versus to an agent.

And this, yeah, I don't know why they wouldn't think it was a pressure cooker and we consistently think of it as pressure cooker, but it may be just linguistic. And this one, most models thought was a shuttlecock or a whistle, whereas it's, according to us, mostly a medal. And these are all based on the same set of options that was given to the models. Of course, randomized in different ways, but options are more or less the same.

And yeah, mango versus pear, not sure. But one of the things, and I'm guessing at least in a few of these cases is, people are getting an intuition for how to draw something that, and that can differentiate between a human and an agent. But in terms of the percentage difference, it's relatively weak. The total number of people that could get something that a human could answer that agents couldn't, let me see if I have the stats for that. Yeah. So we were looking for something where the humans are always right and the agents are always wrong, and only eight could do that.

Overall, metrics are not too bad, that it's 812 where at least the the AI was only partly right, while the humans were perfectly correct, or humans were partly right and the AI was still wrong. It's okay. It's slightly better fraction, but obviously, the AI capabilities are going to keep going up. And learning different ways of identifying model gaps is something that I think we would like to probe. So, as part of GA5 and 6, can request to the TAs, as you are crafting this, please incorporate more mechanisms by which we can get AI to fail while humans cannot. We have the infrastructure to allow humans to test. So that would be pretty useful.

Any questions or comments on that?

Okay. Moving on, another thing, I'll share this link with everyone. So, what I did was cataloged about 10,000, 12,000 prompts that I've given coding agents, as well as non-coding agents: ChatGPT, Claude, etc., to extract the different techniques that at least I have been using for specifying requirements and verifying output, which are the two broad agent-era capabilities that people need. And if we look at what at least for me would rank as number one is, can we have it run the output? Effectively, giving it an environment in which we can run the test cases and see if it can be deterministically validated. The environment could be a coding agent, it could be a chess-playing agent, it could be a physical laboratory, it could be an API, whatever. But I think now we are at the stage where going beyond coding agents is important, that the verification environment starts becoming broader, and a little bit open to interpretation. But therefore, for GAs and more particularly project, I would invite questions, mostly from the TAs, but from anyone in general, what kinds of environment engines can be tested? Now, part of this is being incorporated in Project 1, and I think GA3 as well.

Let me see. In GA3, we might have had It was a Meshy question in GA3, which is technically not Meshy, it's just, yeah, deconstructing a a famous face, and a lot of people have converged to the Meshy plus ChatGPT or Claude workflow as being reasonably good. Yes, that's not a bad solution. However, it hasn't yet taken people to, is there a verifiable environment that an agent can manipulate, a 3D model builder where it can iterate, improve, etc., with vision capability? And that's kind of the next nudge that we would want to go towards. The morphing question is similar, and nobody has very few submissions have any kind of decent morphing. Most are simply doing an animated transition between these, that's rubbish. What I want is the face to really, I mean, any frame in between should look like a real person's face, and a real photo. That is good morphing. And very few people have gotten that far. And again, is there an environment where we can do systematic morphing, and FFmpeg just does not do that, that we can plug into an agent? So even just finding the existence of some of these verifiable environments becomes a useful teaching skill.

Another one is, how do we make sure that you stage something that is irreversible? Can we have a situation where students are forced to decide whether something is reversible, irreversible across a series of decisions? And use that to decide whether they want to spend, as Adwitiya had said, more tokens where it is irreversible, less tokens where it is reversible. In a way that even if they gave the problem to ChatGPT, or Grok, or whatever, it would not be able to, in a generalized way, solve the problem without spending a hell of a lot of tokens. One way of doing it is to tell them, look, here what you You can only give a prompt with instructions. Give the right instructions, that will be executed by another agent. Yes. Codex will figure out a good prompt for that even better, not sure how to design it. But this, knowing what's reversible, what's irreversible, is something that you will have to factor. This could possibly be a good end term question, and therefore, if you're going to be designing the end term questions, this is a classic set of tests saying out of these 10 things, which ones of these would you commit and deploy, or tell the agent to commit and deploy? Which ones of these would you have it just test and you verify, for example?

A third one is, how do we verify the verifier itself? In a number of cases, I've had situations where the test cases were wrong, where the judge prompt was wrong, etc. And validating that becomes useful skill. I'm not going to go through the full list. I just want to say that this is the order of impact, frequency, and effectiveness of techniques that I've been using. It's at least a starting point, and I would suggest we create questions using these for verification as well as for specification.

Any comments or questions from anyone?

Okay. That actually covers the bulk of what I wanted to go over. Just going to quickly check to see if I've missed anything.

I think that covers it. So, primarily, an open request to everyone to share agent-proof questions. We will incorporate that.

Karthik's question as well. Questions from GA3 around these partly, Karthik. The idea for many of these is, given the skills we know are relevant in the agentic era, which of these are relevant? But, the intent behind some of the GA3 questions was trickier than that. Let me share my screen.

Let's see. This is GA3, right? Let's open GA3. Let me go from the bottom.

Which faces are easiest to morph is entirely based on the premise that, look, there is one thing you will find really useful in the future, which is predicting another human's behavior. So here, the point is not what you think is the ranking, can you figure out if your ranking will match with your classmates' ranking? Now there are two ways of solving this. One, you have and build really good intuition, which will teach you the psychology of people, absolutely the most important tool in data science. Or,

---

**Anand**: [49:59] Or it will teach you collaboration, which is you somehow figure out a mechanism by which you and all the classmates rank in the same way, cheat, if you will. But that still teaches you collaboration, which, yeah, okay. I changed my mind. That may be even more important than understanding the psychology. That was the intent behind question eight.

Question seven is to teach you what morphing algorithms exist and figuring out a really good one, obviously, collaboratively. And sadly, very few people have picked up on the right algorithms to do good morphing. There are some fantastic algorithms out there that are extremely easy to use, with the right kind of research. This is a classic solver kind of a problem. Meaning, prompt kind of a problem, where all people have to do is give one prompt to an agent, and it will solve it. Luna will solve it with 10,000 tokens at most.

This, again, people are solving it with Meshy, which is not a bad solution, could be improved on. But again, is aimed at finding a good, verifiable environment.

The humans-only question was similar to the last one: is it possible for you to guess, to create something that aligns with human judgment and misaligns with agent judgment? This would have been tough even with a solver, so necessarily learning. I had to convert it to a bonus mark question because the dates were too tight and a lot of people didn't see it, but it was also an opportunity to teach a very different thing altogether, which is, in life, anything changes at any point. **An agent can sit and watch any change randomly. So you're in TDS now, I'm making this announcement, the instructors and TAs are making their announcement, that stuff will change. So build your agents collaboratively or individually to watch for changes.** At the end, tell your agents, "Look, go watch on the TDS sites, solve the questions, and submit on my behalf if you can." In a reversible or, yeah, preferably in a reversible way. Which brings us to why these checks are there. 10 out of 10 checks is very liberal, but if your agent happily goes checking, checking, checking, at some point, it becomes irreversible. And that's where you need to have exercised the discretion to your agent saying, "Look, every day check, but if there are only a limited number of checks, leave some for my judgment at the end because you might mess up."

So yeah, in a sense, to your question, Karthik, what we discussed today are the kinds of things that we are trying to teach. And did you waste tokens? Yes, absolutely. As much as possible, burn it like crazy and learn from getting your fingers burnt. Best way to learn.

Any questions from anyone?

**Kartikkumar**: [53:20] Sir, I don't know, I joined a bit late, so I don't know whether this is the right forum to ask as well. The PA, in PA, right, there were a couple of questions where there were issues and we submitted those issues, but they were not resolved. And I'm a bit worried whether we lost marks on those or not.

**Anand**: [53:39] Depending on the issue, what what issues?

**Kartikkumar**: [53:42] So, for the the the one where we had to trade those services, right, the deadline was extended. But even though a lot of us had recorded our services, it never showed up on the marketplace.

**Anand**: [53:53] Correct. It will show up after the deadline.

**Kartikkumar**: [53:58] But then how would we trade if it doesn't? Because I think the deadline for that person, somebody to buy it is already crossed, if I'm not wrong.

**Anand**: [54:06] Correct. There will be a round two.

**Kartikkumar**: [54:08] Okay. Okay.

**Anand**: [54:09] Yeah. There is no possibility of changing dates in the way the platform is structured without redoing the entire thing. So round two is meant exactly for that. So yes, this is part of the design, and fix for that is, yes, there will be a round two.

**Kartikkumar**: [54:24] Okay. Okay, thank you, sir.

**Anand**: [54:25] And round two will have slightly different rules. I'm still trying to figure out what the rules are. See, right now, the primary exchange mechanism was people saying, "I'm going to get marks for exchanging stuff. So somebody offer a service, I don't care what the service is. Let's exchange and therefore get marks," which is perfectly fine. But what does it take to create an economy that actually does useful stuff? And I am trying to design round two so that the service actually produces something useful for someone.

**Kartikkumar**: [55:00] Got it. There was another issue that I ran into, which was related to the pictures. You had to draw something and the AI had to recognize it, right? And then somebody else had to rank it, saying that, you know, which ones are good. I think this is for the PA, question seven, picture stories?

**Anand**: [55:20] Yeah.

**Kartikkumar**: [55:21] Yeah. So, the competition for that has ended, but we are not able to paste the final token. I mean, it still says the result is not final yet.

**Anand**: [55:30] Yes, yes. It isn't. I have to do the AI evaluation and people have to do the human part of the evaluation. Yes.

**Kartikkumar**: [55:40] And we were expected to hand-draw it, right? Like draw it hand or like not generate the pictures from AI?

**Anand**: [55:47] I don't think I had enforced that restriction.

**Kartikkumar**: [55:52] Okay.

**Anand**: [55:53] Let's see.

**Kartikkumar**: [55:54] It says, "Write your story privately, ideally three lines, a situation, and upload one." Yeah, "Draw it, photograph a drawing on a paper, make a collage, and or use an AI tool." Okay. Because when I evaluated, most of the people had used AI tools, so.

**Anand**: [56:08] Perfectly fine with that, actually. The point is, can you craft a good story that meets these criteria? Broadly, paper and pen versus

**Kartikkumar**: [56:20] Yeah, it is easier to do it in an AI tool. It's much more challenging if you draw it. I mean, I drew it. So, but then I saw a lot of people had actually created it using AI, which is sort of easier to do.

**Anand**: [56:33] Yeah, I didn't differentiate. The method of drawing, I didn't, in this particular case, happen to, I didn't care about it. But this is something to think about. Let me think about whether No, I don't think drawing is a skill that I want to teach in TDS, at least. A useful skill, but drawing a picture story in itself, I would prioritize in this course. But I will think if there are specific reasons why drawing becomes, hand drawing becomes important. Yeah, Jaideep.

**Jaideep**: [57:10] I mean, can we monitor the number of keystrokes, sorry, the hand strokes that are being used for drawing? And then we can evaluate how good the agent is. Let the agents draw with the least amount of keystrokes possible.

**Anand**: [57:29] That's an optimizable Yeah. That I mean, how well they can direct their agents. Ah, but, but there is the thing: it is more agent intelligence. Given the question and the optimization criteria, the agent will converge to a solution, and not entirely sure that will require human steering. But again, if you can craft a question that requires that, let's take a look.

**Jaideep**: [57:56] Yeah, maybe we can do an internal eval of that, and then decide whether it's worth putting out.

**Anand**: [58:04] Okay. We have time for one last question if anyone has. Yeah, Adwitiya.

**Adwitiya**: [58:11] Okay, sir. So not a question, just a suggestion once again on the same topic that we were discussing. So, as long as the context is an ROE and not a traditional GA, so the idea becomes to teach something and also to, I mean, it's rather a crude way of putting it, but to get us to waste time. So that, yeah, so that we are stuck on one question whereas we could be scoring on another one. So that teaches how to, teaches us how to prioritize, right?

**Anand**: [58:37] Correct.

**Adwitiya**: [58:39] Correct. So in this case, what we could do is draft a question that has an external file attached to it. For example, there was one question, I'm just forgetting the GA, but actually, there were two, three questions where we had a separate file type, a JSON or something, which we had to download and paste it along with the prompt to an agent. Now, I doubt whether even 1% of us would have, you know, actually opened the file and checked what the JSON looked like or what the contents were, because just downloading it and pasting it becomes more of a convenience, right? So now what what if what we do is

**Anand**: [59:15] Agreed. Carry on. Sorry to interrupt, Adwitiya, but I align with the theme of your question, and yes, this is the kind of question that makes it somewhat agent-proof. It is, however, susceptible to collaboration. One student gets it and puts it on a WhatsApp group and says, "Guys, add this prompt, telling it, don't try too hard on question nine." It becomes, yeah, less of a hurdle. Now, having said that, too, it is possible to revise this in a way where even with that, some amount of discretion is required, if buried within it somewhere in a slightly hard-for-an-agent-to-see fashion, there is a there is a data set, or if the information were hidden in a strange, let's say, an audio encoding.

**Adwitiya**: [60:13] But, sir, we don't have to hide the information. That was my See, these days, white text and all is completely like AI is at an advanced stage that simply changing the color of the text won't actually serve the purpose anymore.

**Anand**: [60:26] True, but what if it was not text?

**Adwitiya**: [60:29] Okay, sir.

**Anand**: [60:30] What if it's in video?

**Adwitiya**: [60:33] That is a great idea, but I was thinking along the lines of that even in human cases, if we interrupt the stream of work and change a step that was carried on in the earlier tasks. What I mean is, let me say that there's a very complex problem. At the start of the statement, I tell an AI, in the PDF or the attached file is the part of the problem, okay? So in the file, at the start, we tell it, "x = 10, y = 5," and then you perform these steps. There's a complex calculation and all of that. But at the end, we go edit one, "x was = 5.5." So that would take a longer time, because it'll have to recalculate everything. And on top of that, a student who actually reads the question would just modify the prompt and get an answer in less time.

**Anand**: [61:16] Good idea. What you're saying is edits are tougher for the AI. That is a good premise. I will take that in. Okay, sorry, I need to drop, but I will take that in. Thank you, folks.

# Transcript

**Host**: [00:00] Introducing Anand. In first PyEdu conference, I met him over there. He's been a regular speaker, also, and Anand is a LLM psychologist at Straive. He is a chief of AI officer at Straive. He co-founded Gramener, a data science company in 2023, and he teaches courses in data science and IIT. He's also come from IIT Madras. He's been IBM, Infosys, Lehman Brothers, and BCG. But the most interesting thing when I read about him is that he's addicted to Minecraft and anime, so I guess no other geek can compare with him. He's going to talk about verifiable, very- verifiable AI. When AI writes the code, who checks the AI? Right. So I guess, when they talk- when I talk with some students, their answer will be AI will check the AI, right? But let's hear it from Anand.

**Anand**: [00:57] Thank you. Oh, okay, this- well, I'll just try and speak loud. Am I audible? Okay, cool, with your thumbs up. Maybe if I'm not audible, I'll do that, but-

**Host**: [01:12] Okay, sure.

**Anand**: [01:14] Put it, yes. Okay, that probably- okay, yeah, great. That's better, then. I can speak softer. You know, you are coding agentically. Curious: **what percentage of the software that you use is coded by you?** And the answer could be zero, that's perfectly fine. Maybe you created some software, but haven't really gotten around to using it, and therefore it's zero, that's also perfectly fine. Maybe there's some software that you've written that you actually use once a month, once a week, maybe daily. So, quick question: how many of you, on a daily basis, use a software that you've written?

[02:06] Okay. How many of you have, in the last three months, used a software that you've written? Okay, that's about 3, 4, 5 hands up. Great. How many of you have written a software that you have used at all? Okay, that's 1, 2, 3, 4, 5, 6 hands up. Which is interesting. What are you doing? I mean, if you're creating software- Okay. How many of you have written software?

[02:50] Okay, that's about 10 hands up. How many of you have not raised your hands so far?

**Host**: [02:55] [laughter]

**Anand**: [02:57] Okay. Good. That's one hand up, whereas it should have been about 25 hands up. Great. How many of you can hear me? Okay, there are still some hands that are not. Okay, good. Now I have a sense of, roughly, what kind of response I should expect from this audience. Good. No, no, you're not bad at all. I've had some really interesting audiences. But, no, good to know. I have been using one piece of software that I've written almost on a daily basis. This is my music player. I used to use VLC. The trouble with VLC is that it does not have a composer column that you can sort by. So, out of this list of columns, I can pick whose, which album, which artist, which maybe even which year, yeah, or date, which is useful. But if I want to get in the song by a specific composer, and sort by that composer, or filter by that composer, it's not particularly realistic.

[04:09] So, I said, "ChatGPT, do you know of any music player that does this?" And it said, "Anand, VLC is an open source media player. You are a programmer. I can fix programs like crazy. What are you talking about? Just take it, download it, and fix it." Okay, that's a bit embarrassing. "Okay, ChatGPT, can you please do that for me?" It said, "Okay, yeah, sure. I'll build you a VLC composer version," which, if I hope I've gotten the right version, no, maybe I should start again. And on this one, if I right-click, and yeah, I have the composer as the last column. I was feeling so totally proud, and went to my daughter, and said, "You know what, I had ChatGPT create my own version of VLC." She looked at me like I was so dumb. "Why didn't you have it write the entire music player?" I said, "Oh, okay. Yeah, that's a thought."

[05:15] So, my music player, among other things, works on my phone, as well as on my laptop, with a synchronization. But the most important thing is, I can right-click on it and say, "Find me 10 similar next songs," and it finds the songs that are like the songs I like to listen to next. Effectively, my personalized recommendation engine, which works dramatically well. I find that this sort of a thing is now- I mean, software is malleable. You can take any software, start editing it, and it doesn't even have to be open-source. Yesterday, I was hacking Gmail. Look, one of my problems with Gmail is that I've got all of these things, I kind of know I'm supposed to set up a calendar invite for that, I kind of know I'm supposed to set up a meeting for something else, I know I'm supposed to ask ChatGPT how to answer this email, but I have to re-process this every time. Wouldn't it be great if I could just write a little note against my email? So I said, "Okay, build me an extension that will automatically do that for me." And, where's my email? Gmail. Yeah, here you go.

[06:35] So, I have my inbox filled with little things like this. So, I, if I picked an email, okay, yeah, so here's a note about a hackathon, and what I do is press Alt+Shift+M, type in a note saying, "Okay, ignore for now." I don't have actually have to do anything about this email, and that now appears as "ignore for now", and I can avoid having to re-process that email. So, software is malleable, and I think one of the things that we should do is just think about how we use software, and start using software for ourselves. This, incidentally, has very little to do with the talk. The talk itself is about how we verify AI, but I was curious to see if we were actually using dogfooding it, because that may be one of the most important things that we can think of. But, **what I am going to talk about is how one goes about verifying AI agents.**

[07:44] Yeah, that's actually what I'm going to be talking about. I was thinking if I wanted to add something to that. We run a test. This is a coding test. Wondering if I can show you the actual coding test? Yeah, I think I can. This is how we recruit. So, our talent team uses this software that has tests for all kinds of skills, and I'm fairly sure there was some place where I had- Okay, yeah, some of the questions are like this. Here's a basic analysis question, which asks what actions are appropriate before you handle a large order, and there are three wrong answers and, presumably, oh, okay, maybe three right answers and one wrong answer, whatever. So, there's a question bank, and we have to prepare this sort of a thing.

[08:42] So, I took this test, and here's my score as a data analyst. Question: based on this score, how many of you think Straive would have hired me as a data analyst? How many people say, "Yes"? Okay, a few people. How many people say, "No"? Okay, half a hand went up. Right. Now, 52 out of 59 seems like a reasonably good score, and if we look at the actual performance against questions, so, I got a SQL coding question right, the average time is 8 minutes 40 seconds, I completed it in 34 seconds. Yay! I'm really quick, right? Aptitude questions, numerical, I got it right. I got a spatial visual question wrong, data-driven question right, and notice I'm doing this in like 6 seconds, as against the average of 36 seconds, and reasonably good performance on the Python coding result as well. So, pretty good stuff.

[09:47] And there's also a proctoring result, where I have to turn on my camera and it checks if I am, in fact, the person who is solving the question, nobody is behind me helping me, that sort of a thing. And I passed the proctoring test as well. Only one thing, so you notice that the number of violated images is zero. None of these have any violations. Kind of looks fine, right? Except, **how come I'm eating an apple in the middle of a test?**

**Audience Member 1**: [10:26] The agent is writing code for you.

**Anand**: [10:28] **Because my agent is writing my code for me.** Exactly. And this is what it was doing while I was eating the apple. So, Codex was running. I hope you are doing this on all your tests. If an agent is not taking your test, then you are wasting your time. If an agent is able to solve your test, you have to ask your professor, "What on Earth are you teaching me when my agent can do it?" That's what I tell my students, too.

[11:00] So, yeah, Codex on the right side, not a particularly smart model, this was GPT-5.6 Luna medium, right? I'm not spending tokens on something as basic as this, which is incidentally why it got some of the spatial questions wrong, by the way. So, yeah, it goes there, it starts solving the quiz, does a really good job, and in far less time than I could have solved it, it managed This is real time, by the way. So this is actually how fast it was solving it. First question, it's got a reasonable sense of what needs to happen. Second question, fairly sure it'll move on pretty fast from here, yeah. It is solving one after another.

[11:50] I shared this with the team that put together the questionnaire, and I asked them two questions. One of them I'm going to ask you, but let me ask the first question. My first, let me pause this. One of the things I said to them was, "Why does your question bank have errors?" There was one question, for instance, about how to filter a Pandas table, and Luna used a query function. Query is a perfectly valid function in Pandas. I tested it out manually later on, and it said, "Fine." So, I answered a question, Luna answered a question correctly, I checked it, and the answer was correct, but the question bank is wrong, clearly. And, therefore, I got penalized for it. Now, **who verifies the verifier?**

[12:44] The question bank is supposed to be the source of truth, right? I mean, it's filtering for either a human or an agent, depending on who you think you want to hire, and there is a mistake. Second, and this is a question to you: given that Codex solved that exam, should I have been admitted? Should Straive have taken me, given the score? How many people say, "Yes"? Doesn't matter whether an agent solves. Okay, that's 2, 3, 4, 4 people say yes. How many people say, "Nope, that's not a valid test"? Okay, 1, 2, 3, 4, 5, 6, okay, that's- And, okay, the hands definitely went up faster, as well. So, what we're saying is, "Look, I want to hire the human," or, "I want to evaluate the human, not the agent," maybe. Is that right?

[13:46] Think about it. I'm just tossing a question out here. Here's human A, who's smart enough to use an agent. Human B, who's not even using an agent. Who do I want to hire?

**Audience Member 2**: [14:00] It depends on the role, right?

**Anand**: [14:03] Go on. "Depends on the role"?

**Audience Member 2**: [14:06] It depends on what role you expect to do. So, if the job process is about that, they're supposed to use the AI agent to do something, then of course you hire someone, the other one. You might want someone to actually might use AI agents to start with, but you also want that person to be able to critically analyze the results, or troubleshoot things in the absence of AI, then perhaps [inaudible].

**Anand**: [14:27] Good point. So, the answer is not necessarily a "yes" or a "no", the answer is, "It depends on the role." Fair. For this quiz, then, here's a quiz that can be defeated by an AI. What went wrong, do you think, in the creation of this? Because, I'm staying clearly that: A, it's not measuring what it's supposed to do, it got the question wrong; second, it's not measuring what it's supposed to do because it did not detect me as violating any of the rules. Eating an apple during the quiz apparently is not a violation, though it indicates several, several other things. Why? What went wrong in verifying the verifier? Any guesses? This is an open discussion. Yes, please.

**Audience Member 3**: [15:19] The specification was not complete.

**Anand**: [15:22] Specification was not complete? That's a possibility, but what- what would you have added?

**Audience Member 3**: [15:28] Like eating, you're not supposed to eat during the exam. That could be a violation.

**Anand**: [15:35] Got you. So, add eating, check if they're eating. What if I was not eating, but-

**Audience Member 3**: [15:43] [inaudible]

**Anand**: [15:49] So we change the specification to be what? No hands at the back, either. But, how else would you change the specifications?

**Audience Member 4**: [16:01] There is another way, like maybe we fix the exam nation of spaces.

**Anand**: [16:05] Sorry?

**Audience Member 4**: [16:06] Maybe we fix the examination spaces, the reason for having to [inaudible].

**Anand**: [16:09] Oh, okay. Do not- okay, got it. So, option A, maybe the specifications were incomplete, but how do we complete them is not immediately obvious. Fair enough. Maybe we set it up in an examination space where you can't possibly use an agent at all in the first place, so a change of environment is another way of solving the problem. Got it. What do you think the people who were creating the exam got wrong? Any other answers? Yes, please.

**Audience Member 5**: [16:40] They didn't validate whether they verified what they were trying to.

**Anand**: [16:45] Got you. That's an important one. Does it actually achieve the objective is something they didn't validate. Except, they actually did, meaning, they had a lot of people take the test, and yeah, it was pretty good that it was testing for SQL skills. People without SQL skills weren't doing a good job. People with good Python skills were doing a good job. So, I'm guessing what you're saying is maybe they didn't test it well enough. So, there is a specification issue, potentially, there's an environment issue, there's a validation issue, though what exactly it is, probably needs to be defined. Okay. Anything else? Any other mistakes that they might have made? Yes, please.

**Audience Member 6**: [17:34] Um, they assumed that no one would use an agent.

**Anand**: [17:38] They assumed nobody would use an agent. Almost a blind spot. So, what am I assuming without my even knowing that I'm assuming it? That's a valid point. But, how does one know what are the things that I'm assuming? Just guess.

**Audience Member 6**: [17:59] Can you repeat the question?

**Anand**: [18:00] **How do you know what your assumptions are?** And the reason I say that is sometimes we say, "I assume X, Y, and Z," but in reality, we're probably assuming a dozen other things. "Oh, that's obvious. The world will exist tomorrow." Yes, of course I'm assuming that the world will exist tomorrow. It's not like I need to state that as an assumption. Or that there will be no incredibly powerful robo that would come and eat us up in the future. Just like I kind of assuming that it's not like there's suddenly going to be an intelligence that's as smart as a data analyst that's going to come and take my test tomorrow. Except that it kind of happened. So, how does one be aware of these kinds of assumptions?

**Audience Member 7**: [18:53] Have another agent check. [laughter]

**Anand**: [18:57] That is actually a fantastic idea. You know, that's almost the same as saying, "Look, let me ask a friend, a colleague, a smart professor, an agent, someone to double-check." No, that's actually, you know, that maybe one of the best ways. If you literally ask, "What am I assuming that I'm not even aware of? What are my blind spots?" It can do a pretty good job. One of my techniques is is feedback. I make a list of all the stuff that people tell me that I ignore. The reason I ignore it is, "Oh, it doesn't matter." "Oh, that can't be right." Or, "Oh, I already knew that." Or whatever. But if I'm ignoring it, it's a blind spot, and if somebody is telling me, then it's clearly something that needs to be corrected. But asking an AI is a pretty good way of doing it, as well. Anything else that they may be missing?

[19:54] See, I put what you just said broadly under three buckets: that we could be specifying better, we could be verifying better, we could be reviewing or interacting with the system, the environment, in a better way, in any shape or form. Today we have agents. Agents are arguably smarter than us in some ways, arguably not anywhere near as smart as us in some ways. But the thing is, it's a jagged edge, and if I see Ethan Mollick's description of the jagged edge, here's how I think about it. There is a human level of intelligence, but the agents are getting smarter in certain areas, and where we are today, probably somewhere between here and here. Yeah, they're probably not smarter than us in most areas yet, but they're probably smarter than us in many areas. And, I don't know, AGI, ASI, whatever you want to call it, is when they get to this stage, when they are smarter than us in the majority of the areas. They might get there, they might not get there. I'm less worried about the future. I'm more curious about the present. So, if this is how things are right now, **how do you specify to someone smarter than you? How do you verify someone smarter than you? How do you review someone smarter than you?**

[21:22] Any guesses? You know, how- how do you do it? You've met people smarter than you. How do you specify to them? How do you verify to them? You've seen other people who've interacted with people smarter than them. How do they specify? How do they verify?

**Audience Member 8**: [21:38] Make them show their work.

**Anand**: [21:39] Make them show their work? An example?

**Audience Member 8**: [21:42] Like if you do a mathematical equation, they show the working that gets you to the answer.

**Anand**: [21:47] Got it. Show me the steps, and I will cross-check the steps, and that tells me. Sure. What that allows you to do is probably not get fooled by someone who might be smarter, who might actively be trying to trick you. Or, yeah, even a smarter person can make a mistake, but you still have it broken down into manageable pieces that you can review. That works. Any other ways? Yes, please.

**Audience Member 9**: [22:20] I have heard from someone, I don't know if that is it's easier to verify a solution, just computationally, compared to actually [inaudible].

**Anand**: [22:30] Some solutions are much simpler to verify than actually solve. Fair point, and if we had some way of building a solver, or something already existed, you're saying, that becomes easy. Got it. And I think that's an approach where you say, "I'll stick to that kind of a problem where I can easily verify it," which is a good option. Or, "I will find some way of easily verifying if the answer is right." That's an equally valid option. Can you give me examples?

**Audience Member 9**: [23:04] Like optimization. To search for an optimal can be difficult, but to verify that it is can be straightforward.

**Anand**: [23:15] Could you give me an example where verifying that something is globally optimal-

**Audience Member 9**: [23:19] Not globally, but-

**Anand**: [23:21] Uh-huh.

**Audience Member 9**: [23:22] If let's say, solving it will need a lot of computation, but just to know whether that is, what's it called, the mean, you just compute the minimum cost, or let's say also the complexity, something like that. So it will need fewer computations to verify.

**Anand**: [23:47] Got you. I can see many examples where I can see if if somebody's solution is less costly than the previous one. So, better, yes; best, not sure. But at least you know if it's better, and that's still good. And in a way you're saying, "Look, if it works good enough, that's perfectly valid." Any other ways that you specify to somebody smarter or verify something smarter?

[24:25] I'll take your approach, which is ask AI, right? Not a bad approach. So, I did, and I said, "Look, it can't be that now is the first time we're having to specify to someone smarter, right?" You visit a doctor. How on Earth do you give specifications to a doctor when you don't even know what's wrong with you?

**Audience Member 10**: [24:47] The doctor asks you questions.

**Anand**: [24:49] The doctor asks you questions. So, interviewing seems to be a pretty good technique, where, for instance, you would tell an agent, "Look, I have no idea what I want. You ask me.

---

**Anand**: [24:59] ask me. Figure out what I want and then solve it. **Interviewing is one of the most effective techniques that I've seen**, and I learned that from doctors. How do other professions do it? How does a judge decide in a patent case when they have no clue of the underlying technology?

**Audience Member 10**: [25:19] [inaudible]

**Anand**: [25:23] They ask people smarter than them, they have somebody argue for the plaintiff and somebody argue for the defendant, and compare the arguments. That's not a bad idea. Say, "Claude, this is what ChatGPT said. ChatGPT, this is what Claude said. What do you think?"

[25:42] Not a bad approach, right? So, I said, "Let me do that kind of a thing," and yeah. Where did this go? Yeah, I'm going to change the order in which I did this.

[26:02] So, what I did was asked, hmm did this not load properly? Yeah.

[26:11] So, I asked a whole bunch of agents, "How do experts specify their briefs? How do they review work? How do they verify results?" And not just that, I also said, "Look, I've been using agents for some time now. So, take all of the 10,000 or 12,000 prompts that I've provided this year and go through this. And tell me how I am actually specifying what I want, how I'm reviewing what I want, and how I'm verifying what I want."

[26:44] Today we're going to be only focusing on the verification part and going through some of these approaches, the ones that seem to have worked well on the software that I've been playing around with. But I'll give you the broad outline of this. None of this is unusual. None of this is non-obvious. Perhaps the only one that may not be obvious is that you can run this technique on yourself.

[27:09] **Your prompts are a fantastic data set.** Your prompts are particularly a fantastic data set when you are responding to an agent. If you say, "No, no, no, that's not what I want," you're doing three things. One, you are specifying a preference. You're saying, "I prefer X over Y." Second, you are spotting an error or a misalignment in the agent. The agent is not delivering something that you need, and therefore is potential grounds for training. And I don't mean training in the sense of fine-tuning, but just even creating a skill to resolve it. That's pretty useful. Third, it's a fantastic data set to talk about what it is that you care about, and therefore help you prioritize and build your profile, your objectives set, etc. The single most valuable button for me on both Claude and ChatGPT is that export data button. Click on it and it sends you, well, in ChatGPT's case it sends me a 1.4 GB archive. Smaller in Claude, but worth mining.

[28:13] So, let's take some examples. One of the things that we're talking about when it says when we say specification is defining what constitutes done. Here are some of the prompts that I find myself using. So, I say, for instance, "My aim is not to produce a time log, an activity report, blah, blah, blah. See, I've given you a task. Make sure that your definition of done does not include this." Or, "If the task never defined what does not count, I want you to infer two or three tempting false victories, and confirm that the answer is not one."

[28:55] Effectively, what I mean by that is, look, I've said a bunch of things, I may not have exactly said what I want, but I don't want you misinterpreting something trivial and simple. Figure out what I really want and get there. These are ways of me saying I won't specifically define what constitutes done for you in a specific way, you have to figure it out. Especially the first one, for non-trivial tasks, define what done means and verify before concluding. You figure that out.

[29:29] Now, why is a definition of done something that helps? And why is specifying it in an ambiguous way useful? Because I have no idea what done means. I'm specifying to an intelligence smarter than me about an area that I don't have enough experience in. We're going to be facing this situation on a regular basis, and you probably are already seeing that sort of a situation. But all of my colleagues today are at that stage where roughly half of what they're tasked with is stuff they don't understand. By the time you graduate, most of the stuff you'll be dealing with is stuff you don't understand. You'll be asking an agent, you're effectively the agent's intermediary, which means that you're going to be slowing it down.

[30:17] One of my colleagues, he's a fresher who joined as an intern. I connected him with Ankur, who's the CEO of Straive. I said, "Ankur, you need a demo. Important client, that's going to happen in three days. You reached out to me and said, 'Anand, do you have somebody experienced who can do this?' I'm going to give you an intern. Why don't you just talk to him? Let's see what happens."

[30:43] What I told Varun was, "Varun, look, there's no way you'll understand a word of what Ankur is saying. Do not try. He will talk at a very different level. What I want you to do is: one, record the call; second, transcribe it; three, paste it into Claude; four, send him the output. That's it."

[31:05] He did that, and then shared that with Ankur. Ankur got on a call with Varun again, and said, "Yeah, you know what? I need this, I want to change that, X, Y, Z, whatever." He took the same transcript, put it back into Claude, gave him the result. That evening Ankur and I had a call. He said, "Where is this guy Varun from? He is brilliant!" And I had to tell him exactly what he was doing.

[31:29] **Sometimes the smartness is really about getting out of the way.** The agent was able to understand Ankur better, Varun was merely hand-holding him. We are going to be in that situation. We're just going to need to make sure that we don't get in the agent's way in many of these cases, especially when they're getting smarter and smarter, while still making sure that the output is not completely off.

[31:55] But part of engineering, you'll say, "But how do you know if the output is not completely off when you don't even know what the output is supposed to look like?" In this case, Varun was using Ankur as the definition of done. "You tell me. Does this look good? Does this not look good?" The ability to get that rapid feedback mattered. So, which is why I'm often specifying things as, "You tell me if this looks like it's the right thing to do."

[32:22] Where that helped me was in one of these kinds of situations. I asked it to create this forked bracket. Basically, I asked a bunch of agents, "Here's a forked mounting bracket. Create the CAD diagram for me for printing, 3D printing." And it did. Let me give you a couple of examples. On the left is Codex, on the right Sorry, on the left is Claude, on the in the middle is Codex, and on the right is the actual output or sample that's supposed to be delivered. Is anyone able to spot any difference between the three?

[33:11] Any differences?

[33:28] It looked identical to me, and I went right ahead and said, "Oh, these agents are doing pretty well," until one of my colleagues turned it all the way around and said, "Hey, wait, wait. What's this little thing that Codex has?" "Oh, okay. Yeah, fine. Ah, that's a small error, let it be."

[33:51] I had had two processes. One in which I had asked the verifier to visually inspect and make sure there were as few visual errors as possible. In the second, I did not tell it to visually inspect. I said, "You decide how you want to inspect and see if it's okay." Option A, I told it how to verify. Option B, I said, "You decide what constitutes done."

[34:18] And what it said was, "Anand, this particular diagram, I searched and I can find an exact match in the FreeCAD benchmark. So, there actually are enough material properties around this, and when I look at those material properties, it turns out that Claude gets this right close to 99%, but Codex has made a total mess of it. On the geometry, it's actually only 31% correct. And the reason is, if you look at the solid volume overlap, whole bunch of things that I don't even understand, it turns out that there are big differences in the volume, in the phase center ICP, whatever that is, spatial multipliers, property fidelity."

[35:07] In other words, there are a series of things that I'm not aware of that I should be looking for, that all I had to do was let it loose and say, "You go beyond the limitations of my thinking and figure it out." And it does a better job than me.

[35:23] Now, how do I know that the better job than me is, in fact, right? I don't, but at least it's better. Put another way, what I'm saying is **one of the things that I've found is that I am the person that's messing up the verification of the verifier.** I'm the one who's giving it constraints where I probably should evaluate how good my constraints are, which is a form of checking my assumptions. And that's one way of doing it, with and without an assumption, even when something may not even look like an assumption.

[35:58] Another is testing the tester itself, which someone mentioned as a way of verification. Right. So, I did this. I was grading a class at IIM Bangalore. They had eight student groups, each of them submitting an assignment, which was a data analytics assignment. And I went over to Claude and said, "Look, I have all of this data on my machine. You can see it in my downloads folder. This is a presentation, and I want you to go through, you know, all of this. Take a look at the slides they've shared, treat that as what they've said, inspect the images wherever. Effectively, look at all of this material and score their presentations. And tell me what you think, which group did the best job at presenting their case study."

[36:54] And it said a whole bunch of things. It said the healthcare group, it would probably give them a 19 out of 20, the next group, co-living, was given a 19, and so on.

[37:09] The next prompt was Wait, where did this go? Yeah. Here's another answer from ChatGPT. It was exactly the same question, but answered by ChatGPT, and I said, "I want you to fact-check what it said, what you said. Take what's better, drop what's worse. If that gives you any new thoughts, go along that direction. In other words, compare your response and learn from it." That's what I tell my team as well. You've done something, you've done almost exactly the same thing, compare notes, tell me what you've done better, except that agents seem to be doing this a whole lot better.

[37:53] The answer was fun. The very first thing that it said was, "I was wrong about Group 8's contradictory accuracy figures." It had earlier said, "Look, Group 8 at one point was saying 92%, at another point it was saying 98%, or their slides were saying something, their words were saying something different. That's wrong." It turned out that ChatGPT, which tends to be a little more diligent about some of these things, if not as visually perfect, went and did a bit of analysis, and found that if they take the survey data, knock off the invalid respondents, you get 98%, if you don't knock off the invalid respondents, you get 92%. So, both numbers are in fact correct.

[38:45] That's fair. So, the agent made a mistake by deducting marks for something that was invalid. Another agent did not make that mistake. When you combine the two, the results of the two reduce. Now, that's a reasonable approach. The good part is this is to a good extent a scalable approach.

[39:08] Let me explain what I mean by that. One of the things we were doing was let's take classification of data. If I am classifying a customer chat message like, "Help with adding some items." Now, that is supposed to be a change order, but some models, like in this case Nova-Lite, was classifying it as placing an order. Now, the customer is not trying to place an order when they say, "I want help with adding items." Models like GPT-4.1 mini got that right, Gemini 2.5 Flash Preview got that right, etc.

[39:48] Some of these are tougher ones, there are a whole bunch of fairly easy classifications that none of the models got wrong, and there were some that were of increasing difficulty. But overall, the accuracy, if you take all of this put together, was about nine 85% or so, about 14.something percent error rate. But the thing was the models are not correlated. So, when we looked at how often two models classify it the same way, the correlations are far from perfect. Yellow is high correlation, blue is low correlation. So, Gemma 3, for instance, wasn't classifying it the same way as GPT-4.1 nano at all. So, if I have Gemma 3 cross-check GPT-4.1, there's a decent chance that between the two they won't make as many mistakes.

[40:47] Which is what we evaluated. What happens if you have two agents cross-check the results of each other? Even if you randomly pick agents, that error rate drops from about 14% to 3.7%. The rule is: if Model A says yes, or if Model A says something, and Model B says the same thing, then I will accept your answer. If either one of them disagree, then we will not accept the agent's answers. Somebody will have to manually cross-check it, that's fine. Now, it did increase the manual effort to about 12.6%. That's fine. At least we know that the results only have a 3.7% error.

[41:26] Except we can have three agents cross-check it, and that reduces the error to 2.2%, or four agents, or five agents. When we say, "Look, I will" Yeah, go on.

**Audience Member 1**: [41:39] How is effort measured?

**Anand**: [41:41] How is effort measured? I'll come to that in just two minutes. So, if I have five agents and I say none of these should disagree. If all five say exactly the same thing, I will take the result, otherwise, I'm going to pass it to a human to decide. At that point, I get 99.3% accuracy, but what that means is that there's a much higher chance that the agents might disagree on something trivial. Four of them may say X, fifth one may say, "Oh, I might think it's something else." So now the human has to do the work, right?

[42:10] That's what I mean by effort, which is 28% of the time, the models disagreed. So, that means that if I had 100 tickets, I can't automate 100 of those, I can only automate 72, typically. And 28 people out of the original 100 are still required to check what the agents disagree on.

[42:32] So, I'm reducing the cost 72% at 99.3% accuracy. Agents don't really cost much. For any person on the business operation side, that's fantastic. Yeah, I'll take it, as opposed to, you know, 85% accuracy, which they'd say, "Ah, no thank you, my agents can do better than that."

[42:53] So we Yes, please.

**Audience Member 2**: [42:54] But in this case, your assumption is that an error [inaudible] is not silent, right? So how do you do with silent error?

**Anand**: [43:02] We are classifying What do you mean silent error?

**Audience Member 2**: [43:05] If they all agree, they are all wrong.

**Anand**: [43:08] Yeah, no, exactly. So, what we're doing here is taking these and bucketing it into something like a change order or a track order, or there are a total of some 15, 20 categories. No, exactly.

[43:22] So, in such, in general, if you can get a bunch of agents to talk to each other in some shape or form, that gives us some kind of a scalable mechanism to verify or improve the result. So that's one of the things that I've been using for a long time, which is just asking another AI. I find that frequency-wise I use it quite often, impact-wise it's reasonably high.

[43:50] But let's check something else. Supposing a model says Okay, one of the other things that I ask it is, "How sure are you of the result?" Let's say you're classifying something, or you predict a quantity, "I believe that this particular stock will go up to $800," or, "I believe that this is the next tool call that needs to be made," or whatever. You could ask, "How sure are you?" Maybe you would say, "Are you very sure, moderately sure, high, medium, low?" Or you could say, "Are you 95% sure, 100% sure, 50% sure? Give me a probability estimate. Give me a confidence estimate of how how right you think you are."

[44:34] Supposing we did that, and the model said it's 95% sure. Do you think it's right 95% of the time? Let's do a quick poll. How many people think when a model says it's 95% right, it's usually correct more than 95% of the time? Approximately 95% of the time? No hands so far. Less than 95% of the time? Okay, let's then break that up, there's about a dozen hands. So, if a model says it's 95% right, is it typically what, more than 80% right? Okay, no hands. More than 50% right? Okay, couple of hands. More than 10% right? Okay, a few hands there. Okay, we're not sure.

[45:28] The good part is that's measurable. Right, a calibration is a fairly straightforward thing that we can do, and of course it depends on the problem, but what I was looking at was trying to see, yeah. It was a banking support, customer support request classification. Take a bunch of statements, banking questions, and have the model evaluate and come up with an answer. Also, ask it, "How sure are you?"

[46:01] These are the calibration results. Let's take the blue line, that's GPT-4.1 nano. So, the X-axis is how confident it says it is, the Y-axis is how accurate it actually is. Let's take this number. Uh or no, let's take this one, 95%. So, when GPT-4.1 nano says it's 95 to 95% 97% sure, it's actually correct about 77% of the time. Overconfidence. Effectively, anything on the bottom right is overconfidence, anything on the top left is underconfidence, and at least the two models that I'm showing here, which are GPT-5.6 Luna and GPT-4.1 nano, are in the majority of the cases exhibiting overconfidence. This is a bit of an anomaly, I had only 10 requests, all of which happened to be right, so could go either way.

[46:59] But that seems to be a bit of a problem, right? So on the one hand, you ask a model, "How sure are you?" It gives you a number, but that's not a number you can rely on. So, does that mean that asking a model for its confidence is not helpful? Any ways?

**Audience Member 3**: [47:18] [inaudible] the model's accuracy [inaudible] the model's perceived accuracy and its actual accuracy [inaudible].

**Anand**: [47:25] Got you. So, which is effectively use the calibration curve and work backwards, and see how accurate it is. Absolutely.

[47:33] What I find is that there are what there's one major advantage to that approach and two minor disadvantages. The major advantage is now I can actually with more reliability tell people, "Yes, when I tell you it's 95% sure, it is actually 77% sure. I've done the checks, and it works that way, so you can rely on that number." The the minor disadvantages are twofold. One, I have to recreate this calibration curve for every problem. The calibration curves vary. It's not just model-specific, it's actually model plus problem-specific.

[48:13] The second thing is knowing how confident a result is doesn't really help me. Supposing somebody comes to me and says, you know, "I've got an answer. I am 78.3% sure this is correct." What am I supposed to do with a 78.3% correct or How am I even going to act on it?

[48:35] That probably is one of the biggest things, and this boils down to something we're not going to talk about much today, which is a specification problem. But what's the problem we're trying to solve? Well, if it's a banking classification, the banker says, "Look, I just want the classifications to be correct. You know what I can do as a banker, or if not you can probably guess, or you can ask me, but just tell me what I should do."

[49:02] At which point you'd start thinking, hold on, how's how are they solving the problem today? They've got a bunch of people whose job it is to go through each one of these, solve the problem manually, so we have that as a resource. So, if I went to the banker and said, "You have a team of 10 people. I can probably make that a team of five people or four people, and take the cost out of your system, add a little bit of cost for the tokens, so for less cost you'll be delivering it at the same or higher accuracy." That's really what we want to tell the person, right?

[49:36] So, in that case, the banker would be perfectly happy if you gave them a list saying, "Look, here are your classifications. These are the ones that I'm most sure of. These are the ones that I'm least sure of. Have your team go all the way from the bottom up to however much time and effort they can spend on this, and verify the results." So, effectively, we are giving them a verification

---

**Anand**: [49:59] a verification, a prioritized verification checklist. Now, in that case, I don't need the model or the calibration to be accurate. **I just need it to be monotonic.**

[50:10] Meaning: if you say 95%, are you more sure than 93%?

[50:15] If you say 50%, are you more sure than you when you say 20%? And you can see that these curves are largely monotonic. There are some aberrations, but broadly, yeah, they're kind of there. Higher confidence means more right. Lesser confidence means less right. That works.

[50:31] What's even more interesting is that the logprobs that you get. A fair number of models give you the logprobs as well. Sorry. I'm Just say.

[50:45] How many of you have extracted a logprob from a model?

[50:53] Oh.

[50:55] Let's then Okay, I'll step back a bit.

[50:59] So, models generate tokens. You kind of know how they generate tokens. They work as, let me show you how they Okay, send this. Does this work?

[51:20] No, maybe not. Okay, so I'll use a slightly different app.

[51:30] Okay.

[51:34] So, let's say we asked a model the question: "In which episode of Friends did Joey eat too many marshmallows?"

[51:44] The way it generates the output is it thinks a little and then it says, "Okay, I'm going to start generating the next word." Token. And it begins with: "Jo-e-eating-too-many." The breaks are exactly what the tokens are that get generated. But the way it does it internally is it spends a minute thinking, "How should I begin?"

[52:06] Now, in this particular case for this model, which may have been GPT-3.5, I can't remember. It said there are two ways I can probably begin: 70% chance I'll start with "Jo" going towards "Joey," 28% chance I'll begin with "in." So kind of thinking, "Okay, in the episode, something or the other," it could go that way. It also thought maybe I could start with "the," about 1.7% chance. Then some smaller probabilities. So, it thinks of a few different words that it could say and then picks based on those somewhat randomly. And depending on the temperature you pick, it decides to go for the of to the highest one or choose a little more chaotically.

[52:49] But once it started with "Jo," it had no doubt that the next token should be "ey." It said "Jo," now it's "ey."

[52:59] Before "eating," it said, "I can probably go for 'ate' instead, or 'eats', or whatever." But "eating" seems to be the next best thing to say.

[53:09] So, it keeps going like this. Now, interestingly, it wasn't very sure about "episode 20." It said, "Okay, I have a 45% chance that it's probably episode 20 in season three." And it wasn't entirely sure about season three either. It said, "Okay, good chance that it was probably season three, but Joey may have been eating marshmallows in season seven as well. 7% chance." That is a pretty good chance.

[53:34] So, it's effectively computing—not computing, well, yeah—inferring what the probabilities are of what it should say next. But what that means is that the probabilities have fantastic information about its level of confidence.

[53:51] You can be reasonably sure that it's not making a mistake about the "ey." "Too many marshmallows," it's really confident about.

[54:00] But season three, 77%. Episode 20, 45%. So now I know what I should check. If I had to verify this, the first thing that I would check is in season three, was it perhaps episode 21 or 11, or whatever? Or at least I would double-check the season the episode 20 first. And I would double-check the season three second. That gives me a prioritized queue. And that prioritization has cost implications. Because I can decide when to stop at what level of quality. That matters.

[54:38] It turns out that these logprobs are surprisingly accurate. Well, surprising to me, meaning I did not expect them to be as effective as they turned out to be. **But they are amongst the best ways of predicting how good a model is, especially if you just rank-order them.** Meaning if you say, "Look, I will take the output of a model. Where the logprobs are weak, where the probabilities are low, that's where I'm going to cross-check." Turns out that that's a fantastic approach. Works pretty well in most cases.

[55:12] See how I am doing for time? Okay, we have half an hour, good.

[55:16] So, that allows us to therefore double-check the results of a model. And, yeah, okay, I'm not going to go into the details of logprobs, now it gets a little crazier. But that's yet another way of testing the tester itself. Is the validator giving us good results?

[55:38] Question to you: how do you verify your software usually? What are your top approaches? You write a piece of code, how do you know it's working?

[55:57] Yes, please.

**Audience Member 4**: [55:58] Check against specifications or establish tests, automated tests, and so on.

**Anand**: [56:04] Got you. How do you know your tests are right?

**Audience Member 4**: [56:09] Could be by benchmarking against previous test results, industry practices.

**Anand**: [56:16] Benchmarking against previous test results and industry practices is a perfectly valid approach. What that means is cloning software, especially software that has test cases, is particularly easy, right? Somebody's taken the effort of defining the spec for you. And then the verification follows.

[56:37] Which means—and does it? Open question—that therefore specification, because it can lead to verification against the specs, **specification matters far more than verification?** How many of you would say, "Yes, specification matters more than verification"? Okay, one, two, okay, four, five. How many disagree and say, "Verification probably matters even more than specification"? Because if it goes wrong, then who cares how you specified it?

**Audience Member 3**: [57:07] How do you verify without specification?

**Anand**: [57:10] Good question. How do we verify without a specification?

[57:15] And trust me, that happens quite often. When we download a browser, do we specify what we want? Somebody created it for us. But we still file bug reports. How does that happen?

[57:40] We buy an apartment, we haven't constructed it, somebody's constructed it for us. We haven't given any specs. We still complain to the landlord. How does that happen?

**Audience Member 5**: [57:50] Because the user will have a subset of specifications, [inaudible].

**Anand**: [57:54] The user has a subset of specifications. Some of those specifications are latent, maybe assumed in the shared fabric of society, in civilization, of human behavior, whatever, blind spots. We didn't don't necessarily know, but right.

[58:12] "I'll know it when I see it," is something that's pretty common, right? So, if that's the case Now, you could say, "I'd put this in specification. I'd put this in verification." But how do you capture this sort of a thing when a user might complain about something later?

[58:32] Nobody specified something, and therefore we haven't verified it, but still we're going to get complaints. How do we capture that?

**Audience Member 6**: [58:43] User testing?

**Anand**: [58:44] User testing. So, we share it with a bunch of people. We share it with 50 people, we share it with 100 people, and that gives us a few more inputs. Fair enough.

[58:55] Would that suffice?

[59:04] And I see two problems these days with user testing. When we've given applications for user testing, the users who are meant to be testing it have been assigned for user testing. That's basically like giving you homework. And we know exactly how much you enjoy homework.

[59:27] The You know, I'll give you a live example. My daughter said, "Oh, I built a Telegram bot, Dad, so can you be the user and test it?" I said, "Absolutely." And I turned on to this episode of Matlock which I was watching while Codex was testing the app in the background and sent her a report. Which is not a bad thing. I mean, I may be a bad parent, but Codex was doing a good job, and it created a fairly good report. And therefore, you can use agents for user testing. Incidentally, that works pretty well for so many scenarios.

[60:02] Let me see if I can locate that. Persona gen. Demos. Yeah.

[60:15] An auto company, actually Shell. Shell reached out and said, "We have a problem. Surveys cost us hundreds of thousands of dollars. Nielsen charges anywhere from 100K to 500K per survey. But we saw this Google report which said, 'Oh, if you give an agent a personality, it can act as if it is that person and answer a survey.' Can you build something like that?" I said, "Okay, fine. Let's define a segment." And can Not sure this Yeah, okay, this might work. Okay, skip this. Maybe this won't work. Okay, now, I'm going to skip this. I'll just talk you through it.

[61:00] But effectively, we had a bunch of 30 to 300 agents acting as specific persona and running user tests. Works in the sense that in the absence of a human, you get to at least a certain degree of confidence. Yeah. So here we have about 30 people who have come up with who are in the process of being administered a survey. And now we are running the survey. And yeah, people are starting to answer these questions. Yeah, they'll eventually answer it, and we get a survey response. But okay, are we really getting any new information out of it?

[61:37] Personally, I think we do get some amount of new information out of these kinds of agentic user tests. What happened in this case was not that Shell said, "Oh, I believe this is how it's going to be." They were also looking at some of the verbatim comments that the agents started filling out here. So for instance, it said, "As someone with high price sensitivity, I prioritize the finding finding the cheapest fuel station to save money." They said, "My commute involves a round trip of 23 km, so I usually refuel after work." And these verbatims had fairly useful insights. So, they went through the aggregated results, they clicked on it, "Oh yeah, it's kind of possible that a person might have said it," right?

[62:21] This was almost like a convergence of, "Oh, I had a bunch of assumptions, and you've surfaced a few of those that might need to be questioned." And that's pretty helpful.

[62:34] So, yes, **user testing helps. Users don't have to be human.** I think it gives a very good complementary perspective when users are human, but also, therefore, when users are agents. Which means that you can just have them run this. And to be fair, Claude does this automatically if you, you know, take Sonnet or Opus even and just put it in high thinking on Claude Code. By default, it automatically opens the browser, takes screenshots, tests the DOM, and so on. And all I do in my prompts is add a few more I say, "Test the accessibility tree as well. Test three or four other things that I find it hasn't yet gotten to." But most of my tests are just shrinking. It takes care of those. That helps.

[63:21] Is that enough?

[63:26] When it goes into production, we know software fails. What do we do then?

**Audience Member 7**: [63:42] Collect ongoing feedback from production.

**Anand**: [63:46] Collect ongoing feedback from production. How do you do that? And what tools do you use?

**Audience Member 7**: [63:55] It depends on whether it's technical or user-based.

**Anand**: [64:00] Excellent point. If it's technical, how do you collect it?

**Audience Member 7**: [64:04] Server logs, error logs.

**Anand**: [64:11] Exactly. Sorry, somebody said something? Okay, different conversation.

[64:17] Exactly. So, you get the logs, which means that logging the errors is a fairly critical thing. I've been using Sentry for a fair bit of time. Server error logs are important. But **one of the top skills that I have for my agents is the observability skill.** What does it take to log every single thing that you produce? Make sure that information is there.

[64:43] Put another way, now with the speed and scale at which agents are operating and we are interacting with them, the the digital exhaust is probably the single most valuable asset that we can collect.

[64:58] Agents are going to be able to analyze everything. If we are able to give them more inputs to analyze, they are going to have more context. And therefore, the collection of that input is perhaps one of the biggest human endeavors over the next few years. Biggest in the sense highest ROI.

[65:17] So, what am I doing, for instance? I'm collecting all of my meeting transcripts. Every single meeting, I save, I make sure that the transcript is turned on. And my archive is now well over about 2,000 transcripts. And that is fantastic feedback because before I go into a meeting, I ask it, "Go through all my conversations with my boss. Tell me what I should say."

[65:41] Right? "Go through all of the talks that I run in classrooms. What are the mistakes that I make?"

[65:49] Similarly, "Go through all of the logs on my server-side code. What are the kinds of mistakes you make?"

[65:55] "Go through all of the chat the the the session logs for coding agent sessions. What are the kinds of skills you need to avoid repeating yourself?" Pretty helpful.

[66:08] So that's observability on the technical side. But you also said the user side or the functional side. How do we capture that?

[66:23] One of my colleagues did something clever. It's not something I can show, but the application that he built had a little button which was simple. It said, "Report an error." You click on it, it lets them type, speak, paste screenshots, etc., which understandably files an issue on GitHub as part of the application, which was a pretty smooth implementation.

[66:50] We went two steps ahead of that. Step one was then there was an agent that was running behind the scenes that would fix the bug, deploy a personalized version of that software for this user, drop them an email saying, "Look, you reported this bug, right? We've fixed this one for you. And here's a slightly different development URL that you can go visit. Let us know if that works. If not, just file the bug report again."

[67:18] And people would do that, test it half the time, literally half the time. They would come back and say, "Yeah, this is exactly what I want." The other half the time, they'd provide some kind of edits or, "No, I didn't really mean to do that," or some rubbish.

[67:35] But now there are several different features, variations, etc., that have been tested in parallel for each person. Over time, the product manager synthesizes these. They say, "Okay, here's something that seems to be common across those, so I'm going to release an alpha version with three of these features, see if that gets traction; a beta version with 10 of these features, see if that gets traction."

[68:01] But the second thing that they did was said, "Look, if you want this particular feature, we can kind of lock it for you. We can have your own version of the software permanently running for you. Any new changes to the main one, this will be patched on top of that."

[68:18] So, it's almost like each person is getting to build their own software. Which ties us back to the original question that I was asking, which is: **how much of the software that you write is yours?** It doesn't necessarily have to be, because personalized software is not something that's too far away. People are getting to the point where they will let you build your own versions of the software. Even today that exists, it's just not very agentic. But that starts becoming a possibility.

[68:56] So, if I were to look at some of those techniques I'm not sure where observability is on this, but yeah, I'm just going to talk about the summary on observability. There are three things on the observability side:

[69:14] A, that **observability matters a lot simply for the data.** Just collect all the logs that you can.

[69:22] B, **it can be useful to improve the technical specification.** Just look at the logs, ask the agent, improve the stuff that's going wrong.

[69:31] But C, **also ask the agent to fix based on that, deploy a personalized version, and get feedback from the user.** That user feedback can be pretty effective too.

[69:49] Just going to cover a couple of other things, just give me a minute. What did I miss?

[70:03] Right. Yes, I forgot this. Now let's take a look at This was some of the ways in which I was verifying. What are some other ways in which other professions very uh yeah, verify results? Going to go through some of the top mechanisms for verification.

[70:27] How many of you have read this book or even heard of this book, *The Checklist Manifesto*?

[70:34] It's a very short book. Atul Gawande, who's who used to be the Surgeon General of the US, he wrote this book. And it's a fascinating study. *The Checklist Manifesto* is In the US, there were a bunch of hospitals where the infection rates were pretty high, and a bunch of hospitals where the infection rates were pretty low. Atul Gawande went, ran a bunch of surveys, and tried to find out what was the difference between these.

[71:10] The difference was surprising. One of the major differences was the hospitals where the infection rates were really low, the nurses had more authority than the doctors. Meaning the nurses could specifically tell the doctors, "No, doctor, you cannot operate unless," or, "You should not do X or Y." And they followed a simple checklist: "If this is happening, if this is happening, if this is happening, things are fine. Otherwise, you have to stop and fix it first. Did all of the items—the scalpel, etc.—get washed at, you know, at water at 120°C? If the temperature was less than that, you stop the procedure until that happens." Same thing with pilots.

[71:55] In other words, what people are finding is **a deterministic checklist is a very effective way of making sure that a system does not fail.** Those are effectively your linters, those are effectively your test cases. This is not new to us.

[72:14] But what seems to be new is the construction of these. Earlier, we would have to sit and manually create these checklists, manually create these test cases. What does it take for an agent to constantly go through all of your logs and try and figure out what exactly needs to be built? What exactly needs to be verified? How can you improve your checklist? What percentage of your checklist is working well, not working well? That becomes an augmented mechanism, which I think is more enabled.

[72:48] I'm going to pick another category in this: audits. Someone mentioned that you break a complex task into smaller steps so that you can verify. That's effectively asking for receipts or checklists to make sure Not not even a checklist, yeah, just proof that things are working fine. That as a technique works pretty well.

[73:12] The thing, though, is: how do you know if the receipts themselves are valid? Are you smart enough to check if the receipts are, in fact, correct or not? This is something that professions have solved in an interesting way. You periodically bring in an auditor. Not every report is audited. You hire an expert who comes in occasionally, does a spot check, does a random sampling, sees if some edge cases are covered, not covered, etc. Which means that the scale at which you can solve a problem is much larger.

[73:50] Now, an AI auditing works fine, but if you brought in a human auditor to audit not the results, but the AI audits, that becomes far more effective. That's something that we've been again doing, which is to say: can the agent always prepare an auditor report? What's the minimum information that an auditor needs to be able to check the receipts, cross-validate against that, see if the results are valid? That sort of a technique seems to be working pretty fine.

[74:18] So, we put all of this together into what's called—well, this is basically our approach to agentic software development, which covers verification and specification.

[74:32] So, the StraiveX AI-native delivery methodology is effectively saying, "Look, this is what we have learned about building software with AI."

[74:43] Step one: earlier, we would go to a client and prospect. Ask the question: "What do you want built?"

[74:50] Today, we sense. That basically means, let me give you an actual example. One of our colleagues, Tanuj, he was working inside a client.

---

**Anand**: [74:59] Tanuj, he said, "Anand, you keep talking about this AI-native stuff and all that. Look, **we aren't even allowed to use AI in this organization.**"

[75:08] I said, "What do you mean you aren't allowed to use AI in the organization?"

[75:10] "No, I mean look, we don't have Codex, we don't have Claude."

[75:12] "Okay, what do you have?"

[75:14] He said, "Well, most of the data sits in Snowflake. Snowflake has its own AI called Cortex. That's all I have."

[75:20] "Okay, great. How about you do this? Why don't you ask Cortex: This is the organization, go search online for the business context, look at all the data that you have inside, and tell me what are the most important problems to solve."

[75:37] So, Tanuj did exactly that and let me see if I can, yeah, share. So, and he had Cortex, in a few days, produce this report. The report basically was a set of use cases that would have been most effective for a—this was a waste management company. It said, "Look, we need a revenue analyst agent, we need revenue forecasting, pricing anomaly detection." And it went on into more details about how exactly you would do revenue forecasting, that you take the historical data, blah, blah, blah, laid out the entire approach, etc.

[76:16] In other words, without having to ask the client, he said okay, or what he was able to do was get a sense of what the use cases might be. He took it to Cal. Cal is the head of analytics, and Cal looked at this list and said, "Tanuj, in November we ran a consulting exercise that ran for 4 months. Fairly expensive, detailed consulting exercise. **There's an 80% overlap between their recommendation and what you said.**"

[76:49] Think about it. In other words, the bulk of what a consultant comes in into an organization to do, which is to figure out what the use cases are, to create the high-level specs, is something that agents are able to support with. Not saying human judgment is not required, but it certainly accelerates it.

[77:08] That's the sense part of it. So at this point, now Tanuj has 15 use cases, all of which he can build. So he said, "Anand, here's what I'm going to do. I'm going to create a proposal for each of these that"—oh, sorry, yeah, here we go—"that in 4 to 8 weeks, we'll be able to build this revenue forecasting engine, and that in whatever it was, yeah, we can build the pricing anomaly detection next, and we should be able to go to this customer churn prediction system, that will take only a few weeks," and so on.

[77:43] I said, "Tanuj, if you sit and build a proposal around this, by the time it goes to the client, it's going to take forever. That was our earlier approach, which is we would share a proposal. **Why don't you just put all of this into Cortex itself and tell it to solve the problem? Just go ahead, forge the solution yourself.**"

[78:03] So he did. And for instance, one of the things that—let's take, yeah, pricing anomaly detection. One of the things that came out from the pricing anomaly detection was there were 105,000 transactions that were $0.16 for a service that's supposed to cost $175 to $179.

[78:30] Think about it. This is a company that charges about $175 to $179 to pick up waste. Now, they have 105,000 transactions for which they are charging just $0.16. There are also 84,000 transactions for which they're charging customers 6 to 14 times their median rate.

[78:55] Maybe there's a reason, but look, we have a problem. This is a large number of transactions. There seems to be nothing in the data that indicates why we should be charging them this way. There seems to be a violation of the problem. It's bizarre.

[79:11] So, which means that the identification is easy. The solving of the problem is not particularly hard either. Where the human starts coming in is: did we get this right? How much of this is, in fact, true? How much of this needs an expert to validate? Which ends up becoming the third stage.

[79:31] So, Tanuj shared this in the form of an email with clients. This was one of the actual emails. Yeah, one of the emails was titled, "We're losing $117 million in revenue, and here's the fix." Turns out that customers like—these are anonymized names—Atlas Energy, which was giving us $6.4 million, gone; Orion Motors, $6 million, gone; West Shore, $3.8 million, gone, all in the last quarter or so. And we have Riverbend Mills at 2.8 million likely to leave. That's simply based on the churn prediction, as well as the actual churn data.

[80:10] Should we figure out, for instance, sitting with the account managers, why are these big spenders leaving? What's happening? Talk to the VP of all of the major champion champion customers, etc., and start solving this issue. There were a couple of insights that came up. Two of these were contract renegotiations. Four of these were because an account manager left. Five of these were clients that the client that our customers didn't even know was leaving. So it's a combination of known things, avoidable things, and unknown things.

[80:50] Now, once we know this, putting in an early warning system starts becoming pretty easy and pretty effective, but we wouldn't have got that without the validation step. Up to here, the human involvement isn't really much. We are effectively delegating to clients as the validators, which, if you remember, is exactly what I did with Ankur, who's the CEO of Straive, and Varun, who's the intern, saying, "Look, don't bother trying to validate. **Leverage the capability of the experts who are good in the field.** If you can put something together that where they, at a glance, can see the result and instantly validate, your problem is solved."

[81:28] Which leads us to the fourth stage. I'm going to talk through the remaining two very briefly. Stage four is take the same thing, build this across each of their plants. Every one of those has a different approach, but allow the agents to use the context and get to the result. And run and evolve.

[81:48] Take a look at the queries the system is generating that it has operationalized. How many of those queries have a drift? How many of those have a problem? For instance, on the pricing anomalies, it set a rough rule saying, "I will keep it at the top 10% the bottom bottom 10% to the top 90% as the range. If the pricing goes outside of this band, then I'll flag an error."

[82:11] About 2 1/2 months later, there was a bit of a drift. They had institutionalized a pricing policy where for certain kinds of services, the price would go to about 2x. So, the agent needs to look at this and say, "Oh, I'm flagging off too many of these errors. Let's look at the logs"—that's where the observability comes in—and start revising, iterating, which then starts becoming an opportunity back for the sense.

[82:39] In short, there are many ways in which I've been looking at how we specify, how we verify. That's been drawn from two sources: one, how different professions have been doing this historically; how I've been doing this in the past. All of these work, but interestingly, I find that if I just create a skill to an agent, telling them, "Look, here's all I've learned, now you go apply these," it tends to do it well.

[83:09] Outside of this, where the human intervention seems to be involved is either in a final it's largely in an end user's experience. A person says, "I don't know what I want, but I'll know it when I see it." That's something that I need to tap into. Or an expert who says, "Look, I know exactly what I want, and I will know it when I see it." That's what I want to tap in into. Those seem to be the few cases where I can't actually replace an agent as a verifier, or as a verifier of the verifier. But in almost every other case, there seems to be systematic ways of doing that.

[83:44] And therefore, for these two, observability seems to be the key. What does it take to get the most in terms of data from the humans who actually are using it, removing the intermediaries and extracting that as a form of or a mechanism for getting the data in?

[84:05] So, today, if you asked me, "Anand, if there was one and only one thing that you would do in your software as as a must-have rule?" **It would be make sure that every single reaction or even thought process of the users that are using the software gets logged.** Agents will figure out what to do with it later. The one irreversible thing is the logging of the user reaction at that point of contact. Everything else you can frankly forget because you can derive this, or agents will derive it for you. Yeah.

[84:44] Well, give it a shot with validations. Thank you for listening, and let me know if there's any interesting findings that you have on the verification side. Thank you.

[84:59] The links are available on my website. You just have to do a search for "S Anand" on Google. You'll find me as the, depending on your luck, first or second link.

**Host**: [85:10] [inaudible]

**Anand**: [85:11] Yeah, or ask AI.

**Host**: [85:15] Any questions?

**Audience Member 11**: [85:26] So, one of the things you mentioned is you try to ask the agent to actually so-called interview you. That's one of your techniques. And by logging all those answers, it will help improve the agent quality or accuracy in some sense, right? So, in a way, that assumes the human has certain expertise. So, what's your recommendation or suggestions for fresh graduates or professionals as they enter into this news? Because we tend to—like what you mentioned, we many of us think that the AI is smarter than us, and and there's always a tendency instead of improving in our expertise, we tend to rely to another agent, to another agent, all these kind of stuff.

**Anand**: [86:25] No, very true. Sometimes, or one of the things I've started doing is disintermediating. Meaning, is the software being built for me? If so, I would say interview me. If the software is being built for someone else, I'd say interview them.

[86:44] And the end user is at some level, the ultimate source of truth. Doesn't matter if they know or don't know, it's that set of preferences. So let's take two scenarios.

[86:59] A finance manager says, "I need software." We're talking in the context of software, right? Or A finance manager says, "I need in an invoice reconciliation software." They run a process on invoice reconciliation, and if I ask them what are the things that you would want in the software, they'd be able to at least say, "Look, I don't want this entire thing costing me more than so much. I want to make sure that any invoice that gets reconciled should align to whatever are the government regulations." They'd say half a dozen things which are the ultimate truth.

[87:36] Now, if I if I had asked the agent to interview me, I wouldn't have been able to come up with those rules. So, if I'm not the expert and somebody else is the expert, I would rather interview the expert. But if there is no other expert, if I'm not able to find an expert, then I would ask it, "How do I find an expert?" But if there is no other expert, then my opinion counts as much as anyone else. If I'm the end user, then I'd say, "Look, this is how I feel."

[88:05] And I think that last bit is perhaps the most important. **I don't describe specifications anymore as how to do it. The agent is smarter than me.** I say, "Look, build me something that makes me feel light. At the end of it, I want the experience to be such that I'm not hindered. It doesn't feel like a lot of hard work. It doesn't look like it's too intense." I describe feelings that I want it to evoke and rely on it to do the translation, and have it interview me further to ask what I mean. And sometimes I just tell it, "I don't know."

[88:45] I'm not entirely sure expert if expertise is concretely wordable, it's something agents can learn. And that's how they've been learning so rapidly. Maybe it is the stuff that we can't even express well enough that remains to be expressed, because the rest is reinforceable learning, teachable.

[89:11] In short, when I say interview me, I mean interview whoever is the end user, need not necessarily be me. But if it is interview me, I describe my feelings rather than specify. No idea how what better approaches are. I'm sure there are some. Yes, please.

**Audience Member 12**: [89:38] So, I read one of your blog posts, right, where basically you have this section where things that you have learned for the day, and also questions that you have been asked. And one of the questions that someone asked you was if AI is able to program everything, then should we learn how to program? And your answer to that was let AI do the programming, and we just ideate and come up with ideas. So, let's say all of us in here, right, we apply for the same job, the same job application, and all of us come up with similar outputs, so how do you then differentiate, like, if that day comes, how will someone distinguish amongst everybody?

**Anand**: [90:26] I also teach a course. One of the evaluation criteria that I have for them is **who's most unique?** If everyone's going to come up with the same stuff, that's boring.

[90:38] So, for instance, I had how many students? About yeah, 300-odd students create a picture story. The objective was the story should be an image, no words, and it should be easy to understand, it should be very different, and it should I forget what the third criteria was. So, yeah, let me show you the patterns.

[91:08] So, the plot, each of this is one story. X-axis is how unique it is. Y-axis is how much people liked it. I also had them rate the stories, which do you like more or less, and people rated it. Look at the stories people totally loved. So that's a dog that's been adopted by a little girl. Okay. Dog adopted by a little boy that saves him. Dog adopted by a little boy. Dog adopted by a big boy.

[91:47] I am not going to hire any of you. What kind of a joke is this? Another pattern of story was, okay, crow puts pebbles into the bowl and drinks the water. Sure I saw another one of those. Okay, this is bird as a pet, but I saw the crow story again somewhere. Yeah, one of That's another classic pattern.

[92:11] In contrast, there are some fairly unique stories. So, this was well, the story of the Bhagavad Gita, okay, unique in the sense that nobody else thought of it, but it's a story that resonated with a lot of people. Or this was an interesting story where businessman bribes a policeman, but shooes away a beggar, but the businessmen are just happily giving money to a politician who probably doesn't need it. Very interesting satire. We thought it was quite different, quite unique. Or this one about a girl that's receiving a gift, which she says, "Oh, I love it," but in reality, she absolutely doesn't want that.

[92:55] These are different stories. These are whom I'd hire. Meaning, getting something done is not a big deal. AI can draw, you can draw. AI can probably draw better than you. I'm not looking for the drawing capability. AI can code, you can code. I'm not looking for the coding capability. **What did you decide to draw? What did you decide to code? That's what I want.**

[93:23] Put another way, if AI can do it, that's not what I'm hiring you for. That's not what I'm going to be testing you for.

[93:33] Did that No, it clearly didn't answer your question by the look on your face, but no, no, do go on.

**Audience Member 12**: [93:39] No, yeah, it did.

**Anand**: [93:40] Okay. Then you're probably pondering the implications. Well, let's talk about the implications. To me, there's only one implication that I personally follow, which is the answer to the question: **what skills should I learn in the AI era? My rule of thumb is this: learn what AI cannot do.**

[94:03] AI does a lot of stuff well. Therefore, I will delegate everything to AI, which means that it will goof up sometimes. I will know where it goofs up. That's the part I will do. Therefore, I will learn only the things that AI is at least currently not able to do.

[94:20] It's an easy way of building the skills, but the prerequisite is delegating maximally. Everything goes through AI, because that's when I will know what it cannot do. And I have a point of view based on that on what skills are probably not going to go away in the near future, which is this list. But that's derivable. The intuition there is delegate maximally, do what AI fails, and absolutely do not bother learning what AI can do or will very likely do in the future.

[94:58] There's a short-term need for it because interviews still depend on things that AI does well, as you saw in the very first interview that I had. But it's not a durable skill, I think, because there are enough things that AI cannot do or will not do that are still worth learning, and we may as well spend time there.

[95:19] I know we are out of time, but was there any pressing last question that anyone had? Okay, we can wrap up then.

**Host**: [95:41] Thank you, Anand.

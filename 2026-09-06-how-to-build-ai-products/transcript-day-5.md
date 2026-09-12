# Transcript

**Anand**: [00:18] Alright, shall we get started? Are we okay to get started? Cool. So, firstly, thank you for sharing. I think most of you had been able to put in your chat log links as well as the learning videos and the product videos. I will be going through this in some detail. What we're going to do today is partly wrap up the learnings but also look at what it takes to continuously be able to improve products. First, let me give you a summary of what we've done so far.

**Anand**: [01:13] **What I've been walking you through is roughly the equivalent of the StraiveX methodology that we're using at Straive to build products.** The new way of building products is somewhat different from the old way. Earlier, we would prospect—that is, we ask questions. Now, we don't need to ask questions because we can just scan the data that is available and automatically get a sense of what products need to be built, what are some of the use cases that we need. In this particular case, we didn't really have much data to scan, but what you were doing was just mining your experience, your gut feel. But you might remember that in the first session, I showed you a list of about 150 products that Straive might want to build. That came out of scanning all of the data that I had on my machine as well as on Google Drive, etc. So, that's one part of it: how do you identify?

**Anand**: [02:37] The next part was, earlier, people would propose a solution. They tell somebody, "I can build this product in three months, three years, three weeks," whatever. **Now, it's come down to three hours. So you don't really need to propose, you just go ahead and actually build it or forge the solution.** There is no intermediate step of approval that's required. In fact, you were building multiple solutions, not even just one product, changing it midway.

**Anand**: [03:19] A third step used to be the formal build process that would take a lot of interaction with the clients, but you inverted that, meaning you built first and then took it to a few people and said, "What do you think? Give me the feedback." That brings us to the validation stage. Now you've completed that as well. And then we used to deliver the solution to the client. **Today, we would just deploy and scale directly.** One of the ways you were exploring that was, "Is it possible for me to create a video that will explain what the product does? Is it possible for me to publish it on some page so that others can use it?" And we'll probably go a little more into other ways in which you can use AI in this stage.

**Anand**: [04:22] **Today will largely be about the 'Run and Evolve' stage. Earlier, products used to be maintained by hand.** We would check with people: "Is it working fine? Are there any bugs? Do you need any new features?" Today, we can have the agents automatically monitor how people are using it, what's working well, what's not working well, and use that to build and evolve the next generation of products. And this cycle goes through iteratively, meaning once you have the evolved version of the process, you can use that data to sense whether there is a new product that is required, or even just a new feature that is required, and start the iteration all over again. So product development is not something that you end with one cycle; it's something that you keep running. It's something that's now faster because of AI; it's also something that is, I guess, easier—maybe. It's different, so it's confusing, but it ends up making the current cycle of products much easier.

**Anand**: [05:51] So, this is the bulk of the cycle. But one of the things that it delivers as a byproduct, those are assets. Meaning we're doing some work, and from that work, we learn something that we can reuse the next time, or even other people can reuse the next time. What are things that you may have done that could possibly be reused? Well, one of the possibilities is you've started capturing logs of how people are using the application. That is something that when you or someone else builds the next version of the application, could help minimize errors. Or even let's take the session logs that you were sharing where you were giving prompts. That is something that we could collectively learn from each other and find out if there are any best practices for using those session logs.

**Anand**: [07:11] Let's try that. What we're going to do now is the asset creation process. Let me just see... Okay, so these session... Okay, I started downloading the session logs a short while ago. Something's wrong, I'm not able to click... Okay. For each of you, I have your... Okay, the chat logs are not yet created. They are getting downloaded. Are the chat logs for anyone downloaded yet? Not yet. Okay, fine. Let's just do this manually. So we have the chat logs shared here. They're taking a long time to load. Let's load a Claude chat log. Oh, this is perhaps not a chat log... There's [word?] a post of three pages? Okay, it might be the wrong link. Let's take the next one. Okay, yeah, this looks like the chat log. This looks like a chat log. Yeah, this is a copy of the chat transcript. Let's open this and this and this. And there are a couple of links here. This looks like it's opening. And two chat links.

**Anand**: [08:48] Okay, so then let's do this. Let's kick off a learning exercise from these chats. Here's what I'm going to suggest. The sheet above has a column which has the chat logs that students have used to create the applications. **What are patterns of prompting that have worked well? What are patterns of prompting that have not worked so well?** And what can we learn based on the effectiveness of these prompts and how the agents have executed and interpreted them?

**Anand**: [09:40] **What I'd like you to do is create maybe the top five most prioritized lessons that could be used as a meta-prompt.** That is, I want a prompt that has up to five prioritized rules that I can just copy-paste before creating any new application, and it should automatically make sure that I avoid these kinds of mistakes, or anyone who uses this can avoid the kinds of mistakes that were made in this application or development process, or automatically leverages the best practices that were visible across these. **Don't put in things that agents would already know or people would already know; put in what is unusual about this.** That's specifically what I want you to hunt for.

**Anand**: [10:31] Feel free to use local MCP, and these are already open as tabs on my browser, so you can inspect the browser tabs and get the results if you wish. So in this particular case, what I've also done is given it access to my system and specifically the browser, so it should be able to pick up the tabs even if it's not directly able to visit ChatGPT. Now, you'll notice that I'm specifically asking for something that can be added to other prompts. **And this is conventionally called a skill.** Let me just make one change here... Okay, we'll let it run. This could possibly take half an hour, so but we'll still let it go.

**Anand**: [11:34] Since I'm asking for a prompt that can be used with other prompts, we can blindly take it and just automatically apply it, meaning give it to a whole team and say, "Here are five mistakes or five best practices people usually forget, so always add this to your prompt." And at least that set of mistakes will no longer happen. This is an example of one kind of asset that we can create, which I would call a skill—meaning something that you can automatically add, and there are ways of automatically adding skills to your programs.

**Anand**: [12:15] Another kind would be hooks. A hook is where you tell it, for example, every time I ask for a feature, always write test cases. That may not be such a good idea. Maybe always commit it to a GitHub repository. So that way, your code will constantly be versioned. **The difference between a skill and a hook is a skill is where you tell it to do something and 99% of the time it will do it. A hook is where during the development process you tell it you must do this, and it'll actually do it programmatically. It won't make a mistake.** You don't need to worry about the hooks part of it, that and most of the other things are fairly detailed.

**Anand**: [13:09] But what you'll need to remember is that just getting to a product is only a part of the exercise. I mean, that's almost a starting point. What you would usually want is once you've gotten there, take as much as you can out of it as assets that you can use and reuse repeatedly. So now you can see that it's going through my browser. The browser will probably not be usable for some time, but in any case, I've covered the first part of what I wanted to do.

**Anand**: [13:46] **So what should you do based on this? Analyze your own chats.** Go through Codex, Claude, ChatGPT, etc., and tell it, "Look at what are the things that I'm doing well, what are the things that I'm not doing well." And it's not what you're doing well or not well either; it's also, based on what I say, "What are things that you do well and things that you don't do well? Is there something that you can do to make sure that these problems don't happen again?" **Even if I don't tell you, can you figure out a way of making sure that those problems don't recur?** is something that you can try as part of your self-improvement or evolve process. That is mostly the 'Run and Evolve'.

**Anand**: [14:36] Now, the next thing that I'm going to go into is let's see how well we've done as part of this exercise—effectively the evaluation part of this course. And you will have a say in the evaluation. Now, in order to do this, I'm actually going to use the same process that we followed. Effectively, I'm going to have the system look at what we've covered as part of this course, think about what you should be learning, and see if as part of all of these submissions, you have demonstrated learning those concepts. **In other words, we're going to use AI for the evaluation as well, and each of you will be getting scores and feedbacks based on what the agent has suggested.**

**Anand**: [15:28] But this is something that I would like to allow you inputs into. That is, you can shape the process; you can hack the process, if you wish. And we will use that today to identify how well each of us have done, where we need to do better, etc. To do this, I have given the system the following prompt. I said, "Go through all the course content. Local MCP's my machine and this is the directory where I have all of the course material: the transcripts for our discussions, your submissions, etc." I've also told it where the form submissions you have made are; I've pointed it to the Google Sheet where you've been adding your entries, etc.

**Anand**: [16:21] Now, here is the interesting part. I'm saying, "Based on what I'm teaching the students and what I believe to be important in the AI era..." I've had a lot of conversations with ChatGPT, Claude, etc., and I've saved it on my machine, and I have a point of view on what people should be learning when AI and agents are so powerful. So it can access that. I'm telling it to access that. "How should I evaluate the students and their submissions?" I'm not sure. I may have some points of view; it may have some points of view. But the information that's available to it certainly is more than anything that I can probably think of at the spur of the moment.

**Anand**: [17:01] So I've told it, "Go fetch all the information, all the submissions, and identify the evaluation criteria. These should be a prompt that I can just give an agent." So you put in all your submissions; I will have the agent then go through your submissions, convert the videos to audio, look at the transcript, take snapshots of the videos if required, go through the chat logs, see how you've worked on those applications, analyze the applications themselves—whatever—and use that information to do the evaluation.

**Anand**: [17:40] So it's thought through, and it's saying here are the criteria that we should be looking at. There's:
1. **Are you able to pick a good problem?** And that obviously requires a certain amount of judgment; that's reasonably important.
2. **Are you able to ship something, and not just an easy thing, something that's relatively hard?** That's again reasonably important.
3. **Do you have real user evidence and evidence-driven iteration?** Taking inputs from people, but also changing the product in line with those inputs.
4. **Are you able to verify that the product works well and in a way that is demonstrably trustworthy?** Again, fairly important. These two are—just evidence and evaluation are probably the most important criteria.
5. **Are you able to use AI as part of the whole process well? Are you able to learn from your failures?**
6. **Accountability, limits, and real-world judgment.** Yes, being ambitious, but also recognizing that certain things just won't be possible and stopping ourselves, making sure that we don't create something that we can get into a lawsuit for. Those are elements that you need to exercise some judgment on.
7. **And communication and evidence legibility.**

**Anand**: [19:02] Those are what it suggests as the criteria for evaluation. That looks reasonable to me. But what I'm going to do is make a small application out of this right now where you will be able to comment on these criteria. And you may choose to comment saying, "No, I think we should add a different criteria; we should remove this criterion; we should change the weightages this way." "When looking at this particular criterion, you should maybe pay more attention to this, pay less attention to this." Up to you. You can suggest.

**Anand**: [19:42] **What I'm going to do is build an application that will take all the feedback and it'll give you a response saying, "I think I should take this feedback, I won't take this part of the feedback," etc.** In other words, the evaluation of this course itself is something that you can shape. And that is part of, well, yeah, a little bit of your exercise today, which is: can you actually get this evaluation—can you improve the evaluation for everyone and can you improve the evaluation for yourself as well?

**Anand**: [20:17] This is the final prompt that it has created. What I'm going to do is build an application that has a copy of this particular prompt and allows you to log in and make changes to this. Yeah, of course, this might require you to have a ChatGPT account, but a free ChatGPT account will work just fine even if you have a Claude paid account instead of ChatGPT. So that's something that we're going to do in a short while. I'm just checking if it's managed to... Okay, it's still getting all the evidence.

**Anand**: [21:09] Right, okay. Let's—no, actually, even before I come to this, I'm going to kickstart the other application. Let's run this. Let me download this as a markdown document and let's do the following. I'm going to set up a work session. Small/medium is fine.

**Anand**: [21:49] I would like you to build an application that allows students to submit their suggestions for changes to the evaluation prompt that I have uploaded. Allow the students to share their inputs as a text field with as many details as they would like, and save that. Allow each student to edit their own responses and they can also submit multiple feedback items.

**Anand**: [22:30] If possible, share thoughts on how appropriate or useful it would be to incorporate the entire feedback or change to the evaluation process, either in part or in full. This response may help the student revise their suggestions or add new suggestions. What I will be doing is either at the end of the day or over the weekend, take all of the feedback, run it against my point of view on how evaluations should be run, and change the prompt accordingly, and then finally run the prompt. Feel free to use all course-related material, past conversations, and any other information that you need to build this application, and deploy it on sites.

**Anand**: [23:35] Let's give that a shot. The file that I should... Okay, the prompt itself is in local MCP. The file... And the file name is evaluation_prompt. Other relevant content is directory_above on local MCP and in past chats, and right, figure it out. I'm sure I'm forgetting... Yeah. local MCP won't be live while the app is running, so make sure the app has all it needs in terms of context. But the app may use ChatGPT to respond using the relevant context.

**Anand**: [25:00] Yep, fingers crossed and let's get the evaluation application running. Now, let's go back to what we can learn from your prompts. The first one is a very interesting one. **Treat my proposed solution as a hypothesis, not a specification.** This may be one of the most important prompt suggestions. Very often when we ask for something, we don't ask very well. We don't know how to ask good questions; we don't know how to give good instructions. And models have been trained to follow instructions very carefully. If you say something, "I will do exactly that," because if it does something else when you know what you want, it's doing the wrong thing.

**Anand**: [26:13] But for something as abstract, as big as products, it's sometimes important to tell agents, "I'm telling you something, but maybe you have a better idea. Why don't you try that?" This particular statement is one of my most used skills. I have a skill called 'refame question'. And invariably, in almost all of my prompts, I put in exactly this, and it's basically saying that what I ask may not be exactly my real need. **Think of it as a hypothesis, as an approximation, as a guess. It's a rough draft of my real need.** Which means you're telling the agent, "It's okay, even though I ask for X, it's okay to give me Y, something close, but do a good job." And it looks like that is something in across many of the prompts—not something; it's probably the most important thing that you're realizing. You may have tried something, it gives a result, and then you change it say, "Oh no, that's not exactly what I wanted," or "Can you do it better?" And by allowing this prompt fragment, we are enhancing the result. Any questions on anything we've covered so far? I should pause here.

**Anand**: [27:48] Second is, **prove the riskiest assumption end-to-end before polishing anything.** Some of you have struggled with rewriting applications. You take it in a certain direction three or four steps, and then you find that changing it becomes hard. Should you rewrite it from scratch? Now, if that's the case, it's probably good to test the most important things to see if this direction will work in the first place before carefully fine-tuning the application. A useful premise. This is not something that I have in my list of skills, but is something that I'm learning now—which, oh yeah, I knew this, but I never told my agents this. So this is a skill that I'm planning to now add to my list of skills, so in other words, it will automatically pick up this rule and try and find out what's the riskiest assumption, validate that first.

**Anand**: [28:46] **When something fails, trace before you tweak.** In other words, I think many of you are saying, "Okay, this failed, so change this." But was that the right thing to change? Maybe you need to analyze first: why did this fail? And then suggest a change. It's highlighting that that is one of the gaps in your prompting process. Fair enough.

**Anand**: [29:16] **Never blur reality and simulation.** Hmm. Okay. Sometimes when the agent creates dummy or sample data, or you ask the agent to create sample data, it gets presented as if it's real data. That can be confusing for some of the audience. It should be labeled clearly. Fair point.

**Anand**: [29:50] **Treat feedback as a reason to reintegrate, not merely to add.** That is, translate each feedback into... [cut off]

**Anand**: [30:01] ...feedback into the behavior and desired outcome. Oh, okay. So when some of the users give a feedback saying, "Maybe I could do this," or "Maybe it'll be good to implement a new feature," what many of your prompts are doing is just taking that request and saying, "Add this feature." But that feature may just be a part of how the user feels. For example, if at some point the user said, "The application is not clear to me, what does this button do?" Your prompt may be "Explain what this button does," but there may be 20 buttons that they don't understand.

**Anand**: [31:03] So the reason why they're saying they didn't understand this button is because the application overall is not clear. So your prompt should probably be **"Make the application clearer overall, not just that one button."** So look at the reason to reintegrate, just don't take the feature and add it.

**Anand**: [31:26] In other words, across all of your prompts, these were the top five improvements that could be made. For each of you individually, maybe this is not something that happened in your prompts, but remember two things. Number one, in the future, this is a mistake that you might make. Three of these are mistakes that I invariably make, and one of them I already have a skill for, two of them I don't, so I'm going to add these.

**Anand**: [32:00] Secondly, even if you don't make these mistakes, it's important for you to be aware of these because your teammates will make these mistakes and you should be in a position to share, look at some of their prompts—ideally automatically—and say, "Maybe you should be prompting in a slightly different way."

**Anand**: [32:18] But the meta-lesson is **you can learn from logs. Make sure you have logs.** Make sure you can get access to other people's logs to see how they're doing something that's interesting, share your logs so that other people can learn from your process. **Earlier we used to open source code; now it makes sense to open source prompts, the logs, because that's where the work happens.** That's what actually ends up creating the product. And these, the derived work items from this, get translated into skills effectively.

**Anand**: [32:54] Let's see if this application has been built. Okay, still running. We'll give it some time. Now, here's something that I'm going to do. I will share this link on the same Google Sheet and I'd like you to try one exercise. I'm going to put this under Column B and actually, no, I'm going to create a new sheet for this on Sheet 2. This comes under "Prompting Lessons." "Name" and "Link" for now would suffice.

**Anand**: [34:01] **Take the prompt from these prompting lessons and apply that to your chat sessions.** Ask it, when copy the whole thing, paste it into your chat sessions and ask it the question, "Which of these was most prominent in my chats?" See if you can give that a shot. Meaning which of these did you make—or actually no, let's do this. I think some of you may find it easier to do this offline, so you can treat this as an offline exercise and do this later in the day. We can just focus today's class on execution.

**Anand**: [34:57] Okay, this is still running. It's going to take a few minutes. It's 10:36. Today's session may end up being a much shorter session because some of what I was hoping to cover in the class you've already completed, some of which we will post offline. But any questions from anyone?

**Unsure**: [35:27] Are the mistakes that we're making for each prompt universal to be applied on every AI language model, or are they catered to only specific ones that have perhaps a higher sensitivity to users?

**Anand**: [35:51] Fair point. So, are the mistakes we make on prompts or the list of suggestions that it's provided—are these universal or are they related to specific agents? There are two parts to specific agents. It could be that it applies more for Claude, less for ChatGPT, or vice versa. It could be that it works today for Claude, but not a year later, or even a month later, because new models have come in or new agents have come in. It's also not necessarily model-specific. It could be that if I use Codex with GPT 5.6-soul, I need this prompt, but when I use it with, let's say, DeepSeek V4 Flash, I don't need the prompt because that model does not make this kind of mistake. Possible.

**Anand**: [36:53] **In short, I would say that every prompt suggestion has a lifetime.** It's relevant in that particular context. But it's not just the agent or the harness that is changing; we are changing as well. And over time, we may have absorbed certain learnings. We won't make that kind of mistake again, so there's no point telling it over and over again, right? So what do we do? Do we say only for this model use this prompt, only for that model use this prompt? **Short answer is: test.** I don't know, and there is no universal answer. That precisely is your question: is there a universal answer? No. So what do we do? There isn't any universal answer for what do we do either, so test.

**Anand**: [37:49] The follow-up question that you would ask on this is: do some of these occur more often for people who are using Claude versus ChatGPT? Is there a big difference? Worth asking that question. Let's do that.

**Anand**: [38:02] Is there a big difference in the applicability of some of these prompting lessons to those who are using Claude versus those who are using ChatGPT? Even if there is a clear indicative directional difference, let me know. It doesn't matter if it's not statistically significant; it's not like we have a large number of data points. But do share the clearest signals that you find and tell me how confident you are. Based on this, I might take some of these separately and say use these prompting lessons primarily when working with Claude. However, don't try to invent a signal when there is none. If there isn't a major difference and it really seems to be all over, then just say so. That's fine. Yeah, let that run its next iteration.

**Anand**: [38:58] But short answer, in my experience, prompting tips are generally cross-model. **They're more a function of how we prompt than how the model responds. So they're more to protect human mistakes than model mistakes or harness mistakes.** Any other questions?

**Unsure**: [39:40] Will you be sharing the app for the one that we just discussed?

**Anand**: [39:48] Oh, that is already on the sheet in Sheet 2. And we do have a difference. It's reasonably confident that the "tracing failure end-to-end" is more important for Claude sessions and "proving the riskiest assumption before polishing" is more important for the Claude sessions. But I'm not sure if that's because people using Claude tend to prompt this way or Claude itself tends to make these mistakes. I wouldn't decide just yet.

**Anand**: [40:48] Okay, this app is taking longer than I would have expected. Let's see if there's a small detour that I can run. Okay, we've covered all of these. Let us see if it's downloaded all of the... yeah, it's managed to download all the submissions.

**Anand**: [41:13] Here's something else that I am curious about, which is: each of you have shared videos with your learnings from the process. **What can we collectively learn from our learnings of the process so far?** That's another kind of asset that we can create, right? Let's do that.

**Anand**: [41:37] Students have shared their learnings as part of the process. I'd like you to go through this and identify the top learnings that have high impact and high frequency and sort based on that. Roughly give me the top five learnings across the students based on impact and frequency.

**Anand**: [42:13] Let's give that a shot. And in this, you'll notice that these are two things that we got out of the work that you've been doing. One: how can we improve prompts? Two: what are we learning? But these are just two things that I happened to think of, right? When you think about it, we have effectively a dataset. We have a spreadsheet; behind the spreadsheet are a whole series of links, each of which points to feedback transcripts, video recordings, all kinds of stuff. So that's a dataset.

**Anand**: [42:51] And I mentioned earlier that **one of the things that we can do is, rather than prospecting—trying to find out what we can do with material like this—we can actually sense. That is, use agents to find out what kinds of assets we can mine from this.** So maybe we can create a new educational product out of just the data that you have created, right? Let's see. Let's see if that's even possible. So I'm going to start another branch. Let's branch here.

**Anand**: [43:41] Okay, it looks like we have some interesting data here. One of the things that I've already done is had ChatGPT scan all of this material and identify what are the top prompting lessons that students can take based on their own sessions. A second session that's currently running is: what are the top lessons overall that students have learned, prioritized based on impact and frequency? Now, these are a couple of, let's say, meta-assets or reusable assets that ended up coming from this data.

**Anand**: [44:21] I'd like you to ideate and brainstorm and think about: **what are the other most promising assets that we can build out of this?** In fact, if... and I'm just thinking aloud here, we treat this as two objectives. One: the students should be able to learn based on each other's work as much as possible. That's one objective. Second: in the future, if we want to create a new product out of it, then we should have some interesting assets that could serve as evidence or starting points for that. So yeah, brainstorm and give me the most novel as well as impactful ideas so that I can execute them one by one.

**Anand**: [45:03] And with that prompt, let's see what it does. It's still identifying the learnings. Oh, okay. So what are the top things that we have learned as a class?

1. **AI can do much of the execution, and the human judgment is becoming the bottleneck.** It's interesting that about seven to eight people out of the nine who have shared feedback have mentioned this. And that was because you had to decide what's right, what's useful, what's worth prioritizing, what's trustworthy. Yeah, I would without doubt say that with any kind of AI usage, this should be the most important lesson.
2. **AI dramatically lowers the barrier to build software.** Again, seven out of nine have explicitly mentioned this. The change is not "Can I implement this?" but "Can I tell it what to do? Can I see the output, verify the output, and can I improve it?"
3. **Clear purpose and specific instructions matter more than vague prompting.** This struck me as interesting because this is not something I do. You've seen me prompt very vaguely; I use my prompts as a way of narrowing it down. But what you're discovering—and I'm sure this is also true, it's your learning as well—is that **when you give it specific prompts, you are getting better results.** Which is great and ambiguity caused assumptions, loops, and repeated correction. Yes, please do take this lesson. But please also consider the opposite lesson: that the loops, those repeated corrections, that effort may also be teaching you something that may be worth learning. It's okay to be ambiguous when you don't know what you want. Don't force specificity; that can also take you down a wrong direction. But good lesson.
4. **Real-world constraints should change the product, not merely be worked around.** Okay, six of you. Okay, API costs, model limits, deployment restrictions, unreliable GPS, security, deadlines... and because of these practical considerations, you decided to change features, make it simple, postpone some of the features. Yeah, a very practical resolution. But also what that means is sometimes when you plan something, you may plan 10 things; six, five of those are possible. You should know beforehand which of those are possible, otherwise you will be wasting time. And that I think is exactly why this particular lesson is important, this prompt: **prove the riskiest assumption.** So unless you know what's possible and what's not possible up front, it's going to make it harder.
5. **Real users expose problems that AI and the builder do not see.** So it is useful to check with humans because the agents are not providing that kind of input. Yep, yeah, confusing UI, unclear buttons... these are exactly the kinds of things, an emotional reaction... yeah, these are exactly the kinds of things that humans catch and AI does not, because it doesn't get confused. It understands this sort of thing pretty well. Which is useful.

**Anand**: [48:57] Okay, it's suggesting a few products that I could build. We will come back to this in a while. Hmm, oh okay. Oh, this is an interesting one. **All of you used agents to check your product. You also used humans to check your product. What's the difference between these?** That's a pretty powerful and interesting learning.

**Anand**: [49:30] So yeah, I'm really interested in the synthetic users versus real users prediction differences. So yes, please go ahead, compare the two and let me know what the top takeaways are. Be specific and give me examples of these differences to help understand what exactly the nature of the difference was. And also try and generalize it so that this can be a reusable lesson that we apply not just to building products with AI, but to any AI-based activity that involves user validations.

**Anand**: [50:12] And let's progress. This process at the end of a project or a product development sprint is a **post-mortem.** And traditionally post-mortems are about looking back at what we did the week, the month, the quarter, whatever, or the product release, and asking ourselves: what did we do well? What did we not do well? What should we continue? What should we stop? And how do we document this in a way that in the future we don't repeat the same kinds of mistakes?

**Anand**: [50:47] What we're doing now is effectively a post-mortem. But because we have agents to support us, we have two dimensions of post-mortems that are coming out. One: the agents are able to do the post-mortems and tell us what to do. The agents are also able to tell us what kinds of post-mortems to do, which it gave a list of. Of course, they're also able to capture these and put them into documentation that they can reuse. So even the execution of this is something that we can delegate. **The specification—telling it, "Look, I do want a post-mortem, I do want reusable assets"—that's the skill that you retain, and that's exactly what you have collectively learned as a lesson.**

**Anand**: [51:30] All right, finally, the application is live. `SUTD Prompt Evaluation Prompt Lab`. And I will share this. Okay, anyone with the link already has access. Let me... I will be sharing the link in a minute, but let me just check what the application does in the first place.

**Anand**: [52:01] Okay, so it lets you read the current prompt. This is the prompt; I'm sure it can be presented in a better way. But if I had to provide feedback to the prompt... let's see. "Isn't this too complicated for a student to understand? Can we have a simpler evaluation mechanism or rubric?" And submit that. So if I submit it, let's see. It's giving me some feedback. "Concern may matter, but the exact scoring or rubric change is not clear." Okay, so it's telling me, "Look, Anand, it's fine if you want to change it this way, but what exactly are you proposing? That's not clear." And okay, I am not giving it any evidence to say that the prompt is not a good one. So it's saying maybe I could make the revision so that I can explicitly provide both why it helps and what's the evidence to change. Which is a reasonable feedback. If I had thought it through, I would have asked it to make that change. So maybe I can go back, make a change here, and save it, and so on.

**Anand**: [53:37] This I will add to the sheet. Okay, let's just say "Task: Apply prompting lessons to your own prompts." That's one. "Share feedback to improve evaluation prompt." And that is the link. We're going to pause here for maybe a 10-minute break, at least. I'll invite you to try certainly the second link, which is on Sheet 2 of the same workbook. And go through the prompt... actually, we'll probably need 15 minutes for this. So fine, go through the prompt and see how the evaluation should possibly improve. **Try and give yourselves an evaluation that will give you as many marks as possible. Feel free, hack it.** 10:56, maybe we will resume at 11:10. Help yourself to refreshments.

**Anand**: [55:01] Okay, it's time we get back to the class. What we're going to be doing towards the end is having you come over and present your applications. I would actually like to invite to begin with maybe... let's see... we'll start with **Yuri** for the **Study Walker**. Yuri's not around? Oh, sorry. Hi, Yuri. Hi. I was hoping that you could come over and explain the Study Walker application, Yuri. And followed by **Kosei** for the **Shot Atlas** application. If you could just come over and explain what you built. Feel free to use Japanese if you prefer explaining that, and that's absolutely fine. Followed by **Miku**. Miku, if you could share your **Roam** application, just come in, talk for two minutes on what the application does. **Nanami**, if you could again take your... your application was the fishing, the **Kanto Fishing Map**. And if you could just talk through that, that'll be really wonderful. **Johan**, if you could walk through the **Jurnal Lentera Bursa** as well. Depending on how much time we have for the rest of the day, I'll call on people as we go along.

**Anand**: [56:36] But yeah, no, let's dive right in. What I'd like each of us to do firstly is as we listen to the application, get a sense of the functionality of the application, but also the process that went in into building the application. So, Yuri, over to you for the Study Walker, please.

**Yuri**: [57:14] So, hi, I'm Yuri. I speak only... okay. And can I share my demo?

**Anand**: [57:26] Yeah, or if you think it's easier for you to present, that's fine.

**Yuri**: [57:29] Okay. But I cannot... I cannot speak moving PC together.

**Anand**: [57:40] Sure, I can move if you tell me. No, however you want. Your choice.

**Yuri**: [57:47] I will do my best. Yes. Hello, I made it with Codex. This app is Study Walker. **It helps people to have a goal but do not know how to begin.** The main purpose is to help the users take one small action today. Today is very important, I think. First, I enter what I want to do. Sorry, this is not personal... yes. I said I want to get started... I create a game. Game? Game. And I put this button and the app advises where I am trying to start. I have not started yet, so I will choose this option.

**Yuri**: [60:01] And next, I choose how much time I have. Now, I'm speaking so I choose three minutes. And finally, I choose what I can use now. Now, I have a laptop and computer only, so I choose PC.

**Yuri**: [60:27] Study Walker now gives me one specific action here. And it shows and it shows what to try today. And under this sentence is [inaudible] blue [word?]. It is being here and it shows what to prepare. A PC and browser, so I can do now.

**Yuri**: [61:13] And sorry... and this is how much time it takes. And on the right side, the instructions are shown in the order I should follow them. Now I can understand what I have to do. So, and because I'm a complete beginner, the app gives me specific search words. And sorry... okay. Next page.

**Yuri**: [61:57] Oh, okay. If I push that button, the page opens next, another page. Yeah, that's CodePen, this one. Oh, okay, okay. It's not a good case. Okay.

**Yuri**: [62:32] If you are a beginner, if you are a beginner, this app shows what you can understand, how you have to search. But if you are a beginner, you do not know what the way I start this action. So the app shows you what word you have to search, what word you can access the website, how you start the action. Yeah, and sorry.

**Yuri**: [63:44] And so now I can... and so in this case, first just... in this case, on this page, I can record the first two things I tried. Open the necessary pages and tools. Yes, I can, so I choose. And open CodePen and find the field to write HTML. Yeah, I can find where I have to do, I have to write, so I check this. And you can leave behind what you noticed around the ways, so you can memo what do you think and others. So, but it is optional. Optional. So you can write, but you don't have to write. Yeah.

**Yuri**: [65:10] Oh, sorry. Okay. And as a result, after trying the action, I record how far I progressed. In this example, I completed first action so I choose. And my button... sure. And I completed the first action, so I put the button on the next page. And this app shows this page. And it is final page of this app. And if you want to know what I will do tomorrow, you push here and it shows. And but this is optional. So only one... it's not must. Yeah, it's not must.

**Yuri**: [67:01] And it's final page so... no. And if you want to start another action, you put "Start a different goal" and you can start the same way. And so this is Study Walker that I built past five days. Thank you. Thank you for watching and sorry for my English.

**Anand**: [67:50] No, that was very helpful, Yuri. Thank you. And part of the reason I wanted to use this app as an example was: **functionally, it's not a very complicated application. But the execution is something that is now compressed dramatically.** Yuri's able to do this in one day. In fact, the rest of it was just improving the app from the time from when the idea emerged to the execution is one day. And if things are so easy, then there are so many small little things that are useful to us that we can start building. This was actually useful for me because I, when I tried it on the second day was it, or perhaps the third day, I learned a little bit of Rust because of that. That's something that I've been wanting to do but I've postponed for almost two years now. Small little things, but the execution makes it powerful. Kosei, could we walk through the Shot Atlas?

**Kosei**: [69:12] Good morning. Good morning. I created this site and this site is the Shot Atlas and it shows relationship between shot location and scoring probability. And you can choose open play or set pieces and penalty. And this map shows goals by shot situation such as pass or cross and ball recovery and so on.

**Kosei**: [70:15] And second, this map shows compare the two situations. Left side is first half, right side is second half. Information of this... [Japanese] この黒いバーはシュートの位置からゴールまでを表します。
[Translation: **This black bar represents the distance from the shot position to the goal.**]

**Kosei**: [71:13] And this map shows the species [types] of shots. For example, from corner and penalty and direct free kick. [Japanese] この点の大きさ... 赤とか青とか黄色は得点の違いの... 違いを示しています。
[Translation: **The size of these dots... red, blue, or yellow indicate the difference in scoring.**]
Red indicates high probability and yellow is not high. Yeah, that's all. Thank you.

**Anand**: [72:35] Thank you. Part of why I wanted to take a closer look at this application is: **because it shows evidence directly in the application—it's data-driven by itself—the verification becomes very easy.** People don't need to ask, "Why should I trust the application?" They can just click and see the numbers for themselves and that's pretty powerful.

**Anand**: [72:57] On the other hand, presenting data is only a starting point. **The next step then becomes: how can I use it for decision making?** What should a coach do because of that? Should they have more players standing in a particular position? Should we try and teach people to avoid something like this? Does that actually work? It leads to a whole series of new questions which the application doesn't yet answer, and that's okay; it provides a platform for it to go to the next stage, which is pretty powerful. Let's go on to the next one. Miku, Roam was yours. Yes, please.

**Miku**: [74:45] Thank you. My name is Miku. This application lets you record your trip with some photos. I actually love travel around, so I wanted an application that could help me quickly record my memories while I'm traveling. So, yeah, let me show you how it works.

**Miku**: [75:29] This time, I will record some of my experiences at SUTD. So, "Start a Trip." And "Trip Name" is SUTD, right? And destination is Singapore. Singapore, and destination is Singapore. Start date is September 6th. "Start of my trip" and [inaudible] names. Next, I record my journey and status. I'm still nervous to speak English to you. Destination is SUTD. Record.

**Miku**: [76:59] If you want, you can put some photos. But this is SUTD's PC so try again. If you want, I can do this. Next, "Add an Action." I can add more records of your trip. If you add more records, you will again put some more and photos and put destination, you can add more records of your trip. And if you view the whole trip, go back home, the trip is saved in under here. And if you put here, the record journey is shown again. That's all. It's so simple. Thank you.

**Anand**: [78:22] Thank you, Miku. What's notable here is not just the app, but the process Miku followed. **The first iteration was a slightly different application. It was trying to use the GPS coordinates to see if we can locate where we are and log memories. Now, after multiple iterations, Miku found that that just wasn't happening technically; technical issues. And she changed direction and said, "Let me instead build a memories-based application."**

**Anand**: [78:56] And I think this is important. **Sometimes we go in a certain direction and it just doesn't work out. It's okay, we pivot. And because AI makes the cost of creation very easy, it's easy to build something new. It's also easy to throw something old away.** It didn't take much effort in the first place. Iterations are a pretty powerful thing. Okay, let's go on to Nanami, who had built this one. Yes. English version, Japanese version?

**Nanami**: [79:29] I'll speak in Japanese, so please translate it into English.

**Anand**: [79:37] Okay, so here should we translate to English? English. Perfect, thank you. All yours.

**Nanami**: [79:48] [Japanese] 今から日本語で話すので、英語にしてください。
[Translation: I'm going to speak in Japanese now, so please translate it into English.]
[Japanese] こんにちは。
[Translation: Hello.]

**Nanami**: [80:06] [Japanese] 私は東京周辺の、関東エリアという場所の釣り場についてのサイトを作りました。
[Translation: **I created a site about fishing spots in the Kanto area near Tokyo.**]

**Nanami**: [80:18] [Japanese] 作った理由として、私のお父さんが釣りが好きで、そういうお父さんに使ってもらえるようなサイトを作りたいと思って作りました。
[Translation: **The reason I made it is my dad likes fishing. I wanted to create a site someone like my dad could use and enjoy.**]

**Nanami**: [80:41] [Japanese] 魚の種類とかも分かったらいいなと思って作りました。
[Translation: **It'd be great if I could learn to recognize different kinds of fish, so that's why I made this site.**]

**Nanami**: [80:55] [Japanese] まず初めに初心者の人が使える説明とかも載せてます。
[Translation: **First, for beginners and people who've never used something like this before, I've made it so you can read guides and explanations for beginners.**]

**Nanami**: [81:22] [Japanese] 私自身も釣りをあまりしたことがないので、楽しんで覚えられるように、こういうゲームとかがあります。
[Translation: **From here you can jump to other sections as well. I haven't been fishing much myself, so I wanted to make it fun and help people learn with things like games.**]

**Nanami**: [81:47] [Japanese] ちょっと難しいんですけど、こんな感じで。
[Translation: It's a bit hard, but it's kind of like this.]

**Nanami**: [82:01] [Japanese] 釣れた魚は、こんな感じで分かるようになってます。
[Translation: **The fish you catch are displayed like this so you can easily see.**]

**Nanami**: [82:11] [Japanese] まずこのサイトでできることは、釣り場の検索とか、あとどういう魚がいるのかっていうのと、あと釣れた魚の記録とかができるようになってます。
[Translation: **First, what you can do on this site: search fishing spots, checking what kind of fish are there, and recording the fish you caught.**]

**Nanami**: [82:26] [Japanese] 最初場所なんですけど、場所が分かっていたら、ここに。
[Translation: **First about the location. If you already know the spot...**]

**Nanami**: [82:36] [Japanese] こんな感じで。
[Translation: It's like this.]

**Nanami**: [82:41] [Japanese] 出たらここでGoogleマップに飛んで、どのくらいの時間で行けるのかとかが分かるように設定してます。
[Translation: **If you find the exact spot, you can jump to Google Maps from here and see how long it takes to get there. I've set it up so you can check all that.**]

**Nanami**: [82:55] [Japanese] もし場所とか決まってなくて、魚どういう魚が釣りたいなとかが決まっていたら、魚を選択して、場所が分かるようになってます。
[Translation: If you haven't decided on a location yet, but you know what kind of fish you want to catch, you can select from there and find out the location.]

**Nanami**: [83:09] [Japanese] アジ、ブリ、クロダイかな、っていうのが表示されるので。
[Translation: **If you were wondering where to catch Aji (horse mackerel), Buri (yellowtail), or Kurodai (black sea bream), it will show up here.**]

**Nanami**: [83:21] [Japanese] ここに場所の概要とかレビューとかあるので、実際の声とかが聞いて、状況が見れるようにしました。
[Translation: You'll find an overview of the place and reviews so you can hear real opinions and check the current situation.]

**Nanami**: [83:36] [Japanese] 近くの釣具屋さんの情報が、私のお父さんがこういうのがあった方がいいんじゃないかっていうのを教えてもらったので追加しました。
[Translation: **Information about local tackle shops is included because my dad told me it would be useful to have that, so I tried adding it like this.**]

**Nanami**: [83:51] [Japanese] 魚のカードを開いてもらうと、魚のどういう魚なのかとか、おすすめの食べ方とか。
[Translation: **Open the fish card and you can see what kind of fish it is and suggested ways to prepare or eat it. It's all written there.**]

**Nanami**: [84:08] [Japanese] 今のところ魚の種類は結構まだ少ないので、自分で魚の追加できるようにカードを作れるようになってます。
[Translation: Right now, there aren't many types on the fish list, so I've made it possible for you to create new cards yourself like this.]

**Nanami**: [84:32] [Japanese] 自分の魚を記録できるように。
[Translation: And this is for keeping a record of the fish you've caught.]

**Nanami**: [84:41] [Japanese] まだこれは本当にデモ版で、全然判定できないようになってるんですけど。
[Translation: This is just a demo version and it doesn't actually work yet...]

**Nanami**: [84:48] [Japanese] ここに写真を入れてもらうと、魚が何の魚かっていうのをAIが判定してくれるような場所も作りました。
[Translation: **The idea is that if you upload a photo here, the AI will tell you what kind of fish it is.**]

**Nanami**: [85:04] [Japanese] 以上です。
[Translation: That's all.] Thank you.

**Anand**: [85:12] Thank you. What's particularly impressive about this again is the process. So when Nanami shared this with a couple of people and they pointed out the feedback, that included someone saying, "No, look, this information is not correct." And **on digging further, that turned out to be AI generated information where it was stating things that were not facts.**

**Anand**: [85:38] And post that, **Nanami's changed the application to show evidence, saying this particular one was sourced on this particular date, click here to provide a link to the original.** Effectively bringing in two things: one, feedback about what makes an application useful and iterating based on that; and second, making sure that we know what's right and what may not be right—how verifiable an information source is. And that's pretty important as part of the process as well. Johan, if you could... let's take your application. You want to present from yours? Yeah, sure.

**Anand**: [86:41] Before you start, Mio, if you could... if you're okay, maybe you could share next. And Christopher, if you could share after that, let me just try and format it. Okay, I've signed into yours. It's all yours.

**Johan**: [87:46] We'll change language... Japanese? [laughs]

**Johan**: [88:06] So this is an Indonesian website for an Indonesian audience, especially for the stock traders in Indonesia. And the function of this website is to **log on whatever stock you purchased, how many lots, and you can see the profit that you made as well as the losses.**

**Johan**: [88:34] This is one of the testing data here which... let's say I want to sell. And then I want to sell at the price of, let's say, 6,500. And then this will be my profit. There you go, it logs on the profit. But this is the testing data, so you can't... it deletes all the other data. I'll try to run on my laptop later.

**Johan**: [89:08] And this uses the personalized email address of all the users, so in the admin, I can see who logged on and what did they do, but not their data. So everything is protected.

**Johan**: [89:29] Here, this is also very useful and **one of the features that does not exist in applications today: how much the brokers take—take a cut from your profits—and your transactions.** Do you have to log in again? Yeah, sure.

**Johan**: [90:17] Here you have the privacy notes as well, so no data is being collected. And then you can start.

**Johan**: [90:30] And here I'm logged on to my own account, which is the admin account, so I have this particular tab here, which I can click and it shows me how many people have logged on, recorded the last sessions and for how long, and what did they do. If they did any transactions, it will show here, if they input anything, etc., or not.

**Johan**: [90:58] Past 30 days, 90 days, 24 hours. And then how many users in each of these. [Applause]

**Anand**: [91:14] Thanks, Johan. **The last bit was perhaps for me the most interesting of the lot, because what we now have is not just an application that is useful for each of the users, but potentially a platform where one user can benefit from the usage of others**, because Johan has access to information on who's doing what, are they doing it well, not well, and both centrally as well as from collated information, the application can become more powerful.

**Anand**: [91:41] Some of you might remember that from yesterday's session, I was suggesting that we start adding instrumentation—log what people are doing—and **this is a step towards making the application improve by itself based on others' use.**

**Anand**: [91:54] So, let's go on to... sorry, Mio, if you could, I'll open your application as well.

**Anand**: [92:18] Thanks, Mio. Do you want it in Japanese or English?

**Mio**: [92:22] English? Okay.

**Anand**: [92:24] Oh, you have an English version? Sorry. You should just go with that.

**Mio**: [92:30] Hello. My name is Mio Sakai, and I speak Japanese, so my ChatGPT will translate in English.

**Anand**: [92:51] [to audience] She'll speak in Japanese and the machine will translate it.

**Mio**: [93:09] [Japanese] えっと、今から私が日本語で説明するので、話すのをやめたら英語に翻訳してもらえますか？
[Translation: **I'm going to explain in Japanese now, so when I stop speaking, could you translate it into English?**]

**Mio**: [93:31] [Japanese] 今から私が日本語で説明するので、話すのをやめたら英語で翻訳していただけますか？
[Translation: **I'm going to explain in Japanese now. When I stop speaking, could you please translate it into English?**]

**Mio**: [93:51] [Japanese] これ音出すのどうすればいいの？
[Translation: How do I get the sound out?]

**Unsure**: [93:54] [Japanese] 一番右のやつ。
[Translation: The one on the far right.]

**Mio**: [93:55] [Japanese] はい、これで日本語から英語にして。
[Translation: Okay, now change it from Japanese to English.]

**Anand**: [93:59] [Japanese] そのまま話して。
[Translation: Just keep talking.]

**Mio**: [94:10] [Japanese] 私は、持っている本や漫画を整理するアプリを作りました。
[Translation: **I created an app to organize the books and manga I own.**]

**Mio**: [94:31] [Japanese] はじめに開くと、このサイトの使い方を説明してくれます。
[Translation: When you first open it, it explains how to use the site.]

**Mio**: [94:42] [Japanese] これは実際に押しながら体験できて、とても分かりやすくなってます。
[Translation: **You can actually try it out by pressing through the steps, which makes it very easy to understand.**]

**Mio**: [94:54] [Japanese] 飛ばすこともできます。ちょっと今回は時短のため飛ばします。
[Translation: You can also skip this. I'll skip it this time to save time.]

**Mio**: [95:04] [Japanese] 説明を一通り受け終わるとプロフィールが作れます。
[Translation: Once you've finished going through all the instructions, you can create your profile.]

**Mio**: [95:16] [Japanese] 名前を入力して好きなジャンルを選択できます。新しくジャンルを加えることもできます。
[Translation: You can enter your name and select your favorite genre. You can also add a new genre.]

**Mio**: [95:29] [Japanese] また、好きな作者も追加することができます。これは任意です。
[Translation: Additionally, you can add your favorite authors as well. This step is optional.]

**Mio**: [95:39] [Japanese] で、えっと、さっきの説明はいつでもこのマークから見ることができます。
[Translation: Also, you can access the instructions we mentioned earlier at any time by clicking this icon.]

**Mio**: [95:51] [Japanese] 本の追加はここからできます。誰か、何か追加したいものありますか？
[Translation: You can add books from here. Does anyone have something they would like to add?]

**Unsure**: [96:01] Harry Potter.

**Mio**: [96:06] [Japanese] スペル分かんない。
[Translation: I don't know how to spell it.]

**Anand**: [96:14] Let me type that in.

**Mio**: [96:44] [Japanese] ここで出てきたものを選択して追加することができます。で、スマホ版で開くと、このカメラマークからバーコードを読み取ることで本を追加できます。
[Translation: **You can select and add items that appear here. And if you open it on the mobile version, you can add books by scanning the barcode from this camera icon.**]

**Mio**: [97:03] [Japanese] 登録内容、あ、これ英語に直した方がいいか。細かく登録できて、えっとジャンルもここで選択することができます。説明文とかもこちらで行うことができます。
[Translation: Registration details... oh, should I switch to English? You can register in detail and you can also make a selection there. You can still listen to the explanation here as well.]

**Mio**: [97:29] [Japanese] シリーズ物とかもここでまとめて選択することもできます。
[Translation: If it's a series, you can also select them all together here.]

**Mio**: [97:45] [Japanese] で、えっと、いろんな本を追加していくと、そのジャンルに合わせて自動でおすすめの本も紹介してくれます。
[Translation: **As you add various books, the system will automatically recommend books based on that genre.**]

**Mio**: [98:04] [Japanese] で、えっと、ここに表示する方法なんですが、えっと、いろいろ選べて。
[Translation: As for how to display it here, there are various options you can choose from.]

**Mio**: [98:18] [Japanese] 読み終わった本とかまだ読めていない本とかで絞り込むこともできるし、
[Translation: **You can filter by books you've finished reading or books you haven't read yet.**]

**Mio**: [98:32] [Japanese] 漫画や小説ごととか、お気に入り登録したもの、あとはジャンルごと。
[Translation: By manga or novel, by favorites or by genre.]

**Mio**: [98:42] [Japanese] あとは電子書籍と紙の書籍も選ぶことができます。
[Translation: You can also choose between e-books and printed books.]

**Mio**: [98:53] [Japanese] で、ちょっと今お見せできないんですけど、表示方法が三つあって。
[Translation: I can't show you right now, but there are three display options.]

**Mio**: [99:00] [Japanese] 背表紙と、シリーズごとの表紙とリストがあって、私のイチオシは背表紙表示です。
[Translation: **There's a spine view, cover art for each series, and a list. What I recommend most is the spine display.**]

**Mio**: [99:14] [Japanese] 本物の本棚みたいにずらっと並べることができて、あの、一緒に購入できていない本とかも把握することができます。
[Translation: **You can line them up just like on a real bookshelf and keep track of books you haven't bought yet.**]

**Mio**: [99:37] 以上です。Thank you for listening. [Applause]

**Anand**: [99:46] Thank you, Mio. One of the interesting things about this was again the feedback from the testers. One of them couldn't understand how to use the application. Another tried to add a novel and found that that has multiple editions, multiple genres, he struggled through it a fair bit.

**Anand**: [100:11] But at the end of it, they said, "Oh, this functionality is quite good." Another said, "**But wait, doesn't Amazon already provide this functionality?**"

**Anand**: [100:22] And I really liked Mio's reflection on this, which is: **quite often, telling it what to do is hard. Actually doing it is not the difficult thing.**

**Anand**: [100:33] I know we have only one minute, but Christopher, do you think you could quickly cover in a couple of minutes, maybe, your application? Okay.

**Anand**: [100:59] Can you translate into Japanese? Yes, I think you can. I'll give it one shot. Translate to Japanese. And yes, there you go.

**Christopher**: [101:18] Okay, good afternoon. So what I built is basically a "VC Partner Meeting" simulation practice. So basically this is for those first-time founders and founders in general when they want to practice their pitch towards like investors.

**Christopher**: [101:41] And so this is my app. So basically it's a Q&A session, questions and answers using these categories. And then, so before you start, right, there are several like additional functions you can use.

**Christopher**: [101:58] **So this function is basically to like add in your slides and like all the information about your company so that the AI will be able to fit the questions and answers like more towards like what your company is and also fit the feedback also.**

**Christopher**: [102:22] And then after that, you have this timing system to like simulate like actual real-life conditions when you're pitching to the investors.

**Christopher**: [102:30] And so basically you get started here. And then after that... so basically this is like the questions. So if I'm not wrong, right, the first question is like about your problem and whatever. So there's this microphone function where you can like speak into the microphone. And then after, or you can even type it out.

**Christopher**: [102:54] So after you type it out or whatever your answer is, you can then present it to the partner. So I'm just going to give like a very quick example. So like because this is a problem, right, then I'll just say like...

**Christopher**: [103:14] I want to solve world hunger. Okay, so this is obviously a very unrealistic thing and there's no like details or whatsoever. So I can just present it to the partner like this.

**Christopher**: [103:28] So then after that, you'll keep going on to like several other categories. So I'm just going to copy and paste here.

**Christopher**: [103:46] Okay, so by the end of the seven rounds, right... yeah, **so basically it will give like a feedback system purely on the different categories and then it'll give you a rating.**

**Christopher**: [104:02] And then after that, it can also give you like what actually worked and what is like the biggest flaw of your answers. **And then you are even able to save your transcript as a PDF.** Yes, that's all. [Applause]

**Anand**: [104:24] Thank you, Christopher. What's interesting again is the process. The first version of the application had the AI giving feedback after every question. And Christopher said, "**Wait, that's not how a VC meeting actually works. They don't give you feedback after every slide or whatever; they wait till the end and after that share inputs with you.**"

**Anand**: [104:48] Now, that's your knowledge, your experience of a domain coming in. And **when that sort of a thing comes in, it elevates the entire process.**

**Anand**: [104:58] So, I'll reiterate—we're going to end the session in a minute. **The thing that you've obviously already learned, and you've seen that from your shared learnings, is that AI is quite comfortably able to take care of the execution.**

**Anand**: [105:15] **What remains is your judgment: what to tell it to do, how to tell it, how to verify, how to make sure that we continuously learn from the process and how to iterate so that the next time gets faster.**

**Anand**: [105:28] I have only one thing that I would like you to try practicing: **try delegating everything to AI, as much as you can. See what it's NOT able to do. Focus on learning that. That will be the more important skill.**

**Anand**: [105:47] Okay? Thank you everyone, all the best. I will share an email summarizing all of these details by tomorrow. Cheers. Thank you very much. [Applause]

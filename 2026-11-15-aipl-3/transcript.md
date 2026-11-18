## Transcript

**Leadup**: [09:19] Good morning, professor. For the interest of time, as we already have 29 participants, we can start, and others can keep joining.

**Anand**: [09:29] Oh, definitely. Hey, just a quick check. Is my audio coming through fine? Are you able to hear me clearly?

**Mukul**: [09:39] Yeah. All-

**Anand**: [09:40] Thank you. Three weeks ago, we started with me asking **how far you would let AI go by itself.** And the majority of you said you'd be careful. Out of 33, 18 said you used AI's work, but checked all of it, and only two people said they would let AI act unchecked.

Then we ran a small survey. In that survey, actually, I suspect you may not have noticed, for half of you, you got a slightly differently worded question. Half of you saw a survey where the question said AI gets 95% of expense claims correct. For the other half, I said the same thing, but in a different way. They saw that AI gets 5% of the claims wrong.

I was curious to see if there is a difference. My guess was that the 5% people who are told it gets it 5% wrong will probably be more cautious. Those who heard that it gets it 95% right will probably say, "Yeah, I'll let it act autonomously."

Interestingly, the opposite happened. That is, 3 out of 16 said, "We'll let it pay with some spot checks," and no one in the 95% right group said, "We let it run autonomously." Numbers are small, but at the very least, it felt like a good summary of the very first session, which is that **our gut feel isn't particularly reliable either. Neither are agents.**

And when I said you, in the first session, are allowed to check only 10 out of 100 decisions amongst the claims, about 20% well, the majority, about 20 yeah, 21 of you picked 10 of the costliest mistakes. One of you picked the ones where AI was least sure about. One of you picked ones where the second AI disagreed. And we saw different ways in which we were cross-checking AI decisions: where it's expensive, where it declares that it's not sure, where there is disagreement between multiple AIs.

And what we saw, we saw that what AI cannot do is personal. Some of you would not let it schedule your meetings, some of you were already doing that. Where it works also depends on the tasks, the tools, and the permissions that you give it. It might work at home, it might not work at office.

And broadly in the first session, we saw three ways of making AI reliable instead of debating whether it is or is not. One: **get multiple models to agree.** We saw that errors fell from 14% to less than 1%. But because of that disagreement, humans still had to process a series of cases.

Second: **we saw that testing your own rules is important.** Just telling AI, for instance, "write in simple English" actually makes it start thinking in a worse way. So, is telling it to write in simple language, a rule that we are adding, really a good rule? Worth benchmarking.

And that **if we can convert our policies into rules that can be machine checked, deterministically, nothing like it.** We, at least, can reason about it, and so can AI.

I also learned a bit about myself in the first session when one of the questions, nobody was responding to the questions, I asked AI, "Who hasn't answered?" Got a list of names and started calling you out by name, which was effectively my first roll call ever.

And then one of you asked a question: "When do we say stop? When do we tell AI, okay, that's not the direction to go in, or click on the stop button?" That was three weeks ago. At that point, I didn't have an answer. I promised to write down 10 moments where I would want to stop the AI and check later to see if my approach was right or at least if I have an answer.

Today, I have an answer to the question, **"When do I press the stop button?" The answer seems to be under three circumstances. One: when it looks like it is stalled. Second: when it is clearly going in the wrong direction.** It may be because of something I said, something that it found that is wrong, or whatever. Between us, it is certainly going in the wrong wrong direction. **Third is, I'm going to run out of tokens.** I very carefully monitor whether I'm at 99%, 100%, and I don't want it consuming the task is not important enough to consume the paid tokens. These, in descending order, seem to be the reasons why I stop AI.

This was the first session where we were talking about when do you let AI act autonomously. Our second session, two weeks ago, was: **how do you check AI cheaply?** And before this, I had shared a homework, and each of you had done it your own way. Rhea, for instance, used AI to design a Gen Z styling app, and its summary covered features and the competitors. But there were two risks, in fact, Rhea cared about that it left out: photo privacy, hurting teenagers with body shape comments, etc. And that's an area where there is a personal preference, domain expertise, which comes in handy.

Saurabh converted Saurabh had AI convert test code, which worked, but one conversion actually took two days where he could have done it by hand in just an hour. So, that's a technical success, but an economic failure.

Ketaki's Diwali redecoration: the AI swapped a rug for a table. Her home, so, obviously, she spotted it instantly.

So, what we clearly saw in this is that **the cheapest checker is when you know the domain.**

We also did a side poll where 20 out of 27 of you said your children shouldn't do homework with AI, but you clearly did. 23 out of 24 actually did your homework with AI. I shared this with my daughter, by the way, and she said, "Good, Appa. You have an audience who's very self-aware, to the very least."

And then we went on to the bank game. You had 100 customer tickets, each with AI's label, and you could only check 10 of those, right? And the costs total cost of checking varied all the way from 1 lakh to 2.5 lakhs. There was one particular ticket there, you might or might not remember, ticket T40. That ticket said, "My transfer is pending." The AI was 100% sure. That the first one. Second also agreed. But the actual answer key said that it was wrong, categorized wrongly.

Question is: were the AIs wrong, or was the answer key wrong? And that was a key point we spoke of last time, which is: **the checker also needs checking. Who watches the watcher?**

And we saw some techniques for that. How do you look at the confidence score? When a model says it's 80% confident, is it really 80% confident or only 60% confident? And we did see that AI generally tends to be overconfident, but it is still a useful signal for ranking.

We went on to see if it is possible to, and how we can trick AI. For instance, how do we get it to reveal the secret word "relinquish"? And Lakshmi managed to get Gemini to say it just by asking for an email about property relief.

Now, telling the AI, however, "Please don't do this," doesn't seem to be good enough protection. And clearly, this is part of its non-deterministic behavior. If I just say, "Please don't send the email," it's entirely possible that it will still go ahead and send this email. And that actually happened to me two days ago, when I had broadly given instructions to not send an email, had a slightly longish conversation, then I come back and look at it, and it told me it's already sent emails to 40 people.

**So, unless we have some kind of deterministic checks or constraints, just checking is not sufficient.** And all the techniques we discussed, which is knowing the domain, checking the checker, calibrating, etc., are about improving it. But for some things, you do need deterministic checks.

So, the summary in some sense of last session was: **you want to build controls into the workflow, but only where the risk justifies that.** A bank has a maker-checker for cash, but nobody checks snacks. Not a big deal.

So, session one was about one decision: when do you let AI act? Session two was about how do you review AI cheaply?

Today is about **what happens when multiple agents start interacting.** In session one, one of you suggested, for instance, using AI to screen job interviews. Now, imagine every candidate is using AI, not just to write their resumes, but, in fact, to answer the questions. Now, be let's say, interview questions, or entrance exams. Now, you may say, "Wait, how realistic is that?"

So, let me see if I can share my screen and show you how realistic this is. Okay, I'm guessing my screen is shared. Yeah.

Right. Okay, so we have this entrance exam. Oh, I don't have an access key. It's a fairly straightforward entrance exam. Let me see if I have the Yeah, I have a video for it.

So, what I did was told Codex, "Look, I have this particular link, which is an entrance test, open in my browser. And this is a practice test. I want you to solve it and log the progress." And I asked it, and I recorded what it solved. Here is what it did.

On the right side, it is showing what Codex is doing. Let me turn off the captions for him. Okay.

On the right side, it is showing what Codex is doing. On the left side, it is showing the exam page. Now, the exam page includes proctoring. It includes a video camera that is on and takes pictures of me every few seconds or so. And Codex is patiently going through the left side, seeing what is there, and it is starting to control the page. It loaded the test. On the right side, it was waiting for the page to load, and then took a snapshot of the page, looked at the first question, thought about it, filled out uh went to the It's, okay, still figuring it out. It zoomed in, for whatever reason, okay, or maybe I zoomed in, to be fair, I don't know. It clicked the first option, and then went to the next question. It's thinking about it. It chose another option, went on to the third question, and so on. And this is not an accelerated speed video. This is the speed at which it was actually solving the exam.

At some point, I would have had to tell it, "Look, go a little slower. It looks like on the left side somebody is solving it really fast," or, I mean, to already finish eight questions way faster than I would have been able to even read.

And then it went on to solve some coding tests also. Yeah, essay-type question. So, there was an essay question which required us to upload a text file, or a PDF file, or whatever. It wrote a long essay about an FMCG firm, wrote the case study, formatted the sales report, and uploaded it. And then went on to the coding section, where it had to write some code. This was an entrance test for a data science a data analyst or a business analyst kind of a role.

It scored full. What I was doing was sitting and eating an apple in the meantime. These are the proctoring images. Now, a smarter person would not be eating an apple; they would be sitting and looking as if they were typing this.

**But net-net, today, we are at that stage where it's not just you who's using agents. It's your employees, your colleagues, your clients, your partners, your vendors. Every single one of them is also using agents.**

Now, if agents are doing their job well, everything is perfect. Is everyone better off? That is what we're going to look at today. **What does it take to manage in a world where we have teams of agents? And what does it take when, even when all the agents are individually right, we may still not be better off?**

So, we're going to do this with a small game. And I've set this game up so that it'll automatically assign everyone into groups. I will be sharing the link.

Here is the game: **each of you runs a restaurant in a food court. This food court has four stalls.** There are 40 of us, and therefore each of you will be going into one particular multiplex or mall. And in each mall, the food court has four restaurants; you will be managing one of those, so you will be part of a team of four.

You can ask AI for advice. Please ask AI for advice on what you should do. But ultimately, you have only one decision you can, or 12 decisions you can make: in January, how much discount to offer; in February, how much discount to offer, and so on, up to December. And your choices are also limited: **should I offer 0% discount, 10% discount, or 20% discount in January? Similarly, 0%, 20% uh 10% or 20% in February, and so on.**

Now, here's the thing: if you offer a discount, more people will come to you. In fact, more people will come to the mall. But your profit will be lower, and your competitors' profits will be lower.

If you offer a very high discount, your competitor will also start offering a discount. Or even a medium discount, your competitor will also start offering a discount. And everybody can see everybody's plan. So, this is where you can sit together and plan for the entire year, and you will see how much profit you will make as you change each one of these and share. And you have a chat window there itself in the game, where you will be able to see the results.

So, between the four of you, use agents, use your understanding of business, competitiveness, etc. Keep in mind that giving discounts does bring more people to the mall; keep in mind that undercutting each other reduces your profits and triggers price wars. And see how much money you can make. The objective of the game is simple: **make as much money as possible.**

I'm going to share a link with you, and you would need to log in. The game begins in five minutes, at 12:00 my time, which is 9:30 your time. I'm going to paste the link once I find the chat. Yeah, found the chat. Pasting the link, and I will share my screen so that you can also see what you might see.

So, first, you would need to log in. So, if you're not logged in, which is what everybody will be right at the start, there'll be a big black button. In my case, it says "Sign in as Anand." I am going to sign in with my Google account.

And then you have the instructions. So, I've set this up so that we can play it at in a few minutes, or in half an hour, etc. But ignore all of this. There is a button, "Open food court." That's the only button you need to click.

I repeat: log in and click on the "Open food court" button. The "Open food court" button will open this link, where you can say I'm where it'll let you run a restaurant. Only one of those is active, which is your case, it will show you 9:30 Oh. Oh, yeah, correct, 9:30 AM India, which is 12:00 noon Singapore. Click on this, and the instructions will be there. Read the instructions. In 4.5 minutes, your session will start. If anyone has any questions, just unmute yourself and ask.

In case anyone has not yet reached this page, please just speak up. You may need some help, happy to guide you.

**Bhavya**: [29:53] So, this is like guesswork, is it, sir? Like how do we know who what others are taking?

**Anand**: [29:59] You will be-

---

**Anand**: [29:59] You will be able to see what others have taken. It'll all be shown like a spreadsheet.

**Bhavya**: [30:04] We are supposed to give discounts, but at the same time supposed to be making profit?

**Anand**: [30:09] **Make as much money as possible.** And discounts, if you give bigger discounts, you'll get more customers.

**Bhavya**: [30:19] Okay, thank you, sir.

**Anand**: [30:40] Like I said, AI can take an exam for you. If you consult with AI over these 20 minutes, you may find it to your advantage or not.

The number you are optimizing, by the way, is this thing that says your mark: **60% team score, which is the total food court profit, which gets distributed back, and 40% of your individual profit.**

So, you are trying to compete within the four of you; you're also competing with the other groups.

Is anyone facing any issues getting to this page?

Hi, yeah, Akshika.

**Akshika**: [32:03] Sir, just a question. I have reached the page, but the last line, know, "Customers remember last month's discount a little." So, is it the calendar last month, or the last month they visited?

**Anand**: [32:15] It's the same in this case. It's January, February, March, all the way to December. So, if you give them a high discount and then stop the discount, they'll remember that a bit.

**Kasi**: [32:28] Um sir, what would be the impact of it? Like, is it for us to discuss and gauge the impact of that?

**Anand**: [32:34] You'll be able to see the final profit for the food court, as well as for yourself, immediately when you change.

**Kasi**: [32:41] Okay.

**Anand**: [32:43] So, you'll be able to see the gauge the result, change the numbers, then discuss with each other. But please use the chat, because there are multiple groups, it can get confusing. So, for the next 20 minutes, we'll turn off the not the turn off the audio, use chat to discuss with others.

**Kasi**: [33:00] Yes, understood.

**Anand**: [33:12] Finally, we'll share a leaderboard of your marks to see who's scoring the highest, who's scoring the lowest, what strategies worked.

Yeah, it's about to begin. All yours.

Professor, we have some comments in the chat box showing that the joining has closed.

**Anand**: [40:10] Uh correct, and I did discuss with uh Neelabh, and the same would have been the situation for Sourabh. They joined a bit after the time closed. It's okay, they'll be waiting it out.

**Leadup**: [40:20] Yeah, sir.

**Anand**: [46:02] Uh, Sourabh, Neelabh, when you say it's uh, could one of you share your screen? Maybe I'll uh be able to gauge.

**Neelabh**: [46:16] Yes, sir. Sure, 1 second. I'm sharing my screen.

**Anand**: [46:20] Sure.

**Neelabh**: [46:36] Can you see?

**Anand**: [46:38] I can't see it yet.

**Neelabh**: [46:47] I'm sharing my screen. Are you able to see?

**Anand**: [46:50] Not yet. Yes, now it's started. Right. Ah. Uh, okay. So, I'm guessing you hadn't joined uh before uh 9:30. So, yeah. No, in that case, it would be disruptive. Please just wait it out for 20 minutes. And I'm guessing then Neelabh, the same may have uh yeah. The reason I had put it up earlier was so you'd be able to join before the session starts. Not a problem.

**Neelabh**: [47:18] Yeah, actually, there was some internet connectivity issue, so that I had to reconnect from my phone. It's a hotspot. Okay, no worries. I will join it again. Thank you.

**Anand**: [47:33] Sure. You can stop sharing the screen.

**Anand**: [47:59] There is a "Talk" section at the bottom right, which you may use to discuss within your teams.

There's about 11 minutes left for you to finalize your strategies.

**Lakshmi**: [50:33] Sir, this may be a very naive question, but the one that is highlighted is my uh team, is it?

**Anand**: [50:42] Um, the column that so you are only seeing your team.

**Lakshmi**: [50:47] Are you? Oh, oh, okay.

**Anand**: [50:49] And one of them is you.

**Lakshmi**: [50:50] Okay. Okay.

**Anand**: [50:52] There are four people in a team.

**Lakshmi**: [50:54] Okay, sir.

**Swati**: [52:33] Uh professor, we cannot edit it right, after uh saving it?

**Anand**: [52:37] Oh, you can. Uh, the whole point is for you to discuss with the group and change it however often you want until you have no more time.

**Swati**: [52:45] Okay.

**Anand**: [55:26] You now have a couple of minutes to discuss and wrap up. You may change your numbers based on discussions, and save again.

Okay, time for final negotiations. At this point, you should have a little bit of time just discuss within the group in the "Talk" at the bottom right, or see the numbers, change them, and at this point, whatever you have, save. You have to click on the "Save." Uh not immediately, save won't be enabled now. This 2 minutes is for you to talk amongst each other. At the end, you'll have 30 seconds to change and save. Final negotiations.

Okay, with that, the game has ended. Uh you will not be able to make any more changes. These scores are finalized. Now, what we're going to do I know it's still says 1 minute. That's just for you to maybe see your screen, take a look at what people have done, what you've done. Spend a minute absorbing that.

Okay, now um all of you should see a screen that looks sort of like what I have. Uh if you uh that'll tell you your final uh scores, both by team as well as individual performances, of course, for those of you who are able to see the full game.

Now, let this be there because you will be uh using this as part of today's discussion. But let's now get into a bit of a discussion mode. **What do you think the best strategy was for this game?** Open question to all.

Uh, yeah, Aishwarya.

**Aishwarya**: [56:52] Sir, I I personally feel we shouldn't go with 20% discount at all. So, it would be better to move with 10%, and in case the competition feels like some sales are high during September or peak months, then they may go for 20%, and we can consider whoever is having good sales through 10% or even 20% after that. But I found one of the team members was always for 20%. I think that is a something a drawback for the all the four restaurants.

**Anand**: [57:20] Got you. So, **don't use 20%; anything else is okay.** Any other inputs?

**Mandar**: [57:30] So, in general, what I feel is, during these months, you can give discounts-

**Anand**: [57:34] Uh sorry, Sourabh, your voice is low.

**Sourabh**: [57:38] Oh, it was not me. Someone else was speaking.

**Anand**: [57:40] Oh, sorry. Uh, okay. Sorry. Then please go ahead, Sourabh.

**Sourabh**: [57:43] All right. Uh, so what I felt was, I gave my uh this data to ChatGPT basically to see what it recommends. It recommended that uh July uh June, July, August, reduce it to 10% because uh the customers will uh will come more often to the uh restaurant. And uh for uh January, February, March, April, keep it 20%, because that is when uh people will be going for a discount. And there was based on that, I was actually shuffling around and seeing how can we get to have more uh profit. And uh so that was the one.

**Anand**: [58:25] Got you. Interesting. You know what, I'm going to ask uh let me share a link to a form. And I will also share a QR code, if that's easier for people. Um yeah.

So, this form, which is also on the chat, has two questions for now. Which is, did you, as Sourabh did, use any agent, any form of AI, to help you with this? Yes or no.

And secondly, what do you think was the best strategy for this food court? We are going to discuss this, and we have a couple of inputs so far. But do share your full uh response here as well, so that we can get a more comprehensive picture towards the end of the session. And we're effectively crowdsourcing what would be an input.

So, a couple of people have started answering the first question. I'll leave this uh QR code on, and it's also there in the chat. I will wait for how many people do we have? Okay, we have 44 participants. Some of you were not able to participate. At least 25 responses uh on this, and a series of future questions is what I will be uh looking forward to.

Others, any uh strategies that you think will be most effective for this one?

---

**Pallavi**: [59:59] I was thinking that. But yeah, I I also observed that others were giving 20% all around. So, yeah. That's That's something which can be worked around.

**Anand**: [60:10] Got you, Pallavi. So, that's two observations. One, give more discounts when there are more visitors. And the other is, an observation that sometimes people just constantly keep it at 20%. So, I'm wondering A few seconds, Bhavya. Would we give more discounts when there are more people coming anyway, like in September where there were 93,000 visitors, or would we give more discounts when there are fewer people coming in, like in January, so that we can get more people? Not saying one is better than the other from an overall revenue perspective, but from a profit perspective, this was easy to check. You just needed to put in different combinations and see what would have worked better. But maybe you had already done that and saw the result. But yeah, Bhavya, go on.

**Bhavya**: [61:12] Yes, sir. So, here what happened is the game had time limit, and we were kind of asked to put strategies individually for the team. And other teams also had their own strategy. And for me, I was also asking AI. So, it was like, like you said, agent talking to agent, agent talking to human, and then finally what happens, because in between my standing was three. After submitting, the standing became four. So, I think like relying on too many things, at the same time communication should be stronger. And we should be able to see what's happening across the market. But take some more time to understand, okay, now what do I do from here? Because finally, we are the decision-makers, so how do we strategize?

**Anand**: [62:06] That's an important point. What I'm taking away, Bhavya, from what you said is, one, agent is strategizing, humans are strategizing, I'm strategizing. And there's only 20 minutes. Now, agents don't have a problem with 20 minutes. Obviously, the problem is with us, humans, who are slower than agents, fair enough. But at the same time, we are the ones who ultimately lose if things go wrong. Of course, we also win if things go right. But therefore, the responsibility should be ours and we, at the very least, want to feel like we're not going to get a raw deal. That's pretty important. And it's not just an agent whose output we have to understand. There's another human out there whose output we have to understand as well. And that's something worth discussing. Let me just do a quick check. At the moment, I have 12 responses for the first question and 15 responses for the second. I'm going to wait till we have about 25 responses, at least, for both of these. Please do open the link in the chat window or on the QR code here. I can paste the link in the chat again for those of you who may have missed it. **What do you think was the best strategy in the food court?** In the meantime, any others? Your thoughts?

**Swati**: [63:53] Uh sir, it's Swati here. So, in my experience what happened, sir, in the month where the uh footfall was uh very higher, like uh the last quarter, I first gave the uh uh I mean, the discount over there like 20%. But then, I then removed the discount, I made it to zero. Then I could see that my profit was more. So, then in that sense, I understood that because the footfall is, for sure, because of maybe seasons and uh Christmas and all that, uh festive seasons, maybe giving a discount is not a good option because uh anyway which ways the footfall will be there. So, that way I could sense that this may work as a strategy. So, accordingly, I gave the uh profit percentage.

**Anand**: [64:39] Got you. So, in other words, the discounts were not as effective when the footfall was high in any case. Got you.

**Swati**: [64:48] Yes. Yeah.

**Anand**: [64:50] Any other strategies people tried out? While you are filling this out, I did have another question that I wanted to discuss and I will add that to the list, which is, uh supposing you had let an agent play this game, an AI agent, just like we saw how agents were able to take an exam. **Do you think it would have done better or worse?** I've also added this question to the form. So, when you are filling out the form, that's building I'm going to add a series of questions as we go along. But the last question here is, how would an agent have played this game if the aim was to increase the overall profit, which is same as what you had: 40% for the player uh profit plus 60% for the food court profit? Would an agent have played better? Would an agent have played worse? But let's talk, in the meantime. What's your guess? Uh yeah, Aishwarya.

**Aishwarya**: [66:18] Sir, my guess is it would be better because agents, I don't think they will compete with selfish intentions. And so, I think they will go with all the four having a profit. And also, who can have a win-win situation, that's my opinion.

**Anand**: [66:33] Interesting. Others?

**Sourabh**: [66:36] I think with respect to the numbers, the agent will do better. But with respect to the other team's performance, agent- there also agent will do better. But they are actually the human thing come in between and which try to read the other team and understand what is going on their mind and based on that, we can strategize. **That part, I think agent will not do better. But with respect to numbers, it will do it better.**

**Anand**: [67:07] So, the agent may not understand or persuade the others as much, though it may have a better strategy. Got you, Sourabh. Uh Lakshmi?

**Lakshmi**: [67:16] Yes, sir. Actually, similar uh understanding I also had. With respect to the stats, it will do very better, it is very fast in turning numbers, in trends, understanding everything. But for the dosa uh counter that I had, so, I was thinking that anyway Jan is low, and from July to September also I ended up giving 20% discount because that being a drier month, I mean, if we give more discounts, we'll have end up having more footfalls. So, people will have a default option that, okay, some some times, this this place is always having 20% discounts. Let's go there, something like that. But at the same time, I mean, though I gave 20% discount for the December month, I mean, agent would have actually not agreed with me because anyway it is not going to bring profit if I give 20% there. So, that human aspect of This could also probably be an interesting situation where if the shop is new in the market, to achieve customers for the first two years, the game will be different. And once we know that it's going to be a stable footfall, then the entire I mean, they they may even go with no discounts at all, and come with economic set of prices year-round so that everybody you know that kind of We have some places like you know, in Bangalore, there are some dosa like Vidyarthi Bhavan or something. Year-round, whatever happens in any part of the world, their prices will remain the same. But the footfalls are the highest. So, this this AI thing, I mean, if personally if I think, great for starting things, great for understanding and capturing people's eyes, but for understanding the psychology of a market or, you know, understanding the psychology of how an area works, I think human intervention is definitely required.

**Anand**: [68:59] Interesting. Others, any inputs? So, what you're saying is agents are better at numbers; agents are probably worse at people, relationships. Fair enough. I've added a fourth question. How do you think you, as a group, would have done compared to students? Suppose we give the same question to students. And I actually have, and I have the results. Who do you think would have done worse? Do you think students would have scored better or students would have scored worse? Now, this is the last question that I'm going to or okay, here's what we are going to do. Fill this out, and I'm going to we are going to go for a short break. The break lasts until the numbers hit 25. When I say numbers hit 25, I mean the number just below the little orange circle, when that hits 25, we will resume. And at which point, I will have enough information to be able to discuss. Uh yeah, Chumki.

**Chumki**: [70:37] Sir, just a quick question on students. When you say student, what does this mean here?

**Anand**: [70:44] Oh, college students.

**Chumki**: [70:47] So, if we have to Engineering students. Okay. If we had to run this So, basically, we are trying to compare people who are learning the subject for the first time versus who are experienced in the domain and the field. That's the comparison?

**Anand**: [71:01] Exactly. All of you have experience, varying levels of experience, varying kinds of experience, but significant experience, compared to students who have zero experience.

**Pallavi**: [71:10] But these students But these students have access to the agent, right?

**Anand**: [71:15] Oh, yeah. Exactly the same game. So, students have been told they've come on to a session exactly like this.

**Chumki**: [71:22] Hmm.

**Anand**: [71:23] And they've gone through exactly the same process. How would their scores compare? Would students should be doing better or worse?

**Chumki**: [71:35] Can we share something? I mean, can I share something right away? I mean, definitely, I will answer this other question.

**Anand**: [71:40] Oh, please, please.

**Chumki**: [71:41] So, there there are two perspectives. I think at times, having a lot of domain and context is extremely important. But at times, we get into that biasness, you know, because of our own experiences of whatever world we have seen, we tend to believe that is what it is the whole world operates in. So, if our limited view is you know, that this is how a food court in a Singapore works, for example, like this, I would only apply that, you know, algorithm in my own head when I'm assessing a similar situation versus if I would have been a student or somebody's a student who has a theoretical knowledge, the probability of having a biasness is less. So, while it is very hard to say who will do better, you know, because there are other factors which may play a role like you know, versus a person having a broader view of multiple markets versus, I would say, somebody who is just coming with one-sided view. So, I I think while the question, I mean, the binary response to that question isn't enough to justify the response, is what I'm trying to say. I mean, we can say better or worse, but both ways we can argue from the point of view that, yes, it could be better because there would be less biasness from a student's standpoint because they would only apply the theory and the technical knowledge versus it could also be worse because that person may not apply the context around the market and the dynamics and and the you know, different regional aspects of it. Like, a dosa might sell a lot in southern part of the country if it is in India versus northern part of the country, chaat may sell more. You know, so there could be a lot of arguments. So, so just I don't know if I was able to explain, but what I'm trying to say is that a binary response isn't enough to justify the question who will do better, is what I'm trying to say.

**Anand**: [73:45] Got you. So, hey, you're saying, on the one hand, training can give you an edge, but it can also blind you to new scenarios. Fair point, but it is a binary question.

**Chumki**: [73:57] No, no. Absolutely, we'll definitely answer. Yeah.

**Anand**: [74:01] So, good. I'm going to go on a break until this number gets to 25. In case it doesn't get to 25, I leave it to all of you to reach out to each other and get it to 25. That is the exercise for this break. I'm going to go off video and audio until then.

**Swati**: [76:09] Sir, can you move the QR code a little bit down?

**Bhavya**: [76:54] Swati, I have put the QR code in the chat.

**Swati**: [77:02] Can you repeat? I missed. Hello?

**Bhavya**: [77:07] I have put the QR code in the chat. You can see that.

**Swati**: [77:10] Okay, okay. Thanks. Thanks.

**Anand**: [82:22] Okay, just did a quick check. We have only 20 responses for at the most, 19 for most others. This is smaller than I need to be able to continue to the second half of my session. I had planned this for a degree of statistical significance. And 20 is 25 is bad, 20 is impossible. So, we'll probably end the session early. I will share a few summaries based on what we did in the first what you did in the first hour. But a significant portion of the learning actually comes from the second part, which looks like this was a failed experiment in that regard. So, we will close in about 10 minutes. You get your time back. And anyone wants to discuss for a bit longer, that's perfectly fine. Now, a few things interesting observations. I asked a team of students at IIT Madras the exact same question, same exercise. Let me show you the results. Actually, it was three groups. So, what you would see here on the screen are, I'll close this part. On the left side, a chart showing the average score. Now, the teams at IIT, students Bachelors in Science, not BTech, on average, were scoring the first session 92.5%, 95.5%, 94% in the third session. This group scored 88%. A little lower, it's fine, doesn't matter. The second interesting thing was how many put 20% discounts in their final plans? **It's interesting that the IITian students went for a significantly lower number of 20% discounts.** I do remember somebody mentioning that 20% discounts are probably a bad idea. Yes, they were a bad idea. Either we, as a group, are more ambitious or less aware of the impact of 20%. But either way, it's interesting that the It's almost like 50% of us had ended up putting a 20% discount in the final plans, which is pretty striking. Now, what did we think would be the answer to the third question? Let me just take a look at the results. Sharing my screen here again. So, when asked, "Would students have scored better or worse than you?" Interestingly, many of us, the majority, almost two-thirds of us, seemed to think that, yes, students would have actually scored better than us on a game like this. The data also reveals that, which is particularly interesting and has a bearing to the use of agents. I know this number is not enough for me to deal with it, but this one I'm comfortable sharing. What's your guess? Why did you think and why do you think we actually see students scoring better on this game? Opinions?

**Subramanyam**: [86:27] Most probably, I think the the students might not be thinking about the data-driven uh approaches. If it is an agent, it won't be having any um the human emotions or anything else. It It just goes with uh only the data. And then it Got you, Subramanyam, but my question was, why did the students do better than us as a group?

**Subramanyam**: [86:54] Uh Not agents. Students. Students. See, this is because See, we are also learning. See, if you see from IITians know, they are actually They are coming up with a specific uh the focused group, and then the interactions will be coming into the focus. But here, we are diversified. Um, and then just we, maybe that short span of time and then uh over the time know, we will also come to the same stage like others.

**Anand**: [87:33] Got you. So, you're saying maybe they had more time and you had less time.

**Subramanyam**: [87:37] Time, as well as that See, our experience and our knowledge uh that is also We are a diversified group know?

**Anand**: [87:47] And they have a more similar-

**Subramanyam**: [87:49] More more computer science and mathematical uh knowledge uh. They They are in hands-on as of now, actually.

**Anand**: [87:58] Okay. Got you. Thank you. That was useful, but neither is true. They actually had slightly less time than you did. And they are a remote group. They have never seen each other. Their curriculums and backgrounds are even more diverse. This is not the BTech program. This is the online Bachelors in Science program.

**Subramanyam**: [88:18] Okay.

**Anand**: [88:20] With students who don't know English being a reasonable number. There are some students who are 70-plus, retired, many working professionals. But reasonable number are students. And in terms of experience, no. The vast majority have zero experience and no prior training either. But maybe there is something in that. Chandra?

**Chandra**: [88:50] But what I feel, when I was selecting the numbers, I was going with the flow of uh my experience in terms of how I operate in expenditure, how I operate on this food and all those things. And based on my experience, Why I selected the students run through vectors? That's they have fresh mind understanding the things. Mind things will be in dominant part. A much more dominant, I'm pretty displeased need to work. So, these were my thoughts when I was selecting these options. And uh, as you rightly said, might be they have less time and things went better. Mine is Mine is, I'm not saying all, mine was based on how I operate, and accordingly, I have given in that options. So, that was my perspective.

**Anand**: [89:39] Got you. Saying, "I operated based on my gut feel, what impact that has versus students or agents, is a different thing." Fair enough. Mandar?

**Mandar**: [89:48] Yeah. So, I think including myself, I think we are more rigid. So, less open collaboration, I think. So, that is one clear differentiator that I see in students versus

---

**Mandar**: [89:59] versus experienced professionals or whatever. Less open collaboration, like we are rigid to our thoughts. And like, in that in that particular time, till we established that, like, more open discussions then So, as a team, we performed better, but personally, even I performed bad, actually. I was thinking of some strategy. So, I think that openness, over a period, I think I have lost. So, or or maybe that I become rigid, so maybe. That's the difference later I can think of.

**Anand**: [90:34] You know, it's interesting that you mentioned that. Let me share my screen and share a statistic from what we saw. My theory was collaboration will increase the scores. What we found was that at seven minutes, on average, teams were scoring around 92%. At 21 minutes, the average was around 86%. And six out of seven teams actually finished with a worse score than when they roughly started off.

So, I'm guessing to your point, there are two perhaps two aspects of collaboration, Mandar. On collaboration, more collaboration, less collaboration is one dimension. Better collaboration, worse collaboration. And nothing worse collaboration in the sense that we disagree with each other, but maybe it is just, as you said, we have our biases or less open to change. Maybe, maybe not, or it could just even be a randomness. But it's I think this is an important point. **See, we aren't necessarily irrational. We may well be responding rationally to another person's discounts. And the net result may well be destroying the collective profit.**

Put another way, maybe we have learned that in society, you have to punish somebody who is being too aggressive. Maybe the students haven't learned that lesson yet, and eventually, they will. Again, no right or wrong, but it's a possible explanation. Thank you. Akshika?

**Akshika**: [92:13] Yes, sir. So, I think a couple of what I wanted to answer has already been answered, but I also think that with students, as you mentioned, collaboration, yes, maybe students were more collaborative. And when we whenever we give a task to students, they take it as with more zeal, more enthusiasm, and more risk factor. And I think we, as professionals, when we do, we don't We majorly rely on okay, what what is We'll focus more on the output than the process, I think. The students might have enjoyed the process, had iterations, had thought processes. And we were more focused on okay, what we are going to learn from this exercise. I mean, I'm just speaking for myself. You know, that ways.

So, and also our biases that what we have seen with food courts where we have visited, so we kind of just related it to that, rather than thinking it if we have to start afresh, how would we do? I mean, that is just my personal point view.

**Anand**: [93:12] Thank you. That's interesting. So, it's the initiative, enthusiasm, energy, whatever, that can also make a difference in this case. So, what we're seeing is a couple of things: One, share my screen. A, we feel that students would have done better. At least two-thirds of us do. We actually see that students have done better by small margin of points, but statistically significant. And if we both feel this way and see this way, at least one thing to consider is how much and where does experience really count? And we certainly are hiring for experience to make sure that we have a better overall performance risk-adjusted.

Now, what is striking is we have two-thirds saying students will do better, but interestingly, we're saying four-fifths agents will do better. Meaning, we feel even more strongly that when we allow a food court to be managed by an agent, and, yes, it's a simulated food court, it will probably do a better job. Now, that, to me, is a very interesting learning point because what we're saying is, right now we're doing a bunch Maybe we shouldn't be doing those. Maybe we should let freshers and interns take over this stuff because biases, initiative, learning, maybe we should step back. We seem to be saying even more strongly, "No, I should let an agent play the game instead of me."

Probably because it won't even have the disadvantages that students do, which is it has more knowledge perhaps, it is certainly faster than them, has more initiative than them. So, empirically, I am observing that we, as a group, seem to think we are not as good as freshers or students, are not as good as agents. Are we acting on this? Yes, Chumki.

**Chumki**: [95:36] So, sir, this is again my personal view. I think the example of a food court is what probably is reflecting in the numbers, right? Had this been a banking domain or something which is like from a legal side or a medical side where the experienced people are actually into the subject for many years, would have probably, and I don't know, given a very different result with respect to the questions. And and I don't know if there is a similar study to draw more comparison into the whole study.

So, here, considering that the example is a food court, and I don't know how many of us has an experience of running a food court and food chain, we related to the example as a user, not as a on the other side of the counter, right? So, that is point number one.

So, in this kind of a situation, the understanding is that an AI probably would do a better job because they will not think that whether they're a user or they're a seller. You know, they would operate as a pure number and the information that is provided to them, both qualitative, quantitative, which will be unbiasedly assessed to come up with the final results, right? Versus students, similar situation, no biasness, just pure task-oriented approach, and the result. So, hence, I feel that the results are reflecting on that context that the approach of handling a particular situation or domain also depends on who is being put up in that domain to, you know, respond to that, basically.

**Anand**: [97:23] Got you. What I'm hearing is, "Look, if I'm an expert banker or an expert lawyer, then a student or an agent won't do as well as me. Or, forget agent, students certainly won't do as well as me. But food court, now, I have just eaten more in a food court than a student, probably. But I know no more about running a food court than they do. So, there, okay, maybe students might do better." Have I paraphrased you right, Chumki?

**Chumki**: [97:52] Yeah, absolutely. I think a set of lawyers being asked you know, given a case study on a similar situation which is from their domain, I believe the same case study given to an AI or a group of students would see a very probably a different result. Again, this is my view, I could be wrong, because lawyers would have had more experience in terms of the real-life scenarios, the complexities which they will apply in, you know, answering probably or assessing the situation. While, again, AI and students' approach, typically, if I have to generalize, is very structural. I give them inputs, they take it as a task, they assess whatever context, information, back-end you know, references they have, and they will deliver output basis only on that. The other subjectivity that comes only, yeah, is missing.

**Anand**: [98:48] No, no. Go on. Go on. The subjectivity?

**Chumki**: [98:50] Yeah, so I'm saying the other subjectivity which comes in only when you have done this day in, day out for many years will be missing for both AI and student, which an experienced person will bring in. So, essentially, what what I'm trying to say.

**Anand**: [99:05] Got you. Let me share another interesting thing, which is two-thirds of us did not use an agent to help with this. So, Chumki, what's your guess? What percentage of students used AI to help with this? Just a guess.

**Chumki**: [99:30] Maybe Maybe more relied they they probably rely more on the agents than Because, again, I feel that students are much more structured and task-driven. I think one of us also talked about it, right? I mean, their approach is more like, "I have been given a task, and I need to deliver it," right? While an experienced person has a very different approach like, "What will I gain out of it?" and we start questioning from the point one itself. So, that that's a difference.

**Anand**: [100:05] And often rightly so. In this particular case, I happen to know that it was 100%. And that's how these students

**Chumki**: [100:13] Hmm.

**Anand**: [100:14] operate. Maybe not 100%. Maybe there are a few that were taking it not because they wanted to score, but they just wanted to see the game. So, it's not necessarily 100%, but I know that all those who were actually attempting it for their exams were using agents quite extensively.

Therefore, what you said is spot-on. That it's not really These days, the comparison isn't with a fresher and an experienced person. **It's a fresher with an agent and an experienced person with an agent.** And the experienced person is using the agent, based on this group, about a third of the time. The fresher is using the agent, based on what I've seen, more than 90% of the time. So, it's really expert 2/3 versus agent 90%.

And that comparison, I actually have the results for, and you're right again. When, in 2025, we did this study, this not for food court, but for various tasks. OpenAI conducted a study, GDPval, I may have shared this in the first session, on which profession agents are better than humans at, on expert tasks. So, a lawyer, for instance, when asked, they have to advise a client concerning a series of business transactions on claim liability, advisability of prosecuting or defending a lawsuit, etc. And at that particular point, the agents were doing just about on par maybe with lawyers.

Accountants and auditors were trouncing agents left, right, and center. Industrial engineers were just way ahead of agents. Over time, that has changed. This is the picture today.

Let me go back. 2025, you see a bunch of greens. So, sales managers were doing much worse than agents. Counter and rental clerks were doing much worse than agents. Software developers were doing clearly worse than agents. That was last year. This year, there aren't many professions, if any, where the agents are being beaten by experts.

Maybe this is wrong. Maybe there are specific cases where we can find counter-examples. Maybe we should ask for better studies. Completely agree. But it does lead me to think, "Hold on. Firstly, between last year and this year, so much has changed. Should I How much should I revise my learning or bias, as some of you put it? What should I recalibrate, how much should I recalibrate? Is the student who's using the agent 90% actually better than my general manager who probably will use the agent only one-third of the time?"

Even when my expert auditor, I don't know if I mentioned this, so my auditor has considerable experience in multi What is it called? I pay taxes in Singapore and in India. My auditor is one of those few people who has experience dealing with such multi-country taxation things. And last year, I was very clear. This survey said I will file my taxes through the auditor because the auditor is better than the agent. This year, it was saying the agent is slightly better. Okay, fine. Let's give it a shot. Again, I may have mentioned this, in which case it's a repetition, but let's proceed anyway.

So, I said, let's take an experienced auditor who probably isn't using an agent two-thirds of the time. They probably aren't using an agent, versus a fresher who can audit my taxes. Who's the fresher? Me. I have zero idea of taxation, of finance in general. And I asked ChatGPT, and it said, "Here is your computation." She gave a computation. I sent my computation to her and said, "Look, there seems to be a difference."

She said, "Oh, no, no, no. That is not the case. See, what happened is, if you are getting mutual fund receipts in India for an investment that you made in India, and yours is not even an NRE account, it is an NRO account, then it will be taxed as per Indian taxation laws." Now, I didn't understand this. She said something, I took that and gave it to ChatGPT and said, "Help me understand what on earth she's saying." This is what it said.

Then I asked ChatGPT, "Acha [I see], is that right?" And it said, "No, actually not. There is a recent case, Anushka versus the State of Maharashtra, where this lady, Anushka, was in almost exactly the same situation as I am. Indian mutual fund, purchased in India, sold in India, and she's paying tax in Singapore as a Singapore employee. And according to the Double Taxation Agreement, it says that she should be taxed as per Singapore, where the capital gains tax is zero. So, you should not be getting taxed on that entire amount."

Sent her this email. Sent her this email. She said, "Let me call consult with my superior." They did, came back, and said, "Yes, Anand, you have to pay 14 lakhs less tax this year." 14 lakhs.

So, at the very least, these days, even with my auditor, very trusted, very reputed, I do a second check. We are second checking agents. Maybe should just hire a few of these college interns who know nothing anyway, give them an agent, and say, "Just can you cross-check my experienced senior professionals? Can you cross-check the lawyers that I've hired, the bankers that I've hired, the software engineers that I've hired, the architects that I've hired, the auditors that I've hired? Just anything that they're missing?" Maybe not, maybe they are.

But in this world where the other side is using agents, our side is using agents, **the comparison is never human versus agent. The comparison is human plus agent versus human plus agent.** And even the mix of how much each uses starts coming into the picture. Just something to keep in mind.

But I know we had a few hands raised that have gone down. Bhavya, I know you had a point that you wanted to make. Would you like to? And perhaps I think Mukul, you had a point as well. Go on, Bhavya.

**Bhavya**: [107:48] So, what I see is like, especially the example which you cited, like initially when the mobile came, everyone was like, "Oh, it's like that. It's like this." So, I think there is a bias now with this AI that some of them also brought it up, like if it is a student, then we think, "Oh, they know AI better." And we have a bias that AI knows much more because it's trained, rather than us.

But eventually, I think that gap will go away, like you showed that gradient, right? Like initially it was yellow and orange, and eventually now it's become a new normal. I think once we start getting a hang of it, I don't think we would talk about AI so much. And it could be a level field where we talk about, "Okay, this was what was the outcome," versus, "Okay, this person used this agent, and that's why that is the outcome." I think eventually the agents also will get better, and people also will become smarter, like that's what I feel.

And second thing is the recent outage, that actually when I was leaning on this Copilot so much in my office work, and suddenly that's not there, and I'm still expected to work, I felt my quality also dropped. So, how much we rely on the AI also matters, like we should not be handicapped. That experience should always have an edge, but how does a person preserve it, like with and without the agent? I think that will be a key challenge for us.

**Anand**: [109:21] Fair point. So, what I'm taking away is, A, it's really going to be symbiosis, but that can also lead to over-reliance. Fair point. Mukul, you were going to make a point, were you? Maybe not.

**Mukul**: [109:38] Okay. No. I just wanted to hear your point of view on the because I saw various industries and how you see, because you've been on the academic side as well as entrepreneurial, how do you see education evolving? Education, and cuz there the two extremes, right? So, there there's classroom, online, everything, and then nothing. So, what's what's your view on that?

**Anand**: [110:06] Now, I have not seen probably a few decades education being impacted anywhere near this much. There are two questions I think on the education side. One: How do we teach? If a student can go home and ask ChatGPT to complete the assignment, submit it, what are we teaching? Or how do we make sure that the student actually learns? Very difficult question.

But is something that we have seen in the last few decades. Google did almost the same thing. Student can go home, search on Google, copy-paste or type from or write from Wikipedia Wikipedia. Then what are we teaching? And then we slowly, over the years, adapted to it. AI is that order of magnitude a change on how to teach.

So, how is education evolving? An unclear answer, but the short pattern seems to be, what they're trying to teach is, what do you do along with AI? So, I will measure your learning on the parts that do not involve AI's abilities, but are your abilities. Are you picking the right kinds of questions? Are you judging the right way? Let me give you an example of that.

**Mukul**: [111:42] And and the reason I asked that is in almost all these studies, in almost all the studies the way you showed that the graph also, I have never, ever seen teaching as a profession getting impacted by AI. I've never seen it in any of the studies, including yours.

**Anand**: [112:02] I can tell you my peers the smart ones are shit-scared. The not-so-smart ones aren't yet scared enough. They're just mildly scared. It is It may not have disrupted it as a profession in the sense that people aren't necessarily losing jobs. That may still not happen.

**Mukul**: [112:22] It's more about how it will evolve. So, that's that was the point of view I was looking for.

**Anand**: [112:27] Got you. In that case, let me not bother sharing what I was going to show. My guess is people will realize that you have to start teaching stuff that agents can't do. Because if an agent can do it, my agent, your agent, what difference does it make? My calculator, your calculator, my Google, your Google, that's not a skill.

Which begs the question, what is the skill that we need to teach? And that there isn't clear consensus on because all of the hard skills seem to be teachable. The incredible thing about reinforcement learning is that if you can set an exam that can be automatically verified, then an agent can take it faster than a human and learn new skills.

Industrial engineering? No problem. Last year, they were not able to do CAD drawings. Today, they are able to do CAD drawings. Tomorrow, they'll be fantastic at CAD drawings. Why? Because you have a test that you can give the agent and say, "If you score high, you will get more GPU, energy, whatever." And it optimizes, repeats, repeats, repeats, changes its brain to the point where it does well.

Which means the only things that we can teach are the things that can't be objectively evaluated fast. That is true, and education is going there. But what are those things? There seems to be a bit of a vague opinion on, and the short answer seems to be soft skills, which unfortunately means that from a hiring perspective, we are stuck because we don't know what skills are going to matter in the future. And if at all they seem to be soft skills, for us to transition, it's going to be a nightmare.

But on the education side, let's just say that they are as far behind, if not even further behind, on the industry than the industry trying to see what exactly needs to be taught. How to teach, they're kind of figuring it out.

Yup. But I don't see the institutional structures changing that rapidly. Harvard has endured centuries and will probably endure centuries because you don't go to Harvard because they teach something good or great or whatever. You go there because the best people come there to recruit. And if you are going to go there, then the recruiters know that the best people come there anyway. So, it's like a club. The membership is what matters. Those things are robust, so institutions may not change. What changes will dramatically change, and how we teach it even more so.

Okay. So, with that, like I said, we'll probably have to end this session early. I don't have enough data points to continue on to the next part. But I will just wrap up by saying, what we set out to do today was, in a world where you have agents, the other side has agents, how do we deal with it? And a few patterns came out.

First is, we may want to question humans versus agents from the other side. We, as experts, may not be the best at solving things that are outside of our expertise. And we found that students, in a new problem, were solving it better than we as when we also see this as a new problem. And we also kind of knew it. Two-thirds of us felt that that was, in fact, the case.

What was even more striking was that they were using agents significantly more than we were. And therefore, the advantage often goes to the person who is using the agent, especially in a new area. What about existing areas? Even in existing areas of expertise, we are finding that expertise is eroding. And it may help to have a naive person who does not know best practices, who does not know have biases, who has initiative, come and use an agent to cross-question what an expert is doing.

So, that, to me, wraps up the three-part arc, which is: How do we verify an agent? How do we do that cost-effectively, efficiently? Third: Should we stop at just verifying agents? We really should be verifying the system, which is human-agent synthesis, and see what are the weak elements of the system. And a human may well be the weak element in this.

Do give this a shot. Apply this across your business, your life. See what you learn, and publish your results. The more people are able to see what you get, the better it is.

With that, we end the session. Any last questions? Yes, Akshika.

**Akshika**: [117:23] Yes, sir. I've been meaning to ask this: From the agent perspective, for example, if we take this task that we were playing around, that we have to set up a discount plan. So, when the when we do it, will we give it to the agents for the first time? They do not have any pre-trained data or any pre-learning from their last run or something, right?

So, and we, if we take it as a human approach, we might apply, you know, design-thinking principles or things around that, our past experience, our business acumen, and all those things. So, wouldn't the first round of this be more human It will be better as a human who had given the, you know, prepared plans. And maybe that can be a learning to the agent, and then they can, you know, kind of train on it. Like, is it fair to say that the first time, the first attempt, agents would have done better?

**Anand**: [118:18] It's a very reasonable direction of thinking. That's how I initially thought. And then, over time, I did a little bit of probing. What I found was agents have already read all the books that I've read, including my textbooks, slightly better textbooks than I had read. They had gone through all the case studies that I had been trained on. Ethan Mollick, who teaches at Wharton, said there is no doubt that every single one of my case studies, the agents are doing better. It is answering them better than my students. It is simply smarter than a Wharton MBA.

I have an IIMB MBA from a long time ago. So, I then said, "Okay, chalo [all right]. My domain knowledge or my MBA experience, it's beaten. But maybe if I were a food court expert, I would Hold on. Every single food court's annual report, it has read. Anything that has been published, it has read. Not only that, it has been trained on a whole series of simulations like this. What should you do under this circumstance? It has been trained on design thinking. It has been trained on aesthetics. It has been trained on game theory. It has been trained on negotiation strategy. It has been trained on like how to use and run Excel, write programs.

So, the knowledge part of it, I can I could then later on understand how agents actually have an advantage on that. But what about, you know, I mean can it quickly read the game and understand the dynamics

---

**Anand**: [119:59] understand the dynamics of it? That is where it got even more interesting.

What it did when I ran the agent against it, and which is what the students also did, was it went into the source code.

It tried to see what it could infer from the source code. Source code does not reveal much of the game dynamics, but it read every part of the game dynamics.

And said that, "Look, I can see how the calculations behind the games are running, which is exposed in the source, not fully. But based on this, the optimal strategy..." And it ran a whole series of simulations by writing programs in approximately a minute.

And in those simulations, it found that if we alternated, that is two people give a 10% discount in January, two people in February, two people in March, two people in April, et cetera, that seems to be the optimal strategy.

Not always, because the actual values of demand, that also matters a little bit. In this case, the people who are giving a discount in September, for instance, instead of October, they might earn slightly higher or lower. Okay, so individually, people's profit may differ.

Sometimes it also made sense to club them, that is January, February, two people give 10% discount, March, April, 10% discount, et cetera. It tried across a whole variety of scenarios and said, "Look, some of this is random. You can't predetermine a strategy unless you know the actual stuff."

So, it said, "In this game, your strategy should be alternate months, two people give 10% discount, the rest give zero. Nobody goes to 20%. That will get you to within 0. yeah, point Out of 100, this can, at most, cause a difference of 0.2.

If you really want to hyper-optimize for that 0.2, then give me those numbers and I will run a series of simulations in 2 minutes and give you the result." And some students did that also.

So, in short:
A. It already knows what everybody knows.
B. It can dig deeper into a specific situation, read and understand things that people will find difficult to read unless you also know software and also know food court business.

So, in a scenario like this, it turns out that using agents was the optimal strategy.

Is this always true? No.

Is it becoming truer and truer? Unfortunately.

**Akshika**: [122:41] Got it. Thank you so much.

**Anand**: [122:45] Any other questions?

Okay. Thank you, everyone. Have a good day. All the best with your projects and capstones. Bye.

**Akshika**: [122:56] Thank you so much, sir.

**Mandar**: [122:59] Thank you.

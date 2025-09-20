---
marp: true
title: "LLMs: Ask Me Anything"
author: Anand S
url: https://sanand0.github.io/talks/2025-09-15-llm-ama-gale/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
# ChatGPT: https://chatgpt.com/c/68cd1e67-ba0c-8325-94b1-e4895de93ed3
---

<style>
transcript { display: none; }
</style>

# LLMs: Ask Me Anything

[GALE Partners](https://www.gale.agency) · 15 Sep 2025, 11:00 am IST · [Bangalore](https://maps.app.goo.gl/gkfEuArBEHLwjr8K6)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Transcript](https://github.com/sanand0/talks/blob/main/2025-09-15-llm-ama-gale/README.md)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-15-llm-ama-gale/)

---

## Who’s here & format

- I note **Claude ≈ ChatGPT popularity** in this room; cool mix.
- Everyone seems to use Macs; I’m just gauging the crowd.
- **No agenda**—we’ll riff on your questions.
- I’ll try **dictate mode** so ChatGPT transcribes.
- Let’s kick off with your first question.

<transcript>
I am surprised that there are about as many people

<transcript>

I am surprised that there are about as many people who prefer Claude.ai as ChatGPT. It's nice to see that.

How many of you do not use a Mac? Okay, I see no hands. All right, I am just trying to gauge who I am talking to.

We don't have an agenda. We can talk about absolutely anything that we want. And since that is the case, might as well start with stuff that you are interested in. So why don't we go ahead and have a few questions, which I will probably ask ChatGPT to transcribe for me, rather than me. Let's give it a dictate mode.

**Host**: So, the questions that you guys had put in a form, we have shortlisted some, and we would want you to answer. So I will start with the first question.

</transcript>

---

## How will AI evolve in 5-10 years?

- I **won’t predict 10 years**; I track the next 3 months.
- I see **entry-level roles shrinking** in AI-exposed jobs. (**Edit**: [Stanford/ADP][1] finds \~13% decline for ages 22–25.)
- I stress **price–performance freefall**; near-par quality far cheaper. (**Edit**: Apples-to-apples isn’t 1000×) ([Reasoning Engine][2])
- **Frontier shifts fast**; smarter models unlock new tasks. (**Edit**: Arena ranks show Gemini 2.5 Pro leading; Flash ranks lower.) ([LMArena][3])
- I quipped **“Europe is banning AI.”** (**Edit**: EU AI Act regulates; bans only narrow “unacceptable-risk” uses.) ([CBS News][4])

<transcript>

**Question**: How do you see AI evolving over the next 5 to 10 years? What opportunities are there that you are seeing?

**Answer**: I have no idea. I can tell you how I am seeing AI evolving over the next three months. I can tell you how AI has evolved over the last few months. **That in itself seems to be news to me.**

**We are seeing finally some concrete evidence that entry-level jobs in roles that... something that AI can replace are decreasing.** So there is a job impact for entry-level areas that AI can automate. Fine. And this is after several years of AI promising that this sort of thing is coming. This is at least in the US. So that is real.

The models have been becoming better and faster. To give you a sense of how much that better and faster is, the two things that I look at are how good is the model and how cheap is the model. There was... the way we measure that is, let's start with how we measure the cost of a model. So out here, the X-axis, which I am not able to zoom into, is the number of dollars it takes for processing one million tokens. One million tokens is roughly all of the Harry Potter books put together. For a model like GPT-4, it costs $30. For a model like Gemini 1.5 Flash, it costs 3.8 cents. $30, $3, 30 cents, 3.8 cents. **Three orders of magnitude, 1000 times.**

And notice that the Y-axis is quality. I'll explain how that's measured, but if the Y-axis of Gemini 1.5 Flash is roughly the same as GPT-4... of course, one is an open model, one is a new model... but if they're roughly the same, **what it means is that I can more or less do the same things with a model that is 1000 times cheaper.** **Difference between a $1,000 budget and a million-dollar budget... For exactly the same thing. Where do you see that kind of order of magnitude difference?** Supposing somebody said, "I'm going to give you a car this month, Ferrari. It's going to cost you a million dollars," and then comes back a year later saying, "Now you can have this car for $1,000." **In which industry has this ever happened?** Keep that in mind.

And this progression, the way it's happened is, in May 2023, this is what the models looked like. There was GPT-3.5 Turbo, Claude Instant, Claude 1. And then new models kept coming up. GPT-4 was a leap. GPT-4 was a much higher quality model and could do things that otherwise you didn't even think they could do. And keep this quality jump in mind because **when the model becomes smarter, it starts being able to do new things that otherwise were not possible.** And when you can think that it could do these things... **Arguably, we still haven't figured out anywhere near what GPT-4 is capable of.** We're still exploring the fringe of what it can do.

And then other models started coming in where we had Claude 3 Opus which was actually even better model, albeit priced slightly more expensively. Claude 3 Haiku was a bit of a leap in the frontier. See the stuff in green are the models that are Pareto optimal. There is nothing that is both cheaper and better. If that's the case, there's no reason not to use these models. Why would I ever use, let's say Mistral 8x7B, when Claude 3 Haiku is both cheaper and faster?

The frontier keeps evolving, and Claude 3 Haiku was a big jump in that, but then we had smaller models like Gemma beating it. GPT-4o Mini was another big leap, much smaller and much faster at that price. And then over time, you had the DeepSeek models pushing that frontier a fair bit. And now we have, I guess, a smooth frontier. This is as of a few weeks ago with the Qwen models, GPT-5 being one of the better models in terms of quality. Gemini 1.5 Flash still occupying the frontier on inexpensive. But this is over less than two years, the kind of evaluation on the frontier.

AI has the other property that **it's a human-like intelligence and a scalable thing that I can deploy in thousands of computers or a million computers very easily. And that's something very hard to wrap our heads around.** We're still trying to figure out how and where to use it. People ask me questions all the time about anything, including what the future of AI is. My reaction is, I don't know, I'm going to ask ChatGPT and get back. Why don't you ask ChatGPT and get back? This is what used to happen in 2000. Google had just become the dominant search engine. People would ask me questions, and why are you asking me? Ask Google, that's what I'm going to do anyway. And for the next five, maybe even 10 years, often all I would do was do a Google search, copy the first few results, and send it. Initially, I tried sending them the Google search results page. That doesn't work as well. **For whatever reason, they felt that if I do that search and copy-paste the results, it is better than them seeing exactly the same thing.**

It's happening for ChatGPT also. I get into conversations. I was... in the beginning of the year, I had taken up a series of goals, actually. I've taken up 15 goals, and one of the goals was to co-present with an AI. And at the beginning of the year, I think it was January, I did co-present with ChatGPT. And the interesting thing was, whenever people realized that it was a response from ChatGPT, they'd say, "Oh, ChatGPT." Whenever I said practically the same thing, they said, "Oh, that's insightful." Not at all different.

When I talk to Andrew, who's the CEO of Stripe, I tried this experiment. I used all my brains and came up with stuff, and he said, "Maybe." When I would pose the same question to ChatGPT, I would have posed the question while I was thinking, so it comes up with reasonably good answers, and then I would read out the answers. "I like it, that's a very smart thing, I think we should always come back to you for more such bouncing off ideas." But you have as much access to ChatGPT as I do.

</transcript>

---

## Use AI (quietly)?

- I learned to **use AI—don’t announce it**; people judge differently.
- In my IITM course, **copying & ChatGPT are encouraged** to get the job done.
- I set **hard, collaborative exams**, even “hack it if you can.”
- **Few actually copied**; letting others copy improved the author’s work.
- Net: prioritize **outcomes over purity**; train collaboration.

<transcript>

After that, I learned, and I started telling people, "**Use AI. Don't tell people that you're using AI.**" You have several reasons for doing this. I'm just giving you one more reason to do this. You don't need to tell people you use AI, what is the problem? If they want you to use AI, they will tell you to use AI, or they use AI. What are you, the middleman for?

And despite this, people are not using AI. I run a course, "Tools in Data Science." This is something I run at IIT Madras. And here are the instructions for the course. This is all broadly related to where AI is going. So completing answering the question. But one of the instructions in this course is that **copying and ChatGPT are allowed and encouraged.** This instruction has been around for some time. You can copy from your friends and relatives. You can work in groups. You can use the internet. This includes the exams. You can use WhatsApp. You can use ChatGPT. You can use your notes, your friends, your pets, whatever you want. I have practically told them you can pay somebody to take the exam for you if you want. **Get the job done.**

Why? There are enough courses that teach ethics, there are enough courses that teach not copying, working by yourself, making sure you get the job done. And after having gone through all those courses, those people come to recruit and get recruited, come to my team, and then they say, "I will solve the problem all by myself. I will not ask for any help. If I get stuck, I will eat my own shorts and I will never ever make sure that I've copied from anyone." Get the job done. Just get the job done. I really don't care how you do it. If you can pay somebody to take your exam, come to my office, pay somebody to do your work for you, I don't care. My salary will be used the same. I don't care.

So this course is intended to teach people to get the job done. And for this, one of the things that I've been doing is making the exams harder and harder and harder and harder and harder. I copy-paste the question, put it into ChatGPT, see if it gives the answer. If it does, then I triple the number of questions. There is a remote online exam, 22 questions, 45 minutes. Each one of those questions is approximately a small research project. It is hopeless. The only way you can solve this is if you create a group of 30 people, each one gets to solve one problem, they all pretty much create the code to solve each of those problems, share it between themselves and submit it. There is no other way. There is only one other way to solve it. The other way is... and explicit instruction says that you can hack the exam. If you're smart enough to know how to hack it and I'm not smart enough to prevent it, then I pass.

Now, what exactly happened when I did this? Okay, quick guess. What percentage do you think copied from each other? How many people think it was more than 80%? About five hands, okay. How many people think at least half the people copied? Okay, about 20, okay. How many people think less than 30% copied? 5%. The 5% of people who think less than 30% copied are correct. This is what it looked like.

This one group submitted exactly the same answers, 100% exactly the same. They are all on one WhatsApp group. The person in green was the first person to submit. The people in... the person in yellow was the first copier or first follower or whatever you call it. The rest of them then subsequently copied. There are other smaller groups, so this is another smaller group that copied from each other, this is another smaller group that copied from each other. The vast majority of them, the ones in gray, neither copied nor allowed anyone to copy from them.

What does the performance of these students look like? The ones who did not copy nor allow anyone else to copy scored the worst, about this was about half the submissions. Those that were the first to copy... and here I've used a reasonably liberal interpretation of what copying means. Here code even approximately looks like the other person's code. You may not have copied but at least taken advice. So I set the threshold like this, meaning code is kind of similar, so maybe they took advice, I don't really know if they took advice, but there's a decent chance that at least they helped each other if not copied. And at that threshold, those that were the first to copy from someone else, they scored slightly higher. Those that copied late scored even higher. Understandably, you have more people to copy from, you say, "I like this style, I like that style. Oh, this thing worked for me, at least that worked for me." They just saw this. **The people that scored the highest were the ones who let others copy from them.**

And that's an interesting observation, because what that, I'm guessing means is somebody would have tried it and said, "Oh, but that didn't work for me." "Why? Oh, I see, okay, fine, you had this problem, let me fix that." "Oh, but it didn't give me such a good solution." "Oh, let me fix that." And you get all that feedback and start improving and before you know it, that person's solution improved. I'm guessing that's the mechanics that was happening behind the scenes.

But where I'm going with this, this was an aside, is that on the one hand, I'm saying AI is such a great thing, and all of you should use it more, you don't have to tell people that you're using it more, but I'm also saying that even after telling people they can do these things, we are well-trained. You've seen _3 Idiots_, right? The distinction between educated versus well-trained is something that would hit home. Something like that. We have a thousand things to use, this is one more thing that needs to get added to our life. So, **where do I see AI going? Nowhere... as long as people are around, it will be where it is.** It will come in, it will gently start seeping into our lives. What are we? Are we going to let AI disrupt our lives just because of somebody else's telling you? We will resist. How will we resist? We will bring in regulations, ban AI. The entire continent in Europe is doing that. We will start disrupting it with concerns around security and privacy. How many organizations do you think have... allow employees access to ChatGPT? You are one of the very few that I've spoken to. You are the only organization that I've spoken to that allows employees to access ChatGPT. It's almost a shock to me because I came very prepared with a long set of things that ChatGPT can allow you to do if you don't have access. And then you said you have access.

So we will put in all the roadblocks. In short, adoption of AI is very different from the technology of AI. **The technology of AI is going faster than jetskis. It is going faster than anything that I've seen. And I've seen a lot. The adoption of AI is going at a normal pace.** So in 5 to 10 years, it will be like 5 to 10 years after the internet. Lots of people will be using it: email, web access, a few e-commerce sites here and there, some job loss. The internet had its own share of job losses. Desktop publishing had its own share of job losses. It'll all be there, and then people will find different roles. That's all. Very long answer to the first question, but yeah.

</transcript>

---

## Non-technical adoption blockers?

- **Client bans & privacy fears** block usage—even on public-data tasks.
- Teams are **busy and risk-averse**; “don’t be guinea pigs.”
- Leaders demand **clear ROI**; POCs rarely cross into production.
- **Change inertia** is real; even trivial logins stall behavior.
- Executive **ownership nudges adoption**, but skills ramp lags.

<transcript>

**Question**: Here we go again. We have other questions as well. I think first you were talking about adoption. So from your experience, what are the biggest non-technical barriers to successful AI adoption?

**Answer**: What are the biggest non-technical barriers to successful AI adoption? I'm in the middle of a talk, so I don't really have much time to read your answer. So make sure that you give me a very concise list and the most important points that I should be talking about. But I want you to think a lot, do a lot of research. Make sure you find the most relevant points for Gale Partners, whose business is data science and technology in general. So keeping that in mind, give me a summarized list of points for this. Okay, it's thinking.

I don't like doing work. It's paying $20 a month for this. And some people have been paying $200 a month for this. But this is the problem, right? The screen is out there, it takes maybe two, three minutes to think, it comes up with good answers, but so usually to keep people entertained while this is thinking and this sort of a thing goes on in the background, let me share what I have seen, which will maybe even be lousy answers. But biggest non-technical barriers to successful AI adoption: clients, regulation, fear of the unknown, probably. Within our company, I said that when I was in Vietnam visiting our Hanoi office, I asked the team how many of you are using AI. One out of five projects were using AI. Why? For four out of the five, the clients had said, "Do not use AI in this project." Why? Because the data might go and get trained somewhere. But we are the only client that sends public data. One of the teams, their job was literally to scour public data and do outreach, and enter the data. It's all public data. "Oh, but we have to check with our AI team, we have to check with so and so." Fear and uncertainty, in short, is another of the biggest values.

For another team which had access, we were checking with them why they aren't using AI. The project manager very clearly said, "We have tried AI several times, didn't work. My team is busy. We don't want to be the guinea pigs." And different variations of the same. People are busy. Now figuring out how to learn something new takes up a lot of effort. Let me tell you how much effort. At home, we have one Amazon account, which is on my email ID. My wife does not have a separate Amazon account, which means that if there is any shopping to be done, it has to be on the Amazon equivalent in Singapore, which is Shopee. So if she needs to log in to Shopee, then she needs to log in through my Google account, which has single sign-on, and therefore I need to approve on it through my mobile. It's a pain, she needs to know, shop at all. Now how difficult is it to create a Shopee account with a Google account? The answer is one click. For the last three years since we moved to Singapore, she has not created an account. She would call me and tell me, "Put that thing." I am no better. In our bank account, her phone has the token for any payment that would go. How much effort is it to install that on my phone? Three years, I have not done that. **And I'm going out preaching to people, 'You should adopt AI.'**

Okay, this is a good part. No clear ROI. The good part is most CEOs are saying, "AI, AI, AI." And there's at least some ownership. I'm giving a talk next week to an organization, whose CEO was shown by another CEO how he could code by himself. So he started coding. Now he said, "All of you business leaders should start coding." The HR person said, "Anand, we want to talk. The objective of the talk is to satisfy the CEO saying, 'We have been taught how to code,' not necessarily that we should code." But here's the thing, somebody's pushing. 5% will learn, 10% will learn, at least get exposed. Ownership makes a difference.

Where is the ROI? Everybody's creating proofs of concepts. How much budget has this reduced? How many projects has this actually impacted? Show me the bottom line. And we started doing studies, we find that all of those are just barely going into production. We don't have anywhere near enough data to show the ROI. Wait, the project manager who said my team is not going to be the one who does these experiments, we are busy, is saying exactly the same thing: show me the ROI. And then tell it to the teams that will say show me the ROI in my kind of project. Then they'll say show me the ROI in my project. Doing a small POC, the usual objections. I'll let you read through the rest, you can read faster than I can narrate, but these are some of the common reasons they're saying.

</transcript>

---

## Off-the-shelf or custom?

- Default to **buy services**; self-hosting is costly/complex. (**Edit**: My study estimated 60–700× higher TCO at small scale.)
- **Run your own** only for data-sovereignty, air-gapped, or learning.
- **Fine-tuning** helped niche tasks briefly; **frontier caught up** in months.
- **Wait 3–12 months** unless you have unique, defensible data + budget.
- Expanding token windows can **obsolete bespoke hacks**.

<transcript>

**Question**: When do you prefer using off-the-shelf AI services versus building custom models, and why?

**Answer**: I put this on LinkedIn. **"If you run your own models, the cost... is approximately anywhere from 60 to 700 times higher."** Or it was in April, now I'm sure it's even more skewed. Why is that? GPUs are expensive. We absolutely do not have anywhere near the kind of scale to run GPUs. We absolutely don't have anywhere near the technical expertise to run them efficiently. So from a cost perspective, it never makes sense to run your own models. I think I'm running part of my talk shortly. If I'm not going to run my own model, I obviously cannot run my own trained model in many situations.

So when does it make sense to run your own model? If you cannot send your data to an existing model. You're a government running government secrets, doing STR analysis, you just feel that this stuff you don't want to send to any model. You are a corporate whose data is so secure that you run your own cloud, you don't even use Google or Amazon, fair enough. You're a hospital emergency room that, forget these, the only infrastructure that exists inside the emergency room is airlocked and can be on 10 devices. These are real situations. Okay. And or you are an institute, a software company, or a research university that is trying to learn or teach how to train models. These are valid use cases for spending 60 to 700 times more money, not otherwise.

Training your own model, when do you train your own model? We tried training our own model for Dutch technical term translations. The problem is when translating research papers into Dutch, the technical terms were very badly translated. So much so that they get translated with hyphenation. There is a convention to do the hyphenation, and we're getting both the hyphens and checks at the right spot. Plus a lot with professional quality LLMs were not very capable of doing that. So we got training data, we pushed it into... Gemini had the capability to train models, OpenAI has the capability to train models. We took the training data set, trained the models. Cost us a certain amount of money, not too much. And the time, when I say not too much, I mean it's only 10 times more, not 60 or 700 times more. And the results were 5% better, 10% better. We were about to go live. Six months later, the model itself started doing good hyphenation properly.

Another case, we were converting XML to a different XML format. Problem is the input XML is massive, the output XML is massive, the token size of the models was not large enough. So we did another three-month project: January, February, March, and got it to the stage where it kind of could get some improvement. April, GPT-4.1 was released and the entire XML would fit. Three-month project gone down the drain. So what we've learned is, **if you know for sure that there is some data that you have that nobody else will ever have, and that data does not have any similar substitutes, cannot be synthetically generated, and there's a client who has a ton of money who's willing to pay for it, then train. Else, wait for 3 months to a year.**

</transcript>

---

## Biggest paid-media risk?

- **Platform automation may disintermediate agencies** and squeeze margins.
- **AI overviews likely reduce clicks**; evidence is mixed, publishers report hits. ([World Health Organization][5])
- Shift from SEO to **LLM-optimization (AIO)** changes distribution. ([CDC][6])
- **Assistant-mediated commerce** will move purchases inside assistants.
- So: **own data, SQL, experimentation**, not just decks.

<transcript>

**Question**: What's the biggest AI risk in paid media that brands are not thinking about today?

**Answer**: I'll let you read through the rest. You can read faster than I can narrate. But these are some of the common reasons they're saying.

While we wait for this, let's go back. What are marketers likely missing? **The biggest blindside isn't in terms of pixels. It's AI platforms taking over your audience, your agency role, and your reason for existence... The problem is not that digital marketers are missing stuff. The problem is there are no more digital marketers** whether they belong to your company or any other company.

So what should we do? Brush up your SQL more than your presentation skills. It may take some time maybe, but that is the reality. The thing is, there are constraints that any organization operates under. You have a set of customers. You have to do what you can, delivering to those customers. We are in the same space. Now within that constraint, we are operating in a regulated industry, every industry has its set of regulations. We have processes that work around those regulations. Some new company will come in and say, "Look, I can do 60% of this at 0.0006% of the cost." And there'll be a few people that shift. That's exactly how Google took over the bulk of advertising. That is probably the biggest risk. That apart, there are a bunch of these, let's say AI answers squeezing your distribution and attribution. So the fact that AI overviews are anyway not going to be sending people to the platform means that you know there's a certain amount of LLM optimization instead of search engine optimization. Now how does one monetize that is something that organizations are thinking about. Cloudflare seems to be at the forefront of thinking about how we can actually monetize something even though it goes to the LLM. Assistant mediated in-app commerce, yes. Where we buy will change completely, what kind of technologies do we have to deal with that? I think that's a good one. Platform automation disintermediating agencies. This is clearly the biggest one. I'm not going to go through the list. A different question will probably give you better answers, but I am entirely convinced that this is the biggest one.

</transcript>

---

## Will AI erode self? Bias?

- **Yes—it already happens.** We’ve long outsourced judgment to tech.
- **Bias via AI** echoes **search-engine era** worries; benefits still won. ([roadsafetyngos.org][7])
- I used **“10,000 road deaths/day.”** (**Edit**: WHO ≈ **1.19M/year ≈ 3,260/day**, not 10,000.)&#x20;
- We already **live by machines** (calendars); AI is the next one.
- Convenience wins; **we adapt**.

<transcript>

**Question**: Can we lose our sense of self because we are always asking AI for everything?

**Answer**: **Yes. And it's already happened. We've always done that.**

**Question**: As an extension... do you believe that we are going to be very biased because of what AI is probably going to be telling us?

**Answer**: **Of course. And it's already been happening. 20 years ago, AI was replaced by Google.** And this is exactly the question people would ask. The internet has anybody can write anything there. Can we trust anything? How do we rely on it? And then Google started making it so convenient that people said, "Oh, but can you rely on what the links that Google are pointing to are saying?" And yet we are. And we see the problems that are coming out. Fake news being just one example, but we still are. Because the benefits outweigh the costs.

I was at a PyCon talk yesterday where one of the keynote speakers said, "Imagine if, 100 years ago, or even now, somebody came and said, 'I'm going to give you something magical that will improve employability, that will improve mobility, that will improve, that will dramatically reduce social divides, that will significantly increase the salaries of the vast majority of people, that will improve the economy by 20-25%, but it will end up maybe killing 10,000 people a day.'" Would you go for that? And most people that are posed with this question say, "10,000 people a day? Every day? Are you kidding? No, there's no way we will go for it." These are automobiles. **We've accepted it. Yes, we think 10,000 people a day is worth it.**

I'm surprised at how much we are willing to give up for convenience. Maybe not surprise, maybe I'm a good participant. So there was a time when we would say, "I need to have my own freedom." And then factory said, "We will give you salaries, but you have to work 9 to 5." Kids when they get into school, that regimentation is pretty tough to see. But that is the norm, and we're not that much better. My entire life is driven by a little calendar that tells me what I should do next. I even update my own calendar myself so that it can tell me what I should do next. How beautiful is that? People look at retired people and say, "We are slaves to machines." **It's already happened. This just happens to be a different machine.** Changing machines, nothing more than that, albeit a much smarter machine. I'm not seeing this as any different. I am loving the process. Because this is the one machine that I can feel good about myself as well. It'll say, "Oh, wonderful, that's such a brilliant idea. What you're thinking of is maybe reducing your intake to one meal a day for intermittent fasting, but it's a fantastically good weight loss. I think you're really clever to have come up with that." It almost said it, so it said exactly this, verbatim.

</transcript>

---

## What can’t AI do?

- I keep an **“impossibility list”** and strike items off often.
- I claimed **perfect text in images** via SeeDream. (**Edit**: Seedream 3.0 reports better typography; “perfect” is vendor-claimed/context-dependent.) ([Instagram][8])
- **Start simple**: install a top model and talk to it.
- **Forgive early failures**; don’t force adoption.
- It’s fine to **adopt late**; outcomes > timing.

<transcript>

**Question**: Here are some areas where you shouldn't use AI if you plan to keep your thinking sharp. Is there anything that AI cannot do?

**Answer**: I'll take the second question first. We don't know what all AI cannot do. That is roughly the same as saying, are there things that computers cannot do or are there things that the internet cannot do? Yes, maybe, but there are two problems with that framing, which is we don't yet know what they can do in the first place, and we don't yet know how we can predict what they will not be able to do in the future. So any answer also ends up being invalidated. I usually try to phrase the question slightly differently, which is what are things that I've tried that it failed at? Which is the impossibility list that I maintain. And that list is great to strike off of. So what was, for instance, on my impossibility list about eight months ago? It cannot draw cartoonish animals commercially. And then a whole bunch of models came up that completely invalidated it. It cannot create video, sorry, images with perfect text as of, even the model models tend to make a few errors, GPT-4, DALL-E and so on makes a few mistakes here and there. SeeDream which was released by one of the Chinese labs last Wednesday or Thursday, apparently is able to generate extremely intricate, detailed, almost photorealistic manuals with not a single mistake. So that's another one that's struck off my impossibility list. So I don't know what all it cannot do. I just keep trying, so it is just so detailed that is the list.

What should we use AI for if we are about to lose our sense of self? What's the starting point? The easiest starting point is to install ChatGPT or Gemini or Claude and start talking to it. Another starting point would be simply to listen to somebody who's crazy about AI and spend some time with them and ask how they are doing it. Maybe one of those things will stick. Third, forgive AI. Meaning, you try three things and it doesn't work. It's okay, let it be. Something else might work, might not work. Nobody is forcing you to use AI. And this is often a mistake I've seen people make, not this audience, forcing, and by force, I mean nudging very strongly. Hey, are you not using AI? I was talking to, I was implicitly with a whole bunch of projects like that that for checks or whatever. Nothing wrong with not using AI.

The reason I say that is not because I feel that statement in itself, but because it is the right statement to make to get people in. If somebody is worried that they are not using AI or somebody sees a competitor seeming that they are not using AI especially their social media channels are showing that I'm not using AI or that you feel forced in some way, pushed in any way, then when something doesn't work, your likelihood of trying it next time is lower. So what is a good way to start using AI? Not feeling worried that you're not using AI. It's perfectly fine. Society will move at its pace. I am no genius at that. In fact, my mobile adoption was pathetically late. My manager basically said, "Look, Anand, you are either going to get fired or you're going to buy a Nokia phone." I bought a Nokia phone. It's okay, nothing wrong.

</transcript>

---

## How to keep up with AI news?

- I **use AI to track AI**: scheduled curation across sources.
- The problem flips to **too much good content**.
- I **automate workflows**: transcripts → lessons → try-out lists → templates.
- I **let AI schedule/alert** and pre-fill evaluations.
- When overwhelmed, I **ask AI to raise execution capacity**.

<transcript>

**Question**: How do we keep up with AI because every day there's a new thing coming up, every day there's somebody who's presenting a different different view. How do you cut the noise and know because all of us have limited time. So how do you know what you should focus on when?

**Answer**: How do you keep up with AI when things are moving so fast? Use AI. Seriously, this is something that I'm not saying anymore to me, I'm preaching it to the choir here. So on ChatGPT, I have a scheduled task that goes through GitHub repositories, that goes through Hacker News, that goes through Simon Willison's blog posts, that goes through Ethan Mollick's tweets or sorry, posts on Twitter. A whole bunch of sources. I've also told it what I am interested in and what I'm not interested in. And I say give me a list. It's fantastic because it's reasonably curated for my interest. So I have now suddenly not short of high-quality content to read. Now problem number two starts. Now I have too much good content. Earlier I needed to put in effort to get good content. And it turns out that putting that effort was a good sleep breaker. Now I'm faced with a flood of good content. So my notes are exploding and I have a tasks list which has gone to 168 items or so, but 80% of these were created yesterday, that I need to update my AI coding rules with something, I need to form a habit of automated code review so that it auto reviews every single commit that I make, on and on and on and on. So now, and all of these are good validated things.

So how do I deal with this? I asked ChatGPT. Now I have too many things to do and these are all high-value stuff, so don't give me all this prioritization bullshit. I want to increase my execution capacity. How can we do this? And it gave me 10 ideas. One of them stuck a chord. It said, "Habitualize this and automate." Meaning, you shouldn't do stuff. The AI should do the work for you, and it should be triggered not by a human action, you had a real memory anyway. It should be entirely automated. Okay, that sounds like a good idea. So two weeks ago, one of the things that I did was every meeting that I go into, the transcript of that meeting gets auto-recorded and auto-summarized with a specific set of actions. For example, I was at the PyCon talk yesterday. Now in this talk, it auto-transcribed the talk. So the whole thing is available. Now I'm not going to read the transcript, I have a terrible memory. I'm going to have it read the transcript. And it came up with a set of lessons. And I also told it how to structure the lessons. Give me the top insights, a big useful and surprising. Give me things that I can try out as experiments. I also told it, "Put a star against the really high... really good ones, powerful ones so that I can filter for those." Now every meeting I go, I have an experience, which is again overwhelming. So I asked it, "What do I do?" It said, "Well, why don't you extract from those, filter for what is easy, what is automatable, and create another list?" So that is also now automated. Level three is a tryout list, which has for different discussions, all of the things that I had planned to try out, which I can filter for. Now this again becomes difficult. So I passed it to ChatGPT and said, "Is there some way I can automate all of this?" And for that, it said, "Okay."

It said, "See, all of your stuff falls into high-risk stuff where you want to create some media or a post that you want to publish or a demo that you want to create or a KPI that you want to play around with, a whole bunch of things." So what I can do is build a script that will scan your notes, put it into one of these categories, and then create a template for each one of those. So now I'm in the process of creating templates that will automate the execution of some of these. Now like blog post analysis at least giving the draft is relatively easy and I haven't gotten around to it yet. But this morning, one of the things that I was doing was creating a template that will automate tool evaluation. I keep checking out different things on the AI side, is it good, is it bad. So the prompt that I'm currently using for this is...

Here's my prompt. Evaluate a particular technology against some criteria. There are a bunch of guardrails. The things that I asked it to evaluate might be techniques, command-line tools, libraries, frameworks. These are my preferences, evaluate based on these preferences, blah blah blah. And I tried it on three tools. Rubbish, giving me too much detail. So now I have to iterate on this prompt and figure it out. But here is the thing, now my workflow is AI finds stuff, AI filters stuff, AI collates it, AI converts it into an executable template, and in a few of these cases, the AI does the job by itself. I have it schedule my calendar automatically, saying here are... here is how I, for instance, because I tend to forget meetings a lot, here's my process for scheduling. Set up alarms one minute before the following times: 3 p.m., 3:30 p.m., and 4:30 p.m. And then the painful wait... Oh no, it's not speaking because I disabled the speaker, but it scheduled the alarms. That's pretty much it. I said speaking to AI is almost part of my existence and the one thing that I should take away, I'm repeating that. But in short, when you feel overwhelmed, use AI. Actually, you can remove the "when you feel overwhelmed," at least you can remove the "when you feel overwhelmed." When you have a question, ask AI.

</transcript>

---

## Spot problems & ideate?

- We often **miss that we need help**, not just tools.
- I **feed life logs** and ask for optimizations + wild ideas.
- My **ideator** combines notes into **big, non-obvious concepts**.
- I cited **LLMs topping JEE**. (**Edit**: No official evidence of AIR-1; benchmarks show mixed results.) ([Stanford Digital Economy Lab][1])
- I **rate ideas** and throttle usage to avoid overwhelm.

<transcript>

But here is the problem. There are two things that we don't often recognize. One, that we should ask AI. That is obvious. The second is that we even have a problem. Very often, we don't even realize that I'm in this situation, I need help. Even the most attuned of us find it difficult to recognize that there are opportunities for us to receive help, especially with technology like AI that we don't even know what all it can help with. Again, we know one knows what all it can help with. There I'm finding two things useful. One, passing it all of my life info. I don't know where I have a problem, but you are smart, maybe you can figure out where I can optimize stuff. Second, hallucinations, which is a synonym for creativity, and that is wonderful. You can ask it for creative solutions. Go crazy. So I have an ideator tool. And I'm finding that my job as an innovator is now securely dead. All I have to do is go to this ideator, which takes my extensive notes. Keep in mind that my notes increasingly are not just what I have typed, but it's transcripts as well. So in a sense, LLM-generated data. And it randomly picks up a couple of things, or I can search for something. So let's say I want to take something that I have learned and combine it with good questions to ask.

Here are two ideas. Last year, LLMs were able to solve JEE problems and ended up becoming all-India rank one. Here's something else from prioritization, start with why. Can I convert this into a business idea? A strategic business plan? And generate an ID. What this does is it takes those two, simply copies it into ChatGPT. And I'll play this and then talk about it. It says, "You are a radical concept synthesizer hired from some human experts." I have no idea if it helps or hurts, but generates some big, useful, non-obvious idea that's aligned to the two things that I told you. Here are the two things that I tell it, and I give it some instructions. You saw how I was researching with different kinds of prompts and what works and so on. So some of this seems to work reasonably well. Come up with five ideas. And I tell it ways in which it should be creative. And then score in this particular way with the top score, and then tell me what's the top insight, what I should create, blah blah blah. I've run this about 15 times over the course of the last two months. Why only 15 times over two months? Because every time it gives me an idea, it blows my mind. And then at least an hour is gone. Because just... okay, I have to do this, I have to do this. So I've been really limiting myself from the use of this. Not because these ideas are all necessarily good. I just get overwhelmed easily. And some amount of practice, skepticism, say, okay, this is a good idea. Let this become a $50,000 business. Let this become a $5 million business. We should all just elevate ourselves to that level. It'll take time. We are not that fast. But it's still thinking. But yeah, this, the whole theme of ideation is another possibility.

</transcript>

---

## Vibe coding in production?

- Treat AI like **adding junior devs**; gains vary by task.
- **Brooks’s Law**: adding people to a late project **makes it later**.
- Choose **where AI fits**: gen code, tests, reviews, docs, specs.
- Keep **classic PM discipline**: trust only delivered, validated work.
- Rule of thumb: **use AI more for validation than generation**.

<transcript>

**Question**: I have a question regarding the adoption of 'vibe coding' in teams or projects or any implementations that we are doing. Let's say we ask some tasks to be done, we have ChatGPT and other tools to get the code, and then they go over it, code it, push the code, and then that gets deployed and it works too. But when it comes to a productionized thing, that is where they will start experiencing the problems where they cannot debug it or debug it very well. So rather than reducing our efforts and then getting the things done, there are many cases where it impacts our delivery in those zones. How do we manage these sort of situations?

**Answer**: Vibe coding versus AI coding, the difference being in vibe coding, we don't even look at the code. In AI coding, we are using AI as an assistant. **The ability for AI to improve our productivity can roughly be equated to adding a few junior developers to the team.** Now, let me rephrase that question. We added a few junior developers and we find that when they work, works into production, it's not actually passing. And therefore, adding people to the team has actually made the project slower. What do we do?

Read the 1970 book by Fred Brooks, _The Mythical Man-Month_, in which one of the key learnings was, **adding people to a late project makes it even more late.** So this is not new.

What we're finding is that we don't really know the mix of people to put into the team or the mix of AI capabilities to bring to the team. Do we use it for code reviews? Do we use it for code generation? Do we use it for generating test cases or do we use it for generating functionality? Is it better at generating the front end or is it better at generating the back end? Should we generate synthetic data or should we generate requirement specs? Should we have it generate documentation automatically or should we have it review the documentation that we have put into the code? All of these are different ways in which we can apply AI to a software project. We haven't yet gotten enough experience to know what is a better answer for a given project, nor has the ecosystem been stable enough that what we learned three months ago remains valid today. These are real-world sources.

How should we deal with it? Classic project management principles. This does not change since the 70s, which is, don't trust anything unless it has been delivered. Validate, cross-check. What happens is the client-facing teams say, "This has to be done much faster." The inside developer says, "I have gone from 1x to 10x more productive." Therefore, the project manager in the middle says, "Okay, I don't trust 10x, but 2x?" So I'll reduce the project budget and half. Not just for the development, but also for QA, for documentation, for the requirements, the whole thing. And it ends up breaking. So the developer finds that the first project actually works, gets really motivated because they're able to integrate it into user templates in roughly a promised time which is dramatically faster. And now all the rest of the timeline is a grid. How do you find more projects like this? That particular project might work because it's getting stuck. The second project, the code itself is not going that fast. The second person has not learned how to use AI as effectively as the first one, or the circumstances of the second project are different from that of the first. It's exactly the same as when any new technology takes over. Most of the new technologies were promising 30% improvement, 40% improvement. Here, people are seeing, in some cases, 100x improvement. And in some cases, a 2x, 3x slowdown.

**How you solve for it is a classic organizational management and change management problem that is... but the broad rule of thumb that I would say is, focus more on using AI for validation than generation.**

</transcript>

---

# LLMs: Ask me Anything

[GALE Partners](https://www.gale.agency) · 15 Sep 2025, 11:00 am IST · [Bangalore](https://maps.app.goo.gl/gkfEuArBEHLwjr8K6)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Transcript](https://github.com/sanand0/talks/2025-09-15-llm-ama-gale/blob/main/README.md)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-15-llm-ama-gale/)

---

## Quiz

1. Compute the _input-token_ cost ratio between the highest ELO OpenAI & Gemini models. ([LMArena][3])
2. Cite 2 evidences for AI Overviews’ impact on click-through, and explain why their conclusions differ. ([Search Engine Roundtable][26])
3. Given Stanford/ADP findings on early-career employment in AI-exposed roles, design a mitigation plan for graduate hiring. ([Axios][11])
4. Outline a project workflow where _generation_ assistants help without raising defect risk. Reference a study. ([arXiv][22])
5. List three AI practices the EU AI Act prohibits and one “high-risk” use that is regulated but permitted. ([Artificial Intelligence Act EU][27])

---

## Errata

- **“Entry-level jobs are decreasing (US)”** — Directionally supported, but the magnitude varies by method. Stanford/ADP research finds 13–16% declines for ages 22–25 in AI-exposed roles since late-2022; not a general collapse across all entry-level work. ([Axios][11])
- **“1000× cheaper: GPT-4 vs Gemini 1.5 Flash”** — Ballpark overstates today’s gap. OpenAI’s original GPT-4 input was \~\$30/1M tokens (Mar 2023); Gemini 1.5 Flash (Sep 2025) lists \~\$0.075/1M input tokens. That’s \~400× on inputs (not 1000×), and outputs price differently. ([OpenAI][12])
- **“Gemini 1.5 Flash ≈ GPT-4 quality”** — Current open benchmarks place top models (e.g., Gemini 2.5 Pro) above Flash; Flash targets low-cost throughput, not state-of-the-art quality. ([LMArena][13])
- **“Europe is banning AI”** — Inaccurate. The EU AI Act bans _specific unacceptable-risk uses_ (e.g., untargeted facial scraping, some emotion inference) and regulates high-risk systems; it does not ban AI broadly. ([European Parliament][14])
- **“Self-hosting is 60–700× costlier than API”** — This was published as a cost study by the speaker; it’s a useful heuristic but depends on scale, utilization, and engineering maturity. Treat as scenario-specific, not universal. ([Binadox][15])
- **“AI Overviews will squeeze distribution/attribution”** — Substantiated for many publishers (lower CTR/zero-click rise), though effects vary by query type and study design. Some datasets show severe drops; others show modest or mixed impacts. ([Digiday][16])
- **“Cars kill \~10,000/day (analogy)”** — Overstated. WHO estimates \~1.19M road deaths/year (\~3.3k/day).
- **“LLMs topped JEE (AIR-1)”** — No official evidence. Media references describe mock-test style results; not an authenticated exam ranking. ([The Verge][17])
- **“SeeDream renders perfect text in images”** — Early tech reports show strong typography, but “perfect” is too strong; empirical evaluations are still emerging. ([Binary Verse AI][18])
- **“Adding AI is like adding juniors; late projects slip”** — The analogy aligns with Brooks’ Law; the maxim is well-established in software engineering. ([WIRED][19])

---

## Counterpoints

- **Adoption pace vs. tech pace** — While many firms pilot without enterprise-level EBIT impact yet, surveys show rapid production use and active risk mitigation; leadership and operating-model rewiring—not user hesitation alone—often constrain ROI. ([McKinsey & Company][20])
- **“Don’t tell people you use AI”** — In regulated sectors and client work, disclosure and auditability are becoming table stakes (EU AI Act literacy and governance duties, model provenance). Silence can create compliance risk. ([Orrick][21])
- **Validation > generation** — Strong case for validation, but controlled studies show material productivity gains from _generation_ tools (e.g., Copilot \~55% faster) with some evidence of quality improvements—when paired with reviews and guardrails. ([arXiv][22])
- **Entry-level displacement is uniform** — Labor effects are heterogeneous; AI often _complements_ human skills, raising demand for teamwork/communication while reducing demand for some routine tasks. Reskilling shifts outcomes. ([arXiv][23])
- **Traffic squeeze is total** — AI platforms now send some _new_ referral traffic (e.g., from chatbots), and impact varies by intent. Strategy should adapt (LLMO/GEO), not assume blanket decline. ([Digiday][24])

---

## Feedback

- **Calibrate claims**: Replace hyperbole with numbers + source/date on-slide (e.g., “WHO 2023: 1.19M/yr (\~3.3k/day)”), and label **Observation / Estimate / Speculation** to avoid confusion.
- **Anchor each section with 1 slide**: Audience’s **exact question** (≤6 words), **3–5 answers**, **1 action** (“Do now”)—then move on; keeps flow tight and outcomes clear.
- **Show, don’t tell, the frontier**: Keep a live, zoomable price/quality sheet (QR link) and a static backup chart; avoid “can’t zoom” moments and make comparisons apples-to-apples (input vs. output tokens).
- **Disclose constraints tactically**: When saying “use AI, don’t tell,” add when disclosure is required (client/regulatory contexts) and show a **minimal audit trail** template to keep trust.
- **Use micro-demos over anecdotes**: 60–120s live runs (e.g., “validation > generation” harness, model-switch cost calc) beat stories and make takeaways replicable.

[1]: https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/ "Canaries in the Coal Mine? Six Facts about the Recent ..."
[2]: https://reasoningengine.ai/p/llms-price-reduction-timeline "LLMs price reduction timeline - by Rogerio Chaves"
[3]: https://lmarena.ai/leaderboard "Leaderboard Overview"
[4]: https://www.cbsnews.com/news/ai-jobs-layoffs-us-2025/ "AI is leading to thousands of job losses, report finds - CBS News"
[5]: https://www.who.int/teams/social-determinants-of-health/safety-and-mobility/global-status-report-on-road-safety-2023 "Global status report on road safety 2023"
[6]: https://www.cdc.gov/transportation-safety/global/index.html "Global Road Safety"
[7]: https://www.roadsafetyngos.org/wp-content/uploads/2024/01/GSRRS-2023-launch-1.pdf "Global Status Report on Road Safety 2023"
[8]: https://www.instagram.com/reel/DOf2lB9D8Y3/ "China's AI Image Generation Tool: A Game-Changer for ..."
[11]: https://www.axios.com/2025/08/26/ai-entry-level-jobs "AI is already taking jobs away from entry-level workers"
[12]: https://openai.com/index/gpt-4-research/ "GPT-4"
[13]: https://lmarena.ai/leaderboard "Leaderboard Overview"
[14]: https://www.europarl.europa.eu/news/en/press-room/20240308IPR19015/artificial-intelligence-act-meps-adopt-landmark-law "Artificial Intelligence Act: MEPs adopt landmark law | News"
[15]: https://www.binadox.com/blog/llm-api-pricing-comparison-2025-complete-cost-analysis-guide/ "LLM API Pricing Comparison 2025: Complete Cost ..."
[16]: https://digiday.com/media/google-ai-overviews-linked-to-25-drop-in-publisher-referral-traffic-new-data-shows/ "Google AI Overviews linked to 25% drop in publisher ..."
[17]: https://www.theverge.com/news/647896/openai-chatgpt-gpt-4-1-mini-nano-launch-availability "OpenAI debuts its GPT-4.1 flagship AI model"
[18]: https://binaryverseai.com/llm-math-benchmark-performance-2025/ "LLM Math Benchmark: Stunning 2025 Results You Need To See"
[19]: https://www.wired.com/2010/07/ff-fred-brooks "Master Planner: Fred Brooks Shows How to Design Anything"
[20]: https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/2025/the-state-of-ai-how-organizations-are-rewiring-to-capture-value_final.pdf "The state of AI"
[21]: https://www.orrick.com/en/Insights/2025/04/EU-Commission-Publishes-Guidelines-on-the-Prohibited-AI-Practices-under-the-AI-Act "EU Commission Publishes Guidelines on the Prohibited AI ..."
[22]: https://arxiv.org/abs/2302.06590 "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot"
[23]: https://arxiv.org/abs/2412.19754 "Complement or substitute? How AI increases the demand for human skills"
[24]: https://digiday.com/media/in-graphic-detail-ai-platforms-are-driving-more-traffic-but-not-enough-to-offset-zero-click-search/ "AI is driving more traffic, but not offsetting 'zero-click' search"
[25]: https://www.similarweb.com/blog/marketing/seo/most-used-ai/ "Top AI Tools by Web and App Usage (August 2025 Data)"
[26]: https://www.seroundtable.com/similarweb-google-zero-click-search-growth-39706.html "Similarweb: No Clicks From Google Grew From 56% to 69 ..."
[27]: https://artificialintelligenceact.eu/article/5/ "Article 5: Prohibited AI Practices | EU Artificial Intelligence Act"

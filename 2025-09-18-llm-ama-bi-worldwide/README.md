---
marp: true
title: "LLMs: Ask Me Anything"
author: Anand S
url: https://sanand0.github.io/talks/2025-09-18-llm-ama-bi-worldwide/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
# ChatGPT: https://chatgpt.com/c/68cd0cbb-e2b4-8322-9817-472bdd9a2de5
---

<style>
transcript { display: none; }
</style>

# LLMs: Ask Me Anything

[BI Worldwide](https://www.biworldwide.com/) · 18 Sep 2025, 4:00 pm IST · [Chennai](https://maps.app.goo.gl/GxW7USQhuknHL3Vs5)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Transcript](https://github.com/sanand0/talks/blob/main/2025-09-18-llm-ama-bi-worldwide/README.md)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-18-llm-ama-bi-worldwide/)

---

## What will we cover?

- **You ask; I answer**—your questions set the agenda.
- I’ll note topics from the room and **Teams chat**.
- I prefer live Q\&A over slides; keep it casual.
- We’ll cluster similar questions to go faster.
- If needed, I’ll **club related themes** like trust, bias, privacy.

<transcript>

## Host Introduction

We know what HT session stands for because you have explained briefly about it in one of our email communications. And also this is actually a practice of bringing an eminent speaker from the external world who is a subject matter expert to come and share—I mean, create this forum to come and share the best practices and also the subject that they are a kind of expert in.

And this time, in the HT session for this year, FY26, the first session that we have actually scheduled is today, across India. We, on behalf of DAW India, will welcome with a big round of applause, Mr. Anand.

Welcome, sir. There is a quick note. We were just preparing this quick welcome note, going through his website, and there has been a lot of interesting information that he has written on his own. And he has kept it ready in case of any of these sessions, that he wanted to present what is the welcome note that you want to give him. And few experts from what he has actually listed down.

He is an… he is an LMM psychologist that we have actually mentioned. He takes psychology and also he is a co-founder for an organization called Gramener, which is now called as Strive. And he is one of the top 10, one of the top 10 data scientists in India, right? That is, that is also one other thing.

And he is a student of Vidya Mandir, where even Prasad has been one of his batchmates there. And he is a next alumni of IIT Chennai. IIT, the first, the top 10 prestigious institutions have been listed in NIRT this year. So he is from IIT Chennai. And then, he didn’t stop there. Impressed by his managers in IBM, he also went ahead and did his business studies in IIM Bangalore. Right? So he’s both IIT, has done both in IIT as well as in IIM as well.

And he worked at different companies like Lehman Brothers in investment banking, and a couple of brief stints with Boston and Infosys Consultancy in London. Then the startup bug bit him. So along with his four like-minded friends, he started this organization called Gramener. And eventually, that was, then he moved to Singapore and that was taken over or acquired by a company called Strive. That is where he is from.

And you know, we have also mentioned about his blogs. His blog is S-hyphen-anand.net. And he is also a TED speaker, and you could see a lot of his talks that is recorded, and there is a repository on his website. You can go ahead and look at it.

And finally, on the personal side, he has been called as Ajith or Arvind Swami during his IIT sessions, on a funny side of it. And he is also, has learned both Mridangam and keyboard for quite some years and performed at his college as well. With that note, welcome you, sir. The floor is yours. Thank you.

## Speaker's Talk

So now you know, if you want somebody to introduce you, you write the introduction, give it to them.

What shall we talk about today? The floor is yours, actually. I can talk about all kinds of things. **What I talk about will be interesting to me. What you ask for will be interesting to you. You ask.**

**Question**: LLMs is a broad topic. What would you like to know? What are you curious about? What are you worried about? And people on Teams, please feel free to type your questions or topics that you would like to talk about on the chat. I’ll also make a note.

**Question**: Security concerns and data privacy.

**Question**: What do you mean by LLM psychologist?

**Question**: How do you learn?

**Question**: Who has more scope? The one who creates the models or the one who uses?

**Question**: So we already talked about RIP Data Scientist. So maybe it is playing different roles, so we don't want that to happen. So what is it that it's going to do?

**Question**: How long will LLM rule the world?

**Question**: Can we trust the LLM?

**Question**: And from Teams: Bias and lack of transparency as of now.

**Answer**: Fair point. I will club that with, "Can we trust LLMs?" I'll probably take one or two more questions and then we will... Is MCP server integration to LLMs better than OpenAI integration?

**Question**: What is next to AI and what would be the future of roles in software industries that we have today?

**Question**: Is it feasible from a cost perspective, compared to the lower middle class?

My screen is not yet visible, so I will share my screen. And it should be visible if this says it is visible. Great.

</transcript>

---

## What is “LLM psychologist”?

- **It's a gimmick title**, inspired by Karpathy’s tweet. [#][1]
- I poke LLMs with varied prompts and test how they react.
- My tests: emotional pleas and shaming usually **hurt accuracy**.
- **“Think step-by-step” boosts results** across many models (Self-Consistency).
- I adopted the label publicly to spark curiosity and discussion.

<transcript>

So, some of you may have heard of Andrej Karpathy. He coined the term LLM psychologist. He put in a tweet, and here it is somewhere. This was the tweet that originally coined the term.

Is there a way we can reduce the volume so that I can speak a little louder and people still not have a problem? Okay. Now that I am speaking and this is not picking it up. That's about it. Good. Yes.

So Andrej Karpathy said these examples illustrate that no matter how trivial, it makes sense to be a prompt engineer. And he says, I also like to think of this role as a kind of LLM psychologist. I was delivering a talk at MDI Gurgaon and I needed some gimmick. So, what I did was called up our head of HR and said, "Manju, do you have any problem if I start calling myself LLM psychologist? Can I make that my official designation?" She said, "Anand, you have sold your company, you can do what you want." Okay. I went on stage, opened LinkedIn, and in front of everybody, changed my designation to LLM psychologist and declared myself as the world's first official LLM psychologist.

**What is it? It is a gimmick. What does it really mean? Nothing.** This is exactly what I did in 2011 when the term data scientist was coined. I started calling myself data scientist. That term picked up. This probably won't, but it's still different. But what do I do? What I do is explore LLMs, understand what they do, poke them in different ways, and see if by poking them in different ways, they behave differently.

</transcript>

---

## Do emotional prompts help?

- I tried polite, panicked, shaming, praise—**no consistent gains**; often worse. [#](https://sanand0.github.io/llmevals/emotion-prompts/)
- **Reasoning prompts help**; step-by-step is the only reliable boost (Self-Consistency).
- I measured multiple models on arithmetic; trends were stable.
- Seven models improved slightly; \~20 did worse—**net negative**.
- Results align with research on chain-of-thought sampling (Self-Consistency).

<transcript>

For example, one of the things that I have been looking at is people keep saying if you tell an LLM something like, "Oh dear, I am absolutely overwhelmed and I need your help right this second. My hands are shaking, my heart is racing, I urgently need your help, my life depends on it." So if you emotionally blackmail an LLM, it does better. Some people say if you are polite, it does better. Some people say if you say you are a stupid model, it does better. Are these correct? So I tried it out. I ran this on a whole bunch of models, asked it to do some simple arithmetic. And for each of these models, for each of these prompts, I was looking at when does it perform better, which is green, and when does it perform worse, which is red, took the average, and I find that if you emotionally blackmail it or shame it, it actually does consistently worse for many of the LLMs. Seven of them actually do slightly better, but 20-odd do slightly worse.

Reasoning, that is, **"think step-by-step," is the only prompt where it, by and large, consistently improves the performance** in a statistically significant way. And of course, this is something that most models have already incorporated. That's why we have the new reasoning models. And things like being polite, praising them, being afraid, doesn't have any conclusive evidence. On the margin, they might make the model slightly worse, if anything, that's what we have evidence for. This is the kind of thing that I do. Poke models, try and see how they behave, and try and justify my name of LLM psychologist.

</transcript>

---

## Can lower-income users afford LLMs?

- **Yes—costs plunge while quality rises** along the value frontier. [#](https://sanand0.github.io/llmpricing/)
- For “8th-grade” tasks, today’s cheap models are **good enough**.
- **Price/quality frontier shifts**: newer models beat older at lower cost (Arena).
- “Too cheap to meter” isn’t required; near-mass affordability suffices.
- Lower-middle-class access looks **likely soon**, given current trends.

<transcript>

Is this a technology that can reach the lower middle class? Let's see. If I look at the price of LLMs, now the way in which we quantify the price of LLMs, this is a chart that plots a whole bunch of models. X-axis is the cost, Y-axis is the quality. And I'll explain how we measure quality in a minute. But the X-axis is cost per million tokens. What that means is if you take the entire Harry Potter, all seven books, and put it into an LLM, or if you take the King James Bible in its entirety and put it into an LLM, that's about a million tokens. How much will it cost? For the expensive models like GPT-4.5 Preview, it costs $75. GPT-4 costs about $30. This is a logarithmic scale. If you take one of the newer models like DeepSeek Coder One or GPT-Hi, it costs around a dollar. For the really inexpensive ones, Gemini 1.5 Flash, 3.8 cents. Amazon Nova, 3.5 cents.

Now, the quality of an Amazon Nova or Gemini 1.5 Flash, these are somewhat newer models, is comparable to an old model like GPT-4, because the Y-axis is quality and they are roughly at the same height. What do we mean by quality? There is a site, LMSys Leaderboard or LM Arena as it's called, where people can put in any question like, "Why did the chicken cross the road?" and it then sends that request to two different models, but it doesn't tell you which are the two models that it is sending it to. Both of them will generate an output. And then people can read both the responses. So this one says the answer is of course to get to the other side, but it's saying they are trained to escape the farmer's constant expectations. Now it's trying to crack a joke. Annoying fowl language. Okay, these are not bad jokes. And this one just says to get to the other side. I definitely like the one on the left better. So I'm going to say left is better. Now at this point, it will reveal which model it is to me, but I am doing a blind test. I did not know which was the right model. But like this, about 3.5 million people have rated a variety of different models. Llama 4 Scout on the left, MiniMax N1 on the right. Both slightly old models. But I have contributed my rating to the 3.5 million and then it becomes like a chess match. The Elo score is computed between two players who play chess. The exact same algorithm, the Elo score, is computed for these models, and that's what the Y-axis is about. Grandmaster level is 2,400 plus or some such thing. We have scores right now for models ranging from about 1,000 to as high as about 1,500. And this has evolved over time.

So if we start in let's say March 2023, we had GPT-3.5 Turbo, Elo score of around 1141. Not bad, but in my mind, I think of this as close to, let's say, 8th class level intelligence, which is not bad. This is not an 8th class student who knows only what an 8th class student knows. This is an 8th class student who has read all of the internet. A fairly smart student, and I would rely on them for a bunch of things. And not very cheap, but not very expensive. Claude-1 was more expensive, $8 for roughly the same level of quality. But then things moved over time. We started getting newer and newer models. So around March 2024, for instance, Claude 3 Haiku emerged as relatively cheaper and better than many of the neighboring models. Now the models in green are what we would deem as the frontier. That is, there is no model that is both cheaper and better than those models. Let's take Claude 3 Sonnet. There is nothing that is to the top left. Nothing that is both cheaper and better. Similarly, nothing to the top left of Claude 3 Haiku. So there's no reason why you would not pick one of these models. For any other model, let's take Gemini Pro. Claude 3 Haiku is cheaper and better. So why would you ever pick that? As models improved, the cost falls for a given level of quality. GPT-4o Mini was another big leap in that frontier. And then another one that happened was DeepSeek Coder One, which pushed the bounds of cost and quality a fair bit. And as things... Gemini 1.5 Flash Preview was another big jump in that stage. Gemini 1.5 Pro was dominating. This is where we are approximately as of last month, with GPT-Hi being the smartest model. Now, I said this is roughly class 8 level. Around the middle would be class 12 level intelligence. Near the top is close to postgraduate level intelligence. Meaning GPT-5 today is as good as hiring a postgraduate in many areas.

Now, a postgraduate level intelligence is very different from a postgraduate. For example, you tell a postgraduate something now, they will probably remember it an hour later. You talk to ChatGPT in one window, you reopen another window, it has forgotten it in 5 seconds. So you should think of it like Ghajini. It has zero memory. There are several quirks like this. We don't really know how to deal with LLMs, but let us specifically talk about cost. Is it accessible to the lower middle class? What we have is there was a time when an 8th standard level intelligence was available for about a dollar. Over time, that ended up becoming available for something in the order of higher intelligence was available for 5 cents, processing that entire volume. The difference between the most expensive, $75, and the least expensive, about 3.5 cents, is 3.5, 35, $3.5, $35. So that's about 1,000, more than 2,000 times. In other words, **people are creating good models, and it rapidly becomes 2,000 times cheaper**, or it has become about 2,000 times cheaper. Now, will that continue to happen? Let's talk about that. But if it does continue to happen, or even if it doesn't continue to happen, if we take what we have right now, 2,000 times cheaper is nothing to be laughed at. It is crazy. It is the difference between a $1,000 budget and a $2 million budget. Enormous scale that is possible. ChatGPT has, OpenAI has released a 400 rupee plan, and they are probably going to be doing it at a decent margin. If not, DeepSeek or one of the Chinese companies will come in and release it at crazy cost.

People believe that there will be a time when it is too cheap to meter. Arguably, it doesn't need to become too cheap to meter. Electricity is reaching the masses. So intelligence at that level will probably get there. Long answer, but my point of view on is it reachable to the lower middle class is, **yes, maybe not today, but soon enough, given the pace of progress.**

</transcript>

---

## Will progress keep accelerating?

- **Demand drives optimization**, like browsers and languages did (Chrome V8).
- Moore’s observation: compute scales \~every two years (Moore’s Law).
- AI scaleups may even exceed that pace in systems terms (Huang).
- Predicting “what’s next after AI” is **foolish**; I won’t.
- History is a better guide than forecasts; I’ll use it.

<transcript>

Will the pace of progress continue? That many people that I follow and whose opinion I think is well considered believe that we are nowhere near any kind of limit. Moore's Law, which was that every 18 months, one and a half years, computing power of chips will double, has held for decades, since the 1970s when he coined this as a principle. It's happened, but it's happened for very different reasons at different times. But one of the biggest driving factors was that the entire world was using it and there was a huge demand for it to become better. Languages become faster that way. Pretty much everybody is using a browser. JavaScript was such a slow language, and then Chrome came in and introduced the V8 engine, and the speed at which JavaScript gets executed dramatically increased. PHP is a slow language. Facebook came in, improved it, and it became a much faster language. Once there is strong demand, there will be investments that go into it, that will optimize it. And there is more demand in AI than any other field. So I also don't see it tapering off. Which kind of leads to the question, "What's next after AI?" **I don't even know what's next in AI. Who knows what's next after AI? I have absolutely no idea.** So I'm not even going to try and predict. I'm not going to try and predict the future in many areas. I'm not even going to try and predict the present. It's hard enough to understand. I'm going to try and share what I've seen from the past. But what I've seen is that what we can learn from history is probably more relevant for us than what the future might hold, because we've seen things like this so many times.

</transcript>

---

## How long will LLMs “rule”?

- Foundational tech (like **electricity**) can matter for centuries (Moore’s Law).
- **Transformers may be replaced** by better architectures eventually.
- Popular format isn’t always the best—**Betamax vs VHS** analogy.
- I won’t predict the winner; I’ll track evidence.
- We’ll adapt as architectures evolve; skills will transfer.

<transcript>

How many typists do you know? Professional typists? Word processing killed out an entire industry. What happened to them from a professional perspective? Their job as a typist vanished. Did they vanish? No. In the 1940s, there was a strike of lift operators in New York. The entire city came to a standstill. Where are the lift operators? In the late 1800s, London was entirely powered by an army of lamplighters. They would go light the lamp in every street. The number of these was ranging in several hundreds of thousands in just that city. Where are they now? With self-driving cars, you will probably ask the question, where is the driver as a profession? People will change. But that does not mean A, that we have not seen this before, and it does not mean that it is a good thing either. It can be a bad thing also. But it is not something that we have never seen before or any such thing. These things keep happening. It's just that now that it seems like it's happening to us, we say, okay, what should we do? Which is a good question to ask. What should we do is a good question to ask. But "Oh, this is new" is putting it at a higher level of, putting on a pedestal that it doesn't belong. You've seen this kind of a thing every year, some profession or the other just vanishes at scale. We just haven't been as aware of it.

Which is exactly the answer that I'm going to give to the question, "How long will LLMs rule the world?" There are two parts or two interpretations of this question. How long will AI rule the world? How long will large language models, that is the transformer architecture, rule the world? For the first question, I have no answer. Maybe forever, because electricity was arguably seriously scientifically investigated since the 1700s. Benjamin Franklin has talked about his Leyden jar experiments in that era, and people were discovering new things with electricity every day. And that process of discovery continues today with solar energy, we are discovering new ways of transforming something into electricity. The kind of investment that is going into the energy space, specifically into electricity-based vehicles, is enormous. How to make batteries lighter and more efficient is a continuing discussion. So after 350 years, something as foundational as electricity continues to be fairly important. And at the same time, something as revolutionary as a Polaroid camera, who talks about a Polaroid camera these days? So I don't know whether AI itself will go that way. But transformers, which is the specific technology that is behind the bulk of large language models today, people are saying there are other mechanisms. Yann LeCun of Meta is one of those who is a strong proponent of some of the newer architectures, and he believes that the way forward is where LLMs will understand the world, not just words, and the world cannot be modeled in the same way that we are looking at transformers. It is more language that can be modeled this way. Therefore, we need to go beyond that. And there are several non-transformer architectures. Maybe he's right. Maybe he's supporting a Betamax format. Some of you may know that Betamax versus VHS was a huge debate during the videotape era. Betamax was a better format. VHS was the more popular format. And just with marketing, it won out. That can happen too. It doesn't necessarily need to happen that the better format will win. So transformers might not be the best format. It is the popular format. It is unclear whether the popular one will win or the better one will win. So no idea about this either.

</transcript>

---

## Builders or users: who has more scope?

- **Users have more scope**; infrastructure is built by few, used by many.
- Careers mirror Excel: billions use it; very few build it.
- My IBM story: you can thrive **without compiler design**.
- LLMs will magnify this pyramid—**many makers on top of few builders**.
- New roles emerge as tooling democratizes creation.

<transcript>

Let's take who has more scope? The one who creates LLMs or the one who uses LLMs? Who has more scope? The one who creates software or the one who uses software? How many people think there is more scope for people who create software than uses software? How many people think there is more scope for people who use software? That's about 30%. Which means that 70% of you are very diplomatic. Nice.

Okay, that answers the question about LLMs as well then. That is, there will be more demand for people to use, more scope for people who use LLMs, simply because there are so many more opportunities. When I joined IBM in '96, the person sitting in front of me on the train asked me, "What did you study?" "Chemical engineering." "Why are you coming in and taking all the computer science jobs?" "I don't know." "Do you know how to create a compiler?" I've never created a compiler before. "How will you survive in the software industry without even knowing the basics of compiler design?" "I don't know." I survived quite well. I have probably met about five or six people who know how to create a compiler. They don't have jobs because people don't need more and more compilers. People need more and more people who do simple things like me, that is build stuff on top of compilers. Think of it as an inverted pyramid. Infrastructure will be created by a few people. That can be distributed to a large number of people to use it. How many people use Excel? How many people create Excel? It's going to be like that.

</transcript>

---

## What happens to existing roles?

- Like typists, many will **re-skill** to adjacent, higher-leverage tasks.
- New work (transcription, DTP before; **LLM-native roles** now) appears.
- Some jobs shrink; **net variety expands** as costs drop.
- Organizations revive shelved projects when ROI flips positive.
- Expect **new industries** around LLM augmentation to form.

<transcript>

So, what is the future of software or analytics roles? What was the future of the typist when word processors came in? What do you think happened to them? Any guesses?

**Question**: They learned computers.

**Answer**: They learned computers. And what happened after that?

**Question**: They started using it.

**Answer**: They started using the keyboard, and what jobs did they find?

**Question**: Data entry. Stenographers. Other jobs coming.

**Answer**: Now, something like transcription, this where did this come from? It's a completely new job and suddenly opens up a huge space. People are sitting and doing that. DTP comes in because it is now more practical to enter stuff. See, because we had computers and people wanted to move everything into computers, an entire new space of jobs came in. **Now we have LLMs. Heaven knows what they will lead to. And we'll take some guesses. But that basically means that it's creating a new industry.**

Do you already have those skills? Who knows? Maybe we do, maybe we don't. It's entirely possible that the demand for the skills that each of us have could suddenly skyrocket. Let's take examples. Software. Because LLMs can help a software developer code faster, or LLMs can automate software. Great. So which means that there will be many, many, many, many people who will create software. People who can't even program can create software. Great. Theory number one. Therefore, there will be less software developers because people can create software by themselves. Theory number two. Therefore, the value of software, ROI of software, for an hour of investment, the amount that you can get is dramatically higher. If the ROI or the value of something goes up, demand will go up. The person who's creating the software or wants to create the software will say, "Now I want not one software which I can spend time creating on, I want 10 pieces of software." And it's so cheap. Can some of you do this? And somebody who knows how to create some of the software will have a slight edge. They have seen what the basics will have a small edge. Those who know more stuff will probably be able to design even more complex software. Now it starts becoming possible to create software that was not practical before. Companies will say, "Oh, all those 30 projects that we shelled last year because the cost was 3x the value, now can it be done within the budget?" You can say, "Oh yeah, we can do it at one-third the price, not three times the price." Okay, let's do it. Where are the people? Okay, go hire.

Our clients are coming to us and saying, "We need GenAI people." So what do we do? We take people, we put "GenAI" in front of their designation. Data engineer, GenAI data engineer. QA, GenAI QA. Consultant, GenAI consultant. And we give them training, one-day training, one-week training. With GenAI everything is faster, right? And we put them in front of the client. Now the client says, "Do you know GenAI?" The person says, "Yes, I do." And when you ask, "Do you know GenAI?" "Then I know GenAI."

So, there is a demand. Somebody has to fill it. And people will be filling it. Now, does that mean that if you are not the one who's jumping in early to fill that role, you're getting left behind? Maybe. Or maybe you're the person who will be getting the better opportunity which will come up later. I have no clue. So I think it is going to be completely useless for me to try and predict how jobs will evolve. But there are a few patterns that we are seeing. I will come to that in a few minutes.

</transcript>

---

## How should we adapt personally?

- **Use LLMs now** for learning and productivity; discretion with managers.
- Treat them as **interns**—lots of them—manage, brief, review.
- Practice creative applications; **skill compounds** with usage.
- Focus on **context you give**; results mirror instructions.
- Quiet adoption beats waiting for policy to catch up.

<transcript>

What do we do about it? I think there is one thing that is fairly obvious, which is use them. They are good for us in any case. Somebody has given us a technology at low and lowering costs. At the very least, we should use it for our learning, upskilling, for our jobs. A lot of people have this fear that if they say, "I am using AI for my job," then my manager will then feel that AI can do my job and replace me. Okay, don't tell your manager. That doesn't mean you don't use it. Whether you tell them, don't tell them, that is entirely an interpersonal discussion. But not using it, there is no need to not use it. Especially when it can give you a leg up and it gives you practice. Use it, practice it. Especially when people do not realize what this technology can do and the ways in which we can creatively use it. So the more you are able to use it creatively, the more powerful it becomes.

So now, I'm going to pause here and take questions from the chat. What's the impact of jobs when AI is everywhere? Yeah, I will talk a little more about this in a short while. LLM augmentation in future customer support and personalized data analytics and insights. Yeah, let's talk about this in a specific use cases that we should take up.

</transcript>

---

## What’s our new management model?

- **You are now managers** of countless smart interns (LLMs).
- They out-knowledge us broadly; we out-judge them locally.
- Use them for ideation, coding, analysis—**direct and delegate**.
- Calibrate expectations; promote yourself to **data science manager**.
- Design workflows assuming intelligent, tireless junior staff.

<transcript>

Okay, let me go back here. The answer to all of these is **you are now managers. You have a huge team of interns. Learn how to deal with them.** Soon these interns will become smarter and smarter. They're already smarter than us. I probably know more than an LLM in two or three areas. It knows more than me in 25,000 areas. Okay. We use them. It's not that that's going to cause a problem.

</transcript>

---

## How I build with LLMs

- I **voice-code** apps (e.g., Calendar Time) while walking.
- I rely on **context engineering**: one repo of examples to copy.
- I scope tasks to model capacity; expect **\~50% first-try success**.
- **Tell models exactly what to do**; size and sequence matter.
- This mirrors people management; communication is the core skill.

<transcript>

Now, I said I'll show you examples of how I'm using it, and I showed how I'm ideating with it. I also said I will show how I code with it. Now this ideator tool that I showed you was entirely coded by an LLM. How was it coded? So I prefer coding while walking. Now it's, earlier I could not do that very easily. Now it's becoming possible. How? Well, Codex from ChatGPT is, and you'll find you're probably already familiar with it, has a voice input. I can dictate to it. And I can do that from my phone as well. And many of the items that I merged are of that kind. So I'm going to code using my voice an application. What kind of an application shall we build? I wouldn't mind going through my Google Drive and... so if I ask it... or not even my Google Drive, let's say I ask it to go through my calendar and figure out who are the people that I'm spending the most time with. That sounds like a reasonable application that I can have it build.

So, let's do this. Build a tool called calendar time. This should ask the user to log in with their Google account and ask for Google Calendar permissions. When it does that, go through their calendar, specifically the last two weeks by default, but allow the user to specify a different option so that they can choose a different time period if they want. And then get all the meetings from this time period and show that list. But above that list, I want you to show a table that summarizes who are the people that they are spending time with, that is who are the people that they have sent invites to or who have sent invites to them, with the total amount of time that they have spent with that person, sorted in descending order. This can be a long list, so do some UI magic to make it look good. I want this application to look pretty. Now for logging in, don't use the client secret and client ID and all that. Use the UI-based mechanism. You will find that somewhere else in this repository, so you should be able to figure it out.

Now, this is roughly how I build the applications. Let us have it create two versions. Now, let us code.

</transcript>

---

## What is “context engineering”?

- I keep one repo so LLMs can **reuse patterns** across tools.
- I compensate for **zero memory** by feeding rich context.
- **Context engineering** = knowing what to tell an LLM.
- It mirrors **management/communication** skills.
- **RIP data scientist** → you’re a **data science manager**.

<transcript>

There are three things that I want to flag off in the workflow that you just saw. Voice, two options, and towards the end, I said, similar to the other tools in this repository. Let's start backwards. I find that if I have to give instructions every time, it is painful. The problem is that it does not remember stuff that I remember. We normally expect that everyone knows what we know. That's why we get angry when people don't understand us. This thing has zero memory. So there's a lot of effort that goes in into creating context. Which is all good, and we should do that. The way I find it convenient to give context is, rather than maintaining separate repositories for everything, for my tools, I maintain one repository. And that repository is what I have put this task into. And the reason that helps is it can take examples from my other tools and use that as a reference. And I've built a variety of tools. I have another tool that does something with Google Tasks, so I know it will be able to figure it out. Which also relates to a point that I mentioned earlier, which is knowing what it can and cannot do. I've done this about 80, 90 times, this sort of a thing, not this particular example. This I'm trying for the first time. But I know that this is roughly at the 50% failure threshold. 50% chance it will work, 50% chance it will fail, which is why I'm picking it because irrespective of whether it succeeds or fails, it will be a useful example. In short, make sure that you are giving it enough information. That is largely what context engineering is about. And therefore, one of the things that you should learn, whether you are looking at this as a data scientist or a software engineer or any kind of learner, context engineering is important. **Knowing what you need to tell an LLM for it to do what it should do.** Another way of thinking about context engineering is communication. If you want somebody to do something, you have to give them the information so that they can do something. Now, they will come and ask you. LLMs do that as well. If they don't do the job, you can fire them. You can do that with LLMs as well. After doing this for a few weeks, few months, etc., you will get the hang of it and you will get promoted as a manager. That is what will happen here also. **This is no different from management. And therefore, if you want to know how to learn LLMs, learn people.** Not very different. Management is perhaps the same thing as LLM psychology or AI coding or whatever it is. You have a thousand interns now, who are programmers who can work with you. They are also transcribers, they are also all kinds of other things. But you are a manager now. Likewise, you have a thousand analysts. Therefore, you are no longer a data scientist. **You are a data science manager. Rest in peace data scientist, you've been promoted. That's what happened to you.**

</transcript>

---

## What do agents actually do?

- **Agent = LLM + tools + loop** until done.
- I gave Google access, then asked time-of-day meeting stats.
- To respect privacy, I **changed the question** to avoid names.
- It **planned, coded, ran**, then summarized JSON into insights.
- Code counts; LLMs don’t—**use programs to verify claims**.

<transcript>

Now, this particular thing, which is happening here, right? Can be done in a slightly different way. Let me show you API agent. Agents are all the buzz these days. But here's what is an agent? An agent is an LLM running tools in a loop. Let's go through that. LLMs is clear. Running tools, meaning they can take actions, they can do stuff beyond what LLMs can do. You are giving them arms and legs. For example, one of the arms and legs that I can give it is access to my Google account. So I will sign in with my Gramener email ID. And it's not verified, but that's perfectly fine because I built this app. And continue. And log in. So now I have given it access to one tool. I could have given it access to a whole bunch of tools. Running tools in a loop, which means that you give it a task. It will do something. It doesn't get it right, do it again. Again. Again. Again, until it gets the job done. It can do this loop in a variety of different ways. It can say, first I will plan what are all the things that I'm going to do. Then I'm going to execute it. Then I'm going to run it. Then I'm going to fix it. Then I'm going to interpret it and tell the person. And if there is a mistake anywhere, I will go back and do this. In other words, it will keep taking a step forward, but it doesn't always have to be in the same direction. It can meander all over. You are basically giving it permission to continue working. That is the crux of an agent. And you are giving it permission to continue working in any way it wants and giving it prior guidance, which is what we do with humans. So put another way, I don't know how many of you have used sites like Fiverr or Mechanical Turk or whatever, but think of it this way. An LLM is where you call somebody, ask a question, get an answer. If it works, great. Doesn't work, done. An agent is where you call somebody and say, "Go research this task, get the job done, and then come back and deliver it to me in an hour, a day, whatever." The amount of time that you're giving it to play around is largely the difference, but otherwise they are fully autonomous.

So I'm going to ask more or less the same question here. Go through my calendar and tell me who are the people that I have interacted most with in the last, let's say, a week, sorted in descending order of time. This is dangerous because it will reveal all the client names, which brings us to privacy. But you will notice that the problem here is not me sending data to the LLM. The problem is me giving data to you. So let us change the question. Go through and tell me what time of day and what days of the week do I have the most meetings with other people at? Look at maybe the last one week's worth of data and submit.

So now what this does is, step one, thinks about how to write the program. It's doing a plan. Step two, writing a program to solve the problem. This part is perhaps the most critical to how can we trust LLMs. Don't LLMs hallucinate? Firstly, it has run the program. It has gotten some results. I can't for the life of me read JSON well enough. But it's saying that I have most meetings on Thursday. At least this Thursday, a total of seven meetings. Afternoon, 12 to 5 PM. And Thursdays, yeah. So busiest day, Thursdays. Busiest time of day, afternoons, 12 to 5 PM. Yeah, I can believe that. This I can trust because it wrote a program to do it. It didn't just go through my calendar one by one. You tell a human, "I want you to count how many people are there in this room." Plus or minus one is very common. Instead, I tell a machine, "Let people go through one by one on that whatever that thing is, that... exactly." Now that, however many times it slides, as long as people don't jump, is going to get it right. That's not going to make a mistake. And code is like that. LLMs cannot count, but code can count. LLMs are fantastic at languages. Code is a language. Let's use it.

</transcript>

---

## Can we trust LLMs?

- Trust them **as you trust people**: with checks and process.
- **Maker-checker** and redundancy cut error rates sharply.
- **Ensemble agreement** (2–5 models) reduces misclassification; escalate on disagreement (Arena).
- Engineering helps too: have **code do the counting**.
- Aim for **70% automation at \~99% quality** with selective review.

<transcript>

So the way I see it, the workaround to LLMs hallucinating, one of the workarounds to LLMs hallucinating, which is the same problem that humans hallucinate. humans get stuff wrong. Humans make mistakes, LLMs hallucinate, same thing. Now hold on, **we have centuries of experience dealing with human mistakes. That is literally what engineering is about. It is literally what management is about.** We know so many things about this, right? So, for example, one of the things that we can do is double check, maker-checker, existed for centuries.

We were looking at how can LLMs accurately classify chat messages. Somebody says, "Could I take a quick look at my invoice?" Somebody says, "I need help adding some items." "When will I receive my order?" And we ask LLMs to classify it. GPT-4.1 mini got it wrong. It put it under delivery period instead of, sorry, put it in track order instead of delivery period. But Nova Lite got it right. Meta Llama 4 Scout also got it wrong. It put it into delivery period instead of track order, or the other way around, whatever. Whereas for certain questions, many of the LLMs tend to get it right. So, once we do an evaluation against a data set and we know that the LLMs are getting some of these right, some of these wrong, what we can do is start looking at, are they correlated? Do they make the same kinds of mistakes? It turns out that they are not very correlated. So here, the models that are, so the diagonal is yellow. Models are obviously agreeing with themselves. But the answers from, let's say GPT-4.1 Nano are quite different from the answers from Google's Gemma 3. The answers from Gemma 3 are quite different from the answers from 2.272B. So if the models are not likely to agree amongst themselves, and anyway, humans also don't agree amongst themselves, that's a different story. Then what we can do is have one cross-check the work of the other. They are not going to make the same kind of mistake. What is the impact of cross-checking? On average, if you have a model, let's say, classify this, it makes about 14% errors. When you double check and say, "Only if both of you agree, I will take your result," only 3.7% errors. Now you say triple check it. "Only if all three of you agree, I will take the result." 2.2% error. Quintuple check it. Then five of you agree, I will take the result. 0.7% error. And this is by randomly picking models, meaning that by carefully picking models, we can do even better. But that increases manual work because if they disagree, if even one of them disagrees, we will have to check. How much does it increase by? In this case, we found that even with quintuple checking, it's 28.1%, meaning roughly **70% is automated at 99.3% quality. I'll take that. 70% cost reduction at far better than human quality.** How many people can I say are going to get it right 99% of the time? This is fantastic.

So, there are broadly two directions or approaches to how we solve the problem of systems making mistakes, systems being humans or systems being models. One, we solve it through a management process like double checking, triple checking, quadruple checking. The economics will determine how we run the process.

</transcript>

---

## How do we measure effort?

- I define effort by **cases needing human review**.
- If five models agree, we auto-accept; else, we **triage**.
- You can tune thresholds to balance cost and quality.
- Harder items naturally **bubble up** for people.
- Process economics—not purity—should guide settings.

<transcript>

**Question**: How do you define effort?

**Answer**: In this particular case, if there are 100 messages to be checked, then if the model, five models agree and we pass it, then this happens roughly to about 72 of those messages. The remaining 28 messages need to be checked. They may be complicated messages, so you may say, therefore this, okay, do the calculation. Maybe it is 35% effort instead of 100% effort. But the point is here, I'm simply measuring the number of messages that they disagreed on.

So we can, option A, solve it as a management process solution like this. Or we can use code. And the code here, in this case, solved the problem by automating it, which is the engineering version of the solution. Which is what we have been doing for a long time. Therefore, can we trust LLMs? As much as we can trust people. They have their own accuracies. Some are better than others. Use the principles that we know. Bias and lack of transparency and trust, I will come to in a minute.

But what do we do from a job perspective? Because one of the answers to the question, "What do we do?" is learn how to use LLMs better. I'll tell you how I'm learning how to use LLMs better. I am asking LLMs how I can learn how to use LLMs better. They are smart. It's a postgraduate level intelligence. Supposing somebody said, "Anand, I will give you at the cost of $20 a month, however many postgraduates as interns as you want. However many. You want 100, I will give you 100. You want 1,000, I will give you 1,000." My first response is, "Boss, I can't even manage myself, let alone other intelligences." But if somebody's giving it at that crazy a cost, especially zero marginal cost, I have to learn. And these are smart, so they teach me.

</transcript>

---

## How do I learn faster?

- I **ask LLMs how to learn** LLMs; meta-learning works.
- I keep note vaults and **combine random concepts** for ideas.
- My “ideator” is idea **factory**—I won’t run out.
- I test viability later; the goal is **option discovery**.
- Creative synthesis is my hedge against disruption.

<transcript>

So one of the things that I'm trying to do is explore new ideas. How do I explore new ideas? By asking LLMs. How do I ask LLMs? So one of the things that I learned is somewhere where I was reading through what ChatGPT said, it said creativity is about combining ideas. Now my job is at Strive, the organization that I work at, of heading the innovation team. Innovation is about creativity. So can I get LLMs to help me with creativity? Turns out that there is a specific way in which I can do that. I take notes fairly extensively. I have notes around a variety of topics, and I document them as LLM related notes, things I learned, questions to ask, blah, blah, blah, whole series of topics. So one of the random notes that I took on the 10th of September is that Claude AI can work natively with Excel, PPTX, docx files and so on. Another random idea which I had noted on 14th September is depending on the underlying chip a model uses, floating point multiplications may differ. That is because you, different chips calculate slightly differently, the same model running on different chips can produce different results. And I can randomly pick any one of these ideas or I can pick a specific one. Let's say I want to pick something from things I learned, another thing from, let's say, oblique strategies from Brian Eno or core concepts in different fields. Randomly picking from these, I can ask it to give me something. Let us say I want a startup business idea, combining these two weird concepts, something about habit tooling and something about encrypted computation, and click on ideate.

What that does is send a message to ChatGPT saying, "You are a radical concept synthesizer hired to astound even experts." I have no idea if all of this grand words helps, but... "Generate a big, useful, non-obvious idea that is aligned with startup business idea." This is a templated thing that I have created, so it just plugs in the startup business idea word into it, using the two concepts that I have provided. And I've given it instructions on how to go about doing that. It is supposed to generate five ideas and use specific mental model techniques like inversion, mechanism transplant, constraint violation, all of this I learned because ChatGPT said here are some interesting ways of ideating. And then score them on novelty and utility. Pick the top score and based on that, output the top insight, how I can build this idea, how I can test it and so on, in plain simple English.

Now it is generating it. I have done this maybe about 15, 20 times. Every single time it comes up with something that is totally blows my mind. Maybe it is practical, maybe I can do it, maybe I can't do it, doesn't matter. What I know for sure is **I am never going to run out of creative ideas because this is a factory. It can just keep generating creative ideas.** This is making my job secure.

</transcript>

---

## How do I get better outputs?

- I chase **better models** when available; capability matters.
- I **meta-prompt**: use prompt optimizers, then iterate (Self-Consistency).
- I **evaluate prompts** against examples; measure extra/missing content.
- When it fails, I **revise prompts** and re-score.
- Same engineering loop—spec, test, fix—just applied to language.

<transcript>

Another part of my job is writing code or building demo applications. These days, I have discovered two things. The first is, I can tell the LLM, "Build this," and it will by and large get the job done as long as I know how to size it and prompt it. Sizing it meaning don't give it something more than its capacity to do, which I have to learn from experience. Second is, give it to it in a way that does not confuse it and clarifies how to do things. What do I mean by that? Sometimes I say, "I want a complicated application." Then at the end I say, "Write a very, very simple application." Do you want complex or do you want simple? The latter is somewhat easy to solve. You can use a prompt optimizer. The solution to how do I learn, by the way, or sorry, the solution to... I will rephrase this question. How do you whatever it is, is **ask ChatGPT. It has the intelligence.** Earlier it used to be ask Google, ask friends, whatever. ChatGPT combines both of these.

Now, it's come up with five ideas. It's saying, here is an encrypted habit compiler as a startup idea. A declarative habit file that plugs into your existing tools can change team behavior fast while analytics on encrypted counters so that no one's private work trail is exposed. This is interesting. Supposing I am worried that my manager is tracking all my keystrokes and saying I'm not productive, blah, blah, blah. And you've seen several organizations do that because they want their employees to be productive. And the employees do not want their activity to be tracked at least at that level. Organizations also face privacy issues, so they may not be legally allowed to track. What if there was a way of encrypting what the person is doing, capturing that as habits, and being able to aggregate and run this? This is a practical idea. I did not think of this. ChatGPT thought of it. I am not going to tell my boss ChatGPT thought of it. Not his problem. But I'm going to take this and run with it. So, let's take... is this the one that we looked like? Yeah, this is a reasonably viable business plan. Again, I have to validate it.

If it can do stuff like this, then it gives me confidence that it can do more. But there are a few caveats like I said. One, you have to know what its level of capability is, and you have to know how to increase that level of capability. One of it is better prompting, and I will come to that. But the other is using the best models available. The best model available today probably is GPT-5 Pro, which is accessible only if you have the $200 ChatGPT account. I don't. The best model accessible to me is ChatGPT 5 Thinking, which the free version does not always have access to. Sometimes I get access to it with some quota. And with extended thinking enabled, this is an option that I use. So I'm constantly on the lookout, is there some newer, more powerful model? If so, I will jump to that. Because why would I not?

</transcript>

---

## How do I optimize prompts?

- Use **meta-prompts / prompt optimizers** (e.g., OpenAI tools) to rewrite. (Fact-check: OpenAI exposes pricing/docs; Optimizer exists in platform tooling.) ([OpenAI][10])
- Frame tasks with **checklists** and **reasoning steps** first.
- Evaluate with **expected vs generated** comparisons and similarity.
- Iterate to reduce **extra details** and style drift.
- Standard ML hygiene—**specify, test, refine**—still applies.

<transcript>

Second, I always optimize my prompts. This prompt was carefully constructed by searching for "prompt optimizer." And since I'm using OpenAI models, I search for the OpenAI prompt optimizer. And you will eventually find it, but here is where I would... on the playground for OpenAI, you can put in a prompt. So let's say the prompt is, "Given two concepts, create a new creative idea." Yeah, let's say that is a prompt. Now I click on optimize. What it does is, knowing how a specific model, in this case GPT-5, works, it incorporates prompting best practices, rewrites the prompt, and comes up with a better prompt. Now, this works fairly well if you want to one-shot it, that is you're not really sure what to do and how to improve it. But what if you actually know that there is a specific purpose that you have to apply it for? And while this is churning, I will show you something else. A pharma company came to us and they said, "We want to build a model where we tell the patients what they should be doing after the clinical trial test." So they said, "We administer drugs, and there is a standard procedure. For example, the procedure says that following the administration of investigational antibody MBX 23, blah, blah, blah." That is what the clinical trial procedure says. Nobody will understand this. What we really want to tell them is after you receive the study medicine through an IV, we will watch you closely for four hours at the clinic. We will check your blood pressure, we will check your heart rate. So the left side translates into this. And they shared about 10 or 11 such examples and they said, "Can you convert it?" This is the classic machine learning cycle. And what we can do is pass this to an LLM and tell it to automatically generate the prompt. This is the input, this is the output, you generate the prompt. And it said, "You are a medical communicator tasked with transforming blah, blah, blah," and it provides a prompt. Exactly what the prompt optimizer did as well.

And here for the earlier one, it's saying, begin with a concise checklist, three to seven bullet points outlining how you will approach the two ideas conceptually. And it gives me a reason that initial checklist of three to seven bullets planned first promotes clearer, structured thinking for complex synthesis tasks. The same think step-by-step or the reasoning that we saw earlier. It incorporates these best practices and comes up with a better prompt. Good. So rule number one, always meta-prompt. Not always, if it's important, use a meta-prompt. If it is not important, say what you want. Second, evaluate it. So I can generate the output for this. That is, the first column is the expected input, second column is the expected... input, expected output. Third column is what this prompt generated. So we are taking the prompt that it has given us, generating the output. Now we can then check, does it have any extra content? Does it have all relevant content? What is the embedding similarity between these? And evaluate the prompt. That gives us a set of metrics. So it's gone through this and said, on the generated content seems to be introducing extra details in every single case. So for instance, here, the generated output has extra details that are not presented in the expected output like the study medicine, the disease condition, etc. So the prompt that it has generated seems to be something that is always putting in technical terms, which we don't want in our output. Okay. So now we know that it is failing, which is useful, or it's not working perfectly. And we know that it's particularly failing on this side, but not so much on this side. Good. It's not missing stuff, it's adding too much. Now, rather than manually try and fix it, try to fix it, let's revise the prompt. We will send this again to the LLM and have it correct it. So now it says, okay, instead of you are an expert medical, make it a skilled communicator, not expert, just skilled. And it makes a whole series of corrections like this, which we can then re-evaluate. First time, it got a score of 16.84 out of 30. Next time, maybe it will get something higher, maybe it will get something higher. So you can iterate.

In other words, all of the engineering that you learned is still applicable in this case, just that the domain has transferred. But what we are doing here is learning how to use the tools better. Better models, better prompts, using the tools themselves and whatever else we know to improve the prompts, maybe improve the models. The models themselves are being improved by the labs by the models. And that's exactly what we should be doing as well.

I said I'll show you examples of how I'm using it and I showed how I'm ideating with it. And I also said I will show how I code with it. This ideator tool that I showed you was entirely coded by an LLM.

## Host Conclusion

Okay, that's Anand. Anything more I have to say? I don't know. Great job. Thank you, thank you, thank you. And actually I want to leave it open to the floor, you know? What did you guys get from this session?

**Question**: To use LLMs. If you are not using them till now, then yes, absolutely. Anything else?

**Question**: Go as life takes you.

**Answer**: Go as life takes you. Okay.

**Question**: Transform yourself.

**Answer**: That's one thing. That’s for myself, yeah.

**Question**: Keep thinking about LLMs.

**Answer**: Keep thinking about LLMs. Okay. In fact, once again, I would say don't think. Let the LLM think for you. That's what he said. Right? Don't think.

**Question**: The same thing, if we use LLMs continuously, our brains will deteriorate.

**Answer**: If we use calculators continuously, we stop being able to do mental mathematics. If we use machines continuously, our muscles will atrophy. If we stop cultivating food, then we will lose our ability to survive when there is no food available to us. If we stop wearing clothes, we will lose the ability to protect ourselves against the weather. We should stop doing all of these if we want to live in an environment which is very harsh, where we don't have all of this kind of support. And it is, I'm not saying that we should not do that. I'm saying that over time, the opportunities that we have to live in such environments, the need for such things will keep reducing. We had to study log tables. We did not have the opportunity to use calculators. The current generation has the opportunity to use scientific calculators but not computers in exams. In my exams, I tell them, "Please use the internet, please use ChatGPT, please use your friends, please use your pets if you want, work in a group, pay somebody to take the exam for you, but get the job done." After having told all of this to them, only 50% are copying. The rest are saying, "No, no, I still will not copy. I will do it by myself." And then they come to my company and then they say, "No, I will discover the wheel by myself. I will not reuse, I will only reinvent." There is a place for originality, all of that. There is also a place for reuse and standing on the shoulders of technological innovations is not necessarily a bad thing, but it comes with consequences.

**Host**: Great. Thank you. I don't know, many of you are not sure if you're aware, so Anand is also a professor at IIT Madras, and he makes a lot of new nerds coming out in the space of artificial intelligence, data science, data. If you say data, I think that's him. I know, do check out. I think the biggest learning for all of us, why I really want him to be here is, Anand was not like this two years back. Not like this two and a half years back. He was not. I know him for years, I mean, I don't tell my age here, but or his age, but knowing him from so long. Two and a half years back, in the last two and a half years, if I see how he has transformed himself from being that old data science kind of a person, the old data engineering kind of a person to what he is today, you can figure out when you start following his posts on LinkedIn. He is someone who posts almost every day his thoughts and learnings because he wants to share with the world. With the opinion, if I'm not wrong, that when more and more people share like this, we learn, we are letting our LLMs learn more from it and it's going to help us as we need it. It’s a very different thought process. And I think if you are still using typing and creating PPTs, you do have a problem. If you are still using Excel and formulae on that, we still have a problem. We do have a problem. If you're still not able to understand how to do data analysis from data that you're seeing, you're trying to do manually a lot of things, that means we are not being efficient. I think our promise to our business is about making ourselves more efficient and making our businesses more efficient. And I think there's a huge opportunity. There's a world of abundance right in front of us. And as he talked about Moore's Law, it is always compounding continuously. So please ensure, reflect back, I think the recording is going to be there. Do take a look at it. I'm sure a lot of you will start looking at the recording again, what he did, how he did, how he did the comparisons, how he did the verification of one LLM with another LLM, etc. So please do that in your day-to-day life and ensure that we all actually embrace this as part of our life and not being afraid of staying away from it. That's the last thing that we want to have. And it very much ties into our overall strategy of this year of building the AI muscle. Okay? So thank you, Anand. Thanks a lot. That was eye-opening, heart-opening, I don't know what all to say. You know, I think on behalf of everyone, thanks a lot.

Thank you. Thanks a lot, sir. I also did not know it was so heavy.

</notes>

---

# LLMs: Ask me Anything

[BI Worldwide](https://www.biworldwide.com/) · 18 Sep 2025, 4:00 pm IST · [Chennai](https://maps.app.goo.gl/GxW7USQhuknHL3Vs5)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Transcript](https://github.com/sanand0/talks/2025-09-18-llm-ama-bi-worldwide/blob/main/README.md)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-18-llm-ama-bi-worldwide/)

---

## Quiz

1. **Arena vs. Accuracy:** How does **Arena Elo** differ from benchmark accuracy, and why does that matter for model selection? Cite a risk.
2. **Self-Consistency:** When does **self-consistency** help most? When can step-by-step prompting hurt? Give one concrete failure mode.
3. **Ensembles:** What model diversity / task types make **majority-vote ensembles** outperform single models? When should you avoid?
4. **Scaling Constraints:** Name two **non-algorithmic** constraints that could limit AI progress and describe one mitigation each.
5. **Prompt Safety:** Give one case where **emotion or role prompts** improved outputs, and one case where they **increased risk**.

---

## Errata

- **“It’s a gimmick title, inspired by Karpathy’s tweet.”**
  _Correction:_ Karpathy did write “I also like to think of this role as a kind of **LLM psychologist**,” popularizing the phrase; he did not formally “coin” or define a role. ([X (formerly Twitter)][1])
- **“Reasoning prompts help; step-by-step is the only reliable boost.”**
  _Correction:_ Chain-of-thought with _self-consistency_ is the evidence-backed boost on reasoning tasks; step-by-step alone can be mixed or harmful on some tasks. ([arXiv][2])
- **“Chatbot Arena’s Elo shows quality; frontier shifts.”**
  _Correction:_ Arena Elo measures **pairwise human preference**, not ground-truth task accuracy; it’s subject to biases and provider gaming concerns. Treat as one signal. ([LMSYS][3])
- **“Moore’s observation: compute scales \~every two years.”**
  _Correction:_ Moore’s Law concerns **transistor counts** (originally 1-year cadence, later \~2-years). It’s an empirical trend, not a physical law. ([Wikipedia][4])
- **“Demand drives optimization (Chrome/V8).”**
  _Clarification:_ V8 delivered large, measured speedups (e.g., \~20× over a decade; double-digit improvements in key periods), supporting the claim qualitatively. ([Chromium Blog][5])
- **“AI scaleups may exceed Moore’s pace.”**
  _Clarification:_ Industry figures (e.g., Nvidia) have claimed faster-than-Moore system-level gains; independent analyses warn of energy/data constraints tempering the pace. ([TechCrunch][6])
- **“70% automation at \~99% quality with ensembles.”**
  _Correction:_ This exact rate is **context-specific** (your internal experiment). Literature supports ensemble/majority-vote gains, but effects vary by task and model diversity. ([arXiv][7])
- **“LLMs can’t count; code can.”**
  _Correction:_ Many LLMs still struggle with arithmetic; specialized prompting/training narrows gaps on some benchmarks. Rely on **programs for guarantees**. ([arXiv][8])

---

## Counterpoints

- **Emotional/role prompts sometimes help.**
  Studies report gains from **EmotionPrompt** and **role-play prompting** on some tasks; effects are dataset- and model-dependent and can backfire. ([arXiv][9])
- **Emotion prompts can worsen safety/fidelity.**
  Emotional prompting can **amplify disinformation** or change model behavior in undesirable ways—so use sparingly and audit outputs. ([Frontiers][10])
- **Arena as a single metric is risky.**
  Community and academic critiques note **bias, selective disclosures, and Goodhart effects**. Combine Arena with blinded, task-grounded evals. ([Simon Willison’s Weblog][11])
- **Progress is not unbounded.**
  Energy, chip capacity, and data availability may **bottleneck scaling** this decade; policy and infrastructure timelines could dominate. ([Epoch AI][12])
- **LLM-as-Judge/ensembles have biases/costs.**
  LLM judges show **positional/verbosity/authority biases**; ensembles add latency/cost and can share correlated errors. Use calibrated disagreement routing. ([ACL Anthology][13])

---

## Feedback

- **Pin every claim to a number.** After bold assertions (“2,000× cheaper”, “post-grad intelligence”), add a one-liner with **metric, scope, date, and source**; show a tiny table or sparkline.

- **Label the stance of each statement.** Prefix key lines with **Evidence**, **Opinion**, **Analogy**, or **Anecdote** so listeners instantly know how to treat it; add one-sentence limitations.

- **Tighter demo arc, pre-redacted.** Declare **goal → plan → tool use → code → verify** in 60–90 seconds; show success criteria first; use redacted/sample data to avoid privacy detours.

- **Steer the room with micro-polls.** Open with a 3-option poll to pick the next segment; **re-poll mid-talk**; maintain a visible “parking lot” for deferred questions to keep flow tight.

- **Operational takeaways per section.** Close each segment with a **3-bullet SOP** (“Try tomorrow”), plus **guardrails** (checks, thresholds) so attendees can reproduce results safely.

[1]: https://x.com/karpathy/status/1627366426771337216 "Andrej Karpathy"
[2]: https://arxiv.org/abs/2203.11171 "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
[3]: https://lmsys.org/blog/2023-05-03-arena/ "Chatbot Arena: Benchmarking LLMs in the Wild with Elo ..."
[4]: https://en.wikipedia.org/wiki/Moore%27s_law "Moore's law"
[5]: https://blog.chromium.org/2018/09/10-years-of-speed-in-chrome_11.html "10 years of Speed in Chrome"
[6]: https://techcrunch.com/2025/01/07/nvidia-ceo-says-his-ai-chips-are-improving-faster-than-moores-law/ "Nvidia CEO says his AI chips are improving faster than ..."
[7]: https://arxiv.org/abs/2410.16543 "Large Language Models Powered Multiagent Ensemble for ..."
[8]: https://arxiv.org/html/2406.02356v1 "Language Models Do Hard Arithmetic Tasks Easily and ..."
[9]: https://arxiv.org/abs/2307.11760 "Large Language Models Understand and Can be Enhanced by Emotional Stimuli"
[10]: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1543603/full "Emotional prompting amplifies disinformation generation in AI large ..."
[11]: https://simonwillison.net/2025/Apr/30/criticism-of-the-chatbot-arena/ "Understanding the recent criticism of the Chatbot Arena"
[12]: https://epoch.ai/blog/can-ai-scaling-continue-through-2030 "Can AI Scaling Continue Through 2030?"
[13]: https://aclanthology.org/2024.emnlp-main.474.pdf "Humans or LLMs as the Judge? A Study on Judgement Bias"
[14]: https://arxiv.org/pdf/2403.04132 "Chatbot Arena: An Open Platform for Evaluating LLMs by ..."
[15]: https://www.reuters.com/business/energy/us-data-center-power-use-could-nearly-triple-by-2028-doe-backed-report-says-2024-12-20/ "US data-center power use could nearly triple by 2028, DOE-backed report says"

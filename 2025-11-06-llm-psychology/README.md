---
marp: true
title: LLM Psychology
author: Anand S
url: https://sanand0.github.io/talks/2025-11-06-llm-psychology/
theme: marpessa
paginate: true
style: |
  transcript { display: none; }

# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
# ChatGPT: https://chatgpt.com/c/690f49ee-b9e8-8320-9583-a0739df2f0d2
# Mind Readers Article: https://claude.ai/share/bdaaf00e-b593-484c-96e6-93d344819a64
---

<!-- _class: title -->

# LLM Psychology

[Madhu Decodes](https://www.youtube.com/channel/UCZLuqdSatDu-solUJzxRh6g) · 06 Nov 2025, 4:00 pm IST · Remote
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Video](https://youtu.be/grXvLwWQBAw) · [Transcript](https://github.com/sanand0/talks/tree/main/2025-11-06-llm-psychology) · [Article](https://github.com/sanand0/talks/raw/refs/heads/main/2025-11-06-llm-psychology/mind-readers.docx)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-11-06-llm-psychology)

---

# LLM psychology treats models like people to learn faster

- Treat language models as **minds we can probe** rather than black boxes.
- Ask clear questions, frame hypotheses, and collect evidence like a good study.
- Share findings in simple language so busy teams can act on them.
- The goal is practical insight that **makes it easy** to build better systems.

<transcript>
**Madhu**: Hello, and welcome all to another episode of Madhu Decodes, the podcast where we try to decode complex minds and technologies and job titles that are shaping our future in the world of AI. I am Madhu Satyaselan, your host today, and we have a guest in this show who demands to be decoded, and his work demands to be decoded. Our guest here is S. Anand. Officially, he is the Head of Innovation at Straive and the co-founder of a massively successful data storytelling company, Gramener. He has been named one of India's top 10 data scientists. He's a regular on TEDx and PyCon stages. His background spans from IIT Madras to IIM Bangalore.

But Anand is here today because of the title he gave himself: **the world's first LLM Psychologist**. Anand, it's an absolute honor to have you on this podcast, Madhu Decodes. I'm seriously intrigued and actually very excited to have a conversation with you. It's going to be a tremendous learning exercise for me.

**Anand**: Thanks, Madhu. Pleasure to be here.

**Madhu**: Thank you. Thank you, Anand. I think we have to straight go to the point. So the moment I saw your profile, the moment I knew you are an LLM Psychologist, I was really intrigued. So I think that's where my head is at: to start decoding the LLM Psychologist terminology itself. And I know through my research that this is the terminology that you have chosen to name yourself as.

So when we hear psychologist, we think of human minds, therapies, talking about biases, behavior, etc. So it is a fascinating concept for me to think about LLM having a psychology of its own. And I think since I've started reading, I've started looking at some of your podcasts and your work, I'm starting to think of LLM as different personas. I'm starting to think how LLM would talk like if he or she was a person like, say, Kamal Haasan, for example. So I keep thinking about all of those aspects.

So I wanted to hear from you. My first question is, why that specific word? **Are you actually putting ChatGPT in a couch and doing some therapy?** Or what do you do? Why is that terminology important and why did you choose it?

</transcript>

---

# LLMs show distinct personalities on human trait tests

- Models often display **very varied personalities** when you apply OCEAN-style tests.
- Some trend high on **openness and agreeableness**; others feel quieter or more cautious.
- Personality shifts with prompts and training, so measure, do not assume.
- See demo ideas: [OCEAN testing of LLMs](https://github.com/sanand0/talks/releases/download/talks/2024-08-10-TEDx-MDI-Gurgaon-LLM-Psychology.pptx).

<transcript>

**Anand**: I look at how LLMs respond to inputs. And **they have very varied personalities**. So if you literally take a personality test like the five traits test, popularly called OCEAN, where we evaluate LLMs on openness, conscientiousness, extraversion, agreeableness, and neuroticism. By default, they exhibit different personalities.

Now, models are trained to respond based on a personality that we can ascribe to them. So, it's not like models have only a fixed personality. But without asking them to take on any role, if we give them the standard psychological test that we give humans, then for example, **OpenAI tends to be very high on its openness to experience** — many of the OpenAI models, GPT-4o being a classic example when I ran it last year — and also on agreeableness. So, in a sense, it's kind of like if I take openness to experience as a spectrum from, let's say, people like Warren Buffett or Henry Ford or George W. Bush, who are conservative, practical, fairly rigid in their respective ways, to people like Einstein, Rabindranath Tagore, M. F. Husain, who are curious, open, and innovative. OpenAI, among the models, is probably a lot more on the latter side than any other model.

In contrast, let's say a model like Gemini Flash is a very introverted model. If you take famous personalities like A.R. Rahman or J.K. Rowling or Rahul Dravid, these are very reserved, quiet, reflective personalities, in contrast with, say, a Shah Rukh Khan, Richard Branson, Ranveer Singh—very sociable, talkative, energetic. And Gemini Flash is very much on the former end. So, part of what I do is trying to figure out how models behave, and psychological tests are not necessarily the best ways of analyzing LLMs, but my intent is to observe and extract this kind of information from them. And hence, the term LLM Psychologist.

</transcript>

---

# We study the model’s mindset, not the human

- Focus on the model’s tendencies, not the user’s traits.
- Map how prompts, format, and context steer the model’s choices.
- Use this map to pick the right model and prompt for the job.

<transcript>

**Madhu**: So who is the subject matter expert? So when we say a patient, are you studying LLM? Are you studying how they hallucinate, how they bias, how the world model is emergent? And are you studying a human user or who is being psychologically manipulated, who's using the LLM? Or delighted by AI responses? Or are you studying the LLM's mindset?

**Anand**: **Very much the LLM's mindset, not the human.**

</transcript>

---

# Benchmarks and price show value that keeps rising

- Track accuracy, speed, context, and **steady quality gains at lower cost**.
- Compare scores with what you pay to find the sweet spot.
- Watch market shifts often; pricing and tiers change fast.
- Reference: [LLM Pricing](https://sanand0.github.io/llmpricing/).

<transcript>

**Madhu**: Okay. So what do you do then? When you study the LLM's mindset, you kind of understand the personalities of those LLMs by way of your experiments, I suppose. So can you talk to us a little bit about your journey towards finding the LLM's mindset? What are the steps you do or what are the actions you take to study them, basically? And how often do you do that?

**Anand**: It's probably useful to think of LLMs more as people than as machines. And in that sense, when we look at, let's say, an employee, there are some basic questions that we ask. How much will they cost? How well will they perform their job? How fast are they? What is their background? Will they have a cultural fit and so on.

And in a sense, that's how I look at LLMs as well. **One of the things that I track on a regular basis is against a set of benchmarks, how well do they perform.** It's roughly the equivalent of giving an exam to an LLM. And what we're finding is that for a given cost, the quality of models has steadily improved. To give you an example, let's say if we move back in time to two years ago—no, November 2023—that was when GPT-4 was released. Now, at that time, it had the level of intelligence of—and I'm going to use chess Elo score ratings as an example. So, let's say an Elo score of 2400 would be a grandmaster level, but an Elo score of around 1200 would be maybe a local chess champion level. We already had models at a 1200 level with, let's say, Qwen 1.5 in October 2023. But in November 2023, there was a huge leap with the Elo score jumping all the way up to 1300—100 points of intelligence. Put another way, it's roughly like earlier we had 8th-grade level students among the model ecosystem. Now suddenly we have almost 12th-grade level intelligence coming out.

And at significantly higher cost. So, Qwen cost about 27 cents per million tokens. A way to think about it is if you gave it the entire, let's say, Harry Potter books, all seven, and asked it to process it and answer any question based on it, for it to read through the whole thing and answer almost any question would cost about 27 cents. In contrast, GPT-4 would have cost $10. Now that's almost 40 times higher. Huge difference. But over time, that cost has dramatically fallen. So for instance, OpenAI themselves in July ‘24, just eight months later, released the GPT-4o mini model. Roughly same level of intelligence, but cost-wise, 15 cents. That is 1/60th of the cost.

Now imagine, in November ‘23, a high school student comes in and says, "I will charge you $10 per million tokens." Seven months later, a student walks in and says, "I'm going to charge 1/60th," meaning you can hire 60 such students to do exactly the same thing. That's huge. And it's gone on. So, today for instance, as of November ‘23, you can take a better model, almost a second-year college graduate level intelligence with a model like GPT-5 Nano, and that would cost 5 cents, one-third of what even that student would have cost. Or, well, now graduate. And we have even higher intelligences. You could say that a model like Gemini 2.5 Pro or GPT-5 is about as smart as a postgraduate. And is coming at a cost of about a dollar to two dollars per million tokens. And that's also reasonably inexpensive.

So **part of what I do is research the economic value of different models and how they evolve over time, apart from their personality.**

</transcript>

---

# Small wins convert skepticism into sustained practice

- Early tests may feel underwhelming. Keep asking better questions.
- Simple tasks like chart advice can match expert checklists.
- **All around intelligence across tasks** shows up in classification and synthesis.
- Those moments build trust and trigger deeper experiments.

<transcript>

**Madhu**: Thank you, Anand. That is a good insight. So you understand the LLMs' capabilities by way of giving them certain tests. You evaluate how well they perform for what cost. And then you give a score to evaluate the effectiveness of a particular LLM, right? So that is what you essentially do as an LLM psychologist, right?

I think I'm a little bit more intrigued into your pathway, right? What decision point made you pivot? Because you did engineering in IIT Madras, and then you did MBA in IIM Bangalore. You worked in Boston Consulting Group, you did a lot of projects. But you did your own startup as well as a storyteller and a data expert in Gramener. And what was this aha moment that said, "Okay, this is my pathway," when AI came in, or even before AI came in? I think you were in the direction of thinking about LLMs and doing a lot of data-related analytics work that were anyway leading you to this journey, but when did you actually have the aha moment and what was the pivot?

**Anand**: ChatGPT was released in November 2022. And even before that, the GPT class of models had been released. So I had tried these in the past. For example, I was trying to see if the GPT-2 model could actually generate the configuration for some of the comic strips that we were playing around with. And it turned out that it had some moderate success, but it did feel very impressive. When ChatGPT was out, I tried it once, maybe twice, and I didn't really understand what the big deal was. **And this is how most opportunities get missed.**

There was a client presentation where they were looking to understand what the impact of AI was. I was forced to go back and try it out. I explored ChatGPT on 29th May 2023. I put in a question to ChatGPT, which was, "How can I visualize the change in sales since last month?" I'm in the data visualization space. I know this in and out. So when I as an expert looked at its answer, which was, it said to visualize the change in sales since last month, you can use various types of charts. Here are some popular options. It said line chart, and you would use it here's how you would draw it, here's when you would use it, bar chart, an area chart, a pie chart, a column chart, and mentioned A, when you would use which, how each of these would be drawn, what tools you could use. Like, it would suggest Excel, Google Sheets, Tableau, Python libraries, Matplotlib, Plotly. At that point, I said, "Okay, at least for a basic question like this, it has the ability to give the same answer as me, who is an expert in the field. That's not bad."

And then a week later, 8th June ‘23, I asked it, "Here are, here is a survey that I did of common problems that software developers have. I'd like you to firstly, summarize the five most common problems." And it did, which was fantastic. Then I said, "Okay, I get it. So now against these five buckets—communication, resources, timelines, work-life balance, process—I want you to categorize each of the original problems against that." And it did. Then I said, "Now tell me, which of these should I focus on to have the highest improvement on a software company's productivity?" And it went through, thought through step by step in detail and said, "Focus on the communications-related problems because that's what seems to be, A, mentioned more often, seems to have a higher impact because of these reasons."

Now, given the volume of input, this is something that would have taken me at least a few hours. So definitely a time-saving tool. But **what impressed me was in the middle stage where it did that categorization. I'm not sure I could have come up with a categorization that was as good.** So here is something where it actually has higher intelligence than me. And that's where it struck me. **We are talking about an all-around intelligence, something that may not be as good as an expert in a specific area, but is reasonably good in almost all areas.** So where I have deep knowledge, sure, I'll give an answer. But almost anywhere where I don't have that deep knowledge, here is a tool that I can use to answer my questions, **which means that my need for average people supporting me has suddenly vanished. And that is a huge discovery.** That point, I became a total convert.

</transcript>

---

# Different models fill gaps across tasks and media

- Try multiple models because each has strong and weak spots.
- Some shine at images or long context; others focus on speed.
- Switch models when a task needs a skill your default lacks.

<transcript>

**Madhu**: How did you start learning other LLMs? What intrigued you apart from ChatGPT?

**Anand**: Partly to see what else is out there, partly to fill in some of the gaps that I had. Every model has its pros and cons, every tool or application has its pros and cons. So I was exploring. Price and cost are certainly a constraint. When the Gemini models came out, they were practically free for fairly high compute capacity. GPT-4, for instance, was not available for free unless you were using Microsoft Copilot, whereas Gemini 1.5 Pro was available for free for a fairly large usage limit. I said, okay, that gives me higher intelligence in a more accessible way. But it also allowed me to explore some of the things that, let's say—so Gemini models, for instance, allowed me to process images, which ChatGPT in the initial stages did not do or did not do as well. So depending on my need and the lack of a tool's ability to solve my needs, I started looking out and found others.

</transcript>

---

# Leverage your strengths and practice every single day

- Build on your domain strength so the model’s answers land better.
- Set a high daily reps target; **practice is really all that counts**.
- “Think step by step” often helps; emotional pleading often hurts.
- Evidence: [Emotion prompting tests](https://sanand0.github.io/llmevals/emotion-prompts/), Zero-shot CoT research.

<transcript>

**Madhu**: I'd like to understand a little bit more about the journey so that my listeners who want to become, say, LLM psychologists or who want to venture into this type of work need to understand what they need to invest, right? So I'd like to understand, you are a technologist, hardcore technologist. You were deep into these concepts already before you ventured into your experiments on LLMs. But say from 2023 to 2025, you would have done a lot of homework to to keep going, to keep experimenting and things like that. So I would like to talk about that part of your exercise. What kind of homework you normally do to keep up with your information about LLMs? And not only that, I would also like to touch upon, is it important to be a technologist to start investing time and energy in a concept like this? So those two, I would like to hear from you.

**Anand**: I think a lot of **the strength that we derive is from strengths we already have**. So I am a technologist and therefore chose a technology route. But someone who is, let's say, a legal expert would probably be able to get more legal assistance out of an LLM than anyone else would. And by doubling down on their strengths, they are extracting the best out of that tool. Remember, I mentioned that AI is almost like an all-rounder. But when it gives an answer, I am able to shape its answer much better in my area of expertise, therefore get more out of it. In an area outside of my expertise, I'm just relying on its wisdom.

So if we want to get the most out of a tool, it certainly helps to take assistance where we are not experts in that area. But it makes sense to improve our expertise by prompting it repeatedly where we know it well. And from that perspective, I would say two things. One, the area of expertise doesn't matter. Do leverage your expertise; you don't have to be a technologist to leverage LLMs. Second, **practice is really all that counts**. **I had a target of having 50 conversations with ChatGPT or any LLM every day.** I'm probably still far from it, but having a target and getting as close to it as I could definitely helped.

And doing this like any other form of study in a systematic, intentional way. So for instance, I was experimenting with—I saw a blog post that if you tell ChatGPT or any Gemini or Claude or any of these models something like, "Oh dear, I'm totally overwhelmed, I need your help this second. My life depends on it. I'm counting on you"—that sort of emotional blackmail, it does a better job. So is that true? I said, let's take this prompt with and without this prompt. If I ask LLMs to multiply a bunch of numbers, do they get it right more often? Do they get it wrong more often? And it turns out that, of course, the answer varies, but on average, emotional blackmail makes models perform worse. Roughly, and I tested this across about 20-odd, 28 models. For seven models, it performs better; for 21 models, it performs worse. So that's not a good sign.

On the other hand, a statement like, "Think step by step," that actually tends to improve most models, and by a reasonable amount. And that, of course, also led to the emergence of most LLM players including that kind of a prompt in the models themselves. So simple things like if somebody says something, let us try it out, let us see if it works, if it doesn't work, that's an example of intentional practice, and it helps.

</transcript>

---

# Publish logs, stories, and prototypes to compound learning

- Keep a “Things I Learned” log to capture patterns fast.
- Turn bigger experiments into data stories others can read.
- Ship small prototypes so teams can try ideas immediately.

<transcript>

**Madhu**: The intentional practices or questioning time and again on different concepts, you get an inspiration from the internet, you get inspiration from news, and your own curious mindset leads you to the journey of finding out what an LLM behavior is looking like. So do you then create an LLM psychology report? Or do you maintain a diary or a log of LLM's psychological journey?

**Anand**: I do that at three levels. One, anything that I find interesting, I note in a "Things I Learned" log and publish it. For larger experiments, I create data stories out of those and publish them. And for where I'm trying out a functionality, I build a model, a prototype, a mini application of sorts, and publish that as well. All of these are on my GitHub repository.

</transcript>

---

# Cross-checking models cuts errors and boosts trust

- Start with a single pass to gauge baseline quality.
- Add double or triple checks; **error rates fall sharply with more checks**.
- Send disagreements to humans; total manual work drops a lot.
- See: [Double-checking impact](https://sanand0.github.io/llmevals/double-checking/).

<transcript>

**Madhu**: I think that's a very good pivot into the why, the value of AI therapy or the value of an LLM psychologist's work. So let's talk about the benefits. Because this isn't an academic exercise for companies, the CXOs, the developers are listening, what are the tangible business benefits of having an LLM psychologist on a payroll?

**Anand**: A lot of clients have questions, objections, confusions about LLMs. And being able to help them understand in a systematic way how a problem can be addressed or bypassed is where somebody like me comes in. For example, one of the classic objections to using LLMs is, "Oh, but they hallucinate." That is, they can make mistakes. How do we address that? Now, the truth is, humans hallucinate as well, meaning they make mistakes. How do we deal with it? And that's easy. That's standard management practice. We have someone else verify their work.

So I ran an experiment to see, supposing we asked an LLM to classify chat messages into a bunch of categories, how often do they get it right on average? And it turns out that for the dataset that I was looking at, about 14% of the time, they make mistakes. Okay. What if we had two models cross-check and only if they both agree do we take the result? It improves the error rate, brings it down to 3.7%. That is effective. Now, we can do triple checking, quadruple checking, quintuple checking. And it turns out that the error rates fall: 2.2%, 1.5%, 0.7%. So we can take it to 99.3% accuracy. And the remaining, where even one model disagrees with any of the others, we can have a manual check. But even then, that amount of work of manual checking is only 28% of the total work, which means that 100% of the work has reduced by 72% to just 28% of the manual work. And overall, I have an accuracy of 99.3%.

Now, the models are so cheap that quintuple checking is barely any incremental cost to a single check. And therefore, people say, "Ah, okay, I get it. I now have a lever to control quality, trading it off against the effort." So I can decide if I want double checking or triple checking or quintuple checking. And then which models should you use to improve the effectiveness? Some models tend to think differently, so you would want to pair those. Which are those models? These are the kinds of things where if someone's constantly experimenting, researching, and sharing with the organization, they have an advantage in being able to share with clients and help them move forward in their AI journey and therefore leading to a commercial benefit as well.

</transcript>

---

# Limit risky powers to keep agent systems safer

- Risk spikes when a system holds private data, reads untrusted input, and talks out.
- Pick only two at once to stay safer, and monitor activity.
- Use strict prompts, scoped permissions, and clean data sources.
- See: [System prompt overrides](https://sanand0.github.io/llmevals/system-override/).

<transcript>

**Madhu**: So do you think this is going to be a frontier for AI safety and security as well? Because that is a big question when we talk to business owners. I think people have the question back of their heads. Yes, some of the early adopters are enthusiastic to adopt AI in their business, but the big question everybody asks is how safe is their data, how much they need to rely on AI safety and security systems that exist today. So will this LLM psychology experimental position give answers to AI safety as well?

**Anand**: There are two parts to AI safety at the moment. One is a hard, guaranteed kind of safety, and another is a softer, "try and make sure there are fewer problems" kind of safety. For, let's say, an internal application, the latter is sufficient. Give me more capability, but if a system is unsafe, it means that data leaks from one part of the organization to the other part of the organization. It's not a disaster. If, for instance, one of my colleagues gets my email ID, it's okay. If, on the other hand, it were an external-facing application, if a spammer gets hold of my email ID, that is not an acceptable outcome.

For solving the hard problem, there is what is called the **lethal trifecta**, which is a term that Simon Willison coined. There are three things: access to private data, the ability to communicate externally, and exposure to untrusted content. If you have all three, your system is unsafe. You can choose any two out of these. You can say, "Look, I won't give you my private data. But I am okay to expose to untrusted content; read whatever I want. And I'm okay to communicate externally; send whatever I want." No problem. My private data does not even come into the picture. Or you could say, "I will give you access to private data, and you can even communicate with the rest of the world. But the only thing that you can read is trusted content. I will not allow a hacker to write something that goes into your prompt."

So, in short, it is possible to engineer systems that can only that can access private data, talk to anything, and read anything, as long as you pick only two of these. But for full capability, you want to be able to access private data and talk anywhere and read anything. All three are required for a good, capable system. In that case, we have to mitigate it as much as we can, recognizing that we cannot fully solve the safety problem. And managing prompts, different degrees of permissions for access to private data, try and make sure that the sources are as cleaned up as possible—these are measures that people are trying to take.

**Madhu**: So you've given the answers for therapies basically. So you've said prompt therapy and maybe the choice of model as a therapy. Pretty much. And then of course, re-evaluating elements as another therapy. So very interesting take, very, very interesting take. This is the beauty and complexity of the new world we are stepping into.

### 

**Madhu**: I've coined this kind of a rapid-fire round. I'm going to throw you names or personalities in different fields, and you can probably prescribe an AI or an LLM that they would be better off using or that would enhance their work in their current working model. If you could think about that and let me know. Shall I start giving you names?

**Anand**: Sure.

</transcript>

---

# AI can expand a composer’s creative palette

- For cinematic orchestration, try **AIVA** to sketch themes and export MIDI.
- For quick song ideas, **Suno** lets you draft, iterate, and share.
- Use AI for exploration; keep the final taste human.

<transcript>

**Madhu**: Okay. So for music, let's go with A.R. Rahman. You mentioned A.R. Rahman earlier. So he is a master of blending complex tradition with cutting-edge technology in the music world. Oscar award winner. What would his AI collaborator tools look like? What kind of an LLM he might use for his sounds?

**Anand**: He might use a tool like **AIVA**—A-I-V-A—which is specifically built for cinematic orchestration. It's an AI tool with about 200-odd styles, MIDI export. It can identify the composer of specific songs and the legalities associated with it. Though for the common man who's trying to compose music, a tool like **Suno**—S-U-N-O—might be more apt.

</transcript>

---

# AI can guide athletes and investors with data

- For court analytics, **SwingVision** tracks shots and flags patterns.
- For venture research, **AlphaSense** summarizes filings and transcripts quickly.
- General models can still draft memos and review pitch decks well.

<transcript>

**Madhu**: Next one, for sports: Serena Williams. She's an athlete on court but a powerhouse of venture capitalist. So what AI should she use to go for the court and for the boardroom?

**Anand**: For the court, maybe something like **SwingVision**, which gives AI-based shot tracking and coaching directly from a phone. For the boardroom, for a VC, maybe something like **AlphaSense**, which can accelerate venture research with generative summaries across filings and expert sources. But arguably, even the likes of ChatGPT Pro or Claude's Max, which can do some fantastic deep research both on the sports side but even more importantly across portfolio companies, pitch decks, for example.

</transcript>

---

# AI helps authors speak to every language and reader

- **IndicTrans2** and **Sarvam AI** support many Indian languages with strong fidelity.
- **NotebookLM** can turn sources into overviews and ideas you can explore.
- Together they help stories travel to new audiences.

<transcript>

**Madhu**: Okay, thank you. That's a good insight, and I think that's a good insight not just for Serena, I think also for other AI entrepreneurs who are wanting to venture again into that world. So next one is for philanthropy and literature: Sudha Murty. She's an engineer, a beloved author, philanthropist, a storyteller as well. I love her storytelling narratives. What AI do you give her to scale her impact and empathy that she's already very good at?

**Anand**: Possibly something like **IndicTrans2** or **Sarvam AI**, which have strong translation capabilities across a wide variety of Indic languages for the stories to reach a wider audience. And something like **NotebookLM**, where she could take hundreds of thousands of stories and reports across multiple sources, create audio overviews, and have it generate stories for her or story ideas perhaps.

</transcript>

---

# AI can scale advocacy and defend trust in media

- **Quorum Grassroots** and **VoterVoice** personalize outreach at scale.
- **C2PA** content credentials help audiences verify source and edits.
- Use these to grow reach while protecting credibility.

<transcript>

**Madhu**: Thank you, Anand. That's nice. Next one is for global advocacy: Michelle Obama. She runs global initiatives for education and health, very powerful communicator in the world. What would be her AI prescription?

**Anand**: One possibility would be something like **Quorum Grassroots** combined with **VoterVoice**. This has the ability to generate hundreds of unique message variations, reaching a large number of people in a far more personalized way. Or something like **C2PA**. These are content credentials. They allow media to counter deepfakes and build public trust. These are some of the tools that you could use in public discourse.

</transcript>

---

# AI turns practice sessions into measurable coaching

- **CricViz Centurion** helps plan match strategy from deep cricket data.
- **StanceBeam** quantifies bat mechanics during nets for feedback.
- **Full Track AI** adds phone-based ball tracking and biomechanics.

<transcript>

**Madhu**: Now, coming back to sports again, Virat Kohli. A different kind of athlete. He's obsessed with data, peak performance, computing real-time strategy, right? What would be his personal AI performance coach?

**Anand**: Possibly something like **CricViz Centurion**. It's a comprehensive cricket database combined with models that predict the expected number of runs and can guide on match strategy. Or something like **StanceBeam**. That's a tool that quantifies the bat mechanics in practice. Or tools like **Full Track AI**, which can convert your phone into a full-fledged ball tracking application and also provides biomechanical feedback during net sessions for self-coaching sessions.

</transcript>

---

# AI tutoring can lift learning where teachers are scarce

- **Khanmigo** offers guided help rather than direct answers.
- Students get patient tutoring; teachers gain planning support.
- At scale, this can narrow learning gaps in many regions.

<transcript>

**Madhu**: Okay, something everybody can use as well. It's not just for Virat Kohli, for the aspirants in the cricket world. Yeah, that's nice. A what-if situation for our beloved A.P.J. Abdul Kalam, our scientist, educator, president. What AI would have helped him accelerate his vision for 2020 in India?

**Anand**: I think **he would have loved the Khan Academy AI**. I'm trying to remember its name… **Khanmigo**. Which allows tutoring through AI across a huge number of students. I think he would have really liked… **really good content to have reached students where we do not have good teachers to educate them.**

</transcript>

---

# Curiosity and clear experiments keep you ahead

- Keep asking “What changed, by how much, and at what cost?”
- Share simple dashboards and narratives teams can absorb quickly.
- Build reusable prompts and templates so progress compounds.

<transcript>

**Madhu**: Thank you. I know you're making a lot of sense for the title. You're giving it a lot more justification. Thank you so much for being here and talking to our audience. Thank you so much.

**Anand**: Thank you for the opportunity. Lovely talking to you, Madhu.

</transcript>

---

<!-- _class: title -->

# LLM Psychology

[Madhu Decodes](https://www.youtube.com/channel/UCZLuqdSatDu-solUJzxRh6g) · 06 Nov 2025, 4:00 pm IST · Remote
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Video](https://youtu.be/grXvLwWQBAw) · [Transcript](https://github.com/sanand0/talks/tree/main/2025-11-06-llm-psychology) · [Article](https://github.com/sanand0/talks/raw/refs/heads/main/2025-11-06-llm-psychology/mind-readers.docx)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-11-06-llm-psychology)

---

# Quiz

1. Why does pairing multiple models reduce manual review work even if some still disagree?
2. When would you switch models rather than prompts, and why?
3. How can content credentials change audience trust in public campaigns?
4. What daily habits most improve your prompting skill over a month?
5. Why can “think step by step” help while emotional framing harms results?

---

# Errata

1. GPT-4 launched on **March 14, 2023**, not November 2023. ([Wikipedia][1])
2. ChatGPT launched on **November 30, 2022**. ([OpenAI][2])
3. Gemini access and limits vary by plan; free tiers exist but have **prompt and rate** caps. Pricing and caps change. ([Google AI for Developers][3])
4. “Think step by step” (Zero-shot CoT) is empirically shown to improve reasoning on many tasks. ([arXiv][4])
5. The **“lethal trifecta”** term and pattern are from Simon Willison’s security guidance. ([Simon Willison’s Weblog][5])

---

# Counterpoints

1. LLM “personality” can be unstable or prompt-dependent; refusal rates and reliability vary across tests. ([ACL Anthology][6])
2. Cross-checking models can still fail when errors are **correlated** across providers or architectures. ([arXiv][7])
3. Elo ratings compare systems within a pool; they **do not measure absolute intelligence**, so analogies can mislead. ([Wikipedia][8])
4. Emotion prompts sometimes help engagement, but effects on accuracy are **task-specific** and not consistently positive. ([arXiv][4])
5. Safety is more than “pick any two”; new agent patterns try to reduce prompt-injection risk even with broad powers. ([Simon Willison’s Weblog][9])

---

# Feedback

1. State dates and prices with exact sources to anchor claims.
2. Separate anecdotes from experiments and label each clearly.
3. Bring one simple chart on price-to-quality over time.
4. Show one failure case where cross-checks still miss an error.
5. Leave listeners with a one-page “start here” checklist of tools and habits.

[1]: https://en.wikipedia.org/wiki/GPT-4 "GPT-4"
[2]: https://openai.com/index/chatgpt/ "Introducing ChatGPT"
[3]: https://ai.google.dev/gemini-api/docs/pricing "Gemini Developer API Pricing - Google AI for Developers"
[4]: https://arxiv.org/abs/2205.11916 "Large Language Models are Zero-Shot Reasoners"
[5]: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ "The lethal trifecta for AI agents: private data, untrusted ..."
[6]: https://aclanthology.org/2025.findings-naacl.469.pdf "Do LLMs Have Distinct and Consistent Personality? TRAIT"
[7]: https://arxiv.org/abs/2506.07962 "[2506.07962] Correlated Errors in Large Language Models"
[8]: https://en.wikipedia.org/wiki/Elo_rating_system "Elo rating system"
[9]: https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/ "New prompt injection papers: Agents Rule of Two and The ..."

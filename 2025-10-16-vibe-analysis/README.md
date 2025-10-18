---
marp: true
title: Vibe Analysis
author: Anand S
url: https://sanand0.github.io/talks/2025-10-16-vibe-analysis/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
---

[sheet]: https://docs.google.com/spreadsheets/d/1z88_6xa-uVgE4BTScpwIC7jKYfnstYLk-UEoflhdQ0g/edit?usp=sharing

<style>
  transcript {
    display: none;
  }

  blockquote {
    font-style: italic;
  }

</style>

# Vibe Analysis

[Landmark Group](https://www.landmarkgroup.com/) · 16 Sep 2025, 11:00 am UAE · Remote
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Transcript](https://github.com/sanand0/talks/tree/main/2025-10-16-vibe-analysis)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-10-16-vibe-analysis/)

---

## Playful experiments make learning stick today

- **A playful tone lowers pressure** and invites curiosity; we try odd ideas and keep what works.
- Tangents (like fun T-shirts) **model creative risk-taking** you can use at work.
- Expect experiments; **some will fail fast** and teach faster.

<transcript>

**Anand**: Okay, perfect. Thank you, folks. I will be going through a bunch of slides. The slides are not—well, actually the slides are important because that's where you'll get a few links that are essential for this workshop. I have also put in the link in the chat window. I'm not going to explain much about the LLM psychologist business other than to say that it looked like a cool title, so I thought I'll play around with it. **In fact, I even have a t-shirt with my name and the LLM psychologist title printed on it.** The back of the t-shirt is an AI-designed picture of me. I basically was trying out Nano Banana and said, what the heck, let's create an AI picture. And what's the point of an AI-generated picture if you can't put it on your t-shirt? So I ordered a custom one.

But that's the kind of stuff that I do, play around in completely useless ways and share the uselessness with as many people as possible. This is supposedly a workshop where you will be learning stuff, but in reality, it is also a workshop where I'm hoping to use all of you as guinea pigs and try out some experiments. Let's see how they go.

</transcript>

---

## Active chat and a shared sheet make this work

- **Post questions in chat** anytime; you can also unmute and jump in.
- **Answer each other**—peer help speeds learning.
- **Share progress on the [Google Sheet][sheet]** so we can guide you in real time.

<transcript>

Since this is an online workshop, please put in any questions, comments, whatever you have on the Teams chat window. If you are not on this Teams, please get on to this Teams, mute, turn off the speakers, whatever if that helps, or whatever method, but please do make sure you have access to the chat. I will also—yeah, the chat need not only be between me and you, it can be between you as well. Feel free to answer each other's questions, comment on those, or just unmute yourself and ask, comment, whatever. Just stop me. Two hours of monologuing is pretty painful.

As we go through, there is a Google Sheet whose link I have shared in this presentation and will also share on the chat, where as we go along, we'll be tracking your inputs, your progress, and so on. Your names ought to be here, and I am going to sort alphabetically so that it will be easier for you to locate your name. If you don't find your name, please add your name and we'll sort again. And as we go along, you can fill in the details. But yeah, at least the first two you're welcome to fill in now in a minute or two, but the rest, you can fill in as we go along because I'll give you the context for what to fill in.

And while, you know, two hours... the limit for a person to not get bored is apparently about 20 minutes, which is why the TED Talks are for 20 minutes. This is six times longer than that. You will get bored. When you're bored, please do whatever else. Just pretend that you're focusing on the workshop. Watch YouTube videos on your laptop if you want, but don't push yourself.

</transcript>

---

## We adapt the plan to your tools today

- Tell us your **ChatGPT plan** and whether you have **[VS Code](https://code.visualstudio.com/)**.
- If you use hosted models (e.g., LiteLLM), **that’s fine**; we’ll route Codex accordingly.
- **Add your GitHub profile** on the sheet so we can publish later.

<transcript>

Let's do a quick check on the setup. The first question is, what is your ChatGPT plan? If you have a paid account, then we will do certain things in a slightly different way. If you don't have a paid account, we will do things in a different way. My assumption during this workshop, which is different from what Vinay shared, was that we would be going the Codex route, but we don't have to go the Codex route. We'll try, we'll try a whole bunch of other things.

**Participant**: And yeah. Sorry Anand, I think—Sorry Anand. I think everyone has access to a LiteLLM's self-hosted LLM model. I think if anyone's having issues connecting that to the Codex and customizing it, please speak to Sreejith or Akanksha, our coordinator. But otherwise, you should be able to get Codex running with our hosted models. Yeah. If otherwise, if you have a pro plan, please use, feel free to use the pro plan as well.

**Anand**: Cool. So let's explore that. I'm just getting a sense. Okay, so there's nobody who's mentioned a no—okay, Sandeep has mentioned no against Visual Studio Code. Sandeep, that's a no, you don't use Codex, you use Vim or Emacs or some such thing? Or is that a no, you don't code?

**Sandeep**: I don't do code.

**Anand**: Wonderful. One person. We will—yeah, you don't need code. We'll very much work on this. Another question, and we will be doing some public data analysis. So I'm going to jumble up the questions a little bit. Is there—Okay, I'm going to assume that everyone has, or if not, can create a GitHub repo. So, I am going to add a column and ask you to fill out your GitHub profile link.

So, and actually I'm going to move that question a bit before. And yeah, if you could fill out column D as well. Yeah, let's begin with you filling out columns B, C, and D. With column D being the link to your GitHub profile if you have one. If you don't have one, please let's create one by going to github.com and logging in. There should be a sign up, and you'll be able to sign up with practically any email ID. Or yeah, with your Google account or your Apple account.

</transcript>

---

## Vibe analysis focuses on outcomes, not code

- Set a baseline: **Would you ship LLM insights straight to execs?**
- **Vibe coding**: pretend the code doesn’t exist; ask for the result.
- **Vibe analysis**: focus on the **business outcome**, not intermediate steps.

<transcript>

Now, while you're doing that, let's talk a little bit about a starting baseline. See, on the one hand, since we're going to be doing vibe analysis, it's good to know that LLMs can do analysis and we'll be playing around with it. But LLMs can totally mess things up. You've tried it, you know the problems that there can be.

So, I'd love for you to think a little bit about, given the power of LLMs and given the risk of LLMs, where are you, mindset wise, on: **can LLMs deliver exec reporting? That is, are you—how confident are you that you'd be able to have an LLM-delivered analysis, insight, report, whatever, straight to a senior exec?** If you are very confident, put in a yes. You're saying, "Yeah, most often it can do it," sure. You're saying "somewhat often," put that in. If you're saying, "Look, I don't think it will ever get to the point where I can take it straight to an exec," put in a no. Very rarely, sometimes, whatever. Just let's start with your baseline of opinion in terms of can an LLM-delivered insight be taken straight to an exec? And by straight, I mean without even looking at it, let alone verifying it. Because that's what vibe analysis is about. Vibe analysis is saying, I am going to have the LLM do stuff. I am going to pretend that the code does not even exist, that is vibe coding. Further, I'm going to pretend that the analysis itself doesn't exist. That's vibe analysis. I'm only going to focus on the business outcome. There's data, there's outcome. Nothing in between.

</transcript>

---

## Pick high-impact analyses your stakeholders actually value

- List **data + analyses** your stakeholders care about; think value and pain today.
- **Keep it public** on the sheet—no sensitive info.
- We’ll **start from your ideas** and build fast demos.

<transcript>

Another question that I'd like you to explore, think about, is: **what can we use, what can we analyze? What data, what use case, that will have high impact?** Now, think about the stakeholders that you are catering to across different functions. Think about what's difficult or time-consuming today. What is valuable for your stakeholders? And share, based on that, what data or analysis you think would have high value. Please put this in, keeping in mind that this sheet is public. So, do not put in anything that is sensitive. Put in whatever you are comfortable sharing publicly.

Now, we are going to spend a few minutes just letting you fill out this particular one while I take a quick look at a few things. We have about 30-40% with a ChatGPT plan. Got it.

**Participant**: Someone in the roadmap was saying something?

**Anand**: No, I think it was me. Sorry.

**Participant**: No worries.

**Anand**: Practically everyone except Sandeep and Shikha have a VS Code account. Shikha, I'm guessing you don't program in the course of your day. Is that right?

**Shikha**: No, no, I do.

**Anand**: What editor?

**Shikha**: Sorry?

**Anand**: What editor do you use?

**Shikha**: You're not audible. Hello? Am I audible?

**Anand**: You're audible. What code editor do you normally use?

**Shikha**: Sorry.

**Anand**: Can anyone else hear me? Okay, Shikha can't hear me.

**Participant**: We can hear you.

**Anand**: Okay. Okay, Shikha's rejoining. Cool. Not a problem. And I'm guessing the others who have—Okay, Sarah, what editor—okay, editor do you use? Sahil, what editor do you use? Nesrin, Minnie? You're welcome to type in the chat window. I'm just particularly keen on getting a feel—not getting a feel, making sure that I know where everyone is in terms of their editor setup, please. Because if anyone's not able to follow along and I need to put in a different editor, I will factor that in.

In the meantime, almost everyone's been able to also set up their GitHub account. Which is good. And we are starting to get inputs around the LLMs delivering exec reporting and there's a mix of responses. We'll come back to this later. And I guess people have started filling in the data and analysis that you think will have high impact. That is great.

Okay, and Suresh, you use Codium. Okay, interesting. But you also have VS Code, which is cool. I haven't tried Codium. And it's a fork. Okay, yeah. Sorry, any fork of VS Code works. I mean, as far as column C is concerned, if you have VS Code or a fork of it, please, just assume that it's working fine.

Okay, and some people have jumped to B1, which is great if you also have the Codex plugin and Python installed. That's perfect. For those of you who don't have Python installed, I would encourage you to install Python as well.

I'm just waiting for a few people to fill in some examples of data and analysis with high impact that can be a starting point for us to dive into specific data sets.

Okay, for those of you who have created your GitHub accounts, the next step, since practically everyone has VS Code—and Sandeep, Sarah, in your case I'll share what you might be able to do—you can go ahead and install Visual Studio Code. Sandeep, Sarah, you will want to install Visual Studio Code, but others, if you don't have the Codex extension, please jump to slide 10 and install the Codex extension. If you want to do it on your VS Code terminal, go right ahead. And please also make sure that you have Python installed. I will share a link to a tutorial. And this is for Sandeep, Sarah, and I'm just checking if there's anyone else with a no. Okay. Sandeep and Sarah, please follow these instructions. They are step-by-step instructions. Hopefully should not be too complex. And with that, we will all be able to run code locally on our machines.

Okay, we have a response on the kinds of data analysis that will have high impact. From Suresh, it's an analysis of mobile application catalog files to measure the performance of build-to-build performance deviation. Nice. Performance analysis is a fantastic use case.

Speed of AI image generation and accuracy of image as per prompts. Vidul, that's interesting. You're saying that that's a data set whose analysis will have high impact? Could you maybe unmute and explain?

**Vidul**: Yeah, hi. So, we basically work on AI generation of content right now, and we are using Nano Banana models. So recently, what data we check is how, what is the accuracy of the image which we get as per our prompts. And how, what is the speed of the NA10 workflows or the Nano Banana model which is giving us that image?

**Anand**: Fascinating. Again, performance related on this. Yeah. You know, given this kind of use case, I'm very tempted to just completely skip the public data set. We should just be working with your data sets. Wonderful. Let's just wait for a few more use cases to emerge and then we can dive in.

In the meantime, I'm also keeping an eye on the Codex plus Python installation column. Pravin, if you could take a shot at installing the Codex extension, at least, and certainly Python as well if you could, that will allow us to follow along.

One more use case and we can then dive in.

Okay, we have Devbrat saying allocation and replenishment data to arrive at stock availability. Could you unmute and share a bit more about this use case, Devbrat?

**Devbrat**: Yeah, hey hi Anand. So, I specifically work with the planning and allocation replenishment team, wherein we oversee the initial allocations and subsequent replenishment to stores of stock. So, basically analysis of that to determine what is our availability percentage right now, whatever stock we initially launched, is available at the store in subsequent months or not.

**Anand**: Fantastic. Do you have VS Code, Codex, or Python set up?

**Devbrat**: Yes, I do.

**Anand**: Wonderful. Actually, others, if you don't mind, let's start with this because of the use cases that we talked about, this one is probably most amenable to synthetic data generation. But even before we go there, Devbrat, do you have a public data set of this kind that we can use?

**Devbrat**: I have some data, let me just manipulate it so that we can use it in the session.

**Anand**: Let's do something different. Since you have data, what I'll do is there is—one of my colleagues built a small prototype where we can generate synthetic data of arbitrary kinds that follow a certain hypothesis. I'll ping the link. You'll need to provide an API key for it to work. In my case, I've already set it up by connecting it to our open router API. So works for you, doesn't work for you, doesn't matter. I can run this and share the data set with you, maybe even over Teams.

So what we want to do or what we can do here is you describe the data set and we'll have it generate the data accordingly.

**Devbrat**: All right.

**Anand**: Go on. I'll type, you talk.

**Devbrat**: Just let me just opening my Excel so that I can be as accurate.

**Anand**: Yeah.

**Participant**: Or you could just share the headers for the Excel spreadsheet. I think it's probably easier.

**Anand**: Yeah, that was—

</transcript>

---

## Rules-based synthetic data bakes insights into samples

- Define **columns, hierarchies, geography, dates, sales**—whatever mirrors your world.
- Ask the generator to write **behavioral rules** and **realistic outliers**.
- **Weekend logic varies by region**; bake such nuances into the data.

<transcript>

**Devbrat**: Yeah Anand. So in the data set, we would mostly have the concept name, which is your brand, as we have multiple brands.

**Anand**: Yeah.

**Devbrat**: We would have the date key. Our product hierarchy, which is group, department, class, sub-class.

**Anand**: Okay. I'm going to just say class. Go on.

**Devbrat**: Yeah. Then we would have the territory. So the data that I'm right now describing to you is for a weekday versus weekend sales.

**Anand**: Okay.

**Devbrat**: This is also one of the analysis that we do perform. So then we would have the net sales amount. The retail quantity, that is what was the quantity that was sold on that particular date. The retail cost. And yes, so this is the raw data that we would have. Against this, we would proceed to analyze whether, depending on the date, which day of the week it was and whether it was a weekend or weekday, and then club it and go on with our analysis.

**Anand**: Got you. Fine. So not quite the allocation and replenishment data. This is slightly different data. All right, fine. Let's go with this. Now, what I'll also say is, let's see. I want you to put in realistic patterns that occur in retail. Think about a series of hypotheses on how exactly retail would work, and this is specifically in the Middle East, so keep that in mind. Make sure that there are a few outliers, exceptions, unusual patterns that we normally find in data as well.

Let's transcribe that and hopefully that will in a few seconds... Okay, might have been faster too. We will be analyzing weekday versus weekend sales as well. And have it generate the data set. Now, the other thing of course that I could do is have ChatGPT take exactly the same system prompt, blah blah blah. Allow me to download the data set. And run.

Now, what you are seeing is effectively a somewhat standardized way by which we can create synthetic data for various purposes. So, I effectively have a system prompt that says you are a synthetic data generator and asking it to follow certain rules when generating the synthetic data. Of the rules, the one that I find most important is that we are asking the LLM to create behavioral rules about the generated data and then implement it. In other words, it's not about creating random stuff, it's about creating stuff that will actually have insights baked in. So which will make it a little more realistic. And then yeah, we have it generate the output.

So this is going to take its own sweet time whereas this might be a little faster. It's created some code. I am going to run this code and let's see how much data we have. My preference is to get to at least 100,000 rows. But we have not—ah okay, this one failed. So, let ChatGPT do its agentic thing and solve the problem.

But I am curious, has anyone—let me add this as a question here. Insert one column to the left. Any synthetic data that you generated? If—has anyone generated synthetic data using LLMs in any shape or form so far? I'd love to hear your inputs and while... yeah, please share verbally, it's good enough.

**Suresh**: Yeah, Anand Suresh here.

**Anand**: Yes, Suresh.

**Suresh**: So the data that's synthetically I have generated is that based upon the use case I have written there, right? I have a couple of performance test data that I collect from actual physical devices. Right? You have a mobile device, you have the information of that mobile device holding the information of how much of network, how much of battery usage or CPU usage. That synthetic, that's the original data that I have that is written in log files. Right? So based on analyzing that log files, I generate an HTML report because the file that I use is most probably 1 GB. Right? Not everyone to read it. So I use AI to generate a synthetic HTML report to read out its understanding as a job role does, right? As a performance engineer does, prepare an HTML report out of that.

**Anand**: Got you. And why synthetic data though?

**Suresh**: Help me understand. Why is that needed is what you're asking, right?

**Anand**: Yeah, you have real data. Why synthetic data?

**Suresh**: Yeah. See, I have lines of—in that log file I have, as I mentioned, it's like 1 GB of file, have thousands of lines to analyze. Right? So either I need some level of profiler to understand it as a subject matter expert and prepare a report. Right? That's the use case. That's the, that is why I'm using that, using a synthetic generated report kind of thing there. You answer you right.

**Anand**: If the source is large, I would have taken a sample and run it. Why synthetic data?

**Suresh**: See, sample in the sense, even see, there are too many metrics that that file has, right? Identifying the pattern what exactly I want, right? Is the file has information saying that when the app launched, right? That, that line may be written in some 1000 line or 2000 line, right? I'll not be able to sample, understand where is that line captured that metrics. Out of multiple files that I have. So I need to start some mechanism that can help me analyze all the lines that are written there, pick up what exactly is the console output that I want and give me the measurement when that start and when that stopped.

**Anand**: What I'm taking away is that you, sampling may miss a few scenarios that you want to explicitly introduce.

**Suresh**: Yeah, that's happening, yeah.

**Anand**: I see, got you. And that is often a powerful way or powerful use of synthetic data. In fact, that's probably my most common use of synthetic data. I want to introduce all kinds of scenarios, some of which I know beforehand, some of which I don't, and create this. Anyone else created any synthetic data? And if so, please do fill it in, but please also share verbally.

Okay, comment from Anand Tiwari, "Synthetic data is artificial data generated from statistical models trained on real-world data, designed to mimic patterns and properties without any real individual personal information." And you just created one with Codex for e-commerce. Do share more Anand, maybe if you can unmute and explain.

**Anand Tiwari**: Am I audible now?

**Anand**: Yes, now you are.

**Anand Tiwari**: Audible right? Yeah. So the link you have shared to generate the data, right? So there, prompt is already there for creating e-comm. I took the prompt, given to Codex and asked it to create a Python file and generate, like based on my input, it will generate...

**Anand**: Understood. Nice, nice. Okay. I was curious about any prior synthetic data, but you're just saying now you manage to get that done. Wonderful.

**Anand Tiwari**: Yes.

**Anand**: Perfect. Let's see. I guess we now have this data set which I will share in the chat window, but the data is not found. Try again. And it's still not found. Download. Okay. I wasn't able to download it. Try again. And give me the link.

Hopefully that should do a better job. No. Didn't work. Give me this CSV please.

Usually these links last at least an hour, but sometimes there are problems. I wonder if the file name has an issue. Okay, it says it's created the CSV. Let's download. Okay, that worked. And to avoid the massive size of these, I will—okay, 1.3 MB. I'll zip it anyway and add it to the chat. It's about 250 kilobytes. Oh, that didn't quite work. Let me—interesting. Looks like I am not able to attach it in Teams. What is your preferred file sharing mechanism?

**Participant**: You can just add it to the Google Sheet, I think, as another one. I think the teams can download it from there easier.

**Anand**: Interesting. That is a good point. I'll add it to Google Drive. And I have the CSV. Compress as a zip file. Create this on Google Drive. And share it publicly. And I will put in the link in the chat. So you should be able to download this.

Okay, so now that we have a data set to start with—and my request is others, please, you don't have to use public data. I wanted public data so that we could collectively share in this session. I'd like you to work on your respective data sets. Ideally, something that you've picked and added in column F as the data set that you want to analyze.

So, we are now getting into the analysis stage. We've spent 40 minutes talking random stuff, but now's when the work begins, so to speak. So maybe we can start with Devbrat, you sharing your screen. I'll stop sharing mine.

**Devbrat**: Yeah.

**Anand**: Wonderful. And we'll rotate as we go along with anyone else who has public data. So, Suresh, you have some public data now?

**Suresh**: Yeah, I got some data here. Even I have shared that link, GitHub repo link there.

**Anand**: Oh, wonderful. And Vidul, were you able to get or generate any public data related to this or anything else?

**Vidul**: Yeah, yeah, I'm just in the process of it.

**Anand**: Wonderful. And Anand, you've in any case gotten or created public data. Were you able to download it?

**Anand Tiwari**: Yes, yes.

**Anand**: Wonderful.

**Anand Tiwari**: Yes, it's available.

**Anand**: So maybe we'll rotate between this group and anyone else who has public data that they want to share. But in the meantime, we'll wait for Devbrat to share screens and we will dive in a bit and explore what creative things we can do with the analysis.

Remember, the objective here is vibe analysis. So we don't want to worry too much about the code or the analysis. Ours is more an output focus and how we can get to good answers, both robust and interesting and useful.

**Devbrat**: I'll share my screen now Anand. Just a heads up, I am from a non-coding background, so I do use Cursor and VS, but not very familiar.

**Anand**: **You are the perfect candidate for vibe analysis.** No, with several, with no blinkers on. So, great. Now, as a starting point, please open the folder... there's an open folder, yeah, that has the data set.

**Devbrat**: Let me just maybe transfer this.

**Anand**: Actually, opening the downloads folder works fine too.

**Devbrat**: Okay.

**Anand**: And part of—one of the things that you want to do, general tip to everyone, is if you have multiple data sets in one folder, **create a separate folder, move just your data set in, and do the analysis.** LLMs, coding agents in particular, are as dangerous as you can imagine. So, A, you don't want data exfiltration. B, you don't want malicious code, or you want to kind of sandbox malicious code. And most of these coding agents, by default, restrict themselves to the folder that you are running in. So, sandbox by folder.

Yeah, please open the folder, Devbrat.

**Devbrat**: I've opened the folder. Do you want me to open the file as well?

**Anand**: No, not required. Why don't we now create a plan? What I find effective is keeping the plan part separate and the execution part separate. One shot works well in some cases, and we can trigger that. So actually, let's do both. Why don't you ask it to generate some insights, whatever you want? That's step one.

Okay. But don't press enter yet. Once you've typed in whatever prompt you want, then before pressing enter, I'll share a few ideas.

</transcript>

---

## Parallel agent chats save time and momentum

- Try **Agent Full Access** once or twice; it runs unattended and teaches tradeoffs.
- **Spin up parallel chats** so you’re not waiting on one task.
- Keep an eye on **safety and approvals** in longer runs.

<transcript>

**Anand**: Yeah. Great. Now, at the bottom, there is a dropdown. Could you select… okay, multiple dropdowns. Even below that, there's a tiny little thing. Yeah. Switch Mode.

Yeah. Now, normally you would have it in Agent, but in this particular case, there's no harm putting it in Agent Full Access. So that way you don't have to keep approving. Specifically, what that will… yeah, basically eliminates the need for multiple approvals. You have Python installed on your machine, I presume, right?

**Devbrat**: Yes, I do.

**Anand**: Perfect. The next thing that we want to do is have some of these run in parallel. And I'll share a second tip. But before that, just one thing for everyone to keep in mind, if you have not yet tried Agent Full Access, **try it once or twice. It is slightly dangerous, but you also need to know the benefits that you get when an agent can run autonomously.**

Again, from this point on for a while, I'm going to be sharing a bunch of ideas, suggestions, tips, etc. Good part is it's being recorded, but if you'd like me to repeat any of these or have any questions on anything, please put that in the chat window, and we'll take that as we come along. So for now, please click on Submit on this, Devbrat.

Now, second tip: **it is utterly painful and boring to wait for an agent to finish stuff.** So, I usually find it more entertaining for myself to do something else in parallel. So in this case, could you click on that new chat, Devbrat?

Yeah. And let's try something else. Now, there are two problems that we face when working with LLMs. A, they don't do what we ask them to do well. The converse of this problem is, **we don't ask them to do the stuff that they do well**. And a big part of the blinkers that we have is that we kind of know how to do stuff, we've been doing stuff so far, and we limit ourselves to that. Weekday-weekend analysis is a classic example. You have been doing this analysis, therefore that is what you want to do.

What if you didn't even know how to do this? And if you wanted to be a creative person. Here is a prompt that you can try and type out, Devbrat. **"What interesting, useful analysis can I run on this dataset?"**

Question mark, and run.

Now, what we're doing here is an exploration. We are asking it for suggestions on what analysis can be run. Roughly the equivalent of having it do exploratory data analysis, except that when people do exploratory data analysis, they do it from the perspective of trying to get an understanding of the data. Here, we are asking it to do an exploratory data analysis to help us surface insights, and maybe it will do a little bit of preliminary analysis and say, "here may be an interesting observation, here's another interesting observation."

In fact, we could do something even better. Could you create a new chat?

And ask it to **"find the most interesting, useful, and non-obvious insights from this data."**

Yeah, "find the most interesting, useful, and non-obvious." Obvious spelling. Very interesting spelling also, but that's okay.

Yeah, go ahead, it'll figure it out. Insights from this data. And explain it in simple, witty language. W-I-T-T-Y. Yeah, language for a senior exec.

And go ahead.

</transcript>

---

## Separate planning from execution to think deeper

- First ask: **“What interesting, useful analyses can we run?”**
- Then ask: **“Find non-obvious, executive-ready insights.”**
- **Planning + execution in one go** makes the plan **shallower**; split them for depth.

<transcript>

Now, let's talk about a few things here. In the earlier example, we're saying, "what can we find?" That is roughly the equivalent of a planning mode. You do the exploration and give me some ideas. Now here we are saying, "give me the ideas and give me the answer." Why would we not always do the latter? What I find is that the mental capacity of a single agentic loop execution is constrained. It doesn't go too far. So, **if you ask it to plan and execute, it allocates less thinking power to planning** and, compared to the full thinking power, maybe it does 50-50, 20-80, whatever. But the amount of thinking or planning is less than the whole. So, if I have a pure planning cycle, I usually find that it comes up with more insights that I could explore, out of which I can pick and choose and dive deeper.

Whereas this is a slightly different one. I am not interested in coming up with the most interesting analysis, I'm just interested in coming up with some interesting analysis. In that case, I switch over to this. But in any case, one of the principles to follow is, if you think you know what analysis to do, good, do it. But **remember that the AI can do other stuff that you haven't even thought of.**

Now, let's go back to the list of analyses or list of chats, Devbrat, and pick the first one. Maybe it's run. Okay, well, why don't you interpret this?

**Devbrat**: Right. It's very generous, should I show both Saturday, Sunday weekend? I think it is a strong, it is good analysis, especially that it has also considered that in Middle East, Friday might be a weekend. So it has given us that picture as well without us specifying it.

**Anand**: Well, kind of, the file name gave it away, but it's obviously smart enough to pick it up.

**Devbrat**: Yeah.

</transcript>

---

## Style prompts and simple hosting make stories shareable

- Ask for a **“beautiful visual data story”** in the **style of The New York Times**.
- Turn **reasoning effort to high** for better structure.
- **Preview locally** (`python -m http.server`) and **publish via GitHub Pages**.
- **Share the link on the [Google Sheet][sheet]**.

<transcript>

**Anand**: So which is great. Now, here's the problem. It takes us a minute to read through this and understand it. How about if we ask it to visualize it? I would say, **"Create a visual data story as a single-page web app that explains this insight."**

Now, we'll make a few small tweaks before we submit this. Instead of create a visual data story, let's make it **"create a beautiful visual data story."** Add the word beautiful before visual. And some of this matters because the aesthetics will make it far easier for the audience to understand it. And depending on the model, it has a pretty decent sense of aesthetics.

Next, let's make a model choice. Could you select the dropdown that chooses the models? Auto context is fine. But to the right, isn't there a little tiny little button to the right of that? No? Oh, that's okay, fine. Which… I think we have configured at GPT-5. Could you go to the settings in your… yeah, that one. Select the codex settings dropdown. Open the config.toml. And GPT-5 via light LLM with reasoning effort medium. Could you change the reasoning effort to high? And save it. Save and close.

And okay, the reason I'm saying high is, well, you can try it with medium and try it with high and see the difference. But what I find is that it tends to be a little more, obviously, thoughtful with high, and that can make a difference in terms of the aesthetics, especially keeping in mind that GPT-5 is not as aesthetically sound a model as let's say Sonnet 4.5.

The second thing that we can do is **style transfer**. Now, it's one thing to say create a beautiful visual data story. It's another thing to say create a beautiful visual story in the style of X, Y, and Z. Now, **one of the ways in which we can specify things is explicit**, which is, "I want you to create a header like this. I want you to create a banner like this. I want you to create a scrolly-telling style application, buttons in this form," etcetera, which is verbose. A more efficient way of providing instructions is saying, **"in the style of X."** You could say, "write code in the style of this particular developer," a famous developer. Create visual art in the style of this painter. Create data stories in the style of, say, the New York Times or the South China Morning Post or whatever. In other words, having a mental model of different style catalogs, styles of development, styles of analysis, styles of visualization, styles of anything in your line of work, can be very powerful. Knowing what those styles are becomes important. For now, therefore, why don't we pick the New York Times as the gold standard for visual data stories and add the phrase, "in the style of the New York Times"?

Perfect. Now go ahead and submit.

Right. And could you go back to the chat? And after the next two will, any one of these complete? Can you find the most… yeah, most interesting… Yeah, okay. Let's take a quick look.

Any of these sound promising?

**Devbrat**: Sales and margin basics.

**Anand**: And others, please feel free to pitch in as well, if you spot something that looks interesting.

**Devbrat**: Pareto is interesting, I guess. The top classes that are contributing to 80% of sales. Something which we did not think of.

**Anand**: Any others?

**Suresh**: Devbrat, do you mind closing the welcome window and making the font a bit bigger, please?

**Devbrat**: Yeah.

**Suresh**: Thanks. Thank you.

**Anand**: And control… yeah, perfect. One more control plus might make it easier. Control plus is the keyboard shortcut for increasing font size.

**Devbrat**: Control plus.

**Anand**: Yeah.

You know, one of the analysis patterns that I find almost invariably interesting is **anomaly detection**. And it's saying are there any outlier days or category spikes. The reason is it either flags errors in data or unusual business patterns. Both are almost guaranteed wins.

Cannibalization signals. Okay, that is also another… I find that a correlation matrix is another one of those ultra-powerful analysis techniques. Create a bunch of categories, find out what is the correlation in sales between category A versus category B for every pair of categories, and then see if there are any insights that come out of those. Now obviously, this is dummy data, so the actual insight will not be as powerful. But the important thing here is, given this kind of data, the… what an LLM is able to share in terms of the kinds of analysis we can do is also something that expands our horizons. And **the biggest barrier that I've seen to this is our own skill**. The more skilled a person is in doing a certain piece of, in doing analysis, the more blind they are to analysis outside of their experience. It's not a bad thing because they probably know 90% of what needs to be done. That 10% or what we believe is 10%, could actually be much larger with LLMs.

But what this does not tell us is, is doing this analysis actually interesting or useful? So let's take a look at the last piece of analysis if Devbrat, you could go back to the list and pick the, yeah, that one. And yeah, let's start, stay with the executive summary. I'll read it out. Two big sale waves crush price realization. January and July run a 34% markdown versus the 18 to 20% of the rest of the year, dragging average sale price from 60 to 47. Okay. If I was an exec, that would be pretty impactful.

And Mix is doing the heavy lifting. I'm guessing that's a category. Sneakers, bags, and watches punch above their weight, whereas low average sales price, tees, t-shirts maybe, soak up about 30% of the units and only 9% of the sales, which is the Pareto analysis that we were talking about. Again, useful, but may not be surprising. Returns cluster in high-ticket accessories and modest wear. Okay, and Qatar and Oman are the hotspots for costly returns. That would be ultra-valuable information if it was not already known where are my returns killing me. UAE is promotion-heavy whereas Bahrain is steady on pricing. Again, fairly useful. Now here we have a set of answers, which it has picked from a whole series of different kinds of analysis after spending a good six minutes on this.

Here, we have two advantages and a disadvantage. One, we get answers straight. This is pure Vibe analysis. And it allows us the ability to rerun this analysis later if we ask it to save the code and work with it, which we will do in a few minutes. The disadvantage is that we have not really explored this, and therefore may need to do some validation or perhaps re-ideation.

But let us do two things now. Let's ask it to create a script that will allow us to rerun this. And then later on, offline, Devbrat, you can have it create a visual data story as well. So, could you begin by putting in this prompt which is, **"Create an analysis.py file that will recreate this analysis and generate an XLSX file with required data."** And submit.

And this is another pattern of analysis that I find, which is, earlier we would have written the code, run it, and have it do the analysis. Now we are having it do the analysis, let it write out the code however it wants, and once we are happy with the analysis, then ask for the code. **The code is the byproduct, not the primary product.**

Now, let's go back to the prompt where you asked for the data story. And yeah, the high one, correct. We have created a data story. Now, could you preview this? Do you know how to run a web app locally?

**Devbrat**: Not on…

**Anand**: Start the terminal, please.

**Devbrat**: Okay. Assuming that I should be able to…

**Anand**: Yes, but the three dots, next to the run. Yeah, and then click on Terminal and New Terminal. And type Python space -m space http.server. Yeah, enter.

Lovely. Now on your browser, open localhost:8000.

**Devbrat**: Localhost…

**Anand**: Yeah, one word. Localhost colon. Yeah, instead of 3000, make it 8000. But you already have 8000 somewhere. Yeah, 8000, great. Enter.

Cool. We have a data story, kind of in the style of New York Times. Scroll down, please. Oh, interesting. Okay. Wonderful.

Now, why don't we publish this on GitHub? Have you pushed to GitHub so far?

**Devbrat**: No, I don't think so. I have some private repositories.

**Anand**: Got it. Why don't you go to your GitHub repo? It'll be the easiest way of doing it for now. And then, Suresh, we'll switch over to your laptop. Uh, yeah, go to home and the new repository that you might have just created. If you haven't, then click on new. Yeah. And put in something. Yeah, and scroll down, create repository.

And there is an "upload an existing file" tiny little link in the blue section.

**Devbrat**: Okay, yeah, got it.

**Anand**: Click on that. And choose the three files from your folder. It had created in that folder three new files. If you look at it, you'll kind of be able to guess which ones. Not the Python file, yeah, script, style, and index.html.

**Devbrat**: Alright.

**Anand**: Open, great. And go to the bottom and commit or submit or whatever. And next, in the tabs, there is a settings tab on the right side.

**Devbrat**: Yeah.

**Anand**: On the left side, you'll see Pages towards the bottom.

**Devbrat**: Yeah.

**Anand**: Select, in the branch dropdown none, change that to main and click on save. Now it's starting to publish. And click on… to see the progress and where it is, click on the Actions tab. And give it about 30 seconds. You can just click on it to see what it's doing. All we are doing is taking a bunch of files, including any web story, putting it on GitHub, it will eventually publish it. And yeah, it's now… build is done, now it's deploying to GitHub Pages. Once it's deployed, we will know the link. We know the link, but it will show the link, and then we can click on it. Yeah, please click on this. And congratulations, you have **Vibe analyzed, Vibe coded, Vibe deployed**, so to speak. And it's live. So please copy this, put it onto the Google Sheet as one, and create a bunch more with public data just to get a feel for it, right?

**Devbrat**: Yeah. Sure.

**Anand**: Suresh, let's take yours, and we'll go to the next stage beyond this.

**Suresh**: Yeah. Let me share. I have Codium. Okay, hold on. My screen is frozen. Okay, great. Yeah.

**Anand**: Now this works perfectly. Cool. And you've already created some stuff. Let's take a look.

**Suresh**: Yeah, as I've told earlier, right? I picked up some dataset from some mobile app. This is all the data that it has.

**Anand**: Okay, but anything confidential that you shouldn't be sharing?

**Suresh**: Nothing, nothing, nothing. It's some vibed app that I have. So to start, my prompt says something like that.

**Anand**: Hold on. I would love for you to copy this prompt and put it into the Google Sheet for others to also be able to take a look at it.

**Suresh**: Already.

**Anand**: Oh, you have? Okay, wonderful.

**Suresh**: That's done.

**Anand**: Okay, yeah, fine. Cool.

**Suresh**: Now let's spend a minute on this. "Start analyzing the data in this folder across files by doing a systematic..." Okay, "examining the file like a performance test engineer." Okay, interesting. "And generate an HTML report." Sure, go ahead, please. We'll come back to the prompt.

Yeah, that's the prompt. I said it not to hallucinate, not to do all the false stuff that, right, stick to the data. Because there are too many files and much more to analyze. Yeah, it has analyzed each and every file, generated that performance report. And it did not generate the AppDynamics report earlier. Okay. Looks, yeah, I re-prompted it to fix that thing. Yeah. It has somehow generated it. So the report looks something like this now.

**Anand**: Nice. Okay. And this is more in the style of a dashboard.

**Suresh**: An APM tool report. Yeah.

**Anand**: Okay, I see what you're saying. Okay, fine.

**Suresh**: Because I've prompted out to give me an observatory report. So in the similar state, it has this observatory stuff there. Yeah. It's still not working. The nav bars is not working. I have to prompt it out to fix this. Yeah.

**Anand**: Got you, fair enough. How are you thinking of prompting? Continuing the conversation, asking it to fix it, or new conversation, asking it to fix it?

**Suresh**: No, continuing the conversation, right? Until and unless I have filled out all the window, it will ask for a new window, right? That's how I usually practice. But at the last, I re-prompt it to give me, rather than doing all the multiple prompts, summarize to one prompt. So to reduce my workload there, right? I do that at the last. Concluding everything there, to give me the exact prompt, rather than doing multiple prompts.

**Anand**: Got you. In other words, and tell me if I'm paraphrasing correctly, you're saying given this conversation, give me one prompt that will do the equivalent of all of what we have done so far.

**Suresh**: Yeah, yeah, yeah.

**Anand**: Which is a powerful way of recreating the analysis and learning from failure.

</transcript>

---

## Start fresh chats when context drifts or errors compound

- Long threads **accumulate bad assumptions** (“context rot”).
- If a fix doesn’t land in one pass, **start a clean chat**.
- Keep a short **summary prompt** to re-seed new runs.

<transcript>

**Anand**: What I've usually seen is that **there is a risk of context rot that increases with errors**. It's taking three or four wrong directions, and we don't want it to go in those wrong directions. So we start again, which is great. But by continuing the conversation, that context, even if it is only about 20% of the total context window, so it hasn't really filled it, can still reduce the overall quality a fair bit. So, if after one correction attempt, I don't get to where we want, I find it more profitable, at least these days, to switch to a new chat and try either with the summarized or paraphrased prompt as you mentioned, or a new prompt. However, that may well change with models in the future, not sure.

**Suresh**: Yeah.

**Anand**: Let's go back to the editor, please. And I saw that you are about to create the analysis script that will generate...

**Suresh**: Yeah.

**Anand**: Yeah. No, please go ahead. Let that run in parallel. But there's something else that we can probably try around this. Now, one thing that I find hard to do is reviews. And there are several things that take up my time from a review perspective. One way of reducing the load is to have the LLM do a part of the review. Let's start with one aspect. So far, the output... okay, when creating the visualization, did it generate a set of output data files as partial analysis?

**Suresh**: I did not ask it to generate an MD file or something like that because it's already creating a HTML report. I don't want to create an additional MD file. Right? So I did not ask it to print that, but it's still writing out the analysis, a short summary of what it has done. Right, that's there.

**Anand**: That's okay. The visualization, is it hard-coding the numbers in the JavaScript or HTML, or is it picking it up from a TSV file or a JSON file?

**Suresh**: No, it's picking it from the TSV file. As you said, right? Yeah, the values are not accurate every time. Right? So I have to go back, ask, prompt it out how this value is generated. Right? Or use another model or another IDE, parallely do this in two IDEs, analyze where is where is the difference, right? And do some stuff like that to verify because these are numbers, right? Numbers may not be accurate. I have seen sometimes that if it's 1k, it is showing 2k also. Perfect. Hard to believe why this number is coming, right? So that varying models, multiple prompts in the same model, or picking out three or four models at a time across multiple IDEs, yeah. That I usually practice.

**Anand**: Let's find out how we can systematically identify and reduce the possibilities. Could you open a new chat and try the following?

**Suresh**: Oh, sorry, you want a new session?

**Anand**: Just a new, yeah, yeah, just a new session. Right.

**Suresh**: Maybe this will hold up. Oh, not…

**Anand**: Now it seems to be going in parallel, which is great. Not what must… Oh, is… no no no, it is working. If you click… no no, click on the earlier one, it said working at the bottom. Click on the earlier session. Yeah, at the bottom. Do take some time. Oh, it said working a few seconds ago.

**Suresh**: Yeah, yeah, that's… Let me go back history. Yeah. Oh. Sorry. Wrong. All right. This is just some data, right? Yeah. Fine.

</transcript>

---

## Many independent reviewers catch errors agents often miss

- Ask a model: **“Find numerical/statistical errors in this analysis.”**
- It will flag issues like **division by zero** or **impossible latencies**.
- Use **multiple models** as a **sieve**; each catches different flaws.

<transcript>

**Anand**: Let's rebuild. Now, let's ask it the following: **"Find errors in the analysis that generated the data visualization."**

One small correction, "that generated D". And no question mark. Instead, you could add a full stop please. **"Focus on numerical errors."** Numerical and statistical errors.

Right, go ahead. Uh, no, wait, let's… okay, let it run, let it run. No harm. No, no, no, let it go ahead. What I would have added, and this is something that we can explore going forward is, reading the output from here, from this window, has two problems. One, the format is somewhat constrained, copy-pasting is a little difficult, that sort of a thing. I usually have it generate any output that I want to substantially review into a markdown file. You can always add that later and say, "save this into errors.md" and it will do the job. But doing it upfront allows me to review it as a markdown file and save it and so on. This is behind the scenes using codex or not?

**Suresh**: This is, I think this is, this model is using, what am I using? I think it's using Claude or something. Backend, this ID is wrapped under Claude only.

**Anand**: Okay, fine. I what I will do is show how you can, in case this sort of a thing happens, you how you can go back to the logs, and the logs analysis can be pretty powerful. But why don't we scroll up, maybe increase the font size for others to read, and we'll see some of the errors.

**Suresh**: Control plus. Yeah.

**Anand**: Let's scroll up a bit.

**Suresh**: Yeah, for the third prompt, it has analyzed that analysis file, Python file that we have tried just…

**Anand**: Good. Let's jump straight to the critical errors below.

**Suresh**: Yeah. Go ahead. Ah, critical… memory growth calculation error.

**Suresh**: Let's skip the recording that I liked and the analysis, the analysis. And generally the data visualization focused on the numerical. Okay.

**Anand**: Now the first one it's saying is, in case the denominator is zero, there'll be a...

**Suresh**: Inaudible. As division by zero is correct, wrong. Problem, if finished, number is zero, it's called division by zero. This condition should be showing correct calculation. What is wrong calculation as wrong. Okay, but how do I analyze it?

**Anand**: That and the second one are somewhat smallish issues. Take a look at the third one.

**Suresh**: Frame latency values not, not on, rendering data.

**Anand**: It's saying that there is a frame that took 44 minutes, which is crazy.

**Suresh**: Middle seconds. The suggested data is either two timestamps instead of frame rates. Inaudible, microsecond data. This file has some. Okay.

**Anand**: Which is an interesting observation. And this is the sort of thing that will lead us deeper to figuring out, forget whether the analysis is right or wrong, whether the data itself has issues.

**Suresh**: Yeah.

**Anand**: And item number five is also seems interesting. Could you scroll down? So it's saying, and this is a subtle one, it's saying that this is the peak and average, but we're not looking at the distribution around it. Arguably not an error of commission, more an error of omission. We have not considered something. A different kind of issue that we're looking at.

What I find is if you have, well, you know the saying, right? **Many eyes make all bugs shallow. If you have not one reviewer, but a dozen reviewers, and synthesize across those, invariably it will find stuff that is wrong.** Many of which we may want to say, "Yeah, I will excuse it." But the odds of something that is incorrect going through become less and less. **It's like a sieve. And we can have multiple sieves as filters, run potentially by different LLMs. And each has its own flavor of doing the analysis.**

Now, let's try one other thing. And then we shall move on. Sorry, I was wondering who had the third dataset. Sorry, somebody else had an… Okay, Vidul, you had another dataset, right? So, before we move on to Vidul in a few minutes, Suresh, how might we add test cases to this? Any thoughts?

**Suresh**: Test cases. See, the data that you're looking at, right? If you look at the test case, if you... not line of thought. Let me see.

**Anand**: And others, please feel free to pitch in if you have any thoughts as well. How might we test or add test cases in something like this?

**Suresh**: This is based upon, see, based upon the problem statement, we should generate test cases.

**Anand**: Correct.

**Suresh**: The ideal principle. Yes. If you say energy score statistic error is is something that I have to look at. Yeah. Let me vibe it. The list of…

**Anand**: Cool. I'll just read that out. What are the list of test cases that the performance QA team has to test to debug and do a deep down QA for the energy statistical score issue? Which is great. Now, what this was doing was, firstly, a great thing to ask the LLM the question. And was using a specific issue. You obviously have the option of going broader in two ways. One, doing the same thing for each of the issues, and you could even upfront ask, "How do I go about testing these?" Or potentially even a broader question, which is, I have this codebase, this is the problem that I'm trying to tackle. How might I go about testing it? Why don't you, in while the session is going on, try that out, while in the meantime, Vidul let's...

**Suresh**: I don't have a codebase. This is an external app. I don't have the codebase to identify why this energy, if you say one problem statement, energy score statistics error, right? I don't have the codebase to analyze what method or function is using this energy score. This is a third-party, some random dataset I have pulled in. Right. So I don't have the master code to analyze, to deep down, right?

**Anand**: The analysis.py script that it generated is our code, right?

**Suresh**: Sorry, can you come back?

**Anand**: analysis.py on the left is the code.

**Suresh**: Okay.

**Anand**: We've just generated the code already. Why don't you click on it? On analysis.py. Here it is.

**Suresh**: Analyze data from CSV files and generate a comprehensive Excel report. It has analyzed the data, the original data, and created this comprehensive report. Right. That's what this Py code has. But it doesn't have, it doesn't have the root cause of this energy score statistics error.

**Anand**: Maybe, maybe not. I see your point because that is coming from the underlying… Okay, wait. Let's take a look at the energy statistical score issue. Where exactly did we see this?

**Suresh**: Yeah. So this is an issue. This is a battery usage issue of an app, saying that it has touched 99.67% of utility of peak energy score.

**Anand**: Could you select that?

**Suresh**: This one.

**Anand**: Yeah. Now, it's not saying 99. something percent. It is saying an absolute value of 999.67.

**Suresh**: This is something like this. Battery related kuch graph file hai. Energy consumption analysis. Okay. With respect to timestamp when I'm using that app, there's a touch point at this time period that has a maximum utility of 99.67. Out of all the allocated battery, it has touched 90, if say at the, the battery of that phone is sitting on 80%, at that point, I have used 99.67 utility there, out of that is allocated. Got you. That's one hotspot that it is giving it to me. So now if I have to test it, I have test cases that. But answering back to your query, if I want to deep dive and analyze what's causing this, right?

**Anand**: I see what you're saying. **What we want to do is test the analysis process.**

**Suresh**: Okay. Okay.

**Anand**: Which is what analyze.py does and it is entirely possible that this statistical error is an analysis issue, unlikely.

**Suresh**: Okay. Okay. Not a real issue. Okay.

**Anand**: And in which case, how would we go about writing test cases for our analysis process? We've asked an LLM, "Do the analysis." It has done the analysis. We asked it, "What mistakes did you make?" It told us. Now, we don't want to ask it every time what mistake you made. What we are now abstracting it out to is, I did vibe analysis, I got a result. From the analysis, I'm converting it into repeatable code. But the testing that I did, I want to convert that to repeatable testing as well. That is the direction that we are going in. Okay. So put another way, how can we add test cases to analysis.py?

Do give it a shot. In the meantime, Vidul, could you share your screen? We'll try a few other techniques now. But in the meantime, my request to others is, **please use whatever public data you have. Create a data story out of that. And put it onto GitHub and share the link** on the Google Sheet. Let me pause here for a minute. Does anyone have any problem with this? Okay, let's do one thing.

Could I request all of you to fill in column H? I'll share my screen first. And Suresh, maybe you could stop sharing your... Okay, you've stopped sharing your screen, perhaps. I think my screen is visible. Could someone confirm?

**Vidul**: Yes.

**Anand**: Okay, thanks. So, please fill in column H, which takes the question, what data set are you playing around with? Any public data set that you have. Please create a data story. It doesn't take more than 10 minutes for the application to run. And you can put in any prompt that you want. If you've started, please put in the data set. If you've completed even better, fill in the GitHub repo link. Since most of you have GitHub repos, and for those of you who don't, just create a repo the way we just saw Debabrata create it. And if anyone has any issues, please let me know. What I'm hoping is as at least one part of the outcome of this workshop is **all of you have one published data story with public data.** Okay, Vidul, I'll stop sharing my screen. Maybe you could share yours.

**Vidul**: Yeah. Okay, it's coming up for me. Should be able to see it in a few seconds. Yeah, I can see your screen. Great. Yeah, so I have created this mock data using like two, three rows. And so basically what we do is we have an N8N workflow wherein we upload a CSV file and we have particular short prompts. So suppose for a product you want the model to, like to pose in a certain way, we give each short prompts, which you can see here, short one, short two. So we have around 10 short prompts. And accordingly, we have input images also. So right now we have mannequin images and overlay images of the product, which we give so that Nano Banana can work on the prompt and give me the output image.

Now there are many issues which we see wherein we see that okay, maybe due to rate limiting or maybe due to latency issues, the, like the model does not give us the correct amount of output images or sometimes it also does not generate the correct output based on the prompts. So I've just collated everything inside this data as per like what QC we do and how do we pass or fail the product and what do we go about for each product. And we also have the time, how much time does it take and how much time does it take for each person to QC and and so on. So yeah.

**Anand**: Great. Now are you using Codex or something else?

**Vidul**: Yeah, Codex. So I downloaded VS Code and I have Codex plugin.

**Anand**: Perfect. There seems to be a bit of an echo. Maybe it's some other... Okay, yeah, the echo's gone. Perfect. Let's do this now. Rather than asking it to, or okay, why don't you go ahead and type out a prompt as to what analysis you want to do? Okay. Don't press enter at the end. Yes. I was just trying to...

**Anand**: Yes, please. No, if it's, you've opened the same folder, right?

**Vidul**: Yeah, I have opened the same folder. Do you not want me to add it?

**Anand**: Auto context should... Okay, no, no, go ahead. Nothing, no harm. Please add.

**Vidul**: So what I did was I added, like I have two files. I'll just delete one maybe.

**Anand**: Ah, yeah, okay, I understood. Yes. All right, perfect. But still, no harm in explicitly providing it a context. So please feel free. But after you do that, yeah, wait, you go ahead. And then I'll guide you on the next step. No, no, don't, don't, don't submit. And if you have submitted, stop it. Yeah, copy this prompt.

**Vidul**: Okay.

**Anand**: We'll try a slightly different technique, **meta-prompting**. Copy it. Now open a new chat, new session, whatever. Right. Paste the same thing, but don't submit. Now, here's the thing. We are not prompting experts. Even if we are, the next model that comes up ends up changing the rules of the prompting game. So, let's ask it how we can improve our prompting. Part of that is largely the planning step. So, in the bottom left, instead of agent, could you select chat? This, yeah, the chat option makes sure that it's not going to write the code. Now, what I'd like you to do is in this prompt, press shift enter a couple of times to add a few new lines and say, suggest a prompt, suggest an improved prompt for this. Suggest an improved prompt for this. I'm giving you very concise versions just to make it easier to type. Normally, I would have said this out louder. Now submit.

So, you have explained your intent. It's like, here's my prompt. But in addition, we're just adding one more thing, which is roughly the equivalent of, yeah, give me a better prompt. Now, why does this help? Invariably, our prompts are, they they include contradictions, ambiguities, and omissions. It has the data, it understands English pretty well, it's pretty logical. Have it do one round of clarification so that we give it better instructions. Let's scroll up. Just glance through it.

**Vidul**: I mean, is it like it is explaining what to do instead of doing it?

**Anand**: Yeah. And what I find powerful here, for instance, is, let's read it backwards. It's explicitly asking for **actionable recommendations**. That is useful. That is exactly what we wanted, even though we didn't specify that right up front. It's also asking for the top and bottom performers and significant gaps. Again, something that we didn't explicitly ask for. But without a doubt, a useful thing to put in. Metrics it's captured properly. So this is effectively only a small improvement to the prompt, but in our original prompt, if there are any mistakes, the amount of comprehension that it has to do to circumvent that, overcome that, etc., we do in in one conversation. And then take that clean prompt, put it into a new conversation to avoid any kind of context rot or confusion. Yeah, copy it. New chat now, not the same chat. The whole point is to avoid polluting the conversation. Now, don't submit it yet. Just paste. Now, in that drop-down where it says chat, you can select execute, or sorry, agent. And now go ahead and submit.

This, as a meta-prompting approach, or you could also call this planning, but planning is slightly different. Planning is where you actually ask it to do, ask it how it's going to execute it step by step and correct it if required. That has value, but for vibe analysis, I find meta-prompting more powerful. And let it run. Oh, yeah, okay, you're going to have to, sorry, can you stop this? And new chat. Paste the same thing. Except, instead of agent, choose agent full access. It's a safe enough operation for this and submit. Great.

Next thing that I want to cover is, over time, you will be using AI coding agents for code analysis, whatever, a fair bit, and these things will pile up. When they pile up, you will want to go back to one of your previous conversations, see what we learned, that sort of a thing.

</transcript>

---

## Meta-analysis of logs improves prompts, tools, results

- Your agents write **JSONL logs**; convert them to **readable markdown**.
- Review patterns: **what you ask**, **what it does well**, **where it stalls**.
- From this, **upgrade prompts, libraries, and workflows** with evidence.

<transcript>

The good part is all of this is logged. The trouble is the logs are in JSONL format, not very easy to review. But let's take a look. So, Vidul, could you go to the settings icon and yeah, select Codex settings, open config.toml. This is the folder where the sessions are also stored. Could you press Control O to open files in this folder? Control O, or command O if you're on... Okay, double-click sessions. Go to current date. 10, yeah. 16, yeah. These are all the sessions on Codex that have been run so far. Now, with the date, we kind of know where things are. But maybe just, yeah, pick any one of these. Yeah, open it. And this is one of the sessions that has had 11 messages exchanged or tools run or whatever. Trouble is, this is hard to read. You could write a parser. I vibe-coded a parser for this this morning. So, let me share a link with you, which is tools and Codex log. I will put this in the chat window. What you can do is open this in the browser.

On the Teams chat, you would have received the link. Yeah. And drag or yeah, click on that upload, any one of those log files. User, Vidul, Users, Vidul. And dot codex sessions. Go to the date. And I think yeah, whichever one you picked last time, and click on open. And this is roughly the, if you scroll down, yeah, gives you the markdown conversation, which makes it easy to read. You can download it as markdown and review this.

Now, why did I even bother doing this? Partly because **meta-analysis is pretty powerful**. You use a coding tool like Codex or anything else for that matter, dozens of times a day. Over time, logs build up. And then you could start asking it the question, what analysis am I doing well? What analysis am I not doing well? Are there blind spots in the way I'm asking questions? Are there blind spots in the way the tool is executing? Supposing I downloaded some other tool. If I gave it access to, let's say, scikit-learn, would it be able to run... or even forget access, if I give it instructions to use scikit-learn, would it do better? Should I delegate some of the analysis to LLMs? Search online and find more powerful techniques of analysis than what I'm using. All of these start becoming possible. This is another technique in the AI analysis space, which is **meta-analysis: the analysis of your analysis.**

**Vidul**: Sorry to interrupt, but like is this only useful for Codex or because I majorly use Cursor.

**Anand**: I don't use Cursor, I don't know where the logs are. The technique is the same. And all you need to do is take the Cursor logs, put it into ChatGPT, ask it to write a converter. And I say ChatGPT, but you know, Jules, Claude, whatever you want. Or write it locally or Cursor for that matter. And because you're using Codex and I happen to have a Codex converter, we are talking about it that way. That's all.

**Vidul**: Understood.

**Anand**: Yeah. And okay, it's okay, this is still running. But good. We just covered meta-prompting, and we just covered meta-analysis as part of the portfolio of techniques. I know we have only about 14 minutes left. So I'd like to use this time, at least to begin with, for any questions that you may have. Floor open. And Vidul, please feel free to stop sharing. And once you get the results, if there's any insight, please do share. Suresh, if you found any insights about, based on the test, please do share both on the chat. But I'd like to open the floor to the others whom, who haven't had an opportunity to speak. From what you've been playing around with today or earlier, any questions?

**Deepesh**: Deepesh here. I'm talking from the Harmony room.

**Anand**: Sorry, I didn't catch your name.

**Deepesh**: Deepesh.

**Anand**: Deepesh, okay. Hi, Deepesh.

</transcript>

---

## Shape questions and add checks to reduce risk

- **Ask safer questions** (recommendations with clear tradeoffs) when accuracy is uncertain.
- Request **code + checksums/citations** so answers are **verifiable**.
- Do **post-validation**: run error-finders and **cross-model reviews** before shipping.

<transcript>

**Deepesh**: Yeah. So I'm, yeah, hi. I'm going back to one of the questions that you started putting in in the Google Sheet itself. **Do you really trust the outcome and are willing to share it directly?** So I did some analysis again, largely on sales and GRN. Is there any quicker way of, let's say, validating the outcomes before presenting to the leadership?

**Anand**: Here's what I do. And firstly, to your question, where do I stand on this? My answer is somewhat often, borderline positive. Here's my risk mitigation strategy.

Number one, **when asking the question, ask for a question that cannot possibly go wrong**. What I mean is, LLMs are great at giving general business gyan. Now, quite often, the data doesn't matter. If you could give good general business gyan, people will find it useful, people will take it, people will accept it. So I focus on the recommendation more than the validation in terms of what to present. Which is bypassing the problem, but it still has value. And there are many other ways of error-proofing the question itself, which we can probably get into later. But that's technique number one.

Technique number two is **framing the question in a way that it is less likely to go wrong**. For example, saying, "Write the code to do this." When it writes the code, it's less likely to go wrong. "Add citations in the data." So if I'm saying, "Give me a summary," I'll say, "Break it down into the categories along with the totals. Verify as you go along. Create a checksum list." All of these are ways by which you get the LLM, as it is doing work, to make fewer errors. Now, how do we discover these techniques? Meta-prompting. I would take my prompt, give it to an LLM, and say, "Now, modify it, adding no more than another 100 words, to make sure that the LLM, as it goes along, does whatever it takes to make fewer errors."

Approach number three, **post-validation**, which we saw when playing around with, possibly Suresh's analysis. Ask it, "Where did you go wrong?" Ask multiple models, "Where did you go wrong?" And so on. Human review, of course, is always there. What we want to do is minimize the human review in the first place, which is why these three. So, avoid framing a question that can be wrong. Have the LLM answer in a way that is less likely to be wrong. Figure out what mistakes the LLM made and feed it back. These are my top three approaches.

**Deepesh**: Perfect.

</transcript>

---

## Turn one-off work into a repeatable, testable script

- After a good run, ask for **`analysis.py`** that reproduces the outputs.
- **Schedule the script** for weekly refreshes; execs see **consistent views**.
- Add **unit checks** (totals, ranges, duplicates) so **regressions fail fast**.
- **Prompts are the source**; commit them alongside code.

<transcript>

**Suresh**: Anand, help me understand why we are doing an analysis.py. I did that on a blank shot, but I'm not, there's some output that is coming out of it, but why are we doing an analysis.py?

**Anand**: Great question, Suresh. So, let's say we've done an analysis. It took a certain amount of time and it came up with a result. We created a data story out of it, we created a dashboard out of it, and we show it to an exec. And he says, "Fantastic. Now let's do this every week." Next week, what will you do? If you ask the same, provided the same prompt, it'll give you a different program. And the exec will say, "Wait, hold on. Last week you showed something else. I liked that. This is different. Whether I like it or not, doesn't matter, it is different." Problem number one.

Problem number two, the numbers may actually be different. So the exec is going to say, "No, this is wrong in the first place. Last week you showed me a different number." Third, if we want to verify if the analysis was done correctly, how will we do it? We could ask the LLM, "Did you get it right?" But the whole problem is I don't trust the LLM.

analysis.py solves all of these problems. What it does is takes what the LLM did in that conversation, puts it in the form of an application, which is repeatable. So next week, I will rerun analysis.py. Exec sees the same output. I will then ask this LLM and another LLM and yet another LLM to review analysis.py in the context of this data and find errors. It'll say, "Oh, wait, here you forgot a division by zero. Here you are using the sample standard deviation. You should be using the population standard deviation," or more likely the other way around. "This particular correlation formula applies only for percentages. There is a different correlation formula that you should apply for large numbers." Those sorts of things become possible. In short, **what a script, extracting a script out of a Vibe analysis session does, is makes the process repeatable and verifiable.**

**Suresh**: Understood, yeah.

**Anand**: Cool. Questions?

**Suresh**: The prompt of that, whatever Anand (Tewari) has generated, is not rightly added. Anand, can you add that appropriate in the Excel? I think you have copied mine and added it here.

**Anand**: Sorry, I may have added that by mistake. So yeah, Anand, if you could please replace it with your, with the prompt that you used. Thanks. Anand, your hand is raised. Please.

**Anand Tewari**: Yeah, is, I'm audible?

**Anand**: Yes.

**Anand Tewari**: Yes. So, prompt is there is no sure-shot formula of prompt. While analysis, we need to identify what we are looking for and based on that we can change our plan and we can regenerate. So if I will share my screen, how I have did this. So this is totally connected to GitHub. Since I am from the tech background, a lot of things I already know. So it's very easy for me to follow. If I will do anything, it will directly publish to the GitHub. So as you can see here, I have given, "Please give it mobile friendly and chart and create superb," the current chart actually when it has made, it was super big. So make it looking nice. Lots of insight in one view because we need to see the data, right? So likewise I change my strategy. Before that, "Okay, go ahead and publish to my GitHub." It has taken the care because these these are manual things we can automate in one go. So whenever I'm doing any change, like I ask one question like, "Is it possible to get the customer churn rate from this data?" So it has did the analysis and it has said, "Okay, fine. So update my chart." So once I did this, it will update the dashboard and it will publish to GitHub in the live. So I don't have to do any manual activity over here.

**Anand**: Agreed. Good point. One of the things you could do is by the way use the GH CLI, which it understands natively, and you may not need to give it the commands. Second, there is a plugin, git-doc, which I find useful for live publishing. Just create a separate throwaway branch. As it saves, it can keep committing and pushing. But I think more importantly, you may want to consider an **agents.md**. agents.md is a file that you can keep, preferably in your repository, or in your root folder, which has common instructions that you want to provide without having to type it every time.

**Anand Tewari**: It's super cool.

**Anand**: Once you find that you are doing certain kinds of prompts regularly, you can just put that in your agents.md. To give you a sense of what my agents.md looks like, let me share my screen and put that in here and we will end in a few minutes, but AI code rules, one second. Yeah, this is my somewhat longish agents.md where I ask it to primarily write readable code, explaining how to write readable code, short code, don't change too much, always test. And this may be one of the most important rules in my agents.md: always write test cases, almost always write test cases. How to code, what libraries I prefer, what JavaScript libraries to use, how to lint, all of these things, which means...

**Anand Tewari**: It's very nice. But over the time it will get obsolete, right? Because we are evolving so faster. There is something called context seven, if you add that context seven, so it will take the latest documentation by itself. So we don't have to write anything in that.

**Anand**: And what I prefer doing is telling in my agents.md that it should use context seven for any library.

**Anand Tewari**: Amazing, great.

**Anand**: Which is a meta thing. The, what we are learning about this, specifically around what you said, which is that it's changing so much, is that the agents.md, if we have it as a single global, it changes so often. Therefore, pegging it to a repo helps. Also... Sorry, somebody was saying something? Okay, no. Also, you will want to commit your prompts. **Code is increasingly a byproduct. The prompts are the real source.** This is kind of like if you went back 20 years and found somebody creating, writing Java code and committing their jar files, not the .java files, that's crazy. Same way today, we are writing prompts. The code is a byproduct. Commit the prompts.

With that, I know we are over time. I have one last request. On the Google Sheet, please fill out the last column. We've gone through the session. Now, based on this, you've probably seen more risks, you've probably seen less risks, you have an additional sense of how to deal with issues, how to create better output, what additional complexities may arise. Now, what is your opinion? Can LLMs deliver exec reporting? Can they not? Please just fill out this column exactly the same input that you had provided earlier. If you want to go up, go down, whatever it is, please do fill this in.

And while you're filling it in, do, let me just share one general gyan. **90% of what I said is going to be outdated**. The question is, is it one day, one week, one month, max one year. And new stuff is going to be coming in. Even apart from that, I've probably only covered about 10% of all of the Vibe analysis techniques that are known today. There is really only one way of, forget learning this stuff, of being able to stay somewhat close to catching up this stuff, which is by practice. I have only one request.

</transcript>

---

## Daily practice builds intuition faster than tutorials

- **Do two vibe analyses a day** on small, real data (finance, fitness, browsing).
- Expect **90% of tactics to age quickly**; habits keep you current.
- Small **daily reps beat big, rare projects** for skill growth.

<transcript>

**Do at least two Vibe analyses a day.** Take your phone data, see what you learn. Take your bank statement, see what you learn. Take your phone records and see what you learn. Look at your Google Fit data, look at your Fitbit data, see what you learn. Look at your browser history, see what you learn. Look at your git commits, see what you learn. Look at your Jira tickets, see what you learn. Look at your emails, see what you learn. Look at your calendar, see what you learn. Personal data is everywhere. Look at your Spotify history, look at your YouTube search results, look at your Google search results. There's no shortage. If nothing, you will learn about yourself. Better yet, you may even learn the more powerful Vibe analysis techniques.

With that, let me draw this session to a close. Thank you so much for giving me such interesting insights. I certainly learned a lot out of this in terms of what kinds of analysis can be done. Hopefully, you take something out of this as well. I will be reachable. My email is on this invite, so just drop me an email at any point. I'd love to stay in touch. Thanks everyone. Have a good day.

</transcript>

---

# Vibe Analysis

[Landmark Group](https://www.landmarkgroup.com/) · 16 Sep 2025, 11:00 am UAE · Remote
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Transcript](https://github.com/sanand0/talks/tree/main/2025-10-16-vibe-analysis)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-10-16-vibe-analysis/)

# Transcript

Can someone who is joining remotely confirm that you are able to see me as well as the screen and hear me? The screen is definitely visible. Okay, Satyavrat can see the screen and hear. Thank you, Satyavrat. That is great.

We will kick off. We don't really have much of a concrete agenda. We are just going to hack it as we go along. The objective is this: AI is cool. But student answers are in some way a digital exhaust. **And as far as I'm concerned, that is the most interesting part of what I get.** So one of the questions that I asked them was: "Take a bunch of system prompts that should protect secrets. Then create a bunch of user prompts that will try and get the system prompt to reveal secrets, and have them fight against each other." I've already run the fights—that is, I've had every system prompt fight against every user prompt, and some of them defeated the system prompts. So I have that data. Now, is there a pattern in that? That is something that I would like to see.

What is it that the audience here would like to see? One of the questions that I had posted on WhatsApp is: Can everyone please mention what data sets you are planning to analyze in today's workshop? You don't have to stick to this, but it's always good to have at least one thing that you have as a starting point because otherwise, what are we going to play around with?

I put in all of the stuff that I had on my list that I just walked through anyway. So what about you? Rajat says my Apple Health data. Bhavesh says Google Calendar. Satyavrat says search data. Great. This is good stuff. Google Calendar may not be very large data, and there is absolutely nothing wrong with having small data. If you have 30 data points or more, that's still good. **But because this is personal, it's always interesting.**

Krishna says Google Takeout data. Now, Google Takeout has a lot of information, and you could analyze all of those. But if you have a point of view on "I want to start with this and then this," that is always fun. So, my Google Takeout data—there's a whole bunch of stuff that I exported a couple of days ago. I usually look at the size of these directories to see where the bulk of the data is, and most of my data is in Google Fit, location, active minutes, step counts, and stuff like that. Which sounds promising. There also seems to be a fair bit under "My Activity." That's where the bulk of the data is. My Gemini conversations seem to be the largest, and it's not like I talk to Gemini much—most of my conversations are with ChatGPT—but even then, it's pretty large. Not sure why.

Search data—I definitely want to analyze my search data, which is quite extensive. And there's also Maps data. I guess all the places that I've been to, all the places that I've searched for. Yeah, definitely interesting to look at. My YouTube searches, my YouTube watches—that's again relatively large. Play Store apps that I've searched for and stuff like that. So yes, that can be pretty solid data.

WhatsApp groups are fantastic. The advantage of WhatsApp is it's fairly easy to export from your phone. The disadvantage is that it's hard to get stuff like reactions, who's replying to which thread, and so on. But you can actually scrape that. And one of the things that we'll try and do is write code for a scraper, which will show you a few of the techniques that I've been playing around with recently.

Jayashree is looking at call transcripts. That's great. If you've got transcripts, even the audio version of it, great. But if you have the transcripts, that's even better.

OpenAI data. Okay, Deepak, that could mean either OpenAI the company's data or OpenAI ChatGPT data. Okay, ChatGPT data. Cool.

Mahesh is picking Maps and location data. Yeah, Google says it will take a few days. **You might want to split the downloads, Mahesh, into batches.** That is, go select in Google Takeout, and instead of picking multiple items, you pick one by one. I deselect all and then pick just one of those—if it's assignments, only assignments. And some of these, like "My Activity," will have a whole bunch of data. When it says activity data, it will by default select all; you could deselect and say I only want Maps. That's download number one. Then download number two is something else. That way, whichever is faster, you'll be able to start analyzing quicker.

And Gmail data—yes, massive, very powerful. How to export Gmail data is a question. If you're using Google Takeout, that will take a few days if you've been using it for a while. I've been using it since 2002 or something like that, so I have more than two decades worth of data, and it's a few gigabytes. That can take a long time.

Fine. So let's start with the assumption that 80% of you have the data that you want to download. But there's probably a 20% who either don't have the data that you want to download, or there is some other data that you want to download but you are not able to get it. We will now move into: **How does one go about extracting stuff?**

One of the techniques that I'm going to look at is: How do we build a scraper? The easiest way to build a scraper is to have a large language model build a scraper for some purpose. The traditional scraper will be where the LLM will say, "I will write a Python program," and typically it picks Python to visit that particular website and get the data. This stuff you probably already know. Or even if you don't, you tell it to do it, and for simple sites, it has no problem. The trouble comes when it's a site that you have to log into, and you don't want to give it your ID and password. Even if you give it your ID and password, that site is smart enough to block some naïve scraping attempts.

**The only robust way that I have found so far—not foolproof—is to use the browser itself to scrape.** And there are a bunch of ways in which we can do that. Approach number one is CDP. Slightly expensive, but probably the most reliable. What is CDP? CDP stands for Chrome DevTools Protocol. If you are using Chrome, or Edge, or probably even Brave or anything that's Chromium-based, you should be able to use CDP. Now, what that does is allow programmatic access to your browser.

How do I enable DevTools? Let's find out. Let's ask ChatGPT in the fast mode. "How do I enable CDP for Chrome, Edge, Brave, etc.? Give me quick one-line instructions." And what I will do is paste this prompt into the chat so that you can run the prompt yourself.

In my case, I'm using Edge, and it's saying if I just run `Microsoft Edge` from the command line with `remote-debugging-port=9222`, it should work. I've already done this. So I can test it by putting in the prompt: "How do I know CDP is running?" Let's ask. My aim here in giving you the prompts is simply to say: figure out the answers for yourself. But soon we'll get to the stage where we'll say: figure out the questions for yourself as well.

So it's saying if I curl the CDP endpoint, I should be able to get to this. Which means that there is some link. And that link seems standard. Which if I visit, it should work. And if CDP is not enabled, then it won't work. Fine. So I'll copy this link and paste it. And for me, it's saying that I'm running CDP because it provided some response or the other.

So here's a request: If you are able to get to the point where you are able to see CDP running because you have run one of these commands on the browser, please put a thumbs up.

**Question**: [User asks about running the command on Windows]
**Answer**: It will probably work. You have to go to the command prompt and copy-paste this, and it might work. If it says Chrome is not a command that it can find, copy the error message, put it into ChatGPT, and figure it out.

For those of you who are on Windows and it says Chrome is not a command that it can find or some such thing, copy the error message, put it into ChatGPT, and figure it out. By the way, this workshop is absolutely not dependent on you getting any portion of this workshop right. We'll be doing all kinds of things. We don't even know _what_ we're going to do. If this doesn't work for some people, we'll try something else.

**Question**: [User getting an error or blank page]
**Answer**: It's opening in an empty tab, does no page? Probably a new tab or a new window. Perfect. And then you go to `localhost:9222`. It shows at least an empty page and not an error? If you go to an invalid page, it may say something like "can't reach this page." But if you go to a valid one like port 9222, it'll at least show a blank page. You're getting a blank page? Okay, then it's running. Great.

You may want to try closing all your Chrome instances and starting. That might help. But otherwise—ChatGPT. Looks like about half a dozen people are able to get it running. Great. There are a few people who are facing trouble saying the user data directory is not found. For those who are facing that, whoever has solved that problem, if you can post the solution on the WhatsApp group, that will be very welcome. But what I'm going to do is progress assuming that you can do this. Because you can watch the video and figure out this part.

Now, the next step is: Let's assume you've already installed Codex. If you have not already installed Codex, install Codex or Co-pilot. I think Co-pilot might be the easiest. I'm going to open Co-pilot, but you could use absolutely any coding agent that you have, that you want. No problem. That could be Claude, that could be Cursor, that could be Windsurf, that could be Gemini CLI. The only thing is they should be able to run in "agentic mode." That is, they should be able to run the commands by themselves.

I'm going to pick Claude 3.5 Sonnet as my model. Actually, it doesn't even matter which of the latest models you have. The important thing is that you have it in Agent mode, which is what I have. Now let's ask this the question: "Can you access CDP at port 9222? What does it show?" This is a simple check to see if it is able to access CDP.

In my case, it's trying to access blah, blah, blah. It's saying yes, and it's able to locate all of the pages, the active pages that I have in my Chrome Debugging Protocol. Which is always good news.

Now, the beauty of this is: **Once we are able to give access to a coding agent to the browser, you effectively have Anti-Gravity, you effectively have Comet, you effectively have Open Interpreter... in your hands.** Simply because a coding agent can do anything, including writing code. The browser can go anywhere you can. And combining these allows us to do all kinds of very interesting scraping activity.

So, one of my problems is on LinkedIn. I can't scrape LinkedIn. Actually, I have given up on LinkedIn as a platform except for publishing stuff—almost like my blog—because I have, at the moment, 1,314 invitations pending. I do not look at this on a daily basis. But I need some inbox handling mechanism to at least know who are the people that I _know_ to be able to connect back.

So what I'm going to do is tell Co-pilot the following. Note: I want to describe a lot of things, but it's painful to type. ChatGPT has the best voice recognition that I know of. So I'm going to tell ChatGPT the following:

> "Look, I have a whole bunch of LinkedIn invites. I have this open in one of the tabs and you can access it via CDP. Go through this and extract all of the information that you can about these people and give it to me as a CSV file. Now keep in mind that if you scroll to the bottom of this page, it will allow you to go further down, and it will dynamically within the same page load some more items. So I want you to actually scroll to the bottom, wait for it to load the next bunch, and wait for it to load the next bunch and so on, until it gives up—which I think it does after about 200 entries or so. And then it will give you a 'Next Page' option. Don't worry about the Next Page. For now, if I get at least the latest roughly 200 entries or so from my LinkedIn as a CSV file from invites, that is more than enough. **Write whatever code you need to do this, get the output, make sure that it's working, and then give it to me as a script that I can run again the next time without having to use a coding agent.** That way the whole process gets automated."

I absolutely would not have wanted to type this out.

I have done this sort of thing enough that I know what I want well enough to describe it in approximately one shot. I say approximately because after this I'm sure I'll find ten things that I can improve on this. But it's a starting point. Now that we have this, let's give it to Claude and have it run.

Actually, I'm not going to have it run. The reason is, Co-pilot, I don't know how to configure so that it will run all by itself. So I'm going to configure `codex` on the command line to do this properly.

For those of you who are using Codex and it says "Oh, I can't run, I can't get to port 9222" even though you obviously can see that port 9222 has no error, it may mean that Codex is running in a sandbox mode. Same for Claude. In which case, at least out here, what you might want to do is in that little dropdown at the bottom left where you choose the mode, you can instead of Agent go to "Agent Full Access" and try it. **This is a workshop where we'll be doing dangerous things. You just have to hope that the internet is not already too full of dangerous things that will destroy your laptop. But give it full privilege. Let it wreck your machine.**

**Question**: What is it called in Cursor?
**Answer**: No idea, but if it asks for approval say yes. Ask ChatGPT or Cursor itself what permissions you are supposed to give. It's exploration.

It says CDP is reachable. Perfect.

Now, one of the things that I've told it is: "Here's how you run Playwright on my machine." Playwright is a JavaScript-based tool—or Python-based for that matter—that will allow you to access CDP programmatically. In other words, it can write Python or JavaScript programs to access the Chrome Debugging Protocol. And it has a bunch of useful utilities. So I find Playwright to be a more useful way to access CDP.

What does that mean for you in practice? It means just telling it: "Use Playwright. Install if required." In my case, I've already installed it, so I'm just telling it to use Playwright. I'm also giving it a more specific instruction, but this is honestly totally useless. It knows how to run Playwright. In fact, it knows how to run Playwright better than I do. In this case, I just happen to know that _this_ particular configuration is what I want it to use because the default configuration it uses does not work on my machine. So I'm being very specific.

To recap: If you find that a coding agent is making the same kind of mistake more than a couple of times, then you can tell it: "Don't make this mistake, instead do it this way," after you've figured out how to solve the problem.

This leads me to another technique, another what I believe is a superpower, that I will talk about a little more, which is called a **Post-Mortem**. After running any conversation with a coding agent—or ChatGPT or whatever—I often ask it: "**What am I doing wrong? How could I have improved this conversation? What mistakes did you make, and what could I have told you so that you won't make such mistakes in the future?**" And I log it. If I find that it's making the same kind of mistake three or four times, then I add it to my `agents.md` or ChatGPT custom instructions or whatever. In short, a post-mortem is a very powerful technique. Works with humans, works with machines. I'm too embarrassed to do it with humans; I have no problem doing that with machines.

Now, this thing is still turning white and black, which means it's still working trying to figure out how to get all of my LinkedIn data. And it's relentless. All of these coding agents these days run for hours. I think the METR—I don't know if you follow this organization METR, they track roughly how long coding agents are able to work independently—and that number is approximately two and a half hours as of now. And it's exponentially increasing. About a couple of months ago it was less than an hour. So it seems to be doubling every two months-ish.

So now, let's take a look at what exactly it's doing. It's writing Python programs like this: `import asyncio`, `import json`, blah, blah, blah. And then it's visiting my "Invitations Received" page, evaluating some JavaScript in that page, and then getting the information from there, and then printing the attributes from there. And here are some of the attributes that it got.

I'm going to jump back to what we were looking at earlier. **Question**: Were you able to get _any_ coding agent to use CDP to read data from _any_ site? Thumbs up if yes.

Now that I know I have at least five of these [thumbs up], what we'll do is go to the next section. One of my problems is on LinkedIn... actually I've given up on LinkedIn... [Skipping section as it's repetitive with the live demo].

I'm going to show you another related technique. I'm going to extract all of the data that is there from this WhatsApp chat. I'm going to extract data beyond what the regular phone WhatsApp export can give you. The phone WhatsApp export gives you three pieces of information: at this particular time, this person said this text. What it does _not_ give you is these reactions. What it does _not_ give you is what is a reply to what. The quoted text.

But I happen to have a **Bookmarklet**. I will show you what it does, and then I will explain what a bookmarklet is. This bookmarklet called "WhatsApp Scraper" has copied 13 messages, and as I scroll, it goes back in history and copies all of the messages that are there. And I'm having to do the manual scrolling because in this particular case I want to be in control. But now if I click on this "Copy 54 Messages," it will show as JSON every single message that was there and copied. Now, the order in which it copies may not be... oh wait... I just realized that it is obviously not sorted, and therefore some of the stuff that I've been doing in the past may be an error. So I will make a change to sort it. But even though it is not sorted, at the very least I get, for instance, the quoted text. I get the reactions. So there was one thumbs up and three flames against the UPI data comment that Narasimha Prasad posted. This is useful.

**How does this work?** A bookmarklet is a piece of JavaScript that you can bookmark and run. For example, if I said `javascript:alert('Hi')`, then it will alert 'Hi'. In other words, `javascript:` followed by something is exactly the same as copy-pasting that same thing and putting it into the DevTools console. Now, what I put after the JavaScript can be a long string. It can be a full program. And we can have a coding agent write such a program. Which is what I did.

I have this button. If you inspect this—and I'll ping you the link to this tool on WhatsApp so you can inspect it—you will find that this is `javascript:var whatsapp_scraper...` and it's a huge one. So let me copy... outer HTML... and paste it here. And you'll see that the JavaScript is a full-fledged program.

So, by just clicking on... and because it's a full-fledged program and it's also a URL, I can drag and drop this here. It's just a URL. So I can bookmark a URL which is actually a JavaScript program, which means that by just clicking on a button, I can run something.

And that's exactly what I did on this. I click on the bookmarklet, click "WhatsApp Scraper," it runs the JavaScript code which says "Add a button that says Copy N messages where N is the number of messages that it's able to scrape from this." And at any point—say at a one-second interval—keep polling the screen for any new messages, deduplicate with existing messages, keep them all in a JavaScript array. Pending to-do for me: sort it all by date. And then click—when "Copy" is clicked, put it all on the browser clipboard.

Now you can do this for all kinds of things. I find it useful, for instance, to go to Hacker News. I'm curious about what this thread is about. It's huge. There is no way I'm going to sit and read all of this. So instead, I have a bookmarklet that is a HN Thread to Markdown. Which when I run it, it copies it in a far more concise format. So there are 1,070 messages; all 1,070 it's copied, one per line, with the threading and just the information that I need—which is: this person said this at this particular time as a reply to this other message. Which I can then copy-paste into something like Claude and prompt it to write this in a format that I want.

**Now, the format that I want I will come to, because that is the third superpower that I'm going to talk about, which is Style Transfer.**

But... [checking progress of LinkedIn scrape].

Okay, I'm going to give up on Claude for now because the dataset might be too large. And allow ChatGPT to run its usually very diligent, very rigorous analysis. The only thing is after 15 minutes it will probably time out. If that is the case, then we'll probably take a slightly easier prompt for it to do. But my gut feel is it will probably... oh. "Unpack... we have the full directory structure... oh, it says it still needs one thing from me. What specific... where is my weight data?" Choose one dependent variable. Okay. I don't know. You figure it out. **Let it apply its domain expertise. Don't do work. Please practice laziness. It is a skill that requires a lot of effort. We need practice. That's how we will know how to leverage it.**

So yeah, please go ahead, give it a shot. Have it write and just analyze the data in _any_ format. Ask any question off of your data. The only thing is: you want to get some insight out of it.

In parallel, I mentioned that I was going to talk about **Style Transfer**. So rather than tell you what it is, let me show you what that can do by taking some dataset of mine. I'm going to take my Play Store data. And zip it. And this time I'm going to give it to Claude. The prompt that I'm going to give to Claude is going to be the important one.

My activity... Search... Google Play Store... Zip file. That's a small zip file.

I'm going to take roughly the same prompt, but in close to complete form. Let me remove some parts of this. And I will talk about the context. "This has my Google Play Store data."

The prompt says: "Write like Malcolm Gladwell. Visualize like the New York Times graphics team. Think like a detective who must defend findings under scrutiny." And it goes on to explain how exactly the New York Times and Malcolm Gladwell write their articles.

What I have found is... take for example that Y Combinator thread on Anthropic acquiring Bun. We copied that as Markdown. I sent it with almost exactly the same prompt to Claude. The article that it wrote was beautiful. I could read it. Now obviously I am saying that because I _like_ Malcolm Gladwell's style. You may like someone else's style. In fact, sometimes we don't even know whose style we like.

I was reading Buddha's Kalama Sutras... [Retelling the Buddha story about critical thinking and style]. So I took the sutras and asked Claude: "Look, I want you to give it to me in the style of a modern philosopher, writes really well, easy to read... Tell me who such a person is, describe what their style is, and then explain it to me in that style." It said **Pico Iyer** is the person you should look at. Never heard of Pico Iyer. Great. And then it wrote the sutras in his style. And it was beautiful. To the point where I'm able to repeat the summary of what the sutras were about.

The next thing is I'm going to ask it to translate Thirukkural and Kamba Ramayanam in somebody's style like that. So that I can listen to stuff that I can't follow the script of. Literature is now open to us in so many forms. And our WhatsApp messages are literature. Our medical reports are literature. Our bank statements are literature. You will find such beautiful information. As long as you're able to get it in a style that you enjoy and like.

As a result, one of the things that I've been doing is capturing styles of various people for various things. For example, when writing code... [Recap of coding styles: Luke Edwards, Sindre Sorhus, Mike Bostock].

Style Transfer is one of the most efficient ways of providing instructions to an LLM or an agent. Because you just say "follow that person's style," you already know it. That efficiency comes because of that vastness of training. And that efficiency applies in many areas. I can use it for non-fiction authors. You just saw me using Malcolm Gladwell style. Randall Munroe is another that I use. James Gleick is another.

You can use it for art. So let me show you how... when creating something with NanoBanana... I specifically asked it for unusual illustration styles that are not popular yet visually striking. These may not even have a name, but give me some. It said there is a frottage technique... [Describing texture/charcoal styles]. And then I said, okay, draw a person in a cafe, and then added this style. This is what NanoBanana gave me. Not bad. Okay, that's a style. Good to know. Here's another style. Here's another style. And this one looks kind of photorealistic-ish, and I want it. What is this? Scrumbling. Okay, translucent scumbled layers. I can use that for one of mine.

And all it takes is having a **Style Gallery** to be able to pick styles from. So a process that you can follow is: When trying to communicate something, whether it's for efficiency or for aesthetics, whatever—ask it: "Whose style can I copy? Ask it what that style is. Apply that style."

Which is what we did for my Google Play Store data. And it's still running. Okay, it's finished 46 steps. So that's okay. It's writing all the code to run.

Chat GPT has given up? Or where is Chat GPT? Trouble is... I don't even know which... Fitness Data... Hmm. Great. It's identified that my weight metrics contain my average blah, blah, blah. This is enough to begin the analysis. Next step, I will do it automatically... Now it's saying: If you don't care, reply "For Go Full Investigative Mode." So what it did in my case was did some analysis and said "Now, do you want X, Y, or Z?" I never read this stuff. Just let it do what it wants. What is its intelligence for? But of course, if I have something specific in mind, then I will tell it.

So yeah, please go ahead, give it a shot. Have it write and just analyze the data in _any_ format. Ask any question off of your data. The only thing is: you want to get some insight out of it.

We need to take a break. We will take a break in three minutes. Just for us to get enough people to say they've started the analysis. And let the analysis run. Once it does, we will come back and take a look at what the analysis has done and shown us.

If you want to see the recording later and do it later, usually doesn't happen. I have a whole bunch of "To Watch" videos on my YouTube list. The list keeps growing. And the only reason it shrinks is I knock off stuff from the top, not because I watch them.

So do you have any suggestions on how do we... like, I also have a sequence of a lot of "Watch Later"...

**Question**: Do you have any suggestions on how do we handle the "Watch Later" list?
**Answer**: My solution to that these days is **Style Transfer**. Part of the reason I don't watch is the cognitive load. Put another way, it's too much effort to watch a 20-minute video. Sometimes even a 10-minute video. Watching _any_ video. Or reading a complex article. So I go to NotebookLM. Upload the video. And then say, "Now give me a Malcolm Gladwell style article."

Here is the thing. The first sentence in the Gladwell article will hook me. Once I'm hooked, there is no problem. And the article is not particularly long. Sometimes the article is about as long as the original text or any other kind of summary. But that curve that I have to cross is a lot easier once I have the hook. And my discovery was that at the moment, Malcolm Gladwell's opening line does that for me. You will have to discover that for yourself. But it's usually not hard. Just go with what you like.

Okay, 10 people. Thank you. We will take a 10 or 15 minute break-ish. And we will come back. People on the remote... whatever mechanism you are joining in... please stare at the screen for 10 minutes or whatever.

---

Okay, let's get started while the others join in. One of the things—quick question for people joining online, are you able to hear me? If so, maybe you could just say yes or give a thumbs up or something. Put that on the chat too. Am I audible? Is my screen visible? A thumbs up from somebody who is joining remotely would help. I’ll wait for that before we get started. If there is anyone online, if not, then of course life becomes easy, we can just run this in the room.

Okay, then we will sort it out. We’ll have to wait for [Name] to come back. But in the meantime, any questions from the room?

- _[Technical check regarding audio and screen visibility]_ *

Okay, let's get started.

First, let me talk about the intent of this. This is slightly more chaotic than my normally chaotic workshops. And therefore, a question that's running through your mind is, "What am I supposed to get out of this?"

Three things:

1. I'm hoping that you will **get some insight from your personal data**. That is the easiest part. This is very easily done. Take your personal data, give it to ChatGPT, ask it to give you some insight. It will give you something. And if you repeat it two or three times, you will invariably get something that you didn't know. I'm hoping that at the end of this workshop, we will all go out taking at least that.
2. The second thing that I'm hoping we'll learn is a little more transferable: **How do we go about analyzing such data?** Is there a pattern to what kinds of insights we get? The prompt that I shared is a starting point, and we will spend a portion of the second half going through that in some level of detail.
3. The third, which is probably the subtlest but might end up coming through the clearest, is the **set of meta-patterns or techniques**. Like the fact that you can use CDP (Chrome DevTools Protocol) for scraping, or the fact that you can do style transfers, or the fact that you can do a post-mortem on your queries. These are techniques that work with agents right across the board, and you can apply them anywhere.

While I mentioned the last one explicitly, I didn't mention the first two explicitly, so I'm doing that right now. Our aim is to come up with an insight from personal data and to figure out what kinds of prompts are working well for doing better analysis and narration. The prompt that I shared is my experience, and you will hopefully discover yours.

So, let me once again recap what the exercise is.

**Step 1:** Pick any agent—ChatGPT, Cody if you want, Claude, Gemini, whatever—and pass it your data. Pass it a prompt that roughly looks like the one I put in the chat window. Just use this prompt with your data and see what insights it gives you.

Once you do that, what we will all do is share the results of the analysis. Some of you have already put in your prompts and it's running, so by now it probably has the results.

Let me see if mine has come up with any results. In my case, one of the questions that I had asked it was: "What can you infer from my YouTube listening?" There's an executive summary, but I'm more interested in the narrative story, which it's still coming up with.

Okay. "Two lives of a digital polymath"—presumably the polymath is me, and I'm very flattered, but it does a very good job of flattering me. "Based on 16+ years of viewing history." Every day at 4:00 PM something unusual happens. Now I'm hooked. **What am I doing at 4:00 PM?**

Okay, I kind of come back from the office early some days. Did it get the time zone right? What time zone is it operating on? If it is 4:00 PM India, that is exactly the time when I come back home. Let's see. "When people are wrapping up work or checking their phones, Anand is deep in YouTube. Not for entertainment, but as part of a carefully orchestrated ritual." What ritual have I been running for 16 years?

Okay, "Two distinct modes: learning and living." Ah, maybe, okay, I'm beginning to see a possibility. "Afternoon hours are for absorbing knowledge, watching lectures, reviewing... my own teaching content. And evenings are reserved for life outside screens." Yes. **48% of all of my videos are watched between noon and 5:00 PM. I did not know this.**

See, I did not know that I sit in the office watching—well, useful videos—but still watching videos. I did not think that I was learning much from videos actually. Most of my information I assumed came from reading. This is telling me something that is certainly surprising.

"AI videos recently... scaling... These videos I even rewind and watch and re-watch and figure out what the hell is he saying, which paper is this?" Okay, lots of Telugu and Tamil cinema. More Telugu than Tamil because I can stop at any point and resume; it's all the same story. And these worlds rarely intersect. Correct. I even have different places where I do educational videos vs work videos, otherwise, it gets very confusing to my brain.

"Search obsession. 28% of YouTube activity starts with searches." Ah, this is also true. What I do is, when I search for educational content, a fair bit of this goes into my course content. I just look at the description, see if it is apt, copy the link, and put it in my course content. I don't bother watching the videos. I have better things to do; my students can come and give me feedback.

"I watch a **lot more educational videos than I thought**. These especially happen during office hours in the afternoon, 12:00 noon to 4:00 PM. I didn't know that."

And that is my insight. What I'd love for you to do is share your insights as we go along, and then we'll go a little bit into some of the meta-learnings around how we can get better insights from this.

Rajath has an insight. If you scroll along your weekly distance line, one region is dramatic for Rajath. A week that begins on April 1st, you hit your peak: 13.6 kilometers and eight workouts. Wow. And then the volume fluctuates. The sharpest on-week change happens around April 15th where it plunges to around 10.9 kilometers. Oh, okay. And it says that is the closest your training log has to a plot twist. So congrats Rajath, **your training regime is so robust that it is almost boring.** And this is clearly an outlier.

**Question**: How did you share your YouTube history with it?

**Answer**: I went to Google Takeout. Under "My Activity," it has a whole bunch of things. One of them is YouTube. The direct YouTube listing will not be there on Takeout; it is under "My Activity" and a lot of things are hidden under My Activity.

This is one. Please take a look at your own and see if you find anything interesting. From my weight loss story, it is doing a bunch of plots. One of the things it learned about my weight loss is that it was not gradual weight loss. It was **"cut hard and maintain like a pro."** Yeah, that I know. About 23.5 kilos in six months. And then, yeah, I've struggled to reduce it further. So Jan to late June is almost a perfect linear decline with an R-squared of 0.97. 1 kg a week. Okay, I did not know that it was that high a linear decline. And after that, a near-flat drift. In other words, losing only about 30 grams a week. Which is not much.

"Consistency is the real flex. Most weight loss curves look messy; mine is unusually smooth and monotone." Making me blush now. "Your body fat percent arrives after the plot twist." Correct. I only started measuring it in November for my next year's goal. And yeah, it can't explain how I got from 86 because it starts after the cut. "Subtle sub-story: Weigh-in completeness is highest in Jan and May and drops in July-August." So I'm not consistently measuring my weight because of travel.

And you'll notice this was not as interesting. The main difference between this and the earlier one was I asked it to write like a Malcolm Gladwell story. Here I did not ask it. **The style transfer has a huge impact.** However, what I find is that the **quality and depth of analysis in ChatGPT tends to be more robust.** Not saying that Claude makes mistakes often, but ChatGPT makes even fewer of those mistakes. So sometimes I have Claude run analysis, and then ChatGPT cross-check it after Claude has written the story around it.

Do share any other stories that you found from your data. If it's errored out, try again. The prompt is fairly straightforward. There's a variety of different datasets that you can try.

In the meantime, I'm going to see if there's anything else that I can show you in the background. We talked about post-mortems, we talked about style transfers. Topic modeling is probably the most advanced of what I wanted to talk about. So yeah, let's do that.

This is the part of the workshop where I talk about something, and you continue doing your work. Stuff is getting recorded; if you want to occasionally pay attention to what I'm saying, please do.

Here's what I want to do. I want to take a collection of text and I want to cluster them based on similarity. What are similar things that I'm looking for? Let's take my YouTube searches as an example. I want to see what are all the things that I'm searching for and is there a cluster. Now it already looked and found some clusters, but I want to be more exhaustive.

So, I'm going to open my activity on YouTube. This contains a whole bunch of stuff. "Watched" and all is there, but I want to get all the "Searched fors." There are 5,944 of these. So I'm going to take each of these and delete the first bunch of words so that I have a set of categories. Now, I'm going to take not the whole thing, but maybe a few hundred of these to do sample topic modeling so that you get a feel for what topic modeling is.

For this, I'm going to use a tool that we built. You don't have access to it, but that doesn't matter because I'll give you access to another tool that will do the same thing. This tool lets me paste stuff and cluster any documents that I might have. How is it doing it? It is taking each of these documents—which is really something I'm searching for—looking at the semantic similarity between these. In this case, I'm looking for the movie _Athidhi_, which is a Telugu movie. And it is exactly the same word, so it's found that this is one cluster. I've looked for it five times. I've looked for Visu movies five times, but you'll notice that it's "movie" versus "movies." And it's still saying that at a 90% embedding threshold, these are the same.

Let's reduce the threshold a bit. Now there is one cluster of _Raanjhanaa_ related stuff. _Raanjhanaa_ songs, _Raanjhanaa_ lyrics.

**Question**: Is it looking for text similarity or semantic similarity?

**Answer**: This is semantic similarity, not text similarity. The logic behind the scenes is: calculate the embeddings, find out the cosine similarity, anything that is less than a certain threshold or more than a certain threshold gets clustered.

Here's another big cluster. This seems to be about general Telugu or Tamil movies. I don't seem to be too fussed about the distinction. Here's an overlapping cluster with _Simhadri_, which is I think a Junior NTR movie. And this... though I don't know why I watched it so much... _Bhagyaraj_ movies. I watch a fair bit of. Great. But boring. Beyond a point. Interesting that these are the major ones, but I don't want to have to sit and do the work. What is the model for?

So the next step is to ask it to find maybe about 40 topics that I'm looking at, and you figure out the names for those topics yourselves. Use a good model like [GPT] 4o-mini that is also fast and find the topics. So first, it will do a K-means clustering of all of the stuff. It says cluster number one: _Bomman_. Okay, I don't know why these are similar, but... oh okay. Tamil movie parts, _Maryada Ramanna_ films, Visu movies. It changes dynamically in the sense that it creates the titles dynamically. Next time I try it, it will probably give a different answer. But the way in which it named it was: given these clusters of documents, it creates the names that capture the spirit of each cluster, differentiated from the others.

What was the process followed for this?
Take off these 40 clusters, five samples. Pick the five most representative documents or searches for each of these. And in case they are longer than 200 characters, chop them at 200 characters. Ideally, I should truncate at the middle, but maybe I'm not doing that. And then send all of these 40 into 5, that is 200, times max 200 characters... so max 40,000 characters... which is what, 30,000 tokens? Maybe 20,000 tokens? And then ask it to name each of those.

Which is what it has done. So, "Pink Butterfly" must be my wife. "Crazy Mohan," "Rockstar"—okay, Rockstar is again my wife. "Raksha" is probably... could be either of us. And so on. So okay, I get a sense of what are all the clusters.

Is it grouping similar movies together? Yeah, kind of. Here, for instance, the song "Zara Zara Touch Me" from _Race_ is actually copied from _Deep Inside the Bamboo Tree_. And it's saying that, look, here are some that I'm putting into this cluster that I'm not very confident of. In fact, this one probably seems more outside the cluster than inside the cluster.

So let's take it to the next level. I've got a bunch of topics. Against these topics, you then do a re-classification. For each of these, which topic is the closest? Let's classify those. And done.

All right. So it's saying out of these, "Red Bruce Willis" is 20% similar to a Visu movie. But if you keep going, is there something that it's closer to? Well, maybe not. It's gone beyond the screen. But let's take "Create Infographics." That seems to be matching "Data Visualization Tools" fairly well. So I can take the best match for each one of these. And for "Red Bruce Willis," "Rockstar Movie Songs" seems to be the closest. That's not really anything related to Bruce Willis. 42% "Raanjhanaa Film Songs"..."Jeene Laga Hoon". Is that a Raanjhanaa film song? Does anyone know? _Jeene Laga Hoon_? Probably not. But then I can say, look, don't give me low cut-offs. Give me only stuff that has at least, let's say, a 45% cut-off. And then it says, okay, that's a match, this belongs to this category, and so on. So now I have something that gives me, for each of these searches, what are the topics that it matches? And then there's a big "others" list. But that's okay. I want an "others" list. I don't want it to misclassify.

This is broadly topic modeling. How could you run this? We converted this into a library. One of my students wrote a library which is on PyPI called `topic_model`. And I will put that in the chat window. I'll come back to Mahesh's question.

What this library does, once I open it, is from the command line—firstly make sure that your OpenAI API key is exported—you can provide it a text file. One line per item. For example, if you have all your Google search history, all WhatsApp messages that people are talking about, whatever. One line per item. Then just run `uvx topic_model`. No need to install it. And it will create an output file that has all the topic model details. For example, if your `docs.txt` has these five sentences and you run it, and if you explicitly say `n_topics 2`—you don't need to, it has a default of 10 or 30 or something like that, but you can decide that you want so many topics based on K-means clustering—it will come up with something like this. A text file, tab delimited, that says: This piece of text best matches this topic which it came up with by itself. And here are some of the details. Here is how similar it is to that particular topic. And so on. And then there's also a variation where you can create a visualization and stuff like that, which I'm not going to go into.

But this is another way, which offline you can try for getting insights from digital exhaust. Which is: take any textual data that you have, any logs that you have put in. Run the embeddings—embeddings are very cheap. Apply a model on top of it that will explain it. That is also cheap because we are not sending the entire documents, we are sending only a sparse sample of the documents. And you will get a result which then is matched in a rigorous way.

This will work best for normal English. For what I was trying, it will not work so well because embeddings don't recognize song similarity that well, and these embedding models are ancient. What would it work best for? Email subjects. It's perfect. If you wanted to take all the email headers—just the subjects in particular—and say, "What are the kinds of email subjects that I'm getting?" this is the best tool. Calendar as well.

In the meantime, anyone else who has found any insight, please do share and let's discuss.

**Question**: Google Takeout gives all data in JSON, but a lot of our personal data are in PDFs. What's a good practice to make them available in an efficient way? PDF to Markdown converters? Possibly, or just upload your PDFs.

**Answer**: Let's do that. So I'm going to be brave and go to Claude and give it all my bank statements.

**Question**: [Audience member mentions trying this before and encountering issues with password protection and multiple steps].

**Answer**: Got you. And the short summary I'm taking away from that is: **Allow an agent to run it.** Now the good part is ChatGPT and Claude and Gemini are also agents with the ability to run code. So let's upload it. So I'm doing exactly what you said, with only one twist, which is I'm doing the processing remotely. So I've uploaded a zip file with a bunch of PDFs. This has all of my bank statements. And we will put in the same prompt which is "Analyze insights" with a few small tweaks. "Analyze my bank statements like blah blah blah" and on the output format I will tell it to ignore the exec summary and actionable report. Just give me the narrative Malcolm Gladwell style story. And let it run.

My guess: **Bank statements are very well structured. It will have zero problem extracting it.** It will probably make a mistake in 2% of the cases. For 2% for this kind of an analysis, it doesn't matter. I'm not balancing ledgers.

**Question**: But bank statements are password protected.

**Answer**: Good point. The bank statements are password protected. I have removed the passwords on my bank statements and stored them. Yeah, correct. Exactly.

So it's doing this. In the meantime, does... Ah, Krishna has patterns in "large wait good bad trades."

**Krishna's Insight:**
**"Your best buys are all buys."**
Is that a known insight or is that new?
**Audience**: New.
**Anand**: Wow.
"You accumulate aggressively during weaknesses and often catch the inflection."
**Anand**: What's your comment on that?
**Audience**: Now that it mentions it, it makes sense. I never thought of it that way.
**Anand**: Interesting. You never thought of it that way. Okay. But it makes sense. That is good to know.
"Worst calls are sells. You consistently exit early."
**Audience**: I didn't know.
**Anand**: Wow. Okay. Because selling is actually the point of buying. And this is useful to kind of reflect each time I sell going forward. A very good point. A very good point.
"Especially during temporary dips. And the classic pattern is that **you sell on fear and stocks rebound immediately after**."
**Anand**: Okay. And this is ChatGPT was it?
**Audience**: So what I did was... Zerodha gives you a portfolio dump which I do on a regular basis. It is there in my temp folder. So I was able to pull all the files from the temp folder into one folder just now. Used VS Code to create one integrated file out of it with the timestamps of each portfolio holding date. And I fed that into ChatGPT. And asked it to analyze it for insights, concentration risk, sector exposure, blah blah blah. And this is the most important insight that came out of it.
**Anand**: Fantastic. Fantastic. And this is what we are hoping to get to. That is for each of us to take something that is meaningful simply by virtue of forcing ourselves to sit for three, four hours and getting something done from some data in an environment that is conducive to it, but we might not have done it otherwise. Simple as that. Please continue because the kind of stuff that we get out of it... there is no end to the insights. Others, I'd love for you to share. As long as it is something that you didn't know, please do share. And if it is something you already know, try again with any other data and we'll be able to find more stuff.

**Audience**: [Inaudible comment about realization of repeated behavior].
**Anand**: What happens is I didn't realize that this is my repeated behavior. Because exactly what happens when you sell something... you make a decision, you don't track how it behaves subsequently. You kind of, you know, you're okay. And then...
**Audience**: actually... And here... so the state is not complete data. Because what happened here is if a stock has gone to a zero holding, the software doesn't know what the stock price was subsequently. So I went from 100 shares to 50, 50 to 20, then there is a timestamp of the price also there.
**Anand**: Oh okay.
**Audience**: But when it went from 100 to zero, then it doesn't show up in my subsequent holdings. So the software does not know what happened to the price.
**Anand**: So this went to the internet?
**Audience**: No it hasn't run it yet.
**Anand**: Okay.
**Audience**: So the next step would be to say I'm going to have further timestamps even for positions where I exited fully.
**Anand**: Yes. That's what I should be doing.
**Audience**: And then see what happened. So this is partial data in some sense. Not complete data.
**Anand**: Okay. So maintain a record of share prices even after you exit. Only those. You can't maintain all the shares.
**Audience**: Yeah. So ideally what I should do is convert this into a matrix which has got essentially all holdings and timestamps of all dates with prices as well as holding levels.
**Anand**: Summarize then when you exited something, was it good looking back from the future?
**Audience**: Yes. That's what I should be doing. I think the next step is going to be change the windows. Right? So here, like what is the window? Is the window supposed to be one month? Window supposed to be three months? Like it has to vibe with my style of investing. That hasn't happened here. It is assumed I'm a trader or I'm a short term investor, long term... I don't know what assumption is. All that I have to put in as my style.
**Anand**: I think you got more than your money's worth.

For those who didn't hear that, Mahesh's comment was Krishna got more than his money's worth from this session.

Okay. From Bhavesh: "You don't work a 9-to-5, you work an 8-to-12 and a 9-to-1."
Okay. Interesting.
"Our forensic analysis of 2,516 calendar events and network metadata reveals a double hump work pattern that defies biological rhythms."
Bhavesh is you. Okay. Tell us more Bhavesh about this.
**Bhavesh**: Yeah, it's not regular now, but I think it was past data. I'm an engineer right, and my team is divided across US and India. So majorly the meetings were either in the early morning or late night.
**Anand**: And your calendar is mostly empty between the 12 to 9 window. Nice. Nice. Okay. So arguably not necessarily surprising. You knew this. Could you prompt it to find something that is surprising? And taking a cue from what Krishna discovered, could you even prompt it to say give me something that is actionable? A) Tell me something I don't know, and or I'm not likely to know, and B) something that I can do about it that will improve my lifestyle? Just continue the thread there.
**Bhavesh**: It's there in the article.
**Anand**: It's there in the article it generated regarding that page? Oh, I see. Okay. No, please take a look and if there's something that you find that is truly surprising and useful, do share that as well.

Again, if anyone else is finding anything else that is interesting, please continue sharing. My bank statement analysis is now at 27 steps. It is in detail parsing my bank statements. Which we will let it do.

Okay, this story we already saw.

Okay. Now, let me go on to a couple of other things which are fairly easy to do and you can process this in any way you want. But it's also something that you have likely seen.

Let's start with **NanoBanana**. NanoBanana is a **thinking model**. And because it's a thinking model, it can do a fair bit of pre-processing beforehand and give you a result. So, here's what I'm going to do. I'm going to take a transcript. In fact, let me take the transcript of my last workshop. And I'm going to give it to NanoBanana. And say get me insight, but there is a small twist which you will see in a few seconds.

First let's take a look at my talks. My last talk was probably an SCDM keynote which is transcribed here. So this is a fairly long-ish transcript. I think this has... yeah, okay, only one part. The prompt that I'm going to use again is something that I will dictate into ChatGPT.

"Here is the transcript of a talk that I had delivered at the Clinical Data Management Society's annual conference. Find big useful and surprising insights from this talk. And give it to me as a **sketch note**."

Now you've seen sketch notes. Nice artistic representations, but the thing about sketch notes is they often depict what happened during a talk. I don't want what happened during the talk, I want the insights coming out of that. Let's give it to NanoBanana. With thinking mode enabled. This thinks. It really thinks a lot. And then draws the picture. Not saying that the picture is letter perfect. There's 1% percent, half a percent, maybe even less... [errors].

- _[Anand mentions uploading or pasting the script]_ *

I pasted the script below. And yeah, somewhere here. It's a long piece of input. But once I ask it to deliver the insights as a sketch note, hopefully eventually it will also generate the image.

Ah, did I... I clicked the stop button which I didn't intend to. Let me... Or okay, fine. Even now, let me just generate a sketch note. Let it continue. But my guess is that's what it would have done even otherwise. And if it doesn't, big deal. We have two parts. One where we just have the conversation with it, get the insight, and then have it generate the sketch note.

Now, sketch note is a popular format and easy to understand format. But is it the only format? And if everybody starts creating sketch notes then what is the big deal? right? So, let's ask Claude the following question.

**Prompt**: "I'm creating sketch notes from documents and talk transcripts which is useful. But sketch notes are not a very unusual format. I mean it's almost become commonplace. I want some other formats which are less popular but still as engaging and as effective as a sketch note in communicating the bulk of the information that has happened at an event like a talk. Can you review and identify half a dozen such and pick two or three formats for me that I could use? Give it to me in a form that is concise and passable to an image model like NanoBanana."

That way I know that I just have to copy-paste. And this helps. Trust me, being able to tell an LLM just give it to me in a copy-pastable way saves you so much of review time. And I'm going to change just one word here. Instead of "review," I'm going to say "research" and ask Claude to do it.

Why not ask ChatGPT to do it? I find Claude to be, when generating prompts, Claude tends to give the most succinct prompts. ChatGPT tends to give the most verbose prompts. ChatGPT's opinion is: I am smart, the other model is likely to be dumb, I will over-specify. Claude's opinion is: People are roughly equally smart, I will share it in a way that I will understand, and that works well for me because that's also less review time for me. Gemini is closer to Claude in that sense, so I use it as an alternative. But if I wanted to give a prompt to a weaker model, let's say I want to give a prompt to Claude 4 Haiku or GPT 4.1 Mini, then I would go to ChatGPT and say now you give me the prompt because you can be prescriptive, you can use your intelligence which distills that into something a weaker agent can execute just step by step. Let that happen.

It's still analyzing my bank statements. Have anyone else shared any stories? Okay. We have a bunch more. That is lovely.

**Shreechand**:
"You don't ride when you're motivated. Ride meaning bike... Cycle. Okay. You ride more when things are slightly out of control. Your highest volume phases correlate with irregular sleep hours, late night/early morning rides, cramped clusters of activities with almost no recovery days."
**Anand**: Do you... Is this something you knew?
**Shreechand**: But not in this way.
**Anand**: Not in this way. I was hoping but I've not understood this level. Very insightful.
"You cycle most when life is least stable. Not when you feel disciplined but when you feel restless. That's why your best months were not your best phases in life. How much data did you upload? There were transitions, identity changes, unfinished chapters. You didn't cycle harder because you were inspired, you cycled harder because you were processing something. And this isn't guess work, it's traceable. Bursts of 4:00 PM plus 2:00 AM rides. My god. Irregular patterns. 30 days in a row and then none. No periodic structure. Not weekly, not monthly. Motivated people form habits. Restless people form spikes. Your archive shows spikes. My god."
**Anand**: If this isn't a roast I don't know what is.
"You bike to metabolize chaos." Wow.
**Shreechand**: I really do 2 AM rides.
**Anand**: Yeah. Later usually after 12. What about dogs?

Okay. That was really powerful. That was really powerful.

Okay. **Anirudh**:
"176 days. You consumed approximately 1500 hours of video. That's a 4 minute average per video assumption. Got it. And the content from thousands of unique creators. A diet that defied easy categorization. Thousands of creators is fascinating. You are not the algorithm's ideal user. You didn't binge, you didn't re-watch, you aren't... you don't loyalty subscribe. You are a grazer in a platform designed for bingers. YouTube doesn't know what to do with you."
**Anand**: Oh wow. Okay. So how much of this is a surprise to you and how much of this did you know?
**Anirudh**: I mean yeah, I don't binge but then this is very surprising to see the numbers.
**Anand**: Okay. Surprising to see the numbers. And I think that is a meta-pattern that seems to be emerging. We kind of know a certain amount of this but not quite as starkly or as quantitatively. And that reinforces I guess some of what we know but also deepens some of what we didn't know. Fascinating. Fascinating.

Please continue sharing. And if you've got one insight, get another one.

But here are three picks that Claude has for me:

1. **Radial Maps:** Create a central topic in the middle. Major themes as picture segments radiating outside. Blah blah blah. And a prompt that I can give is "A radial diagram with a central circle labeled topic and blah..." Okay. That sounds something that is worth trying. It'll look nice.
2. **Zettelkasten Network:** This is the most different paradigm. Network diagram with rectangular card boxes containing single concepts connected by labeled arrows showing relationships like a neural network or knowledge graph. Okay. Yeah. Kind of.
3. **Journey Maps:** Horizontal journey map with six to eight illustrated box sequences. Wavy emotional curve line. Oh, this is interesting. Okay.

So let's try these. What we'll do is apart from the sketch note, redraw as... and a journey map with storyboards. Yeah. I'm just going to take the whole thing and put it out here.

Okay. That is one. But let's take a look at the sketch note of the talk that I had delivered for this clinical trials thinking.

"AI in Clinical Data Management... Big Insights from the Talk... The pace and the shift... old ways... new programming language... Yeah." Okay. For someone who is in the clinical data management space, this would be a useful summary. But what it's missing, and I clearly did not ask for it, is the engagement factor. I said give me a sketch note, it gave me the average sketch note. Let's apply style transfer to this sketch note. And what we'll do is... or if not style transfer, at least have it deliver... "Redraw the earlier sketch note in... I'm just going to take the same original prompt. Copy it. Open Gemini. And ask it... Generate a sketch note that is funny and engaging. Most important: funny and engaging."

Now why am I iterating that? Because unlike the GPT class of models, I have not yet tested how faithfully Gemini 3 or NanoBanana Pro follow instructions. With Claude I tend to do this at least once with capitals if not twice. With GPT, starting GPT 4.1 series, I stopped doing it with the GPT 4.1 class of models because when I do that, it takes those instructions so literally that sometimes even when it is not possible, it won't stop. Even when I have given it contradictory instructions, it will somehow find a crazy solution that is some utter obscure edge case that meets every single instruction that I provide. So these days my instruction sequence has changed to from "Do this" to "Where convenient consider doing this." Very gentle. And it will very seriously consider and say "I gave it very serious thought, I have considered it deeply, and for these 17 reasons I believe that it is not the appropriate thing to do and therefore I'm taking..." Thank god. That's how crazy... Okay.

Once I... okay. Now. Now I learned something. It did all the thinking but it did not draw the image. So it looks like I do have to take the thinking step versus drawing step in two separate parts. It's not able to automatically combine those.

In the meantime, Claude failed on my bank statement analysis. After all of that work. Yeah, it just gave up. So let's... let's try again. See where it goes. This will probably not even finish in this session. But hold on. I said NanoBanana. Did it not... This is a sketch note? Okay. Generate the sketch note as an image. Keep it funny and engaging. Fine. So clearly I know that Gemini needs a little more work on the instruction following side of things. GPT models would not make this kind of a mistake.

But on the style side of things, we missed this. This is a useful one. Something that I could even use in corporate decks I think. Which is showing a timeline.

What we're finding is that NotebookLM is now able to generate slides purely through images. And the slides are pretty good. Now you may say, hold on, that defeats my purpose because I want to be able to edit the slides. That is true. But if you do not want to edit the slides, then using NanoBanana Pro for slide generation is now increasingly a possibility.

Any other insights? Can I please share the prompt for the sketch note exercise? Sure. It's actually just... I will share the prompt with my... transcript. "Find useful surprising... and draw it as a sketch note." Let me share that as a reply to this. So you can try this out. And yeah, do try the sketch note prompt. But it's really nothing more than "Draw a sketch note." And remember, part of it is a discovery of new styles. And style applies to image prompts as well. So that can make a big difference.

I'm going to close this. Close this. Keep this for posterity. And yeah. Okay. This is supposedly a funnier one. "Clinical Data Genie and the 40 cent PhD intern. Holy cow it's fast intro. You know Chat GPT but you're missing the pace. It's crazy town. Traditional pharma speed is abacus. And okay. This is a child that is growing. Okay. This is a clever analogy. Yeah. And it hits the mark. Billion dollar boredom versus two cent solution. Old method, half a million to two million dollars of following a 68 page guideline, the soul crushing reading. And now it's done before your coffee cools for a few cents. True. So treat it like a genie, an employee or a really eager intern who doesn't need to sleep."

Yeah. That is so true. I read... so you saw the Hacker News scraper that I showed as a bookmarklet right? So there was a thread that Simon Willison had posted about Brenda. There was a TikTok video about Brenda who's this random employee in the finance department who is the only one who makes the Excel sheets in the entire company work. And because of AI she gets fired, what's going to happen? It's an imaginary video. But there was a thousand comment... at least 500 comment thread on it. Which I passed to Claude and said now give it to me as a Malcolm Gladwell story. It was fascinating to see. But one of the comments that it surfaced there and it said here's something that a lot of people reflect... resonate with is this:

The value that a human is providing is partly the accountability, partly the quality assurance that they provide, partly the flexibility that they can do things beyond a system can provide etc. But it comes at a significant cost. That the manager has to accept this quality level in and in return be polite to that person. Take whatever idiosyncrasies that person has. Cannot slave drive them partly because of regulation, partly because of human decency. All of which are problems that vanish with an AI. So if I don't really need that level of quality... which happens in several cases because I as a manager half the time don't want a solution, I just want to pass on the problem to somebody else. When I get an email, I don't want to necessarily give a thoughtful reply to that email. I just want to get it out of my inbox. Not in every case, but enough times that's what I want to do. So I copy it, I put it into ChatGPT, whatever reply comes, I don't bother reading it, I send it back. It's out. Somebody else's problem. And there are many such Brendas whose function is merely to take the problem away from my plate and put it into somebody's plate. In which case I would rather have someone who has no idiosyncrasies, who can work 24 hours a day, whom I can scream at and they will say nothing. So much better. And on top of that they are cheaper. No brainer. Of course I'll fire my employees.

So what people are missing when they say "Oh AI is going to take over my work" is that AI is going to take over the problem and pain you were causing as well. Just that your manager didn't value the work as much as they undervalued the pain. That's also a factor to keep in mind. And so on. It's definitely a funny and interesting one. So we will come back to this later.

Any others? Okay. Nishant was added. Cool. All right. We are at 4:46. The plan was to go on till 6:00 and we can offline do that. But my aim is to wrap this up in the next 15 minutes plus some spillover. So if there are any stories please do add. But I do want to... in case I miss summarizing towards the end, I want to make sure that I'm capturing some of the summaries.

One, at least some of you have learned something that surprised you based on your own data. Now it doesn't get more insightful than that. That is powerful. You also tried it with a few prompts, perhaps based on what I shared, perhaps based on your own. But either way that prompt led you at least on this dataset to something that was insightful. Tweak it. But remember to apply as you tweak it, the principle of **post-mortem**. And the post-mortem principle is simply that when you don't get what you want, you say "I didn't get what I wanted. This is roughly what I wanted or this is what you did wrong. Why did this happen? And what should I tell you next time so that it doesn't happen?" Then tell it to do that. Of course, you can just continue prompting, but the post-mortem is for you to learn.

If you don't like the way it wrote it—whether it's the way the insights were crafted, whether it's the way the narration happened, whether it's the way the chart was created, whatever—use **style transfer**. And what that will allow you to do is pick the style of someone you liked, whoever it is, and apply that. And it's trained on all kinds of styles. So it'll be able to pick it up.

If you are not even able to get to the data in the first place, then if you are able to see it, you should be able to get to it. And that's where the techniques around **CDP** and the use of Playwright and the likes come in.

**Style transfer, sorry. Did you share the style transfer kind of prompt that you did in the chat?**
I believe I did, but let's find out. Did I share the style transfer prompt? There was a... okay. Maybe not. So let me share the exact prompt... set of prompts, my catalog really. `styles.md`. This is my style catalog. Now please keep in mind that this is _my_ style catalog. Meaning two things:

1. It's a long list, 99% of which I never use. It's just there for the future.
2. Second, it is _mine_. You may have no interest in any of these. But you get the idea.

**Jayashree**: You are able to get a fairly neat sketch for a transcript. Classroom that you put it... Please do share. We want to see it.

Okay. So that's the meta-lesson. Now. Let me go on to a couple of other things which are fairly easy to do and you can process this in any way you want. But it's also something that you have likely seen.

Let's start with **NanoBanana**. NanoBanana is a **thinking model**. And because it's a thinking model, it can do a fair bit of pre-processing beforehand and give you a result. So, here's what I'm going to do. I'm going to take a transcript. In fact, let me take the transcript of my last workshop. And I'm going to give it to NanoBanana. And say get me insight, but there is a small twist which you will see in a few seconds.

First let's take a look at my talks. My last talk was probably an SCDM keynote which is transcribed here. So this is a fairly long-ish transcript. I think this has... yeah, okay, only one part. The prompt that I'm going to use again is something that I will dictate into ChatGPT.

"Here is the transcript of a talk that I had delivered at the Clinical Data Management Society's annual conference. Find big useful and surprising insights from this talk. And give it to me as a **sketch note**."

Now you've seen sketch notes. Nice artistic representations, but the thing about sketch notes is they often depict what happened during a talk. I don't want what happened during the talk, I want the insights coming out of that. Let's give it to NanoBanana. With thinking mode enabled. This thinks. It really thinks a lot. And then draws the picture. Not saying that the picture is letter perfect. There's 1% percent, half a percent, maybe even less... [errors].

- _[Anand mentions uploading or pasting the script]_ *

I pasted the script below. And yeah, somewhere here. It's a long piece of input. But once I ask it to deliver the insights as a sketch note, hopefully eventually it will also generate the image.

Ah, did I... I clicked the stop button which I didn't intend to. Let me... Or okay, fine. Even now, let me just generate a sketch note. Let it continue. But my guess is that's what it would have done even otherwise. And if it doesn't, big deal. We have two parts. One where we just have the conversation with it, get the insight, and then have it generate the sketch note.

Now, sketch note is a popular format and easy to understand format. But is it the only format? And if everybody starts creating sketch notes then what is the big deal? right? So, let's ask Claude the following question.

**Prompt**: "I'm creating sketch notes from documents and talk transcripts which is useful. But sketch notes are not a very unusual format. I mean it's almost become commonplace. I want some other formats which are less popular but still as engaging and as effective as a sketch note in communicating the bulk of the information that has happened at an event like a talk. Can you review and identify half a dozen such and pick two or three formats for me that I could use? Give it to me in a form that is concise and passable to an image model like NanoBanana."

That way I know that I just have to copy-paste. And this helps. Trust me, being able to tell an LLM just give it to me in a copy-pastable way saves you so much of review time. And I'm going to change just one word here. Instead of "review," I'm going to say "research" and ask Claude to do it.

Why not ask ChatGPT to do it? I find Claude to be, when generating prompts, Claude tends to give the most succinct prompts. ChatGPT tends to give the most verbose prompts. ChatGPT's opinion is: I am smart, the other model is likely to be dumb, I will over-specify. Claude's opinion is: People are roughly equally smart, I will share it in a way that I will understand, and that works well for me because that's also less review time for me. Gemini is closer to Claude in that sense, so I use it as an alternative. But if I wanted to give a prompt to a weaker model, let's say I want to give a prompt to Claude 4 Haiku or GPT 4.1 Mini, then I would go to ChatGPT and say now you give me the prompt because you can be prescriptive, you can use your intelligence which distills that into something a weaker agent can execute just step by step. Let that happen.

**Data Storytelling**
There was another use case I wanted to talk about which is **Data Storytelling**.
This is from a few years ago. One of our salespeople was trying to reactivate some old contacts. We had about 700 contacts in our Hubspot to whom we had sent no proposals. Dead assets. And we had about 13 deals worth about $28 million where there was no activity. And I asked the salesperson, "Why aren't you following up?" He said, "I don't know what to write."

Now, if you don't know what to write, you give them a dashboard. If _they_ don't know what they want, you generate a data story.

So, treating the data as a story is a powerful technique. I took the Hubspot data and said, "Write a story about this contact." And it wrote a story. "Once upon a time there was a contact named [Name]..." And it gives you a perspective on what happened with that contact. Now, you can automate this.

**Agent Harness**
There is one last meta-pattern I want to talk about called the **Agent Harness**.
The idea is: **The agent writes and runs and improves the code that does it.**
So save yourself tokens by reusing the scripts... but also increasing reliability by having the agent run it.

So, **practice**. Whatever you remember, practice. Try as much as you can, share what you can.
Thank you for joining in.

---
marp: true
title: Vibe Coding
author: Anand S
url: https://sanand0.github.io/talks/2025-10-23-vibe-coding/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
---

[sheet]: https://docs.google.com/spreadsheets/d/1a4xBlO1snYLT5Bzi71SG5Wqel2j6yoAM3CAw0UNWCRg/edit?usp=sharing

<style>
  transcript {
    display: none;
  }

  blockquote {
    font-style: italic;
  }

</style>

# Vibe Coding

[Straive](https://straive.com/) · 23 Sep 2025, 4:00 pm SGT · Remote
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Video](https://drive.google.com/file/d/1NmuSHWAotDHo5uDvi8s5V8sUJHWRDhvo/view?usp=sharing) · [Transcript](https://github.com/sanand0/talks/tree/main/2025-10-23-vibe-coding) · [Spreadsheet](https://docs.google.com/spreadsheets/d/1a4xBlO1snYLT5Bzi71SG5Wqel2j6yoAM3CAw0UNWCRg/edit?gid=0#gid=0)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-10-23-vibe-coding/)

---

## Vibe coding gets results by letting the agent work

- **Vibe coding focuses on outcomes, not code artifacts**; the agent writes code as a means to an end.
- Treat “coding” as orchestrating steps and letting tools act.
- Judge success by job done, not elegance of implementation.
- This mindset lowers fear and speeds experimentation.

<transcript>

This is a workshop on vibe coding. What is vibe coding? Vibe coding is where you are coding but without even looking at the code. **The point is to get the job done.** By the way, an LLM will write code. You don't care about the code itself as an artifact. You are getting a job done, and by the way, it's coding.

</transcript>

---

## Choose Codex via LLM Foundry to keep setup simple and auditable

- Codex is a coding agent chosen for **easy install and solid quality**.
- LLM Foundry acts as a unified gateway to models and logs.
- Auditability matters when code and data flow across tools.
- Cursor and Claude Code exist; we pick one path to reduce friction.

<transcript>

We will be using Codex for this. Codex is an LLM coding agent. There are several LLM coding agents. Cursor is a popular one, Claude Code is a popular one. I've picked Codex because I found it easy to integrate with LLM Foundry and also easy to install and use compared to some of the alternatives, and also of very good quality.

</transcript>

---

## Track progress live so everyone moves together

- Mixed audience? **Use a shared Google Sheet** to track install status and wins.
- Call out blockers in the sheet to triage quickly.
- Keep talking minimal; let participants do the work.
- Use chat for questions so issues don’t derail flow.
- References: [Progress sheet](https://docs.google.com/spreadsheets/d/1a4xBlO1snYLT5Bzi71SG5Wqel2j6yoAM3CAw0UNWCRg/edit?gid=0#gid=0)

<transcript>

Why via LLM Foundry? Because we want to make sure that our code, our data, all of this stays auditable. And LLM Foundry is our gateway to all APIs.

Now, this session is meant for developers and non-developers alike, even though it's supposedly a coding session. I'm not going to be doing much of the work. You are going to be actually doing all of the work. I will broadly be talking. But to make sure that we progress steadily and I know who is being left behind, who is able to progress forward, we will be using a Google Sheet that is in the invite to track progress as we go along.

</transcript>

---

## Install the basics and open a working folder

- Install VS Code, Codex, and Python; then **File → Open Folder** so tools can act.
- Use provided videos and config to set API tokens.
- If Microsoft Store fails, capture the error for IT.
- Share blockers in the sheet so patterns emerge.
- References: [Codex+LLM Foundry tutorial](https://sanand0.github.io/tutorials/codex-llmfoundry/)

<transcript>

I will briefly share my screen, or at least this tab, and talk you through the sheet. So firstly, in case anyone does not have a link to the sheet, I will put it in the chat window. And I encourage you to go to this sheet and fill out your name if it is not there. If it is there, then against your name, mention whether you have Visual Studio Code, Codex, and Python installed. If you're not clear about what those are, I will be walking you through those in a minute. I see that many of you have already filled this in.

Firstly, sorry, that apart, this invite, who all did it go to? It went to, firstly, a set of people who were invited by their managers, and then to the GenAI newsgroup. So you may have seen it from one of these two sources, or somebody may have forwarded this to you. In which case, you may not have much of a context on what we are going to do. Doesn't matter. None of us have a context on what we will get out of it, other than we are going to explore LLM coding agents.

Since we have a large audience and it's going to be difficult to maybe answer each person's question verbally, my request is, please type any questions that you have or any comments that you have in the chat window. And we will use that. I mean, I'll be periodically looking at that.

Now, the first thing that we, I want to make sure that everyone is able to do, is install the prerequisites. I'm going to assume that you have already installed the prerequisites. That was part of the email that I sent, but we will spend maybe about 10 minutes just making sure that you at least know where the prerequisites can be installed from. And I will do that by sharing my screen.

First, I've pinged the link to the prerequisites, and I've also opened that link on my screen. We will need to set up Codex, which is the coding agent, on Visual Studio Code in whatever operating system you have. I mentioned Windows 11 because I've written the instructions for Windows 11, but whatever version of Windows you have, or if you have Mac or Linux, you should still be able to set those up, though the instructions here don't quite cover that. And how to set it up using LLM Foundry.

So, you would need to install VS Code. This is a video that can guide you through the process. Then you have to install the Codex extension. Again, there is a video here that explains the process. You will have to click on the Codex icon, type in some dummy API key initially, and later on, replace it by opening this configuration file with this text and setting your environment variable to include the LLM Foundry API, the LLM Foundry token. And after that, when you restart Visual Studio Code, you will be able to in VS Code, at the bottom left, be able to type anything, like ChatGPT, and it will start answering, but with the additional ability to write code, and especially writing Python code, which, if you install by following this video, the shorter approach is you just go to the Windows search bar and type Python. It will take you to Microsoft Store and start installing.

A number of you have already been able to do all of this. So let me switch back to the status tab and see who has, who's at what stage of implementation on this. Sorry, I'm just going to share this tab again. Yeah, that was shared. Okay, the majority of you have a green against most of these. That is good news. Let's go through a few. And yeah, so here's my request: for anyone who has a red, please fill in the problems that you're facing when either installing Codex or Python or Visual Studio Code. That will help me maybe give you some guidance, but in any case, since the majority are a yes, we'll still go ahead, and you can watch the recording.

And got you, Kavita. You're saying it says contact your system administrator for more information. I will put that in against your note.

Add a folder. Okay. Anoop, thanks for filling in that problem. One of the things that you need to do in VS Code is File > Open Folder and open a folder. Then it will start working. Just quickly seeing if there are... okay, unable to open Microsoft Store in Sudheesh's case. I'm not sure how to fix that, Sudheesh. Maybe IT will be able to help. And Raja, unable to continue from configure LLM Foundry. Okay, I'm sure that will be easy to fix, but we can take that offline. Just going to come back to this, and we will take a look at this in a few minutes.

Sushant mentioned that you're not able to install Python. Please mention what problem that, oh, okay, Sushant, you're... is it according to the Google Sheet, you've installed Python?

**Question**: Sorry, actually, yeah, actually I installed the VS Code and I can type, write Python code in the VS Code.

**Answer**: Got you. So this is actually a no, understood. And just mention what problem you are facing in the installation in the Google Sheet. What I will be doing is collating all the problems in the Google Sheet, and if there's a common pattern that maybe IT can help with, then we'll see how we can resolve that.

</transcript>

---

## Crowdsource tasks first to make practice relevant

- Ask everyone to add real tasks they care about.
- Seeing peers’ ideas sparks better experiments.
- Aim for **20+ concrete tasks** to cover diverse workflows.
- Use the list to pick live demos that matter.

<transcript>

Okay, that was step one. Now, step two, for everyone, how about we take a minute and write what tasks you would like to try out today? You may not have much of a context. That's okay. If there is any anything that you're doing at work that requires you to use an LLM, or that you think you might benefit from using an LLM, let's try automating that today.

What have I seen people use it for? All kinds of things. Yesterday, someone created a set of PowerPoint presentations using ESG data from a particular folder. Someone else was working on data extraction, that is automatically going to websites, pulling data from there, and saving it. Someone else was using it to analyze Excel sheets and create a summary. In fact, we are running a project out of it. One of our clients is using it to answer questions from a big bunch of PDF files. Another team is using it to create images. Yet another team is using it to analyze images. Some people are using it to automate web tasks, that is, going into, for example, the Google Console, Google Cloud Console, and changing specific settings for multiple users. Some people are using it to improve their own system, that is, make system settings changes so that their systems get optimized. I've used it to run a security scan of my website to see what are all the security issues that can possibly come up. We can consider organizing files in our computer. We can consider sorting through our emails or calendars. We can consider building models—and when I say models, I mean data science models, machine learning models. Some people have created data visualizations and data stories out of it. We could consider generating code for our projects, which coding agents are really good for.

And what I shared are about a dozen examples of what I've seen people already using Codex for. So, please go ahead, put in in the, in column F of the sheet that you see on the screen, like others are doing, some examples of what you would like to use this for.

What I'm going to do is, once we have maybe about 20 entries—there are 80 of you, so even if 25% fill in the entries, we will have 20 entries—I'm going to copy those, send it to Gemini, and ask it for interesting things that we could do based on that.

So let's do a quick count. How many entries do we have so far? We have seven entries. I'm looking at the bottom right where the count says eight, so excluding the heading, that's seven entries so far. We have eight entries. Nine entries. Please do keep in mind that when you think and put in something here, that you will get an idea of what to try during this workshop. If you don't have an idea, that's okay. You can follow along with whoever. I'll be inviting people from here to try this out. But if you can think of something, you will have an advantage. Then you will be able to learn in a way that is contextualized to what you are doing.

Okay, we have a dozen entries so far. That's good. 13, 13, okay, 12, 13, 14 entries, 15 entries, 16 entries, 17 entries, 18 entries. Waiting for two more, and then we will send it to Gemini for input. Still at 18 entries. 19 entries. We just need one more. Okay. So now that we have 20 entries, but please do continue filling this in. I'll do a second round.

</transcript>

---

## Pick three practice tasks and use voice prompting

- Use an LLM to shortlist interesting tasks from the sheet.
- Voice prompting **lets you think aloud** and add richer context.
- Start with PDF→XML, browser automation, and Excel analysis.
- Color-code selections so the room can follow.

<transcript>

Now, what I'm going to do is take all of these, copy them, and paste that in another window which I will share. So I had already put in the details of this workshop. So I'm going to say, "The audience has suggested a series of additional tasks that they would like to try out. Select three of these that would be an interesting test of capability and useful for this workshop." Or some such thing. And here is the list. Let's run it.

Now, you'll note a couple of things. One, I was using voice prompting, and I prefer voice prompting because it saves me time. But also, when voice prompting, I find that I'm able to think aloud, explain more to the LLM than when typing. I don't even have to do this in English. When I was in Vietnam, we were speaking to—well, I wasn't, but our colleagues were speaking to it in Vietnamese, and it worked just fine. And that can be pretty useful. The second is that I'm using Gemini instead of LLM Foundry because we have more, well, lower-cost access to more powerful models out here.

So, the three that it suggested—and not that these are necessarily the best or anything, it just picked three—publishing or BPO task. The second is an AI agent task for browser automation. And a data science task to Excel files which contain 50 columns. Did somebody actually put in all of these details? Excel... Okay, somebody said, Venkateshwaran said data analysis from an Excel file. Okay. Let's take that as one that we will run. I'm trying to color this cell in something else that is more prominent. Yeah, let's take this one.

The second that it suggested was a browser automation. Okay, that's Nagasushanth. And let's highlight that as well. And the first that it suggested was a PDF or HTML to XML conversion. PDF, DOC, HTML, I guess that was from Snehapriya. I will mark that in green as well. Let's see. Yeah, okay. Let's start, Snehapriya, with you as the first item.

I'll stop sharing my screen. Could you share your screen and open Codex? We will try this out.

**Question**: Yeah.

**Answer**: Yeah, you're unmuted, we can hear you. That is great. Please do share your screen. And my request is for others to try and follow along, do something similar. The idea is to learn in new ways.

**Question**: Sorry, by the way, do people call you Sneha? Do they call you Priya?

**Answer**: Anything is fine.

**Question**: Sure, what do your friends normally call you?

**Answer**: Sneha.

**Answer**: Sneha. Got you. Perfect. So let's do this, Sneha. You have Codex installed. Do you have any folder where you have a PDF, Word Doc, or HTML file that you want to convert?

**Question**: Yeah, I have.

**Answer**: Great. That folder is open? Is that the folder you are currently on?

**Question**: I have to add some files.

**Answer**: Okay, your voice is a little low. Would you be able to be louder? We can hear you, just not loudly enough. You're on mute. That's perfectly fine. We'll give you a minute.

**Question**: Yeah, can you hear me now?

**Answer**: Yes, this is slightly better. Sorry, what did you say last?

**Question**: I was about to keep some files in this folder.

**Answer**: Sure, please add those files, and we'll see how Codex might be able to tackle that. So my invitation to everyone is, let's all try putting a bunch of PDF, Word, or HTML files into a folder and see how we might convert them into Excel. It doesn't matter what files. It doesn't matter if you don't have a specific need for it. Initially, in this workshop, what we're trying is to learn the capabilities, what works, what doesn't work, etc. So just toss a bunch of HTML, PDF, and/or Word documents into a folder and open that folder. In case you are not sure how to go about doing that, in Visual Studio Code, go to the File menu, Open Folder. That's it.

</transcript>

---

## Convert PDFs to XML and weigh full-access risks

- “Agent full access” **acts faster but carries risk**; limited mode is safer.
- Ask it to find files and run conversions on its own.
- Expect retries: agents will fix their own scripts.
- Add a sheet column to mark who produced XML.

<transcript>

Okay, now we have a bunch of files. So, could you go to the Codex icon, Sneha, and click on the new chat icon on the top? That's the one, yes. So the reason I'm proposing a new chat is, that way, it won't get confused with anything else that we may have said earlier.

Okay, so now why don't you go ahead and type a prompt, but don't submit. Ask it to do whatever you want it to do. Just wait before submitting.

</transcript>

---

## Clear requests turn you into the “analyst” the agent needs

- Vague asks (“PDF to XML”) confuse both humans and agents.
- **Specify outputs, granularity, and structure** (e.g., text vs. JATS/NLM).
- Treat prompts as requirements; iterate toward clarity.
- Everyone is a business analyst now—practice makes this natural.

<transcript>

While Sneha is typing, just a broad instruction here: the prompt makes a big difference to the output. But nobody has really mastered what prompt we should give in what context. So for now, we'll just try whatever comes to our mind. It's okay. Over time, we will learn.

So I'm going to zoom in a bit on the screen because the font is a little small. "I want to convert a PDF to XML output. Please give some Python code." Okay. Let's make a small change to this, Sneha. Remove the second sentence. Yeah, let it write code, let it not write code, who cares? It will figure it out.

Now, we're saying, "I want to convert a PDF to XML output." We haven't told it what PDF. We haven't told it what XML. Doesn't matter. Why don't you go ahead and submit?

Let's see what it does. It's thinking. Now, one thing you may notice is that at the bottom, Sneha has "agent full access" enabled. Sneha, could you click on that "agent full access" at the bottom? Yeah, that icon has three options. **Agent full access means it won't ask you for permission; it will happily go ahead and run code on your machine.** That can be good because you are not bothered, meaning it will not bother you, but it can be bad because we don't know what code it is running, and that code might delete some files that you didn't want it to delete. So for now, decide whether you want to go the risky route but convenient route, or less risky route but less convenient route. I toggle between these depending on my mood, really, or depending on the question.

Okay. Now you'll notice that it's doing a bunch of things. The whole point of vibe coding is to not worry about what it's doing, how it's doing, etc., but rather to see if it is able to get to a good output.

**Question**: Anand, just to interrupt, sorry. I just ran the same prompt, but in my case, within a fraction of a second, it gave a Python snippet, a code snippet. It does not go through all the steps.

**Answer**: Interesting. And then what we'll do, Sushant, is maybe look at your screen in a few minutes. We'll get there shortly.

**Question**: Raja's question was, "Shall we follow the same settings for agent full access?"

**Answer**: For now, yeah, go ahead, Raja. If your machine gets deleted, you can blame me later. But very unlikely. Okay, thank you.

**Answer**: Okay. So what it's done is it's created a Python file. But at the end, notice that the last comment it says is, "If you share the PDF path, I can run the conversion now." Okay. So, Sneha, why don't you tell it, "Run it on all my PDFs in this..." Don't, don't, don't give it... **the whole point of vibe coding is to do as little work as possible.** Tell it, "Find the PDFs and run it." Let it do the work. While it's doing it, Sushant, could you share your screen, please?

**Question**: Yeah, I think now it is happening. I actually gave the full access to the agent. Now it is doing the same. Previously, I, the access was limited. That's why it just threw me a Python code.

**Answer**: Interesting. Let's take a look at the screen.

**Question**: Yes, yes, yes.

**Answer**: So you will notice that tradeoff, and this is a possible approach you could use. You could start with agent access and then switch over to full access if it's bothering you too much or it's not doing the stuff. Yeah.

**Question**: Yeah, initially I gave this one, but without full agent access, it threw me this output, this snippet, code snippet. But then I again I gave it with full agent access, then it started going all the steps. Thinking.

**Answer**: Nice. Perfect. Now the good part here is it is able to correct itself. It will run, it will find errors, it will change the code, and get to the output. But as far as this workshop is concerned, we are less worried about the code and more worried about the output. So if it gets there, good. If not, we will tell it to do something different.

**Question**: Has anyone managed to complete a script and gotten some XML output? If so, just unmute and speak or put a "yes" in the chat window.

**Answer**: Okay, well, now Sushant, you have one. But here's a request to everyone: if you, once you have, okay, Sneha, you got a "yes" as well. Once you have gotten an XML, please put in a "yes" in the... Actually, let me add a column here in the Excel sheet: "Generated XML," and on that, you could please fill in a "yes" or a "no."

**Question**: Sushant, could you open the XML file that it generated for you?

**Answer**: Yes. The one below that, yes. Okay, "Bank of New York Annual Report 2023." Yeah, if you click on it, it might open. If not, it may have generated it somewhere in that file.

**Question**: It is not opening actually.

**Answer**: Got you. Could you increase the size of Visual Studio Code so that we see it in the full window? Yeah. Now on the top left, there is... or okay, can you go to File > Open? Or yeah, click that, either way is fine. Open File. Uhm, not here. All right. Can you click "Cancel"? And just ask it, "Where did you create this file?" And once you have it, please open it. In the meantime, Sneha, could you share your screen and let's see if we can see your output.

**Question**: After that, Souvik, you are getting an error starting conversation. We will take a look at your error very soon. Anupama, your hand is raised.

**Answer**: Yeah, Anand, I have not given the full access. I am in the agent mode right now. It is asking me to do a lot of installations, PDFMiner.six and everything. So where are all these installations being done and so I had that question.

**Question**: I also have that question. I have no idea. Why don't you ask it?

**Answer**: Okay, sure, I'll do that. Thank you.

**Answer**: So, let's take a look, Sneha, at the XML file that you just had open. Okay. What are your observations about this? Is this what you wanted?

**Question**: No, because my PDF file contains some content text.

**Answer**: Hmm. Got you. So what do you want in the XML?

**Question**: So I want some text which is present in my PDF.

**Answer**: Got you. Then as a next step, why don't you say, "I want some text that is present in my PDF"? Just continue that conversation and let's see where it goes.

Now, in the meantime, Souvik, could you share your screen? We'll see if we can resolve the error.

While Souvik is bringing the screen up, I'll make an observation. When we give a prompt like, "Convert this PDF to XML," I, as a programmer, don't know what I'm supposed to do. It doesn't know any better. If we take it a step further and say, "Give me the text," give the text what, as one big chunk? Should we structure it in some way? What am I supposed to do? Again, I, as a programmer, don't know what to do.

**There is, in fact, literally a profession of people whose job is to explain to programmers what we want.** We call them business analysts, sometimes they play the role of project managers, whatever. But effectively, all of you now have changed your roles to also be analysts. Meaning, earlier, you would tell somebody, "This is my requirement," and they would translate it, figure it out, explain it to a programmer, whatever. **Now you are having to do that to a somewhat dumb programmer.** An LLM doesn't really understand you well. Soon, you will pick up the skill, just like everyone picked up Excel. We will also pick this up, and it's largely practice.

Cool. Souvik, I can see your screen. Let's take a look at what Codex says. Just type "hi." Or anything, yeah, for that matter. Okay, still running. Fine. Can you open, can you click on the `config.toml` that you have open? That looks fine. Could you open the environment settings? You had opened the environment settings using the Start menu.

**Question**: Yes.

**Answer**: Yeah, could you open that?

**Question**: I got the problem. Yes.

**Answer**: Yeah. And it does not look like the LLM Foundry environment variable is set. So click on "New." Type `LLM_FOUNDRY_TOKEN` in caps. No underscore between LLM and Foundry. LLM Foundry is one word. After that, there is an underscore, token. LLM_FOUNDRY_TOKEN.

**Question**: Not there.

**Answer**: No, here in variable name, LLM Foundry. After that, type an underscore, and then a token. Yes. Now, copy your LLM Foundry token as the variable value. You'll find that...

**Question**: Yeah, I think the problem was, I, the token was not saved or something. That's why it is not running maybe, because I saved this one.

**Answer**: Got you.

**Question**: Anyway, I got the problem. Yeah, thank you.

**Answer**: Perfect. No worries.

**Answer**: Okay. So, I'll just check the chat to see if anyone else has... okay, we have Venkatesh and Nitin generating XML files. Venkateshwaran, maybe you could share your screen and let's take a look at the XML that you've generated. And I also see on the Google Sheet that Srini has generated an Excel, Praveen has generated an XML, and cool, at least a couple of people there. No issues, Venkateshwaran, we can maybe go on to Nitin. We'll skip you for a bit. Ganesh, maybe you could share your screen?

**Question**: Yes, Anand. I'll do that.

**Answer**: Let's take a look at the XML.

**Question**: Yeah.

**Answer**: What we'll do next is make some tweaks to it, see how it improves.

**Question**: This is the XML I got, where it is taken the character bounding boxes. It has taken the bounding box for each character.

**Answer**: Perfect. What do you want, though?

**Question**: It should be converted into an NLM XML or any other, like, JATS XML like that, so where the paragraphs will be like, you know, like paragraphs, and math will be in MathML like that. Those kind of conversions we require.

**Answer**: Great. Why don't you ask it to do one of those? And let's see how it works.

**Question**: I already done it. Okay, here I had done it. Convert PDF to NLM XML. But it is giving the things and then it is asking me to integrate any of these particular things, okay? Grobid or Sermat to get scholarly structure like that.

**Answer**: Okay, sure. Which of these are, if you want it to do all of these, you can ask it to do all of these also.

**Question**: Okay. So integrate like that, I can type?

**Answer**: Yeah, why not?

**Answer**: One of the things I find powerful is **the model itself giving us guidance on what to do.** In this case, it is giving us ideas. And that sort of a thing can be pretty useful. So the next step that we will take is, how do we encourage certain kinds of behaviors? So we will come to that.

Okay, Raghav, you mentioned in your case, you got the XML without it asking you which PDF file. So maybe it found some PDF files somewhere. Why don't you ask it, "Where did you get the PDF file?"

**Question**: Vinod, your question was how to install Python. Could you share your screen? And we'll try two things. One, we will ask it how to install Python. And then, let's see if we face any issues with that. Are you in a position to share screens, Vinod?

**Answer**: Okay, I guess your screen is coming up. You may want to unmute yourself.

**Question**: Yes.

**Answer**: Perfect. Sure. Now, let's go to Visual Studio Code, please. Great. And you can open Codex and ask it, "How to install Python?" Just enter. Could you make this, make this full screen and also press Control and Plus to increase the font size a little? Control and Plus will increase the font size. Yeah, great. That makes it more readable.

The beauty of this is that Codex can be used just like you're using Gemini or LLM Foundry. The only difference is that it is additionally writing code to do whatever you want it to do. Now just scroll up a little bit. It's saying blah blah blah, download something, blah blah blah.

</transcript>

---

## Use `AGENTS.md` (and skills) to steer behavior

- Put **standing instructions in `AGENTS.md`** (e.g., “write readable, short code”).
- Test it with a fun rule (“always answer in poetry”).
- Keep per-folder behaviors and reusable “skills” files.
- History view helps jump between past chats.

<transcript>

So why don't we do one thing? At the bottom, there are two icons just below "Auto-context." There is one icon. There's "Auto-context," a little bit to the right. Just below that, "Auto-context," huh. The one, there's another icon just to the right of that. Click on that. Go to "Agent Full Access." Just continue, yeah. Now, why don't you say, you know, "Install Python for me and test it."

This is another pattern that you might want to consider. If you want, but...

**Question**: It will require admin rights, right?

**Answer**: Maybe, let's see. See, these things are smart enough. Let them figure out if it needs admin rights and come back. If it finds a way of installing it that does not require admin rights, why not? Go ahead, enter. And that is another major unlearning that I find that I have to do. My assumption is that certain things it can do, certain things it cannot do. But the reality is I have no idea what it can and cannot do. It itself doesn't know what it can and cannot do. So, usually, I just let it figure it out. And if it cannot, fine.

**The vibe coding approach is where you don't try too hard.** If it works, very good. Do more of it. If it doesn't work, doesn't matter. Let it go. So, looks like it's setting up Python. I'm shocked, actually. I did not expect this to happen. But okay. And just because it set up Python doesn't mean it will actually work. Let's see. And it's chosen Python 3.12. Fair enough.

In the meantime, Sneha has a comment: "When I ask for the context of the PDF, it is saving the content in a text file." Interesting. So yes, this is a behavior we should comment on. See, when we type something on the left, it has the ability to give us the answer in that box. It also has the ability to create files and do other things. So sometimes it decides whether it will create a file which has the information we need, which is good because that information is persisted for later and we come back, we can still refer to it. Or it will just display it on the left, which is somewhat—I wouldn't say temporary, but yeah, somewhat temporary.

We can tell it, "Don't create any file, just give me the answer." Or, "I want you to put the answer in a file so that I can refer to it later." Either option is absolutely fine.

Now, you'll notice that it says "2 out of 5 tasks completed." So, let's do this. Vinod, could you click on that "2 out of 5 tasks completed" on the left side? So, what it does is it plans. Step one, I'm going to do this. Step two, I'm going to do this. Step three, I'm going to do this, and so on. It's like a checklist for it, and using a checklist is helpful.

Like this, there are a bunch of things that we can also give it as guidance. These guidances are called instructions. And we can store the instructions in whichever folder we are working in, in a file called `agents.md`.

So let us test that out. Vinod, right now you are working in some folder, right? Which folder have you opened? You're on mute by the way, so we can't hear you, but that's okay. We can see you progressing. Sorry. No worries. Alright. Great. Visual Studio Code working. Great.

So, in this folder, what we will do is create a new file and we will give it some instructions. Now, how do we do that? Let's go back to Visual Studio Code. Click on File > New. New file. And yeah, click on text file.

Okay. Now, let us just test out something. What shall we ask it to do? Okay. Give it some weird instruction. **"Always answer in poetry."** Now, save this as `agents.md`. File, save. Agents. And just... No, no, this is not the folder. Just make sure you're saving it in the same folder that you had earlier loaded.

Kavita, I see your question. How do you navigate the first chat in Codex? In a few minutes, I'll ask you to share your screen and we'll go through that together. Agents, plural. A-G-E-N-T-S. No, no. A-G... The spelling is A-G-E-N-T-S dot M-D. Yeah, save.

Okay. So now it has done two things. It's installed Python on the left, which is great, and it's now going to answer in poetry. Let's try this. Could you click on the new chat icon that is on in the Codex window? No, it's on the top. "How to install Python?" Yeah, just to the right of that, there's a new chat. Yeah.

Next, what shall we ask it for? "Who is Donald Trump?" Some random question. Let's see what it answers. I'm just trying to test if it can answer in poetry. So now, in theory, it should read your `agents.md` and the logic is, whichever folder you are working in, it will look for a file called `agents.md` in that folder. And it will follow those instructions. You can give it a variety of instructions.

Okay, yeah. It is answering in poetry. "**A polarizing figure, rallies loud, campaigns' long run.**" Oh, okay, the whole thing is poetry. Fine. Good.

So, here's the next thing that I will request. And I'm going to put this on... I'll share my screen briefly before we go to Kavita's screen. I'm going to add one more column here, which is "Follows agents.md". And you can just put in a "yes" or "no" against this. "Follows agents.md". I did not want it to hyperlink. Remove the hyperlink. And expand this a bit.

So, for those who have been able to generate an XML, please put in a "yes" in this column. Because based on whether you've been able to or not been able to, I'll follow up with support. If you've been able to create an `agents.md` and it's following the instructions in `agents.md`, please put a "yes." Again, I will follow up based on whether you have been able to do this or not.

In the meantime, Kavita, could you share your screen, please? Let's take a look at the navigation question you posted.

**Question**: Yeah, in one chat I have created a command for converting a PDF into PowerPoint summary. In another chat window I have asked Python to install. It's completed. Now I... yes. ... You said how do you navigate the first chat in Codex? What first chat?

**Question**: See, here, initially I have created a chat and then given a task to convert the PDF into summary. Then I opened a new chat and given this Python installation.

**Answer**: Got it. So how do you go back to the first chat is your question. Got it. Usually, there is a little left arrow next to Codex. Could you click on Codex? Yeah. Okay, yeah, click once again. Yeah. Okay. Now let's see. The words "install Python for me" is there, right? To the right of that, there is a "1" circling. Click on that "1". Okay. Now you see the history. You can go back to any of the previous ones. Thank you.

So, for others, please note, **you can see the history of all of your conversations** somewhere. Just dig around and you'll find it eventually. Which means that you have the ability to, like on ChatGPT or Gemini, keep a series of conversations. I haven't used the history feature much, so I'm not sure if it is folder-specific or global or how it works. Play around, you should be able to figure that out.

Now, we are at almost 50 minutes into the workshop and what we have are about 27 ideas. Let me just quickly take stock from my screen. We have about 90-odd people who have Visual Studio Code installed, and some subset of whom... filter column with just "yes"... We have about 80-odd people who have Codex working. For those who have not yet been able to, we have the issues that you're facing and we'll get back in case you haven't been able to resolve it and figure out what's not working.

Next, we have about 26 ideas. Now that you've seen this generating XML, you probably had some more ideas. Please put in your ideas. It will help in two ways. I'll learn as to what can be done and go offline, do some experiments. You can see each other's ideas and say, "Oh, that sounds interesting. I have a need for it. Let me try it out." The more ideas you put in here, the more we'll be able to learn as a group.

Generating XML. If you have been able to generate an XML file from any source, and so far we have 15 people, please put in a "yes." That way we'll know that you have this ability. Others can reach out to you if they need help on that and you know whom to reach out to if you want to bounce off ideas or try different XML variations.

"Follow agents.md" is mostly for me to guide you in case you're having trouble with `agents.md`. Keep in mind that **`agents.md` is one of the most powerful ways of guiding the model**. I'm going to show you my `agents.md` and how I use it in a few minutes.

We will, in about maybe five, seven minutes, go on to one more use case, probably data analysis. Oh no, Venkatesh, you mentioned that you're not able to share your screen. So, let's instead go to Nagzshan's use case on automating a browser task, which sounds interesting. But before that, there are a couple of questions in the chat window. If anyone else has any questions, please put them on the chat window. We will take those up now and then move on.

**Question**: Question from Sushant. Do we need to install... sorry, Shantanu. Do we need to install PowerShell for running the script for PDF to XML?

**Answer**: Shantanu, if you're using Windows, PowerShell is already there and you don't need to install it. If you want to install something, you can ask it to install. If you don't know what it should install, **tell it to install whatever it needs. Let it figure it out.** The general answer to most questions can be figured out by asking it itself.

**Question**: Question from Arpit. Do we have a usage limit on Codex like we have a daily dollar limit on LLM Foundry?

**Answer**: Not yet. Maybe that will come up at some point. Currently, no. Sushant, your `agents.md` is not working. Got you. Maybe in a while, we will debug that. Shantanu says, "It's asking me to install." Please go ask it to install. Tell it, it should be able to install PowerShell by itself. Let's see if it does it.

**Question**: Raja has a question. I don't have an idea on follow `agents.md`.

**Answer**: What we just did a short while ago, Raja, was create an `agents.md` file. Let me share my screen in case others have the same question and guide you on this. In any case, I was planning to explain how `agents.md` works. On a related note, Anoop, to your question, how do you stop it from using `agents.md`? Change folders or delete the `agents.md`. That's all.

So, what is `agents.md`? **`agents.md` is a file that contains instructions telling Codex what it should do**. It's almost like every time you don't have to type the same instructions. You can give it a set of instructions in each folder. In this folder, let us say I always do PDF to XML conversions. So, do that. In another folder, I always analyze Excel files, and I do it in a certain way. In another folder, I always write Python code, I do it in a certain way. So what does my `agents.txt` look like? Or `agents.md`, sorry.

This is my `agents.md`. And this is a common `agents.md` that I've created for all folders. I'm not going to explain how to do that. You can figure it out. I say, "Keep... Write readable code." If it's writing code, I want to review it. And I put in this instruction and some details around how to write readable code. "Write short code." It keeps writing long code. I don't have time to review it. "Change existing code minimally," and so on.

I also have given it a list of tools that I have installed on my machine. So if it wants to do PDF parsing, it can use qpdf, it can use pandoc. If I need to copy files, it can use rclone. If I need to maybe, let's say, convert PDF to markdown, markdown is there. Image processing, ImageMagick is there. So this makes it pretty convenient. This apart, I've also created some additional files. I'm saying, "Read the relevant `skill.md` file." That is, I've created a bunch of other skills for you. Depending on what is relevant, read it. For example, there is a PDF skill which has comprehensive PDF manipulation toolkit for extracting text and tables, etc. Now, this in turn contains detailed instructions. I didn't write this, I'll come to where it came from. On how it can write... how it can read PDF files, what libraries can be used to merge PDF files, how it can split PDF files, extract metadata, rotate pages, and so on.

This is a concept that Claude, Anthropic, as part of Claude code, brought in a few days ago. **The concept is skills.** That is, you can give it instructions saying, "Here's how you do stuff. Depending on what you need to do, read the correct file." This is a somewhat advanced topic. I'm not going to go into the details of this. The important thing that I wanted to flag off is, you can give instructions in an `agents.md`, it will follow it every time, and you can even ask it to read other files as part of those instructions.

Next question.

**Question**: From Ujwal. How do you ensure data security and what all it has access to? Can we give access only to a certain folder?

**Answer**: Let me share the permissions that it has under different circumstances.

</transcript>

---

## Keep data scoped; use tests to cut hallucinations

- Chat/Agent modes restrict to the opened folder; full access goes wider.
- Short timeouts prevent infinite runs; agents **adjust plans** when slow.
- Add “write tests first” in `AGENTS.md` to verify results.
- When unsure about sensitivity, **generate code but run it yourself**.

<transcript>

**By default, it will access only the stuff that is in that folder** if it is in chat mode or agent mode. In agent mode, if it wants to access something outside that folder, it will ask you permissions explicitly. If you put it in agent full access, then it can access stuff outside that folder as well. So, from a data security perspective, keep it in agent mode if you want to limit access. If you are confident, go to agent full access.

**Question**: Question from Raghav. Is there a time limit for each task in Codex?

**Answer**: Yes, kind of. It times out each task after, I think, 10 seconds by default. But if it finds that the task stopped because of the timeout, it will either increase the timeout, or rewrite the task so that it will run faster, maybe on a sample, or do something else. So yes, there is a time out, which is good because then it won't wait forever for stuff to get done, but it also has the ability to change that time out.

**Question**: Ranjit asks, can we use `agents.md` to improve LLM output quality and gain better control over hallucinations?

**Answer**: **Yes, absolutely.** One of the things that you can do is ask it to double-check all its answers. You can... one of the things I have here, for instance, is, "Add failing tests first." If the test exists and write fast tests. That helps me because what it will do is read my instructions, write the tests that should pass, and keep writing code until those tests pass, which means that the chances of hallucinations are much lower. And this is one example, there are many ways in which we can do this.

**Question**: Uh, next question from Ujwal. The data stays within the Strive ecosystem, right? As it's connected to LLM Foundry.

**Answer**: The code that is being generated is currently being generated by the OpenAI models. So the code, at least, is going outside the Strive boundary. The data itself in its entirety is not going from your folder, but maybe some samples or snippets from that data is going. So if this is something that needs to be within the Strive ecosystem, if you're not really sure of what, of how Codex works, don't use Codex yet. If you know how exactly Codex works, that is, what data it will send, what data it will not send, then go ahead and use Codex. I don't know how we can switch to an OpenAI... okay, no, I do know how to switch. In the `config.toml`, there is a setting that we can modify. Instead of this base URL, we can choose a different base URL. So, I have not tested that out yet. I'm not going to test that in this workshop. Kujwal and anyone else who wants to use Codex within the Strive ecosystem and make sure that the data doesn't go outside of Strive's tenant, please drop me an email or let me put in a column here.

Need session on Strive tenant config for Codex. I will set up a separate session inviting whoever needs... No, actually, why am I bothering? I'll anyway send out instructions to everybody, but I'll create another file with the configuration and drop an email to everyone. So it's optional, this column. Ignore this, not a problem.

Okay, now that we have questions exhausted, let me stop sharing my screen, and we'll go on instead to Sushant, your screen please.

Yes. Okay. What task did you... you were saying maybe automate booking, ordering, etc. Any specific thing that you had in mind to automate?

**Question**: Are you asking me, Ananth? ... I am Sushant.

**Answer**: Oh, sorry, sorry. Naga Sushant, who had mentioned this. Sorry.

Yeah, I'll just share my screen. Yes, Naga. For... To avoid confusion, I'll call you Naga Sushant.

Yeah. So when I want... when I thought of that, I was thinking how we can actually read some data and then convert it into a table. Like we can scrape some contents from browsers and then convert into some data like tables.

**Answer**: Perfect. How comfortable are you coding?

I'm good. Yeah, I have experience using in-code.

**Answer**: Perfect. So what we are about to do is a slightly experimental and slightly advanced topic by which I mean that it may not work for you, and I mean you in plural, it may not work for everyone, but let's try it out. Could you open a terminal, command prompt, whatever?

Okay. So now, it turns out that we can automate the browser by using a debug terminal. I'm going to share my screen for a bit, partly because I don't know what exactly I should be telling you. So I'm going to experiment and then we will figure it out.

</transcript>

---

## Automate browsers safely with Chrome remote debugging

- Launch Chrome with remote debugging to let agents drive it.
- Use a separate user-data dir to sandbox activity.
- Point the agent to `localhost:9222` and describe goals.
- Start small: search, click, screenshot, and save artifacts.

```bash
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Temp"
```

<transcript>

So, let's use Gemini for this and ask it, "See, I know it's possible to open Chrome in a debug mode. For Windows, can you give me the command line instructions that I can use for that? And I believe that it will open a debugging port in port 9222. Can you... yeah, just explain the instructions?" 9222. Let's see.

Okay, it's taking a long time. I didn't realize it was going to think so much. Yeah, this is the command. I will, once it pastes it, I am going to paste a version of this command in the chat. I'm not going to put in the path, but yes.

So, let me stop sharing my screen. And Naga Sushant, could you share your screen again, please? Yeah. Now, the user data directory doesn't have to be that. You can put in anything. Just put in any temporary directory that you know exists.

For others who are watching, what we are going to do is start Chrome with debugging installed. What that means is Codex will be able to control Chrome. Let's see. Yeah, go ahead, go ahead. Enter. Okay, you'll have to find the path to Chrome. Do you know how to get the path to Chrome? Program Files maybe? Okay, oh yeah, local installations are also possible. No, it's quite... both are possible.

Google, okay, yeah. Chrome, application, okay, maybe? `chrome.exe`. Yes. So copy... type the full path to that. Okay, that also works. Run the same command. Yeah, you can press... yeah, enter.

So this has opened a new Chrome window. Okay, don't sign in, whatever you want. Either way is okay. All right. Now, try something. Go to `localhost:9222`. Localhost, the whole local host spelling including an 's'. Perfect. So it's working.

Now let's go to Codex and pass it the following instructions. I'm going to paste the instructions in the chat window. I have Chrome remote debugging running in `localhost:9222`. Okay. I've pasted a prefix. So Naga Sushant, could you copy from the chat, the last... yes, copy that. Paste it into Chrome and add more instructions... Sorry, paste it into Codex.

And yeah, yeah, go ahead. Type whatever you want. "Can you search the topic 'AI website traffic' and scrape the content and convert into any usable data? The data where I can see it using visualization." Okay, interesting. Go ahead, let's see how that works.

In the meantime, I'm also going to try something. Let me share my screen. I'm going to use the same prompt and see if I can automate something. Downloads. My downloads folder I'm going to create. "scrape something". Not quite. "scrape something".

What I've just done is opened Visual Studio Code in an empty folder. Why an empty folder? Just for cleanliness. And I am going to paste the same thing that I've put in the chat window here. I have Chrome blah, blah, blah. Now, what shall we ask it to do? Open my inbox. My Gmail inbox at... okay, it should already be open. Read the first email and type a draft reply to it and save the draft. Let's see. I have no idea if it can or cannot do this, but if it is working, then I should be able to see it work somewhere in one of these windows. Yeah, that's my Gmail. In theory, it should send a draft reply to this junk email. I'll move that. "Oh, I'm sorry, I cannot help with that." Oh, okay, fine. Security policy and all that.

Let's try something simpler. Um, open... let's see, Darwinbox. Uh, Darwinbox, Strive... No, I can't log into Darwinbox because I may not have access from here. Let's have it go to `llmfoundry.strive.com`. `llmfoundry.strive.com`. Is it working now? Um, no, it's down. So let's pick a site that requires login. LinkedIn. What's LinkedIn for? Open... and let's look at my invites, actually. This is something that I have tried in the past, so it should work now. Open... and look at the LinkedIn invites I have received. Of the first, of the 10 most, or let's say 30 most recent, how many people are from the IT industry and how many are outside of it? Save the details in `invites.md`. And run it.

Again, no idea if this is going to work. I have tried it in the past and it worked, but who knows? It's largely hit and miss. In the meantime, Naga Sushant, how's yours going?

**Answer**: It has taken up five tasks and the first task one is still going on. That is basically installing dependencies.

**Answer**: Installing dependencies. Okay. Maybe... I didn't expect it to install dependencies. Let's see.

I have it in my full access mode.

**Answer**: Ah, fair enough. Just cool. In the meantime, I'm just curious, has anyone... is anyone else even trying this? The remote debugging mode? Okay, let me know if you are.

**Question**: Mohammed Hussein saying I am exploring coding with LLM using Cline on VS Code for any LLM I choose. It tells you if you if it supports prompt caching or not. How does prompt caching help in token usage reduction? Is there a way to know if the prompt I'm entering will use caching and reduce token usage or not?

**Answer**: This thing is still running. It's doing some work with my browser. So let it continue. Just going to keep an eye out for it. But to give you a sense of what prompt caching is, out here, it's making a series of requests, one after another. These requests are all going to LLM Foundry one after another. Some of these will have a long history. Let's in fact take a look on LLM Foundry history. LLM Foundry history. Not mine, but overall. Any of these using a GPT-5 model? Next. Okay, it could be but... No, this was not multi... GPT-5. That's look for GPT-5 Codex in particular.

Okay. So here are a bunch of requests. Let's take Divyansha Shree's request. Does this have multiple? Yeah, this... Fine. Let's take a closer look at this request. Not that. Okay.

So first, what Codex did was send some environment context. This is the computer it's running on, this is a policy, blah, blah, blah. And here is the prompt: "I have two PDFs in the current directory, I want to convert them to XML." That is the user request. And then Codex replied with some reasoning, thinking. It said, "I'm going to inspect the current directory to confirm the PDF files." And then it ran that and then it thought a little more. It called some other function with PowerShell, it did all of these things.

So now, one after another, it kept sending a request, getting a response, sending a request, getting a response, and so on. This conversation keeps going on and on and it is constantly adding to itself. Such a long conversation can consume a lot of tokens, but what prompt caching does is, anything that is only appended to, that is if let us say up to this line, at some point all of this conversation has already gone to whatever model, in this case GPT-5 Codex, and we are only adding this new stuff, then the earlier tokens are cached for some duration, maybe up to one hour. So within one hour if we continue that conversation, then **the previous tokens have a 90% cost discount**, automatically. So huge cost discount. 90% cost discount, and it is automatic. We don't have to do anything. And this is captured in the log, in the usage somewhere.

Okay, the request will not contain the usage. The response will contain the usage. So this is the response. And let's take a look at the usage. Not quite. Huh, the usage, I saw that somewhere here.

Okay. So the input tokens were 30,000 and none of it was cached. Okay. For whatever reason, for this particular request, none of them were cached. But if they were cached, and I've seen that happen quite often, if the response was using cached tokens, then that response will have a lot less cost. Let me show you an example of what one of those looks like. And you can see your logs when you go to your Codex settings, open `config.toml`. In the same directory, there is "sessions". Under that sessions, if you go to 2025, 10, what is today's date? 23rd. There are a bunch of logs. If you open one of those logs, right at the bottom, it will show the usage. So in my case, the input tokens were 600,000, 6 lakh tokens. But the cached tokens were 5,62,000. So I'm actually being charged with a 90% discount for these 5 lakh tokens. And only the remaining 1 lakh tokens have an incremental cost, at least so far, and it is... the conversation is continuing.

That is one part of the answer to your question, Mohammad, which is how does prompt caching help? Now, which LLMs supports prompt caching or which models? If you are using the OpenAI models, then **all of the OpenAI models support prompt caching**. If you are not using an OpenAI model and one of the others, many of them also support prompt caching. A rough rule of thumb is, unless you're using some reasonably obscure model, it supports prompt caching, and therefore it will reduce token usage.

Okay, so you'll have noticed that my code is still running and it's trying to do something with LinkedIn. And in some window, it's... yeah, probably reading all of my LinkedIn stuff and figuring out what. Let's give it another maybe five minutes and see if it's gotten anywhere. But Naga Sushant, have you gotten anywhere with your prompt?

**Answer**: Yes, Ananth. So what it did is, if you can see my screen, Yes. it has searched for 'AI website traffic'. Okay. And it has automatically opened all these tabs. Wow, okay. And then subsequently, I got a HTML report. Basically, my first... I got a CSV file. This is the CSV file that it gave. Okay. And this is the script that it had run actually.

**Answer**: Wow. Okay. So what you've effectively done is reproduced a portion of what is called computer use. And this is becoming a popular topic. That is, you have a coding agent or an agent use your computer.

Now there are two powerful things that we can do from this point on. One, you can ask it to take screenshots on the way. For example, why don't you give it a prompt saying, "Take a screenshot of one of these pages and save it as a PNG file and analyze that screenshot." What it will do is take a screenshot, send it to Codex, analyze it, and do stuff with it on the fly. That is powerful, which means that it can get a visual sense of what the page contains.

The second thing that it can do is, you can ask it, "See, you scraped all of this stuff and created a Python program. **Give me the Python program in a reusable way so that I can run it tomorrow without taking Codex's help.**" That is powerful because what we're doing is not going to the program first. We're not saying, "Give me the program first." We're saying, "Get the job done first." And then, if the job is good enough, then we will ask it for the program. And when we run that program, we don't need to use the LLM again. No API cost therefore.

</transcript>

---

## Reuse wins: extract the final script after the agent succeeds

- After a good run, **ask for a self-contained script** to reuse without the agent.
- Capture screenshots or HTML while scraping to aid review.
- Add a “Scraped a website?” column to share successes.
- Expect multiple techniques: Playwright, HTML parsing, APIs.

<transcript>

So, this is a very powerful technique. I strongly encourage you to try it out. I am conscious that this means a little bit of programming to use the browser. But **that's what agents are for**. In theory, you should be able to tell it, "Launch Chrome in debug mode." And if it says, "Where is Chrome?" tell it, "You figure out where Chrome is. You automatically launch it in debug mode. You figure out how to scrape sites." Let's see if it works.

I would strongly urge people, try this out. Have it scrape a site which requires a login and see how it performs, see where it works, where it doesn't work. I'm going to share my screen and add this as a column that you could try out. Mine is almost done, by the way, so I'm going to stop that in a bit, but where's the other window? Okay, I think I've lost… Vibe Coding Workshop. Yeah, I found the tab. I'm going to add a column asking if you were able to scrape a website.

So, any of you who have managed to use Codex to scrape a website in any shape or form, please put in a yes. The reason I'm keen on this one is, like I said, it's a very powerful capability. And if this is something that you've been able to do, please do show off here. But also, it'll help people reach out to you to understand the way in which you went about it.

The number of ways in which a coding agent can do this is vast. It could install a command-line tool and just scrape the HTML. It could use your browser and scrape it. It could install a completely new tool and figure it out. It could use a third-party API which is probably free that it discovered and use that to fetch that information. Even within these, the way in which it does it, for example, does it directly use WebSockets? Does it use Playwright? All of these are very exciting possibilities, and we can learn from each other which of these techniques worked in your environment, which of these techniques have advantages, disadvantages, etc.

So, that is okay, and we already have at least one yes. Okay, which is you, Sushant, great. Others, if you have been able to do this, please put in a yes, or a no, for that matter, if you've tried it and it's not working. Please put in a yes or a no. On agents.md, okay, we have about 20 people. About 70% of it have said, of the people have said yes, and generating XML, we have about 20-odd yeses. Okay, that is good to know.

We have another just under half an hour. I'll probably keep it to about 15 minutes to explore maybe one more use case. Any volunteers? Anyone says, "Can we please try mine?" Anyone wants to share their screens and try something that you're finding interesting or hard?

**Question**: Sugu, this is interesting. Create a config for Amazon GuardRails to allow for a chat window. Sorry, Sugu, what was that?

**Answer**: Yeah, so I mean, we keep getting, or at least the destructive tester in me always gives random questions to any chat windows or any chat agents that we define. Obviously, we don't have any guardrails set up. Most recent example is when we had a traffic analysis implementation. I went there and asked something like, "How do I build something?" some construction question I asked. And the chat window, I mean, the agent responded to that question as well. So, what if we were to limit the responses to a particular use case alone? Because that was only a traffic use case.

**Question**: Interesting. So that's how I defined that.

**Answer**: Got you. Let me reframe that to say, would it be able to figure out whether Amazon has guardrails that specifically allow for certain kinds of configuration, and if so, where do we find them and explore that? Which the browser agent kind of situation might be able to solve. I would peg my confidence at 10% that it can solve it today, but non-zero, and I'm sure it will improve in the future. What we could do is let it loose on AWS and say, "Go through AWS, take screenshots, read the page, whatever, and see what you can figure out."

Let's see. In the meantime, I'm just trying to see if my coding agent has... Okay, it's created a scrape invites and it's... okay. So it's gone through my LinkedIn invites and it's found that there are 19 people in the IT industry and 11 people outside the IT industry with, oh, okay, all the details of the people. And yeah, I can confirm that this is actually from my LinkedIn invites. So, that worked.

Any volunteers for the next iteration? We haven't done Excel. Souvik, are you okay for us to play around with Excel? Are you in a position to share screens?

**Question**: Yeah, sure.

**Answer**: Great. Why don't you share your screen?

**Question**: Yeah, just give me one moment.

**Answer**: No problem. So what we'll do next is see how Codex can handle Excel files. There are multiple ways in which it might do it. One possibility is it can directly play around with Excel using PowerShell and manipulate. Another possibility is it could use Python to write code and manipulate. Maybe there are other options as well, other tools that it could install. So, part of this is to see in Souvik's environment what it decides to do.

</transcript>

---

## Create and analyze Excel data the lightweight way

- If real data is sensitive, have the agent **create a dummy Excel** first.
- Ask for summaries, visuals, and a brief PowerPoint.
- Tweak charts yourself; let the agent draft the heavy lifting.
- Log successes so others can replicate.

<transcript>

Okay, your screen is visible, Souvik. Great. Do you, what Excel file do you have and what do you want to do with it?

**Question**: Yes, can you repeat again?

**Answer**: What Excel file do you have and what do you want to do with it?

**Question**: Yeah, let me think about, so there are some Excel files. So basically what I want to do is I want to, you know, like summarize the data that is present in Excel and then, you know, create a report maybe in a PowerPoint, something like that.

**Answer**: Nice. Let's pick an Excel file.

**Question**: Yeah, sure.

**Answer**: And this is a very, very common and useful use case. I would very strongly urge everyone, please pick an Excel file and play around with it using Codex. Have Codex do something. Put it in a folder, open that folder in VS Code, ask Codex some question based on that Excel file, or give it a task based on that Excel file, anything.

**Question**: Yeah, let me think. I'm thinking of some Excel file because some Excel files I may not be able to share here.

**Answer**: Sure.

**Question**: So, let me just give me some time, okay?

**Answer**: Let me tell you something different. Why don't you, in a new empty folder, ask it to create a dummy Excel file?

**Question**: Okay, that will be fine. Yeah.

**Answer**: Yeah. And then we'll work on it. New chat. Always start a new chat. Okay, I'll read that out for those for whom the font is small. Create a new Excel file. Go on.

**Question**: Go on, go on. Go where?

**Answer**: Create a new Excel file to do what? Or which contains what?

**Question**: Okay. Let's say the age and height, like very basic Excel file maybe.

**Answer**: Then, in that case, if it's that generic, let me suggest a prompt. **Create a new Excel file which contains some interesting data that I can do analysis on.** Let it figure it out.

In the meantime, does anyone have an Excel file that they would like to analyze? If so, please unmute yourself or comment in the chat window. And I do see a comment from Kavita that says, "Created a comment, created a summary sheet with visuals using Excel using Codex." Oh, nice Kavita. That is fantastic. Actually, could you share your screen? We'd love to see that.

**Question**: Will share it.

**Answer**: In the meantime, Raja has a comment, "Please share the recording along with the tutorials on Codex. Your configuration is running fine but will go through the recording and verify." Yeah, absolutely. The recording will anyway be, will reach everyone who's joined this session, I think. Thank you. Yeah, your screen is visible Kavita.

**Question**: Yes. So this is a sheet I have created using Codex. The daily summary report what we extract from the mail box. I use certain pivot which is in a number table format. I just want to explore what it suggests with the visual. It has taken the base data and then created the summary.

**Answer**: Wow.

**Question**: Maybe I have to tweak here and there to make it more clear in the form of presentation. I've just given few inputs. It just taken the summary from the existing base file and the source data from here and this is created by Codex.

</transcript>

---

## Read session logs to see what actually happened

- Codex keeps per-day session logs under its config folder.
- Zip and share logs to learn what tools it installed.
- Logs help debug odd behaviors and estimate usage.
- Use logs to teach future workshops.

<transcript>

**Answer**: Wow. You know, I would love to see the logs for this.

**Question**: Okay.

**Answer**: So could you go to Visual Studio Code? And this is something that will help everyone understand how you can analyze the process that it followed. Now, in the settings icon, the gear icon, where you had a config.toml setting, yeah, could you click on that and go to Codex settings and open config.toml? Just below that, there's open config.toml. Click on it. Yeah, open config.toml. Perfect. That's the one.

Now, go to File, Open, the menu File, Open. Open File. Yeah. It will open, it will show you the directory which contains the config.toml. Under that, there is a sessions. What you could do is maybe just right-click on that sessions.

**Question**: Okay.

**Answer**: And create compressed whatever folder. Create zip file. No, that's not there. Oh, I see. Maybe it doesn't appear here. Okay, then let's do one thing. Let's cancel this and instead open that folder. So could you go to your home directory in the list of files?

**Question**: Open file?

**Answer**: No, not open file. Could you open Windows Explorer where you normally see the folders? Go to your home directory and go to under that .codex.

**Question**: Oh, okay.

**Answer**: Not in OneDrive. It will be in this PC, yeah. Users maybe. Yeah, Users. Ah, okay. I don't think that's... Ah yeah, there it is. Okay, .codex, yes. Now right-click on sessions. You should be able to create a zip file. Show more option... compress to, yeah, compress to a zip file.

So that will have the session logs. If you could just mail this to me, I'd love to analyze it to see what are all the tools that it installed in order to do this and what are the kinds of commands that it run.

**Question**: Sure.

**Answer**: You can do that offline. That would be great. I'm just doing a quick check to see if anyone else has a yes against process Excel file. Not yet, okay. But scrape a website, okay we have three people who've been able to scrape a website. Okay, two people. Got it. Hari, I see you mentioned a no. What issues were you facing?

**Question**: I have a bad internet connection.

**Answer**: Oh, okay. That's a different kind of issue then. No worries. Fine. Okay. We've covered, I think, about all of the basic stuff that we wanted to cover. Let's maybe do 5, 10 minutes of Q&A. Any questions from anyone? And you're welcome to unmute yourself, you're welcome to put it in the chat window.

</transcript>

---

## Agents are a big leap; learn to delegate in small steps

- Agents feel like the **jump from chat to action**; start simple.
- Delegate tasks, not technologies; guide like a patient manager.
- Expect failures; switch models or break work into steps.
- Keep sensitive work inside your tenant when available.

<transcript>

While you do that, what I wanted to do was summarize what I'm hoping you will take away from this session. The creation of LLMs was a step ahead in that it can answer almost any question. This year, people have termed the year of agents. And we are close to the end of the year. **What you are now using is almost as big a leap forward from the creation of chatbots as since then.** Meaning it's that big a leap because you're moving from being able to answer anything to being able to do anything, to perform actions on your behalf. And that's exactly what agents are capable of.

Like two years ago when we barely knew anything about how to get the most out of these models, we barely know how to get the most out of agents. We're all learning. Luckily, like last time, when LLM Foundry gave us access to these agents, the combination of Codex and LLM Foundry is giving us access to, sorry, LLM Foundry gave us access to models. Codex and LLM Foundry are giving us access to agents. And I will soon share with you the instructions on how to set it up so that it can stay within the Strive tenant, which means that you will have safe access, at least from a model perspective, to this. Do try it. I think the important thing now is to learn how to delegate to these by learning their strengths and weaknesses and learning how to communicate with them.

</transcript>

---

## Plan for limits, formatting pain, and try alternatives

- Some Word/PDF translations fail; **shrink scope or split files**.
- WSL + Windows apps can need port tweaks; try native first.
- Ask agents to propose a plan.md before acting.
- Share wins and misses so the group levels up.

<transcript>

**Question**: A question from Venkateshwaran: is it possible to create code that can translate a Word document that has other language content to English?

**Answer**: I believe so. Do try it Venkateshwaran. The answer to "is it possible" is almost certainly yes. Let's try it out. But specifically for this one, I think the coding agents will do a good job. There are two parts to this. One, can you do a few, can you process a few documents? And then it will probably take the Word document, convert it to text, if it is too large, it will split it up. But in all likelihood, it will find that the document is not too large and then it will convert a new Word document. Then we will say, "Hold on, I want you to preserve the formatting." Now, let's ask it and maybe it will take portion by portion, translate just that portion with context and do something. Who knows? The thing is, we don't know what tasks are complex, what tasks are easy. So, like guiding a child, we may have to say, "Okay, try this." That didn't work. Okay, now I'll break it up in parts for you. Or if we get stuck, ask it, "Why did you get stuck? What can I do to help you?" In other words, all of you have now become managers, whether you like it or not. And it's worth trying.

**Question**: A question from Aniketh: if I run Codex inside WSL, WSL is Windows Subsystem for Linux, it is unable to access Chrome running on the host Windows machine. We'll need to install on VS Code and try again.

**Answer**: Yes Aniketh, I have not tried Codex with WSL. Exposing some ports from that should be possible. If you find that you're able to get this working, please do share in the GenAI News group what you found and what works, what doesn't work please.

**Question**: A question from Souvik: how safe are we to upload sensitive information related to company, like an Excel file to an analysis using Codex?

**Answer**: **When in doubt, play it safe Souvik.** Use one of the safe models, for which I will send instructions. What is safe is having Codex generate the code. So one possibility is don't keep your Excel file in that folder. Just tell it to generate the code. You run the code. If it doesn't work, tell it, "Here is the error, fix it," etc. That is safe. But if you actually want it to get some guidance by giving it that Excel file, then use one of the safe models which we will shortly enable.

**Question**: A question from Sudheesh: how accurate are the results? How can we know if there are any hallucinations that have skewed the accuracy?

**Answer**: Same approach as with models directly, Sudheesh. We have to test it. The good part with agents, like with chatbots, is that we can ask it to cross-verify. We can have another model check the results. We can ask it to write test cases to verify this. There are a bunch of ways, very similar to how we know how accurate a human's results are and how can we know if the human is hallucinating or has skewed the results.

**Question**: Raja's comment is: currently I'm using Gemini 2.5 Pro for some of my tasks to generate Python. Sometimes it's a challenge to get the revised code. Hope I can try with Codex and see better performance.

**Answer**: This is a perfect use case for Codex, Raja. Given a piece of code, you can tell it, "Modify it." Not only modify it, you can tell it, "Run it, find the errors, fix it automatically, and keep doing it until you get it right." And it will do the task. That's what agents are for.

**Question**: Comment from Venkateshwaran: I tried doing it with one page but it ended up with translation failed and the formatting is not retained.

**Answer**: Yes, please do break down that task. Anytime it finds something complicated or unclear, it will mess it up. So we can go step by step, maybe give it a small Word document, and then say, "I want you to modify only a few words in this, but with the formatting retained." That could be one approach. Trying out different approaches will eventually stabilize or help us understand what works, what doesn't work. An important thing is, beyond a point, give up. Today it is not possible. **But these models are constantly improving. Sometimes all we have to do is wait three months and something that is not possible today starts becoming possible.** Instead of breaking our head against a few specific problems, we can explore what is easy and go in that direction.

**Question**: Comment from Aniketh: in my other experience working with Codex, what I find helpful is to ask it to generate a plan of action in a markdown file before acting and review the plan before asking it to execute.

**Answer**: Yes, that is an excellent approach in general. We can ask it, "How are you going to do it?" Correct that plan if required and then ask it to do it. Maybe try alternate plans, maybe ask another model to generate the plans. Keep in mind that you can move back and forth between, let's say, LLM Foundry, Gemini, Codex. You have multiple tools available to you and these tools can be used to create different, a fusion of different kinds of things.

Okay, that concludes the questions that were there in the chat. Let me share my screen again and we'll do a quick stocktake. Okay, so we have about, almost 90 people who probably joined in for this session. Almost a dozen of you are having problems with installation. I will go through this and see if any IT support is required and reach out on that. We have a bunch of, we have about 20-odd tasks that people have wanted to try out. Let's spend the last few minutes on this.

Could you please go back to this sheet? I will ping this sheet on the chat. And please fill out or extend your existing list on what are some of the things, now that we've gone through this workshop, that you would like to try out. I'm hoping that at least half of this group, that is close to 40 people, will have at least one thing that you want to try out. Why is that important? Because while you are thinking about this, that is when you will have a certain momentum and say, "Okay, here's something specific that I could try out. Maybe it will work, maybe it won't work." Without an idea of what to try, the chance that you will actually try something is pretty low. And in any case, by seeing others' ideas as you scroll through, you may get new ideas yourself. So, do scroll through this. See what tasks others are trying out. And when something strikes you, fill it in, that way others can learn from what you may want to try as well. Please do fill out what tasks you would like to try with Vibe Coding. Okay, see a bunch of people starting to type. That is good. And of course, in the meantime, if anyone has any questions, you're welcome to put that in the chat window. But I'll just wait for this count to start nudging upwards.

**Question**: A question from Naga Sushanth: did you try executing a click action on the browser? Let us say accepting the invites that you got.

**Answer**: Yes, I tried clicking, I've tried scrolling, I have, and Nitin who's on this call has probably tried more. Nitin, if you are still on, are you able to unmute and share your experience in scraping Salesforce, was it? Yeah, I think Salesforce.

**Question**: Yeah, of course, Anand. For that I need to use my personal laptop. So give me just one minute, I'll share my screen.

**Answer**: Yes. Please do watch this. This was a fascinating exercise where Nitin was using his system to extract information from, I think it was Imagine Learning's Salesforce website. And keeping in mind that A, it is a site that requires login. B, it is a somewhat old Web 2.0 site, not particularly easy to navigate. But using exactly the same technique that we tried now.

Let me know when you're ready, Nitin. Just unmute yourself when you're ready. But in the meantime, Ranjit has a question. "Trying to access a few websites and extracting leadership information but getting the error, 'I cannot fetch or browse from this environment because outbound network access is disabled.'" Ranjit, that is a classic sandboxing problem. In agents, enable full access. You remember that little icon at the bottom where it says "Chat," "Agents," "Agents Full Access"? Enable "Agents Full Access." That is when it will have outbound network access.

**Question**: Okay Anand, thank you.

**Answer**: Cool. Okay, the count has nudged up to 30. Thank you, those who filled it out. For those who have not yet started filling it out, please give it a shot. Just put in some ideas on what you would want to try out while we wait for Nitin to share his experience scraping Salesforce.

**Question**: Yeah, I'm ready.

**Answer**: I'll stop presenting. You can start. So I have one instance of a Salesforce with which I want to extract the data for a particular code ID for a particular profile. So here is the page for which I need to extract the data. So that, so I just went to the Codex and write some prompt that I have one Chrome debug session.

**Question**: Could you show the prompt? Just one moment. Yeah. So the prompt was something like that. I need, I need to give one URL. This is the Amazon URL, but I put out the Salesforce instance URL in place of it and then some extract the data for the particular code I need.

**Answer**: And ChatGPT has given you, sorry, could you go back there? Not just that one prompt, but it's also given you an additional prompt. Could you go back to ChatGPT? I just wanted to point out on the browser.

**Question**: Yeah, so I was searching for some more use cases on this.

**Answer**: Ah, so A, how to collect headings from news articles, how to... Okay. This is another thing. If we don't know what we can do with Codex, ask a model, "What can I do with Codex?" And it gives us ideas. Sure. Back to you, Nitin.

**Question**: At the end, I was able to scrape the data from the for a particular code. Wow. That is in the, in this. Okay. Now I am trying to extract the hovering element. When we hover on particular values on the website, then we are getting some hovering values also. So currently I am working on that in this window.

**Answer**: Ah, okay. But it's empty, I guess, but...

**Question**: We need to re-authenticate again.

**Answer**: Understood. No worries. Cool. So we are pretty much at the end of the session. You can stop sharing screens, Nitin. So, but we still haven't gotten to the 40 people filling in your use cases that I was hoping to. Please give it a shot. But we will wrap up now.

In short, **please try Codex. Please try using it actively. Please share this with other people.** When you find something, let people know, "I tried this, this worked. This didn't work." Both kinds of sharing will enable everyone. This is very new technology. So, just awareness will help. Knowing what's working, what's not working will help.

We will probably have a few follow-up workshops, but I suspect that from now on, the majority of the information sharing will happen more through informal channels, emails, groups, that sort of a thing. Keep it going. At some point, I'm sure that the usage quotas, limits, whatever, will start getting applied. So you have a window until usage cost becomes high that IT says, "Oh, we have to put some kind of a reasonable limit. We'll have to put project-based budgeting and stuff like that." But until then, you have access to play around with it. Do give it a shot.

All the best. Thanks for attending. Have a good day, everyone. Bye.

</transcript>

---

# Vibe Coding

[Straive](https://straive.com/) · 23 Sep 2025, 4:00 pm SGT · Remote
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Video](https://drive.google.com/file/d/1NmuSHWAotDHo5uDvi8s5V8sUJHWRDhvo/view?usp=sharing) · [Transcript](https://github.com/sanand0/talks/tree/main/2025-10-23-vibe-coding) · [Spreadsheet](https://docs.google.com/spreadsheets/d/1a4xBlO1snYLT5Bzi71SG5Wqel2j6yoAM3CAw0UNWCRg/edit?gid=0#gid=0)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-10-23-vibe-coding/)

---

## Quiz

1. Why can “agent full access” be both helpful and risky in a workshop setting?
2. What specific details make a “PDF to XML” prompt actionable?
3. How does `AGENTS.md` change agent behavior across folders?
4. When would you extract a reusable script from an agent-run?
5. What simple steps improve safety when automating a logged-in website?

---

## Counterpoints (alternative views)

<small>

- **Vibe coding focus**: Some teams require code quality and traceability first; inner-loop TDD can be faster than post-hoc cleanup.
- **Audit via gateways**: Gateways like LLM Foundry add latency and cost; direct model endpoints can be simpler for prototypes.
- **Scraping may be banned**: Prefer official APIs to avoid account risk. ([LinkedIn][6])
- **Remote debugging** is unsafe. Try **headless Playwright** ([Chrome][2])
- **Skills/AGENTS.md**: Central skills can drift from reality; schedule audits or CI checks for stale instructions. ([Claude Docs][4])
- **Prompt caching economics**: Discounts vary by provider and deployment; **don’t assume 90%**; check your billing dashboards. ([OpenAI][5])
- **PowerShell installs**: Windows includes PowerShell, but **PowerShell 7** requires install; scripts may behave differently across versions. ([Microsoft Learn][1])

</small>

---

## Feedback (speaker improvements)

1. Frame “agent full access” with a 30-second threat model and a quick safety checklist.
2. Show a **before/after** of a vague vs. precise prompt to teach “analyst” habits.
3. Demo `AGENTS.md` with two contrasting folders to cement the concept.
4. Close the loop: extract a reusable script live and run it without the agent.
5. Add a 3-minute “terms check” slide reminding people about site automation policies.

[1]: https://learn.microsoft.com/en-us/powershell/scripting/what-is-windows-powershell?view=powershell-7.5&utm_source=chatgpt.com "What is Windows PowerShell?"
[2]: https://developer.chrome.com/docs/devtools/remote-debugging/local-server?utm_source=chatgpt.com "Access local servers and Chrome instances with port forwarding"
[3]: https://www.linkedin.com/help/linkedin/answer/a1341387?utm_source=chatgpt.com "Prohibited software and extensions | LinkedIn Help"
[4]: https://docs.claude.com/en/docs/claude-code/skills?utm_source=chatgpt.com "Agent Skills"
[5]: https://openai.com/index/api-prompt-caching/?utm_source=chatgpt.com "Prompt Caching in the API - OpenAI"
[6]: https://www.linkedin.com/legal/user-agreement?utm_source=chatgpt.com "User Agreement"

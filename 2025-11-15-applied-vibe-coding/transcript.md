Okay, let's dive in. Just reconfirming, is my screen visible to everyone?

**Question**: Yes.

**Answer**: Okay, great. So this is a workshop on vibe coding. That means a couple of things. A, because it's a workshop, you will be doing stuff. B, because it's on vibe coding, you will be coding without necessarily needing to know how to code.

Vibe coding was a term coined by Andrej Karpathy. And in fact, it'd be good to give you a feel for what he actually said. He put out a post. Right, I'm trying to see if I can locate the original X.com post. Okay, maybe not, but I should be able to find it at least from, yeah.

**Question**: Will it be shared later?

**Answer**: I actually have no idea. I am recording my copy. You should probably record yours, but I do see a bunch of people recording. It says this meeting is recording, so at least it's being recorded. The first part, will it be shared? I don't know. We'll try.

So Andrej Karpathy shared a tweet where he said, "There's a new kind of coding that I call vibe coding, where you fully give into the vibes, embrace experimentations and forget that the code even exists." And this, I think, is the crux of vibe coding. The point is you are not trying to write code, you are trying to get some work done. By the way, you are using code to get the job done. Which means whether you look at the code, don't look at the code, whether you know how to code, don't know how to code, doesn't matter. It's just a tool. It's almost like saying, I am getting the question answered by some search engine. Could be Google, could be Bing. It's going to look at some reference source, or maybe I'm going to get an intern to find the answer to my question. The point is I am answering my question. The mechanism doesn't matter.

**This is different from AI coding where we are using an AI coding agent to write code, and what we want is the code. In vibe coding, what you want is not the code. The code is just a by-product.**

Keeping this in mind, let's dive in. This workshop has a few slides, and the slides are mostly basic material that I'll be using to outline this talk. The link to this is available from github.com/. Let me just paste this link in the chat window. Yeah, the link in the chat is where you will find the slides for this talk. You can also just go to my GitHub repository, s-r-a-n-a-n-d-h-0.github.io. Rika, you have your... I'm going to mute you because there's an echo of my voice coming from your mic. Done. The first link here will be applied vibe coding. You can click on that, but the easiest thing to do would be to use the Zoom chat message that I've just sent, and you can open it, you will go straight to this link.

Next, what we are going to do, or what you are going to do is, first of all, click on the spreadsheet link.

**Question**: Hello sir?

**Answer**: Yes, please.

**Question**: Sir, this is from the BS ops. Just a kind request, sir. We have muted the participants because we found that few were unmuting and it was kind of quite a disturbance. So we have muted them all together. During any question-answer session, they'll be raising their hands, we can unmute them. Okay, sir?

**Answer**: Sure, Rashmi. I think there are also going to be... Sure, Rashmi. There are also likely to be a bunch of requests for the link to the slide for people who have joined in late. If you could, please, just every time somebody asks, send the link again so whoever joins in late can also see this.

Now, there is a link on the homepage to a spreadsheet. That will take you to this sheet, which is where we are going to be tracking what we are doing. I'm going to zoom in into this spreadsheet a little bit. All of your names are, ideally, already here in the spreadsheet. If not, please go ahead and add your name at the end. Try not to overwrite on each other's rows. If you do, well, correct it. No big deal. We will be filling in stuff as we go along. For example, I have already filled out mine. Again, it's in row 41 against Anand S. It has my GitHub profile link, which is where we will be publishing the results of our workshop.

Then there are a couple of questions, like which GitHub plan am I on, which ChatGPT plan am I on, do I have VS Code installed, etc., which will help us figure out which course or which path to take in this workshop. And I will be explaining a bit more of this as we go along. At any point, if anyone has any questions, confusions, whatever, please post in the chat window. Some of you are already doing that and I would encourage you to continue. When we get to the point where people can ask questions, at that point we can unmute. But until then, just go ahead and post any comments or questions or even have side discussions on the chat.

Now, what we're going to do in this workshop, as I said, is create, build an application through vibe coding. The point is to build the application. Coding is almost irrelevant, for which we will need an AI coding agent and we will need a GitHub account. If you already have a GitHub account, please use your GitHub account. If you have multiple GitHub accounts, use any GitHub account. Doesn't matter which one. If you need to create one, go ahead and create one. Just click on github.com and it may ask you to sign up for github.com. Fill out all the details. The easiest will probably be to click on "Continue with Google" and you can then log in and create the account.

Once you do that, then you know your GitHub account. That will be at... in my case it's github.com/sranandh0. Copy this link and put it in the spreadsheet against the GitHub profile link. That's the first part. So that means that whoever has completed this step is able to go on to the next step, which is where we'll be using an AI coding agent. It will be a little tricky to use GitHub coding, I mean to use a coding agent without GitHub in the first place.

Next, so this is step one. You've set up GitHub and filled out your profile. Then you'll have to pick an online coding agent to work on. It could be a local coding agent as well. If you know how to use coding agents, go right ahead, build something. You don't need this workshop. For those of you who may not have used an online coding agent, an online coding agent lets you write code in a GitHub repository. Slide three mentions some of the popular online coding agents. The first of these, jules.google.com, is somewhat free, meaning anyone can log in and use it for a few requests and build and vibe code an application. If you have not used any of the others and don't have an account, then you could use this one.

Many of you might already have a GitHub Copilot account. And this, actually, it says ChatGPT subscription, that is a mistake, it requires a Copilot subscription. Now what you can do is click on that link or go to github.com/copilot and see if you can ask some question here. You can just ask any question, or even just say hi. That will trigger the coding agent and you get a response. If you get a response, then you have access to GitHub Copilot. And I expect that many of you will have access to GitHub Copilot.

Some of you will have access to a paid ChatGPT subscription. That may be ChatGPT Go, which is the 399 rupee version. That's fine. It may be ChatGPT Plus, which is the $20 version. That's fine. It may be ChatGPT Pro, that's the $200 version. That's fine. Or you may have a Teams or an Enterprise account from your organization. That's fine. Whichever ChatGPT subscription you have, you can use Codex. That is a third option. Or you may have a Claude Code subscription or an Anthropic subscription. In that case, and if you do, then you know what subscription you have, you can use that too. There are other coding agents as well. Cursor is an example, and a bunch of others. It doesn't matter which one you use. Pick one of your choice.

What you can then do is update columns D and E, which asks what GitHub plan you are on. Now how do you find out what GitHub plan you are on? Just click on the link in the header and that will take you to your billing. In my case, it says I am on GitHub Pro. So in that case, you can enter GitHub Pro, which is what I have done against my name. I've entered Pro. Similarly for ChatGPT, put in the plan that you have. When you click on that link, it will open a pop-up. In my case, it shows that I have ChatGPT Plus, and this is something that I have entered, saying Plus, that's the $20 account. This will help us identify as we go along, or help me identify as we go along, what guidance to give you based on what account you have.

You may have other coding agents already installed. That's column G. If you already have, in my case I have GitHub Copilot installed, Codex installed, Claude Code installed, and Gemini installed. So I put a tick on all of these. You may have some others or something that is not on the list, in which case you can just select the other. Select all of the tools that you have access to right now during this session. This is not asking what have you used in the past. This is saying for this workshop, what can you use that is installed in the system that is in front of you right now.

Next, what we are going to do is build something. Sorry, before that I forgot. There's also one column which asks if you have Visual Studio Code installed. If you have it installed, say yes. If you are not sure or you don't have it installed, say no.

If you have Visual Studio Code installed, then you could also try some of the command line tools or VS Code extensions for these coding agents. I am not going to cover this in the first half of this session. I'm only going to cover this in the second half of the session.

Now, in a few minutes after I take questions, we will go on to the next part, which is where you decide what you want to build. And there is absolutely no restriction on what to build. This is a workshop where we're just going to play around. It's vibe coding at the end of the day. So you can choose what you want, and there are a bunch of ideas here. But first, what we'll do is go through the chat and see if there are any questions, and if so, I'll cover them, and then I'll come to people who have raised their hands and answer those.

So let's start with the chat questions, which for some reason are not able to... okay yeah, I have it. I'm going to go from the bottom.

**Question**: My ChatGPT subscription is ChatGPT Go.

**Answer**: That's great, Ramshad. That will work with Codex. You can use Codex or if you're not sure how to do that, then give it a minute, follow along and I'll show you.

**Question**: Someone please share the links.

**Answer**: Yes, those links have been shared.

**Question**: Not able to edit the spreadsheet.

**Answer**: Harshavardhan's response is right, the traffic may be high. Just give it a few seconds. And if you don't edit it, it's not a big deal. If you have a question, then I'll be able to refer to the sheet and say, "do this or do that." And it will help me at the end of the session to collect some statistics and do some data analysis, which will benefit me more than you. So you don't have to worry about not being able to edit the spreadsheet. But if you can, please do, when you can.

**Question**: PyCharm or VS Code and Anaconda?

**Answer**: In this session, we're going to be covering VS Code, Hemant. But if you are familiar with the others and know how to do what we are covering in the session on those, go right ahead.

**Question**: Will you share the recording?

**Answer**: Since it's being recorded, I'm guessing it will be shared, but I'll let the organizers comment on that.

**Question**: Qwen?

**Answer**: Absolutely. Feel free, Bhavesh. Qwen is a great model. Qwen2-Code is an excellent model, in fact, at a very low price.

**Question**: Gemini Pro... Claude Code... Cursor Pro...

**Answer**: Charchit is responding to a comment saying Gemini Pro is not good for vibe coding, use Claude Code instead. If you have access to either a Claude Code API or a Claude Code subscription, go right ahead. But Sashwatham, Gemini Pro is also absolutely fine. Nothing wrong with that. And Cursor Pro is fine too. For the purposes of this workshop, we are not too fussed.

**Question**: ChatGPT Go is enough?

**Answer**: Yes, Rani.

**Question**: Browser Comet?

**Answer**: Khushi has answered, "Yes, I'm just using Edge, I'm not using Comet." I'm on Linux, which unfortunately Comet doesn't yet work on. That's a pity.

**Question**: Personal email is fine?

**Answer**: Sashwatham's comment is probably already answered. A personal email is fine, institute email is fine. Create a new one if you like, anything's okay.

**Question**: Windsurf?

**Answer**: Windsurf is perfectly fine. Go right ahead. Being broke is a great state.

**Question**: How not to be broke?

**Answer**: I have no idea, Dhananjay. When I find that out, I will tell a lot of people.

**Question**: ChatGPT Go does not offer Codex. Is it?

**Answer**: I find that interesting. So let's ask ChatGPT. When in doubt, does ChatGPT Go allow users to use Codex CLI? And figure that out. I should hopefully be able to get back to you soon.

**Question**: Can you repeat from the GitHub.com?

**Answer**: If you're looking for a recap of that, please go through the slides, Dhruvan.

**Question**: I have VS Code and Copilot but ChatGPT free version.

**Answer**: No problem. As long as it works, that's fine. Personal GitHub is fine. After creating the GitHub repo, just see if you are able to log in into any one of these coding agents mentioned in slide three.

**Question**: Okay, ChatGPT Go by itself does not give you access to Codex CLI. I was mistaken. I thought ChatGPT Go would give you access. So, yeah, you can either upgrade or get an API key or use something else.

**Question**: GPT 5.1 Codex preview?

**Answer**: Yes, that's wonderful. Please go ahead.

**Question**: Gemini CLI and GitHub Copilot?

**Answer**: Either of these will work in the process, Sashwarthan, no problem.

**Question**: Will the GitHub profile automatically be added to the spreadsheet?

**Answer**: You have to do it manually, Lalit.

**Question**: How do you add it?

**Answer**: You just open the spreadsheet and type it in, Lalit.

**Question**: Charchit's already created a rain monitoring Flutter mobile application.

**Answer**: Wonderful. And that tells me that Flutter is a possible framework that I could ask the LLM to use. Let's do that.

**Question**: Sharad's going to be building a Tic-Tac-Toe game.

**Answer**: That is cool on mobile. Yeah, that would be interesting.

**Question**: Can you do anything that's not mentioned in the slides?

**Answer**: Yes, Jason, in fact, please do something that's not mentioned in the slides. That's more fun.

**Question**: Do you need to push the code in GitHub?

**Answer**: You will actually end up doing, or the agent will actually be coding on GitHub if you are using a remote coding agent, Sanjay. But if you're doing it locally, then yes, please push it into GitHub.

**Question**: Can it make error-free enterprise-level applications?

**Answer**: **No. Straight away.**

**Question**: Will agents help us with testing?

**Answer**: **Yes, they will, Ramalingam.**

**Question**: For someone who is a complete beginner, I won't be able to mention currently what I would build as I'm a complete beginner.

**Answer**: And Kushagra, in that case, you could ask the agent what you might want to build, and it can give you ideas because it knows itself better than we do sometimes.

Okay, good stuff. So you're all putting in your apps here, which is great. Also, feel free to put it there. Now, what I'm going to do is use GitHub Copilot to build my Grand Theft Auto-like game. Now, here's the problem. I have never played Grand Theft Auto. Now, I don't know what a coding agent can build. **So I have two levels of ignorance. I don't know what I want, I don't know what it can do.** Now, what am I supposed to prompt?

And this is where AI comes in handy. I am not even going to try. I'm going to ask some chat engine, let's try Kimi, which people seem to be raving about. You can use whatever you want. And I am going to, actually, I'm going to type this in ChatGPT, but paste it in Kimi because ChatGPT has better voice dictation.

"I am running a workshop on vibe coding and I'd like to create a game. I ideally would like to create something interesting like Grand Theft Auto, but the reality is I've never played Grand Theft Auto and I'm not particularly fussed about Grand Theft Auto in the first place. I'm okay with any kind of application of that style. I also am not really sure what AI coding agents can and cannot do, and I don't want to fail in an embarrassing way in a workshop that I'm conducting. So I'd like you to give me ideas for games that I can build that will be as impressive and interesting as Grand Theft Auto, directionally, and at the same time will be something that an AI coding agent with the capabilities that it has in November 2025 will be reasonably comfortably able to do. You can search online for other things that people have built using vibe coding to get a sense of the latest capabilities in case you don't know that already."

Now, what I'm going to do is let, after I transcribe this, let ChatGPT do its work. I'm also going to ask Kimi to, yeah, search and think and give me some ideas. I am going to ask Grok to come up with some ideas, and I'm going to ask chat.deepseek.com which I need to log into. My system crashed so all of my credentials and browser cache have vanished, but I should be able to get back into DeepSeek with a deep think and a search option enabled. And finally, Claude, which I should be logged into, and have it answer the question.

Now you'll notice a couple of things that I did. The first was I used dictation. I find that it's a lot easier for me to talk to an AI agent than to type. At least I end up saying more and in a richer way. Second, I am using multiple... I am using multiple coding... AI chatbots to give me ideas. Why multiple? Well, because different ones may have different ideas and while it's thinking I'm bored, so I may as well toss it with something. I usually find that the first one that gives me the answer is the one I like best because that has the maximum uplift, but there's no harm in trying out different ones.

And let's see. Kimi is saying they can do 3D worlds. That's a good idea, blah blah blah, but I'm not interested in what they can do, just give me the answer. Neon Courier: District 7. So that's a hoverbike through a cyberpunk city. Okay, and it's saying create a 3JS game with blah blah blah. Okay. Now that is... it's saying this is safest bet. Okay, I want to go for the safest bet. So, create some kind of a 3JS game where the player drives a hoverbike through a cyberpunk city. Yeah, this looks decent. Let's see what the others have said just for curiosity. One Block City. That does it have a prompt? Let's see. Top down 2D... okay, this is a top down 2D city block. 2D doesn't sound so interesting, so I'm going to skip this. And blah blah blah. Just take a quick look at Claude because Claude is a nice writer. Okay, 3D dogfighting game. Interesting. Okay, I am going to go with this.

So, the next thing is I should now get a prompt for this. Let's ask it for the prompt unless it's already given a prompt. So, go with the dogfighting game. Okay. "Give me a prompt for the dogfighting game." You'll notice that this one I didn't dictate because copy-pasting is easy and it's not like it was a complicated or long one.

So now, we know what we're going to build, or what I am going to build, which is a 3D dogfighting game. The beauty of this is you can start imagining new kinds of games that don't even exist. But here is the phase one prompt. Next, where am I going to build it? Let me build it everywhere. Meaning, there are a whole bunch of these coding agents. So, just to show you what coding agents can do or how you set each of these up, I'm going to go one by one.

Let's start with maybe Jules. So, on Jules, I have already logged in. Now it allows me to choose an existing GitHub repository. I cannot create a new GitHub repository. All right. So, let me go to github.com/sranandh0, create a new repository and type in the repository name which will be, let's see, this is where imagination fails, so I'm just going to... let's see. Dogfight... okay, dogfight, yeah, let's just call it dog... should I create multiple repositories? Yes. So let's say dogfight-jules so there's no confusion. And the rest I'm going to just leave it at default, except perhaps to add a license. I'm going to add an MIT license. Now why am I doing this? Some of these coding agents crib if there is an empty repository. So at least I'll put in a license and I also anyway want to make it public for anyone to use. And now this repository has been created.

Let me go back to Jules, start the session, or reload the page so that the repository will probably be reflected. We called it Dogfight. Yes, so Dogfight-Jules is available. And I'm going to paste this prompt. I haven't even read the prompt, but that's okay. It's not going to cost me anything... well yeah, Jules is not going to cost me anything anyway. Let's see. So I will start it and then read the prompt. The prompt is saying, create a 3D browser-based flight game using 3JS where the controls from a fighter jet, blah, it's going to do something from a technical perspective. But what I am interested in is I can use arrow keys to control it, Q and E to turn left and right, spacebar for speed. Okay, and there should be some ambient music. So at the very least, I should be able to fly around somewhere. Now, one rule of thumb that I follow is **never waste your time, waste the machine's time instead**. This is saying, okay, approve plan. Fine, I'll approve it. Let's go on to the next coding agent, GitHub Copilot.

So for this, I'm going to do the same thing. But let's create a new repo for this. github.com/new and that's dogfight-copilot, which will be initialized with an MIT license. Create the repository. And let's go back to Copilot. Add a repository which is dogfight, copilot. Having added this repository, I'm going to paste this. Now, in some of these tools, many of these tools, you have the option of choosing a model. And as someone mentioned in the chat window, different models have different capabilities. And Claude 3.5 Sonnet is one of the better models. GPT-5 is almost as good. GPT-5 Codex, some say is on par, even better. Each has different advantages. And I'm going to choose for GitHub Copilot, I'm going to choose Claude 3.5 Sonnet as a model that I'm familiar with, I like its style, but you can choose whatever you want. And I'm going to click... Okay, I don't know what that did. I think we have to click on "Task new" if you want to create something. I'm not that familiar with Copilot, I'm just playing around with it here. But let's see. It looks like it is doing something. Let it run.

Third coding agent, Codex. Let's open Codex. I'm going to create a new repository which is called dogfight-codex. Create an MIT license and create the repository. Go back. Paste this on... Now, Codex operates in a slightly different way. You have to create an environment with a repository. So I'm going to click on "Manage environments," "Create environment," and search for this dogfight repo. I have dogfight-codex, I'm going to choose that. Having chosen that repo, it then asks me a few things like, what image do I want to use? There's only one option there. What environment variables and secrets? I don't want to add any. But the important one is internet access. Should I give it internet access fully to install stuff, partly... sorry, fully to do whatever it wants, partly to install stuff, etcetera. I'm going to give it unrestricted internet access because what is the worst that can happen? The new repository that gets created has some hacking code from somebody. I'll be careful when I visit the page, or I'll take a look at the code beforehand.

So I have enabled internet access on because it's a completely fresh repo in a container. And I'm going to click on use this. And then, now here, it has the option of creating one or multiple versions. I'm going to choose one, but actually no, I'm going to choose two. Why not? Let it create two versions and let's see what both look like.

Finally, Claude... this does not include Gemini, but no, actually I'm not going to go for more. If you have Gemini, go ahead with Gemini. If you're using Claude, use Claude, etcetera. Now, some of these agents have probably already completed. Jules is still working. Copilot is still working, Codex is still working. So, since they are working, let me take some of the questions that have come up recently.

**Question**: from Ashish, are we pre-assuming that current coding tools have limitations to build GTA-like game in our prompt?

**Answer**: I am, Ashish. Not because I know that they have a limitation, but because I have been programming for 30 years now. And I find it a little disturbing to believe that some AI coding agent that was born two years ago can build a game that I can't. All of these years, these games were a little difficult, so I'm assuming that it cannot. In other words, my mindset is accumulated practices from 30 years. Some of which are good practices, some of which are outdated practices. So yes, I am assuming that the coding agents may not be able to build a GTA-like game in our prompt. But I don't know if that's right or wrong.

**Question**: Lawrence suggests using Replit.

**Answer**: Sure, Lawrence, that is a good idea. There's a whole host of tools like Replit, Lovable, Bolt, etcetera. So, why not Replit? Let's log in. I don't think I have an account or maybe I do. I have to check. I'm going to open in another window my passwords file. And look, okay. I have logged in with my Google account, but it's not a paid account. And continue.

Alright. What do I want to make? Let's see. Can I just click back? 3D game. Okay, and start chat. Is that it? Okay. It's planning. Now, this is one of the common things. You also remember Jules having created a plan and then asking for approval. Somewhere at the beginning, Jules had, yeah, said, "I'm going to create a basic HTML, CSS, JavaScript files, set up a 3JS scene, blah, blah, blah." And then it asked if you're okay with the plan, and I approved it without reading it. Not a good idea sometimes. Not a bad idea sometimes.

When should you review the plan? If you're building something important and useful, and you don't want to waste too much time, then read it. If you're building something that's throwaway, if it doesn't work, big deal, you just move on, don't read it. In this case, I'm building something that's throwaway. If it works, great. If it doesn't, big deal. I'm learning either way. So, I'm not reading the plan. I'm going to go ahead.

**Question**: Next was a question from Shashwatam, how to add GitHub in VS Code? And Chirchit and Harshavardhan have answered that. Question from Aditya, why am I using MIT licenses?

**Answer**: If the question, Aditya, is why am I using MIT license compared to the other licenses, **it is one of the shortest, most permissive licenses. Why complicate things when simple works fine?**

**Question**: from Tarang, shall we start ourselves?

**Answer**: Yes, please. I didn't realize that I had not made that clear. Please go ahead, build your app by yourselves. It's a workshop. Let me know where you're stuck, post a message. Hopefully, someone will be able to answer this.

**Question**: Lalit, you're not able to paste your GitHub profile link.

**Answer**: Paste it here in the chat, Lalit, no big deal.

**Question**: Shivam's doing this for the first time. I'm not able to catch up with you. Please help.

**Answer**: There's nothing specific to catch up, Shivam. This is more like a group... this is more like a setup where a bunch of people are trying to vibe code. And I have been vibe coding for some time. I clicked on a few things and figured it out earlier, and now I'm doing it faster in front of you. You need to visit any of the links in page three, follow the instructions there, and when you get stuck on something specific, put it in the chat window. Or better yet, take a screenshot of that, put that into ChatGPT or Gemini and say, "I'm stuck here," and ask it. This is more a... I'm not giving you step-by-step instructions to follow along, but rather a space where whenever you get stuck, you can ping back.

**Question**: from Saurabh, what to do after it finishes doing its work?

**Answer**: Ah, okay. That is wonderful, Saurabh. Please put in a link to what you have built. This was what you will build. And link to your app. In column I, which is link to your app, please put in the link to your application. So, Balai Singha has put in a GitHub profile, not quite what I wanted. So once I build the app, the actual GitHub repo link, you can put in here. Better yet, you can publish it as GitHub Pages and allow people to play the game or use the app or whatever it is that you've built.

**Question**: What distro do I use?

**Answer**: Ubuntu, Varun.

**Question**: Could you use Google AI Studio?

**Answer**: No, Sarang. Google AI Studio is more an API playground. It won't be able to commit or push code to GitHub.

**Question**: A word like GTA is doing a lot of heavy lifting. It means different things to different people.

**Answer**: True, Noel. That is true.

**Question**: What's my suggestion for coding standards?

**Answer**: That's from Ubaraju. Okay. Coding standards are a big area. I will be covering that a little towards the end of this discussion. This recording will probably be shared.

**Question**: Rudransh says, "Can AI make full-fledged apps?" Okay, maybe I should just... okay. I did not expect that somebody would delete the entire app. So let me, hold on. This is an interesting one. Version history, see the version history, and I will go back to a recent version. Mark modified. Okay. This is probably the version I should restore. Let's see. One or two of you might find that your... Damn. So, whoever it was, if you were trying to intentionally delete it, please don't. Whoever it was who accidentally deleted it, please don't. And I'm not able to get in, so big deal. That's perfectly alright. I've learned that now I should not use Google Sheets for such large collaboration.

Okay. **Question**: from Shivani, there's no deadline to build the app, as Harshvardhan said. Question from Mahadevan, what about building a 3D portfolio website like Bruno Simon's?

**Answer**: That is a great idea, Mahadevan. That would be fantastic.

**Question**: Vaikuntavasan says, "Shall I use Kwen-3 Coder?"

**Answer**: Yeah, sure. Go ahead. And Lalit's already created an app. Let's take a look at that. You okay, you created a repo in which it's going to be presumably putting in more code. That's fine.

**Question**: from PK, can we use Google Colab with Gemini?

**Answer**: Yeah, technically that's vibe coding. So yeah, why not? I'm going to jump to the... actually, no. I'm going to see what the status of the apps are.

Let's see if Jules has... Okay, Jules has completed something. Now, and it took 5 minutes to build this application. I'm going to publish a pull request. What that will do is send a request to GitHub saying, "I have created all of this code. What do you want to do with it?" Now we may say, "I want to go through the code carefully. I want you to make changes," or, "I want to just accept it as it is." Now, ideally, we would want to see the output before accepting it. Unfortunately, that preview is not available in many of these tools, though Replit will probably show us a preview. So for now, I'm just going to say ready for review, merge the pull request. There's a merge pull request button. If you click on that, that will work fine. And delete the branch.

Now, when I go to the homepage of this repository, it's created an `index.html`, `main.js`, and `style.css`. In other words, it's created a bunch of files. How do I see it? Because it's a web application, what I can do is publish it and see it online on GitHub. On in the settings of my repository, in the left-hand side, there is a Pages link. So I went to settings and then I went to pages. When we have the pages enabled, we can say where we want to deploy the pages from. I'll click on main and save. Now, main is the branch where it pushed to. You'll probably only see `none` or `main` by default.

When you select the branch as main and click on save, in some time, it will publish. Where will it publish? You can see that in the Actions menu. So let me just recap. I went to Settings, Pages, selected main as the branch and clicked on save. Settings, Pages, main branch, save. Actions will show me where it is publishing. And it's still publishing. This circle is going round and round. And finally, I see a link: `s-anand0.github.io/dogfight-jules`. And I'm going to paste this in the meeting group chat as my link.

Okay. So now if I press space... okay, the speed increases. Okay, this thing is turning around. If I press Q... okay. Basic 3D app. It's kind of flying. Not exactly what I thought would be... well, it's very basic. But it may not be very different from what I asked for. And there's nothing that stops me from going to the next stage. In any case, Claude had already given me a second phase prompt too. So, I'm going to copy this, tell Jules to go ahead and create the next phase. So in this, I'm going to create a new session and just put in the second prompt. So let it build something. Let us take the second application.

Copilot has finished working, has created a pull request. I'm going to do the same thing as before. Okay, wait, this is nice. Copilot has given me a screenshot. And I find that when something gives me a screenshot, it's a lot easier to review. Clearly, this looks a little better than what Gemini had created. Now, how much of this is Claude code... sorry, Claude Sonnet as a model, which we used here, and how much of it is Copilot's own capabilities, who knows? But good, I like this more. And okay, there's some exhaust glow, there's boost, altitude ceiling. Okay, it's added some decent game dynamics. Very good. Ready for review. And then merge pull request. You can just click on merge pull request. I like to click on rebase and merge instead. Just a quirk, makes little difference. And I'll do the same thing. For this repo, settings, pages, main, save. And in some time, it should have built the page and I should be able to preview it.

Let's take a look at what Codex has done. It has not created a screenshot, but it's created some code. I will again tell it, create the pull request. After it creates the pull request, we'll follow exactly the same steps. While we are at it, I may as well take a look at what... oh, okay. Replit has built a Sky Fighter game. Now, the difference between the coding agents that I shared earlier and something like Replit is that I can play the game directly. Let's see. So, I'm going to click on Sky Fighter. Okay, if I press Q and D, it moves. Okay, it's flying. I'm going higher. Wee! This is nice. Crashing. Okay. This is good. And space gives it a boost. Yes, I can see it going higher. Okay, there's an ocean there somewhere. Can I actually go closer to the ocean? Maybe a little. Kind of. So yeah, it has some decent amount of control over the terrain. So, nice. I like this too.

Let's go back. We will merge the pull request that Codex has created by rebasing and merging. And for the Codex version, I will go to the settings, pages, main, and save. And wait for this to get deployed.

Okay, now, the Copilot version is deployed. Let's play that game. I don't see anything. Is there an error? Okay. So, Copilot has made an error. In the dev tools, I see something in red, saying 3JS not found. What to do in such cases, I will come back to in a short while. So let's do a quick review. Jules is on its second task. Codex did a good job of the screenshot, but there is a problem. And Codex is still building. Replit did a good job, but I'm not sure how exactly we can deploy this. Oh, okay, there is a publish. Let's see. Click on publish. Okay, I have to upgrade my plan to publish, so I can't quite show this to you yet without getting a plan. But that's all right. This is ChatGPT Codex, yes.

Let's take a look at Codex's version. I see a sky, but okay, again, 3JS failed. So, this is interesting. Gemini managed to get something kind of crude and it's working, but both Copilot and Codex failed.

Let's now see what you do if there is an error. The point is with vibe coding, **you should absolutely not have to know anything about coding.** So, one approach is to simply take a screenshot. Let's see, take a screenshot. I'm going to go back to Copilot, which seems to have vanished. `github.com/copilot`. And instance of coding, what? Jules. Where did this go? Dogfight Copilot. Okay, now that's the output. Where do I... this one looks promising. Ah, this, yes. This is the window where I had originally put this in. Now it's saying the pull request is already merged, so I'll probably have to create a new task. Okay, let me do that. I'm going to create a new chat. And for this task, for Copilot, I'm going to say... first, let me paste... I'm not allowed to paste this image? Okay. On Copilot, it looks like I'm not able to paste that image. That is perfectly all right.

I'm just going to say, I saw this... I'm going to move this to another window so that I can refer to it. I... this app doesn't work. It shows the controls, speed, altitude controls, etcetera. But I don't see the terrain. I don't see the plane. I just see a black background. Now, here's the thing. This sort of a mistake is wasting my time. I do not want to have an application that... it makes basic mistakes, something you can't you see? So, let me tell it, "**Run it in the browser and test it and make sure it actually works.**" Now, this is a very powerful line.

What we're saying is, "I don't want to do the first cut review. I want you to do the first cut review. Take some ownership." Now, why didn't it do it in the first place? I don't know. Maybe once they get smarter, they will. But by telling it to do so, at least I'm asking it to save me some trouble. Let's give it a shot. Which is exactly the same thing that I'm going to tell Codex. This is not Codex, this is Copilot. Okay, Copilot is so far... what is this? This is the Copilot agent's one. This is the Codex deployment. All right, cool. So now this PR has already been merged, so I'm going to start with another task. Or can I just continue with this? Yeah, probably just create a new one.

Paste exactly the same thing. This app doesn't work. And in Codex's case, the problem was slightly different. Oh wait, it didn't take an image. `s-anand0/dogfight-copilot`. No, sorry, Codex. The problem was, ah, it's just a black screen. So, it not black, just shows a blue sky screen, but I don't see the terrain. I don't see the controls. Not a black background. And have it do the same thing. I'm just going to ask it to create one version.

Now, you remember last time, I had it create two versions in Copilot. Let's see what happened to the other version. Version two, let's create a separate pull request for that. Actually, no, now that I've merged that one, that might cause some complications. So let me not do that.

Okay, so what we've done in the last, maybe 10 minutes, is deployed a few versions. Jules' version was crude but worked. Copilot's was promising but didn't work. Codex's, we don't know, didn't work. And Replit's worked absolutely fine, but I can't deploy it without an account. And even if I did deploy it, it would be within Replit's environment, not in my GitHub repository, which may be okay for some purposes.

Second thing that we did was when we found that there was a problem, we just told it what the problem was and asked it to fix it, but also to test if it has fixed and move on. Now, what I'm going to do is pause for a little bit and move on to some of the principles of vibe coding and synthesize those. But I can also take a few questions from the bottom.

**Question**: What's the use of VS Code here?

**Answer**: Ramshad, we haven't yet used VS Code. Time permitting, we will come to that.

**Question**: from Aishwarya, can we create GitHub Pages for every project?

**Answer**: Yes, as long as it's browser-based as Ankit mentioned. I'll just pick the questions that have not yet been answered.

**Question**: Lawrence says, "I made a website using ChatGPT. Will I check it?"

**Answer**: toolstech.in. Sure, happy to check it offline.

Question... bumped up a little bit. Okay, I've lost track of questions, I think. **Question**: from Amanpreet, how to stay safe while using vibe coding?

**Answer**: Easiest way to stay safe, Aman, is to not vibe code on your machine. Vibe code on somebody else's machine, like Replit or Jules or the likes.

**Question**: A comment from Arjun: "I've been using vibe coding for a few months and it's helped. What's a future direction? Should we focus on traditional paths like DSA, LeetCode problem solving?" In other words, how should developers progress?

**Answer**: Personally, any tool that comes up, the more powerful it is, the more we end up using it. When databases came up, they completely ate the transaction processing system world. When the browser came up, a significant portion of development shifted to browsers. And of course, there was new growth of new capabilities. When mobile came in, mobile application development became a large thing. Similarly, with AI, AI coding is going to become a fairly large part of the toolkit. So, the good part is colleges and courses will anyway teach the old stuff. You don't have to take much effort there. You may as well spend that extra effort learning some of the newer things that are not covered in curriculums. That's my thought.

Okay. Let's switch over to slides for a bit. I know I've covered only one app. We will be going on to another app, but let's talk about some of the principles that I keep in mind when vibe coding.

Number one, **it is risky.** As you saw here, two of the vibe coding attempts did not even create something that worked. One of them created something that was not so good. One of them created something that was decent, but I couldn't deploy it. So in every case, I've had a problem. Now, supposing somebody asks for something specific, and you say, "Yes, I can do it" because you're confident vibe coding can do it, you are making a mistake. **Don't promise upfront.** AI coding is unreliable. Vibe coding is even more unreliable. By unreliable, I mean sometimes it works, sometimes it does great, sometimes it works terribly. And when it works terribly, you have to do it manually, which means you get no benefit. So plan for it accordingly. Assume that you may not get a benefit and then promise. Or finish the work and then promise. Try not to become overconfident. This is a typical pitfall that I see both fresh developers, well, non-developers and fresh developers fall prey to. Experienced developers are slightly more vulnerable to this. They have a different problem. They don't vibe code in the first place, which is another kind of problem.

Second, you'll notice that I didn't even look at the code. The specification, what we want to build, is increasingly becoming a more important component, and code is almost a byproduct. We gave the same spec to different coding agents. They delivered different outputs. If one of them delivers a good output, I'm fine. If not, if none of them deliver a good output, I will change what I want and try it out with a bunch of them. If it doesn't work, it doesn't work. But what I specify is increasingly becoming the product. So one of the practices that people are following is to save the prompts. Store it locally, commit the prompt, put it along with the pull request, type it in a separate file somewhere. Anything is fine. But preserve the prompts, preserve the conversation history. These things are increasingly becoming more important.

The amount of time that it took to code does not impact me in any way. While it was coding, I was asking another agent to do something. And then another, and then another. So its coding time does not take up my time. But the review time is my bottleneck. When I was after looking at the PR saying, "Oh, why is this not working? Oh, this is a blue sky, this is a black screen. Maybe I should check something." That review time, in this case, I spent very little time reviewing because it was easy to verify visually, but sometimes setup can take a long time, checking if it works takes a long time. What you want to do is to make sure that the amount of time taken for review is as little as possible. One of the ways of doing that you just saw a short while ago. I asked it to run this in the browser, test it, and make sure that they pass. That is one of the ways in which you can reduce at least some basic review time, and simple mistakes are caught. But in general, save your time, not the AI's time.

Sometimes you get stuck. We haven't yet seen that situation yet, we might. But if you get stuck, then there are two ways. One, tell it what to change. Two, start from scratch. My suggestion is if it goes off track and you're not able to fix it in one attempt, maybe two attempts, don't continue in that direction. **Start over.** Because correcting is harder than not making mistakes for AI agents these days. I don't know if that's going to be true in the future, but right now that seems to be working better. Therefore, if you're going to plan to start things over and over, it usually helps to keep tasks small. Give it a big task, something doesn't go wrong, go well, you'll have to start a big task all over again. If you broke it down into smaller chunks, then at least it's a smaller chunk that you have to rebuild on top of. Might help.

Another thing that you could consider is making the repositories LLM-friendly. What I mean by that is, if you find that there are some instructions that you are always giving it, then store that in the repository. If you find that there are some libraries that you want it to use, some coding style that you want it to use, use it. One convention that is emerging for this that a number of coding agents are adopting is a file called `agents.md`. It's just a text file. In this file, you put in whatever instructions you want for the coding agent to follow. For example, you may say, "Always double-check your code, try it in a browser, and see if it is working." You could say, "Always write code that is compact. Make sure that you write secure code." It may follow those instructions, it may not follow those instructions, but if you find that you are often giving the same instructions when vibe coding or AI coding multiple times, it helps to keep a list of those instructions and copy-paste or put it into the repository as a file called `agents.md`.

One of the things that works best is if you give it an example to copy from. You say, "I've already created this, or somebody else has already created it. I just want you to copy and make a change to this." That sort of a thing works remarkably well.

**Work in parallel.** You saw that. That's what we were doing here. When you're giving the task to one agent and it's working, work with another agent. Take another task, take another task. The point is you are trying to maximize your productivity while the agent is working on the side. Now, what this means is you therefore need a queue of tasks, you need a bunch of things that you can do one after another or side by side that you can give to the agents. And they should be both things that an agent would probably be able to do, or broken up to the size where it's going to be able to do. How would you know that? Practice, really. So, try something. If it's... if it solves it, then try something harder. If it doesn't, try something smaller by breaking it up. That's the kind of thing that we will explore.

Finally, the benefit of something like vibe coding is very, very different based on where you are in the coding journey. People who are experienced are able to get significant productivity boosts because they know what needs to be done. When the AI coding agent gets something wrong, they can point out and say, "This is the mistake you made." For example, some of us could see that it was not loading the 3JS library properly. So I could have simply taken a screenshot of or copy-pasted the console log and given it a very specific instruction and it would have fixed it. So knowing that you can do this sort of a thing, which an experienced developer does, is helpful.

On the other hand, novices in some sense get a bigger boost. You were not able to do something, but now you are able to do something. And that's fantastic. It's a great start. The risk is that you think what you've done is correct, complete, perfect, whatever, without knowing the kinds of mistakes that crop up. If you then try and make a change on top of it, it can collapse like a house of cards, and you may not know that. That's a different kind of risk, unlike the experienced developer who may not be trying to get as big or as imaginative as a leap as a novice. So, one of the things, especially for those who are coding in an area that you're not familiar with... remember that everyone is both an expert and a novice in different areas. So I'm probably an expert in JavaScript. I am a novice in Java and even worse, a novice in a language like Go or Rust. So, depending on the area that you have or do not have expertise in, **plan to learn along with the agents, not just delegate.**

So these are some of the things to keep in mind while exploring vibe coding. Now, what we're going to do is go back to the exercise itself and try out a few other things. But I'll take a quick look to see if there are any questions.

**Question**: from Ayush, what's the best learning path for a beginner who wants to utilize these coding agents?

**Answer**: Use it as much as possible. **Maximize your usage.** Second... I didn't want to do that chat... found it. Yeah. Second, while it creates, learn from it. See what it's doing, why it's doing, ask it to teach you.

**Question**: AI is on a developing stage?

**Answer**: Yes, absolutely, Chakravarti. Meeting recording, yeah, I think that should be shared.

**Question**: Why do we not try all possible things that can be built, such as generate content instead of create a game?

**Answer**: Absolutely. Part of what we are lacking right now is that **we don't even know what are all the kinds of things that can be built.** So yeah, do go ahead, Chakravarti.

**Question**: And Harshvardhan's commented that building apps or games using vibe coding is helpful for a developer.

**Answer**: Yeah, true, but if I'm a market researcher, I might instead want it to do a market survey of imaginary people. And that could be a pretty good idea. Nothing to do with coding, but it may generate persona and generate synthetic... generate synthetic persona using code on the fly to accomplish the task. Or I may ask it to generate an RFP response. I actually did do that yesterday. And in order to do that, it was vibe coding. It went through the RFP, it converted it to different formats. The RFP had a few Excel attachments. It made sure that it was calculating it right. It created some synthetic data for me to showcase in the RFP. So yes, we can create all kinds of things and coding is just a way to do it.

**Question**: Can we deploy using services other than GitHub Pages?

**Answer**: Maybe. I have not seen any of these coding agents work out of box with other coding agents. If you're using it locally, then yes.

**Question**: So maybe vibe coding can be used for small tasks but not for full-blown apps.

**Answer**: Maybe, but we don't really know that. So my suggestion is to try building it, try building what you want, and in case it works, great. If not, then make it smaller.

**Question**: And yeah, try learning along with the agent. That's right. Can I build any project for a large audience level?

**Answer**: Give it a shot. It might work, it might not work. And as Chirag is saying, it's probably not going to be production level. Probably. So you wouldn't want to bet on it, but if it works good enough for you, sure. Yes, please add the project link to the spreadsheet after the call is over.

**Question**: College placement and upcoming years of advanced AI what skills will companies expect in the next 30 years?

**Answer**: Actually, I don't know what skills companies will expect in 13 months, let alone 30 years. It is a rapidly evolving field, and what we find is when a technology comes in, the skills that are complementary start becoming more important. Meaning, if because of this technology we are able to do some new things, people will start asking for skills to do those new things.

Now, you just saw what I was playing around with. What skills didn't I need? Coding. So maybe that is not as important, or if it is, then the growth of that may not be as high as it used to be. What skill was still important? For somebody to figure out what application to build. So, definitely ideation is important. For somebody to break it down into the chunks that are roughly the right size, that may still be there. For somebody definitely to verify and see that this is useful.

So, I don't know how much the game developer market will grow. It may grow because game development is easy, so the return on effort is high. Or it may shrink because AI can build the games. But the game player market will definitely grow. So, if you become a game tester, I expect that you will have a little more demand. And I guess we need to start thinking along these kinds of lines.

Lalit's built a scraper. That's cool. And you have some glitches. Yes, just feed the glitches back, Lalit, along with screenshots and see how that works.

Can I show how to use Gemini CLI in VS Code? Yeah, let's do that. I'm going to take VS Code next since we do have time. Can we use it in an RAG application? You can use it to build anything. Can we use coding agents locally? We're going to do that in a short while. Is this the next best thing? I have no idea.

Kwen is not able to push files to the public repo even after having given it the auth token. Yeah, Tarun's suggestion is probably the right one. Download or copy-paste the files and push them manually.

If you don't have any pro subscriptions, can we do vibe coding? Sure. Ask ChatGPT to give you the code, copy-paste it, commit, publish.

I'm not able to publish the code from GitHub Copilot to the linked repo. Will I need the paid version for it? Not sure, maybe. Copy-paste for now.

So, what we'll now do is go to how we can build a vibe coding, or how we can vibe code an application locally. Now, this is slightly different from what we were trying, and I know I've started a bunch of tasks, but I'm not going to do much other than maybe just initiate the pull requests on these. Co-pilot is still working. Okay, interesting. Codex. Okay, I'm not even going to bother going through this.

I am now going to do something on my local machine. I have Visual Studio Code installed, and what I'll do is share a link on how you can get one of these coding agents installed. I'll share this link on the chat, which has instructions on how you can set up Visual Studio Code with Codex. The process is very similar for any of the other applications. You install Visual Studio Code, and it'll give you some kind of a screen like this. And then you click on extensions and install the appropriate extension. It could be, let's try Gemini CLI.

Gemini Code Assist is what I think they've called the extension, and in my case, it's already installed. There's also a Gemini CLI companion, which makes all of this very confusing. I'm going to use the Copilot one. Why? Because I think many students have the student account, and it's built into Visual Studio Code. So GitHub Copilot Chat, in particular, comes with Visual Studio Code by default in many installations.

And what you can do is enable this. Control+Alt+B is what does it for me, but you can just go to chat and select "Open chat." Control+Shift+P, "Open chat," or just click on the top and just say "chat." Okay, figure it out. But it appears here on the right-hand side, and it works in a very similar way. You can type in commands here, asking it to build something, and it will do that locally in that directory.

You can also run this in the command prompt. What I'm going to do is go to a new folder. I'm going to create a folder, but this time I'm going to do something slightly different. I want it to build a native mobile application. The trouble is, in the half an hour that we have, building a mobile application and moving it to my phone, for someone who's never done it before, might be too big a leap. So, I am instead going to ask it to build a native GUI application in Linux. And yeah, let's see how it works.

Sorry, I did not mean to type Codex. I meant to type `code`. What I've done is opened Visual Studio Code in a new directory. And what I want it to do is actually create a native application that uses something from my list of files. Let's say I have a local file, something that I've downloaded. I seem to have a CSV file. Okay, I know what this is, but retail_transactions.csv. This is interesting. Okay.

So what I want, what I have here is a CSV file that contains a bunch of transactions people have made in some store. It's dummy data, but I will copy this retail transactions file to this directory. And now ask Copilot to do the following. I'm going to type the prompt out here in a large font so you can see it.

`retail_transactions.csv` has transactions made by customers in a retail store. Now, create a native application that shows insights, or okay, that lets me filter and visualize the data. Now, what do I mean by native application? Do not code in Python. Oh, okay, but then it'll need to download something. I'll leave the choice of language to it. So when I say create a native application, I mean a desktop UI application and build it. Now this is not something that I've done in probably a decade or so. So let's do this. But I'm going to choose Claude 4.5 Sonnet as the model. And is there some kind of a give full permissions thing? Okay, let's just run this.

Now, it's going to run. I'm in parallel going to have Codex do the same thing. To run Codex, what we do is `npx -y @openai/codex`. If you have NPM installed, then it will automatically pull this repository and run it. I may need to log in. No, okay, I've already logged in for the first time. I have a paid account with Codex. I'm going a little fast here because if you've worked with CLI tools, this is broadly familiar. If you haven't worked with CLI tools, you should not be doing this.

The next thing that I'm going to do is give it full access. Slightly dangerous, but this is a completely new machine that I've set up today because my laptop crashed yesterday. So, I don't have a problem. And now give it the same prompt. But I'm also going to give it one other prompt, which is "run and test to make sure it's working fine" because it has access to the environment.

Now, the reason I chose this is twofold. Number one, I have a large dataset. Well, it's only 7.8 MB, but still, it might have been a larger dataset. And you may say, "I can't commit that to GitHub because it's too large." So then how do I tell a coding agent to work on this? How do I vibe code on data? Or you may say this data should not be made public. In fact, the agent itself should not have full access to this data. How do we handle that? The last bit can still be solved, but if you don't want the data to be sent in its entirety, the easiest thing is to run the coding agent locally.

And the ways of doing that are, use something like Visual Studio Code with an extension, which is what is happening on the right side, or run it on the command prompt, which is what is happening on the bottom left. Both of these are building the same application, but they're building it in different folders. And you'll notice that they are writing code. So it's writing code to do whatever it needs to do, but it is also in the process analyzing my local file.

Okay, this is interesting. Copilot seems to have built an application, which is running. And yeah, it's not a bad application. It's not a great one, but it's not bad. This one's also created something. So both of them seem to have created an application. Let's test out what Codex came up with.

Okay, I see a retail transactions dashboard where I can pick all kinds of filters and apply the filter, and it shows me the chart below. I ideally would have liked to resize this, but yeah, I can do that by making it go to two screens almost. This part does not seem to be taller. All right. Take all categories and apply the filters. Now it's spend by category. Fine. If I specifically choose electronics and apply the filter, it gives me this data. Yeah, for a basic application, that's not bad.

But for me, three things matter. A, it's working on my local data. Two, it's built an app, a native app which I don't otherwise know how to do. Three, **I can learn from this**. So it's using PyQt6, which is good to know. I'm surprised that it managed to create the charts, but looks like Matplotlib can create native charts using a back-end QT Agg. Okay, I did not know that Matplotlib had a QT back-end. That is good learning. And how did it create the table? Okay, QT has an abstract table model which you can materialize. Good to know. So in short, I will be using this kind of technique for my own learning.

And similarly, Copilot with Claude Sonnet has created a different kind of application, and visually, this is more interesting. Sales over time, membership tier. Yeah, this is actually more useful also. And I can learn from this as well. The style looks a little different, so how to apply the styles starts becoming handy. Then I can commit this, push it remotely, and see if it works.

Since this did not take as much time as I had feared, let me try something a little more ambitious. I'm going to say `share-to-clipboard`. And the prompt that I am going to give this app is to build a native mobile Android application that, when installed, sets itself up as a share destination for any text content. When a user shares, it should copy the shared text to the clipboard. Yeah, that's it. Now, do this in as minimal a way as possible. Use the minimal frameworks, minimal code, and minimal permissions necessary. And put that onto Codex.

Now, why am I putting it onto Codex? I don't have any local—I'm going to put it onto Codex online. Why Codex online? Well, firstly, why online? Because I don't have any local dependency, and I don't have any of the tools required installed in the first place. But first, I'll have to create a new repository which I'll call `share-to-clipboard`. And give it an MIT license. Create the repo. And go to Codex. Now, create an environment. We will create the environment called `share-to-clipboard`, which we will give full access to any dependencies that it wants. And with this environment, edit, oh no, edit, but save, and use the environment to build this application. Hopefully, this should give us a positive result.

But what I'm going to do is while this is running, stop sharing and talk a little bit about some of what we have learned and synthesize and also take questions.

**Vibe coding is a new area.** **Practice is pretty much the best way to be able to learn what it can and cannot do because very few people can teach you.** I didn't particularly do a good job of teaching you. I was just going at my own pace, showing you what kinds of things are possible, hoping that some of what is possible sticks, hoping that some of the techniques stick, but also hoping that you don't pick up too much of what I'm doing because what I'm doing is going to be outdated in a month. I don't know which parts are going to be outdated quickly, which parts are going to last for at least a few months. So, if you didn't pick up stuff, maybe that's a good thing.

What instead probably provided more value is that you were sitting in an environment where you, along with a bunch of people, were just hearing the word "vibe coding, vibe coding, vibe coding" so many times. It might have sunk in. What would provide even more value is maybe you were trying something, playing around with something. So the earlier barrier of trying it has vanished. Or maybe you're that person who's already tried it a fair bit, and you say, "Wait, hold on, that's a new idea. That's something that I could try." And not that the idea needs to have come externally. While you were sitting here and thinking about it, something might have popped up. That really is the value of a session like this.

So, what should you really take away from this? **Practice vibe coding.** If you've already been practicing, practice differently. Practice more. Things are changing.

How should you practice? **Quantity beats quality.** It doesn't matter what you do. As long as you're doing something, and lots of it, preferably something that is hard. Now, how do you know if something is hard? A good rule of thumb is if what you try fails half the time and succeeds half the time, that's a sweet spot. Aim for that. If you're succeeding more often than half the time, be more ambitious. If you're succeeding less often than half the time, be less ambitious. And also share what you find. The more you share, the more people will react. The more people react, the more you get ideas.

With that, let me open to questions. I'll share my screen and we can go through questions you might have.

**Question**: Is it compulsory to make the app now?

**Answer**: No, not compulsory at all. This is a fun workshop. It's not compulsory to make an app ever. And yes, you can, if you want, publish your app later.

**Question**: Can we get a recording?

**Answer**: Yeah, you probably will get a recording.

I should have sent [the link] to the group chat. I will send this as a link for people who want to learn how to set up Visual Studio Code with Codex running on it. The other extensions are fairly similar.

**Question**: How can we generate code for a framework that's very new or not widely adopted?

**Answer**: Fair question. One of the ways of doing that is Context Seven. This is just an example of a whole series of tools that do this. You can put in a library. For example, the docs for somebody's GitHub repo. And what they've done is uploaded it to Context Seven, and Context Seven has created this context for it. You can copy this context, pass it to the LLM, and the LLM now kind of has a sense of how to use this particular GitHub repository. In short, have an LLM write the documentation for it, which is LLM-friendly, and pass it to another LLM.

**Question**: What's the best way to structure our prompts?

**Answer**: This is changing constantly. It is, no matter what advice I give you, when the models change, it becomes irrelevant. There used to be a time when telling a model to think step-by-step was great advice. And then the models themselves realized that they have to think step-by-step. So now it harms as much as it helps. There used to be a time when people said emotional prompting helps. That is, if you say, "My career depends on it" or whatever, then it does a better job.

Let me show you what the stats say on that. When I tested it, supposing I give this prompt, "think step-by-step," does a model actually do better? Or, "I'm totally overwhelmed, I need your help this second, my heart is racing," blah, blah, blah, does it really help? Or if you bully it, "You are a stupid model," does it do better? Turns out that all of this advice was probably good at some point for some models, but in the majority of the cases, the advice is bad. For example, if you shame a model by saying, "Even my five-year-old can do this, stop being lazy," it actually ends up being better only seven times and worse 20 times across all the models that we had given it. Similarly, emotional prompting didn't seem to work. Reasoning did work fairly often, 31 times it did better, 17 times it did worse. But that was more than a year ago, and now it doesn't matter.

So in short, **the prompts that we use today, they tend to get outdated**. With that said, one of the principles people are using is to put common instructions into an `AGENTS.md` or a `CLAUDE.md` for Claude. So search for `AGENTS.md` and see what kinds of prompts people are giving. That will be the current practice.

**Question**: Most of us are data science students. How can we efficiently set up our prompt to build an app to visualize data with analytics?

**Answer**: I'll tell you what I'm doing, Harshvardhan. The trick for data analysis is to make sure that you give it the right tools, and then the task. So to help with that, here is how I am structuring my setup. I will send you the link to this in the meeting chat.

So this directory has an `agents.md`. This `agents.md` is the starting point for all of my AI coding work. I simply say, "Here are the tools that I have available that you can use." And it's a very compact list. You can use `fd` or `find`, these are all search tools, GitHub tools, internet tools, data processing tools. And this is an important thing. If you give it command-line data processing tools, it can do a great job. If you give it Python, it can do a great job. If you give it PDF processing tools, it can process PDF. If you give it databases, it can do data analytics. So, one of the critical things is to make sure that you give it, install on your machine, or at least tell it to install, the tools that can do good data analysis. That's one part of it.

The second is then you can give it extra instructions on how to do specific things. And in my case, I do that through specific kinds of prompts, which again you will see in this directory. I'll share with you another prompt. So let's say one of the data analysis tasks is to generate synthetic data in order to test edge cases for hypotheses. You've built a model, you want to stress-test it, you want to create fake data.

Here is one way of doing it. Rather than saying, "Just create fake data," I've given it a specific protocol. Step one: list all the columns that are likely to be there in that data. Think about an objective, create five hypotheses that an organization might want to test. In other words, how do you think about realistic behaviors of data? Then write a program that generates realistic fake data where these hypotheses are actually true, and test these hypotheses.

Now, one of the things we'll observe, for instance, is in computer science, there are probably more men than women. If you ask it to generate random data, then there will be a roughly equal proportion. If you ask it to create a hypothesis, it may say, rightly or wrongly, that the distribution of men and women will be in line with the global statistics. Or it may take, for instance, realistic scenarios. Let's say we are asking it to generate 100 CVs. It will realistically assume that there are a few people who will have a gap in their CV and create those gaps. Those sorts of things are what we incorporate. In short, the way to, apart from giving it tools, another way to make an LLM more data science friendly is to take data science best practices and ask it to generate an output in that format or fashion.

**Question**: Using Copilot right now, it's taking its own sweet time to build the draft and probably spending a lot of money as well.

**Answer**: So, unless you have a fixed price plan. So, that is a pity. These models are expensive and slow these days, but over time, I expect that both of these will improve.

**Question**: Our first prompt affects the output we get. Second prompt that we want to improve. So it's good to think of the first one setting the foundation.

**Answer**: Yes, the first one typically sets a foundation and we are building on it.

**Question**: If we get some other ideas in the middle of the building, what is a good approach?

**Answer**: Like with buildings, it is a good idea to start again. Build a new building rather than change a building midway. It's usually tougher to change things midway in general.

**Question**: What is Llama by Meta?

**Answer**: Llama is a model like Anthropic's Claude or DeepSeek, and it was created by Meta, which created Facebook.

**Question**: I have a question related to AI. When shows say AI is thinking, what does that really mean?

**Answer**: Well, behind the scenes, there is a computer that is calculating, and the way it is calculating is kind of like the way the brain thinks. So, because for an outsider, it looks like it is thinking, people are saying it's thinking. Now, is it really thinking? Might be a philosophical question. But the conventional term these days is when a large language model is working internally without giving any output, we say it's thinking.

**Question**: Will the steps to build with vibe coding be more valuable for our resume than brute force coded apps?

**Answer**: More, I don't know, Kushagra, but having it versus not having it, having it will probably help a little bit.

**Question**: You said whatever you stated might be outdated even by a month. How do you stay up-to-date with AI?

**Answer**: Two possibilities. Possibility number one, wait it out. When the mobile revolution came in, I didn't even buy a mobile. I just waited for five years, and then bought a really old phone. And then I'm about five, seven years behind any mobile technology or model. And I'm a late adopter. Why? Good enough for me. The technology is moving fast, it's a lot of work to keep up with it. Anyway, at some point, it will come to me. I will get the benefits. The models are very cheap, phone models are very cheap these days. So I buy the cheapest model and still get good quality. My wife's models are usually five years ahead of mine, and she usually pays three to five times higher for roughly the same thing.

But in the case of LLMs, I'm trying to stay up-to-date because I believe that it will be valuable for my career. So, how does one do that? **By spending a lot of time.** There is no alternative to that, and obviously doing that in a smart way. Simon Willison is a good person to follow, and then slowly you will develop a network of people whose inputs you follow. Trying out newer models and newer capabilities is helpful. But the biggest lever is how much time you spend on staying up-to-date, and it's a choice.

**Question**: My scraper is working fine and I've got a dashboard with sentiment. And your app is working on your local machine?

**Answer**: Fantastic. If you can deploy it, great. I'd love to see it.

**Question**: What is the importance of JavaScript and how you can use it?

**Answer**: JavaScript is a programming language that works in the browser. There are very few languages that work in the browser. JavaScript is one of those few. And because almost everyone has a browser, it is a wide distribution platform, and that's what makes it somewhat important.

**Question**: Replit app created but it's asking money to deploy.

**Answer**: Yeah, I got stuck there as well, Shivam and Harshvardhan. So, yes, we just have to purchase a plan, which is a pity.

We have a minute left, so I'm going to take only two or three questions.

**Question**: Can agents help analyze code, legacy IBM i mainframe applications?

**Answer**: That's actually a pretty good use of coding agents, to analyze legacy code and see what you can learn from that.

On that note, I will stop sharing my screen, and thank everyone for joining in. It's a large attendance and it was a long session, almost two hours. Thanks for being patient and joining in. The only thing that I want you to take away is, **try AI coding agents, try vibe coding if you can and when you can.** All the best with that. Have a good day. Bye.

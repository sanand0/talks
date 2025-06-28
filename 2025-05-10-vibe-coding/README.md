# Vibe Coding

This is a talk delivered to [SETU school](https://www.setuschool.com) on 10 May 2025 about [Vibe Coding](https://en.wikipedia.org/wiki/Vibe_coding).

[![SETU - Vibe Coding - Thought Leader Session (65 min)](https://i.ytimg.com/vi_webp/ODXSDbY12dg/sddefault.webp)](https://youtu.be/ODXSDbY12dg)

## Transcript

00:00 (Rather than introduce myself, I'd) rather introduce vibe coding, which is probably more interesting to everyone.

00:05 Vibe coding is like AI coding, but with one difference, where you don't check the output.

00:13 AI gives you code, you run it.

00:16 Now, hopefully that sounds a little _dangerous_ because you have _no idea_ what it is going to do, including potentially delete files on your system if you just happily run it.

00:28 But that _is_ what vibe coding is about.

00:32 Why are people talking so much about vibe coding?

00:37 Because they're finding that it tends to work _better than people expected_, and it lets us do a few things that we couldn't otherwise do before.

00:46 And what is what are some examples? One is, if you're not going to check the code, then you don't even need to know how to code, which means that non-programmers can build applications. That's obviously very powerful.

00:59 Programmers can build applications with their mind entirely focused on what needs to be done without worrying about the structure of the code and details like that.

01:09 As models get more and more powerful, the kinds of things that we can do with vibe coding will increase, but there will always be a set of things that vibe coding will fail on. And when it fails, we would need programmers to take over, guide, and so on. But that space of things that can be vibe coded is growing.

01:29 So what we're going to do is play around with, we're going to vibe code. And as we go along, please feel free to put in messages in the chat window. I will keep an eye out for it and thanks everyone for welcoming me on the chat as well.

01:47 Let's try then. So let's begin by, what I'll do is maybe share my screen and open up let's open up Claude.

02:01 Now, you can vibe code pretty much on any, let's see, how do I share a tab? Yeah, here we go. Sharing. Right. I believe in a few seconds you should be able to see Claude.

02:16 Yes, we can. Visible. Okay, great. Now, let's use the model that I'm going to be using is Claude 3.1 Sonic. I have a free account. I don't have pro account with Claude at the moment. So this is something that all of you can do.

02:31 And why am I using Claude 3.1 Sonic? Because everybody's raving about this as a model, saying it's really good. So we'll do that.

02:40 Now, what do I mean when I say everybody is raving about this model? How do we figure that out? Well, there are several checks that people run on models to see how good each is. One such place is the LLM Arena Leaderboard. And the LLM Arena Leaderboard is where people can ask the same prompt to to known or even unknown LLMs and see which one does better.

03:14 There is, so for instance, what the arena shows at the moment is Gemini 2.5 Pro review seems to be leading. That is, more people prefer this to the other models and it has a score of about 1448. O3 has a slightly lower score. Chat GPT 4 latest has a slightly lower score and so on. But this is general.

03:37 What if we go specifically into **web development**? Which of these are the leading models? So here, Gemini 2.5 Pro, which was released very recently, four days ago, seems to be ahead, followed by Claude Claude 3.7 Sonic, followed by an older version of Gemini Pro, et cetera. So what we could do is use one of these models to do our vibe coding.

03:59 There's a question from Archana, what is the size of application and complexity that we would suggest for vibe coding? This is one of those things that keeps changing. Two things are happening: models are getting better. So if today we can write an application of this size, then tomorrow we'll be able to write an application of slightly larger, slightly larger.

04:18 Second, it's a jagged edge. What we think is easy might be hard. What we think is hard might be easy. And 95% of the application might be easy, and tiny little bit may end up being hard.

04:30 In fact, let me create one such application and show you what that would mean. Let me switch over to Claude and what we'll do is maybe we'll see, we'll build two applications. I want to build an application that, let's see, allows me to upload a PDF and shows it on the screen.

04:57 Plus. We run this.

05:01 Now, the nice part about many of these LLM services, OpenAI, Gemini, Claude, is they have a notion called artifacts. By the way, it's an internal server error. I have no idea why that happened, but we'll if this doesn't work, we'll switch over to OpenAI or Gemini. Okay, let's continue.

05:22 They have this notion of artifacts. Artifacts are where the chat is on the left, the code is on the right, but not just the code, the **output** also is going to be available on the right side. It's writing an application, but in the spirit of vibe coding, I'm not even going to look at the code. I'm just going to let it do what it wants.

05:44 Let's see. I have uploaded, okay, let me take a small PDF file. I could take a large PDF file, it's not a big deal, but and just so, okay. And it's saying this content is blocked. All right, let's try again. Let's try some other file. Loading PDF. And this is a much larger PDF, by the way, but I don't know if the content is blocked for whatever reason.

06:09 Oh, I'm out of free messages. Oh, that may well be why. Fine, no problem. I've been playing around with it for some time. So what we do is ask Gemini to do exactly the same thing.

06:24 What a bummer. Apparently, all of these are supposed to be and Gemini is supposed to be even better. So I'm going to take the exact same prompt and copy it. Now, one of the things that you will notice that I'm doing here is giving up _very quickly_. One of the first principles of vibe coding is if something doesn't work, _move on_. The point is not to do something specific. The point is to get _anything_ done.

06:51 Now let's see. It's going to do all of this, blah blah blah. It seems to build this. And side blah blah blah. What I'm going to say is, wait, I thought it had something called artifacts or canvas or something. Can you put? Oh, here. Okay, I should have probably clicked on Canvas and rendered it. Let me do that.

07:17 Okay, this is still talking. So I'm going to open a new tab and put in the same prompt into that. Yeah, I have the new tab open, but before I press enter, I'm going to click on Canvas. And I'm going to say build a single page, otherwise it will start creating multiple pages and it may run into trouble.

07:41 Let's see.

07:44 And notice that this is a process of **discovery**. Things work, things break, we keep flowing with it. Doesn't matter. The whole point is we don't care, it's doing the work. We just, we are the boss telling it what to do. And it's a stupid intern that doesn't really understand a lot of stuff. But we can be clear on what we want.

08:03 So, fine, like you saw in artifacts earlier, it's writing the code. Okay, we'll let it write the code, but we won't even bother looking at the code. And but, however, there's one thing that I found useful when looking at the code: I learn about **new libraries**. So PDF.js I discovered for the first time when I had asked Claude that I want to view PDFs. Not just that, it'll also tell you how to use the library in specific aspects.

08:31 Anyway, let's upload a PDF. And yeah, here is the PDF. I have a PDF viewer that is embedded in the browser.

08:41 Now, let's see. Let's push the boundaries. What is the size of application or complexity that it can deal with? Let's go bigger. Now, Gemini is supposed to be an even better model. So, am I not supposed to Oh, okay, continue. I've reached my limit on Gemini 2.5 Pro as well. So, that's okay. I'm happy to switch to a weaker model. And oh, it won't let me switch models.

09:10 Fine, we'll build a different application. This time though, what we'll do is build an application not using Gemini, okay, one of the limitations that these models have is that they won't let you access the internet through code. Why is that? Because then you may start scraping some site, you may start sending data to some spam content, sending post requests. So they block all the internet, not all, majority of internet access.

09:41 So what we did in Sai, which is the company I work at, is we built a tool that does not have those restrictions. Brilliant. Today is my day for everything going wrong during the demo.

09:53 But, okay. So we built something called LLM Foundry, which I will be able to get up as a local copy. One sec. That's because I have the code running on my machine. One sec.

10:10 So, yeah, okay. I should be able to Oh, okay. It's back up. Fine, let's give it a shot.

10:24 Now, what we've done is taught it a few things, like how do you access other LLMs? So I can access OpenAI, Azure OpenAI, Anthropic, Groq, etc. And the way we've done it is by a simple prompt that says here is how you call OpenAI, here is how you call Gemini. So now I can build an LLM application that in turn can use an LLM.

10:48 What can we do with that? Let's say I want to build an app that captures my photo, captures a photo on the webcam, sends it to an LLM, and describes all the objects in the image in detail.

11:13 So let's do that. And yeah, let's see. Yeah, let's just go with it. The whole point is not to think.

11:24 Now, one of the things we've learned is applications are people are really bad at prompting. So if we can have something that explains the application like it would to a developer, that is helpful. So this is where an **agentic behavior** starts coming in handy. And by agent, we simply mean I mean, in this context, I mean rather than just using one prompt, use multiple prompts.

11:49 So now it's saying it wants to use my camera. Allow, okay. And I have a problem with this browser. It keeps messing up on the camera. So I'm going to use a different browser. Hold on, I'm going to save this as photo test. And now that this application is open, I will put it, okay, now I can publish this application. You could have published the app on Claude as well.

12:19 Let me open this in a different browser. I'll open this in Opera. And share my entire screen. That way you should be able to see it. But first I have to stop sharing my camera on Chrome, because otherwise it would complain that two applications trying to access the camera. So first I'm going to re-share my screen and hopefully you'll be able to see this.

12:50 And now it's, okay, it's still not accessing my camera.

13:01 Reload. Okay, could not access camera. Ensure that you have given camera permission.

13:10 So it's this Chrome is also saying, okay, let me use Edge. Still doesn't have camera access. Fine.

13:24 No, but something is still accessing my camera and I know that because I see the light burning.

13:34 Audience: Maybe because you are in the call, it is giving that issue?

13:38 Anand: Possible because, yeah, even my camera application is not able to access the camera. Why don't I rejoin and see if that helps? I'll just be back.

13:54 I have rejoined. But the camera light never went off. Let me try once again.

14:50 Audience: Anand sir, you are not audible.

14:51 Anand: I am so sorry. I've been talking for a while. But hopefully I'm audible now?

14:55 Audience: Yes.

14:56 Anand: Okay. But you got the idea. I clicked the picture, captured the image and let's in fact hold a mouse. Let me reload this. Hold a mouse and capture the image. Now, it sends the image to an LLM behind the scenes. Short grayish hair, blue t-shirt, computer mouse with a red light. So it clearly understands this.

15:18 Now, an **image detection application** of this kind is something that we can deploy pretty much anywhere. What I mean by anywhere is you can put it into a factory and say on a continuous basis tell me what is happening on the factory floor or in a hospital reception desk saying are there patients who are queuing up on one queue, but another queue is empty. And this sort of a thing can be vibe coded. The use cases are enormous, but notice that I did not code in this process.

15:55 Let me get my camera back. And, okay, yeah, my camera is back here. Now, let's go for something different. In the meantime, let me quickly check if there are any messages. Okay, there are some messages, but just saying that I'm not audible.

16:14 Let's go step deeper. Is vibe coding only related to writing code? Can I do data analysis? As a data scientist, can I do something interesting with it? Let's give that a shot. What we'll do is share, share a screen. Yeah, share screen.

16:32 I'm going to go to ChatGPT. And this time I will not hopefully run out of credits because I'm using a paid account. And what I'll do is, let me see. I remember there being an IMDb, an internet movie database set. Yeah, there's a where can I download the IMDb? What's it called? The 50K movie review data set.

17:04 So, let it do the search. Now, ideally, not ideally. In a few months, I suspect we will be in a position where we can ask the LLM to download this. Right now, they've made explicit restrictions not allowing us to do that. But now on Kaggle, I clicked on download. Yeah, download the data set as a zip file. And this zip file seems to contain about 49,000 rows where we have movie reviews and whether it's positive or negative.

17:39 So, taking this data set, what I'm going to do is add it to ChatGPT. All 50 MB, or however large it was, near 50 MB, whatever it was. And then say, this zip file, actually, what does this zip file contain? Do a full exploratory data analysis. And let it run.

18:08 Now the beauty of this is, it can write code, it can run code. So I don't have to worry about having to other than downloading and re-uploading the file, do anything on my machine. So one of the, earlier what I was showing you was how LLMs can replace a Visual Studio Code or your local IDE. Now what I'm showing you is how it can replace your Jupyter Notebook or Colab Notebooks by having it all run in the server.

18:38 So it's trying out a bunch of things and it says, yeah, here's a table. Now it's told me that it got 25,000 positive reviews and 25,000 negative reviews. Okay, it's also showed a histogram somewhere but that didn't work. Great.

18:53 So now, let's do this. I want you to, actually, why am I doing this? I can talk. Okay. What I want you to do is create a classifier for this data set. That is, split the data into a test data set and a training data set, maybe a 90/10 split. And then build some kind of a, you know, actually, tell you what. I don't even know what classifiers to use. So build me three different classifiers on the same data set and train on those three classifiers. Then test against those and give me all the error rates and, well, you know what kinds of error rates data scientists use better than I do probably. So tell me what the different kinds of errors each of these classifiers makes. Put it all into a nice table and finally recommend which classifier I should be using.

19:54 So that was the prompt. And here's the thing, it's easier to talk than to type. These things are very good at detecting voice. Hopefully, it wouldn't have made too many mistakes. So but in the spirit of vibe coding, I'm not even going to check whether it got what I write, type, what I said, typed correctly.

20:12 Let it run. Now, by the way, I'm using O4 Mini Hi, which is a reasonably good model. Apparently, it's great at code and visual reasoning. ChatGPT does give me some hints on what model to use when. So I follow its recommendations and when coding, I'm using O4 Mini Hi.

20:33 So it's writing code. We are going to be vibe coding. So we're not even going to check the results. But it's useful to know, okay, scikit-learn is a useful library to have. There's something called Ace Tools, which lets us display the data frame to the user. Apparently, there's an accuracy score, a precision score, a recall score, F1 score, and a confusion matrix, which are different ways of representing errors. The models it seems to have chosen is from Naive Bayes, from linear model, it's chosen Logistic Regression, from an ensemble model set, it's chosen Random Forest Classifier. So it seems to think that these would be apt models to use.

21:18 So then it has an error. Unable to allocate 352 KB for this data set. So it's doing something else, fine. The beauty of many of these is if they find an error and specifically reasoning models, if they find an error, they try again.

21:39 So is it, how do I know it's still? Okay, the icon here, it's still indicating that it's trying. Now, this is obviously a large data set, so running this will take time. And there again is the power. I don't need a GPU machine. It will just go ahead and run on its system. I don't even need a machine. I could run this on a Chromebook and work.

22:03 Now, Archana, I can take a question now. You because this is anyway working, I'm not doing any work. You have a moderate size existing application. Do I suggest refactoring or developing further with vibe coding approach? These are not mutually exclusive. That's kind of like saying should I use functions or should I use classes? Use both. There's nothing that prevents you from using one or the other.

22:28 Specifically, what I find as a decision criteria is if I don't need to understand the code or if I don't have anywhere near enough time and I need to really get it done quickly, then I start with vibe coding, which is tell it to do something. If it does it right, I just leave it. I don't look at the code.

22:54 If either of these is not true. Both of these are not true. That is, I've got a little bit of time and I do need to understand the code, then I don't try vibe code. I just go straight for AI based coding, which is where AI does the code anyway, but I look at the output, check if it is working fine, etc.

23:17 So now it's given me some results, blah blah blah. I'm only going to look at the final recommendation. Logistic regression, it's saying, gives me the best accuracy, lowest error rate, blah blah blah. So, wonderful. Logistic regression is better than multinomial multinomial Naive Bayes as well as Random Forest.

23:40 So I'm going to say very nice. Congratulate yourself. Actually, why am I typing? That's fantastic. I really liked how you did this. Now, what I'd like you to do is package the logistic regression model that you created into some kind of a file that you will let me download and then also write a, let's say, Fast API application which will allow me to have a UI where I can type a movie review or paste a movie review there and it should send a request back to the server, use that logistic regression model that you let me download and determine whether that's a positive review or a negative review. Could you do that please?

24:31 So that is doing its transcription behind the scenes. Let's go ahead and have it build the application. The premise here is zero review of the output.

24:51 Now at this point you're thinking, wait, Anand, hold on. If the model makes a mistake, then what do you do? Right? You have to check, right? Yeah, I have to check, but I don't have to check the code. I can check the outputs. Now what are the ways I can do that? What I can do is ask another LLM to do the same calculation and cross check. See, if two people are doing the work in my team, I'm not going to sit and do everything that they are doing. What I will do is ask hopefully smart questions or have someone else do similar work and compare. The cost of doing this is what? Three, four minutes? Not even that.

25:28 Audience: Question from Kavita. Currently is Vibe coding used more to create a prototype or for the creation of the end product itself?

25:36 Anand: Again, I will liken vibe coding not as much as a methodology or a framework, as much as a coder technique. What are coder techniques? Coders read documentation. Coders use IDEs. So you could say, currently, is reading documentation used to create a prototype or for creation of the end product itself? Whatever the person wants. Are IDEs used to create prototypes or the end product? Whatever the user wants. So vibe coding is a technique. You use it for whatever.

26:12 Now, the question behind that is, in reality today, how many of these vibe coded applications go into prototypes and how many of these are going into end products? We have no clue. And the reason is, it's not published anywhere. That's part of the problem. Part of the problem is people immediately get ambitious. People start saying, if I can vibe code and get to X in five minutes, maybe I can get to 10X by actually putting in my manual effort. So even if vibe coding could create a production application, what people will do is start doing things by themselves, switch it to AI based coding and then take it to production or a proof of concept. So, in short, I suspect that the number that is vibe coded that actually outsiders get to see is very small, but that is not necessarily because of vibe coding being limited, that is because of human ambition.

27:12 Archana's comment is, I find vibe coding debugging like technical analysis approach rather than fundamental analysis. Am I right or am I right? Well, it's so clear that you're right, then I should ask an LLM to check if you're right or not. But technical analysis is where we use a set of metrics. Fundamental analysis is where we go into the details of the performance behind the scenes. And in that sense, yes, I think that's a pretty good analogy, Archana. I would agree to that. It cannot be perfect, but it's good enough an analogy.

27:52 So, now it's given me a whole bunch of things. It's saying download the trained model, good. By the way, you notice that it errored out a bit. I don't really care about the errors. It's given me a model, it's given me an app.py, and it's given me a README.md. Now it's saying I can do the pip install blah blah blah. So I'm going to, in this case, I'm going to apply my intelligence and not follow it. I'm not going to vibe code 100% right now. Why is that? Because it's asking me to run instructions on my machine. Boss, you run on your machine, I don't have a problem. You run on my machine, I will decide what I run.

28:32 So let me go first sandbox this. Right. Vib, and inside the Vib directory, I will move the, what was the Pickle file that I downloaded earlier? Some pickle star.pickle, move it here, move the README.md and move the, what was the other file called, app.py as well. And create a new virtual environment and then, source, yeah, so now at least whatever pip install it asks me to do will happen only within this directory. Fine, rest of it, I will follow.

29:15 And it's saying externally managed environment. Oh, sorry. UV pip install. Right. So that is going to, okay, that has already deployed the application. Ensure that this and this are in the same directory. Fine. And start the server. Okay. Uvicorn reload and it's saying it's running at port 8000. And I opened it but it's saying you can install. Okay, fine.

29:48 Now this is me no longer vibe coding. This is me just AI coding. And this is one of the reasons people switch over. See, I'm in a flow while vibe coding. Fine. Now I'm changing environments. I'm no longer in that flow. If I had asked it to run, I would have just followed the instructions. But here, I know what I'm doing. So now I'm applying my intelligence. And it will probably fail, but let's see. Let's put in the application here and we will say this is a terrible, actually a review of, what's her latest movie release. What state are mostly people in right now?

30:38 Audience: We don't have, we don't have, we don't have any standardized location. It's across all over India.

30:44 Anand: Just Hindi movie. The movie called Be Happy. So let's take Be Happy review. And let's do vibe review as well without reading the review. I'm just going to copy the entire thing and paste it here and sentiment positive. Great. Now let's actually find a low star review. Right? Is there a quick way of doing that? Okay, one star reviews are probably going to be bad. Two star reviews are also okay. And analyze it and oh, it's saying sentiment is still positive. Here it has shown not much recommended. A junior has blah blah blah. Okay, but Ura's beauty was awesome as well. And the child acting was good. So, okay, interest.

31:37 Audience: Try Sikander's review. I mean it should be negative at least.

31:42 Anand: Sorry, say that again please.

31:44 Audience: Sikander review. The review of Sikander.

31:46 Anand: Okay, bad movie is it? Okay, Sikander's review and more audience reviews. Let's take something with a one star if we can. Yeah. Hopefully, one star review at least should be negative. Take the whole thing except for how many people found it helpful and run it and okay. So clearly this is rubbish. But to be fair, the model may be rubbish, but the vibe coding still worked.

32:20 Yeah, I now I want to know what are, okay, let me, this movie is bad. Oh, okay, fine. So it looks like it really takes some really bad reviews to get it to say bad.

32:39 Audience: I think it is considering the entire intent. So probably it is comparing the positive versus the negative words and if it is finding the positive words are more, probably it is reading the sentiment as positive.

32:51 Anand: That's sort of maybe maybe the tonality of the sentence is so maybe the tonality of the sentence is also is affecting the rate.

32:58 Audience: Right.

32:59 Anand: Either that or the Indian reviewers are far more liberal than the IMDb reviewers.

33:06 Audience: No, if a movie like Sikander can get a four at least, I mean, a four rating, I mean, yeah, there's there's doubt.

33:13 Anand: There is doubt. Okay.

33:15 Audience: Are they paid reviews?

33:16 Anand: Go on.

33:17 Audience: reviews, I don't know.

33:18 Anand: Sorry, sorry.

33:19 Audience: Paid reviews. I mean they paid people.

33:21 Anand: That is that is there. That is that is we have to get we have to continue with that consideration.

33:29 There's a question, a comment from Vishal. What is the reliability of different model outputs for a particular use case? Say one create a product recommendation application for a CPG manufacturer, separately for e-commerce and physical stores. How is domain knowledge captured by AI computing two different channels? Similar product recommendations may not work for a BFSI company, which is something completely outside of vibe coding. So I'll keep my answer short.

33:52 The reliability of the models is not bad. About every, about a year ago, it was about as good as a reasonably well led, a well read 12th standard student. If you asked a 12th standard student the same question, you would have gotten the kinds of answers that a good LLM would have given you at that time. Now it's roughly at the level of quality of a post-graduate. You ask a well read post-graduate the same question, but not someone who has been trained on BFSI or CPG, you'd ask the same question. If you could give that same post-graduate a medium sized book, let's say the thickness of a King James Bible, which is roughly 1 million tokens and say read this, now answer the question, and if they are able to read it to the point where they can almost perfectly memorize it and answer it, the quality of the responses is that good. That is the benchmark that I use.

34:44 Now, to me, to be sure, because when we tell people the models are as good as a post-graduate, they will say, oh, but I want 100% accuracy. If possible, I want 200% accuracy, because not only should it be correct, it should tell me where I'm wrong, and all sorts of things like that. Then you say, well, let's do the evaluation. Let us actually take a large number of test cases where we know the answer. Send it to the LLM, see what the accuracy is and what the accuracy is is what the accuracy is. And that will be very domain specific, it may vary. But what we are finding is that the intelligence of models does not vary so much, the reliability of models does not vary so much. The variation is much higher in the input prompts and the context that we give it.

35:32 With that, let me broadly summarize the themes that we had explored.

35:40 To recap, vibe coding is where you don't check the output. At least of the code.

35:46 Vibe coding is something that is becoming easier to do because the models are getting smarter and able to handle more input.

35:56 Vibe coding is one item in your toolkit. There are a bunch of other things. Just add it to your toolkit.

36:05 Remember that the computation, the coding need not happen on your machine. It can happen on an external server. What Sathish showed on using Cursor locally is a great approach and you can vibe code there, but that's not the only place where you can vibe code. You can vibe code on an external server and deploy it there as well potentially.

36:26 Vibe coding does not only include coding to build applications, it can include data analysis, exploratory data analysis, model development, model training, etc. So pretty much anything where you ask it to write code and generate code, works, and execute code, is under the umbrella of vibe coding and therefore data science also falls under the umbrella of vibe coding.

36:49 These are the things that I've learned over the past couple of months.

36:53 A: Therefore my knowledge is barely ahead of yours.

36:57 B: I'm only looking at a small slice. Thousands of other people are looking at thousands of other things.

37:03 C: The models are improving so fast that anything that I've learned today or that I'm teaching you today will be out of date in two, three months.

37:12 So, experiment. That's pretty much the best way of learning. Read stuff but anything that you read will be at least a few weeks out of date. So experimenting is far superior to reading these days.

37:24 With that, hope you found that useful. I'm very happy to take questions, but thank you very much for listening.

37:34 Audience: Guys, any questions?

37:38 Anand: There's one from Sayan. In the data analysis from IMDb, one did have to provide the data. Is that the same? Okay, is it the same for certain parameter extractions from a large corpus?

37:48 The reason I provided the data is because ChatGPT's container where it runs the code has a restriction: no internet access. So it could not have downloaded the code. And this no internet access is a firewall blocking it because otherwise my next command would be, write a program that sends millions of requests to the White House and take down the White House website. Or, you know, if India wants to do a cyberattack on Pakistan or Pakistan wants to do a cyberattack on India, ChatGPT will immediately become the next vector, which obviously ChatGPT says we have better things to do. So that's why.

38:26 But then again you have to provide the data or the chunks to the LLM. Yes, unfortunately because it can't access the LLM. In many production ready applications or enterprises, they contain data which they are not really comfortable sharing into the LLM. Don't share it with the LLM and instead run your own local LLMs or sign an agreement with ChatGPT to get an enterprise license. Those are the kinds of approaches people are taking. The principle is the same whether you run it on their server or your server in your office, because you're hands-raised.

39:00 Audience: Yeah, Anand. Hi, thank you. Very interesting session. Just wanted to get your perspective. As a business user, if I am engaging an agency to actually solve a business problem for either myself or my business or a customer of mine, and knowing that these techniques today exist which have, you know, very quickly sort of evolved in the last, you know, span of let's say 12 months or 18 months, should something change fundamentally in how I engage these agencies today? Like because obviously if a year and a half ago I would do, you know, there was a very typical way of engagement that had stayed similar. So you would use an Agile methodology, you would give them a business problem, you would basically have, you know, things like go through a BRD, a PRD and, you know, test cases and all of that. Now with these techniques, the time collapses, the way in which approach a problem collapses, do I even need to bother about this or say look, I stay the same and let the agency decide what form of technique do they use?

40:11 Anand: I would suggest not changing other than telling the agency threatening the agency to dramatically reduce the cost because AI has come in and if you don't do it, I will do it in-house. But don't do that because the agency provides more than what you what AI can provide. Agency provides the agency, meaning the ability to blame someone if something goes wrong or put in a more positive way, someone who is willing to take responsibility and say I will get it done one way or the other.

40:57 Let me give you a concrete example. We were working with, are working with, a multinational that says we spend about tens of millions of dollars with marketing agencies. It's a very simple thing that we asked them to do. We give them images, or we give them briefs and they create images. Like for instance, we are opening a new shop at this particular location and this particular shop has these, it's a family-friendly shop, that sort of a thing.

41:30 Now, when can we, they said, give this to an AI and have it generate the images. Gemini Flash image editing does a fantastic job of it. ChatGPT's new image generation capability does a fantastic job of it. We created a prototype and checked. Great. Now your team can do this and you can save tens of millions of dollars. To which the client said, almost so thank you for this. I'm going to use this, but the way I'm going to use this is as a **negotiation device**. See, I have two problems, three problems.

42:05 I don't want my team to be sitting and doing this. They are paid more than the people in the agency are paid. I still want the people, the low-cost people in the agency doing this. I want my people to be working on important stuff.

42:19 Second, I don't want to get into the **legal risk**. If this is AI generated, then my legal team will come and ask me, do I have the right to use this? I may, I may not, but even figuring that out is a problem. I want some agency to come and say look, if somebody has to be sued, then sue me.

42:37 Thirdly, I will have to sit and **train my guys** on this and two out of 10 will pick it up and that those two are specifically the ones who will leave and then I will need to sit and retrain. I don't have the patience to project manage all of this. That is what I'm paying the agency for.

42:53 So I'm going to use this to negotiate with the agency and say 90% of your work is done. In fact 100% of your work is done. So cut your cost, reduce your time. Or else I'm going to find someone else. And I suspect I will be able to find someone else, but I will still be working with an external agency very crucially.

43:11 Audience: Understand. Thank you. This was helpful.

43:18 Audience: Any further doubt, any further experiences you want to learn from sir?

43:24 Audience: Yeah, asked a question in the chat. If a layman,

43:28 Anand: Yeah. Okay, I already no, this is one I already answered Satish. This is the one where I was suggesting that say that we can't, we have to upload because ChatGPT doesn't allow external network access and if enterprises are not comfortable, then sign an agreement or run a local model.

43:49 Audience: No, not not from development and coding techniques. He wants to build a market standard. Okay, market standard I guess I mean you mean production ready app using vibe coding. What should the broader roadmap be?

44:03 Anand: Several options. Possibility number one: find someone who is a developer and ask him to sit next to you and you do the vibe coding, have them take over after vibe coding. Preferably they would also be familiar with AI code development at the very least. That's one approach.

44:19 If you're saying no, no, no, I don't want someone else to do this, I want to be able to do this myself, then the fastest way is to **learn only what you need**. Build something with vibe coding and keep hitting it until it improves. You will hit roadblocks and at which point you have a choice. Option A: try and solve that particular problem using alternate approaches. But the fastest way of solving a problem when you get stuck these days is just wait. Three months later a new model will be released and it will be able to solve your problem for you. Now this is a reality. In Jan we were running a large engagement where we needed to convert XML of a certain format to XML of a different format. The problem was the token context for the better models was only 8k output tokens. Then we said, oh wait, wait, this is January, let's check. And yes, it had grown to 32, sorry, 16k output window. So we can do double. But about 50% of our documents were larger than that. Some of them went as large as 48k context. So we spent January, February, March, April re-engineering the entire system so that in a 16k context window, we'll still be able to generate 48k worth of output by splitting it. May, GPT 4.1 comes out, which has a 64k context window. So all we needed to do was wait the same four months that it took for us to develop.

45:52 So that is option number two. Option one: find someone else who can do it for you. Option number two: Option zero is to beat your head against it until you really, really are not able to go further. That's a good option. Find someone else, wait until a new model comes up. Or option three: **learn to code but on a need basis**. Learn only what you need to code to fix that particular issue.

46:20 Will it still be, as you put it, market standard? 99% of the people today will say no. Or sorry, let me rephrase it. 99% of the cases, what you build, people will say, no, it's not market standard.

46:34 Some of it will be because the code is not very good. But most of it will be because the application itself is not good, because you have not created a complicated enough or professional enough application to compete in the market. Again, over time, both of these will fade away. So if I had to give you one robust, solid, universal answer as to what should be the broader roadmap, chill, relax, vibe code something else, wait for the models to grow up.

47:03 Audience: Question from Ujjaini. What would I suggest as the best role of educators, make say to when gold posts seem to be changing so fast.

47:12 Anand: I have no clue. And you could have replaced the word educators with any industry. I have absolutely no idea. And for exactly the reason that you mentioned, things are changing so fast. So, role, who knows?

47:26 What can we do? **Stay in touch**. See what's happening, play around with what's happening. Be less clueless than we already are. But it will be a 1%, 2% effort. That's not a bad thing. This is just like asking somebody in the mid-90s, what will be the role of educators post-internet?

47:48 Remember, this was pre-Google, this was pre-Wikipedia. Now you could say on the one hand, nothing has really changed. We still go to classrooms, we still study. Except everybody seems to have a laptop in the classrooms these days. Half the students don't come to the class. The teachers are not really trying to teach the curriculum. They just share the notes online and they are expecting the students to read up online. The assignments are done online. Half the corrections are done online through multiple choice questions. We are going, we've gone so much more towards multiple choice questions because the systems are able to correct it, so the teachers don't really have to do the manual correction, which means that the entire evaluation mechanism has changed. In '95, could someone have predicted that? Yes, a lot of people did predict it. But would we have known that this particular prediction in '95 would have worked and not some other prediction? No.

48:42 So I can give you a thousand themes, some of which are reasonably clear and obvious. But 95% I don't know. So let, what is that 5% that I genuinely believe or is very likely to be?

49:01 One is the role of or the method of **evaluation** will definitely change. No question about that. In particular, I believe that subjective evaluations are going to be a whole lot easier. You just ask an LLM to evaluate it based on your rubric, it will do the job. So there will be one shift back from from objective to subjective.

49:30 But how am I using LLMs in education? That at least I can concretely answer.

49:36 One, **curriculum design**. For a course that I'm running at IIT Madras called Tools in Data Science, the curriculum is largely written by LLMs using this process. I upload my past material. I say, here is a new topic that I want to teach. DuckDB. Go online, do research on DuckDB. Find all the important and useful things that students should know. Write it in the same style as this. And I find that Claude writes in a very similar style to or is able to match my style very well. OpenAI ChatGPT is able to do the research much better. So I do a two step process. Research here, paste the research and get Claude to write it. So curriculum design is one in which the educators can change their approach, which means that the curriculum can change much, much faster. If a new tool gets released or I want to get rid of some old stuff. Now it's not a bother. I just quickly change the curriculum. So earlier TDS used to change every the course used to change every year. Now it changes every term. Actually, it changes mid-term also.

50:39 Second, I'm able to give **personalized feedback**. How? Because the student submits code. I have an LLM review the code against predefined criteria and for each student it gives a specific answer saying, in your particular case, the code was quite long but it was very well structured. You may want to introduce fewer comments and the comments should be explaining why, not what, that sort of a thing.

51:05 Third, this is not really related to how the role of educators may change or maybe it is, but I'm able to detect **plagiarism** much more easily. Not necessarily more robustly, but much more easily. And I'm encouraging plagiarism. I'm telling people, look, copy as much as you can. The point is not that you independently when you get into the workforce come up with the greatest discovery. The point is you collaborate and come up with something great. As a result, I'm giving people assignments that are tougher and tougher and tougher, things that I there's no way I would have been able to do. You collaborate and get the job done. But I am able to detect it and that helps.

51:45 I use it to **transcribe lectures**. So after each lecture, the notes are available for the students who have not joined that session, which means that the educator will probably have to talk to a camera even more than they used to. Students can catch up on the transcript. They can start querying the transcript. The transcript will act as a virtual teaching assistant. That's not a bad thing.

52:06 Which leads us therefore to **virtual instructors**. Take all of your transcripts, take all of your Q&As, take all of your course material, take all of the exam content. And create a virtual assistant out of it, which means that the actual virtual assistants A will find that the demand is dipping because virtual assistants can take that job. But I mean teaching assistants. And they will have to step up. And we may find that teaching assistants now themselves can start running courses. So we will run sub-courses within main courses. The instructor is supposed to do something really amazing and powerful. And the teaching assistants will do what is actually being done by the faculty these days.

52:48 Across subjects, I believe that educators will start teaching **prompt engineering**, which is basically how do you get the most out of LLMs in whatever subject they teach.

52:58 I suspect that more **projects** will include LLMs. These days what project doesn't? In the early days of the internet, several projects would tell you use Wikipedia for this, use Google for this. Like that today we will tell them going forward it will become an obvious thing.

53:14 These are some of the things that I'm doing, but like I said, this is the 5%. Who knows what will come up.

53:22 Audience: Yeah, sir, I have one question. Like if we consider the tools and data science course, there is so much topic included, so much concepts are included and the assignment was really tough to complete within time. That is one part. In the industry, we observed also, a few days back, if I am busy learning transformer, then agentic AI came. So, scenario is changing, the pace it is moving. What I found that it's really, really important to learn that how to learn. Now, I really want to hear from you, is there any best practices or mindset we should follow? Because often we are loaded with so much concepts and unlearn something and then relearn from the clean slate perspective is often it gets difficult. So, on that part if you have something to share with us.

54:27 Anand: There is a book called _Learn Like a Pro_ and a Coursera course on the same topic taught by Barbara Oakley. And I would very strongly recommend it. It literally teaches you learning how to learn. The book is also very short.

54:50 Let me share what I have learned from this as concisely as I can.

54:55 One, you learn better when **focused**. Set a Pomodoro timer, remove distractions, take a break after 25 minutes. This is a robust approach. Set aside time for learning and do that.

55:09 Second, don't focus too much. If you get stuck, **defocus**, let your subconscious work on it. In fact, consciously distract yourself when you are stuck. Chaos helps, the subconscious takes over and that is an effective mode of learning.

55:27 Third, remember stuff and learn stuff by **chunking**. Create building blocks. Build on top of those building blocks and connect those blocks. So concepts are not independent but hierarchical. So as you pick up bigger, broader concepts, right now, within vibe coding, there were three or four things, maybe 10 things that you remembered or noted. But see if you can get all of vibe coding into one block and use that as part of a broader coding strategy and use coding as a broader building block to building businesses maybe and so on. What this also does is increases the size of your working memory. At any point you can probably hold three or four things in your mind. If those things that you hold are bigger chunks, that works.

56:21 Practice **active recall**. What that means is after you learn something, the next day, the next, the same day, the next day, and the next week, practice remembering what you learned. Write it down, flash cards, however you want.

56:39 Create a **good environment for learning**. People around you, habits that you take up, promises that you make to others that will force you or encourage you to keep learning and also motivate you will help.

56:54 Lastly, just be able to **read faster**. Reading fast is a powerful technique in any case and well worth doing.

57:04 Audience: If somebody else has a question they can ask. Since I haven't seen a hand raised, I'll just ask one question.

57:10 Anand: Please, please. Please do.

57:12 Audience: So I think what's interesting is that like in the last three years or so, we have seen LLMs dramatically evolve and improve and now we've got reasoning model and God knows what GPT5 is going to be like and, you know, so obviously and we're moving, apparently moving to agentic. But one thing that's interesting is the way to engage the LLM hasn't changed. The way ChatGPT screen was three years ago and Gemini was. So what's basically becoming very apparent is that the way you engage the intelligence through that chat interface hasn't really changed. So unlike when computing evolved, we would go from, you know, using very monolithic apps to browser based apps, to mobile apps, to, you know, whatever, whatever there is going to be. So do you see this this aspect of engaging with this intelligence that is going to be increasingly becoming more and more, you know, sophisticated around us change as well or just the intelligence will evolve like the way it has it has happened over the last two, three years?

58:19 Anand: My guess is there will perhaps be a **consolidation of user interfaces** in the near future. Arguably, this happened with Google as well. Google's interface hasn't changed in well over two decades, at least not much. And many applications started mimicking that interface, and even applications that had very little to do with search as a concept. And there was that phase of UI consolidation where things were starting to move in that direction. And then came an explosion: dashboards, data visualizations, that was one theme, faceted filtering, which Amazon brought in, that was another, small little ways of presenting products, which again Amazon brought in. A whole bunch of UI innovation that came around or after that phase of consolidation. Not that it was linear. But in a similar space, what we're seeing right now, if what I'm hearing of is people are saying look, chat is the universal interface for now. And by chat, we include voice based interactions and so on. So even within an IDE, we are really talking to it. And applications, so if I if I have let's say my customer, let's say CRM is on Hubspot, I would talk to Hubspot. I don't need Hubspot's interface. I just ask it a question and it comes up with an answer. If I'm talking to let's say GitHub and not even for coding, for administrative purposes, let's say I want to get the logs of the last 20 deployments and figure out which of those logs errored out. I would use the chat interface.

59:53 So, Satya Nadella in one of his talks mentioned that he sees chat as becoming or the intelligence layer becoming standardized. And behind that, the transactional logic is through APIs. Applications are just going to be databases plus business logic. But the layer on top is just going to be AI, probably with a chat kind of an interface.

1:00:18 But even that is evolving so, so clearly in my mind, though subtly. For instance, citations, the way in which perplexity brought in citations and then ChatGPT and Gemini brought in citations, awful. The way in which Claude brought in artifacts, which we, which OpenAI calls and Gemini calls canvas, which splits something onto the right side, that is a very powerful innovation. The way in which deep research is structured, where the agentic thinking is brought in, so the entire way in which I mean not just research, all thinking, all reasoning, all the way in which the thinking is shown, that's a different kind of output interface. And if we go through the list of changes that were made in the mobile application, that's even more extensive. You're right that it's all falling under one overarching umbrella and I see that as a **convergence of many different kinds of existing user interfaces** being brought into one umbrella chat interface. So that will probably progress. But there will be branches from here of a variety of kinds which I have seen which will be a next phase of explosion maybe a couple of years down the line will become more robust.

1:01:34 Audience: Very interesting. Thank you so much.

1:01:37 Anand: In today's world the industry is running after every new solution no matter if it's the probable solution. Fear of missing out is more visible and which is exiting from identifying and solving the nature of the problem. Aren't we moving away from fundamentals and only embracing the glamour more?

1:01:55 Yes, we are, like we always have, meaning this is not a new phenomenon. We're continuing embracing the shiny things. And I'm guessing that this has had a, an evolutionary purpose as well, because by embracing these new things is how we have discovered and innovated and moved on. The reality is, as you said, we waste effort by running after every new solution. But with the benefit of hindsight, we don't know which is the probable solution beforehand and therefore which is the one to run after.

1:02:40 You may argue we need to be more thoughtful. The counter argument is when we have been thoughtful, we have made probably almost as many mistakes as when we have been blind. Penicillin was a mistake. Sticky notes were a mistake. There were several other mistakes that were thrown out of the petri dish because we didn't know that they could be used in other ways.

1:03:02 So, the way humanity seems to have approached this, maybe just nature, not even just humanity, is have a small percent of people who are slightly crazy, who don't really necessarily care as much about their well-being or don't even know enough to care about that their well-being, who run after these and try out new things. 90% of them die out. Today we call them startups, but they fail miserably. But in the process, somebody discovers something that becomes a huge social good and runs after it.

1:03:39 And guessing that this is not a natural thing for most people, because in every corporate that I talk to, the single complaint that the leadership has is, oh, nobody is using AI. Now wait a second. Here you're saying the industry is running after every new solution and there they are saying nobody is taking up these new things that we are delivering. Where is the disconnect?

1:04:08 The thing is, people are talking about the new things. 10% of the people are doing new things. 90% are not. 90% of the news is covering the 10%, because that is what is more interesting. And it is probably required because we want to hear about these new things and that inspires a small number of people that innovate and create something new. This is how it has always been.

1:04:35 So, I would not assume that what we hear people running after is what people are actually running after. It is very distorted. The hype is all about new shiny stuff. That's all.

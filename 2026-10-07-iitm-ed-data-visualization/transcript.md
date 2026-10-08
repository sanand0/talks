# Transcript

**Palani**: [00:00] ... you can hear. That's all. Okay, Anand, we'll get started because people are able to hear what you're saying.

**Anand**: [00:11] Okay, cool. Let's dive in then. And like before, it'll be good if you otherwise just interrupt with questions as much as you can because it's one way of staying awake.

**Palani**: [00:24] Right. So I'll inform, but I'll also stay on the stage so that if anyone has any question, I will ask what that question is and I will relay on the computer to you. You heard what I said? What he said rather? He said just to make sure that you are all awake and listening to what is being communicated.

**Anand**: [00:48] Not for me to stay awake or for me to get feedback, but I had a classmate, a fairly senior classmate who was doing his PhD while I was doing my MBA. He was at that time the Finance Secretary of the Karnataka government. And he would periodically ask questions. And of course, class participation is rewarded literally with marks. But in his case, he said, "**I ask questions more to stay awake in class because if I don't ask questions, I will fall asleep.**"

**Palani**: [01:28] (In Tamil: *Appa idhu panni aaganum*) **So we have to do this.** One second, the thing came. (Looking at technical setup) Where is the boot connect device? (In Tamil: *Illaye idhu mattum dhaana kaattudhu*) **No, it's only showing this one.** (In Tamil: *Bluetooth connection sir*) **Bluetooth connection, sir.** Rockerz Trends is this one? Now is it coming? Connected to Green. Okay, Anand, can you...

**Anand**: [02:37] I can still hear you, but if I'm speaking, am I better audible?

**Palani**: [02:40] **Fantastic, yes. It's better than if you were here.** Alright, all yours, Anand. I'm around.

**Anand**: [02:51] Cool. I'll just briefly recap, which is please ask questions. If nothing else, the class will go in the direction that you want rather than some random direction that I will be taking it.

[03:01] There are four broad themes that I'm planning to talk about today which will relate to some of the material that you've seen before. The first is that **tools are going to be shaping visualizations, like they used to.** When William Playfair was creating his visualizations, they were more hand-drawn, and that meant that there was more variety, more flexibility, and fewer people could create it. Then we had the Excel era where standardized charts became more the norm and therefore more people could do stuff, but there was lesser variety in charts that used to come out. **With AI creating more visual formats these days, we have a lot more of the kinds of visual variety that we used to see before and can probably start seeing more.**

[04:00] I'll show a few of the visualizations that I saw recently that I thought were interesting and were created by people with varied levels of visualization experience, which I think is the main point. I'll start with a visualization called JEV's Keep. Some of you may have heard of this model called JEV (J-E-V). There's a lot of buzz around it in recent times. It's a relatively inexpensive model unlike the likes of ChatGPT etc., which generate text. It can only say yes or no or choose between categories or generate a number, but it is pretty fast.

[05:01] So one of my colleagues who is fresh out of college, he took JEV and started doing security screening. That is, when a request comes to a website, can we check if it is an SQL injection attack? Can we check if it is a path traversal kind of... okay, not able to zoom in, it makes it worse... but on the right side you may be able to see the different categories of attacks. The way he implemented it—I have no idea if it was intentional or just a model choice, but I think there must have been some intention behind it—where he encoded each of these as little dots. That is, **every request that's coming in is a little dot going through a castle, and as the requests come in, if they are a security act, they get added to the tally board on top, effectively creating a dynamic bar chart race.**

[06:03] Now, he's not familiar with bar chart races. It emerged as part of the discussion that he was having with the model. The whole concept of a castle again just emerged, and the dynamic streaming of course, this I can and should accelerate—let me just play it at 5x speed—came in because of a discussion that we had saying, "Look, let's run this as a simulation so that people can see what's happening." Pretty interesting. Now, a lot of people have in recent times asked me, "**What is this kind of animated visualization that you use?**" and I think that this was recently in a trip to Manila where they were not as familiar with animated visualizations as they were with Excel visualizations. **Today that's so much more a possibility than it used to be that people are just using it left, right, and center. Why not? Why does visualization have to be static when the medium that we are using these days can support dynamic formats?**

**Anand**: [07:01] Let's take another visualization. This was created by a Japanese student in his first year of college from City University of Tokyo. The interesting part of the visualization, the broader story... but this was for... I forget which football series this is, but he effectively created a **heat map of where the goals were successfully scored from.** And a bunch of variations around this to see where individual specific spots from where each individual goal was scored, with the ability to look specifically at what time, who scored which goal, and animated right down to the point of the individual goal position and each one of these goals step by step walking through what exactly happened. So if... this goal... so this was potentially the origin. They don't have the origin data, but this was probably the origin. This is the recorded shot position and it moved in here.

**Anand**: [08:15] Palani, you were saying something? Maybe not. The idea here is that a heat map of football goals is not something that...

**Palani**: [08:33] Anand, suddenly your voice became very feeble.

**Anand**: [08:41] Oh, oh. Okay. Sure, I don't think I've changed anything on the mic but I'll get a little closer in any case. Is it okay now?

**Palani**: [08:49] Yeah, now it's okay.

**Anand**: [08:51] Okay, fine. I'll just continue this way then. Now, it's not that a heat map kind of a visualization is particularly difficult if you knew D3, but this is a student who knows no programming. And I think that's becoming the second kind of capability unleash that's happening. What that means is that **some of those who are artistically inclined or have a strong domain sense probably have a bit of an edge in creating visualizations because this student obviously knows football and says, "Look, this is how I want to see it," and the tool ceases to be a constraint because now you just tell it to do something and it can do it.** It almost becomes... the question now becomes then: **Do you have a good enough story to tell and do you have an interesting way of telling those stories?**

**Anand**: [10:14] Some of these stories emerge just from the domain itself. For instance, one that we've been sharing with the Times of India is on environmental change insights. I'm not sure if I showed this last time, but if so it'll be great if someone could just let me know and I'll go a little faster. But what we did was **looked at satellite imagery and zoomed in into specific areas comparing... so let's take Chennai.** I'm going to zoom out of Chennai a little bit and what you have here in these little grids is how much water is retreating or drying. So green means water coverage has increased, red means water coverage has decreased between 2015 and 2025. Effectively, if I take the map as it was in 2015 and compare it with the map as it is in 2025 for each of those little—I think 100-meter by 100-meter—grids, we used a vision model, specifically a geospatial vision model called Olmo Earth, to see what is the water coverage before, what is the water coverage now, and create a heat map of where in Chennai water bodies have grown and where they have shrunk. So for instance, let's look at one of these hotspots here. Zooming in... oh, you aren't even seeing the screen, sorry. Let me do this again. Apologies.

[11:42] I will start again. So that's Chennai's water coverage or water difference. So this is Chennai in 2015 and this is Chennai's satellite imagery now. **If we take Olmo Earth's evaluation of in each 100-meter by 100-meter grid how much water coverage there was before versus now, the greens are where there is more coverage.** Let me zoom in into one of these spots which should be pretty easily recognizable, but is it... can anyone name what this bright green spot is likely to be?

**Student**: [12:28] Greenery?

**Anand**: [12:35] It's water, but where is it?

**Student**: [12:44] (In background) Adyar?

**Anand**: [12:45] No, no, I'm asking if anyone could guess what that green strip was.

**Palani**: [12:48] Green strip? They said greenery, but yeah, in the discussion it turns out that it is water.

**Anand**: [12:55] Correct, but... well, let me put it this way. Does anyone know Chennai well enough to know where this is?

**Palani**: [13:03] Where this could be in Chennai? Adyar Poonga?

**Anand**: [13:06] Exactly. The Adyar River, correct. And if we just take a look at... this is the current situation and this is what it used to be. Now, the fadedness of the image is not what it's using as the metric. The amount of water itself, which you may be able to see from the edges, has grown more in this area. But of course, you could also say it's because there is more water for it to grow. But still, the Adyar River has certainly become a lot wetter. And there are other spots like... let's just randomly pick one of these where, okay, there is more water coverage, probably some northern part of Cooum or whatever which used to be a lot drier. No, this is not Cooum, probably the northern part of Buckingham Canal or some such thing that is a lot wetter. And similarly, we can look at this from a vegetation perspective as well, or greenery as you looked at, to see where greenery is growing and where greenery is shrinking. **Very simple heat map visualization, but the underlying data is changing.**

**Anand**: [14:31] Yet another kind of visual representation that I'm finding a lot more of these days is SandDance. So this is a research report that is based on McKinsey's Global Energy Perspective report. They've been publishing about 27 of these very detailed reports every year. And in those reports, what we'd done was take every single fact in it and broken it down, saying that, look, there are a total of about 2,200-odd facts. Each of these is one such. So here, one of the facts that are claims let's say that they've put in is, "Power sector gas demand in 2035 will be less than 100 BCM because renewables are going to be more competitive." Some statement of fact. And each one of these is one. The nice part is that it was easy for the audience to see...

**Palani**: [16:19] Anand, are we still looking at the water map or is it a different map that we are...

**Anand**: [16:24] Sorry, I will start again. My apologies. I must consciously switch tab to tab and see the different screens. So let me do this again. This...

**Palani**: [16:40] The McKinsey one. From there, you didn't change the screen.

**Anand**: [16:44] Correct, exactly. So the McKinsey Global Energy Perspective report has about 27 of these publications. And each publication was broken down into about 2,200 claims. So one of these is a claim that says, "Under accelerated renewables etc. are projected to plateau after 2020." They're making a forecast of this kind. And like this there are more than 2,000 of these, which it becomes easier for people to get a sense of, you know, get a map of so to speak. By saying by year we seem to have a lot more of these claims in 2024. There are many more forecasts than estimates, than facts, than causalities. The ones that we need to watch for, high probability or high importance, there are about 1,250 of those. Where they occur across the reports. And of course, if you say, "Look, just tell me in which report are there things that I should watch" and sort by that or even let's say color by that, **it becomes easy to track groups of claims across different categorizations. This is a characteristic of the SandDance kind of visual animations.**

**Anand**: [18:08] We've seen that these are not Excel-creatable charts at the very least; they're certainly D3-creatable charts which are limited to a smaller audience, but almost all of these were created by people who were not able to create visualizations but knew the domain. Let me switch to another one and share the tab before I forget. Another visualization was created for a company, Optum, to show their product portfolio. Again a very simple SandDance kind of a visualization that said, look, you have about 208 products that are documented and they belong to a whole bunch of these categories and they fit into these workflows. So **rather than think of a product being a monolithic whole, think of it as it is delivering some capabilities.** These capabilities are focused in specific areas. What you need to do is maybe rationalize it in a slightly different way. If we look at what are the key common areas that you should be focusing on, there are some products that are emerging right in the middle of these capabilities, therefore maybe you should focus on rationalizing those. Here are some external dependencies where you're dependent on a competitor, so maybe watch out, either buy that competitor out or remove that dependency, are examples of somewhat more novel visualizations that I've seen in the last month or so. Again, almost all were created by people with a strong understanding of the domain and a relatively weak understanding of visualization or technology.

**Anand**: [19:54] What am I therefore leading towards? You've seen in this course that over history at different points when technologies became available, the shape of visual representations changed. Today, as in today meaning over the course of the last few years and the next few years, we are at another one of those inflection points. **Treat what you're studying from a tools perspective with a little bit of skepticism.** The tooling is changing rapidly. And treat what you're learning from a technique and a history perspective with a little higher importance. The lessons both of history and the principles that we learn might last a little longer.

[20:44] And one of the principles that we are talking about is just **how well do models see things?** Or sorry, how well do people see things? Graphical perception. We have our own set of biases. We are able to spot differences in color, even subtle shades, when they are right next to each other. But move them a little further away, surround them by other colors, and we totally get confused. Length perception is pretty good, area perception is not perhaps as good, angular perception is pretty bad. When we stack things near each other, we're able to see smaller differences; further apart it becomes trickier. These are the kinds of mistakes we make.

[21:33] But now with agents coming in, **agents are increasingly a consumer of our visualizations as well.** What I mean by that is half the time when somebody sends me a presentation which probably has a bunch of charts, I just upload it to ChatGPT and say, "Tell me what they're saying." Now that will contain a chart. Ultimately, ChatGPT is the one that's going to be reading the chart. **If you are going to be creating visualization, you may as well make sure that Claude or ChatGPT or Perplexity or whatever is going to be consuming the chart for probably half the audience can read it as well.** Of course, you could put it in the text too, and that's a good thing. But there are likely a set of things that LLMs are better able to visualize when shown as a picture that's just almost impossible to convey as images.

[22:31] So how do LLMs see and what are their biases? That's something that's probably worth exploring as well. So let's take a look. We were playing around with a few benchmarks and I'm shifting to a bookshelf benchmark. One of my colleagues, again fresh out of college, took a bunch of photos. And here is an example of one of the photos he took. It's of a bookshelf. And asked a series of models, "Can you tell me all the books that are there in this particular bookshelf?" (A, B, C etc.) He manually classified all of those. Some of those, like the first two, are relatively easy; you can see the titles clearly and completely. Some of them are harder, like the last two, where they're both messy, not very visible, etc. And he created a benchmark.

[23:32] The prompt was fairly straightforward: "List all the books." And he compared the books against the results. And the results are interesting. There were a couple of runs that he made, and looking at the overall F1 score, what we're finding is a couple of things. One, that **the newer models, especially the Anthropic models (Opus 5.5 and Sonnet 5.5), are way ahead of the latest Gemini models, which is... not way ahead, a bit ahead.** 86% is what Opus 5.5 scores with high effort as compared to Sonnet 5.5 which was at 80% and Gemini 3.8 Flash scored 70%. In other words, they're able to get more than half the books right, but none of the models could get all of the books right. Fair enough.

[24:32] Now that gives us a couple of things. One, that there are models that can see better and there are models that can see worse. The second, in each of these cases he tried it with low effort as well as with high effort. And the models have the tunable parameters so you can literally tell them, "Look a little closer" or "Just tell me what you see." And in many cases, the high effort outperformed the...

---

**Anand**: [24:59] ...performed the low effort. Not always. For instance, for Luna, if you actually asked it to look harder, it did worse. It happens. If you tell Gemini to look harder, it doesn't really have much of an improvement. But for Sonnet, there was a decent improvement.

**Anand**: [25:18] The other factor is: how much is this going to cost? Now, on this chart, the x-axis is how much it cost. The y-axis is how accurate it was. And you can see that the **more expensive models tend to be more accurate**, or vice versa—you pay for a certain degree of accuracy.

**Anand**: [25:40] Put another way, unlike humans where you say, "I have an audience, the audience has to read it," you now have to start factoring in: **Does the person whom I'm going to send a visualization to have a model that's going to read it?** If so, do they have a better model? Do they have a worse model? How is that model—or what are the biases that that model has—that I should factor in? This starts becoming a question.

**Anand**: [26:08] Incidentally, the person who built it, Atharva—he chose to use an interesting visual representation for the uncertainty in the cost. You see that the cost has a horizontal bar. The reason is when I asked him what the cost of each of these was, he said, "Oh Anand, I didn't measure it." I said, "Okay, you have the chats, right? Go back and do a measurement." He said, "I have the chats, but I don't have the reasoning text that is hidden by ChatGPT, so I don't actually have the full reasoning tokens. I can probably do an estimate." I said, "Great, use a model, have it go through the transcript and run a similar process again, see if you can measure it, and put in an uncertainty estimate."

**Anand**: [26:57] So this is an **uncertainty estimate by a model of a model's cost**, and the range varies. For instance, for Sonnet, the range is relatively narrower; for Luna, the range of cost estimates is much wider because we have far less understanding of how much it thinks. And we'll come to this uncertainty bit and how we handle it in a short while.

**Anand**: [27:35] But where I want to go with this is that **models are reading charts. Models have different abilities to read charts. And there may also be a certain amount of bias in doing this.**

**Anand**: [27:58] Let's look at what we know about the models' biases. There is a benchmark called ChartQA Pro. It's on GitHub. And what the team that put this together did was they took a series of questions—let me open one of these... hold on, I'll switch to a new tab.

**Anand**: [28:36] So for instance, the first chart of the eight that you see here is an image with a question: "Calculate the total percentage of deals made by buyers from USA, Japan, and Singapore combined," with an answer: 70. Are models able to figure this out? This is what ChartQA was evaluating.

**Anand**: [29:12] And the evaluation results are here... I'm not sure how well you can... hold on... yeah, this is probably about as big as I can make it, but I'll just summarize by saying there are some models that do a good job, some models that do a poor job. But what is perhaps more interesting is: **is there a bias? Meaning, do some models really get some questions right and really get some questions wrong?**

**Anand**: [29:38] Nobody seems to have published a paper based on that, so I told ChatGPT about an hour ago, "Look, what I want you to do is download that dataset. I want you to download ChartQA Pro and answer the question: what are the different kinds of charts or questions that models typically get wrong? What does it tell us about their perception? Do different models have different kinds of weaknesses and strengths? Why don't you do the research and give me a story about it?"

**Anand**: [30:13] And here is the story that it's given me, which I'm looking at for the first time; I haven't seen this so far. And it's saying: **a model can know what calculation to do, but still misread the picture that it is calculating from.**

**Anand**: [30:30] So here is one question: For this picture, "When does the wind capacity first exceed 100 gigawatts?" Okay, I'm not sure if you can answer that question, but let me try. I have to look at this green thickness and see when it exceeds 100 gigawatts. I think my answer is "never." But it says... okay, the ground truth is 2037-38.

**Anand**: [31:04] Oh, okay fine. I should have looked at it cumulatively then. All of that was cumulative and I misread that chart. And 2037-38 is, yes, when it hits the 100 mark. And Gwen 2.5 said 2024 or 2025. Gwen 2.5, a larger model, said 2035. And yet another model said 2033-34. At least the larger models seem to be roughly in the ballpark. Fair enough.

**Palani**: [31:41] Just a question on the previous thing. So the graph is on the left side, and the models that you are talking about are answering the same question: when does it cross 100, correct?

**Anand**: [31:53] Exactly.

**Palani**: [31:54] And okay, alright.

**Anand**: [31:55] And I assumed that the thickness or the height of the green is the wind, but it turns out that it's asking for the height from the bottom, not just the green part. Which is my mistake, but the models seem to have done better than me in any case, for sure.

**Anand**: [32:21] And I'm just trying to see... okay, what are the kinds of mistakes that they are making? **The weakest perception signal is approximation.** I see. Okay. So **if the question contains words like "approximate," "estimate," or "roughly," then the models need to infer a number rather than just copy the printed label.** And that kind of inference they seem to be doing much worse at.

**Anand**: [33:07] So if what this is saying is: look, at least if you look at ChartQA, **one of the principles is: don't ask the reader—the model in this case—to infer something from the chart. Print the number there directly, otherwise they do a bad job of it.** Frankly, this is something that I tell all of my team members anyway: **never have the user infer a number, just show it there.** That's reflected for models as well.

**Anand**: [33:40] Visual density. So what it's saying is, the denser the picture... okay, I'm not even able to figure out what it's saying. Okay. This is a good comparison of how models compare with humans. And you probably remember the Cleveland and McGill experiments where people were looking at how well humans do on comparing positions which are in a common scale, non-aligned, etc. It's interesting that the models seem to have a similar perceptual gap.

**Anand**: [34:36] I'm going to go through this and probably come back with a more detailed understanding. But the two things that I wanted to share are: **A) models have their own biases.** They may be similar, they may be different. But **B) they also are part of the audience now**, and we may as well get familiar with the kinds of mistakes they make.

**Anand**: [35:03] So:
1. **AI is able to create visualizations.** That's going to change the shape of visualizations; therefore, focus more on technique than tools.
2. **AI is going to be the audience for your visualizations.** So understand them not just as a tool, but as an audience that will consume your visualizations as well. That's going to make a difference.

**Anand**: [35:24] These were the first two of the four things that I'm planning to cover. But let me pause here. Any comments? Questions?

**Palani**: [35:35] Any questions? Comments? Anything? No questions, Anand, we can proceed.

**Anand**: [35:46] Okay, then let me ask a question, an open question: **What does this mean? As a result of this, what are you going to do about it?**

**Palani**: [35:56] Did you get the question?

**Student**: [36:00] No, no.

**Palani**: [36:01] Can you repeat the question, Anand?

**Anand**: [36:02] What does this mean for you? What we've discussed so far, what are you going to do about it? What is the need for you? What does this mean? What does this imply?

**Palani**: [36:24] What does it mean for you? What is the meaning? Not "meaning" as in... okay, got it. What does it mean for you? Okay. **What are you going to do about this now that I've randomly said a couple of things? What will you do with this information?**

**Palani**: [36:41] He's given a few things, including going and looking at some benchmark information and generating these observations, right? So how do you reflect upon that—"reflect" might not be the correct word—how do you use it? Or how might this reflect upon your work? How can you use whatever you've seen?

**Anand**: [37:12] Exactly. What's the point of learning if you're not going to do something about it?

**Palani**: [37:19] I wish you'd answer that! Throughout the course we've been asking this question again and again.

**Student**: [37:25] (At microphone) So the first thing which was brought up was that **it is becoming easy for each of us to kind of use the LLM and visualize in the way we want.** That was the first thing which you kind of tried to convey to us. But the second thing is that **whatever LLM will rather generate for each of us, are we going to bank upon the same thing or are we going to analyze further?** And that analysis can only be done if, and only if, we know how they are rather trying to see the material or generate the charts in some sense, if I'm on the right line. So we need to understand how they are reading the stuff.

**Anand**: [38:20] Got you. Interestingly, I would frame that differently, the second part. We'll come back to the first. **The second is saying: when you create a visualization and you send it to somebody, they are not going to open it. They're going to upload it into their ChatGPT and their ChatGPT is going to see the visualization.**

**Student**: [38:50] Okay, so one model is rather creating it and the other model is being the... evaluating the output of the first model. Okay.

**Anand**: [38:58] Exactly. So **the model has to understand the visualization.** And you've aptly summarized what I've said. My question is—and you're welcome to answer it, or anyone else is welcome to join you—so what are you going to do about it?

**Student**: [39:18] It's totally a subjective question because now **everybody wants too much of stuff in so little time.** We would rather try to compete with our own people who are there around us and try to match what is going on in the world. So **the first is survival: whether we are able to survive or not.** And after we are very certain that we'll survive the competition, then comes: what are we really going to kind of add from our perspective? So as of now, what I'm saying is that we are just trying to survive. That is the first takeaway for me. Others are doing it, but to an extent until the time I'm stable. Once I'm stable, then I'll start asking the next questions, like **is what it's going to give me really good? Is it really bad? Is it going to have any impact and what that impact is going to be?**

**Anand**: [40:14] Got you. Anyone else? Any thoughts based on what we've covered? How are you going to apply it?

**Palani**: [40:34] Any other thoughts? Satyam?

**Palani**: [40:42] No additional answers, Anand.

**Anand**: [40:46] I'll wait. Sometimes it's worth pushing.

**Palani**: [40:51] (Laughing) Okay, so he's unlike me. He says, "I will wait." Some application that you think could be used. I mean there's the beautiful stuff that he showed in the first, the JEV screening—I don't know what is the underlying model that goes behind it, but it is like **real-time monitoring.** So real-time, the dynamic chart also keeps changing. This is one of the major things, for instance, if you're doing IoT, any manufacturing stuff. It's not about static data; it is about components that are coming in, machines are running, and you'll have to monitor this on an online stuff real-time. Okay? Or marketing analytics, for instance, is real-time. So many of these things—stock market—many of these things you actually want real-time graphs and not static graphs. So I thought that was... I don't know the model, I just saw the JEV screening for the first time when he showed it today. So to me, I think that's one thing. But then that was just the visualization part. But if we use the **interpretation engine**, you know, that is one application that the last discussion might be relevant to me in that context.

**Anand**: [42:08] Completely. Got your takeaway. Let's also hear from some students.

**Palani**: [42:14] Student? She's coming to the microphone.

**Student**: [42:20] The question basically was that LLMs are generating the visualization, LLMs are evaluating the visualization also. Right. So what is it that we can do?

**Palani**: [42:38] Correct, that is my question to you.

**Student**: [42:41] **Optimize the cost versus accuracy.** If it is doing the evaluation also for the cost that we are spending, how can we improve? Did you get that answer, Anand? He says **optimize the cost versus accuracy.**

**Anand**: [43:00] Fair point. Okay, tell us more, please.

**Palani**: [43:03] In terms of making the decision. Go on.

**Anand**: [43:08] Maybe you could just come out to the mic and I'll hear better.

**Palani**: [43:13] Okay, so he's asking... that's it? He says that's it, that's all, his point of cost versus accuracy.

**Anand**: [43:20] Got you, which is a fair point and that is the practical implication. Any others? Harini?

**Student (Harini)**: [43:35] I think what we are doing is we are the ones making the decision at the end.

**Palani**: [43:43] She's coming to the mic. I'll introduce my own bias if I say what you're saying.

**Student (Harini)**: [43:49] So yeah, I mean what I understood from all this is that **it can save our time, it can give all the visualization and everything, but at the end, what we are going to do is we are the ones who will be deciding on whether to completely rely on it or how we go about the final decision.**

**Anand**: [44:06] True. And because of that, what do you think you would want to do differently?

**Student (Harini)**: [44:13] I mean, maybe **assessing the answers which it gave or, yeah, basically optimizing it.**

**Anand**: [44:31] Got you. Thank you. I'm learning something from this class, actually, a whole bunch of things. One of my major takeaways is—and now that I reflect on my classroom, my times as a student sitting in a lecture as well—the mode of learning for many of us... actually, I should frame this differently.

**Anand**: [45:06] **For many years, I have been learning stuff because I wanted to do something.** I have a problem, I will go learn how to solve the problem. That makes sense. In your case, you have a problem: you have an exam to crack. So you're kind of using one technique, which is sitting in the classroom and figuring out how to solve it. Obviously, you don't really know what of what I'm going to say is going to come in what exam or whatever.

**Anand**: [45:34] I find that half the time, most of the time, **when I don't know why I'm learning something, I learn a lot less.** So I usually just walk out of any place where I don't know why I'm in that room. You are in a less fortunate situation; you probably, at least for attendance quota, have to sit in there. But I have one degree of freedom, which is: **the second half of this class, I can choose to answer what *you* want to know rather than me telling you what I think you should know.** Because you want to understand why *I* think you should know that, and it's hard for me to communicate. But if you say, "Look, I want to know this," I'll answer. I'll answer. That at least will be a more... at least you will get the answer to something that *you* want to know, rather than knowing something that you don't even know you want to know.

**Anand**: [46:51] So let's flip this around. At least 15 minutes, pure Q&A. **What would you like to know about?** And we'll talk about that. I'll share from what I've learned. And in case the audio wasn't clear or I was just rambling, summary: at least next 15 minutes, any questions related to visualization and AI that you have.

**Palani**: [47:20] He's flipping the setup now. He delivered some stuff, he asked you questions, now I don't know, from our end we may have an opinion about it. So what he says is he's turning the tables now and he says, you first raise the questions and accordingly I will set up the class, that's what he says. This is like absolutely open, right? It can be any question on visualization. It need not be what he covered today; it could be something that we've seen in the last six, seven weeks or it could be anything, anything in that sense related to visualization or AI or in the intersection of AI and visualization.

**Palani**: [48:08] And think about how it will help you. Please be selfish in your questions. No point asking random... don't feel pressured to ask a question. And it could be "Why should I care?" is a valid question.

**Student**: [48:27] **Is it always necessary to know the requirements or like what are we wanting in entirety before we start visualizing?**

**Palani**: [48:37] Can you come over? Yeah, I'll just ask him to come over.

**Student**: [48:44] **Is it compulsory that we need to entirely know the problem definition before we really start visualizing something?**

**Anand**: [48:51] Great question. Let me rephrase that: **Do I need to know the problem before I start visualizing something?**

**Anand**: [49:01] Depends very often on who needs the visualization. **In practice, every dashboard that I've seen is created by someone who has no idea what they're trying to visualize. They don't know the problem. It is also requested by someone who doesn't know the problem.**

**Anand**: [49:20] Here is the typical sequence: There is a business owner, typically a senior leader, who says, "I want to understand," and he will give a list of, "Why is my operations falling? Which of my machines are likely to fail in the next three months?" He'll give 10 questions like this to his project manager. The project manager will understand 20% of those questions, write it down, and then give it to a vendor. He will say, "I will create an RFP." And the RFP will say... [audio cuts out]

---

**Anand**: [49:59] ...will say, "I want to be able to answer 10 such questions and 30 more of any kind." This will be picked up by somebody on the sales team of some company, let’s say Wipro, who knows nothing about operations, who knows nothing about data visualization, but has a quota. So they will write a proposal saying, "Here is how we will deliver the dashboard," which will be reviewed by the project manager, executed by a developer who doesn't understand operations, who does not necessarily understand data visualization but knows Power BI or Tableau or Excel or whatever.

**Anand**: [50:45] And after a whole series of rounds of QA, they will produce 20 charts. The business user will say, "I don't understand head or tail of it. What rubbish." Project manager will say, "No, they didn't understand it." The developer will say, "Okay, I will create 30 more charts." They will say, "Okay, look, if I take this part of this chart and I put in this part from here, then I might be able to answer at least one out of my 10 questions." But—and then the business owner's boss will say, "**You spent half a million dollars already, right? Are you getting value for it?**" What is the business owner going to say? "Yeah, yeah, yeah, I've got the answer to at least one of my questions." Okay. Project has been a success.

**Anand**: [51:31] Now, in this chain, **most of the people did not know the problem definition before they started visualizing something.** They were given a statement, and they tried to adhere to it. In contrast, some people are creating visualizations that *they* want to see or are testing against users. For example, the newsroom of *The New York Times*. The editor has an excellent idea of what the general public will understand. They will tell the graphics team: "Create it like this. Make this change. Iterate, iterate, iterate." They are sitting literally on their heads because the timeline is a few hours before they publish something. In that case, **it's still the graphics designer does not need to know what the problem is, but the editor is sitting right next to them. The editor knows.**

**Anand**: [52:31] And or the journalist, whoever. So that is a slightly different kind of situation. The same thing happens with, let's say, *Scientific American* or Springer Nature, some of the popular scientific publications or *The Economist*, where again the person creating the visualization is sitting very close to the person who understands what the audience needs. So it still works.

**Anand**: [52:56] The third is the **citizen data scientist** or the analyst or whoever who says, "Look, I have a problem. I want to buy a laptop. I need the maximum features and the lowest cost. I will plot it. I will see which is on the top left or top right and buy it." **Off there, you know exactly what you want.** Or last time when I showed you my Internet Movie Database chart, right? Ratings versus votes. I know exactly what I want.

**Anand**: [53:25] Put another way: **most of the time, if you're creating stuff for yourself, it's important that you should know what you want. But even if you don't, you can iterate on it.** Otherwise, have somebody close to you who knows the problem definition well. In reality, **90% of visualizations today are created by people who don't know the problem, and you can still make a living out of it.** Did that answer the question?

**Student**: [53:50] (At microphone) So basically, I will assume that as far as data visualization is concerned...

**Palani**: [53:56] Closer to the mic. Yeah, he's coming.

**Student**: [54:03] So for any data visualization to take place, the first assumption is that there is some data and there is going to be a question that is going to be asked to him or he can himself curate that question.

**Anand**: [54:13] That there should be data? Usually true. That there should be a question? Usually not true. **Most dashboards are basically saying, "I don't know what question can be asked; you should be able to answer *any* question."** I’m not saying there *shouldn’t* be a question. I’m just saying in practice, most data visualizations are created not to answer a specific question but to satisfy somebody. But I'm still—I suspect I'm still not answering your question. So go on, push. What are you really asking?

**Student**: [54:50] Yeah, so basically the thing is that **the problem is also in trying to understand what kind of data are you going to visualize because there is so varied kinds of data as of today.** Like you showed that the text can also be kind of visualized, the satellite imagery can be visualized, and you know, the normal data, the numbers as such can be visualized. So like, how do you really hone in on a very specific kind of data to, you know, visualize?

**Anand**: [55:21] Got you, which is a slightly different question. I'll reframe it this way: I don't exactly know what I want, but I am the audience. I have some data. There are many ways of visualizing it. How would I go about it? That's part of what you're learning in this course. Supposing you see 50 different kinds of visualizations, and you take a closer look at them. You get a sense of, "Okay, tomorrow I can use this."

**Anand**: [55:53] **It is very similar to cooking.** You've tasted 50 dishes and you say, "Oh, I kind of like this, I kind of like that." At least you'll be able to pick dishes next time. Or if you've prepared a dish, you know that adding this ingredient makes it taste slightly this way. The next time you'll be able to cook much easier. So, how does one go about knowing how we visualize data and what problem can we solve? Through trying out a variety of different techniques. You don't have to be the one who does all of it. Meaning, **to be a good cook, you don't have to cook every dish. You certainly ought to taste a lot of dishes and cook a few.**

**Anand**: [56:45] So **see as many visualizations as you can of different types.** And by "see," I don't mean you necessarily need to spend more time looking for visualizations. The current time that you spend looking for visualizations, look a little careful and ask the question: "**How can I use this?**" Which is exactly the question I was asking earlier. I showed a bunch of stuff. If you ask, "How can I use this?" the time that you spend looking at the visualizations will help you more. That to me is probably the easiest. I'll summarize my answer as: when you spend time with creating or seeing visualizations, ask yourself, "**How is this helping me or how will it help me in the future?**" so that when you create your own, you will find it easier.

[57:53 - 62:04] [Silence / Technical issues while class re-establishes connection]

**Palani**: [62:05] Anand, can you hear us?

**Anand**: [62:06] Yes, I can. Am I audible?

**Palani**: [62:08] Yes, yes. So, I’m sorry the wireless dropped. You are on data right now, but let me just make sure. Yeah, go ahead.

**Anand**: [62:15] No issues. Where did the students lose me?

**Palani**: [62:18] Where did you guys lose him? What was I last saying that they heard?

[62:27] [Cross-talk about technical setup and login names]

**Palani**: [62:27] Someone, Kumar, is trying to login? Santosh? Is that you? I'm sorry, okay. What was he trying to answer and where did we got lost? What was the last thing that you heard? Someone else is trying to enter the same meeting, so I was slightly confused. We didn't share the link with anyone, but yeah.

**Anand**: [62:43] More the merrier! Let them join. What do we lose?

**Palani**: [62:46] We don't know who this person is, yeah.

**Anand**: [62:50] Whoever it is, let them join. (Laughing)

**Palani**: [62:52] What was he answering? He was answering this question on, you know, "Should I know what type of data to connect and what is to be plotted?" and all that. Is it something like a cookie choice and all that? Today you could... you will be able to generate graphs. That is where we sort of got disconnected on.

**Anand**: [63:11] Okay, okay. Then I have to re—which is probably about—the internet hung for a couple of minutes. Got it. Fine. I'll just summarize then by saying that when you are looking at any visualization, think about how you can apply whatever you are seeing. That way, when in the future you want to create a visualization, you will know what works, what doesn't work, what techniques might be relevant, and so on. You don't have to spend more time studying visualizations, but you have to spend the time that you spend on visualizations more towards learning how to use it rather than just looking at it.

**Palani**: [64:01] Other questions? Yes, come on.

**Student**: [64:12] (At microphone) So my question is about: **LLMs can generate visualizations or some plots, and then it can interpret also. But it may or may not be correct. The interpretations may or may not be correct. So is there any validation technique there?** Because it can give the plot, it can give the trends, but how can I believe its accuracy of values?

**Anand**: [64:39] Thank you. Now I will go to the third part of what I was going to cover because this is it. But question to you: I will share something, how will you use it?

**Student**: [64:51] Um, I can give the data to the LLM and try to plot. And then from the plot, I'll just give the prompt and interpret the plot. This is the way I can do.

**Anand**: [65:06] Okay, and how will that help you? I mean, that's what you're saying—this is what I will do. Okay. What is the benefit of knowing the answer to your question, which is...

**Student**: [65:17] Yeah, I can know both the data and what kind of decision I can make from the interpretation. So this is one way I can look at it.

**Anand**: [65:29] Still weak, but that's not a judgment. What I’m saying is that **if you had a clearer idea of your question, the answer will land more strongly.** But I'm still going to go ahead and give you an answer to a related question, perhaps. Let's see where that goes. But I would love for you and anyone else to answer a specific question, which is: so how are you going to use what I'm just sharing?

**Anand**: [65:58] Let's start maybe with a few... well, let's start here. My screen should be visible. Okay. So one of the things that I did a short while ago was have an LLM take an engineering drawing and asked it, "Now, can you create a CAD diagram out of this?" It tried. This was given to Codex. The only information that it was given was this drawing. FreeCAD is the software that it had access to and it had the ability to run a render command.

**Anand**: [66:52] First, it did all kinds of things. It said, "I will look at this image closer, I will do some cropping of the image, I will try out other tools," etc. Then it gave up. And then next attempt, it said, "Okay, I'm going to generate this image." Now this actually looks pretty much like the drawing. The interesting thing is that **it passed all of its own tests.** It said, "I will write a series of tests to make sure that it is same as the drawing. I will check if what I've drawn passes those tests, and if it does, then agreed. If not, I will keep iterating until it does." And it built a part that, against the drawing, if I were to look at it, I would probably say, "Huh, this kind of looks like that. I'm not sure I know much better."

**Anand**: [67:44] **But it looked at it closer and said, "No, I'm not happy with this."** It said the support is a 48 mm feature and it should be 35 mm, so I'm going to redraw it. So this protrusion that you see on the left is wider than the protrusion that you see on the left—it inferred that from the diagram. Went through that and said, "Now this is the final thing. I can't find any mistakes in my operations. It looks like the right kind of bracket."

**Anand**: [68:21] **This is what it was supposed to produce on the left.** The image on the left was not given to Codex. What it actually produced was the one on the right. And you can see the difference. Firstly, there is an entire bottom portion that is missing. It should be curved rather than rectangular at the bottom left and the bottom right. At least those are the two major errors. Very similar, but they are not the same object.

**Anand**: [68:59] And the interesting thing is that if we look at the metrics—I'm going to skip all of this—if you look at how it decided to construct it, the construction methods are similar. The original reference, the object that was to have been created, started with an **I-boss**. It then was supposed to add a **main body profile**, then the **lower fork profile**, and then **cut holes**. Codex also cut holes at the end, but it started with a **base**, roughly the equivalent of the main body profile. And in the third step, it cut the hole instead of right up front. It added the **circular eye** at the second iteration. **But what it missed was this lower fork profile, which it could not see clearly enough.**

**Anand**: [69:52] But what is more interesting is that **the tests for this that it created were insufficient as well.** And the final tests—I'm trying to see if I have the list of—oh yeah, it's further up. No, where did the tests go? Okay, maybe this version doesn't have the tests, but the test cases were generated by a CAD benchmark called **FreeCAD**, where it provides not just the drawing but also **what is the volume of these? What are some of the finer details of the shape?** About 40-50 parameters that you can very granularly test along with the specification. And only if it matches all of those will we be able to say that yes, this matches.

**Anand**: [70:50] What does that imply? What I take away from these things is number one: **if I give a picture to a model and say produce something, these days it is able to produce something. Not only produce something, it is also able to correct mistakes in what it produces.** Second thing that I'm learning is: **I am not able to tell the difference.** You already saw me reading a chart worse than even a basic model. I’ve been reading charts for decades. This kind of a mistake is just too easy for me to make, so I'm not very good at spotting mistakes. Third: **that there are benchmarks out of there and there are ways of specifying correctness out there like the CAD bench that I can use as a format to say, "I will consider this correct only if it meets all of these criteria," and I have to sit and create those criteria.**

**Anand**: [72:03] Those are three takeaways for me in terms of how does one go about verifying... having an LLM generate a visualization—in this case it wasn't quite a visualization, but close enough—and I'll show you some visualization examples and how do you verify those. But what are your takeaways?

**Palani**: [72:27] The question is in your court now.

**Anand**: [72:33] So Anand, actually, we are sort of done with the class time. It's 3:15 here. We'll leave that as an open question.

**Palani**: [72:43] It was in any case the last thing I was going to cover, so yeah.

**Anand**: [72:47] All right. So we'll leave that as an open question and then probably we can revisit when you're talking to them next. And for the next session, I would like—can I assign homework?

**Palani**: [73:01] Yeah, yeah, absolutely! Why not?

**Anand**: [73:04] I'll drop you an email with some homework.

**Palani**: [73:07] Sure, sure, absolutely, yeah. All right, fine. Cool. Thanks, everyone.

**Anand**: [73:11] Thank you.

**Palani**: [73:18] Okay, just one thing before you guys leave. See, **he is one person—today if you're going to like pick up, you know, one of the top three to five people on data visualization who has been there, done hands-on stuff, run a company, sold a company, being a Chief of Innovation at some other place and all that, it is that guy. Okay?** And many things that whatever he is showing, including the Mahabharata stuff, is most likely anchored by him. Of course he has a team and all that; he is extremely, extremely hands-on. And whatever he showed, probably he generated after a discussion with me just about an hour ago or hour and a half ago. Okay?

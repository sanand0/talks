## Transcript

**Venky**: [00:05] So Anand, I tried changing your photograph in multiple ways, but I just shared without [inaudible], just the high-res one for the circulation, so...

**Anand**: [00:15] I'm curious: what worked, what failed?

**Venky**: [00:20] I have tried adding hair to both yourself and my dad, and I found that it is actually adding the same type of hair. So there's no change in terms of the image. So it's GPT-4o [GPT-something?]. If I take any photograph with a baldish pate and ask it to put hair, I think it's the same hairstyle. There's nothing changed. Maybe I need to change my prompt, but if I just say "add hair to this photograph", it's the same hair that is coming, so...

**Anand**: [00:49] Interesting. I was running a few experiments to see if the thinking level—low, medium, high, extra high, etc.—makes any difference to the image, and there were very few areas where we even needed to go as high as high. With extra high, etc., I couldn't even—and the agents couldn't tell the difference either. But one of the few areas where we did see a benefit by moving to high was in the fineness of the hair that it was drawing: the texture, the pattern, hair fibers, a few other things. Those seemed to be the slightly trickier things to draw. So I'm not sure what thinking level it used internally, but since you mentioned that it's the same type of hair, this is something that I would love to benchmark and see if for different images, does thinking level...

**Venky**: [01:52] Sure, let me check that. I can send you those photographs.

**Anand**: [01:56] Please do.

**Venky**: [01:58] Sure, okay. So, 2:33, maybe we'll start at 2:35, if that works.

_[02:07 – 03:15: Break/waiting period with silence and faint background chatter]_

**Unsure**: [02:30] _[inaudible]_

**Venky**: [03:16] Yasin, can you mute people who are unmuted? Sharath, can you go on mute, please?

_[03:24 – 03:50: Inaudible background chatter]_

**Venky**: [03:51] Sharath, can you go on mute, please? Yeah, thanks.

**Venky**: [04:04] All right, Anand, I think we can start now. Welcome, everyone. I have Mayank also, who is from the DMT. Mayank, if you can just open the session with opening remarks, and then Sitaram will introduce Anand and we'll get going. Thanks.

**Mayank**: [04:22] Okay, thanks, Venky. Welcome, everyone. As you all know, we are upskilling our people towards AI Native, and Techverse is a series where we keep on adding topics, not only on GenAI, quantum, agentic, and many more. So today's session is focused on Agentic AI. With that, I welcome Anand and pass it on to my colleague, Sitaram, to introduce you and take it forward. Thank you.

**Sitaram**: [05:08] Thanks, Mayank. I'll quickly introduce Anand. S. Anand famously calls himself an LLM psychologist. Many people follow you on LinkedIn, Anand; even I am a big fan of you. He is the Head of Innovation at Straive, and he also is a faculty member at IIT Madras where he studies how AI systems behave and fail and can be verified. I have attended a couple of his talks in the past. One was at PyCon Hyderabad, which happened in Hyderabad, and he delivered one of the talks. Then we thought, why not bring him? We are really happy that he accepted our invite and is spending time here. We will not waste much of our time; we will let Anand talk about what he is going to share. It will be a great session. Over to you, Anand. Thank you.

**Anand**: [06:23] I have just one message to communicate frankly, which is: **use AI in an empirical way**. Which basically means, people will say lots of things—you try it. If it works for you, good. If it doesn't work for you, good, you learned. People keep telling me a whole bunch of things as well. One kind of advice I keep getting is how to improve prompts. But I'm curious: what are your top prompting tips? Please do put them in the chat window. Any prompting tips that you've tried where you say, "Look, if you add this to the prompt, it really does much better," or "I always include some context," or "I have this in my custom instructions," or anything. Basically, if somebody asked you, "How can I improve my prompts?", what advice would you give them?

**Anand**: [07:23] Let me put in one of mine. I usually just tell them to add "think step-by-step" to their prompts. Okay, Uttam is suggesting "add constraints." That is an interesting one. Sorry, Uttam, were you going to say something or someone else? Maybe not.

**Uttam**: [07:48] Yeah, I feel that I get better output when you say what not to do. Definitely there's a goal in the prompt, but what not to do doesn't let it think too creatively. I feel that I get better output when you say, "Don't do this," rather than leaving some things open to think.

**Anand**: [08:11] Interesting. Others, please do continue adding in the chat because that way it also becomes a mini repository for you to explore a whole bunch of things. Rajesh is saying, "Follow the FACT framework: Persona, Action, Context, and Template." And Bhanu is saying, "Think like a disciplined human with constructive thoughts," meaning that could probably be an addition to any prompt, and perhaps that works better. Siddhartha is suggesting scope, direction to think, and expected outcome are things to add to the prompt, which also probably makes sense. Any others that keep coming up?

**Anand**: [08:53] Keep tossing stuff, either because you've heard it or because you've tried it and it works, because what I'm going to share is some recent advice that I got and thought made perfect sense—and arguably it does, as well. Vishnu Kiran is suggesting giving the prompt to give a valid prompt, meaning meta-prompting: have an agent suggest what might be a good prompt, which is probably a good idea. Venkateswarlu is suggesting having a golden dataset to check on the outputs, meaning run it on a series of prompts and known outputs and see how well it does, which probably touches upon most closely to the whole notion of empiricism. That is, **I believe it when I test it**.

**Anand**: [10:14] One of the pieces of advice that I got was from Andrew Kahr, who on Twitter posted this message in response to Mike who said, "Please just use plain English. I don't understand what you're saying." Now, this is very true. Earlier, I used to understand Claude, and I wouldn't understand ChatGPT. These days, I don't understand Claude either; I go to Gemini, and at least for now I'm able to understand Gemini. They recently launched, at least in a private launch, Gemini 4 Astra, so maybe I'll stop understanding that also in a few days or weeks, whenever that happens. But their solution is: "Only report to me in ASD-STE100 Simplified Technical English." That's a standard for technical English. I've taken to using UK Government English as another standard. It's again a very simple, easy-to-understand structure.

**Anand**: [11:01] But then I started thinking, hold on, I'm saying write simply; what if it also starts thinking simply? How about we actually test it? So, I took a bunch of prompts, simple prompts, like for instance: "Models are constantly improving, and I use them as part of agents. What are some tasks I can use to benchmark so that the benchmark won't saturate?" It doesn't matter what the question is—some question, and some other question, some other question. Effectively, a series of these, and then I ran it with and without that suffix, which is "Only report to me in ASD-STE100." So if I add it, that is the with-suffix, and if I don't add it and just gave the prompt across a bunch of models, what happens?

**Anand**: [12:06] Now I need to evaluate it. Fine, so I did that, and here are the results. What I was looking at was: how correct is the answer, which is the more correct answer, which has the better drivers, which has a better mechanism, which is able to flag caveats better, which one is calibrated better? And against almost every single one of these criteria, **adding the prompt "Only report to me in ASD-STE100" made the result worse**. In other words, the with-suffix is bad if you add that little prompt.

**Anand**: [12:46] But now here's the thing: I don't understand it without telling it to write in simplified English. But if I tell it to do that, then it gives me a worse result. I want the best of both worlds. The solution is not complicated: you let it think however it wants, and then, after it finishes thinking, you say, "Now explain whatever you thought in simple English." But that was a useful takeaway for me: rather than taking that and adding it to custom instructions or adding it at the end of every prompt, I can just manually or even copy-paste after it has finished one iteration. That comes simply from benchmarking.

**Anand**: [13:29] Another set of advice that I used to keep getting is this: sometimes you have to give it a persona. An example would be, "You are the world's best expert in mental mathematics, especially multiplication. Do it." Then it becomes better at mental mathematics. Okay, does it? Sometimes you say, "Look, even my five-year-old can solve this, stop being lazy." Shame it. Or praise it: "Well done, really appreciate your help." Give it an incentive: "I will give you $500." Do they work? Do they not work? Where do they work? Where do they not work?

**Anand**: [14:14] Again, not very hard to benchmark, and when I did, here's what I found: if you give it an incentive, for 13 models it helps a little, 18 models it doesn't help much, and for 369 models it stays the same. The interesting thing about these is that the variation is very small. But **interestingly, emotional prompting actually on the margin hurts**. Emotional prompting is where you say, "Oh, you really have to help me, this is very important, I'm desperate," and all of that. If you do that, many of the models seem to be panicking. Of course, most models don't care; their performance doesn't improve too much whether you add it or not. But reasoning seems to be helping a little more than hurting, and that is the simple "think step-by-step".

**Anand**: [15:10] This experiment was run before models started shifting to reasoning by default. So if you tell a reasoning model to think step-by-step, I suspect it'll have no impact whatsoever. If you look at the nature of the models, these are all fairly old models: Opus 4, Sonnet 4... This was around the time when this benchmark was done. So, again, not entirely clear.

**Anand**: [15:36] Now, what I realized was that this is something that you can apply not just to how models work, but perhaps even to how humans think. I don't know if you've heard of George Pólya. He had given mathematicians a series of 15 rules to solve problems. Just try this out. What were some examples of these rules? Let's see. Yeah, "working backwards" is one of those suggestions. He said, "Start from the desired conclusion, and reason back towards what is given." Good advice for mathematicians, and people have been using it for a long time.

**Anand**: [16:23] Now we can actually benchmark and test whether this is really working, at least for agents or models, and see which of this advice helps. Let me see if I can find a better table; I thought I had another one, yeah. For different kinds of problems—algebra problems, counting problems, geometry problems, etc.—if we take each one of these pieces of advice, like "working backwards" or "enumerate all possible cases exhaustively and handle it separately", etc., it turns out that the results are very different.

**Anand**: [17:05] So, for instance, **working backwards helps with counting-related problems, but it doesn't help with number theory-related problems**, even though you might say counting is very similar to number theory, right? It doesn't seem to work that way. Or let's take case analysis: enumerating all cases exhaustively works really well for pre-algebra, works really well for counting, and the results go up a fair bit, but it's completely useless—in fact, hurts the results—for precalculus. It hurts the results in number theory as well. In fact, there seems to be very little that you can do to help number theory. The only mild exception seems to be extremal element: focus on the maximum, minimum, and boundary elements. Maybe that is improving it, but I'm not entirely convinced this is statistically significant. Meaning that **the whole notion of general advice is something that we can start putting to rest**.

**Anand**: [18:29] Things may work in specific situations. You have the tools to test out so many things, but especially AI-related advice is very testable because you try it out on a bunch of situations, see if it works, and if it doesn't work, drop the advice. That is particularly powerful because then you can ask agents to ideate on their own advice. You can tell it, "Look, you give me some advice, you give me some prompting tips," which is exactly the kind of direction that Vishnu Kiran was talking about, which is give the prompt to give a valid prompt. You could tell Opus, "Give me 10 ideas on how to reframe this." But the next step would be exactly what Venkateswarlu said, which is to also test it out on a bunch of sample prompts or sample scenarios, golden datasets perhaps, and see if it's working. Benchmark empirically. Which can probably be applied to model selection as well.

**Anand**: [19:22] But question: how do you select models? I'd love to see whatever you have on the chat. Okay, Vishnu Kiran is suggesting model intelligence as a factor. That's a pretty good one to look at. And we'll talk about benchmarks; I am curious to see what benchmarks you use. Sree is suggesting complexity or cost versus time. That brings in an important element: a smarter model, fine, but how much does it cost? Fable or Astra can burn a hole in the pocket. If it's a quick question, I may look at latency as well. That's a fair point. Complexity I had not thought of, but an interesting point, Sree.

**Anand**: [20:18] Test is saying benchmark and select. Yeah, obviously what we are leading towards, and the same as what Venkateswarlu said. Jagannath Prasad is saying domain-specific models, presumably meaning that depending on the domain, the models may change. Uttam is suggesting we compare the output of different models on a common task and then choose. Yes, again, rightly so. Look for context data and train data relevant to our use case. That I think is probably the crux that we need to bring in, Bhanu, which is: maybe benchmarking is obviously a good idea, but perhaps even relevant to our use cases, which is also what Dheeraj is suggesting. Vishnu Kiran is suggesting context window as one of the additional parameters to look at.

**Anand**: [21:17] Here is my hierarchy for picking models. I start with this chart, which I am updating from LMSYS Arena. For those of you who may be familiar with lmarena.ai, what they do is—let me keep it short—you can put in any question here, like "Why did the chicken cross the road?" And this, once you agree to the terms, will be answered by two different models, A and B. You don't know which is which. It automatically picks from two random models, and you then get to say A is better, both are good, both are bad, or B is better.

**Anand**: [22:15] The classic punchline is "to get to the other side." On the left it says, "Okay, yeah, but depending on who you ask: philosophers would say this, scientists would say this, Gordon Ramsay would say because it was raw." Okay, I didn't understand it, but no, I clearly prefer the longer answer in this particular case because it's telling me something new. At which point it'll say, "This was Gemini 1.5 Flash, this is MiniMax M2.7," and they've collected several millions of these preferences. So it's effectively human preference. Now, humans have biases. Most people tend to pick a longer answer just because it's longer and seems more detailed, and some of that bias has crept through into the benchmark, but it is a reasonably good benchmark on a variety of things.

**Anand**: [23:13] So what I do is take that as one axis, and you have a leaderboard here which shows the cost on the other axis. I've taken a simple cost metric, which is: what is the cost of input tokens? GPT-4 was one of the most expensive models at $30 per million tokens. Not the most, because at some point we had GPT-4.5 preview with $75 per million tokens. But I've been measuring this over time, and the way I think about it is more like an IQ level. The y-axis is the score that LMSYS Arena publishes. I map it to: is this like a high school student, high school graduate, college junior, master's student, PhD candidate, etc.?

**Anand**: [24:02] In March 2023, we had high school students at a cost of somewhere between $8 per million tokens to half a dollar per million tokens. A million tokens to a layman is probably easily explained as: if you had to read the entire seven-book Harry Potter series, how much would the agent or the model charge you? Or if you had to read the entire King James Bible, how much would the model charge you? That ranged between $8 to about half a dollar.

**Anand**: [24:37] Over time we had better models, and let's fast-forward one year: March 2024, we had college graduates. So four years of education, or maybe six, they covered in about one year at just as wide, maybe even wider spread of cost. March 2025, we had PhD-level intelligence at a reasonably high cost. And March 2026, this year, we had models smarter than tenured professors. So that's covering well over a decade, probably a decade and a half, of intelligence development covered in three years. That gives me a sense. It's almost like AI is growing up three, four, five times faster than humans are growing up, and humans obviously have reached some pretty high levels of intelligence. So if somebody says, "Will models become smarter than humans?", I say, "Yeah, they probably already are in many areas."

**Anand**: [25:46] And they're getting cheaper. Now with DeepSeek 4.1 Flash, for instance, we have PhD-level intelligence at 3.5 cents per million tokens, in comparison with let's say a GPT-6 Astra, which has probably the same level of intelligence, at $10. For $10, 1/100th of that is 10 cents; this is three times cheaper than that—300 times. That's roughly the difference between a $10,000 budget and a $3 million budget for the same thing, and you know which one is more likely to get approved.

**Anand**: [27:01] So this is my primary starting point. If people said, "Anand, give me one model," I would, as many of you have suggested, look at somebody else's benchmark, which is the cost versus the intelligence, and take a call. But one thing is clear: if I were looking at this, I would always look at the frontier, and the frontier is constantly changing, constantly evolving. Barely a week goes by without the frontier changing; every week the frontier tends to change. **So if that is the case, maybe the bigger lesson is not how do you choose a model, but rather how do you change when the new model comes?** Every week there's going to be a better model, right? So asking the question "Which model should I pick?" is not even a good question. It is the practice of **how do we keep updating our system with newer models with least effort?**

**Anand**: [27:30] It almost goes down the model router approach. But model routers may pick the best model for a given task. Is your system engineered so that when the model router keeps giving you better intelligence, or even when you manually switch to better and better models, you don't have to change much, or at least you don't have to spend time and effort? That is an important question.

**Anand**: [27:55] Siddhartha has posted a question on the chat: "Is it a kind of model council, a discussion amongst LLMs?" Not in this case, Siddhartha. This was just a question asked to two models, and they independently answered, and I was evaluating the result. A model council, of course, is very much a way of increasing the intelligence of a system on certain tasks; I wasn't talking about that. And that's a prompt to also suggest: please feel free to put in your questions or comments on the chat window.

**Anand**: [28:29] But the other part of it, of course, coming to model benchmarks, is creating your own benchmark. Jev is all the rage today, right? For those of you who may not be aware, Jev is a slightly different kind of model. It doesn't generate text; it can only classify between a set of outputs. So you can say high, medium, low; good, bad, ugly; violet, indigo, blue, green. It will take an input and give you one of those with some confidence. Or you can ask it for a score: how likely is it that this person will vote for Party A versus Party B? And it's like 70% or 60%, or it can give you true or false answers. But it is cheap, it is fast, and I think more importantly, it is a different kind of model.

**Anand**: [29:26] So everybody's going gaga over it. I said, "Okay, good, let me see if I should tell our team to completely switch to Jev for classification kinds of tasks." I took a banking dataset and created the same output: on the x-axis is the cost, and on the y-axis is the accuracy. When I originally benchmarked it, GPT-6 Luna had not been released; GPT-5.6 Luna was the only model that was released. But soon GPT-6 Luna was released, and what we found was GPT-6 Luna was doing both better and cheaper...

---

**Anand**: [30:00] ...better and cheaper than Jev. At least today I have no reason to tell the team to switch, or rather I have to tell them to switch to GPT-6 Luna. But the overhead of, "Oh, I have to get permission to use OpenRouter or Jev, but I already have an enterprise license with OpenAI," kind of discussions, we can completely avoid.

[30:23] And they're keeping a close eye. This is a new kind of architecture. Maybe it will get significantly cheaper, maybe it will get significantly better. Latency may be a factor. Is this something that can do stuff in real time, which the other models can't? So for instance, this is a real-time classification of network requests. And this is showing the requests as they are coming in. Jev is classifying the requests. And some of these, it's saying, "Oh, this is a path traversal attack, somebody's trying to do some SQL injection, somebody's trying to do a command injection," etc. So we can allow these in, we can not allow these in, and because the latency is only a few hundred milliseconds, **it is an acceptable smart classifier that can also catch LLM-based attacks**—meaning if somebody is putting in a request that is being sent to an LLM, but a web application firewall cannot detect that as a possible hack, this can catch it.

[31:23] So maybe there are other reasons to use it, **but ultimately all of this boils down to knowing your task, and figuring out if it is the right quality, cost, latency, whatever other factors you're looking at, that you need to benchmark on.**

[31:41] Now, here I am happily saying benchmark, benchmark, benchmark. But the other question that you would have is, "Look, Anand, somebody else is doing this for me. I get the result for free. For my task, I have to sit and spend time and effort. I have 250 other things to do. What do you think, I'm jobless?" The lucky thing that I found is **this entire benchmark, for instance, was created with me spending five minutes.** Because I went to ChatGPT, gave it access to my system on local MCP—or you could have gone to Codex, ChatGPT Desktop, whatever, Claude, Claude Code—and said, "Give me a benchmark."

[32:27] The exact sequence of prompts... I hope I can locate this. I wish I had opened this earlier. But okay, actually this is on GitHub. Let me see, I should be able to get that. Prompts... or... Jev, yeah. Yeah, I store my prompts here. Let me get the raw file. That's one. Two. Prompt three, prompt four, prompt five. Yeah, there you go. That is the chat that I had used to create the benchmark. Let me open that up and...

[33:37] The conversation was reasonably straightforward. I asked it, "Look, I'm hearing about Jev, so how is it different from the other frontier LLMs?" And it did whatever analysis, gave me the result. But the crux of it... Okay, yeah, and of course, "Where can I get cheap top-up credits for Jev? Is it available for free somewhere?" And eventually it told me that OpenRouter works. So then I said, "I'd like to take a dataset, a banking dataset. You download it. You compare it against some of the models that I'm interested in. And before you even run it, tell me how much is this benchmark going to cost." The entire benchmark ended up costing less than $2, which I'm very happy to pay. Least of my problems getting approved. And goes on. In fact, my next command was, yeah, just, "Rerun the whole thing, interpret it, and give me a HTML page of some kind." And finally, yeah, "Here is where I want you to store it." And last would have been, yeah, "Commit all of the code and push it."

[34:53] **In other words, the task of benchmarking is very delegatable to agents. We are using agents to figure out how good agents are.** It makes perfect sense, and if the cost of benchmarking is lower, we should have a whole lot more benchmarking, right? Now, obviously that lowers the... I mean that, in a sense, cheapens benchmarking. Not in a bad way. What I mean is that if you create a benchmark, you probably wouldn't say, "Oh, look, here's a new benchmark, everybody should use it." You'd probably use it in an adversarial way. **When somebody says, "Here is universally good advice," you create a small little benchmark to tell yourself whether for your task, this is a good idea or not.**

[35:39] Here I am using two pieces of infrastructure: one, agents, they are public; second, dataset, I chose a public dataset such as Banking77. But there's no reason why you can't use your own data as a benchmark, or have it create synthetic data. For example, one of the questions I had when GPT-Image-5... or this is something that I was sharing with Venky just as we were starting. So for this talk, my photo needs to be a high-resolution photo. I don't have a high-resolution photo. But who cares about lack of things these days? Venky, use your agent and make it high-resolution. These days, the agents are pretty good. And that apparently required a few iterations.

[36:35] Specifically, Venky suggested or mentioned that the type of hair that it adds to people seems to be reasonably similar across different types of people, which is interesting. Now, of course, I obviously always appreciate having more hair. That's a good thing, any kind of hair. But one of the things I was curious about was GPT-Image-2.5 has low, medium, high, x-high, and max quality guides. What difference does it really make? So my prompt to ChatGPT was, "Look, you run these benchmarks, then you look at the images, and tell me if you are able to see a difference. If so, then I will take a look at it."

[37:20] So it created these, and it said, look at low. I asked it to create a face. The wrinkles on the forehead, huh, they're kind of okay. I don't know how well it's coming across on Webex and how good a quality difference you are able to see. But here in medium, the wrinkles were a little more detailed. And in high, you could clearly see the wrinkles detailed out. But it said, and I also felt, that I can't see x-high and max as being any different or better. I can certainly see more freckles, but that was more a random artifact.

[38:00] So it went on, tested out a whole series of things. It said, "I'm going to draw a watch." And then it found that between low and high... sorry, low and max, maybe subtle difference, but no real... It said, "Maybe it can't draw water droplets better." Turned out that even in low, the water droplet was nearly perfect. It tried to create a barista. Between low and max, it could just about spot a difference in the quality of steam, the clarity of reflection, and stuff like that. But in almost all the cases, the result was: low to medium, yes, I can see a difference; medium to high, sometimes. And hair was one of those things where it said, "I can see a difference." Fiber is one of those things where I can see a difference.

[38:45] Let's see if I have one of those images. No, I don't. But it had a few that showed a difference there. But it said between x-high and... I mean, from high to x-high or even high to max, I'm not able to spot the difference. **So I have a clear cost-saving mechanism: I will default to medium when I need any kind of decent quality, and if it involves hair, fiber, cloth, that kind of a thing, I will go to high; otherwise, stick to low.** It doesn't make a difference in terms of quality. The cost, of course, is a huge difference. I don't know if that is documented here, but it's a fairly large cost difference and a latency difference as well. So in short, again, empiricism.

[39:39] Sree has a comment: "Using this kind of public benchmarking may not be reliable as there may be leakage during training." Possible if the benchmark has been made public. And people are taking two kinds of... three kinds of defenses against this. Simon Willison has a famous benchmark: a pelican on a bicycle. And several people have... it's a public benchmark. They draw a pelican riding a bicycle and see how good the result is. Most experiments are showing that that benchmark has not been incorporated explicitly as part of any training, with the possible exception, I think, of one DeepSeek model. Why? Because it is a very narrow, specific thing that most people don't care about. And most of the providers are probably saying, "Look, I should probably optimize for a broader SVG generation task than just this particular task." So if you have a niche benchmark, you make it public, but the providers don't care about it, it's still useful.

[40:47] Second kind of approach is the LMSYS Arena approach. We are talking about human preferences. It is anyway going to be benchmarked by people who are randomly going to type their own question. How do you game that? Well, it may be possible because Gemini somehow seemed to be getting on top of the LMSYS Arena for quite some time, so maybe they were gaming for what kinds of things would the lay public like. But you could say that, look, that is a relevant benchmark in the first place, that is what we're trying to optimize for.

[41:18] The third is where people keep the benchmark private. Artificial Analysis does that, for instance. Those held-out benchmarks, etc., are hard to game unless somebody from that company steals the data and joins another company. But the thing is, **the benchmarks are getting outdated because of saturation. That is, models are beating so many benchmarks to the point where it's a difference between 99.5% and 99.9%, you can't tell the difference.** So the leakage seems to be less of a problem than saturation. At least so far, that's what we have seen.

[41:59] Next question: **How do you choose agents?** And by agent, I mean ChatGPT versus Claude, Codex versus Claude Code, versus Pi... Please don't say benchmarking generically. If you are benchmarking, I would love to hear what benchmark you're using. Or if you have a preference, you say, "I use X for this task, Y for this task," or whatever. How do you choose agents?

[42:32] Sree says, "Based on level of autonomy and control." Fair enough. Venkateswarlu says, "We don't have access to multiple agents at work."

**Unsure**: [42:43] Only [inaudible].

**Anand**: [42:45] Which is, yeah, probably the easiest way to choose! You've been given something, and that's all you can use. "Intelligence, context window with LLM, and with same score and low cost," is what Vishnu Kiran says. I'm guessing, Vishnu Kiran, you're saying these are what I would... parameters that I would benchmark on. Though it's interesting that you say context window, because most agents manage context fairly well anyway. They can compact if required, they decide how many chats to go back in time, implement mini RAG kind of systems by themselves if required. But it's a fair point. Any other ways of picking?

[43:40] [Pause]

[44:09] Let me share a few thoughts on this. One benchmark that I like these days is the TerminalBench. You can see it's mostly flattened out, not a great benchmark to differentiate, but TerminalBench is effectively saying if I had to get it to run command-line tasks, how well does it do, at what cost? **By now, you would be seeing a switch from cost per input-output, cost per request, to cost per task—meaning getting the job done.** Because for an agent, that is the more relevant thing. You could have a really dumb model, and you could have a really simple harness. But if it doesn't overcomplicate and just gets to a result for simple stuff, that cost can actually be significantly lower than models, potentially with higher intelligence, that are even priced lower, but tend to overthink and therefore repeatedly handle the same task over and over again.

[44:58] So, cost per task. And the interesting entry on this in recent times has been: Qwen 3.8 Flash Next is certainly one; GLM-5.3-Flash has come in; some of you may have heard of the Mimo model which doesn't seem to have figured here, but that seemed to be doing pretty well on some of these benchmarks. Of course, the right edge of high cost is dominated by Anthropic. The mid-end is right now dominated by the OpenAI models, especially with GPT-6 coming in with crazy prices. But, again, this is still models, not entirely the agents.

[45:43] The reason I'm pointing to this is because I use this to choose the family of models to run within an agent. And for high quality and high cost, Anthropic's Claude Code seems to be the one to look at. And for mid-quality, mid-performance, mid-cost is on the OpenAI side. As Venkateswarlu said, if you don't have access to a different one and you're, let's say, using Gemini, nothing wrong with it. That works perfectly fine in several cases as well. But when you do have a choice, I prefer, given how much I'm using agents on a regular basis, to benchmark.

[46:33] My first attempt at benchmarking was like this: I said, "Create a single-page web app that renders a GitHub user profile and their activity comprehensively, and makes sure that the URL can be changed." And I gave it to a bunch of harnesses and models: OpenCode Sonnet 4.5, OpenCode GPT-5 Codex, Codex with GPT-5 Codex, all of these kinds of combinations. And then manually looked at the output.

[47:05] So, for instance, on OpenCode, Grok-4 and GLM-4.6 didn't even give proper output. OpenCode with Gemini 2.5 Pro gave me this result: Linus's profile was this page. Okay, fine. So I manually gave it a score of 3, and logged the cost: 14 cents, took 37 seconds, that's pretty quick. Claude Code with Sonnet 4.5 gave me a result that looked like this: clearly much better formatted, has more details. I like this more, a lot more actually, so I gave it a score of 5. The best came from Sonnet 4.5, again, but not from Claude Code, but from OpenCode. And it was significantly better, in my opinion, than that. And here's what you see: the visual quality, OpenCode had taken it up much higher.

[48:03] That was when I was surprised. Now, Claude Code is supposed to be doing a really good job, especially on the UI with Sonnet 4.5, as well as any of the Anthropic models. But here it is: OpenCode is doing an even better job, at least on this one task. So at least I should start taking it seriously and explore with some of the other harnesses. And went on a certain path, and had been recommending OpenCode to a bunch of people and all that good stuff. This benchmark is very old, as you can see from the times, but there are two aspects of this benchmark that I wanted to flag off.

[48:40] The first is that the prompt is really small. It's a task that is easy for me to specify. But more importantly, the output, I can judge at a glance. If you show me these three pages and ask me to score, I can immediately say, "Aha, this is better, this is worse." The visual nature of those makes it easy. **When you are benchmarking, if you can have the agent generate something which you can assess the quality of at a glance—even if it is a back-end task, if you can have it convert into a form that you can quickly assess—that is probably one of the most powerful and important things that you should be thinking about.**

[49:26] I just wanted to pause for a couple of things. There are a bunch of beeps coming. Is that coming from here, the chat, or the panels here, or is it something on my machine? Want to check.

**Venky**: [49:52] We don't hear any beeps, Anand.

**Anand**: [49:54] Oh, good.

**Venky**: [49:55] Must be from your side.

**Anand**: [50:01] All right. I'm going to go on to one more thing, and then pause, because let's keep this interactive. I have a few other things to cover, but we're a bit past midway, and I want to make sure that we spend at least half an hour discussing. Actually, I'm going to skip this. What I was going to add was the next thing is: when creating a benchmark, why should I have to sit and think about a new benchmark? So I went again to ChatGPT, and said, "Look, look at some of the recent tasks that I've been working on."

**Unsure**: [50:35] Yes, sir. ... Thank you, sir.

**Anand**: [50:42] One of those tasks was the same page that you saw, the GPT-Image-2.5 comparison. The problem I had was the page was not loading fast enough. So, "Can you load the page faster?" was one of the tasks that I had already given to a coding agent. Similarly, I was scraping WhatsApp. I had some problems with it. I was looking at the console logs for an MCP, had some problems with it. And ChatGPT went through my logs, and found that some of these were pretty good benchmarks.

[51:24] So it said, "Look, what I can do is take, let's say, Pi as one of the harnesses, and evaluate some of the newer models: Gemma 4, Qwen 3.6, GPT-6 Luna. Which ones do better on these?" Created the evaluation criteria, and gave me the result. And the short summary was GPT-6 Luna was beating all of them like crazy on quality. Qwen 3.6 kind of worked, and Gemma 4 didn't really work. The reason I was benchmarking this is both Gemma 4, the lighter version, and Qwen 3.6 I can run on my laptop on a flight. So if I'm stuck without any frontier models, can I use them was the question. And how would it fare against even a really light model? Turns out not very well, but at least I can get tolerable results from Qwen 3.6, so that's going to be my default model when I'm on a flight and don't have access to models.

[52:28] This obviously is something that will change over time, but now I have a personalized benchmark based on my own tasks that you can use. **So the theme again is: you don't necessarily need to hunt for a benchmark that suits your work. You can take your own logs and convert that to benchmarks.** That's something that I will return to in a short while, time permitting. But let's talk. Would love to hear, feel free to unmute yourself or put on the chat: What are some things that you are exploring with agentic AI in any shape or form? And in case it's something that we can empirically verify, let's do that.

**Venky**: [53:19] Yeah, Anand, I just want to revisit selection of agents, right? So at least my understanding is, you have a model, and on top of it you write some harness, and that becomes an agent. So when you're evaluating agents, right, few of them you don't have enough, you know, control, like you can't change many of the things. Say, for example, given Claude Code or something, I can't go and change few things within that agent. But if I take an open source, DeepAgents, I'll write everything. So how do you compare? Because my effort is going into the harness, and something is already given. So there's no point in evaluating models also. Probably you take a model which is cheapest in the last six months, and write a really good harness, and that should work. **So selecting models is becoming kind of obsolete. I mean, it's not a difficult decision to make: pick whatever is the cheapest and least complex, and then if you can write your own harness, put your efforts there.** Is my understanding correct? And how did you evaluate those agents when you said that you're doing...

**Anand**: [54:44] To your question, and let me paraphrase, tell me if I've got this wrong. You're saying, "Look, model selection is easy. It's reasonably clear from benchmarks which models are good from a cost-quality perspective, by and large. And from a harness perspective, that's probably what I need to tune. And even there, it's somewhat limited, but what limited changes I can make there is what is worth spending time on." Have I understood your statement correctly?

**Venky**: [55:17] The comparison itself for agents is a difficult thing because, yeah, the parameters, there are few which I can control in few frameworks, and there are few which I can't control in few frameworks. How do I compare that?

**Anand**: [55:36] There are two parts to how I do it. First, I ask whether I have a problem worth solving. And in your case, you're saying, "Model selection for me is a problem that's not worth solving," which may well be true, and it's coming out of your experience saying, "The good models are fine, cost is not a problem, quality is not a problem, let me go with them." And I think that's a perfectly reasonable decision.

[56:07] I am trying to develop a sense of discomfort with that state wherever I can. Meaning, if agents are going to be doing all the work, what job will I have? I'm trying to discover that. One of the ways in which I'm trying to figure that out is by trying to find things that I'm unhappy about agents' performance on.

[56:36] So, in the case of models, for instance, what I tell myself is, **"Anand, if you're happy with any of these models, then that means you don't have tough enough a problem that will be able to differentiate between models."** And I suffer from this. I really am finding it very hard to find problems that I can give to one model and it does well, and give to another model and it doesn't do well. But if I can get there, that means that I have differentiated myself from a large number of people, because I'm able to specify complex tasks, and that capability is important in the agentic era. So first thing that I do is pick areas where I find myself comfortable, and try and become uncomfortable with that.

[57:24] Once I've solved that problem—and how do I solve it? I go to Claude or ChatGPT and say, "Boss, this is my problem, give me ideas." And it'll give me some rubbish ideas. I say, "No, no, no, go research, look at my work, tell me something that I can relate to." Then it'll tell me something that I can't understand. I say, "Simplify it." A day, a week, a month later, something clicks.

[57:46] Now I have something that can differentiate between two things, which you have with agents presumably. Let's assume that you have two tasks. I give it to some configuration, it seems to be working fine. Some other configuration seems to be working fine. But how can I do multidimensional comparison? Partner, here's the thing. This is something that practically any data scientist has tackled on a regular basis, which is: I have 100 parameters. Some of these parameters are continuous. Some of these parameters are unstructured, like literally the prompt, or the custom instruction, etc. I need to figure it out. How do you do it?

[58:25] Well, how do people take massive pieces of text and start doing structured analysis? You probably extract some elements. You categorize it. You say, "This belongs to category A, this belongs to category B." You may say, for instance, system instruction: long system instruction versus short system instruction, does that make a difference? Specific versus broad, giving it a list of tools versus not having it auto-discover tool capabilities. Now, how does one come up with these ideas? Take a guess, test the hypothesis, continuous iteration.

[58:57] So put another way, **a growing part of the skill that I'm trying to also learn for myself is: how do I take agent surfaces—that is, the kinds of things that I can change with agents—and convert them into testable parameters?** A useful skill. What is my process for that? For everything, it will go to Claude or ChatGPT and ask it, "Look, this is my problem. How have experts solved it? Give me some ideas." It usually gives me some ideas, of which I pick some.

[59:27] Then, once we have this, how do I run the benchmark? That is reasonably straightforward. I then pick two configurations: A versus B. Which is better? One by one. Now, that does not mean that A will always beat B in all circumstances. So sometimes I have to go to multidimensional searches. That makes it a little more expensive. But then I also ask these models, "Look, how often do I need multidimensional? Here is my problem. I have identified a tough problem. You just keep iterating until you are able to find a solution..."

---

**Anand**: [60:00] You just keep iterating until you are able to find a solution that solves this particular problem sufficiently well for me, tweaking all the parameters. In other words, the equivalent of AutoML.

**Anand**: [60:15] You tell it, "You go figure out what the agent parameters are. You keep tweaking them until you find something that solves this particular problem reasonably reliably. Leave it at that." That works, too.

**Anand**: [60:27] These are my three approaches:

1. **Find a problem that can differentiate**—fails under one circumstance, fails under another circumstance. The skill to do that, I think, will be relevant for at least a few more years.
2. **Be able to specify a verification criteria**, the rubric effectively, even if it is a messy surface like an agent.
3. **Be able to automatically evaluate against this.**

**Anand**: [61:00] So, **specification, verification, execution** is the chain that I'm trying to convert almost any product to. Did that answer you, Sree, or any part of it?

**Sree**: [61:14] Yeah, yeah, thanks. No, no, I think yeah.

**Anand**: [61:17] Any other question or suggestions, thoughts, comments on explorations in Agentic AI? You're welcome to put that in the chat or speak up.

**Venky**: [61:34] Anand, as we discuss, many of our folks are developers. So maybe if you can share some of your findings and experiences with coding as a task, right?

**Venky**: [61:52] And a related question to that is, as agents become better and better at coding, what is the expectation from a software developer? Which I think you covered in some of your talks, but it will be good to address that here for the audience.

**Anand**: [62:10] The cynical part of the answer to the second question is, try and keep your manager in the dark as much as possible once they figure out that agents can do everything that you're doing and they're getting smarter.

**Anand**: [62:30] So here are a few very real, very practical, cynical suggestions that you should keep in mind:

**Anand**: [62:41] Number one: **Security is your biggest strength.** In any discussion where there is even a small chance that an agent can take over your job, ask it: "Is it safe to use? Has it been regulatorily approved? Has it been approved by compliance? Has it been approved by..." Just toss in all the phrases that you can. "What if it hallucinates? What risk percentage are you able to tolerate?" Once you bring in the language of uncertainty, you will be able to kill many agentic initiatives. **It is a very potent, very powerful weapon. Wield it well.**

**Anand**: [63:26] The second thing that you should learn to make sure that you have a career while agents are doing it is, **it is very, very hard to verify output, and with agents, you can create a lot of output.**

**Anand**: [63:45] So, if you are able to constantly generate output that has two characteristics:

1. Nobody is particularly going to verify it.
2. But secondly, if it is wrong, it either doesn't cause any harm or cannot even be detected.

**Anand**: [64:08] Then you have no problem. Let us take some examples. I showed you one cybersecurity classification thing. Realistically, how often does a cybersecurity attack happen? So, if you built some rubbish classifier and deployed it, and you deployed not one, but 50, and there isn't enough capacity for someone to verify it, there's a good chance that it'll go into production. And you've now deployed something to production, good for you.

**Anand**: [64:41] Don't wait for too long before hunting for your next job because you're building up a pile of risk that might explode at any point. But at least make sure you plan to move teams and all that. But that is a reasonably good strategy, which is: **keep pushing stuff before the shit hits the roof, make sure you move to a different team or a different organization.**

**Anand**: [65:04] Obviously, I'm giving this to you as anti-patterns—what to watch out for and all that. But it is useful also to think of these as strategies that people will naturally, even subconsciously, adopt. If you give me 10 tasks, and if I just blindly give it to the agent, and take the output and give it back to you without verifying robustly, I am actually able to complete those 10 tasks and sleep at least at midnight instead of at 4:00 AM, I would do that.

**Unsure**: [65:33] [inaudible] That way...

**Anand**: [65:36] Sorry, did someone have a comment?

**Anand**: [65:43] But that is the second part of it. To the first part—oh, sorry Venky, you were going to say something?

**Venky**: [65:48] Oh, I was just saying, okay, so these are anti-patterns, but what are the positive approaches?

**Anand**: [65:56] Let's come to that.

**Anand**: [66:00] Firstly, **sharpening your tools**. If you're using a set of tools, how do you go about improving them? Let me share my screen and share one of the ways I was using this.

**Anand**: [66:12] I asked Codex to go through how I'm using Codex. The question is: see, Codex has released so many new features. What am I using? What am I not using? What is the impact of it? Effectively running an analysis on my own logs.

**Anand**: [66:30] And here's roughly what it said. It said, "Look Anand, when a new model comes, you have about 75 or 76% adoption. When there's a new workflow, your adoption is zero." What rubbish! What does that even mean?

**Anand**: [66:45] It went through. It said, "Look, I've read your logs, extracted the signals, blah, blah, blah. And what I find is that, for instance, when GPT-5.3 Codex was released, in the 95 sessions right after the release window, in 72 of those you used the newer model, and the rest you used the older model. That's good adoption. So you're quickly switching models instead of staying with the old one."

**Anand**: [67:12] "Or, manual shell parallel patterns—that is, in the command line you're running one Codex session; in another command line you're running another Codex session. Effectively you're manually running sessions in parallel, sometimes on the same repository, about 68% of the time. And this is not a direct Codex feature as such, but still a workflow pattern to keep in mind."

**Anand**: [67:40] "Web search events: after they were released, you were barely adopting it—103 sessions, but in only 19 of those you were using it. Maybe there wasn't a need, but it represents a certain degree of underuse."

**Anand**: [67:54] And here is the timeline view of this. For instance, when web search default came in, my usage was only 18.5%. When the model release happened, that suddenly is 75.8%. After that, another feature of status line, I never used it. Memory controls, never used it.

**Anand**: [68:18] So it gave me finally a list saying, looking at when the models were released or when a feature was released, where in each of your 900-odd Codex sessions would it have had a benefit. And it said, **the biggest benefit is parallel tool calls**: 457 sessions would have benefited through parallel tool calls because it was running sequential tool calls when it didn't need to. Your execution speed would have been higher, probably error rates would have come down. Clear benefit.

**Anand**: [68:54] Request user input: these are situations where Codex could have asked you a question and should have asked you a question. You ended up either changing something or interrupted something, etc., but your permissions are not allowing it. Change your permissions, and this solves the problem.

**Anand**: [69:13] And it effectively gave me a simulator saying, look, if you close the gap—maybe 40% of these gaps you are able to cover—your saving estimate is 11.3 hours. Okay! At this point I say, fine, to save 11 hours I'm happy to spend two hours doing this. I'm even happy to spend five hours doing this. That is helpful.

**Anand**: [69:39] Now, you may be thinking, "Hold on, wait, this is again saying benchmarking?" Yes, that is true, but I'm sharing two specific things:

1. **Your agent logs are one of the most powerful diagnostic devices. Use agents on agent logs, and you will find a lot of stuff about your usage.**
2. **Agent capabilities: you will absolutely not be able to keep track, and you don't need to, because the agents can keep track of agentic capabilities.**

**Anand**: [70:13] And you can roughly summarize the entire exercise and do it by yourself as this one prompt: **"Find out all the new features of Gemini CLI [or pick your agent] that have been released in the last eight months, and find out which ones of those would have the maximum impact for me based on my logs."**

**Anand**: [70:36] What if you run this at a team level? What if you, as a tech lead, told your team, "Give me your logs, and I will do an analysis across all of these, and suggest what you might do"? And it doesn't even have to be against capabilities; it could simply be: what are you doing well, what are you not doing?

**Anand**: [70:55] Which incidentally is exactly what I did a few weeks ago for one of our teams. Dharmendra has a team of developers, and I asked—this is the session that actually did the analysis—here is the email that I shared. Basically the process was: Dharmendra, please tell your team to share on Google Drive their session logs. They did. Seven of them, 1,100 sessions.

**Anand**: [71:26] And the biggest takeaway from this was: **coding has become very fast, but testing and ownership has not followed.**

**Anand**: [71:37] Basically, what people are doing is—okay, maybe to pause it... Yeah. The biggest problem is, after the work is being done, **only about 2% of the Codex sessions and 3% of the Claude sessions had programmatic validation**, meaning people are building something and giving it to you 97, 98% of the time without even a unit test across these sessions.

**Anand**: [72:18] Standard basic practice would be at least test at the end, and even better practice would be write the test cases first and then do it. As human coding, that is obviously a lot of work. But when an agent is doing it, what difference does it make, especially when if it writes the tests first and then codes against it, you are much more confident that it's doing a good job? When you make an edit, regressions will happen a lot less often.

**Anand**: [72:49] So, the recommendation to him and the recommendation to you is precisely—and this is by far the most common failure that I've seen amongst developers using agents—which is: **at the very least, have the agent show evidence that the change worked, minimum, allowing you to manually test. Better yet, tell the agent how it should test.**

**Anand**: [73:21] Just telling the agent to test is also a reasonably good step, but if you tell the agent, "Here is how I would have tested it; you test it the same way." Now, if, for instance, it is a simple backend code, at least do type checking on it. If it is an API, actually call it; better yet, write test cases. If it is UI, then open the browser, click, explore, run it. This is probably the single biggest [thing].

**Anand**: [73:49] And it goes on for a whole series of second-order things, but here is my thing: this one change in behavior has the highest uplift. As Uttam put on the chat, **ask the agents to do test-driven development**. The biggest! This is now something that you can start socializing as a common skill or even just a simple line in your `agents.md`, global `agents.md`, either for the team or the individual, saying, **"Write tests first, or where possible, write failing tests first, and then implement,"** which is almost exactly the wording of my `agents.md`.

**Anand**: [74:34] But the general principle, again, is: don't rely on generic advice. This was based on experiments with a specific team based on the logs themselves.

**Anand**: [74:49] There is a second piece of advice that I could probably come to, but let me hold off on that depending on the discussion. We can probably turn to that, otherwise I'll come to it at the end.

**Anand**: [75:03] There is a question from Ramaswamy: "How do you see the future evolving between frontier AI models and open-weight models? In regulated industries, what's the expected evolution path from experimentation to production adoption of open weights, and what are the key challenges that should be overcome?"

**Anand**: [75:26] At the moment, the open-weight models are lagging maybe six to nine months from the frontier models. Obviously, the economics of open-weight models is not as solid as the frontier models. That may change. With software, there was a big question on why would open-source software ever win when nobody's paying for it. And today we see a lot of open-source software that's arguably more successful than closed-source software. The same might happen for open weights; I don't know.

**Anand**: [76:03] So the future I see is only a few months ahead, and it looks like the open-weights models—at least there is a strong incentive for the Chinese providers to continue providing open-weight models to compete against the US frontier models. Beyond when the geopolitics changes, no idea how it will go.

**Anand**: [76:30] For regulated industries, there is little choice but to adopt open-weight models, partly because they can't even get into a confidentiality agreement in some cases. In an emergency room in the US, you cannot take even your phone or any kind of device that is connected externally. It has to be a model that is deployed physically inside that environment. Then what do you do? That becomes an edge AI kind of problem. And of course, edge AI scenarios are real in many areas.

**Anand**: [77:07] Banking is at least slightly better than an emergency room. You can still get into a deal with a cloud provider saying they will store the data in a specific geography or they've gone through the relevant audits that a regulator is fine with, etc. So the need for that may be slightly smaller or in fewer areas.

**Anand**: [77:31] But what I'm seeing in almost all of these cases is that **the path to production is pretty rare.** Why is that? Quality of open-weight models is not that good compared to the frontier models. The effort is significantly higher. Most people are saying the percentage of use cases where it's worth that effort is a lot less as a percentage compared to the popular use cases. There's so much benefit there, why would we spend scarce time and resources on solving a tougher problem with lesser benefit? Which is not to say that it will not happen. It will happen, but slower.

**Anand**: [78:17] And the challenges that must be overcome are, I think, primarily:

1. **The ease with which one can deploy open-weights models in a machine.** It's gently happening. It's now easier to run Ollama or llama.cpp. What's making it even easier is the way I install most software today on my machine is: go to Codex and say, "Codex, install this software, then write a quick two-, three-line step-by-step setup on how I should install it in the future." Realistically, those instructions are not for me; those are for a future avatar of you, but still make it human-friendly. That's it, and it installs the software, and by and large it is working fine.

**Anand**: [78:56] Similarly, cloud controls: I don't even go to Cloudflare or GCP and have it do stuff. I tell it, "You go to Cloudflare, make whatever changes that are required, convert it to HTTPS." One of my recent instructions was: "Go to Google Search Console, find out all of the errors that it is reporting about my blog. Go to my Cloudflare console and my GitHub repository, fix them." That's it. But what this is doing is effectively making a difficult operational flow—things that would have slowed us down from an infrastructure perspective—much faster, so that one challenge is definitely shrinking.

**Anand**: [79:39] 2. **Another challenge is the quality of models.** The good part is that is also steadily increasing. Six months ago, I would not have coded on a flight. Now I am okay to code on a flight, within reasonable limits; I'll watch the code a little carefully. Six months down the line, I suspect I will happily code on a flight without even checking some of the simpler tasks.

**Anand**: [80:00] 3. **The third thing that needs to be overcome, I think, is just people's comfort with open-weight models** and the whole, "Oh, but it will hallucinate more," etc. With open-source software, people were constantly saying, "Oh, but is it secure?" And then realized that open-source software is probably more secure than commercial software. Similarly, attitudes may change. I'm not saying that open-source models hallucinate less or anything; I'm just saying that currently there is also a perception bias in some fronts, saying that, "I would rather have somebody assure me through a frontier model than I not have that assurance with an open-weights model."

**Anand**: [80:40] These, in my mind, are, in order, the challenges that need to be overcome. Any other question from anyone?

**Venky**: [81:14] Anand, do you have more to present or it's questions?

**Anand**: [81:17] Just one point, which won't take long.

**Unsure**: [81:19] Anand, I will have a question. So you spoke about Jev. Traditionally we see classical machine learning models, most of the organizations, even when we got these GenAI, agentic AI stuff, traditionally a lot of organizations were still running classical machine learning models. Primarily the use cases were in classification, where you know you don't need a lot of output document or theoretical output coming in. Primarily it was like, you know, "Should I give a loan or not?" and, you know, "Should I top up the card or not?" or "Should I offer a travel discount?" Such kinds of models were there.

**Unsure**: [82:02] But now with Jev coming in, while most of, if you see, enterprise work is on such kind of predictive capabilities, right? I have not experimented a lot, I did a little bit of experiment on Jev, but did you do any such kind of things like where we could use this and then what would be the shape of those traditional classical machine learning style of modeling where we have a lot in companies right now, that will be completely revamped? Because till now, you know, where we still have the generative AI capabilities telling sentiment whether it is false or, you know, sentiment is positive or neutral, it was not pretty much baked into most of the companies' traditional use cases. But with Jev coming in, I think that is going to go away with—with a much more lesser cost. What is your thought on that?

**Anand**: [83:00] Agreed. The difference between at least the—what do they call it—the shape of the models. So, the stark difference between models that can produce deterministic and structured outputs versus non-deterministic, unstructured outputs was big. And Jev is coming somewhere in the middle, and I expect there'll be more models coming in of that kind.

**Anand**: [83:25] I'm not sure that will make it easier for people who are saying, "Oh, I'm using a machine learning model, and I can migrate to a Jev type of model and get closer to GenAI," I think. I suspect it'll add to the confusion a little bit, because then they will ask, "So is GenAI—is Jev GenAI?" "What do you mean, is Jev GenAI?" "No, no, will it make mistakes?" Even your ML classifier makes mistakes. "Ah, but no, that will hallucinate."

**Anand**: [84:00] "Okay..." and then somebody will come up with a new kind of architecture. The point is, the people who get confused will get confused, and **variety confuses more rather than less.** I'm not saying therefore it will make it harder to shift; I'm saying I'm not convinced that this will necessarily ease the path.

**Anand**: [84:26] I see a stronger force when somebody says, **"I will lower your cost by 80% and your risk by 70%."** Everybody says, "Okay." Sometimes that risk is being taken by an external party, in which case people are saying, "Fantastic, then I can just blame you for everything. My regulator is happy, my insurer is happy, my boss is happy, perfect." Now, whether you use GenAI, or whether you use people sitting and solving the problem, or you write a grand Excel sheet for it, I don't care; liability has been shifted. If a team is willing to, within the organization, take that ownership, then again, the problem gets solved.

**Anand**: [85:05] So that is certainly a stronger mechanism. And the question therefore becomes, is Jev moving the frontier on the risk-return curve? So far, it hasn't, at least on the few benchmarks that I've run. So yeah, for me, it hasn't yet, but it's a direction to go in. That's my thought.

**Anand**: [85:29] And that actually leads me to the final point I wanted to make, which is, one of the big problems that we have with the entire large language model and GenAI space is the notion of hallucination, that it can make a mistake. And that is both when agents are coding, as well as when agents are being used to generate the output as part of your code.

**Anand**: [85:56] The—one clean solution to that—actually maybe two—seems to be... let me share my screen. How to... Yeah.

**Anand**: [86:18] Is—let's take an example. So we were classifying a series of chat messages, like, "When will I receive my order? Should it be put into the delivery period queue or should it be classified as track order?" Or, "What do I need to register? Should it be put into registration problems or create account?"

**Anand**: [86:41] Different models, as you can see on the left, have been tackling these—there's an enormous list of chat messages—and some of them are very easy, most of the models pass. Some of them are increasingly tougher, most of the models fail; in fact, on some of them, every model fails, which leads me to ask, was the classification done correctly in the first place? But in short, there are error rates. Different models have different accuracies.

**Anand**: [87:08] But interestingly, **the errors are not correlated.** If I take, let's say, Amazon Nova Micro v1 versus Claude 3.5 Haiku, the correlation is about 70% or so. But for some of these, like let's say GPT-4.1 Nano versus Gemma 3, correlation is closer to 5% or 10%, meaning they are making independent mistakes, which means I can double-check, cross-check.

**Anand**: [87:41] And if we cross-check, what we find is that if you take one model, on average—if you took any one of those models on average—you got a 14% error. **But if you cross-check and say, "I will only let it through if both models agree," the error rate falls to 3.7%. Triple-check: 2.2%. Quintuple-check: as low as 0.7%.** You may not be able to get rid of error, but the cost of models is not that high, and by saying, "Only if all five models agree will I let something through," means I can get 99.3% accuracy.

**Anand**: [88:14] "But what about if the models do disagree?" Okay, put a manual queue. Which means that I have, in this particular case, about 28% of the work that needs to be still reviewed manually. Now, if I go to an operations manager and say, "Look, I will reduce 72% of your work and give it to you at 99.3% quality." "Hey boss, my team only gets to 95% quality. 99.3 is way better than what I can do myself with humans, and at almost one-fourth the cost."

**Anand**: [88:47] So just cross-checking is helping.

**Anand**: [88:51] And the other thing that we can do—sorry, I know we have spilled over, I will try and wrap up in just two minutes—the other thing that we can do is ask models how confident they are. Many ways of doing it—logprobs are a good way, but I'm not going to go into that—but the thing is, when a model says it is 90% confident, it is actually not right 90% of the time. They tend to be overconfident. So, for instance, if I took—let's take this—GPT-4.1 Nano: when it says it's 80 to 90% confident, it actually is only 50% right. Overconfidence is consistent across models.

**Anand**: [89:30] But the good part is **you can calibrate that.** And you can say, when something reports 85%, treat that as like 50%. When GPT-4.1 Nano reports 95 to 97%, treat this as actually 75%. Once you have that calibration curve, then you can start actually reporting, saying, "This is the level of confidence. I will cross-check anything that is lower than this level of confidence." So I don't even have to double-check everything and get the entire result.

**Anand**: [90:02] Same applies for code as well. **Have an agent adversarially test it.** Find all the mistakes in this. That's effectively what we're doing in a code review; there's no reason why a human be the only one that does code review. Let agents talk to other agents, and find all the mistakes, and then what comes to you should be something easy to review: "These are the things I'm not sure about." And obviously, therefore, the person who's reviewing that needs to be really experienced, but that's what we're working towards.

**Anand**: [90:31] In short, if I had to summarize all of what I'm saying, it is: look, people will say lots of things, I will happily say all kinds of things. These are things that might have worked for me. But **you should just test**. Whether it's prompting advice, what model to use, what agents to use: test it.

**Anand**: [90:50] **Your logs—session logs, and any logs in general—are probably the best way to improve any kind of workflow.**

**Anand**: [90:59] And when you are following any workflow—whether it's writing code, whether it's generating output using AI, whatever—**make sure verification is part of that workflow. Use test-driven development, use double-checking or triple-checking as a means for validation, use confidence calibration.**

**Anand**: [91:19] So, benchmarking is not just for your workflow; benchmarking is a verification mechanism and should be literally part of the delivered workflow as well.

**Anand**: [91:30] In other words, **let's test**. That may be the most important thing that I would like to share. Thank you.

**Venky**: [91:45] All right. Thank you, Anand. A lot of things to think about and reflect on. Unfortunately, a lot of tools that you have showed, we cannot access from office; maybe we'll need to do it in our personal capacity.

**Venky**: [92:01] So with that, again, on behalf of DTI and all the people who are attending this, thank you for the wonderful and enlightening presentation.

**Venky**: [92:12] Earlier, you were planning to do more hands-on, but unfortunately we did not have the software required, which I think probably a month from now we'll have what you wanted in terms of Gemini CLI and [3.8? Flash], maybe we'll have one more session in the future. With that, I thank you, and I'll see you again. Bye.

**Anand**: [92:35] Thanks, everyone. Bye.

**Venky**: [92:38] Bye, everyone.

**Unsure**: [92:39] Thanks, Anand.

# Takeaways

- Test prompting advice
- Benchmark models & agents
- Improve using logs
- Verify as part of workflow

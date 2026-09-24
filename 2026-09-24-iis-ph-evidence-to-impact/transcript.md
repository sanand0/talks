---
model: gemini-3-flash-preview
cost: 0.187526
prompt: |-
  Anand delivered a talk on AI, with a host introducing him at the start and summarizing at the end. There were a few audience questions towards the end.
---

# 2026-09-24 IIS Evidence to Impact Talk

## Transcript

**Host**: [00:00] ...turning data into competitive advantage. Organizations generate more data than ever before. Learn how AI and analytics can transform data into actionable insights that improve business performance and decision-making. Our speaker this morning is the Head of Innovation and Research at Straive. Ladies and gentlemen, Anand S.

*(Applause)*

**Anand**: [00:34] It's switched. I hope you can hear me. It's going to be easier for me to type without a mic—easier that way.

**Anand**: [00:43] **I think it pays to be a little skeptical about AI.** I'm not saying that AI doesn't deliver its promises, but it's not something we know too well, and therefore **evidence is something we're constantly looking for.** And what I'm finding is that **AI is pretty weird. We don't really understand it.**

**Anand**: [01:03] Let's do a quick check. Supposing I asked ChatGPT to pick a random number from 1 to 100, what number do you think it would pick the most? Just take a guess.

**Audience Member**: [01:15] 75.

**Anand**: [01:16] 75.

**Audience Member**: [01:16] 37.

**Anand**: [01:17] 37.

**Audience Member**: [01:18] 15.

**Anand**: [01:18] 15.

**Audience Member**: [01:19] Three. One.

**Anand**: [01:19] 1, 3.

**Audience Member**: [01:23] 99.

**Anand**: [01:24] 99.

**Audience Member**: [01:25] 100.

**Anand**: [01:25] 100.

**Audience Member**: [01:27] 50.

**Anand**: [01:27] 50. Still waiting for... Yours was the closest, but not quite.

**Audience Member**: [01:32] 1.

**Anand**: [01:33] 1. You know what? **I have never seen it pick a single-digit number, ever. I have never seen it pick something with repeated digits, ever.**

**Anand**: [01:46] It's a random number, right? I mean, they should be as common as the other. So when I did the experiment—and it wasn't just with ChatGPT, but we'll sort them through one by one—this...

**Host**: [01:58] Somebody from the audience said that they can't see the screen.

**Anand**: [02:01] I can sit.

**Host**: [02:02] Yes.

**Anand**: [02:02] Or I can shift or something. Yeah, I can sit. Thank you for flagging that. Yeah, that's easy enough.

**Anand**: [02:14] Here is what happens, or happened, when I ran it on GPT-3.5 Turbo: **47 just popped up way ahead.** 42, you'll see gently nudges, and 37, yeah, is on the list. Nothing below 10. No 11, no 22, no 33, no 44, no 55, no repeated digits. Why 47? I don't know. It doesn't know either. If you asked it, "Do you have a favorite number?" it says, "No, I'll just guess any number."

**Anand**: [02:53] Different models pick differently. Now, **Claude 3 Haiku really likes 42.** This, I know why. Does anyone know why 42?

**Anand**: [03:09] If there were programmers in the room, you would have probably latched on to it. Douglas Adams, a BBC radio producer, radio program host—he authored *The Hitchhiker's Guide to the Galaxy*. It was a fairly famous show in the '80s. And in *The Hitchhiker's Guide*, there is a computer, Deep Thought, which took several millions of years to answer the ultimate question of life, the universe, and everything. After waiting millions of years, people went to it and said, "Have you got the answer?" It said, "Yes." "What is the answer?" "42." Like, "Okay, what is the question?" Deep Thought thought for a while and said, "I don't know."

**Anand**: [04:04] And then the story goes on, and it's a pretty interesting one. But 42 became famous because of that. And you'll find it in a lot of programming literature, and Claude's been trained on a lot of programming literature, and for some reason, it just picks 42. But it likes 47 too, and 57, and 67, and 87—numbers ending in 7. You're seeing the pattern, right?

**Anand**: [04:27] Gemini, at least 1.0, did seem to be slightly broader. It did manage to guess 0, 97, etc., but the subsequent models tended to have a narrower range. **In fact, you could say that how good a model is, is dependent on how non-randomly it guesses.** Think about it: if a model is guessing randomly, then why would you ask it a question? And if you wanted to guess a random number, you would write a macro in Excel, or ask a program to guess a random number, or just close your eyes and type something.

**Anand**: [05:06] It's almost like **some of the things that we expect a computer to do well, models don't seem to do well.** And they seem to have choices for weird reasons, like 42—I mean, what? Numbers ending with 7, I can kind of understand; that's how humans think. But yeah, okay, 42? It's weird. So that's one thing that's clear to me.

**Anand**: [05:30] It's also not clear to me what they can do well and what they can't do well. How many of you think LLMs are really good at multiplication? Raise your hands. Numerical multiplication. One. How many of you think that it's not good at multiplication?

**Anand**: [05:52] Okay, so one person thinks it's good at multiplication, zero people think it's bad at multiplication...

**Audience Member**: [05:59] We don't know!

**Anand**: [06:01] We don't know. **"We don't know" is a great place to be, because then you can start checking,** which is what I did.

**Anand**: [06:08] It turns out that some of the models—some of the reasonably good models, like GPT-4.5 Preview—when you asked it a question like 1,234,567 multiplied by 8,901,234, and asked for the answer, that number is wrong. Every single one of those numbers is wrong. But if you ask it for a six-digit multiplication—123,456 times 789,012, and a whole bunch of others—every single one of those is right. So it's almost like it has the mental ability to multiply six-digit numbers.

**Anand**: [06:45] But the earlier models were worse. If I took Gemini 1.5 Flash, it could go as far as—five-digit numbers was all it was able to multiply. The newer models are on top, and they seem to be able to... Today, for instance, Claude Opus 4.8—which isn't the latest model, 5.5 is the latest—can quite comfortably multiply nine-digit numbers in its head, and probably much more; I just stopped at nine digits.

**Anand**: [07:18] Clearly, **even something as basic as multiplication, which your calculator can do, your phone can do—you don't need a large language model to be able to do it—they mess up on.** And this may not be obvious. **The second thing is that they are getting better.** And unless I'm constantly watching it, what I knew last year is no longer true. Because they're improving so fast, we effectively need to keep up with their weirdness, and the shape of the weirdness is changing as well. It's almost like we're almost always on the back foot, right? **So what do we do? Be skeptical.**

**Anand**: [07:56] We could ask people for advice. But I would question advice as well. Let's check something. I've been given advice on various ways in which we can tell models to be more accurate. Some people have told me, "Look, shame them. Just tell it: 'Even my five-year-old can do this. You can do better than that.'" Or praise it: "Really well done. I'll really appreciate your help on this." Or reasoning: "Think step-by-step." Or be polite: "If it's not too much trouble, could you please..." whatever. Or: "This is your last chance. You'd better get it right." And different people have told me in various conversations, "Try this, it really works."

**Anand**: [08:40] Okay, let's do a quick poll. How many of you think shaming helps? Okay, one. How many of you think praise helps? Okay, that's a reasonable number, about half a dozen, more than that, maybe eight or nine. How many people think reasoning helps? Okay, that's about 80% of the audience. That's a lot of people. How many think politeness helps? No one thinks politeness helps? Wow, okay. Fear: how many people think fear helps? Okay, yeah, not that many hands.

**Anand**: [09:16] But of these—and you were right as an audience—**the only one that helps is reasoning. Nothing else helps, and this helps consistently.**

**Anand**: [09:25] How do I know that? Because I benchmarked it. I took a whole bunch of these and asked the question to various models. So I said, "Amazon Nova Lite, if I ask you to be an expert, if I ask you to be curious, if I bullied you, if I shamed you," whatever, "in each of these cases, is it doing better or worse?" and checked what the result was.

**Anand**: [09:46] It turns out that reasoning is the only one where there is a consistent improvement. If you ask it with a strong emotion, like, "Oh dear, I'm totally overwhelmed. I really need your help right now," and all of that, many of the models panic. Shaming doesn't seem to work either. Politeness doesn't really help that much, praise doesn't help that much, fear doesn't help that much, and the others don't help—they're neutral.

**Anand**: [10:16] Now, this may change. Keep in mind that every model is different. As the models evolve and new models come in, this advice may be different. Maybe it's different for different kinds of questions. **The point is, you've got to question the advice. You don't really know if something is valid in your context.** I'm not saying don't use the advice. Sometimes you don't have time; you've got to just trust somebody and run with it, which is fine. But know that you're not doing it because it's right; you're doing it because you don't have time or it's not so important. That's okay, just don't fool yourself that people really understand AI. Somebody standing out here who's done a whole bunch of experiments telling you stuff: I don't really know AI, you don't know AI, AI doesn't know AI. **Test it out, and if it works, great. If it continues working, great. Nothing more than that.**

**Anand**: [11:12] This can apply in so many areas. How many of you have heard of the mathematician George Pólya? Okay, no? Famous Russian mathematician [Hungarian-American], and he had given a whole bunch of advice on how to solve mathematical problems. Some of the things that he suggested were, for instance, advice like "work backwards." He said, for instance, start from the desired answer and reason step-by-step backwards to the original information. Or sometimes he would say, use the pigeonhole principle: identify objects and containers; if there are more objects than containers, then there will be something that's left out, so that's a useful way to prove theorems.

**Anand**: [12:03] This has been useful advice for mathematics students for many decades. People have been following this blindly. Does it actually work? Now we have a systematic way of testing it. What we can do is give students—but even more simply, large language models—the same advice. Give them a whole bunch of algebra problems, give them a whole bunch of counting problems, geometry problems, etc., and ask: does his advice on symmetry work for this kind of a problem? Does his suggestion on using a simpler case or contradiction work?

**Anand**: [12:37] It turns out that the answer is different in each cell. The point is not whether there is something that works universally. There are some that seem to work really well. There are some fields, like number theory, where it doesn't matter what advice you take—almost doesn't matter, except external element. So there is one piece of Pólya's advice that works really well here. Good to know. And there are subjects like pre-algebra or counting where it doesn't matter what advice you take, most of them seem to work.

**Anand**: [13:07] **In other words, advice is now verifiable. Advice is quantifiably verifiable.** And once you start shifting into that mindset and say, "Experiments cost me very little because I'm going to have some model run it," then **the whole notion of how you respond to or take advice changes dramatically.** Right?

**Anand**: [13:32] Here's another one that I was playing around with. Andrew Carr on Twitter gave this piece of advice. He said, "Look, I don't really understand most of what LLMs are saying." Doesn't matter, I'm not able to access Twitter. But he therefore said, "What I do is add this little prompt to all of my prompts, which is: 'Only report to me in ASD-STE100 Simplified Technical English.'" And it doesn't matter what the standard is. What I do sometimes is: "Give it to me in the same language the UK government uses." That's really nice, simplified English. There's another simple standard for English; there's an ISO standard for English. All of these tend to make the model write in far simpler terms, which I find much easier to understand. Even if it's an area of my expertise, I just like simpler writing.

**Anand**: [14:29] So I said, "Wait, this sounds like good advice. I should be doing this all the time, right?" Except: question advice. So I did. And the next experiment that I ran was: does it actually improve or worsen the answer, or at least keep the answer the same? I'm okay if it keeps the answer the same. But what happened was, when I tested it on a whole bunch of questions—each row is one experiment—every green is where simple thinking improved the answer, and every red is where simple thinking worsened the quality of the answer.

**Anand**: [15:04] **Simple writing hurts thinking.** Which means that there is an easy solution: **what you can do is tell it to think however you want—don't tell it to write simple and all that, just get the job done—and then explain it to me in simple terms.** It's got the answer, so we just break it into two steps, right? We can still follow advice, we just have better evidence on how to follow that advice. Question, measure, check all of these things. It's relatively easy these days.

**Anand**: [15:39] And the good part is, AI is making verification easy. You may say, "Wait, hold on, AI can't be trusted, right? I mean, that's half of what you're saying. It hallucinates, it can't even multiply, and so on." True, right? Except, **that's the beauty of verification. An additional verification costs you very little.** Supposing somebody says, "Oh, I don't trust it." Say, "Okay, let me check." Somebody says, "Here's a specific mistake." Check! Maybe it made a mistake in spotting the mistake, but you can check. All it's doing is giving you places to look. And if 20 people give you 20 places to look, as long as you have time and it's important enough, you don't lose anything. And that's the power of verification.

**Anand**: [16:23] One of the things that we tried was: how do we deal with hallucinations? We had different models take chat messages, like somebody sent a chat message saying, "Take a quick look at my invoice," or "Help with adding some items," "When will I receive my order?" Now, we know which bucket these have to be classified under. So we check which models are able to classify them well. Some models do a pretty bad job. An early version of Gemma, which is a tiny Google model, seemed to have the lowest pass rate. It was only correct 57% of the time. Some of the earlier Anthropic models: 87%, pretty good. GPT-4.1, which had just about been released, was 94% right. But it still got some of these wrong. For "When will I receive my order?", the expected output is "delivery period," but it actually put it under the "track order" bucket.

**Anand**: [17:21] At some point, I started thinking, "Hold on, if all of these models are getting this wrong, did I get it right in the first place? Meaning, did I put it in the correct bucket? Do experts always agree? Are experts always correct?" I don't know, but if we assume that experts are correct and we still want to get as close to 100% accuracy—but even the best model was only giving us 94%—is there a way of improving the process?

**Anand**: [17:48] The next thing that we checked was: do these models correlate with each other? Do they make the same kinds of mistakes? When we paired models, what we found was yellows are where the models are making the same kind of mistakes. And the same model makes the same kind of mistakes; that's obvious. But the models don't always agree with each other, and that's useful! **So if someone gets it wrong, another model is not likely to get it wrong the same way. They're likely to make different mistakes. And that can be leveraged pretty powerfully, because all you need to do is have another model double-check it.**

**Anand**: [18:22] It turns out that the error rate... I said, "Look, I'm going to pick a random model. Close my eyes, pick one model. What's my average error rate?" If it was the best model, it was 94%—if it was the worst model, it was 57% accuracy. The error rate on average was about 14% if I pick one model at random. If I said, **"Let's take two models and double-check: if both of them agree, only then I'm going to take it forward," the error rate falls to 3.7%.** That's pretty good! Which means that now I have a better accuracy than the best model. Even the best model at 94% had a 6% error rate. This is just 3.7%.

**Anand**: [19:04] But when the models disagree, I have some manual work to do. I have to check. That happened about 12.6% of the time. That isn't too bad. What that means is—what I'm saying is, look: AI can't do all the work. It can probably do seven-eighths of the work, and the rest you've still got to check manually. But what it does, it's going to do with just a 3.7% error rate.

**Anand**: [19:34] Now you can take this forward. What if I had three models? Triple-check, quadruple-check, quintuple-check. You can't get it to zero, it tapers off, but we were able to get it to 0.7%, and the manual checking ended up being about 28%—about a quarter. So think about it: somebody comes and says, **"I can give it to you at 99.3% accuracy, but I can't reduce 100% of your workload. I can only reduce 72% of your workload." I'll take it!** That's not a bad deal at all, right? Especially when you know that this one particular stream is really accurate. You can just take the people away from it.

**Anand**: [20:13] And we'll come back to this point in a short while, which is the whole notion of being confident of the accuracy. It's one thing to say here's what it's classified something as and it's 90% accurate; it's even better to know which part is 90% accurate and which part is the 10% where it's not so sure about, so that way you can just focus the human effort on the part that's less sure. We'll come back to that. But **double-checking makes this a very powerful attribute, and if multiple models are able to agree on something, there's a good chance you've got it right.**

**Anand**: [20:54] That brings us to calibrating confidence. When we ask a model a question, how often is it right in its own knowledge? Specifically, let's do a quick poll: when an LLM says it's 95% confident, how often is it actually correct? How many people think when it says 95%, it's probably 99% or more correct, meaning it underestimates its confidence? Okay, no one. How many people think it's probably 95 to 99%? No one. How many think it's 90 to 95%? Okay, that's about 40% of the audience. How many think it's only 80 to 90%? Okay, that's about 15% of the audience. Just 50 to 80% accurate? Okay, nobody thinks it's that bad.

**Anand**: [21:47] Our collective perspective is that it tends to be a little overconfident, not too overconfident—not a disaster. Okay, we can measure this, right? And we can measure this against various kinds of problems. So that's what I did. And the answer changes from model to model. So let me just take one of the recent models: GPT-5.6 Luna. When it says it's—let's see, stated confidence of... yeah, okay. **If it says it's between 95 to 97% correct, it's probably about 70% right in reality.** That's for this model. And at 90 to 94%, it's more or less the same; it's about 70% right.

**Anand**: [22:42] The curve here is: the x-axis is what it says; the y-axis is what it actually is across several attempts. The diagonal line means perfectly calibrated: if it says 50%, it's 50%. Bottom-right is overconfident; top-left is underconfident. They are overconfident, clearly, for this class of problems.

**Anand**: [23:09] Different models have different levels of overconfidence. Nano behaves in a very weird way. There is actually a small segment where it says 90 to 94%—now, I don't know if it's just because I haven't run this experiment long enough—but it seems to be slightly underconfident there. It was in fact right on 10% of the requests with no mistakes at all. This could be a statistical anomaly; eventually maybe the curve will look different. But **the point is that every model has a curve, and you can measure that curve, which means that you can create a queue.** Saying, "Look, I'm going to ask the model for an answer. I'm also going to ask it how confident it is, and I'm going to translate that confidence into a real number—meaning the real confidence with which I can either send it to a client or hold it back and have somebody recheck."

**Anand**: [24:04] The good part is, the order is pretty consistent. Where a model says it's more confident, it usually is more confident. Where it says it's less confident, it usually is less confident. So you could just start at the bottom of the queue and say, "Look, you say 50%, maybe you're only 10%. I don't care. I'll start with the bottom, where you're least confident, and keep moving up the chain."

**Anand**: [24:26] There are other ways of calibrating the confidence. Sometimes you do need to tell a client, "Look, I am 80% sure about this," because the model said 80% sure, right? In such cases, we can use prompts. And here's what I did: I went to ChatGPT and said, "Look, I want you to try out a whole bunch of different prompts and tell me which prompt can actually make the model do a better job."

**Anand**: [24:54] The premise here is that when experimenting and I'm coming out with a benchmark, there is no such thing as wrong. I've got numbers to prove it, right? So it could have randomly concocted a prompt like that shaming thing: "Even my five-year-old can do it. Can't you get the percentage right?" And if it worked in this case, great! It works. Here is a model and here's a problem for which that solution works.

**Anand**: [25:20] It suggested four of these. One of them, it's roughly like: "Look, it's completely okay to be uncertain. Don't be confident just because you feel like you have to be." Or: "Look, what is a competing alternative classification? What's a different label that you might want to give? Think about that," and so on, explains a bit more. A third one: "Think of the two most plausible labels and allocate the probabilities." So you could say, for instance, the first one I'm 80% confident, second one is 10% confident, and the rest is 10%, and so on.

**Anand**: [25:54] For each of these additional prompts, we looked at the calibration curves. The blue out here is the default, and that's the overconfident one. Most of the others are clearly better; they're closer to the diagonal. Adding almost any of these prompts certainly seems to improve things. And if you ask me, maybe this particular prompt—"top two probability"—is, at least for most of the values, a better one. The top two probability prompt—which you'll see on the top right here—was the one on the right extreme: "Pick the two most plausible alternatives, distribute the probabilities amongst those, and then give me the result."

**Anand**: [26:37] Why does this work? I don't know. Is this the best? Almost certainly not, because I'm sure with a few more iterations we can come up with something. But **the theme here is: once you are able to benchmark, it becomes easier to continuously improve, because you have something to measure.** Then you can try out experiments which cost very little, and see if that improves, if that improves, if that improves. And this is exactly how the AI companies are able to improve their models.

**Anand**: [27:08] In fact, they are specifically able to improve their models better and faster in fields where you can verify. **Why is AI so good at software today? Because when a program doesn't run, it just doesn't run. It's so easy to verify it.** Why are they producing so many new mathematical proofs, which you may have seen about in the press? That's because in mathematics, you either prove it or disprove it; it's right and wrong. And increasingly, the sciences are getting crowded that way: there's a whole bunch of biology experiments that are being run, a whole bunch of physics experiments that are being run. They're slightly more expensive to verify than software or mathematics, but not overtly so; they are verifiable.

**Anand**: [27:48] But it's really hard to verify whether, I don't know, is coffee better than tea? When it becomes subjective. Or when somebody says, "When will I get my order?", is that the delivery period queue, or is that some other queue? In some of those where there is ambiguity, the improvements become a little trickier. **So if you can create a benchmark, and you can use that benchmark to tune your results, you can continuously improve. That's obviously pretty powerful.**

**Anand**: [28:23] There is another way in which we can improve models, and to explain that, I'm going to tell you a bit about how LLMs work. Many of you may know this; this is fairly well known. But **LLMs are next-token generators. In other words, they take all the text, they hear you, and then they construct the next word, and then the next word, and then the next word. It's roughly the equivalent of speaking as you're thinking.** Which is fair—I mean, we all speak as we think. But the important thing therefore is to realize that it hasn't thought through all the way to the end before it gets to the end.

**Anand**: [29:01] Specifically, the way it decides is... let me see if I can get to the app. I am not connected. Wow, this makes it a bit unfortunate, but hopefully I should be able to connect. Get onto the Wi-Fi... and yes, I am connected. Let me open the app. Fingers crossed. What we're going to do is have it actually generate text and look at the mechanism by which it generates text. While this page loads... Okay, page loading very slowly. That's okay. I can have it load in a different window, and stop this loading. I'll just show you an example that I've already concocted, if I can find it. Yeah, no, it's okay.

**Anand**: [30:05] Right, so here's a question: "In what episode of *Friends* did Joey eat too many marshmallows?" Now, what it does is starts by answering with the word "Joe". Now, you'd say, "Wait, hold on, 'Joey' is a word; 'Joe' is not a word." Well, it uses a different language, and the words are called tokens, and roughly in its language, "Joe" is a word and "y" is a different word, so it just strings them together. That's fine.

**Anand**: [30:36] It thought that there's a 70% chance that I should say "Joe". But there was a 28% chance where it thought, "Maybe I should begin with 'In'—in this episode." There was a 1.7% chance it thought, "I could begin with 'The'—the episode that..." whatever. And at this point, it has to make a choice. And **every model makes a choice at every word that it's generating.** I'm going to use the word "token," which is what I really mean, but I'm going to say word.

**Anand**: [31:10] In this case, it happened to make the choice "Joe". But it could have made any of these with these probabilities. Now, how widespread or how randomly it picks is based on something that you can control, called the temperature of the model. High temperature: very random. Low temperature: not so random. Earlier, OpenAI, Anthropic, etc., they used to let you control the temperature. Now they figured, "Look, that's too much work." They decide it for you and they just give you the result. But behind the scenes, this is how it's working.

**Anand**: [31:48] Once it's decided to say "Joe", it has absolutely no doubt that the next word that it's going to say is "y". It thought, "Okay, maybe I could have just said 'ey'." And then "Joel" was a small, tiny chance. And there was an even tinier chance that it thought, "Maybe I should just stop speaking now." Why, I don't know. And "eJ", I don't know where that came from, there's an even tinier chance. But all of these are fleeting thoughts that it instantly discards. It said, "There's almost no way I'm going to say any of the other things. I'm going to say Joey."

**Anand**: [32:22] And then "eating", "ate", "eats", "Trib"—Joey Tribbiani, fair enough—"Joey's"—all of these were possibilities that it considered, saying, "Yeah, I'm going to go this way." So you're getting a sense of how it's deciding, right? And once it's chosen "eating", there was no doubt: "too many marshmallows"—marsh-mallows. And here, it wasn't sure: "too many marshmallows is," "too many marshmallows happens to be," "happened to be," "was," "occurs," "occurred in"—many possibilities.

**Anand**: [32:57] **Which gives us a way by which we can figure out where the model is uncertain.** There are multiple paths, and the reds are where it's uncertain. So let's look at Season 3—that's a factual statement. And it's saying, maybe it could have been Season 7, too. Maybe it could have been Season 5; maybe it could have been Season 2. Lower chances, but I mean, there's only one-tenth as much of a chance that it could have been Season 7. But if we wanted to be really sure, that's what we'd double-check. Within Season 3, it wasn't too sure about Episode 20. Maybe it could have been Episode 21, could have been Episode 11, could have been Episode 13, and that's what you can double-check.

**Anand**: [33:42] Which means that we have some means of investigating a model's thoughts. **These are called logprobs—the logarithm of the probability—but effectively, logprobs is just a term that says at this particular word, here's how confident I am or here's how uncertain I am.** And you can approximately take an average—a geometric mean of this—and say this model has this level of confidence for that entire statement. For a different statement, it has a different level of confidence. And when running those classifications, we could have calculated those logprobs and checked: how good are the logprobs? Which I did.

**Anand**: [34:21] The interesting thing about the logprobs is the numbers themselves aren't great. That is... where did this go? Yeah. So when the logprobs report a probability of 99.9%, it's only 56% correct. So the number itself is useless! But what happens if you just sort it and say, "I'm going to take the worst logprobs and assume that that's the worst, the next is the next worst," etc.? **It turns out that in that case, the error rates are much better.**

**Anand**: [35:07] The brown is how much... Supposing—I'm just going to talk through this. If you said, "Look, I want to use as little budget as possible, and I want to make sure that as many errors are caught," then I have two choices: I could ask the model, "How good are you?" and use that information, or I could compute the logprobs and use that information. And it turns out that using the logprobs is actually slightly better. **Don't take the number for what it is; just sort by the logprobs and go down the queue, and that gives you a better result.**

**Anand**: [35:42] Okay, what does this mean? A couple of things: firstly, there are ways in which you can interrogate a model to find out how confident it is. You can just ask it. You can ask it in a better way. You can continuously improve the way in which you ask it, and you will be able to get to a number. There are ways of interrogating a model without asking it, and that's computing some of the additional information that it's generating, which an IT team will be able to get from the model, and it turns out that that's even better.

**Anand**: [36:13] What does that mean? It means that **models aren't as self-aware as we think. We can, by placing probes into their brains, get better information about them than if we just ask them.** But we could also ask them, and both of these are signals by which we can calibrate the confidence.

**Anand**: [36:35] This leads us to another theme, which is: so if we're doing this, then some models are better than others at some tasks, etc. How do we go about benchmarking it? What do we benchmark? I think every single decision needs to be benchmarked, and perhaps the most important decision to benchmark is: what model should I use?

**Anand**: [36:58] The reason this is a particularly important benchmark is this particular chart. In May '23, I started by plotting—a little hard to read, but I'm just going to talk you through it—I plotted model intelligence on the y-axis and model cost on the x-axis. Let's fast-forward to today. These are all the models that exist as of last month. And if they are on the right side, they're expensive. Left is cheap. Bottom is not very smart; top is pretty smart.

**Anand**: [37:41] How smart are we talking about? In March '23, we had three models which roughly had the intelligence of a high school student. The kinds of answers that they would provide were very similar, and they would cost... Claude was among the more expensive ones; it cost about $8 per million tokens. What does that mean? If you gave Claude about a million words—how big is a million words? Think all the Harry Potters put together is a million words; King James Bible, that's a million words. So if you said, "Look, read all of this and give me a one-sentence summary," that would have cost $8 with Claude. But with GPT-3.5 Turbo, it would have only cost you 50 cents. $8, 50 cents—big spread, right? But roughly the same level of intelligence.

**Anand**: [38:37] That changed. One of the big leaps that happened was Claude 3 Haiku. Now, you want stuff that's on the top left: cheap, but smart. Claude 3 Haiku was a bit above the cut. What this was able to do was at 25 cents per million tokens—meaning give it a King James Bible, say, "Yeah, just here, 25 cents, I'll give you a good answer"—and it was at the level of intelligence of a college junior. That's a pretty good one. And there were, of course, more expensive models like Claude Opus, which would have charged you $15, almost 100 times more, and been only slightly smarter. But sometimes you need that smartness. Fine, go with it.

**Anand**: [39:26] Over time, you can see that the horizon gently progresses—sorry, "gently" is the wrong word, this is rapidly progressing. Another big leap that happened was with DeepSeek-V3. It doesn't look like it's a big leap here, but it actually was a substantial leap, and people panicked about how this kind of new training was possible. Part of the reason for the panic was the cost of building this model was remarkably lower than other models. Another reasonably big leap came with Gemini 2.5 Flash Preview, okay, and the Pro Preview version as well.

**Anand**: [40:08] Yeah, the Gemma models, these are interesting. Google released a couple of models called Gemma; they run on my phone, they run on your phone. The application to download is Edge Gallery. So when I'm on a flight, I take a picture of the meal that the hostess serves, and I'm a little too embarrassed to ask if it's vegetarian, so I ask Edge Gallery instead: "Is this vegetarian?" It says, "Look, almost all of them are. That little thing is chicken, just place that aside." Okay, yeah, it works! No, it's practical, right? I mean, if I had ChatGPT and an internet connection, yeah, sure, but in the absence of that, that works.

**Anand**: [40:47] This also works in emergency rooms, where you can't take any external connection, right? Just take a picture and say, "Wait, am I cutting the heart or the liver?" Obviously better questions than that! But there are places where you need edge models. And here's the thing: **this is about as smart as a PhD candidate. Ridiculously smart.**

**Anand**: [41:12] Now, is that... well, I've spoken to a number of PhD candidates and you'd ask, "Well, how smart are they?" Well, it depends! But a number of questions that I would expect a PhD candidate to be able to answer, it does answer. I wouldn't say that it has a lot of common sense; that's a different story. For common sense, we'll have to go even higher. And as of now, some of these models, like GLM-5.3 Flash—this was as of last month, there have been even better models—it's like taking the frontier to something remarkable. And the frontier is now beyond that of a tenured professor.

**Anand**: [41:49] I can ask these models questions that I have no basis for even validating. How do I even know that it's right? I sent it all of my tax returns, and it came back and said, "Anand, you have two problems: in your India tax return, you are due a refund of 14 lakh rupees, which your auditor missed." Okay, that is good news! "And the Singapore government is double-taxing you." Whoa, what? Seriously, both of these actually happened. There was some entry which our auditors in Singapore had made once again. And it went through all of my bank statements, it went through all of my tax records by opening the browser and going to the respective sites and so on, and it saved me, well, almost $100,000.

**Anand**: [42:41] And I have zero basis for understanding tax in any country. I don't even tally my bank accounts! So when it says something, how do I even know that it's right? Remember I said question advice, right? Yeah, except these things are just getting smarter and smarter and smarter. Okay, if I could run a benchmark, if I could run 100 audits... but I'm not an auditor. How do I test some stuff against the real world?

**Anand**: [43:11] So here we have to rely on others who are doing the benchmarking. And there are several organizations that do a benchmark. One that I particularly like is OpenAI's own benchmark. The reason I trust them is because on many occasions they've said Claude is better than GPT. Okay, fine, you're probably honest!

**Anand**: [43:36] What they did was looked last year—this is a year old—at different parts of the US economy. Each of these boxes represents one profession: software developers, lawyers, financial managers, etc., and asked: **where are models better than experts?** They took the same task—and to give you an example of a task given to a general and operations manager, it was: "You are a retail manager at a bridal store and you need to teach your entire bridal sales team how to overcome objections and hesitations, and you're supposed to create a document that covers all of these blah blah blah," and asked it to actually generate a Word document. These were real tasks, meaning in the sense that they were created by professionals in the field who were rated very high, that AI and different professionals/experts did. And the experts evaluated which ones were doing better.

**Anand**: [44:32] Among the tasks given to general and operations managers, Claude was the model that did best and beat experts 67% of the time. Two-thirds of the time, you would go to Claude rather than an expert in that field. Accountants and auditors: only 24% that time. Financial managers were okay. Customer service representatives: 59% of the time, GPT-5—5, yeah, 5—was able to do a better job. And now we are at GPT-6; this number could only have increased. Software developers: don't even go near that, 70%. Sales managers: don't bother, 79%. Shipping, receiving, and inventory clerks...

**Anand**: [45:19] I'm not saying that I would treat this as the right answer, but I'd say, "Look, I don't have the ability to experiment, I don't have the ability to benchmark. Somebody has benchmarked it for me. It's a starting point." The simpler question now—at least more manageable question now—is: do I trust the person who's doing the benchmark? And if the answer is, "Yeah, kind of, at least in some of these spaces, yes," and then over time I get a sense of is this right, is this wrong, but this is a wealth of information.

**Anand**: [45:51] **So if you can create a benchmark, fantastic. If you can't, then find who's creating a benchmark and use it.**

**Anand**: [45:59] What I therefore realized was that because of this rapid change—and look at how it's changed: there was a time in March when the best model was about as good as a college junior, and then March '25, two years later, we have PhD candidates. And less than a year later, we have somebody who's smarter than a tenured professor. **In other words, in the course of about three years, models have become about 15 years smarter of human development.**

**Anand**: [46:35] We don't see this pace slowing down, and which is why a lot of people are saying artificial general intelligence, artificial superintelligence. I don't really know what that means; maybe some people do, most people don't. But I think what's clear is: **things we try today that don't work might start working tomorrow. It's good to keep checking.** Is this working today? Is this working tomorrow?

**Anand**: [47:02] I keep an impossibility list: things that I've tried that failed. On my impossibility list, for instance, a few months ago was: can it convert my parents' black-and-white wedding photo into color? And let's see, yeah. So this is the picture: here is the original, and here is the version that it created just last week.

**Anand**: [47:32] Until last week, this was on my impossibility list: "It's not going to get the job done correctly." Between this picture and this picture, can I spot a difference? I may be one of the only people in the world who can actually spot some subtle differences, like I know my mom wasn't smiling as much, nor was my father; they were both a little more serious. In fact, I went through this carefully, and the one theme that I could find was: everybody seems to be slightly happier than the original!

**Anand**: [48:10] Okay, we know the bias in that model! But luckily, this happens to be one of those few benchmarks that I'm reliably able to evaluate, and I'm one of the few people who can evaluate because, heck, it's my parents' wedding photo, right? So I know their faces better than anyone's.

**Anand**: [48:26] **So if you can find a benchmark that at a glance you say, "Yes, that's right," or "No, this is wrong," and it could be anything, you've got an edge. You can evaluate AI on at least some things.** But for most things, there isn't really much of a way that you can trust yourself to be able to evaluate it, other than to say, "I tried it, it didn't work. Maybe it's me, maybe it's the model, but we'll try again." And your list will keep shrinking. Try adding to that list, because that's when you will be on the frontier. And if you're not on the frontier, then AI can do most of the things that you're doing anyway. What are we there for?

**Anand**: [49:09] That takes us to the last thing that I wanted to talk about, which is: all of this is a problem because we are using models that are non-deterministic. They give different answers different times, sometimes they could be wrong, etc. But rules—at least they're deterministic. And if we change a rule, it stays where it is, and you can check how often a rule is right, how often a rule is wrong, and improve it. **The good part is, you can use AI to create and improve these rules. That's a pretty powerful way.**

**Anand**: [49:40] Effectively you're saying, "I want to do a certain classification, I want to compute a certain number, whatever. You probably already have rules for many of these things. Use AI to improve those rules." For example, one of the things I was curious about was: let's take student performance data. This is a dataset where for each student we have information about their family size, their mother's education, father's education, guardian, blah blah blah. And one of the things then that I asked it to do—let's just skip the analysis—I said, "Let me predict the grades." G3 is one of the grades. "And give it to me as a decision tree." So effectively I'm saying, "You give me a rule by which I can predict the student's grade."

**Anand**: [50:28] What it did was it went through all of that, it generated a set of rules—which I'll show you and walk you through in a second—but it's saying, "I can give you a rule that's 86% accurate." Wow, okay, that's pretty impressive! Student performance isn't supposed to be that easy to predict. Let's look at the rule. The rule says: "If grade 2 is less than 10.5..." Hold on! You're using one grade to predict another grade, which is kind of like saying, in your second exam if you got a certain score, then I can tell you what your score will be in the third exam. Okay, yeah, but I kind of want to know before I look at any of the grades, right?

**Anand**: [51:07] Okay, so let's do this then: I'm going to ask it, "Predict G3, but don't use any grade information, and now give me a decision tree." Thinking—it's just running ChatGPT behind the scenes. And now it says, "Oh, I can only give you 31% accuracy." Okay, how are you doing it? Okay, is the failures rate from previous years less than 50%? Then it looks at is this a boy or a girl, and oh, do they have a guardian—that seems to make a difference. Mother's job seems to matter, not the father's job, I don't know why. Absences matter. Well, it's kind of helpful, but 30% is not very good.

**Anand**: [51:48] What I'd do is: let's see if you can do better. "Can you convert new metrics? Take all of these, and maybe divide a couple of these, come up with additional metrics, and use those instead." And with the new information that you have—so it says, "Look, I've created the parents' educational average, total alcohol..." Okay. "Absences by age, grade improvement, family relationship, romantic interaction..." Okay, whatever it is!

**Anand**: [52:20] "So use all of this new information that you yourself have computed, and give me the G3 score—just don't make it too complicated a decision tree, just max depth of 3—without using grades, and run the analysis." Churning, thinking, redoing the analysis, and it's saying, "I can get you to 67% accuracy." Okay, for a quick assessment, that's not terribly bad. But it's saying that the most important thing is study efficiency. I don't know what exactly study efficiency is, I'll have to go back and check the metric, but that seems to matter. If their efficiency is low, then check how often they are absent. And the absenteeism—not just absenteeism, absenteeism by age. So older students allow a little more absenteeism, younger students allow a little less absenteeism—that seems to be a better predictor. And overall study time. If I look at this, travel time to study time seems to be a big factor.

**Anand**: [53:16] Okay, so this is useful information in two ways: one, I know what factors are important and therefore I can start making changes, not just predictions. The second thing that it helps me with is coming up with a rule that I know is about 67% accurate, and I can over time start improving this on a regular basis.

**Anand**: [53:37] **This is the premise based on which people just love AI writing code. Code is deterministic, mostly.** And therefore, what people say is, "I'll use AI, I'll have it write code, and use that code on a repeated basis. Doesn't cost me anything—no tokens used. Deterministic: when I run it again, it'll give me the same result. And I can use AI to improve it the next time. I'll have people check the result of it: if it's working well, great; if not, I'll have people making revisions and telling AI, 'Look, don't include grades, don't do this, don't do that, fix all of these,' and continuously improve."

**Anand**: [54:16] **This whole loop of running something and evaluating it using AI is a pretty powerful cycle.** But what you need is ultimately a certain degree of skepticism.

**Anand**: [54:35] What you want to do is:
* **When somebody gives you advice, question it.** It may be right, it may be wrong, but in your context, it might not work.
* **Verify it, and use AI to verify.** Verification with AI is largely harmless. It might cost you a little bit of money, it might cost you a little bit of time, but that's in your control. Beyond that, there's no danger because you're still holding the decision.
* **Calibrate the confidence.** You can ask it how confident it is; you can instrument it and find out how confident it is. And once you know how confident it is numerically even, that gives you a lot of edge because then you can decide what to accept, what not to accept.
* **Benchmark.** If possible, you run the benchmarks; if not possible, find out who you trust who's running the benchmarks, and keep checking.
* And **generate rules.** Create rules through AI. You can get rid of a lot of that non-determinism. AI is not a tool just meant to create the final output; it can be used to improve the process as well.

**Anand**: [55:35] In short, **with evidence, you will find that the amount of impact that you can create is much, much higher.** Do give it a shot, keep practicing, and you'll find that your impact will dramatically grow. Thank you.

*(Applause)*

**Host**: [55:56] Thank you very much, Anand, and to our partner Straive for this session. But we still have three minutes, so if you want to ask questions to Anand...

**Anand**: [56:07] Questions? Sure, please.

**Audience Member 1**: [56:10] So I noticed that the percentage on the medical field in the benchmark is much higher as opposed to some other industries.

**Anand**: [56:20] Yep.

**Audience Member 1**: [56:21] So does it mean to say that we did a lot of benchmark on the medical field because the margin of error should be less, because it's under the medical field? Is that a safe assumption?

**Anand**: [56:34] Absolutely. So the question is, given that the medical field is somewhat more important, people's lives are involved, should we benchmark more? Definitely, and that's a generalizable rule: **benchmark more where things are important; where it's less important, proportionally benchmark less.** Based on the degree of risk or based on the degree of impact, the level of care, skepticism, etc., that you need to treat will vary. So yeah, I would probably wait for this to get to 99% before I take an important decision. But if it was just asking about maybe, I don't know, what exercise should I do, then I'd probably say, "Yeah, 50% is good enough."

**Audience Member 1**: [57:11] *(Laughs)* In order to avoid going to the doctor!

**Anand**: [57:14] **I always verify with AI. Take the doctor's reports...**

**Audience Member 1**: [57:18] But their rate is much higher!

**Anand**: [57:20] Exactly, yeah, true. Double-check anyway. Yes, please?

**Audience Member 2**: [57:24] I have two quick questions. One, on the tool that you used to verify and define rules, is that available to the public?

**Anand**: [57:32] Straive has built the tool, and I think we're in the next room as a booth and we can probably show you more. But my advice to you is just ask ChatGPT, or Claude, or whatever your AI of preference is. And here's something you should try: you should say, "Build this for me. I went to this session, Anand was talking about all kinds of random stuff, this is what I roughly remember: build it for me." If it builds it, fantastic; if it can't, write it in your impossibility list: "This week, this is impossible." And ask it for ideas: what else can you do that solves the problem? Because increasingly I'm finding that when I hear somebody say, "Oh, this is not possible," or "Here is a way in which it should be done," that I'm not 100% okay with, or I can't access it immediately, AI might be able to solve the problem for me. And that's a source of problems—these days, problems are tougher to find than solutions.

**Audience Member 2**: [58:26] And the other one related to your tax returns, sorry—just curious, did you verify that result in another model?

**Anand**: [58:36] No, I didn't actually, because I was so happy that I just sent it straight to the auditor! Who said, "No, no, no, Anand, you don't get a 14 lakh refund because your bank account is a non-resident ordinary account, whereas it should have been a non-resident extraordinary [Non-Resident External / NRE] account." Okay... ChatGPT: "Here's the transcript. What on earth am I supposed to say?" And it said, "Look, point her to this particular High Court case, and that indicates that in Anushka Shetty versus—or Anushka somebody versus the High Court of... or the Income Tax Department of Mumbai, there is evidence that the account type—type of account—does not matter." So I said, "Look, copy-paste, send it to her." And she said, "Okay, I'm going to check with my senior." She checked with her senior, came back and said, "Yeah, it turns out that you're right." Yay, I'm a tax expert! She must be thinking I'm some kind of genius, right?

**Audience Member 2**: [59:28] That's just a good reminder again that, you know, if you're too excited, don't forget to verify!

**Anand**: [59:34] Yeah, true!

**Host**: [59:37] Wonderful session, Anand. That's a wrap for today. But our photographer is asking for one group photo with our speaker.

**Anand**: [59:49] I'll just go stand in the middle?

**Host**: [59:50] Yes.

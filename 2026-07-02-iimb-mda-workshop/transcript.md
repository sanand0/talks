# Transcript

**Prof. Shubhabrata Das**: [00:39] Good afternoon everybody. Hope you are all well. IIMB is proud to have Anand as an alumni, and the privilege of teaching one course. I think I did teach, or did I not? Not your batch? So that's why he became the gold medalist, okay? So anyway, I've been in touch with him for several years and impressed by what he has done. So I was very much there when he graduated in 2001 and to the best of my knowledge, certainly in all these years, he's the only person I know who was the **gold medalist in the academic rank and the all-rounder**. That is only one part of it. I think he did not work for it; it happened to be so because of who he is and it showed in what he worked. Subsequently, I'm sure you'll have much more fun in the session. Among other things, he has told you mobile phones and laptops—laptops are anyway allowed in my session—but he has also said mobile phones. So you'll have a lot more interaction and fun. I hope you'll also learn some things based on what you have already seen and I'll see you next week or the week after after the break. Good luck. Over to you Anand.

**Anand**: [02:08] This mic should be working. Can the people at the back tell me? No? Okay. If I speak louder, is it better? Or if I keep it closer to my mouth? No? Let me use this one. I've used this [handheld mic] many times, so that's actually easier to manage. Can you hear me now? Is this volume better? Am I kind of okay? Okay.

**Anand**: [04:15] **How many of you have used the `AI` function on Google Sheets?** (No hands are raised.) How many of you have used Google Sheets? (Several hands are raised.) Okay. I believe—and I may be wrong—but there is on `sheets.google.com` a pretty interesting function. I'm connected to my phone, which is slow. I couldn't figure out a way of connecting to the campus network, but it turns out that **there is an `=AI` function**. Let me make the screen a bit bigger so you can see it from the back. **`=AI()` and you can put in whatever you want there. This is actually a pretty fun function.** Any suggestions? What shall we try?

**Unsure**: [05:18] Generate a list of numbers.

**Anand**: [05:19] "Generate a list of numbers." Let's see what that generates. I put a hyphen. Now, it's turned purple, then it's generating, and it's gotten "-1, 2, 3, 4, 5." It treats lists as markdown, so "-1, -2, etc." which is still not a bad thing. Okay, what can we do now that is useful?

**Unsure**: [05:54] Instead of big formulas that are more complex, we can use this.

**Anand**: [05:58] Instead of big formulas, we can use this. Example?

**Unsure**: [06:01] So for example, let's say I have revenues of companies and I want to categorize them into buckets like small, medium, large. So rather than having if formulas, I can use this. This is just a small example, but for bigger scale formulas.

**Anand**: [06:16] Categorizing revenues of companies. That sounds like a good idea. Let's try that. Let us see if I can ask for a small public data set that has some details about company revenues or something, which I can pass to Google Sheets and then easily have it classify. Say I'm in the middle of a class and I want you to quickly come up with something that I can just either click and download publicly or you generate something and give it to me as a download. That way, I will upload it to Google Sheets and also tell me by the way how I should be demonstrating the use of the AI function on Google Sheets. **The advantage is classroom preparation for the educator becomes very easy.**

**Anand**: [07:11] **Our strategy is very simple: Make sure you can't use AI. Make sure we can use AI.** Our life becomes easy, and we like torturing you. No confusion about that, right? This is one session where you are encouraged to use AI. Beyond that is up to your course policy. But "encouraged" is not the right word—you *have* to in this session to get started.

**Anand**: [07:44] So it's saying it would create a small Google Sheets ready data set. In a few seconds, it will let me download it. I often wonder why I would not give you all a different case study every time rather than the same case study. If I give you all the same case study, you can copy. If I give each of you a slightly different case study, you will have a little bit more trouble copying. Except, of course, there's a strategy around that either way. **How would you effectively copy when each person gets a slightly different case study?** No thoughts? **I teach a course at IIT Madras where copying is allowed, by the way. Not just allowed, encouraged.** In fact, there are some assignments that you cannot do except by copying from each other. I'll be showing some of the details of this.

**Anand**: [08:44] But what I find amazing is that **AI can write programs**. I used to think that it can make mistakes, but it can write programs. Programs either run or don't run. If they don't run, fine, it will try again. **If they run, then at least it is going to be deterministic**. When I run it again, short of random number usage, it will give me the same output. So I don't really have as much of a worry about determinism and LLMs coming up with different answers every time as long as I tell it, "Give me a program," and then keep running the same program over and over again.

**Anand**: [09:18] But anyway, we will soon come back to the AI function. It seems to have created a sample sheet, and in a few seconds, it will let me download it. But the **AI function therefore can be used to classify all kinds of things**. The power of this comes when I start taking something like Apple, Orange, Jamaica, Trinidad, and Football. And I will create a formula: `=AI("categorize into fruit, country or sport", A1)`. And it eventually will come up with "Fruit." Good enough.

**Anand**: [10:14] The power of this comes when I can change the formula out here to concatenate and say `&A1`. Now, that gives me the same result, but if I drag this across, it runs it for each one of these cells and I get the answers. **Classification therefore has become a slightly easier problem.** I don't know if Excel has an equivalent of it. Maybe it does. Maybe some version of Excel has it. Excel Online probably has it. Even if it doesn't, all you have to do is upload it to ChatGPT and say, "Do this for me," and it will do it for you. **Classification of text has suddenly become a whole lot easier.**

**Anand**: [11:08] Let me download this data set. Here's a simple CSV. Now, let's do a small exercise. I will host this data set and I want you to classify and share the counts. 25 companies, not too many, so it shouldn't take too long. It's saying I can **classify the business model, classify the company type into SaaS, Marketplace, Services, Manufacturing, Consumer Brand, or Fintech**. Let's do that. I will make a change here, call it categories, and put in each of these categories. Except that these categories I will misname—I'm just putting them all for your reference. Let's save it. Now, this is called `companies.csv`. Let me upload this and then it will be over to you where I'll tell you the exercise that you could try out.

**Anand**: [12:35] The link will be `files.s-anand.net/pages/companies/companies.csv`. I'll write this in a much larger font so you can see it if it works. Yeah, that's working. So let me give you the link. Slightly hard to read but just type it in. **Your task is: download this list, put it into any AI that you want, and tell me how many companies are in each of those categories.** It's 2:40. I'm curious to see the time of the first response.

**Anand**: [13:47] Is there anyone who does not have a laptop and does not have a phone? Is there anyone without access to AI of any form? So we'll get an answer. Everyone has some AI. While you're doing this, I generally ramble a bit. This part is not important; you can focus on what you're doing. This is just to keep me entertained. But what I'm trying to do is figure out how different the results are. Each of you will be putting it into a different AI. **On the one hand, we suddenly seem to have discovered a capability to classify text.** Classification is something that you will probably be covering more for numerical content. But all of a sudden, there's a function that can classify text and actually do a whole lot more than just classify, but suddenly also classify text. If that's the case, then let's just get a little familiar with it. Which then starts begging the question: Once somebody gives me a survey, I can start classifying the surveys, go back and text as well, not just the numerical parts of it.

**Anand**: [15:08] I'll give it two minutes. Okay, each category is exactly 4 companies for each of the 6 categories? That would take the number of companies to 24. I believe that there are 24. Okay, that is one possibility. Any other responses? And which model, which AI?

**Unsure**: [15:30] Gemini Flash. Directly uploaded a CSV. Got you.

**Anand**: [15:35] Anyone else, irrespective of whether you get the same answer or a different answer? Same answer, same answer, same answer. Four same answers. Which model were you using?

**Unsure**: [15:51] ChatGPT. 5.5 Instant.

**Anand**: [15:56] And what is the distribution you are getting?

**Unsure**: [16:09] 5, 5, 5 and 3, 3, 3. Manufacturing, services, and consumer brand were 5. SaaS, marketplace, and fintech were 3. Total 24.

**Anand**: [16:21] Interesting. Okay, so 5-5-5 and 3-3-3 instead of 6 x 4, which is a clear difference. Anyone else getting any other results?

**Unsure**: [16:33] 6 classes and what is the distribution? It gave a distribution and the names of the classes are on the right side.

**Anand**: [16:43] What I would like is to take the 24 companies, figure out which of the classes each of those belong to, and count. And see if the numbers are matching because—yes, please?

**Unsure**: [16:55] 4, 3, 4, 4, 4, and 5.

**Anand**: [16:58] 4 each. Yes. Clearly, the majority seems to be 4 each. My guess is ChatGPT would have also created 4 each, but ChatGPT itself is saying, "I will sometimes classify this slightly differently." **This is something to keep in mind, which is that if you ask two people, they won't necessarily say the same thing.** Even if they were the ones who said it again. For humans, we call that lying, we call that loss of memory, we call that absent-mindedness. **For AI, we call it hallucination.** Not that much of a difference.

**Anand**: [17:34] But what this means is instead of you sitting and doing the classification on a survey that has 4,000 respondents—instead of you having an intern sit and do it or an assistant do it—once you get into your jobs, you can pass it to one of these models or you can pass it to the AI function, get the list, and it does the job. Now, question is, would you agree with that distribution or would you disagree with that distribution? So let us take yours. It is 5-5-5 and 3-3-3. Could you go through those and tell me—since we kind of know that it should be 4-4 across all of those—which are the three that it has misclassified and how? That would be a useful exercise because we also get a sense of the nature of misclassification.

**Anand**: [18:30] A second exercise: Could all of you please run it on a different model or at least a different chat and see if any of you are getting any different results? Either from yourself or from anyone else. The idea here is, if we ask multiple people, will they all consistently come up with the same answer or might they come up with slightly different answers? Once you have your second response, please let me know what you got. Same or different; both are okay.

**Unsure**: [19:03] Four classes on the basis of growth stage.

**Anand**: [19:13] I see. Okay. What we wanted to do was classify them on the basis of these six categories: SaaS, Marketplace, etc. So ideally, what I'd like is for it to tell you how many are SaaS, how many are marketplace, etc. Anyone got their second response yet? Same on the same model? GPT instead of Gemini Flash. Got you. Anyone got their second response? Same or different? If it's different, let me know. Same. Got you.

**Unsure**: [19:58] Different in Claude Sonnet versus Opus. What did we get as numbers? 5, 5, 4, 3, 4, 3. 5-5-4-3-4-3. This is on Sonnet? 5-5-3-4-4-3. Okay, got it. Whereas the earlier model was consistent right across. Which essentially means 5-5-4-4-3-3 is how it had distributed it.

**Anand**: [20:36] Okay. Now, were you able to figure out which of the three misclassified?

**Unsure**: [20:41] MetricNest, ClinicFlow, and Buildpulse. These three should have been SaaS, but the judge classified it originally to marketplace, services, and manufacturing. And now it's saying there was a mistake.

**Anand**: [21:04] Okay. And what did you prompt for it to say that it was a mistake?

**Unsure**: [21:07] I just said that another AI said something else and there should be four each. Try to find the misclassification.

**Anand**: [21:14] Got it. Which then kind of leads us to another technique. **That is, we are able to tell different agents—"You classify," "You classify," etc.—and then feed the results of one to the other and see if they say, "Okay, yeah, I change my mind."** Exactly what you would do to a team, right? The only difference is that is something you would have probably been learning in an HR class. Now, we're starting to have to learn this in a Multivariate Data Analysis class because the agents are getting a lot more powerful these days.

**Anand**: [21:55] Now, let's talk a little bit about the theory behind this, and then we'll go on to what we can do along these lines. So one of the experiments that I was trying was: **What does it take to improve the accuracy of LLMs?** At least consistency. We were taking messages like this—chat messages or emails sometimes. "When will I receive my order?" "Could you show me my order ETA?" "What do I need to do to register?" These are all actual chat messages that came to one of our logistics client's inbound service centers. And we knew what the classification of each of these is supposed to be.

**Anand**: [23:13] For example, when we classified with GPT-4.01 Mini for "When will I receive my order?", it classified it wrongly. The expected output is "Delivery Period." That is the queue that it should be sent to; that is the bucket it should have been classified as. It actually classified it as "Track Order." It got it wrong. But Gemini 2.5 also got it wrong. Nova-Lite, which is not such a great model generally, managed to get it right. So some models got it right, some models got it wrong. Some questions are easy; most of the models are getting these right. Some are harder; some models near the top are getting more correct, some models near the bottom are getting more wrong.

**Anand**: [24:00] There are some that every model is getting wrong. And interestingly, **every model is putting the chat "Help registering" into "Registration Problems" instead of "Create Account."** At this point, we went back to the client and said, "Look, every single model was putting it here. You seem to be saying something different. Are you sure about this?" "Absolutely. This is where I've been putting it right across." We went to a few others, including his boss. "What rubbish? Absolutely should be 'Registration Problems.' Why should it be 'Create Account?' He's saying 'Help registering.'"

**Anand**: [24:40] **After that, we learned something. Usually, when people say "classifying it correctly," they mean "classified the way I have been classifying it or I would classify it." It does not mean "classified correctly" because they could be wrong.** Our lesson therefore has been: When somebody gives you a task, a requirement, whatever...

---


**Anand**: [00:00] I checked with a few other people because it was such a requirement. Is the requirement correct in the first place, or are they making a mistake? Because otherwise, we'll be breaking our backs trying to solve the wrong problem—or at least, a problem in the wrong way.

**Anand**: [00:15] But this in itself is a signal: That **if all of the models are consistently getting it wrong, then there is a good chance that the classification is happening incorrectly at the source.** This is another possible signal. Who knows which of these is right, which of these is wrong, etc.

**Anand**: [00:30] But the interesting thing is that **the correlation between the errors is not particularly high**. What that means is that the kinds of mistakes one model makes are very different from the kinds of mistakes another model makes.

**Anand**: [00:46] How many of you know how to compute correlations? [Pause] Not enough. If you don't know how to compute correlations, the easiest is to go to Gemini or ChatGPT and say, "How do I calculate correlations in Excel?" Earlier, this would have been part of when *we* were studying—it was "how do you compute this in SPSS?" Today, it's an R function or an Excel function. Going forward, it will probably be "Ask ChatGPT," and it will give you the answer. But at the end of the game—and before that, it was computed using a certain algorithm, tabulated using a calculator, before that, using a slide rule.

**Anand**: [01:31] At every point, we had a series of tools that were helping us. The tools have moved forward, and **it's good to know the old tools, it's good to know the new tools. No harm in either of them.**

**Anand**: [01:43] But what the correlation basically is saying is: How similar are they? So, what we find, for instance, is the correlation between Llama 3 as a model versus Amazon Micro is probably in the order of 20%. Not a very high correlation. 80% of the time, they would anyway say different things. This is useful because then I can ask two models what they think, and if they give different answers, it's unlikely that *both* answers are wrong.

**Anand**: [02:18] I can ask three models, I can ask four models. All of them giving the same *wrong* answer is very unlikely. If they were all collaborating, colluding, the correlations are high—then okay, that's a different story.

**Anand**: [02:30] So, what we found, in fact, was for this particular case, it's easy enough to measure: **If randomly I ask any of the models, there is a 14% chance of error.** Now, I'm not differentiating between good models and bad models; some good models will give me 3–4% error. But a random model will still give me 14% error and 86% correct, which is not terrible, but not great.

**Anand**: [02:54] **If I ask two models and only take what both models agree on, that error rate falls to 3.7%.** If I take three models and all three agree, then only 2.2% error. If I take five models, 0.7%—meaning **99.3% sure that the result is correct**. That's pretty solid. That's as high as most agents get on their best days. But if they disagree, yes please?

**Unsure**: [03:24] For an even number, like two and four, do you take it only when they all agree? What happens when they disagree?

**Anand**: [03:32] I send it to an agent. A human—a human agent. Not an AI agent. And then say, "Look, these two agents are disagreeing. You've been doing this for donkey's years. What do you think is the answer?"

**Unsure**: [03:44] But that will be classified as incorrect.

**Anand**: [03:45] The agent will be—one of the agents would have to be correct. There is still a chance that both agents agree on the same thing and it still passes as incorrect, but that is only 3.7%, and I can keep changing that. **But that means the manual work goes down.**

**Anand**: [04:02] So, we calculated how much it goes up by. Turns out that if two agents disagree, that happens only about 12% of the time. Five agents disagreeing even once happens about 28% of the time. Which means that **my call center workforce of 100 people can become 28 people, and I still have 99.3% accuracy**. I'll take it. Makes sense.

**Anand**: [04:29] This is one of the ways in which we find we are able to reduce the—effectively **improve the hallucination or reduce the hallucination risk**, and therefore that is proving to be less of a problem.

**Anand**: [04:43] Quick recap so far. I just dived straight into doing without telling you what I'm going to cover—I actually don't know what I'm going to cover; we'll play it as we go along. But what we're finding is that **classification of text is easier than we thought**. It isn't always deterministic, but we know how to deal with indeterminism somewhat. It is no different from how we deal with people's indeterminism. People also give different answers, and management knows how to solve this for centuries.

**Anand**: [05:17] Put another way, **some of the principles that we are learning in human management apply to AI as well**. Something to keep at the back of your head.

**Anand**: [05:25] How can we use this in practice? How *I'm* using it in practice. I took all of my Google searches, at least until last year, starting from January 2021. And I put it into a similar sheet like this, put an `=AI`, and asked the question: **"What am I searching for, and how is that trending?"**

**Anand**: [05:48] And this is my result. **My number one search category is Indian celebrities and directors.** So, yeah, you know what I'm interested in. And this has been slightly trending downwards over time. JavaScript and DOM libraries—the length of the bar is how much I've searched for it across four years, and the color indicates whether it's growing or shrinking.

**Anand**: [06:12] JavaScript and DOM—I've been doing a lot of programming, but with the advent of AI, I have had to program a lot less. It is doing a lot of the programming, and that has steadily shrunk. I moved to Singapore; that was growing a lot—Singapore local info. OpenAI and AI-related research—a category that you can see the visible growth in. The JavaScript and DOM had the biggest shrinkage, but Python programming, Node.js programming, all kinds of programming started declining. **AI models and ChatGPT in green is increasing. APIs and tokens is increasing.**

**Anand**: [06:49] Put another way, **I was able to get a mirror into myself**. In this case, I had implicitly gathered survey data about myself by looking at my Google Search history. How does one do that? **How can you get your Google Search history?**

**Unsure**: [07:02] My Activity on Google.

**Anand**: [07:05] Exactly. Google offers a service called **Google Takeout**. You can go there and say, "Download my almost anything." One of them is my search history. And it will tell you on this particular date you searched for this particular word and a few other things. Which you upload to ChatGPT or what—I'm going to use ChatGPT as a broad synonym for any AI agent—and it will do the analysis for you and get you the result.

**Anand**: [07:28] Now, you could do this for anybody, including your customers. So when you have your customers' transactions or purchases, you could say, "Upload all of these purchases. Tell me what are the categories, what are the trends of those categories for every single customer or for any category of customers." Are Chennai customers buying slightly differently compared to Bangalore customers compared to US customers? Online purchases, offline purchases, bank statements, card transactions. If you are working on any UPI-based system, take all of that, put it in.

**Anand**: [08:02] At this point, you realize that **what we are able to get is a new column—a very powerful new column or powerful set of new columns**. Why is this powerful? Because largely for the last 40–50 years, people have not been analyzing text, but we have lots of text. So anything that we can do with it is likely to be new and therefore insightful.

**Anand**: [08:23] Secondly, the kinds of things that we can get out of it—it's pretty flexible. We can choose any kind of categorization. And therefore, with one column, we can say, "I want to find out the type of purchase. I want to find out whether this is a high-value purchase or low-value purchase." We can start creating our own theories and start testing them fairly rapidly. That is one of the ways I was using it.

**Anand**: [08:47] Let me share another example. One of our clients is a waste management client. And what—let me share what exactly we did for them. What one of my colleagues did... yeah. He took all of their invoice lines. I'm trying to see if—yeah, okay, this is probably the best one. Invoice line categorization.

**Anand**: [09:27] Right. They have a whole bunch of source systems—three ERP systems, a couple of legacy billing systems, and so on. All of this data is going into a Snowflake database. Some database. Now, as part of this, there are invoice lines—invoice line items—and somebody is sitting and categorizing each of these line items into a whole bunch of buckets.

**Anand**: [09:52] What this solution that my colleague Manoj built was—it effectively took a function called AI Classify within Cortex. **Cortex is the AI that is sitting inside the Snowflake database, just like the AI function in Google Sheets that we just saw.** And he applied almost exactly the same thing and said, "Categorize it this way."

**Anand**: [10:13] What he found was interesting. That **the classification of whether the invoice line item was a standard service or an emergency or a spot or one-time was more than 90% accurate**. Now, this 90% accuracy is about as accurate as the people that are classifying it. So, lead time is reduced. The effort of all of these people is reduced. This is a solution he straightaway put into production, saying, "Look, I'm giving you an extra column. You don't want to use it, don't use it. It is there for free."

**Anand**: [10:45] And this is the kind of change that people are able to bring into an organization. Initially, he had proposed... okay, whatever. So those were a couple of examples of how one goes about using classification.

**Anand**: [11:03] This is time for me to break into a small survey. Which, for some reason, does not seem to appear. Ha. So, here's a request. **Scan this QR code.** Does anyone have... okay. For those of you who are on a laptop, you can go to—I'll tell you the link. Hold on. `forms.s-anand.net`. That's the link. And for those of you who have a QR code, you can just fill it on mobile.

**Anand**: [11:42] I'll walk you through the questions in a few minutes. The reason we are going to do this survey is twofold—actually threefold. **Number one, the survey itself will tell you and me a few things, both about using AI in survey analysis and data analysis.** Second, this survey will be analyzed by AI now. We will live see what we can do with survey data and apply some of the techniques that you will be learning as part of this class. The third I will tell you at the end.

**Anand**: [12:19] Is there anyone who's not been able to scan or not been able to visit the page? If so, please raise your hands. You will need to log in with your Google account—any Google account. Doesn't have to be Gmail; could be literally anything. And once you log in, there are probably less than a dozen questions. Couple of questions you'll have to type; most of the others you can just click.

**Anand**: [12:47] Since I'm not seeing many more phones, I will switch to the form itself. And some of you may have questions on the questions, so I'll clarify. Question 1... okay, 13 of you have already responded. "How often do you use AI?" Great. "And which of these have you used in the last month?" Some of these are easy.

**Anand**: [13:12] I will... yeah, pause at Question 5 and 6. These are questions that require you to think a little bit. **Take a guess; it's absolutely not evaluated. The point is not whether you get this right or wrong; the point is what is the first answer that comes to your mind—even after a bit of thought, what answer comes to your mind.**

**Anand**: [13:35] Because the important question is the next one, which is: **"Do you think AI will get the same question right?"** That's what Questions 5 and 6 are about. Put another way, what we're doing is getting a sense of how—what the class thinks AI will say. And let us test whether AI actually gives the same answers that we think it gives. Part of our ability, if we're going to use a tool, is to know when the tool will get something right and when the tool will get something wrong. That's part of what we're testing.

**Anand**: [14:14] If anyone has any questions about any of the questions, please just speak up.

**Anand**: [14:52] 76, give or take. So, I'll wait till we have—okay, we have about 57 answers to the first question and nine answers to the last. I'll wait for us to get to maybe about 60-odd answers on all of those.

**Anand**: [16:01] And for those of you who've completed, if you have any questions, you're very welcome to ask. Yes, please?

**Unsure**: [16:27] Is it easier for us humans to judge AI, or AI to judge us?

**Anand**: [16:51] What do you mean by AI judging us?

**Unsure**: [16:55] Because in one of the cases that you told, some humans thought the AI was wrong and we are not comfortable with that.

**Anand**: [17:12] **Is it possible that the AI knows more than us? In which case, how do we even know if it is correct?** Supposing a friend says something and you don't know it. How do you judge? What's your suggestion? How do you judge?

**Unsure**: [17:28] By checking multiple sources of data, thinking and effectively doing the research and independently trying to come up with the answer.

**Anand**: [17:38] That is a great approach. And sometimes you don't have that much time, energy, effort. How else? It's an open question. We are not an expert. AI said something. **How do we know if it's right or wrong?**

**Unsure**: [17:52] If we cross-question and it still says the same thing, then it can be trusted.

**Anand**: [17:58] **Cross-questioning—absolutely.** That's the second approach. We've seen another approach in this class. Two other approaches, actually.

**Unsure**: [18:08] Use another AI.

**Anand**: [18:09] **Use another AI. Ask another friend.** And tell it, "Look, my friend said this." Fourth approach: **Don't use another AI and tell it, "You are wrong. Find your mistakes."**

**Anand**: [18:21] Henry Kissinger used to do this. His approach was: Somebody would submit a report, and he would ask them, **"Is this your best work?"** "Umm... I'll come back to you." He'd go back and he'd try it again. Second time. "Is this your best work?" "I'll come back to you." Third time, the guy would just give up and say, "Yes, I can't do better than this." At this point, Kissinger would take it and read it. **"What was the point of me wasting my time if that was not your best work?"** You could apply the same to AI.

**Anand**: [18:55] These are techniques you're already familiar with. And these are not the only techniques you're familiar with. **How does an auditor, who knows nothing about the business, audit a company?** How does a judge or, in countries where there is a jury, who know nothing about scientific discoveries, rule on patents? How does a regulator, who probably has no clue of the domain they're regulating, still pass regulations?

**Anand**: [19:24] And these are institutions that have been running reasonably successfully—not without errors, but reasonably successfully—for centuries. **People with low expertise have figured out a variety of different mechanisms to manage the veracity of smarter systems.**

**Anand**: [19:45] For software, you write a large application. You give it a test case. Say, "Against each of these, this is the expected output," and you don't share the test case with the models. So, put another way, one of the things that we can do is learn from each of these practices.

**Anand**: [20:01] **How do I know this? Not because I have done all of these, but because I asked Claude this question a few days ago.** And I said, "Look, I don't know how to do this. You tell me how are other people doing it?" And it gave me a long list, and then it extracted from that what are the techniques that I should be practicing and how I should be practicing it. **In other words, a big part of what is the counter to AI is: Learn from AI.** Another big part of it is: Treat AI like an expert or a human institution. And both of these seem to be working.

**Anand**: [20:36] Okay, we have over 60 across all the questions—67 plus. Yeah, good enough. So I'm going to treat this as we have the data. I'm not yet going to analyze this; I am going to analyze this in a short while. But we are going to talk about slightly different things and then come back to this.

**Anand**: [20:58] So, let's talk about classification just to stop there. Fine. Let's talk about clustering. So far, what we covered was: **It is possible to take text and classify it. Maybe that is useful.** You've seen a few different uses of it.

**Anand**: [21:19] **It is possible not just to classify text; it is also possible to cluster text.** Now, what exactly does clustering mean? Clustering is basically bringing a bunch of things that are similar together and saying, "Oh, all of these are one thing," and "All of those are another thing." At which point you'd say, "Wait, but isn't that the same as classification?"

**Anand**: [21:36] So, question: **In your minds, intuitively, how is clustering different from classification?** This is not a "what is the definition?" question. This is a "how are you thinking about it?" Yes, please?

**Unsure**: [21:51] Sir, one live example we can also see from the task. So, when [Unsure] tried to classify, the AI generated the entries based on *those*. If we did not provide any input, the AI automatically just went through the data and then figured out that some companies belong to some other group. That is more of the form of clustering. But if we specify something at first, then that is more classification.

**Anand**: [22:15] That's how I think about it as well. To summarize, it's: **If I say, "Put it into these buckets," and I know the names of these buckets, it's classification. If I say, "You find out what the buckets are—maybe give it names, maybe don't even give it names—but just group the similar things together," that's probably clustering.** Fair enough.

**Anand**: [22:31] Now, for clustering, we at least need to know whether two things are more similar than each other or less similar compared to each other, which means we need some measure of similarity. Now, for numbers, we have measures of similarity. For multiple numbers, we have measures of similarity. You have X and Y, you find out the distance between those two points. Fine. You have X, Y, Z—find out the distance. Any number of numbers, you can find out the distance. And there are many ways of finding the distance as well.

**Anand**: [22:57] What if it is not numbers? What if it is code?

**Anand**: [23:01] I told you I teach a class, right, on—what is it called?—Business Data Science. So, in this class, cheating is not only allowed, it is encouraged. There is an exam which, right at the top, says: **"You may copy from each other. It is perfectly allowed. Sit in a group. Pay somebody else to take your exam for you. I don't care. Just get it done. Score high."**

**Anand**: [23:22] Now, despite this instruction, not everybody is copying. What is your guess on the percentage of students who are not copying? How many students are not copying? Guess.

**Unsure**: [23:40] 50%. 30%. 20%. 5%.

**Anand**: [23:47] **50% of the class is not copying.** I'm begging, I'm pleading, "Please copy, score higher marks by copying." "No, we are ethical. We don't have any friends." Multiple reasons. "We are independent-minded."

**Anand**: [24:04] And so I said, let us see what this does to them. Each of these boxes—sorry, I'm going to reload; it's going to be a little bit slower—is one student. And **if two students have copied from each other, their solutions are similar**. This is where the solutions are identical. This is where the solutions are mostly similar, even more similar, even more similar.

**Anand**: [24:33] And you can see that—let's start here. So there is this group of students who have copied from each other. One student, roll number 23F10050, is the first person that created it. And the second person in yellow copied it. All the others in red copied from either the first or the second. So, leader, first follower, and whatever the rest are.

**Anand**: [24:57] Here is another cluster. One student...

---

**Anand**: [00:00] One student created it, another student copied, and so on. Now, are these really independent clusters? What happens is some of—this cluster, for instance, is merging into the earlier cluster at 99% similarity. How is that happening? This person in green has copied from someone in this cluster, probably made a small change—one line, intentionally, accidentally, whatever—we can go take a look at the solution and see how it is different, right? And that person's friends have copied from that. Great.

**Anand**: [00:39] So, we also have a sense of how the copying is spreading. The grays are the ones, even at whatever—50% similarity, the grays have neither copied nor allowed anyone to copy from them. Perfect standalone independents. Great.

**Anand**: [00:58] Now, at this level, it is roughly 50% who are grays; they're not copied, they're not allowing others to copy. But how am I figuring this out? **We need some kind of a distance measure between two pieces of code.** How can we do that? So I asked ChatGPT, and it said you can use something called a Jaccard similarity. "Boss, I don't understand what Jaccard similarity is. It's an ugly formula." "No, I know you can solve it. I am going to teach in a class. I have to at least know as a teacher what I'm doing."

**Anand**: [01:31] So it explained to me, and the concept is reasonably straightforward. **What it does is it takes a program and splits it into words.** And then it decides a window—five words. First five words, then the next—from the second to the sixth, third to the seventh, fourth to the eighth, etc. So now, if the program has 100 words, now it has 100 minus 4, 96 such five-word phrases. **It takes all of these five-word phrases for all of the programs and sees how many are common as a percentage.**

**Anand**: [02:08] That is very intuitive. So, how many five-word phrases are common between two programs? Now, how are you defining phrases? It said, "Oh, I will remove the comments; I'll do this." "At this level, I don't need to understand. It's fine." Next, if you want, I'll do abstract syntax trees. I said, "Which you think is a better approach? Is this your best?" And after two iterations, it said, "Yes, this is my best." "Okay, good enough for me."

**Anand**: [02:37] But now we have the Jaccard similarity, which is a percentage metric, and therefore I can say how many people have more than 90% similarity, 80% similarity, 70% similarity, which allows me to create this cluster. How did I create this cluster? I asked ChatGPT or Claude in this case, "Create the cluster," and it created the cluster. That's all.

**Anand**: [02:59] If that is the case, then wouldn't it be cool to be able to do this for text as well? Now, this is text, you could say. And therefore, I could do the Jaccard similarity between two pieces of text to see how much they've copied. But here's a problem: **Copying takes many different forms.** Yesterday, I was asked to submit an article for *Built In*. *Built In* is a magazine. And they said it should not be AI-written. Now, I don't know how to write without AI.

**Anand**: [03:31] So I anyway asked AI to write an article. I said, "Look at all my notes, create the article." And they said you have to put it into Pangram, which is a tool that detects if it's AI-written. It said 100% AI-written. Okay, fine. "Now rewrite it in my style." It rewrote it, and I put it in, and it said 100% AI-written. "This is not working."

**Anand**: [03:52] So I tried something else, which was: I read out the article. And it had some weird phrasing. But **I just took the same article that it wrote, I read it out, but making a few modifications—the way I would normally speak. Translate that, put it into Pangram—it's 100% human-written.** Now I have a trick. At least I have an accelerator; I still have to read it out.

**Anand**: [04:22] But what that means is other people like me, when they're copying, will smartly change a few words. Forget copying; supposing you want to find out in a product survey whether there are certain concepts that people are clustering around. They will be writing in different languages, they will be writing in different phrases, words—**you can't just take the Jaccard similarity or the word similarity or phrase similarity. You have to do something different. And that is what leads us to the concept of embeddings.**

**Anand**: [05:01] How many of you have heard the word "embeddings," or how many of you know what embeddings are? That's about 10%. Cool. Let me explain how embeddings work. Supposing you had a dictionary of 40,000 words, approximately. Put that as columns in Excel—all 40,000 words. Take any sentence, and if the word is there in the sentence, put a 1; otherwise, put a 0. Now you have converted sentences into a set of numbers—zeros and ones. Or maybe if the sentence—the word is there three or four times in the sentence, put 3 or 4.

**Anand**: [05:43] That gives you a word count. That in itself is kind of useful to tell you the similarity between two sentences—how often the words are overlapping. **Instead of words, supposing we replace that with concepts.** Great. I can somehow find out—AI anyway doing somehow all kinds of things. Somehow using AI, we map it to the concepts. Then I can start finding the similarities much better. That's effectively what embeddings are.

**Anand**: [06:17] Now, what are these concepts? We don't know. We kind of have an intuitive understanding of what some of these concepts are, but nobody's really bothering these days. **Have we covered Principal Component Analysis yet? We have covered it.** Okay, so in PCA, you are probably trying to interpret the principal components. **Imagine that there are 1,500 principal components that break all of the language into. That is what embeddings effectively are.**

**Anand**: [06:55] Now, what that allows us to do, therefore, is to figure out if one particular phrase versus another phrase are very different on the first dimension, very different on the second dimension, etc. And these dimensions are reasonably independent of each other. So that allows us to do some fairly interesting things.

**Anand**: [07:22] **I'm going to actually, before we do that, ask you to try something.** How many of you have vibe coded so far? How many of you have not vibe coded so far? Okay, that's about 5%. All right, not bad. Cool. Great. Since the majority of you have, and the rest of you, it's not a big deal, let us vibe code the following. **I'd like you to build and share an application where I can type in two phrases and it will calculate the embedding similarity between these.**

**Anand**: [08:03] It will say these two phrases are 80% similar, 20% similar, 5% similar, whatever. Give it a shot. Of how would you do it? Increasingly with AI, the answer is: Tell it to do it. And if it can't, ask it why it didn't do it. And once you have that link, please share that. I will give you another—let's see, I'll call it "Vibe Code Link," in which I'll say "Share the link to your embedding similarity calculator."

**Anand**: [08:50] And the form should have the last question now as the embedding similarity calculator link. It's 3:24 PM. Let's again see how long it takes for you to vibe code—for AI to vibe code—an embedding similarity calculator. Right before, and let me quickly talk to filter the time. If anyone has any questions, you're very welcome to ask; otherwise, I'll randomly talk stuff, which is not so cool.

**Anand**: [09:27] I'm conscious that many of you may not know what embeddings are. Doesn't matter. As long as AI knows, for now it's okay. Many of you may not have coded this before. Doesn't matter. Try it. If it fails, what do you lose? As long as some of you are able to do it, we'll put it on the screen and plumb through it. **Maybe it is not even technically possible.** Great. Ask it how to make it possible. **Do I personally know if this is possible? I don't.** I have never asked for an embedding similarity calculator to be vibe coded.

**Anand**: [10:33] Just something to keep in mind: It's not like AI will overcharge you. Don't bother asking a question to one of your friends; ask three of your friends. Save you time. That's one of the things that we're discovering about AI in the era of plenty. **Generation or doing stuff used to be expensive, so we would think, we would rationalize, we would plan. Now it is cheap. What is the point of conserving something that is cheap?**

**Anand**: [11:54] In case anyone's still not sure what prompt—what to do, here's a simple recipe. You can just copy this entire text, put it into your favorite AI. For those of you who feel that is too much work, you can take a photo of this and put it into your favorite AI.

**Anand**: [13:21] Okay, please share and paste the link in the same form. The form link is out here—`forms.s-anand.net`, in case you have missed it. It's the same form that you were filling earlier. Right at the end, there is a "Share a link to your embedding similarity calculator." So that was six minutes. Great. The link is `forms.s-anand.net`, in case you don't have it.

**Anand**: [13:58] So those who have completed it, just go back to the same form and... okay, so we have one response. I am going to see the form responses. Okay, we have a Gemini link. That would have been my guess as well. And this was created by another person, which is great. And Gemini is loading, which, given my phone connection, will take its own sweet time.

**Anand**: [14:41] And... yes. So, "The quick brown fox jumps over the lazy dog." "Fast dark-colored fox leaps above a resting hog." Yeah, these look similar. Calculate the similarity, and... whoa. Okay, I am going to reload this page. Sorry, I'm going to close this page. Fantastic. This was by Saurabh. Is Saurabh here? Sorry, okay. Very nice. That is not what we wanted or needed. And not that this is...

**Anand**: [15:37] Let me talk this out. **What it is doing is downloading something like a ChatGPT on the browser and then telling it, "Here is one phrase, here is another phrase, how similar are they?" This is a remarkable feat of engineering.** Remarkable for a couple of reasons: One, it's literally running an LLM in my browser itself. Second, that it was able to do it in six minutes, which is crazy. However, it is not what I want for this class.

**Anand**: [16:11] Now I'm trying to think. Here's something that is really powerful; on the other hand, it will take us in a different direction. What do we do? **Why don't you tell it, or in parallel run something different—effectively saying, "This embeds an LLM. This runs an LLM. I just want to use an embedding model."** Tell it, "I don't want to download the model." Why? Because my phone connection is low. Actually, this may still be an embedding model. Many LLMs have an embedding model, so I may be wrong.

**Anand**: [16:51] We had another link—a Claude artifact from Avni, and a bunch of others. Let's see. Let's take the Claude artifact as well as Saksham's Gemini. Okay, this is an embedding similarity calculator. So I am going... how do I run this? Any idea how I change the words and run it?

**Anand**: [17:24] Oh, what this does is it lets me type two pairs of numbers and then calculates the cosine similarity between those. Kind of correct in that if I give it a bunch of numbers and say "How similar these numbers are," it is calculating it. But **what we wanted to do was give it a pair of text phrases and then have it convert them to numbers and then find the similarity.** So, again, not bad, not quite what we wanted. And we could give it the same feedback that I just shared.

**Anand**: [18:04] This says, "Here's an interactive text similarity analyzer." Calculate the similarity. Okay, so Sentence 1 and Sentence 2. Let me—if I'm able to change it... okay, I'm not able to change the sentence here. What you may want to do is share the artifact, not the chat itself. There are two different share buttons.

**Anand**: [18:28] **A big part of this exercise is really teaching you how to vibe code on the fly, how to share, etc. So the fact that all of these little nitty-gritties I'm pointing out, despite having accomplished something pretty significant, is to take you to that next level.** So please don't worry that you haven't gotten there. Who else have I... okay, Om's... let's see. Oh, okay, let's take Pawan's and let's take Om's... Pragdheesh. Okay, Pragdheesh, if it's a document, that's not what we want. We want an application. Wherever Pragdheesh is. Avni's we've seen, Saksham's we've seen, and I will take Rohit's as well.

**Anand**: [19:20] Okay, here is again... fine, something that will do a cosine similarity. Worst case we will live with this, but let's say we take "cat," add it, and calculate the embedding... okay, the model is still loading. I'm going to close this. This technically works but is pretty expensive. Let's say "cat" and "bat" and compute the similarity. This is saying 15%. But how is it doing that? Let's try...

**Anand**: [20:00] Who had shared this Claude artifact? Okay, got you, Om. Let's see if this is doing it in a way that won't eat up too much of my bandwidth. "Cat" and "bat." It is sending a Claude Sonnet message, kind of doing it in a different way. Okay, **what this is doing is asking Claude how similar these two phrases are, and it's coming up with a number. Embeddings work somewhat differently.**

**Anand**: [21:05] So, let me share how I might do this. Actually, maybe I've just given you an impossible task without an API key. How many of you have an API key? Okay, a couple of you. Not too bad. Want to try it with your API key and share? The rest of you, I know you have no idea what we're talking about, but that's okay. Give it a shot. Yes, please?

**Saksham**: [21:39] My link should be working, actually. I just checked it on a separate laptop.

**Anand**: [21:44] So let's—well, or I could just let it load. Can you just point me to which row it is? Last but 1, 2, 3?

**Saksham**: [21:52] Yeah, just below the Pawan's...

**Anand**: [21:55] This one? Ah, okay, yeah. Pawan, okay, sorry. Yeah, what am I saying? I can see your name. Great. Let's—fine, let's give it a shot. And let's just... aha. Is there a load... okay, downloading 6%. Fine, let it run.

**Saksham**: [22:31] It's also at the bottom, if you want to connect to OpenAI directly.

**Anand**: [22:34] No, it's okay; it's just slow, it's not expensive. So we will talk in the meantime. Yes, please?

**Saksham**: [22:45] Sir, the link I shared for Gemini...

**Anand**: [22:48] Saksham's link is working. Let's validate. No, it may simply be that this is taking too much bandwidth—my bandwidth, not your bandwidth. So let's... okay, this one... Oh, I see what you mean. Okay. Even further? Okay.

**Saksham**: [23:11] Ah, I didn't see this. Thank you. Okay, text similarity analyzer. Got it. And here is where you're saying I can type.

**Anand**: [23:18] Yes, you have to backspace the old text.

**Anand**: [23:22] Okay, I'm not able... yeah, I think it's because it was shared as a chat, not shared as... but anyway, I used the same lab on a different browser, and it's still able to... no, definitely not in my case. And I doubt if it's a browser thing. But no, these are in the early stages.

**Anand**: [24:18] So let's go here and calculate the similarity. Okay, calculate embeddings, and it's created a similarity matrix. Now, let's talk a little bit about this. This was Pawan's. So what Pawan's calculator has done is—and we'll keep it simple. Let's take two phrases. I'm going to say... okay, no, let's take half a dozen phrases. **"Apple," "Orange," "Jamaica," "Football," and some other country—"Jordan."** And calculate the embeddings.

**Anand**: [24:59] What this is saying is: **"Apple" is very similar to "Apple," but has a roughly 37% similarity with "Orange."** 28% similarity with the third one, which is "Football." Oh, okay, okay, with "Jamaica." 27% with "Football," and 35% with "Jordan." "Apple," "Jordan"... I don't know, there's some Michael Jordan, Apple the company connection? This is a little higher than I had expected, but it's entirely plausible.

**Anand**: [25:40] But **what is clearly emerging is that two of the highest correlations are between "Apple" and "Orange"—37%. Another very high correlation is between Doc 5 and Doc 3, that is, "Jamaica" and "Jordan," both of which are countries.** So, clearly, it's gotten the hang of it. Countries are similar to each other, fruits are similar to each other, the rest are slightly dissimilar to each other.

**Anand**: [26:11] In other words, **it is possible for us to calculate the similarity between any two phrases as a number.** With classification, there is a difference. We were saying, "Put it into some bucket," and it was doing a reasonably good job. **Here we are saying, "Give me the exact distance," so to speak, between two phrases or documents, and it is giving me a number.**

---

This is the final part of the workshop transcription.

**Anand**: [00:00] ...gives me a number. That allows me a little more control and allows me to do a slightly different set of things, including clustering. Now, how can we use this? Well, let me show you an app that I had vibe coded some time ago. Let me reload it.

**Anand**: [00:23] **This is an employee survey. This is real data, by the way.** This is the Gramener 2020 employee survey, where we had asked our 200-odd employees at that time: "What is good about Gramener? What is bad about Gramener?" One of them said, "Good: rigorous delivery and culture of experimentation. Good: work-life balance," etc. And what is bad is at the bottom: "Scope of work and timelines, internet instability in Bangalore, need to focus more on work-life balance, transport from the old office, new office," lots of stuff.

**Anand**: [00:59] Nobody has the patience to sit and read all these. These were the two last columns, which were generally left unanalyzed, apart from a number of classic NPS score kind of things. Let us analyze it. What I'm going to do is click on a "cluster documents" button. **This, behind the scenes, is doing exactly what we saw Pawan's tool do a short while ago: calculate the similarity between each of these and show it as a picture.**

**Anand**: [01:31] Very similar to what we saw before. What this is saying is: Anything that has a similarity more than some number, you connect the dots. So, something that has a similarity of more than 0.99—or greater than or equal to 1—connect them. What that means is these are identical: "Team collaboration," "Team collaboration." These are identical: "I am satisfied while working at Gramener." **Imagine two people typing in exactly, right down to the full stop and the capitalization: "I am satisfied while working at Gramener." So now you start wondering: Are they copy-pasting the survey also?** Unlikely. "Flexibility," okay, I can understand. But some of those phrases were... sorry.

**Anand**: [02:22] Now, let's start clustering. One cluster seems to emerge. What is this about? "Work-life balance. Good." Now, what is interesting—by the way, the... broadly, people seem to feel work-life balance is something that they are happy about. "Nothing as of now. Okay." That's another smallish cluster. "Nothing. Okay." But these two clusters should really be joined together, right? And maybe that will happen at a slightly lower threshold. And yeah, they're kind of coming together. Still not quite joined; maybe they've joined, I don't know. But still not joined, right? Yeah, fine, but let them stay.

**Anand**: [03:07] Now, this is one major cluster: "People at Gramener are approachable," "Working at Gramener," "Office infrastructure," "Physical IT." **Sort of seems to be the way in which we're working at Gramener that seems okay.** "Work-life balance, work-life balance, work-life balance," blah blah blah. That's one big cluster. What is this? "Team members, collaboration, communication," and so on. And here is another: "Nothing as of now, nothing as of now." Yeah, we saw that.

**Anand**: [03:41] Now, at this point, I have, on the one hand, a very powerful tool. I get a sense of the major clusters. I also see that there is a long tail. There are some of these which are very different—meaning, even at a very high level of similarity, some of these comments are still outliers. So, what are these outliers? Oh, okay, these are all blank. So maybe they're all blank, and the blank ones just have not... okay, fine, these are all the blank ones. What are real outliers? Okay, some of these are just jutting out, about to explode... almost there... Okay, yeah, so this—these two at least: **"Recently joined the org, still exploring the org." Very different from what anyone else is saying.** What is this cluster that is so different from all the others? Okay, this is the "Nothing" cluster. Okay, fine, that is an outlier. And you get the idea.

**Anand**: [04:39] Now I can use this to start seeing what is just moving outside and seems to be more of an outlier. "Project management" seems to be a bit of an outlier. **Clearly a powerful way of getting a new kind of insight into—a new kind of exploration into—the data.**

**Anand**: [04:55] **So, exploratory analysis with clustering starts giving us a different kind of insight.** But let me clarify three things here before we dive a little deeper into this. Number one: A lot of the power of this is coming because of the **textual embeddings**. We are able to process text which was hard before. Embeddings make that possible, and LLMs somewhat enable the embeddings. That is power number one.

**Anand**: [05:22] Power number two is from the **clustering algorithms** themselves. In this particular case, I'm not really using a clustering algorithm; I'm using something far simpler. I'm just saying, "Connect the lines that are similar." But that is not all. There is a user element interface to this, which is a **force-directed layout algorithm**. How does that work? It connects the dots and then keeps them like planets connected by springs—not planets, more like electrons connected by springs. So the electrons repel each other; they don't go near each other. But because they're connected by springs, they cannot move too far away, and it does a physics simulation.

**Anand**: [06:05] Now, who's going to sit and write all of this? The answer is: There are already libraries to do this. You just say "vibe code it: create a force-directed layout on a network diagram," and it will do it. And there are simpler ways of doing it as well. But part of the power is coming from the algorithm—in this case, force-directed layout, but it could be a K-means clustering or anything else.

**Anand**: [06:29] The third power comes from the way in which we have allowed interactive exploration—to be able to "brush," for instance, and select a region and be able to inspect it. It is a simple thing, but when you add that kind of an interface, you start being able to do more things.

**Anand**: [06:47] This takes us towards one path, which is **Exploration. Exploration is fantastic when you are trying to figure out something you don't know you want.** Meaning, beforehand, I don't know what the clusters are going to be; I don't even know what I'm going to do with them. So if that is the case, exploratory analysis is a good thing.

**Anand**: [07:08] **Sometimes you don't want to do much of the work. You don't want to sit and figure out what the clusters are; I want IT to figure out what the clusters are. And this is called Topic Modeling.** Topic modeling is simply—let's go here—finding the topics. So what I'm going to do is say, "Run a K-means clustering and give me maybe a dozen topics. And once you've found those clusters, choose some model to give it a name and find the topics."

**Anand**: [07:38] So it is now thinking. It will soon find all the clusters and then give each of the topics names. So there's one person who said, "I am not sure, thank you." Very different cluster; completely independent cluster of one. And the name is "Gratitude and no change." Fine. A whole bunch of people, 43 documents, belong to the "Office amenities and IT" cluster. Great. "Project planning and delivery" cluster, 45 documents. "Team collaboration and quality," and so on.

**Anand**: [08:14] **How did we come up with this? Step one: Get the embeddings**, almost exactly like Pawan's similarity matrix. For each one of these survey responses, calculate an array of numbers. Those numbers represent the concepts. **Second: Calculate the similarity between each one of those pairs.** **Three: Do a K-means clustering based on these similarity numbers.** How do you write all this code? Tell ChatGPT to write the R code; it will write the R code. Tell it to run the R code; it will run the R code.

**Anand**: [08:48] **Once you have that, then the fourth step—which is the only additional one—is give it all a name.** So for this, the logic is: Take all of these documents—what I did was send the entire document set to ChatGPT, specifically GPT-5.4 Nano as a model, and said, "Here are clusters of documents. Give me two to four word topic names for each cluster and capture the spirit of the cluster, differentiate from the other clusters." Which gave me the list of topic names.

**Anand**: [09:19] So now I know that the kinds of things people are talking about in this survey are: "No feedback yet," "Peer/manager support," "Work-life balance," "Open communication," etc. From here, having done the **discovery of clusters**, including the naming of the clusters, I can start doing **classification**.

**Anand**: [09:41] What I mean by that is: I look at this and say, "Hold on. 'Gratitude and no change'—what can I do with that? Actionable? Ignore it. 'Office amenities and IT.'" Now, Girish is our office admin; Sagar is our IT admin. They have very different priorities. I can't tell Girish to do Sagar's job; I can't give Sagar something for Girish. I want to split these. So: "Office amenities and physical infra," "IT infra."

**Anand**: [10:14] **So once I've discovered what the clusters are, I can decide that some of these clusters are not actionable; a different set of clusters are actionable.** Because ultimately a person has to do the job; I am simply going to give the feedback to the person. This is how I want it classified. "Project planning" will go to Shiva, "Team collaboration" will go to Manju, "Work from home" also will go to Manju, blah blah blah.

**Anand**: [10:41] So now I know who's going to get what. Some of these—"Overall satisfaction" doesn't help me, "Gratitude and no change" doesn't help me, "No feedback..." okay, fine. Maybe I can combine all of these: "No feedback yet," "Overall satisfaction," or "Gratitude and no change"—put them all into one bucket. Now that I have this, I can then say, "Classify against these."

**Anand**: [11:06] **Now the interesting thing about embeddings is that I can use the same distance to classify as well.** Option one was: We send the input to ChatGPT or use an `AI` function and say, "Which of these categories does it belong to?" Or, the embedding we computed—we can find out the exact similarity. **And this is somewhat deterministic.** Every time I run it, it will give the same result. It may not be very nuanced like an AI function or ChatGPT, but it is at least deterministic and reasonably accurate. And as the embedding models get better and better, these will also get better and better.

**Anand**: [11:43] So now I can say, "Give me the best topic." "Rigorous culture and delivery of experimentation" fits best in "Learning and experimentation." Absolute sense. "Work-life balance" fits best in "Work-life balance." Okay, that is very obvious. "Recently joined the org, still exploring" seems to fit best in "Learning and experimentation." Yeah, maybe. 28% for "No feedback yet, overall learning," etc., was also a possibility, so not really sure.

**Anand**: [12:12] **So with this, we now have the classification derived from the clustering the way I want it.** This means, number one: Any kind of textual data anyone collects in a survey, we can find out what are the different things people are talking about—answering one of the most common questions that people have, which is: "What did people say? How can I get insight from a massive survey?" Supposing you're running an interview, a group discussion, product discovery, something? **We now have the ability to identify what are the topics people are talking about.**

**Anand**: [12:47] Number two: **We have the ability to change those topics however we want based on how we can actually act, reclassify, put it against those buckets, and filter down and get to the results.** The incredible power of this is we have moved from numbers to text. But from text to images, code, video, audio, DNA sequences, food recipes, and a whole bunch of enormous possibilities—is only a small step.

**Anand**: [13:21] Given that we're supposed to break at 4:00 PM—why don't we do this? **That is what we will start with in the second half.** If any of you want to continue vibe coding and share a link in the form, please go ahead and do that. But we'll take five minutes for questions and then break. Any questions so far?

**Saksham**: [13:46] So, when we did the discovery, you had those two Excel sheets and you asked us to like classify into those six buckets. So that time we just ran the prompt directly to the LLM and then did it. So that time also it must be doing like, on the backend, like first embeddings and then calculating the similarity and finding out. So why is that...

**Anand**: [14:14] **Excellent point.** The question is: Wasn't ChatGPT also doing embeddings? What was different about embeddings? **LLMs work differently. They predict the next word—and I'm going to use "word" as a synonym for the technical term, which is "token."** What that means is: These are models that have been trained saying, "I'm going to take... predict the next word, next word, next word," etc., because in the past, whenever these words came together, this is the next likely word, and so on.

**Anand**: [14:48] But the same data has also been used in a very similar way to train slightly different models. And these models are called **embedding models**. And the embedding models are not what ChatGPT, Gemini, etc., use. They provide them separately through an API; they are available for download.

**Anand**: [15:10] Those models do something very different. **When you give me some text (or images or whatever it is), they say, "I will do a equivalent of a Principal Component Analysis and give you all the concepts that this represents as a 1,500 or 3,000 long vector." That is what they do.** And thanks for raising this because it brings up an important point, which is: There are two ways of using AI—LLMs broadly. One is as token generators, which ChatGPT does, and embeddings, which are a lot less popular. Usually programmers are aware of it, not others. But you don't need to be a programmer to vibe code, so use it. **Advantage: Very cheap. Deterministic. And reliably on your data.** Any other questions?

**Anand**: [15:58] We could break then. Let's do that. 4:15 PM? Thank you.

---

**Anand**: [00:01] Okay. We were talking about embeddings and how embeddings can be used to find out if two pieces of text are similar to each other. Not only how, but the fact that it can be used. What we're going to do now is move on to images and other forms.

**Anand**: [00:29] Let me take a step back and talk a bit about the way in which we’ve been running this session so far, which is happily diving in without giving you much context. Let me share the **three things that I want to ultimately leave you with**, not as a lesson but as an experience. **Number one, use AI. It can do things you may not have thought of.** Maybe some of you have tried a few of these things. Maybe some of you have tried all of these things, and I’d love for all of you to try all of these things.

**Anand**: [00:59] So in short, this is **how can I do multivariate analysis using AI**, and the AI part of it I’ve front-loaded. Second, the bulk of the session—the first two-thirds of it—is going to be about **how we analyze unstructured data**. A significant portion of the course is about how you would analyze structured data. **Text, images, and more are things that we can now, with AI, analyze**, and this is a great exposure into how you can do that.

**Anand**: [01:31] I’m comfortable not going into the nitty-gritty of how, or teaching you the theory, because that you can and will learn. And if you don't want to, AI can solve that problem for you. So both options exist. But **knowing that this is possible and how this is useful is also what I want to share**.

**Anand**: [01:54] The third is I want to give you an exposure to the kinds of things that we are doing at Straive and Gramener. All of this is coming out of the real world. **This is what is happening today when we're analyzing data. Keep that as context.**

**Anand**: [02:11] Now let’s take images. So one of the projects that we were doing was for a real estate company, not very different from Airbnb. And they said, we have a whole bunch of pictures. **Can we start clustering these pictures?** Times of India reached out to us and said we have a massive catalog of images. **Can we do an image search automatically?** If I type let’s say Rajiv Gandhi, will it be able to find Rajiv Gandhi? If I search for Rajiv Gandhi sad versus smiling, will it be able to differentiate?

**Anand**: [02:43] Now, if I have documents, I can find out the answer using embedding similarity. Now, why am I saying embedding similarity instead of using Chat GPT? Because with Chat GPT, I have to upload a large document set. That takes time; that takes tokens. **Embeddings, once you have pre-computed them, you have a bunch of numbers with you. You can store those numbers. You can calculate them with R, Python, whatever, and the cost is zero.** So that way, embeddings have an advantage that just uploading every time to Chat GPT does not.

**Anand**: [03:17] Similarly, **if we can get embeddings for images, that is fabulous. Embeddings exist for images.** Let’s talk a bit about what we can do with that.

**Anand**: [03:31] Let's start with this. These are photos of Bollywood actors. And if I ask the question, whose photos are the most similar? I don't know how clearly visible this is, but are you able to recognize the actors on the right side? [inaudible] Okay, not quite. Yeah, some people got it right. That is Riteish Deshmukh, and yeah, that is Rajkummar Rao, and this is Shreyas Talpade.

**Anand**: [04:05] Now, between these three—and if I took it to a slightly closer one—two photos of Riteish Deshmukh? Yeah, obviously Riteish Deshmukh looks like Riteish Deshmukh. But what it's saying is **Shreyas Talpade looks closer to Riteish Deshmukh than many other people look to themselves.** Meaning, there are two photos of Arjun Kapoor, there are two photos of Vani Kapoor, and so on. It's saying that Shreyas Talpade looks closer to Riteish Deshmukh than they look close to themselves.

**Anand**: [04:36] Not an unknown thing. When I did a Google search and found a number of blog posts where they're talking about, "Oh, long-lost twins, why are they so similar?" etc. Good to know that it's picking this up. What that means is **if I wanted to cast a duplicate or a long-lost brother for one of these actors**, Shah Rukh Khan looks like Shah Rukh Khan, Aishwarya looks like Aishwarya, and who's this? Varun Dhawan looks like Varun Dhawan. So we've identified only... well, Rajkummar Rao maybe a Riteish Deshmukh clone. Who else can we cast as duplicates? These are all people who are matching themselves. Anyone matching someone else? Let's see. Not quite yet, but maybe it will emerge.

**Anand**: [05:29] So rather than do this, let me just find out. I think I can do a... yeah, let’s take Nana Patekar. I want to cast somebody as a duplicate for Nana Patekar. Let me move him out here and see who comes closest to Nana Patekar if I reduce the embedding similarity. Oh, okay. In this photo, Anil Kapoor seems to be close to Nana Patekar in this photo. Again, not sure how well you are able to see it in the bottom, but okay, let me move it to the top. This photo of Nana Patekar and this photo of Anil Kapoor seem close enough. So there is a decent chance that I’d be able to cast one as a duplicate or a long-lost brother of another.

**Anand**: [06:21] At this point, you can see the fun potential of it. But **the real potential is if somebody said, I am looking for an Airbnb kind of a room. I have seen this sort of a... let’s say this one. I’ve seen this bedroom. Do you have any other properties that are similar to this?** And you say, "Yeah, ma’am, I have one property that looks very similar. Here is where it is. This one seems reasonably close. Would you like to inspect this property?" Which was actually the use case that the client had come to us for.

**Anand**: [06:54] Similarly, for car photos. I have a used car; it looks like this. Can you give me a used car that is kind of similar to this model that I saw online? Again, fairly useful.

**Anand**: [07:11] Or also **the axes that we can look at**. So one of the things that we did was not quite a principal component analysis, but an embedding similarity on—let's take Hollywood actors. Can we plot who is smiling and who is frowning? So the X-axis is the similarity to the word "smiling" and the Y-axis is the similarity to the word "frown." Or let's change that to: X-axis is similarity to the word "African," Y-axis is similarity to the word "Chinese."

**Anand**: [07:51] Now, Morgan Freeman's photo here is the most African-like photo of the lot. And this is Eugene; he's the least African photo of the lot. So if I needed to cast in, let's say a Bollywood film, somebody who clearly looks African, then Morgan Freeman is someone we could go to, and here is one cluster. Among the Chinese, Jackie Chan looks most Chinese and Zendaya looks least Chinese.

**Anand**: [08:21] What you notice here is that we have done something pretty interesting. **We have taken an embedding similarity between a photo and a piece of text.** That too is possible. **That is the nature of multimodal embedding.** So for me to take a phrase and search, or at least find similarity to that phrase on an image, becomes possible and that is useful.

**Anand**: [08:50] Now, this leads to other kinds of capabilities. The Times of India again came to us and said, "Can you tell us... can you give us interesting news articles on an automated basis? AI can automate so many things. **Can you analyze the geospatial data and give me some insights on it?**" So one of my colleagues, Varun—who is still in college? [Audio interference/Check, check] Okay, no, no, I should... we can move a little less. [Audio interference]

**Anand**: [09:37] What he did was took geospatial data. **There is a model called AlmoEarth.** He doesn't know really what this is, nor do I. We just heard that it does geospatial data. He tossed it into Claude Code and said, "**Can you find out what has changed in a specific region over time?**" How exactly would he do it? What he did was took words like vegetation, water, urbanization, bare soil, etc.

**Anand**: [10:15] So in this case, the word is "vegetation." He took the similarity of the word "vegetation" with the satellite photo of a portion in Bangalore in Marathahalli in 2015 and compared it with 2025. This is the picture in 2025; this is the picture in 2015. And asked it: **vegetation versus this picture, tell me the similarity.** That is number one. **Vegetation versus this picture, tell me the similarity.** This is number two. **Tell me how much these numbers have changed between 2015 and 2025.**

**Anand**: [10:57] Same place, same word, how much has it changed? In other words, it's implicitly asking the question, **how much has the vegetation of this place changed from 2015 to 2025 just by calculating cosine similarities?** And did that for a large number of regions in Bangalore and plotted that as a map. This is going to take some time to appear, but eventually we hope it will... the colors... Okay, maybe not. Maybe I have to go to a different... Bengaluru... Okay, the tiles are loading. Okay, this could take some time, but let it load.

**Anand**: [12:03] So what he was able to do was do this over a 100-meter by 100-meter grid for every spot across various cities. And eventually, yeah, you get a rough heatmap, which is not too clearly visible, but I will zoom in a bit and... okay, I’ll set the opacity to a higher value... okay, this is... oh, okay, it is my network and that is real slow.

**Anand**: [12:35] **The reds are where the vegetation index has dropped. The greens are where the vegetation index has increased.** Put another way, this is a map of where between 2015 and 2025—sorry, it's still drawing—but between 2015 and 2025 where the vegetation has increased or decreased all over Bangalore. And you’ll see that it's largely decreased.

**Anand**: [12:59] But this is a spot where there is a huge amount of reduction. Which allows us to zoom in into that particular area and ask the question, what exactly is happening? So this spot seems to be one of the biggest drops. What is happening here? So it looks like there is some lake. Let’s change the base map to the ESRI imagery. This is the current situation. This eventually will appear as what happened... what was there in 2015. My guess is this is Bellandur Lake. So in the Bellandur Lake in 2015, this is what it looked like. And now, this is what it’s looking like. A lot of the lake has retreated and we have green coverage but effectively less overall vegetation as a net decrease.

**Anand**: [14:02] How can people use it? For the Times of India, it was, "**I don't have to sit and search; the data itself gives me stories.**" Second, I have validation. I can just go look at the satellite imagery and do a comparison. **How could you apply it, or how are we applying it? A whole lot of retail companies are asking, where should we open our store?** Now, with the kind of satellite imagery that we have, we can start answering that. **A lot of AgriTech companies are asking, where should we buy? What crop health?** A lot of environment companies are asking us where is deforestation happening? These are all live projects, and now we have a completely new tool to answer this.

**Anand**: [14:41] **Made possible by the exact same concept: embeddings. And an embedding is able to create a multidimensional vector of concepts, not just of text but of images, of video, of audio, and even recipes.** So this for instance, Epicure—and I’m not going to go into the details of this—is an embedding model tailored specifically for recipes and will tell you which ingredient, which recipe, etc., is similar to each other. And you can start using this for a variety of purposes.

**Anand**: [15:21] As a result, **embeddings now become part of your toolkit not just to do the analysis, but to get a new column.** So keep in mind that there are two possibilities here. One, I can get more data by adding new columns. One way we saw of doing that is classification. You say "equals AI" and tell me what type of company this is right at the beginning. That gives us a new column. This is giving us a new set of columns in a different way. It’s a long list of numbers, and that is additional data which we can cluster, which we can classify, and so on.

**Anand**: [15:59] Let's talk about a slightly different technique, which is how you can apply this kind of an idea to principal component analysis or UMAP. Have we covered UMAP yet? [No] Okay. Think of it as a slightly different way of doing something similar to principal component analysis. Before we go there, any questions so far? I’m very happy to monologue; you’re very welcome to interrupt me at any point because we can take this anywhere where you want. [pause] I’m just debating how interactive we should make this. Yeah, I’ll probably monologue for another 15 minutes and then we go crazy.

**Anand**: [16:50] This is the **UMAP of Calvin and Hobbes**. How many of you have read Calvin and Hobbes? Okay, Calvin and Hobbes is a popular comic strip. And to give you a sense of what it's like... okay, my network is so very slow. Right, so simple black and white strips that used to run. It's about Calvin, who's a child—a six-year-old—and his imaginary tiger, Hobbes.

**Anand**: [17:39] And what I did was I spent about seven years typing up all the Calvin and Hobbes from 2001 to 2007. There are about 3,700 of them. And then I took the text and the images, created the embeddings. Once we have the embeddings, we can cluster them; that’s one possibility. But what we can also do is **identify the principal components**. Take all the embeddings; what is the one axis that spreads out all of the Calvin and Hobbes strips extensively? What is the second axis that spreads them out extensively? What is the third axis, and so on?

**Anand**: [18:20] Except that instead of using principal component analysis, I’m using a different technique called **UMAP, which tends to do a slightly better job of pushing things out and helping us understand what the spread is about.** What this is showing is there are... okay, I also did a cluster analysis, and that cluster analysis is saying that there is a pink cluster, there is a red cluster, there is a yellow cluster, etc. What exactly these clusters mean is something that we can sit and analyze.

**Anand**: [18:50] But it is obvious that there is one bunch of comics which are standing out very different from the others. What are these about? **These seem to be mostly about this particular character. His name is Moe.** Moe is the class bully. And all of the strips related to Moe, they seem to be very distinctive from the other comic strips.

**Anand**: [19:18] The other example is these strips, very distinctive. These all relate to Rosalyn. Rosalyn is the babysitter and for some reason those strips again have a separate nature, very different character of their own. And this is... okay, I’m guessing all the superheroes. So Calvin imagines himself to be various kinds of superheroes. And this is probably some mix of those superheroes. That is another theme.

**Anand**: [19:51] Kind of similar to how we had created the force-directed layout, but there is a difference. In that case, it was non-deterministic; we could move it around, we could position things. **This is closer to principal component analysis and we can freeze them and put them where they are.** This is using text and images.

**Anand**: [20:12] What is the practical use of this sort of thing? The National Institute of Education, Mysore reached out to us and said, as an institution, our **NIRF ranking**—NIRF is an educational ranking by the government—is now at around 200. It used to be almost 100. We've fallen down a lot. What we need to do is improve it.

**Anand**: [20:43] So we asked Claude, we did a bit of research, and we found that **the number one factor that they could improve was research**. That is, the more publications, research publications they have, the bigger the influence it will have on their NIRF ranking.

**Anand**: [20:59] So the next question was, how can we improve? And what is the kind of research that is happening out there? What is the kind of research that we are doing? What can we do about it? So **step one was taking all of the research publications that they are doing, embedding it. Taking all of the research publications that are there, embedding it, and seeing where they fit against the background of this.**

**Anand**: [21:28] This is that space. The blues are where research is happening. The oranges are where they have published research. And we can see how this evolved over time. Let me see. Okay, yeah, this is where the data starts coming in. Yeah, so let me take a one-year period. Sorry, let’s take a six-month period.

**Anand**: [22:01] So in this six months starting from 2021 where there was practically no research... 2023... okay. **The bulk of the research seems to have started around the 2023 period.** And then suddenly most of it vanishes. I'm not sure why; I think that's just a data issue. So let me take a one-year period because I suspect that the data is at an annual level. So, 2022, not much research happening. 2023, they start doing research in this space, whatever this is.

**Anand**: [22:30] **Artificial Intelligence, Chat GPT... in other words, a lot of their research that started in 2023 was triggered by Chat GPT.** That is what seems to be on the left side. 2024, this area has strengthened, but they also seem to have a decent amount of research in, for instance, safety in civil, some amount of research in remote sensing, some amount of research here in composites in materials science, and so on.

**Anand**: [23:00] And out here... probably data was not complete, but the research in the same areas continued. So a few things are clear. **There does not seem to be any research, for instance, in Mathematics.** There does not seem to be any research in Medicine. There does not seem to be much research on chemical science, and so on. Fine, we get a map of where they are.

**Anand**: [23:28] But the next opportunity is **how can we use this to figure out how the space is moving and how they can evolve in this space?** So what we did was took each of these fields. The X-axis and the Y-axis are the two principal components roughly—they're the UMAP components, but it's more or less the same thing. We took Mathematics as a field and asked: take all the Mathematics papers in 2021, on average where are they? All the Mathematics papers in '22, '23, '24, '25. **And it seems that Mathematics is clearly moving, whereas Engineering is not.** Medicine kind of had a big blip but hasn't net moved that much. Chemistry hasn't moved that much.

**Anand**: [24:23] Okay, so Mathematics is moving a lot. Fine. Where is it moving? How is it moving? What do these axes mean? That brings us to the interpretation of the axes. That’s possibly manual work. We again asked AI to interpret it for us and tell us what are the best options, have somebody validate it. And it said, look, **the left axis or left side seems to be more AI, vision, perception related. The right side seems to be more materials, energy, devices related.** Those are the two differentiators of this axis. Y-axis seems to be equations and formal systems.

---

**Anand**: [00:01] ...formal systems. On the top, it seems to be living systems, biology. Okay, so more deep mathematics versus more biology. **So in 2021, there was a lot of focus in Mathematics on the biology side. That seems to have moved significantly away from the biology side towards equations and formal systems.**

**Anand**: [00:23] And they figured out why this was happening. **Reason number one is Covid. At which point there was a lot of research going into anything biological, and Mathematics was moving in that direction as well.** A lot of papers were getting published in that direction. And AI is the second trend, which is what is moving it downwards. So two forces that are moving it downwards.

**Anand**: [00:46] Which helps them because now that they know the direction it’s going in, and Mathematics was one of those areas they were considering starting to write papers on but they haven't yet, they said, "Okay, what this means is formal systems seems to be a white space that we can target and incorporate into our strategy."

**Anand**: [01:03] For other engineering, chemistry, we had other similar conclusions. But what that led to was a data story where we were effectively saying, look, here's how your department’s papers are moving. So in EEE, you’re moving in this way; Physics, Chemistry, etc.—each of your subjects is moving in a certain direction. And what you should do, therefore, is start factoring in where exactly these are in the space.

**Anand**: [01:34] I’m not going into the details, but also there was a list of who is writing papers in similar areas to the papers that you are writing in. So it turns out that, for instance, **even within their departments, Ramya Jayachandran in the ECE department is writing papers that overlap a lot with the Mechanical Engineering papers of Imran Jamadar. Why don't you collaborate and write a paper? That starts giving you more ideas because they’re already overlapping.**

**Anand**: [02:04] Or Ashok from ECE and Vinod Kumar from Mech—your papers seem fairly similar. Why don't you start collaborating and writing towards this? Especially because in each of these cases, it was also saying one of you is more towards where the industry is heading—the research is heading—in the first place.

**Anand**: [02:27] Not just that, it was also able to identify where to collaborate. So, for instance, one area that you probably want to write about is catalytic materials and green chemistry because there’s a gap, there’s a growth in citations, etc. And here are some of the external institutions that are already working in this area. And how do we know this? Because the oranges, where you are, overlap with some of the blue papers that were in the background. And these are the institutions that are writing those blue papers.

**Anand**: [02:59] **So reach out to the Chinese Academy of Sciences, [inaudible name], [inaudible name], somebody Zhang. And now you have a list of names and universities that you can start reaching out to, which makes it ultra-actionable.**

**Anand**: [03:22] So now they have a clear plan of action. **Number one: my objective is to increase the NIRF ratings. To do that, my biggest lever is research papers. To do that, I need to identify where the gaps are and how the industry is moving, which we are able to see. Second, who I should collaborate with, both internally and externally.**

**Anand**: [03:47] And how is all of this happening? Just two things. One, these are the embeddings. But second, we are also able to interpret by creating factors—how exactly the industry is moving and who's similar to each other. That is an example.

**Anand**: [04:02] So at this point, I’m going to stop yakking around. And let's take... okay, yeah, I have one more that I can yak around, but let's ignore that. We have a survey. You are going to be playing around with surveys. A significant portion of this course is teaching you the theory of how to analyze them. Let me approach it from a different perspective.

**Anand**: [04:31] I have some data. I kind of know what the survey was about because I read the survey questions, but I did not create this survey. **This survey was created entirely by Claude, which I prompted late last night with the professor's email saying this is the session, all of the details about it. And I said, "Look, in the class, I want to run a survey and I want to analyze the survey and give me the survey details."**

**Anand**: [05:00] It also knows why it has asked for all of these. **Every question that you have filled out, it has a reason for asking. I do not know the reason.** This is the exact opposite perspective from what you’re doing, which is intentionally solving a problem. I’m saying unintentionally solving a problem—but the problem gets solved if you can solve it.

**Anand**: [05:25] Let's try it. So here's what I’m going to do. First, I’m going to go to ChatGPT. Why ChatGPT? Because I’m going to dictate. Why not dictate to Claude? ChatGPT’s dictation is better. I’m uploading the survey results for the form that you had given me, but I’ve made some changes to the form, so I’m also uploading the actual form that I used.

**Anand**: [05:56] **"What I want you to do is use the data analytics skill and tell me the most powerful insights. Also use the meeting readout style because I’m in the middle of a workshop and want to give a readout concisely explaining the top insights that are coming out of it."**

**Anand**: [06:16] There are three things that I’m doing here that I will flag off in a short while. Let me now go into this. "I will also add: keep in mind that I want you to demonstrate the power of the analytical techniques this class covers—this course covers, whatever." And let's upload two things. Number one... the form... the responses... yeah, these are the responses and this is the form itself. Great. And it's going to churn.

**Anand**: [07:07] What are the three things that I want to flag off? **Number one: dictation. Dictation is like a superpower. We don't... we’re not trained on dictation.** There used to be a time where people had assistants to whom they would dictate and stenographers would note this down. And then people started using word processors, desktop publishing, self-publishing, and that habit vanished.

**Anand**: [07:33] **But it is a remarkably powerful thing because when we are typing, our ability to think reduces a little bit. When we are speaking, we are able to brainstorm and come up with stuff on the fly, and it is a skill that needs learning.** With AI, we have stenographers in our pockets, so we might as well dictate. If nothing else, you’ll be learning a different style of thinking. And a different style of thinking gives you results which are very useful. Practice dictation. Don't have to only use dictation, but practice it itself, see the gap.

**Anand**: [08:06] **The second is recognizing that there is an alternate way to analysis. One approach is purpose-driven analysis: I have an objective, I want to solve it using data. The other is data-driven: I have some data, I want to do something useful with it.**

**Anand**: [08:31] The second approach has been around for some time, ever since the entire Big Data revolution. In fact, we did a whole project for Star TV on how they could just take their data and what use cases we can create for it. But with AI coming in, we now have a revolutionary leap in this capability. **Because we can just tell AI, "I have this data, you figure out interesting stuff out of it." As long as it is, for instance, going to make me money, I’m happy. As long as it is going to make me famous, I’m happy.** Whatever your objective is, give it that broad direction.

**Anand**: [09:07] **Third, the use of skills. I’ve mentioned "use my data analytics skill" and the "readout concise meeting readout response style."** What I’ve done is over the last few weeks, months, whatever—years in some cases—taken everything I know about a professional topic and said, "Here is how I do stuff."

**Anand**: [09:34] For example, data analysis. I’ve been doing data analysis for almost a couple of decades now. And all that I teach my team, I’ve condensed that into a two-to-three-page document that says, "Here is how you do data analysis if you want to maximize the insights that come out of it." Different people have different analysis styles like this, but what I find is that this gives me the kind of analysis that I want.

**Anand**: [09:59] Second, meeting readout. I find that this thing talks too much, and I can't make head or tail out of what it’s saying half the time. So I’ve spent some time creating a meeting readout response style. "Look, I’m in a meeting. I just want to read out what you’re saying. Here is how you should write it so that I can at one glance figure out what you’re saying and be able to read it out, and it will make sense to me and the other person."

**Anand**: [10:25] **In other words, what we’re doing is codifying what we know as a skill and what we want as a skill, both intent and ability, into a set of prompts that we can releverage.** All the popular AI engines come with it; they're called "system prompts." Store it in Notepad, copy-paste whenever you want. All internal engines are doing the same thing as for copy-paste.

**Anand**: [10:52] And this is running the stuff. And we come to how it's come out with the answers. But let's see. Okay, it's saying, "**I misjudged the room badly.**" Oh, "you misjudged your own room badly." Okay, this is what it has to tell me. Fine. "**Looks like you misjudged this room very badly. On average, you guessed that 70% of you would let the AI run most of your work unchecked. Turns out that you as a group will only let AI run unchecked 26%.**"

**Anand**: [11:30] Implication: that you think that everyone else will just happily use AI, but in fact, you only use it 25%. You roughly think that people will let AI run without verification three times more than yourself. Which is interesting. Factor that in, and this is a reasonably common observation that I’ve seen. Most people feel that they are a little more conservative about AI and others are not as conservative or as responsible about the use of AI, which when averaged inevitably more or less ends up being the same.

**Anand**: [12:09] **Everyone of you, in other words, thought that you were the careful one and everyone else was reckless. You're wrong about each other.** This is the survey result. The crowd is bad at reading the crowd. "**Only one in four of you caught the AI's mistake and correctly did say so.**" Interesting.

**Anand**: [12:26] So there was one question where you had to critique the AI. And the correct answer is that... okay, in case you want to see the question—even if you don't, because I don't remember the question... [Laughter] [01:24:41.00] **It's the assumption of normal distribution.**

**Anand**: [12:42] Exactly. So it’s saying we ran the model assuming a normal distribution of monthly income. Supposing AI says that, what should be your critique? And **since income is usually right-skewed, normality may not apply is the biggest critique or best critique.** Not that the others are not valid, but this is the strongest one. Why that, you will go figure out whatever, but one in four of you caught that. And only one in four of you caught that.

**Anand**: [13:14] **Which means that most of you are, when you're validating AI, perhaps not at the level where you know where it’s going wrong.** Which is fine, we spoke of the various ways in which you can figure out where the AI is going wrong even when you don't know where it’s going wrong. But keep this number in mind.

**Anand**: [13:42] **In something like Statistics, which you are studying, where you will likely be delegating the work to AI, this is the kind of thing which you will not be able to catch.** And you need to know what are the kinds of things you don't know how to catch and what are the ways around it. And therefore, yeah, catching what is wrong is a skill.

**Anand**: [14:04] "**People who trust AI the most are the worst at checking it.**" Okay. "**People who trust AI caught the flaw 11%. People who didn't trust AI are catching it 26%.**" Interesting. So as a rough rule of thumb, **the more favorable you are to AI, the less critical you are about AI. Watch that out.** Being favorable towards AI is not a bad thing; it will encourage you towards higher use. It will also end up leading to higher mistakes, disproportionately higher mistakes because this is a percentage. Watch out for that.

**Anand**: [14:43] Okay, "**clustering found two of you in this room.**" Okay. "**One tribe nailed the base rate, one tribe fell for it.**" Okay. "**The math sorted you on its own**"—I have no idea what this is—"**and notice what clustering did.**" Okay, so I better ask it what on earth did you mean by that clustering thing you said. "Explain it in simple language, please." That is one thing that I would have to clarify later.

**Anand**: [15:13] "**There is no single AI-savviness score.**" Okay. So principal component analysis couldn't find one main axis. **Being good at one kind of error told me almost nothing about another.** Which is interesting. So the errors seem to have no pattern of correlation in terms of what you’re catching. Implication: don't trust anyone who sells you one number for how good someone is with AI. Ah, that is interesting.

**Anand**: [15:41] **Takeaway is there are different ways in which we might make errors with AI; it's hard to condense it into a single number.** And with sixty-plus of you, this is probably reasonably statistically significant, but I will double-check that later on. And then some stuff on this.

**Anand**: [16:01] Now, how did it go about doing this? It view two files and blah blah blah script. Okay, now notice this bit. Here it is writing Python code to analyze the data. If you happen to understand Python, fine; if not, Python is a moderately readable language—please glance through it. It seems to be doing something from collections, it is opening a responses file... oh, that vanished. So I will go back and... yeah.

**Anand**: [16:42] And then it is computing the question-answer, it is... okay, there seems to be a distribution, "dist of Q," it is computing some distribution and doing some counting. Okay, so far it is just doing the counting. Then parsing the text, the free-text base rate answers. It’s written a script to do something else. Wisdom of crowds, predicted versus actual—it is doing something. No idea what it is doing.

**Anand**: [17:17] Show more. Okay, correlations here and it seems to have loaded a statistics package. And somewhere I believe it will be doing the correlation calculation. Yeah, here's where it’s doing the correlation coefficient and coming up with the results and so on.

**Anand**: [17:39] Now here's the thing. I don't know what it’s doing. **If it is correct, I don't have a problem. If it is wrong, I need to know. Even if it is correct, I need to be able to explain what it’s done. So what are our options? What do you suggest?** [pause] Yes, please?

**Unsure**: [18:08] [inaudible] data to go to another agent and ask to cross-check, for example.

**Anand**: [18:13] We can give the output to another agent and have it cross-checked. Great. How can I understand what it’s doing?

**Unsure**: [18:18] You could use the agent itself, ask it to explain it, tell it... in simpler terms that you can understand. If it doesn't give the output, maybe you give a reference of the output that you're expecting.

**Anand**: [18:30] Good point. Let us do both. So, for the second for those who are not able to hear is: ask the agent to explain what it did in a way that you can validate. So let me do both of these. And I will just take the easy route out.

**Anand**: [18:47] "**I will be presenting the analysis to an audience. I want you to explain to me in very simple terms what you did in a way that I can communicate to them. Second, I want you to go through your own analysis and find every single error. The more errors you find, the better the outcome is for me.**"

**Anand**: [19:09] Now this is a slightly stronger version of Henry Kissinger's "Is this your best work?" Effectively telling it, "Look, I know this cannot possibly be your best; I know there are errors here. Are you able to spot the errors?" The intern will happily go and... unhappily go and still find out the errors because Kissinger has told him that there are errors. These things are very eager to please.

**Anand**: [19:36] So, but before that... oh, okay, fine. He caught me hand-waving what clustering is. Okay, that I know. Okay, so when I said "clustering formed two tribes," I meant I handed the machine everyone as a row of numbers and asked it to find bunches. Okay, and it drew a line between the base rate catchers and the base rate missers. So some people understood... okay, got it, and some people missed... okay. But I picked the three and blah blah blah, so it went... No, I still didn't understand it.

**Anand**: [20:20] Which happens all the time—part of the time. Okay, 20% of the time I find that the explanation is nowhere near enough or clear enough for me. **What do you do in that case? One of the most important techniques that you have to learn is to give up.**

**Anand**: [20:41] When some stuff is hard and other stuff is very easy, who cares? I didn't have an objective in the first place; I just wanted interesting stuff. It gave me four interesting things and one thing that I don't understand head or tail of. Ignore it. Yes, please?

**Unsure**: [21:00] What if you then tell them to take those three things in simple terms and as a story and as a chart what they are?

**Anand**: [21:06] Absolutely. We can ask it to explain in a simple form as a story. That’s what I thought I had told it, and it’s still complicated. But arguably what I’m going to do tonight is go back and find out what it is that made it give me such a poor answer. How can I improve my prompting? That is how I improve my agent management skills.

**Anand**: [21:31] But in this situation, I have other things to do. I’m just going to drop it because the cost is negligible. And I will tell it to find five more insights. **I see these as complementary approaches: purpose-driven analysis, data-driven analysis. Purpose-driven analysis gets you to an outcome you want, you know, you plan. Data-driven analysis gets you to something interesting that you do not know about and it is a discovery. AI can be used in both.**

**Anand**: [22:01] **With data-driven analysis, one of the advantages is that because the generation is cheap and the outcome is unspecified, you can create lots of them. Pick what works, drop what doesn't. Don't waste your time.**

**Anand**: [22:17] And a big part of running this in parallel is that it takes very little effort. It is doing the work; you’re not doing the work. Don't try and do the work. **Increasingly, the term that is being applied for this is "loop engineering." Earlier, the term that people applied was "human-in-the-loop." AI can make mistakes, put a human in.**

**Anand**: [22:42] **What happened? We found that AI can generate so much volume, and that has economic value, that the human-in-the-loop was getting overwhelmed. So we changed the system a bit.** We said what we'll do is try and build deterministic tests; we will have another AI check it, etc. So the human is not in the loop monitoring, but there's an AI in the loop and the human is monitoring the loop. And it’s called **"human-on-the-loop."**

**Anand**: [23:06] So what I’m going to do is see if it is generating fine, it is being verified okay. Is the verifier flagging off something that I should review? I will review the exceptions. So that means that if the verifier is catching maybe 10% of the things that need to be reviewed by me, I’m the human-on-the-loop monitoring the loop.

**Anand**: [23:26] Then we found that this cycle has so much economic value that the amount of stuff that we’re doing with this has expanded like crazy. **So now we’re getting into "loop engineering," which is: let the agent come up with the loop. You generate, you figure out how to verify, you verify, and you keep monitoring if the system is doing well, not doing well, continuously improve yourself.** What I will do is see if you are doing a continuous improvement properly. We're in the early stages of this, still not quite there, but you’re seeing the pattern.

**Anand**: [24:03] We are increasingly moving ourselves from the loop, so to speak. Because generation has become cheap, and what is cheap and lowers cost increases the return on investment. When it increases the return on investment, volume will likely increase, which means that the human effort ends up becoming more expensive.

**Anand**: [24:23] What is the last bit that it is saying? Every error that it can find. Let's start with this. "**The headline sheet claimed it is basically five people. I told you high-trust folks caught the error blah blah blah. In real counts, that is two out of eighteen versus seven out of twenty-seven.**"

**Anand**: [24:50] In other words, the significance of this is not very high. So if it were a larger audience, it could be more confident. With a smaller audience, it needs to be less confident... [Audio ends]

---

**Anand**: [00:00] With a smaller audience, it needs to be less confident. Good. So I would want to run this on a larger group. I silently coded the non-answers as failures. Nine people skipped the disease question in clustering. I coded everyone of them—that's not an answer, blah, blah, blah. Some other mistakes. Clustering was oversold and so on.

**Anand**: [00:22] Put another way, it has managed to catch a bunch of errors. **If I were a human-in-the-loop, I would go through all of these. If I’m a human-on-the-loop, I would say, "Plus, you caught your errors; now fix them."** Let's do that. "**Since you have caught your errors, rerun, fixing them. Give me the final result. Use a meeting response type and tell me how you did it and what the insight is.**" And let it run.

**Anand**: [00:58] The fact that you can do this live in a session, or in a meeting, or wherever, means that the scope of what you can do has expanded considerably. You can do this literally in a class, or in an exam, or in a project, wherever. And with that, let's go back to how AI can help with the purpose-driven side of things.

**Anand**: [01:21] You're running a project, you have a survey. You tell it to do a concordant analysis; it will do the concordant analysis. Especially because it's going to be writing a script. Now you may need to present that script as part of the project. **Tell it to write it in R. Take the script out, run it, verify it, see if you’re getting the same results. See if the script does what you expected it to do. Give it the feedback.**

**Anand**: [01:46] Put another way, at the very least you’ve gained an assistant who can write your code for you. Or you write the code, have it verify. **You’ve gained an assistant that can cross-check, find the errors and the flaws. You’ve gained a brainstorming partner.** You can ask it what are other interesting ideas that I can do with this.

**Anand**: [02:08] That last bit is actually particularly powerful. And let me tell you the story behind that. Remember I had said for a waste management company, Tanuj had created this invoice line categorization? The way this came about was not because he said, "I want to do invoice categorization." I told him, "Tanuj, why don't you find out what AI can do?" He said, "Anand, we don't have notebooks, we don't have product code, we’re not allowed to use Gemini, what do we do?" "Okay, what are you allowed to use?" He said, "Snowflake, and within that there is Cortex." "Okay, use it. It has all the data. Let us use the **data-driven discovery approach**."

**Anand**: [02:52] Feed it all the documents about the client. Feed it all the files, emails, whatever that you have. Ask it to find the use cases. And that is what he started with. He got Cortex to generate a slide deck, an HTML slide deck, which listed out fifteen use cases. He then took it to the head of analytics, Cap. Cap looked at this and said, "**Tanuj, in November we did a strategic consulting exercise. Fairly expensive, one month, three months, and at the end of it we got a set of use cases. 80% of that matches with this.**"

**Anand**: [03:31] **In other words, 80% of the value of an expensive strategic consulting exercise got into him being able to do just like that.** How long did it take Tanuj to do this? For him, okay, he had to find the documents, upload it. It took him about half a day to collect all of it and then make a few iterations, telling it "Don't do this, no no no, this is not right, I forgot to give you this document," etc. Half a day.

**Anand**: [04:02] So then he said, "Anand, now what I’m going to do is write a proposal for each one of these." And he went ahead and wrote a proposal saying, "We will do revenue forecasting for you, this is the something, this is the approach that we will be using for revenue forecasting. We can get all of this done in just four to eight weeks lead time," etc. Why? Because that is how he is used to doing purpose-driven analysis. "I have an objective, I know how to set up a team that does any kind of data science work, get the job done. This is typically how long it takes."

**Anand**: [04:36] I said, "Okay, look. If you're doing purpose-driven analysis the traditional way, this makes sense. But if you’re doing it in an AI-driven way, why don't we try something else? You put together how long it will take for each of these, but you're not going to be doing it. AI is going to be doing it. Why don't you just tell it to do all of it? Just come up with the answer."

**Anand**: [04:58] Tanuj was a little taken aback, but went ahead and finished all of those in a week. **Fifteen use cases, every single one of them. All he did was put the first use case and said "solve this," do the second use case and "solve this."** And that was how that invoice generation was identified. That's not the only one. He found some pricing anomalies. And then we had it write the whole thing as an email.

**Anand**: [05:25] For instance, this is an email that actually went to the client. Among other things, it says, "**There are 105,000 transactions which are charging the client 16 cents. Your waste management service costs between $175 to $179.** What is this? Either this is a data error—in which case we need to do massive cleanup—or you are leaking money like crazy."

**Anand**: [05:51] "Or, there are 84,000 transactions where customers are paying 6 to 14 times the median rate. This is an even worse kind of a problem. If they find out that they're paying some crazy amount, how long do you think they will last? We need to fix this." And how did we find this? How can we do this? What are the next steps? "**Look, let's build an anomaly model for each of these. Let's identify who these 90k people are. These are the people that we need to reach out to.**" The entire set of next steps ended up getting the result.

**Anand**: [06:21] Why am I sharing this? **The first part was effectively AI acting as a brainstorming partner.** He already had the data sitting in the database and was able to tell the model, "This is the broad business objective, this is the context of the company, now you play around with the data and see what you can find." Which worked.

**Anand**: [06:42] Let's try the same thing now. What I’m going to do is pass you this data anonymized. And let's see what you are able to come up with that is insightful. Same data, applying the principles that you’ve learned in the class so far and principles that you’ve not learned so far. So let's go to ChatGPT and let's take...

**Anand**: [07:05] "**I want you to give me an anonymized version of the responses file. Don't change anything other than removing the columns that have any personally identifiable information like name, email, or whatever. But make sure that it still has all of the information that will be required to do the actual analysis.**" And have it give the data.

**Anand**: [07:29] Now, normally it's just deleting two columns. I can open Excel, delete those two columns. But **what I don't know is what I don't know. If I had applied my brain, I’m only applying my brain. By doing this and giving it clear instructions on what needs to be done, I can always cross-check.** "Hey, it’s okay, it deleted these two columns and nothing else, great." That's a validation. But am I missing something? Is there, for instance, one of those text fields where somebody has put in their name or some other personally identifiable information? This can catch that. That is its job.

**Anand**: [08:08] So put another way—and this is a broad rule of thumb that I use—**always bring AI to the table. You don't lose much. It's practically a free 1000 PhDs sitting in your pocket.** Why not use it? As a cross-check.

**Anand**: [08:24] So put another way, one is to say I will use AI as the **source**: let it do the work, delegating entirely and stepping back. That is one extreme. The other is I will use it as a **partner**: whether it's for brainstorming, whether it's for verification, or whether it verifies... whether I use it for verifying it or it does the work and I verify it or whatever. Third is as an **assistant**: which captures some of the routine tasks which I delegate—my small tasks, basic routine tasks—I don't want to sit and waste my time. It probably would have taken me 30 seconds of staring at the screen and deleting those two columns. Why waste 30 seconds?

**Anand**: [09:05] Here is the data set. And I will download this TSV file. I will place this in a folder that you can analyze. And let's see... I'll call this as responses.tsv. Sync the file. This part I can't delegate—I mean, I could, but it’ll take me very little time to get this done because I just need to synchronize it. This file is going to be available at files.s-anand.net/temp/responses.tsv.

**Anand**: [09:50] The objective... Yep. Yes, that came through. I will paste the link in... [Anand works at the computer, there is silence for a minute].

**Anand**: [11:15] That is the link. What I’d love for you to do is download that data and use AI to apply any of the survey analytic techniques that we’ve been exploring. **Find something interesting about this class and share it to the group.**

**Anand**: [11:41] What we're effectively getting to here is: it's possible in a session to create a survey technically—because I didn't really spend that much time with Claude to create the survey—execute the survey—most of you have filled this out—analyze the survey and get insights. And you can very easily get to the point where you are presenting it as slides because all you do is tell the AI system to create slides. In other words, it's like a mini-project done end-to-end in, well, two hours forty-five minutes so far, including the break. [Silence for several minutes as students work].

**Anand**: [13:52] Once you start getting any insights that you are comfortable with, please do share. Just look at the screen. [More silence as students work].

**Anand**: [14:13] Yes, please?

**Unsure**: [14:14] We found there is a "skepticism paradox," that low-trust users—people who say "I don't trust AI"—end up using more AI tools in general.

**Anand**: [14:26] Let's try and cross-validate. How do you cross-validate? Upload this into another chat and type what he's saying and ask it to find the errors in that. I would also like people to find the flaws in this. Please share one insight at a time.

**Unsure**: [15:01] So the numbers find that highly skeptical users are some people who think that they don't trust AI, and end up using more AI tools in general. So the people who said they use AI daily, they don't trust it as much as the others.

**Anand**: [15:22] **People who don't trust AI use more AI. Interesting.** I would love for people to find out whether that is (a) correct, (b) statistically significant. Any other insight you can find? And I'll repeat that statement, which is: **people who use more AI are more skeptical of AI.**

**Anand**: [15:46] Great, and that's a great insight. If that turns out to be true, right, people who use it more are more skeptical? Now, what that means interpretation-wise is up to us. We could say, "**Because they're using it more, they understand all the problems.**" Possible interpretation. Or, "**Even though they’re using it more, they don't have as strong an awareness of how deeply they are into it.**" Also a possible interpretation. You need a further second-order question to figure out the "why." But that would be an insight. Any other insights or a counter to this? Yes?

**Unsure**: [16:24] The other insight that I got was a projection bias, which is people who say "I verify every step myself" also rate lower that people in general would be using AI to... which was 45%. Whereas if somebody is using AI 100% end-to-end, then their estimate of other children is 80%. So **my estimate of how much people use AI is directly proportional to how much I use.**

**Anand**: [16:54] Got it. Interesting. So let me play that back. What you're saying is: **people who say they are using AI a lot also say others are using AI a lot.** And those two are correlated. Okay, good. Love for people to falsify this hypothesis. People who use AI a lot also say that other people use AI a lot. That it is correlated—the regression is positive slope, however you want to frame it.

**Anand**: [17:26] Is this correct? Is this statistically significant? And I think we should just pause to see if anyone has any results on the falsifications, on the validations. If not, I'll run one. Let me run one. I will just take the same exercise and ask ChatGPT. "**Is it true and statistically significant that the people who say they use AI a lot also say that others use AI a lot?**" Is that the correct framing? Got it. Let's run this. We don't need extra thinking for this; I will just change it to 4.0 High and run that.

**Anand**: [18:18] While that cross-checking is going on, any other insights that came out? This insight, by the way, did not come out when I ran it. So this is net new. Any other insights that came out? And also, is anyone trying to run any kind of classification analysis on this? Is anyone trying to run any principal component analysis on this?

**Anand**: [18:45] Okay, it's saying that survey never asked how much others use AI.

**Unsure**: [18:54] There was one question about what percentage of the class you think uses AI...

**Anand**: [19:01] No...

**Unsure**: [19:04] There was one question like that. What percentage of the class will pick 75 or 100 on the trust question.

**Anand**: [19:08] And therefore, one of the gaps is I didn't pass it or you the questions themselves, which of course you could copy-paste from the form, I assume that was an option. But let me now give you the questions so that you can pass it to AI and see if it can cross-check. The file will get saved. I will tell you the link. responses-questions.tsv. Sync the file. Take a look. This second file is the set of questions that were asked.

**Anand**: [20:02] To be fair, it should have known the set of questions because there's a column name. So I don't believe that there could have been a problem. But looking at the actual questions: "**How often do you use AI?**" "**Which of these have you used in the last month?**" etc. But what we're asking about other people is, "**What percentage of the class do you think will pick above 75% or 100% on the headline trust question?**" The trust question is whether you will let it run unsupervised.

**Anand**: [20:48] Now, take a close look. **Is this a gap in the AI's response or your interpretation of the response? Both of these are useful inputs.** Because if you think AI made a mistake, then we have found a new pattern of hallucination. Usually, I find that modern AIs don't hallucinate at this level. But as you saw me fumble with its response, it's entirely possible that we don't necessarily understand what it’s saying and it's become more complicated. That seems to be the bigger issue right now.

**Anand**: [21:21] Two ways of interpreting this. One is to say, therefore, we need to make sure that we understand it better. The other is to say we need to engineer a system so that humans don't even need to understand—it directly takes actions. Which ultimately will leave humans free to do other stuff. Neither of these is invalid. On a case-to-case basis, we need to carefully evaluate which is the right direction to go. Any other insights that came out? [Silence].

**Anand**: [22:07] But again, I’m curious if either PCA or classification or clustering is something you’ve figured out. And what were your learnings from that? [More silence as students continue to work].

**Anand**: [23:07] Yes?

**Unsure**: [23:08] My interpretation and AI, both were wrong. So what it did was the variable name was "predict_room" in the responses, and from that it picked up that this is a "room session."

**Anand**: [23:18] Good point. I did therefore the mistake, not the AI, it was mine. I didn't give you enough data. Fair point. Okay. And now with the revised analysis, what is it saying?

**Unsure**: [23:28] It's saying the same thing. After picking up that... so there are six people who have chosen 100%, and okay, their estimate says—average is 80%—that what percentage of class will be relying 75% or 100%. So their average is 80% compared to the rest of the 60 people who might be using, say, 50% AI themselves, and they also think that the rest of the class also uses around 50%.

**Anand**: [23:49] I didn't understand that.

**Unsure**: [23:51] So there are six people who have said we use 100% AI. And their response to the question "Then what percentage of the class do you think is also using 100% AI?" Their response is 80%. They think that 80% of the class is completely dependent on AI, and they are also completely dependent on AI themselves. Compared to, let's say, the remaining data, which is 60 people. They might be using, say, 50% AI themselves, and they also think that the rest of the class also uses around 50%.

**Anand**: [24:27] Still didn't get it. And let me propose that you explain it as an observation about this class without referring to the numbers.

**Unsure**: [24:41] I would say **people who use AI a lot also think that others are heavily dependent on AI.**

**Anand**: [24:52] **Heavily dependent on it. Got it.** Let's try that phrasing. "Use AI a lot, also say that others are heavily dependent on AI." [Audio ends].

---

**Anand**: [04:02] **There are two possibilities. One, is there an interpretation gap? And the other is, are the numbers actually correct?** Because we saw earlier that it's not very likely that two models will make the same mistake the same way. Cross-checking once is something that I’m reasonably comfortable with. Cross-checking twice is ultra-careful.

**Anand**: [04:46] The link points are where you'd expect. Heavier users guess a bit higher for the room, and it isn't statistically significant. So it could be a chance... interesting... so it's saying the opposite of what I thought. I said people who say they use AI a lot also say others are heavily dependent on AI. Is it true? It's saying no. Oh, sorry, sorry, no... I misunderstood... correct. It is saying it is significant, but there are only six responses. Directionally right, but P is equal to 0.2, not statistically significant. Okay. 0.2 I can live with for this audience. We've done another test to be ultra-sure, but it's not a bad correlation for something as subjective as this.

**Anand**: [06:33] The last one is very interesting, about saying "because" or "why" it is so. Ah, 59 of the 67 are daily users, so nobody is using it light to compare to. That's a very good point. So yeah, this is pretty weak, but directionally a possible thing worth a further experiment to test. Yes, that is a fair point. Any other insights that came up?

**Unsure**: [07:12] We found another insight. For example, there's a question of what type of AI agents you use, and there's a question for those respondents: "How do you check if the AI's data output is actually valid?" So basically, for people who just use non-specialized coding agents like ChatGPT, most of them feel that the results are statistically significant and they accept it. But for the people who actually use specialized coding agents, they don't trust the data. So they feel that there's a lot of data nuances which the AI is not capturing. So basically, the insight is like, if you are not using the coding agents, then you are not [inaudible].

**Anand**: [08:00] Let me frame this. "**Is it true and statistically significant that the people who are not using AI coding agents don't trust AI models a lot?**" Let's verify that. And if that is the case, again, that is a very interesting result. As we use AI coding agents, possibly our trust grows because it's a bit more advanced...

**Unsure**: [08:31] No, no... I'm saying they don't trust it because it's non-specialized [inaudible].

**Anand**: [08:44] Oh, I framed it the other way. I’m saying people who are not using AI coding agents don't trust AI models.

**Unsure**: [08:52] No, the people who are not using AI agents trust it a lot because they are not deep into the data working. When they are, they actually know the nuances that are missing.

**Anand**: [09:03] Got it. **I'm saying that they trust AI almost identically. So there's no difference. This does not seem to be the case.** Let's... why don't you feed it back, saying another model said that for the two groups, the results are almost nearly identical. And how did you come up with your result, or am I interpreting it differently? Cross-check. And this is something that we can do with people as well. Me in front of a model, another person in front of another model. You tell me what insight you find, I tell you what insights I find. You cross-check mine, I cross-check yours. **Good way of doing pair programming or adversarial red-teaming, depending on which context you’re taking this in.**

**Anand**: [09:47] **Because the speed at which you can do this now becomes much, much higher.** We are not very good at critiquing our own work, we're not particularly good at critiquing AI either, but we seem to be reasonably good at critiquing each other as people. So AI can serve as an assistant, and we can cross-verify that.

**Anand**: [10:07] While we continue this, in the last ten minutes, there are two questions that I would like you to fill out in this form please. The survey... yeah. Same link, forms.s-anand.net. I've added two very simple questions at the end. Just fill those out, and I'll share an email with some analysis on those questions. Your email ID is anyway captured on the form.

**Anand**: [10:48] It's a controlled experiment that I’m trying out. One of the questions is just asking you for a random word. Just enter some random word. It'll be interesting to see how random your random words are. Just think of a random word. Don't use AI for this; just one word, whatever word pops into your mind, and put that in. Let's see how this performs and what we can learn from that.

**Anand**: [11:15] One more question. The idea, again, is just to see how we are thinking about AI. These are the two last questions on the form. Link is forms.s-anand.net. Just go right to the bottom, finish this sentence—fill in the blanks—and type any one random word. Question 11 and Question 12. Please give this a shot. Ah yeah, Question 11, please just follow the same pattern... Oh, no, no... sorry, I made a mistake... yeah, just finish the sentence.

**Unsure**: [12:11] [inaudible].

**Anand**: [12:15] **Whether hallucinations will completely vanish? Hallucinations have already reduced. And some hallucinations may be irreducible.** Supposing you ask, "Was Rajiv Gandhi a good Prime Minister?" I don't think there's any answer that some part of the world will say is not hallucinated. In other words, **subjectivity can be seen as hallucination.**

**Anand**: [12:47] Let's flip it around. Hallucination is creativity. **If I want a model to come up with powerful new ideas, the more diverse its thought process, the better it is.** So, (a) some hallucination may be unavoidable depending on how we define hallucination, (b) some hallucination we may want because we want it to think creatively.

**Anand**: [13:10] So I suspect that we will reduce what we call hallucinations in areas where we find it useful. It may not go down as much as we would like, but we'll have other mechanisms. And on the other hand, we will preserve some essential nature of hallucinations. What are the other ways in which we can reduce hallucinations? We just saw one. AI was not analyzing the numbers. It's not particularly excellent at doing mental math. It used to be terrible, now it's much better, but still not great. Instead, it is writing code. And if the code has an error, it is able to tell me and find the error because it doesn't even compile.

**Unsure**: [14:02] [inaudible].

**Anand**: [14:14] Got you. So the document had ten categories, ChatGPT said five, Claude said ten. **Hallucination has been greatly reduced.** If the document has ten categories that almost any human who looks at it will agree that it is ten, that kind of hallucination is steadily reduced. If it is a document where, when five humans look at it, some of them will say, "I think it has five categories," others will say, "I think it has ten," that kind of hallucination will not reduce much because we don't even know the answer. Why is that? Because we're training it based on our data. And it is reflecting human preferences in the majority of cases. And if humans are divided, AI will also be divided.

**Anand**: [15:06] Okay, I can see 31 out of 39 responses. We have four minutes to go. So please keep filling this up. If there are any other insights, I definitely want to take them. But otherwise, I'll just wrap up with some of the things that I believe are the most powerful takeaways in this AI world.

**Anand**: [15:33] **I find that using AI allows us a certain complementary way of working. Not better, not worse, just complementary.** And it's a useful skill to have in our pocket. One of these is to learn how to delegate to the AI. AI anyway can do a lot of things. What is the point of me learning what AI can do? So my approach is: **I will build skills in what AI cannot do.**

**Anand**: [16:02] How? Give every task to AI. What it cannot do, I will learn. And it happens by necessity. If it makes a mistake, okay, I have to learn that. If it's not even able to do it, I have to learn it. It cannot physically go talk to somebody? Okay, I will learn relationship skills. It can write the R code? Let it write the R code. Then I don't need to understand it. Fair.

**Anand**: [16:30] Where that need arises and AI cannot do your understanding for you, that becomes a skill you have to learn. But put another way: **there is merit in learning what AI cannot do rather than learning what AI can do.** That too is important. See if you can practice that. Number one.

**Anand**: [16:47] A second thing to keep in mind is that AI can be treated like people as a mental model. Which means that even in your entry-level job, you really have a management role. **You have, literally with every chat, a person who's reporting to you. Possibly much smarter than you, but still reporting to you, because you have the accountability, you have the ownership.**

**Anand**: [17:18] If that is the case, then learning how to manage a team of people or agents, how to organize them, how to feed one person's work to another, how to specify, how to give them work, how to give them feedback... you saw me struggling with the feedback—I couldn't get it to explain it in a way that was simple enough for me.

**Anand**: [17:39] Ethan Mollick, who's a professor of management at Wharton, writes a lot about use of AI. And what he finds is that **management skills are exactly the kind of skills that are enabling people to work better with AI.** You are therefore in that somewhat unique position. Use it.

**Anand**: [18:01] Third, as far as this course is concerned, what we were doing today—almost all of what we were doing today—was introducing you to a complementary way of working. An alternate approach to why the theoretical underpinnings of the course is what will help you understand what is happening. **Using AI will make you more efficient as long as you know how to use it well.** Learn that. Both will come in handy. You need to know how the fundamentals work. You need to know how to execute effectively. Give that a shot.

**Anand**: [18:33] All the best, and thank you for your time. [Applause].

**Prof. Shubhabrata Das**: [18:41] Thank you, Anand, very much. I’ll take a few minutes just to explain few things... okay. Thank you. And I think you summarized some of the things that they will realize back also. What we have been talking in the remaining eight sessions prior to this may seem completely different from what you saw today because of the pedagogy and the way it is.

Some part of it is because the examples and the context that he was doing are images, voices, use of the generative AI, etc. I cannot thank you enough. I always love when we move into classroom situations because I don't know how much you learn, but you learn a fair bit... I learn a lot. **And it is always something that we learn from complementary things.**

While the techniques, etc., at one level, there is a similarity there, our approaches to things are often quite different. And that, as an academician, helps me to question what I do and look at the outside world. I’m just going to take an example. He talked about something which is almost nothing to do with what we are doing, but it has everything to do with why we need to do it: that in a real-life problem, you have a problem that you want to solve, you go out and collect data through surveys, and then do whatever and try to find answers to it. And then he said, "No, no, no. I have the data, whatever it is, wherever it’s from. What is the most powerful thing that I can do with that data? As long as it sells, gives me money, and gets me fame, why not do it?"

That’s what he described to us. I kind of often go and say, "No, no, no. I don't care about the first approach for me is right." And if you remember when we are talking about the project, that's what I am saying: "Do something, a real problem, and try to find the best solution that you can come up with." They may seem completely two different things, and I’ll say when you look at high level, both are correct. You can see what the context is sometimes, what you need to do.

So my message is: look at it more carefully. And Anand has almost agreed to it—some things—so I'll modify this, how we want to do the project. He had volunteered, subject to finding his schedule etc., the final presentations he would join remotely and he would give his comments etc. on that part. So you would probably have real-life people. That’s what it will be.

For projects, so hence my mandate... so you'll understand, there are certain things in the techniques, etc., we talked about. I am asking you in the context, apply those, right? But there are other things which I am not talking about in the course. **If you are completely free and use any kind of technology that you feel will use that and incorporate in your project to deliver results, that's wonderful. And you have complete freedom to do that.**

Okay. Just a comment on the project part. So the only thing is that I will modify the deadlines for the submission of the presentation guidelines, so I can send it across to Anand so that he can have a look at it. And I’m sure all of you would not mind that, you know, whatever few hours we postpone.

One final comment is, if you look at the exercise, the data he collected and he was asking what kind of interesting questions that you come up with—being known as a hard taskmaster—so look at the questions that you all asked. There were interesting things, but actually they were all DS1, DS2 [Data Science 1 and 2] type questions. Univariate analysis questions, mostly. Correlation a little bit you brought in.

**But we did not see the multivariate analysis questions that you would ask, right?** So think about from that perspective, what could be additional things that you could do on that dataset which are core to multivariate data analysis. Remember what he said: "Of course, any dataset you have, first thing you’d look at is what can I do using any one of the questions or finding connections between the two, but **the heart of this course is how you can look at all the questions together.** What more can I generate that is beyond just the univariate and the bivariate analysis?" Right? So think in that direction. With that, I’ll close. Thank you. [Applause].

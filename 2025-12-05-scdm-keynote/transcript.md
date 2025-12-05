# Transcript

Thank you. Anand sends his apologies; whoever it was that was announced here sounds like a very impressive personality. I will instead try and do my best.

We are going to be talking about AI mostly and what it can do. It's something that you're all kind of familiar with. You've used ChatGPT, you've used Gemini, you've used Claude. You know how this works; it's not probably such a big deal.

**What we might be missing, however, is the pace at which things are moving.** And it is a crazy pace.

So, first, let me invite you to use that QR code for any questions that you may have during this session and right after this session. There's going to be a panel discussion, and you're very welcome to post your questions on this, and we will take it up as we go along. Please keep in mind that your questions will benefit not just you but others as well. And certainly me, because **what I'm curious about is what is it that you as an audience really want to know.**

But what we're going to talk about first is why Gen AI is different from the other revolutions. I think there are two things here that make Gen AI somewhat more different than the others.

The first is that so far in the last 50 years, we've been able to process **structured data**. Now we are able to process **voice**, we can talk to ChatGPT, we are able to process **images**, we are able to process **video**. Increasingly, we are able to process **human motions**, we are able to process **DNA**, we are able to process **proteins**. All of these, almost using the same kind of models. And that's fundamentally different.

Second, the way in which we are able to talk to it. And you will see this in a short while. We are able to converse with it to program. **So effectively, English has become the most popular programming language.** This has already happened. People are, without knowing it, programming. And you see some of this happening.

So, therefore, now **what AI can do is almost anything. Who can do it is almost anyone.** And that's where the power comes in.

But let's make this real. Let's say you are facing a day-to-day challenge. There is an informed consent form that you've received. You need to validate it. And there is a huge 68-page guideline that you need to go through. And this guideline has a whole series of what you can do, what you can't do. In any organization that let's say runs about 50 to 100 clinical trials across 20 to 50 sites, assuming that this review of 68 pages takes two to four hours, **it's going to cost you anywhere from half a million to two million dollars.**

That's a fair bit of cost. What if we just took that same ICD guideline and put it into ChatGPT? Which is what I'm going to do right now.

Let's take the following prompt, which I'll read out in a short while, against a specific informed consent form. So let's say this is for a double-blind placebo-controlled study of Glucofix, which is going to be a diabetes drug by BioPharm. It's about evaluating Glucofix compared with a placebo for such and such an age group, blah, blah, blah. So we'll take this and ask the question that I had posed:

> Validate this ICF against the guidelines at this particular link... attached... and list all the non-compliances.

And submit. How long do you think that might take? What's your guess? About a minute? Yeah, probably. Last time I ran it, it took about two and a half minutes, which is boring, so I'm not going to wait for that long. I'm going to just open the result that it showed.

And here is the result. It says:

> Here are the places where the ICF does not meet the addendum expectations.
>
> - Trial involves research is not stated clearly. It describes a study but never reveals that it's for research.
> - The subject responsibilities were not described.
> - The experimental aspects are not explained. It goes on and on and on and gives you about a dozen items that you need to look at.

Fair enough. You probably have done this. Sure. What is the point?

Here's the thing. **It's almost free capacity.** That, in terms of cost, was a few cents or less. In terms of time, was a few minutes, not a few hours. That's fair. And we ought to learn how to ask it the right question, the right way. That's kind of important. And we ought to know that it sometimes can make mistakes. That's important too.

But think about it. That is a massive economic force. **We are effectively getting something like free interns.** The cost at which they operate is one-hundredth, one-thousandth the cost of something at a comparable skill level at infinite capacity. That's where the power comes in. If we had that kind of capacity, do we even know what to do about it? The short answer is no. As an economy, we don't; we're trying to figure it out.

But let's push further. There is one challenge that we definitely need to address, which is: **What if it makes a mistake?**

And my response to that is: **Okay, don't humans make mistakes?** Ultimately, it's humans that are processing it. The kinds of mistakes we make vary. There are experts who do a really good job. There are people who do a terrible job. And we have processes for dealing with these. We have checklists, we have SOPs, we have reviews, we have audits. And all of these apply to these LLMs as well. **Meaning, you can just treat it like a human, like an intern, like a genie, like an employee.** It's exactly the same mental model.

To give you an example of how we might do that. Let's say we want to create a checklist. What we could do is just send Claude or Gemini or ChatGPT the file and say, "Now give me a checklist." And people are starting to create solutions around it.

So here's an example where we take the same document and ask this model to ingest it and create a series of rules that we need to check against. Effectively creating an SOP. And what it's done is document by document, it's processing it. It's processed the first document, it's now running the second document. And it's saying that based on my read of the document, one of the rules that you must check is that the sponsor must... that the monitor must submit written reports after the visit. It tells you what are all the rules a document says, and with the reason, and with the level of importance.

All we did here was know to ask that given a document, I want a checklist. And it provides it. Almost like a genie or an intern.

We can take that a step further. We can then say, now I have a bunch of ICFs to validate. Take all of these and I would actually like you to validate against all of these rules one by one. And tell me what the result is. And it's processing it. It's saying the first rule doesn't apply to this document. Second rule doesn't apply. This rule passes. And there are probably some failures that will appear. And it gives you a reason for each one of these. Again, like an intern who's practically running on this for free. And giving us a result saying that these are the ones that are applicable, these are the ones that passed.

For instance, the investigator's brochure must be on file pre-trial. That's valid because the informed consent form is documented and signed before the participation. We know that from the ICF and you can read that. So across all of this, we are in a position to not just run this document after document painstakingly.

But remember, it can make a mistake. So what happens if it makes a mistake? Well, if a human makes a mistake, we cross-check, don't we? We have someone else validate it. And if we apply that to Large Language Models, we are able to, in fact, find some fairly impressive results.

So one of the things that we tried was supposing we take a chat message like "Help registering" or "I don't know what I have to do to find the invoice" or "Could I take a quick look at my invoice" and try to see if a model can figure out which category it belongs to. So, "Could I take a quick look at my invoice?" is supposed to be in the "Get Invoice" category. But this model, GPT-4.1 Mini, put it in the wrong category. So it failed. In many other cases, it succeeded.

Now, **what if we took the results of one model, passed it to another model, and asked it to cross-check?** In other words, double-checking the results. What happens then is that **the default error rate of something like around 14% falls to about 3.5% with double checking.**

Now that increases the amount of manual work though, because if two models disagree, we still have to manually check it. Okay, fine. So we do. But the good part is that that only increases to 12.5%. We can triple check, quadruple check, quintuple check. If we have five models which still are practically free all cross-checking the work of each other, and if all of them agree, then we pass the result. The accuracy rate is 99.3%.

But if even one of them disagrees, we manually check. So that means that the amount of manual work that we do ends up being about 28%, **which is still a 72% reduction. So we effectively have scalable quality.** It's almost like a knob that we can control and say, "Yeah, I just want more quality. Give me more."

And it's stunningly cheap. The cost has been falling over time. The way we measure cost against quality is against two axes. The x-axis is the cost per million tokens. That's roughly saying if I took the entire King James Bible or the seven Harry Potter books and put it into an LLM and asked it to process it, how much would it cost? A dollar is what it typically costs today. And that varies from model to model.

The y-axis is the quality. The approximate way of thinking about it is: the lower end is a grade 8 student. The mid-range is a high school student, entry-level college student. The high end is close to a postgraduate, bordering on PhD-level intelligence. And we have models at that level. And these have been evolving rapidly.

So in March '23, for instance, Claude 1 was a model that cost about $8 per million tokens. And it was one of the better models at that time. November, just six months later, GPT-4 came in at $10. A very similar price but a significant jump from a grade 8 intelligence to beyond a grade 12 intelligence, almost a college-level intelligence. At roughly the same price.

But they started becoming cheaper. So if you go to November '24, a year later, that same level of intelligence—GPT-4 level intelligence—is available with Gemini Flash at **7.5 cents.** That's less than one-one-hundredth of the cost.

**Imagine somebody saying, "I'm going to do work for $40 an hour," coming back a year later and saying, "I'm going to work for 40 cents an hour."** You'd hire 100 people at the same cost. **That is the speed at which the cost has been falling.** And it's continuing. The quality has increased. So now we have even smarter interns, genies, whatever, coming at the same cost. And this is progressing at a pace that doesn't seem to be letting up.

So with that kind of progression—double checking, triple checking, quintuple checking, whatever—we can do anything. So what are some real things that we can do with this sort of capability? Let's take some examples.

Let's start with a fairly common scenario. Let's say we have a medical trial protocol, a document like this. And somewhere in the middle of this document is a table, the Schedule of Assessments. Now what we need to do is extract this and pass it into some software. Let's say this needs to go into RedCap.

Now RedCap accepts a specific format, an Instrument Event Mapping CSV format. I have no idea what that format is. You may have been doing it on a regular basis and therefore maybe doing it faster. But models have been trained on pretty much all of the world's intelligence. So all we have to do is take a prompt like:

> Extract this Schedule of Assessments table and put it into the RedCap format.

And give it to a model like ChatGPT. And let me just do that. Upload the file... and let it run.

Now the advantage of doing something like this is, at the very least, it serves as a **cross-check for the work a human has done**. It'll give a result. The human comes up with a result. Its result is free. Doing the cross-check is something that we can do deterministically. And if there are any differences, we cross-check.

But better yet, we can have it find all the errors and correct them itself. And it does a pretty good job at cross-checking it itself. Which I did just a few minutes before this talk. I uploaded the same file just to see what it does. And exactly the same prompt.

Here's the thing. It thought for two minutes and 57 seconds. And I'll come back to a bit of this. And it says here is the CSV. Below is the content which you can copy-paste into a CSV file. And this is in the RedCap format, which you can also download.

Then I said: **Find all the errors and correct them.** And it goes through diligently, about three and a half minutes of cross-checking. And the thinking that it goes through is actually pretty interesting. It's saying: _I'll use Python to open and read the PDF. I'm going to use Python to extract the text and write some code. And I'm going to list necessary corrections starting from source extraction._

So it's almost going through an internal checklist, thinking about how it should make corrections. And here are some corrections that it's made. It said:

- I used bogus invalid citations, which it removed. Okay, who cares if you made invalid citations? I never asked you for citations in the first place. That's okay.
- I assumed that the RedCap project should have two arms, Glucofix and Placebo, and it corrected the default to a single-arm longitudinal project. Okay, you thought it was this format, but you should have given it in this format. Again, still not quite an error of the kind that I was worried about.
- Instrument names were arbitrary abbreviations and it renamed the instruments to something that is more corresponding to my table. Okay, that's again more a convention, not an issue.
- And I said direct upload without warning about RedCap's exact name matching. Okay, I don't mind that you didn't warn.

Effectively, after a detailed review, it's found that on this relatively small and not very difficult data set, it hasn't made a mistake. And that has been my experience in the last three, four months. A year ago, I would have worried about models making mistakes in 100 lines, 150 lines. These days, I do not worry about it making mistakes in anything less than a thousand lines. And even then, it's not a problem. Because **it's actually writing programs to do this on the fly.**

Increasingly, models are not just treating themselves as language models. They're treating themselves as computing models that are capable of writing code on the fly, which I will illustrate through my next example.

Let's say we have a bunch of lab results. So we have lab listings for a diabetes clinical trial that looks like this. So we have across different sites, and there's about 11,000 records. We have several patients for different visits ranging from screening to baseline to week whatever. These people have run these tests and have gotten certain results in certain units, which we compare against the normal range. These were collected at a certain time by a certain technician.

What if we just asked an LLM: "I've done all my edit checks, but the problem is those are deterministic. I'm not able to figure out the stuff that... we are not able to go beyond what we would do in a routine deterministic way. Can an LLM go beyond that just by asking it?"

> Find data quality issues. Look for temporal patterns, site-specific anomalies, and so on.

Now I did that. And let me show you what it gave me. This may surprise you a little bit, but the prompt that I showed you is not the exact prompt. I added a line after that. But look at this.

The patients who got worse. It's saying:

> When 19 people improve and one deteriorates, you have a medical mystery. When 19 deteriorate and one improves, you have something else entirely.

And it goes on to tell a story. Jan 2024, 200 patients enrolled in a diabetes trial. And they came in with the same thing: low blood sugar, better health, blah, blah, blah. The nurse drew their blood and the trial seems fairly meticulous. But there was a strange pattern. Across the 200 people, 10 clinical sites, and 11,000 lab measurements, there are three sites it says that have quality issues.

And let's specifically look at what the quality issues are. The HbA1c variability for one of these sites is unusually low. Looking at how the values are for the other sites and comparing it with this 8.67—too perfect, too smooth. It's like a jazz musician who never misses a note or an author who never makes a typo. Technically flawless in a way that actually makes you suspicious.

And this is peculiar, but it's saying Site 9 is actually impossible. What it's saying is that in almost all of these, the HbA1c from the baseline was negative, things improved. But for just this one site, it increased. Now what are the odds of this happening? It's almost impossible. So clearly there is an anomaly here.

And it goes on to list, like a Malcolm Gladwell story, in full detail in a span of about eight minutes: what exactly happened, why potentially, and what we need to do. Site 9 definitely requires a forensic audit. We need to look closer at Site 1 and Site 6 across review. Effectively there are three sites, it says, that there are problems potentially. And this is what we need to do about it.

What was that one additional prompt that I added? I added a sentence: **"Narrate the insights like a Malcolm Gladwell New Yorker article written in the form of a New York Times data visualization story."** That's all.

See, **it's a genie. It can do practically anything that we ask it for.** Half the problem is we don't know what to ask for. Some of these it does really well, some of these it does moderately poorly. And it's improving at a rapid pace as we saw. So a big part of what I'm learning is what we can ask for that makes our life easier with this kind of infinite capacity. And this is one of those hacks that I'm finding.

Now, the other thing to notice is the way it did it. Even though it did this in the form of a story ultimately, the process of getting there is a very detailed 14-step analysis. It started by looking at the data, it examined the structure by writing code. And here's the thing: when it is writing code to do the analysis, the way code fails is very different from the way language fails.

If somebody is looking at two sets of numbers, trying to match them, and they are unable to do the match correctly, yeah, that's human error. But if a program fails to make the match... either the program is completely wrong, in which case it will give rubbish results, or it's right, in which case it will get it right.

Now programming is a language. Large Language Models are good at languages. It's in their very name. And therefore, a trick is to **use Large Language Models to write code to do reliable jobs.** And that makes them far, far more reliable. And ChatGPT, Claude, Gemini, etc. have been doing this for quite some time. They might need a nudge occasionally, but in this case, they didn't even need a nudge. You give them data, they will write code to do the analysis, they will give you the code to re-run the analysis, and you can validate it.

Let's go on to our third one. What if I have a bunch of patients, I have the patient data, and I want to run a set of clinical enrollment protocols. Let's say a series of inclusion and exclusion criteria for this Glucofix drug. I have an age criterion, a diagnosis criterion. We have a document that explains exactly what the criteria must be. And we have a spreadsheet that again says this is the patient profile. We have potentially a thousand patients with all of these demographics and other details that we can filter from.

Doing this manually, that's going to cost a fair bit if we want to do it for every site. And there are going to be screen failures. A 40% screen failure rate is fairly typical.

What if we had an LLM not just write this, but give it to us as a story? Give me the set of people... and the prompt that I used here, by the way, is:

> Given these inclusion and exclusion criteria and this patient database, tell me who meets the inclusion criteria. Who does not qualify and why? Give me the reason. Rank them by the likelihood of successful enrollment so that I can go back and pick the next batch if I need. And give me the code to run this locally.

All of which it did. And just so you know what it looks like, I'm going to show you the output file that it produced. Let's open that.

So for each of the thousand patients, having gone through the inclusion and exclusion criteria, it's identified for the first patient, they're ineligible. Exclusion reason: the CKD stage is over 3, the EGFR is less than 60. But the inclusion potentially was because the FPG and EGFR are okay. Those are the criteria I knew.

Second and third patients are eligible. And they have a score of, let's see, 41—not so high—and 88. So the third patient looks very promising. And the reasons for that are something that we can fairly quickly infer against each of the criteria.

And given something like this, and the code that will run it, we can check if the code is valid. Therefore less likelihood of errors. The next time we want to run it, we can re-run the same code. No need to even go to something that is potentially less reliable. In short, the impact of this is something that can bring the cost down for and the reliability up for a site inclusion criteria.

Wherever we find data, there is serious potential for the use of LLMs, simply through the vector of using programs as a means of getting to that end.

Now here's the thing. There is this **GDPval study that OpenAI did that compares human performance against AI performance** across pretty much the entire spectrum of work. For software developers, for managers, for sales managers, for financial managers, for nurses, and so on. And tried to see where on real-life tasks the average model does better or worse than humans.

Green is where the model does better. Red is where the human does better. And you can already see that roughly in half of the places, models are performing better than humans. The average human. The role of the expert is still safe. But I'm an expert in one area. There are 20 areas that I'm not an expert in. I may as well leverage something that is better than the average person in these areas and become far more self-sufficient, far more productive, far more reliable in these areas. Especially when the cost is negligible, practically zero.

Keeping that in mind, I have just three things to offer you as guidance.

These models, they're there. We may as well learn them. And what that means is also using them more and trying to use them better. Towards this, **Practice is your biggest lever.** My rule of thumb is having **50 conversations with Gemini or Claude or ChatGPT every day.** 50 conversations every day. Just that one thing will suffice.

On top of that, when I'm stuck, I don't even know what to ask it. I ask it, "What am I supposed to ask you?" **Research.** You have access to the internet. You have access to what other people are asking. You have access to the various capabilities that you have internally. You tell me. Based on my past conversations, which you are aware of, you figure out my interests. It does some fantastic psychoanalysis, by the way. It can tell me more stuff about myself than I know.

Thirdly, **Post-Mortem.** I try something, it doesn't work. I ask it, "You went wrong. I know this because X, Y, Z. At least in the areas where I'm an expert in. Why did you go wrong? And what should I do the next time so that you don't make this kind of a mistake?" And it works pretty well.

Use it as a thinking partner. If nothing else, you'd be more efficient, more productive, more future-ready. But sometimes you can have it write a Malcolm Gladwell story and have fun as well.

Thank you.

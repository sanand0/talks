## Transcript

[VIDEO](https://www.youtube.com/watch?v=kihmwxFLSf8)

**Host:** Anand Subramanian, known as an LLM psychologist. He is recognized as one of India's top 10 data scientists, an AI influencer, and a frequent speaker at TEDx and PyCon. He is an alumnus of IIM Bangalore, IIT Madras, London Business School, IBM, Infosys Consulting, Lehman Brothers, and BCG. On a more personal note, he shared with us that **Anand has hand-transcribed every Calvin and Hobbes strip ever published**. He is happily hooked on Minecraft and Anime, courtesy of his daughter, and hopes to watch every film on IMDb's top 250—except _The Shining_. He’ll have to tell you more about that. Anand, thank you.

**Anand S:** It's scary. I read the book, and I've seen Jack Nicholson and Stanley Kubrick separately. I can't combine them. No, thank you.

The _Calvin and Hobbes_ stuff also got me to my first Digital Millennium Copyright Act takedown, so I have been on the other side of the law. But most recently, I've been teaching students to hack, copy, cheat, whatever. Ajit mentioned me publishing the assignments; a few months ago, I tried an experiment. I told my students at IIT Madras, **"You can copy. Feel free."** Cheating is allowed. And then I tried to see how many people actually copy and how it impacts their performance.

[SLIDE](https://sanand0.github.io/tds-2024-sep-project-2-results/similar.html#?similarity=0.5)

This was a coding assignment. I can figure out how similar two pieces of code are. Here are a bunch of students whose answers were 100% identical—exact character-to-character match. Now, of course, 100% similarity is too strict a measure of copying, so I can probably choose a looser measure, say about 40–50% measure of copying. But the strange thing is, even then, only about 40% of the students are copying. Now, what do I have to do to get you to copy?

Does it make a difference? The **Greens** are the originals; that is, they have published a result and somebody else has copied from it. The **Greys** are the independents; they have not copied, they have not let anyone else copy from them. The **Yellows** are the first copiers; they find a Green, latch on, and submit the assignment very early. The **Reds** are the late copiers; they wait, they find the assignment, and so on.

What's your guess? Who do you think scores the highest?

**Audience:** The Reds.

**Anand S:** The Reds. Okay. How many people think the Reds score the highest? Majority. How many people think any other... 100%? No, that was the Reds, the ones who copied late in particular. The Greys, who were independent? Any—how many people think the Greys, who didn't let anyone copy nor copied? Few. Anyone thinks the early copiers scored the highest? Anyone thinks the person who let other people copy scores more? Chance is there, one or two.

I belong to the Green bucket, according to Ajit. And yes, **they do score the highest. By a solid margin.**

What I want to believe from this is two things. One, when you create something original and you let others copy from it, two things happen. First, you get feedback. You probably get early feedback, which means that your result is better, you're able to improve, and you end up coming up with a better result overall. They scored higher, after all.

The second thing that I believe is that **it actually allows you to collaborate and learn from the other person**, not just based on the mistakes that they point out, but also their solution. Part of what gets copied becomes yours. Where I'm going with this is that very often we think that there is value to intellectual property through propriety. "I own it. It is exclusive." And that is a valid approach. There is another approach, which is where we learn through collaboration. And that too is a valid approach. In this particular case, that seems to have gotten a little more of a result.

Incidentally, who scores the second highest? You're right. The Reds. The ones who are waiting right till the end and copying from someone because they have a far larger variety. But the Yellows who copy early don't do so well—smaller pool to copy from. **So don't copy early. If you're copying, copy late.** (Audience laughs)

But do copy, because it's better than being the independents who are scoring the worst sitting in their own pool, developing their own solutions, not copying, not letting anyone else copy, and faring the worst. Great if you can build stuff, but if you do, share. Or else, at least copy.

This probably has not too much to do with Agentic AI, so I'm going to dive right into the topic itself. Now, some of you—many of you—may have submitted a Google Form where we had asked for a bunch of questions. Now, how did these questions come up? See, I'm lazy. I absolutely cannot do work. So what I did was when Ramya called, I took a transcript of that call and fed it into Claude and said, "What am I supposed to do for this?"

<!-- https://claude.ai/chat/8ab5cbdf-89ac-4241-860b-55830945c45e -->

[SLIDE](https://claude.ai/share/ee4927b5-5c77-4f9f-b176-b232b626c610)

Here is the session: "I am delivering the talk at Deloitte this month, blah blah blah, I can send them material beforehand," and so on. **I am lazy. And I'm going to repeat this many times because this is an invitation for you to be lazy. For you to copy. It's very high ROI, by the way. You should try it sometime.**

So I didn't bother typing all of this stuff. All of this is dictated while on a walk. Why waste time when walking? And said, "Look, give me some cool stuff to play around with." See, delivering a talk can be boring, especially if you're delivering the same content over and over again. Talking to a client is boring; they'll ask the same bloody questions every single time. Why not gamify it for ourselves? Let's have some fun. Maybe at their expense, but maybe also for their benefit. So part of this was also me saying, "Look, I want to run a mini-game of some kind." I have two purposes: one, entertainment; and education—for me. You are the byproduct. Actually, as they say, right? **If you are not paying for this, you are the product. So you are, in some sense, my product. And I am learning something from this experience.**

<!-- https://docs.google.com/spreadsheets/d/1g7fvFVZYvKHKBQ8jFhEQJwD5mJ7g2NJxDYq81OhCQiE/edit?gid=1614943229#gid=1614943229 -->
<!-- https://docs.google.com/spreadsheets/d/1yN4ttc9OT3Hj7f3k9AOiRPqvyb1oir8zxxB1VnaMRas/edit?gid=0#gid=0 -->

[SLIDE](quiz.xlsx)

It gave me a set of questions and it did a solid verification on which of these statements are facts versus fiction. So for instance, a statement like: "AI agents can now autonomously negotiate and close binding procurement deals for tail spend categories without human intervention." How many people believe that this is a reality, by the way? Just a quick check.

**Audience:** [Show of hands]
**Anand S:** One... How many people believe it's not a reality? Half a dozen. Okay.

**Anand S:** And based on all the deep research, **Claude thinks it's partially true**. There are some instances where this sort of thing is happening. **Gemini thinks it is in fact reality**, and if it is going this strong, then there are citations in there showing it is in fact happening. **ChatGPT says it's mostly hype**, but still gives it a three out of five.

**This is a lot closer to reality than we as a room might have assumed.** I would not have known this either. Neither would I have known to ask this question, nor would I have known the answer. But I know enough to ask all the agents the answer. Why bother doing the work when we have agents to do the work for us? **And this thing changes so quickly that knowledge is not worth hoarding. Yet another reason to share what you know, because it's anyway out of date. You're selling old stock.**

The questions that you've shared... the next step is, now that I have put together this set of questions and you've collected the answers, to analyze them. Now, imagine here is a client situation. One of your clients comes to you and says, "What I'd like to do is analyze this survey data." Here's the survey data. Let's assume that it is the same survey data that we had. We asked our team—the client says—on what they believe is reality about AI and what is hype about AI. "And I'd like you to come in and do a quick advisory exercise telling us how we should improve."

How would you go about it? Any suggestions?
**Anand S:** Client says, "We've done a survey. We've asked our senior leaders for each of these questions: is this hype or is this reality? We have an exec meeting tomorrow where we'd like you to come in and present your advice on how this group should learn from AI and do better."

**Volunteer 1 (Female):** [Inaudible - mentions using Deloitte tools/Sidekick]
**Anand S:** Very good. How will you use Sidekick?
**Volunteer 1:** [Inaudible - mentions putting data in to understand the saving]
**Anand S:** Wonderful. Any volunteers to come in and do that? Please.

**Anand S:** And what we'll do is maybe just dictate it into ChatGPT. So... let me stop this so that you can get a sense of the data itself. The data is here. Each row is one person's response. The columns, which are barely visible, are the questions. And this is their rating on whether it's hype or reality.

_[Discussion with volunteer regarding recording/microphone]_
**Anand S:** Sure. So that was the client research team. They want to find out where the difference lies.
**Volunteer 1:** Yes, please.

**Anand S:** And others, please just have a think about how you might approach it. A lot of the effort that goes in in working with AI is less about doing stuff and more about knowing _what_ we want to do. And a little bit around _how_ we guide people on doing it. Put another way, there's probably more role for psychology than science—though psychology could be called a science, I don't know—but you get my point. **It's more about almost human behavior than it is about technology.**

And while we are at it... I'm certainly going to invite another volunteer in a short while to try out another prompt on top of this. But until then, please just think a little bit. Yes, please?

**Volunteer 2 (Male):** Since I've started using most of the GenAI tools out there—not just for work but even day-to-day life related issues—so keeping aside the limitation we have within Deloitte, which is like using Sidekick, but if you're open to use all the tools available... A couple of things which I would have done:
**One: If I'm starting with ChatGPT, use ChatGPT to even come up with the right prompt.** So, in an abstract manner, put the bullets of what you're trying to achieve. Use that prompt to come up with the disposition or the scoring or the categorization of the survey response.
**And the second thing which I typically do is I make ChatGPT come up with a summary.** I would say that I would want, say, **Gemini or DeepSeek to validate or review your response** and identify gaps or give feedback. For that, have ChatGPT summarize—or basically have it give you a prompt which you can just copy-paste into, say, Gemini. Paste that into Gemini. Gemini would either agree with most of the points or it may give some suggestions. Feed that feedback back into ChatGPT and refine your output.

**Anand S:** **That covers two techniques: Meta-prompting and Cross-validation.** Meta-prompting meaning prompt for a prompt. Cross-validation meaning double-check somewhere else. Both effective in almost any situation. But please.

**Anand S:** Okay. Now this is taking one question and figuring out whether the answer is right or not. Which is a great starting point because why would you do this?

**Volunteer 1:** Why would I do that? First thing, if I know the answer, I might want to come up with a baseline answer for it. But since I don't know the answer, I want to get some baseline information on what is the reality around it. Get that understanding, then I can utilize my firm's knowledge or skills. Then I can utilize what I know from my firm on how do we put a point of value—POV—around that. So for me, at least as a starting step, I need some basics and that's what I have used it for right now.

**Anand S:** Which is a great starting point in 2025. In 2026, we would do it slightly differently. No, thanks. I'd like to invite another volunteer to come forward please. Any other volunteers? While you prepare yourself to come over here, let me share why we might consider an alternative approach in 2026. And I'm not saying this is _not_ the right approach; this is a solid approach.

**Anand S:** What we're doing is saying, we'll learn and we will deliver an answer. I work with a team of freshers. We call ourselves the Innovation Team. There are, depending on the day of the week, anywhere between two to four people in the team. And we produce roughly two to four prototypes on a daily basis. And the team basically comes to me every day and says, "Anand, you have given me only three tasks for today. Can you give me more?" Which is a very unusual situation. But the nature of these is: "Here's a client presentation tomorrow, can you put together some kind of a prototype for it?" They take the RFP, they build the solution, and give it.

These people don't understand the domain. Some of them don't know how to code. I mean that. They actually are not coders either. What skill do they have? Nothing. **Ignorance is probably their biggest skill.** They come in and say, "I don't need to understand the stuff; AI can understand the stuff. I don't need to deliver the solution; AI will deliver the solution. I don't need to know how to prompt; I can meta-prompt. I don't need to know if it is right or wrong; AI can cross-validate it for me and get to the result."

And we'll do that now. You will do that now. Any volunteers? All you have to do is come here and speak. Please. And we'll have you next, there's enough prompting that we could do.

**Anand S:** So let me encourage you to try something as a next step. What we want is not to bother trying to understand the domain. Somebody has given you a survey. You don't know what that survey is about also. And your job is to create some kind of an output, and it's up to you. How would you go about doing this?

And let's do it this way: Let's dictate the prompt into ChatGPT. We won't run it. And then we will actually execute it on Claude or Gemini or something. So, let's create a new chat. What would you tell the LLM to do? You can just speak into this while using this.

**Volunteer 3:** I would tell the LLM that please analyze the data that has been recorded from the survey. **Give me top three trends out of it. Summarize the survey in a manner which is presentable to maybe a group of practitioners who filled up the survey as well as the people who would be wanting to look at it from a leadership perspective for reporting on that.**

**Anand S:** Perfect. Let's give that a shot. So if we take this prompt... thank you, we'll run this. I'll just change this to "Please analyze blah blah blah" and I'm going to take this and put it into Gemini to do the analysis. Now, why am I jumping between models? Because... I'll tell you later.

**Anand S:** Now, let's upload the datasets. These are your responses, without even giving it the correct answers and all of that, and run it.

Now what we are doing here is **treating it like an intern to which we have given the entire job.** Let it do it. **Why are we standing in the middle trying to interpret it almost like a man in the middle?** Now, will it work? Will it not work? I don't know. Let's find out. But let's do something different... Meta-prompting. I don't know how good this prompt is. We just came up with it on the fly, right? So what I would do is tell ChatGPT something along the lines of:

<!-- https://gemini.google.com/app/f584be637fac5b64 -->

> Look, I got a data set. It's a survey of some kind and the client wants me to present this data set to their team to, I don't know, get some kind of insight out of it. Honestly, I'm not really sure what to do, but I'm not too fussed about it. **Keep in mind that this is a very important sale for me to make. I want to wow them.** I'm going to give you a starting point of a prompt. Use that as the basis, but do two things. Number one: **come up with a fantastic prompt that will give me some really impressive output.** Second, by the way, **tell me how you improved the prompt and what I should learn from the process by which you improved the prompt.** Here is the prompt.

With that, I am running a meta-prompt, which is taking some time. I’ll paste it here and just say, "This is the prompt." Except I'm not going to run it on ChatGPT; I'm going to go to Gemini for now and run it. Now, at this point, you may be wondering, why does this guy speak into ChatGPT then go to Gemini? Why not Claude? **I ran out of Claude credits because I was sitting and coding there.** (Audience laughs)

ChatGPT has fantastic voice recognition. Gemini is much faster than ChatGPT. If I sit and run ChatGPT, it will give a perfect answer 30 minutes after the end of the presentation. Knowing this, I am timing it partly for show, not just "do."

Now, there are two ways in which we normally approach this. One: read it, understand it, share it. Second approach: **don't read it, don't understand it, just share it.** Both are valid. You have a lot of practice in the reading/understanding side. **Practice the not reading, not understanding side also.** Copy. Cheat. (Audence laughs)

So now, let's take this prompt. It has some context, blah, blah, blah, and the prompt ends here. Now let me upload the file—same file—and once it uploads, we shall run it. Now let's go back to the earlier prompt which we ran. What this did is, based on the survey from 22 participants, here is an analysis of the key trends. **I remember I said, "don't bother reading." This is too much to read.** There is a presentation tomorrow. If I have to sit, understand, validate, and then go to the presentation, it's going to be a little time-consuming. I'd rather make it easy for me to validate.

It's saying something—there are three trends: universal consensus, human-in-the-loop mandate, great cost debate. Here's what I'm going to do. I'm going to say: **"You've done the work, right? Give me the presentation."** So here is how I'm going to do it.

[SLIDE](https://www.s-anand.net/blog/prompts/fragments/)

Actually, this is where copying comes in handy. Let me share a prompt that I have used in the past. I keep my list of prompts for creating slide decks handy. I will put it in here as "creating a canvas" and generate it with Pro.

Let's spend a few seconds looking at the prompt. It's saying: **Convert this into a beautiful slide deck—McKinsey style.** You would obviously want Deloitte style. Arguably... anyway. **Make the slides content-rich, clear, self-explanatory with enough detail so that it can explain without a narrator, and write it as a single-page HTML application.** That's pretty much the bulk of the prompt. I did this when sitting there, which is what made me run out of credits. This will do the job, and I'll show you the output.

But until then, let's see the output of almost exactly the same set of prompts that I ran a short while ago.

[SLIDE](https://claude.ai/public/artifacts/ef6b2fd8-6a69-49af-b5a0-a68c1db5886c)

Here's what it is saying about your understanding of AI hype and reality. It's saying that, at a glance, your overall accuracy was about 70%. Not bad. You got most of the results right. But one question was particularly contested: **AI supplier onboarding.** Is that something that can be done by AI autonomously? Half the people said yes, it can be; half the people said no, it cannot be. That was one where there was the least agreement. On the other hand, almost everyone identified deep fakes as a threat. One person did not identify deep fakes as a threat—you know who you are. **Deep fakes are a threat. No question about it.**

Now, what are the insights that we can gather from this? Security threats, you all understand. Regulatory landscape, you all understand. **Emerging capabilities are where you, as a group, seem to be struggling.** Understandably. That's one space that's evolving fast. So, as a rough rule of thumb: something like regulation, something like security, that has been around for a long time—we know it, we know how to tackle it—**trust your gut.** If it's a new area, **don't trust your gut.** Check. Verify. It is more likely that AI will have a better point of view than you having a better point of view than AI.

Incidentally, almost 45% believe that inference costs are a barrier to adoption. **The cost of inference is falling like crazy.** To give you a sense of how crazily they are falling, let me show you how LLM pricing has evolved over time.

[SLIDE](https://sanand0.github.io/llmpricing/)

If you track two metrics for LLMs: the X-axis is the cost (right side is more expensive, left is cheaper), the Y-axis is quality (if you compare two LLMs and see how often one beats the other like a chess match and give it an Elo score). One way of thinking about it is that the 1200 level is roughly high school student-ish level; 1350 would be a college graduate level; 1450 is a postgraduate level. Today the models are at a postgraduate level.

If you look at how this has evolved over time, if you go back two years to December 2023... GPT-4 was the top model. **It cost about $10 per million tokens.** What does that mean? If you take the entire King James Bible or all the Harry Potters put together and gave it and said "summarize," it would approximately cost you $10. And it would do a pretty good job. Things changed. There were cheaper models like Claude 3 Haiku that came up—not as good as GPT-4, but close, and a whole lot cheaper.

To the point where in August '24, we had Gemini 1.5 Flash. That was the same quality as GPT-4, but the price is **7.5 cents.** Not $10. Not $1. Not 10 cents. 7.5 cents for the same. **That's less than one-hundredth.** The difference between a $1 million budget and a $10,000 budget. Same work.

Now at that kind of cost reduction, think about what becomes possible. And this frontier has been steadily improving. We've had far better models—GPT-4.5 Preview coming in at a crazy cost of $75 per million tokens, but close to being beaten by Gemini Flash at 50 cents for better quality. So, a rough rule of thumb is: **for the last two years, every year or so, the cost has been falling by something like 50 to 100 times.** Times.

Inference costs? Doesn't even matter. By the time we think of a use case and it goes into production, the cost numbers are meaningless. I tell our clients: **I will personally fund your entire inference bill.** As long as I can build the solution. You guys will build inefficient solutions and crazy models; I will build the solution. But if I build it, I'm willing to fund the entire thing. And internally, I tell our client team members: Look, I will fund this personally, literally out of my own pocket. Negligible. And it's falling like crazy.

But the point is that this is like compounding—something very hard for a group to understand. So keep in mind that the costs are falling faster than we really can grasp it. Consumer AI seems to be overstated. Digital twins for autonomous purchasing? Not quite there yet. So the growth has been on consumer AI, but we as a group perhaps don't get where it's gone far and where it's not gone far in relatively newer areas.

This is one slide out of a slide deck that goes in question by question, tells us where we did well, where we didn't do well, what was the distribution of responses against each one of these. Which are the questions where the opinions are diverging? For instance, questions around AI twins purchasing: 55% feel that it's hype, 45% feel that it's not hype. Cost as a barrier: strong 50/50 split out there. And the kinds of topics where we really get it: legal, regulatory, deep fake. Kinds of topics where we don't: supplier onboarding, digital twins, cost as a barrier.

So, cost and new areas seem to be the trend. It goes on. And "what to do about it" generated while the others were speaking. And you can do this with the same set of prompts. Let's in fact see if we managed to get this one to generate. Yeah, okay. So we've got a bunch of slides out here: "State of Agentic AI."

<!-- https://gemini.google.com/app/d4f4b98fe98f5e92 -->

[SLIDE](https://gemini.google.com/share/904b785bf8f5)

So this is a slide deck that, based on your prompt and my prompt combined, has created an executive summary, the defensive necessity, autonomy gap. I'm not going to go through this, but it's effectively exactly the same data and the same set of results. Something pretty interesting. Trend number one: cybersecurity consensus. Everyone's agreed on this.

This is something that people with your level of skill will be able to take in front of a client, present with just two, three minutes of reading before the deck. What does that mean? It means when the client says, "I need something done," **you don't need to look for a team.** You don't even need to look for one person. The only question you need to ask is: "Can you send me the data?" Second, **you don't need to ask for time.** You can say, "I'll have this for you by the time you reach home." Not same month. Not same week. Same day. Arguably same hour.

Third, you could say, "Let me go a step further. I'll build a dashboard out of it for you." So for instance, I took Gemini and said, "Give me a nice data visualization out of it."

<!-- https://gemini.google.com/app/a7e49ffd7ccb2cef -->

[SLIDE](https://gemini.google.com/share/31ad13627c1c)

So it took every single response, and now this shows, for each question, where each person stands. So each dot is one person. So this is somebody who answered correctly on autonomous regulation saying that it is hype, and also answered correctly on the second question and the third question, but answered wrong on the fourth question on digital twin purchases—though that's a marginal call one way or the other. **Being able to drill down like a dashboard, like an interactive presentation, as an add-on that you can put into this.**

And if you wanted to convert this into an application where you can do a simulation: "What if our team starts becoming a little more savvy on the cost side, will that have an impact?" Start talking about implications: "What are the use cases that we can build on top of it?" and so on. **Building applications, building slide decks, creating new forms of output that we haven't yet thought of—these are all a norm today.**

If that is the case, we need practice. And the best people to practice are people who know the least about a particular area. Because you don't know what's possible. The more you know about it, the more you assume that some things are not possible. So it's usually good to practice complementary things. **If you know how to code, try and avoid coding.** If you know how to build presentations, try and avoid building presentations. Do the opposite. You're not familiar with code? You build an application. A developer is not familiar with how to present? Have them come and create presentations. Not that they will be effective. As long as they know _what_ to ask for they will be effective, but they may not know what to ask for. But that's part of the learning process: capability versus needs. Now, let's take another exercise... Sorry, before that, any questions?

**Question**: What we did today has been commoditized to an extent that the clients could themselves get this kind of an output, right? They don't need Deloitte to do this for them. So where do we focus now? We understand that the basic knowledge of prompting and utilizing the toolsets in the market is going to become mainstream table stakes in the next maybe weeks, months—this year for sure. But there has to be a differentiator that we bring to the market. What value are we adding onto what's really table stakes? And that is what keeps evolving every month because of all the capabilities that keep coming up. And those are the key problems that I face daily... How do we cope up with those?

**Answer**: Good question. Something that I struggle with every day. And one of the things that I'm learning is: **practice helps.** And let me demonstrate what constitutes practice. Standing here, my natural inclination is to answer this question based on the months of reading and research that I'm doing. I am not going to do that. Instead, let's ask. Let's see if we can figure out how to frame this question in a way that will be meaningful. And I'll paraphrase, but I'm sure I'm getting it wrong.

"AI is moving so rapidly that the kinds of capabilities that we have today are getting commoditized. For example, it's possible to build a presentation or an application or a data visualization or pretty much any kind of artifact in a matter of a few hours. And anyone can do that. So if we as Deloitte want to build some kind of an advantage, a differentiation—ideally something that is sustainable—where might that lie?"

If you could look at examples from history on how such challenges have been faced, how people are approaching it today, and share the best practices for me concisely in just three or four sentences, that would be very helpful. And let it run.

Now, here's the thing. I don't think there is an answer that stands independent of how we use it. What I mean is, what it says as an answer is a starting point. Okay, we could think about it. But as an organization that may not work perfectly for us, as a team that may not work perfectly for us, so we iterate. And we figure it out.

<!-- https://gemini.google.com/app/5c274dec4bc6837e -->

But while it's coming up with its point of view, here is my thought. For the vast majority of history, the assets that we've been building are things that have been difficult to copy. So the question now becomes: **what is difficult to copy?** Software posed this kind of a problem. Software is about as easy as anything to copy. Art, with the invention of photography, became so easy to copy. Actually, it became easy to copy even before that with the brushes becoming more popular, but over time it became easier and easier.

So what were solutions? One solution was regulation. People said, "We want to protect property, but property is no longer just physical, it is also intellectual." And therefore the entire regime of intellectual property rights came in. Fair enough. So we may actually turn to—not _may_ actually, _will_ almost certainly turn to—regulation. And that in my opinion is probably the only true sustainable source of advantage. So, the answer is a weird one: lobby is what we can do.

But before I go on to others... **Sustainable differentiation lies not in the artifact itself, but accountability for the outcome and the trusted relationship that allows you to navigate the nuance.** Making friends with your clients to the point where they say, "Huh, that answer from ChatGPT, when it comes from you, I will trust more than someone else." Arguably, what was I doing as a consultant at BCG? I was taking some junk which anyone else could have done and sharing it. The reason the clients were buying it was because the partner was friends with the client.

So that's one. Also, anchoring your premium pricing to proprietary data integration. Yeah, that's a moat that you can protect. "We have something that no one else does"—either training data, prompt data, validation data, and so on. And **assumption of liability. This is probably the biggest one. "If we go wrong, we will stand by you.** We will fight your cases for you. We will guarantee success monetarily, legally, however we want." That's another possibility.

Now, is that the answer to your question? Probably not. Because you were really asking two questions: What can we as an organization do? What can I as an individual do? And the answer to the second is somewhat nuanced. Let's come to that towards the end. Any other questions?

**Audience Question**: In the early days of my career, when we didn't have any of these tools, I remember I specialized in Oracle technology. So when I was in the middle of a project for a client and there was a specific functionality of the tool that was just not documented—there was nothing available either on Google or no documentation—I put in hours or a couple of days to try out different scenarios and figure out what that functionality is.

But what I learned then, I still remember freshly in my mind and depth. So that while it takes time, that effort results in knowledge that lasts long. And when you talk to [the] client, that experience matters. As compared to say, junior practitioners in our firm now who have these tools at hand. When they are able to create these deliverables or answer client questions with the help of such tools, while it's also a problem of effort being put in and saving time, the learning gets bypassed. So how do you strike a balance to make sure while we are leveraging these tools to drive efficiency, at the same time our bread and butter, which is the experience we gain through consulting work, that's not lost?

**Answer**: A strong parallel to education is: should students use calculators? They bypass the learning. But how much value is what they're not learning have, or how much does it carry into the future? The answer is: it depends. There are scenarios where we need mental math. There are scenarios where we need to know how to solve the problem on the spot.

The proportion of times that we need that skill is falling. Same with how many of us can survive in a jungle? How many of us _need_ to survive in a jungle? So part of the question becomes: What is the skill that is required more often in the future? And as long as we are catering enough to that, the rest, of course, is a good-to-have. You could argue that we don't really need muscles given machines, but we have sports. And that's a very different function altogether where muscles do matter.

Similarly, I'm sure that there will be things that will have value either for aesthetics, or for the sheer pleasure of doing it, or historical value, or niche scenarios. But a lot of the things that we consider skills at any point in time, over time fade in importance, and we are in yet another one of those eras. So, if somebody says, "But aren't they losing the learning?" my follow-up question will be: **Are they losing learning in an area that is likely to become more important as a skill, or less important as a skill?**

If it's more important, do the work. What constitutes more important? Well, if AI is going to be doing a fair bit of the, let's say, intellectual work, the relationship work is going to fall on humans, at least in the near future. **So the value of relationships is going to go up.** Which means that if there is an exercise that people need to do that involves building the relationship muscle, good. Which was actually my intent in that copying exercise. Not only do you learn to copy, you learn to make friends. Do you have any one person even whom you can reach out to and say, "Let me copy your assignment"? And if you don't have even one person and don't know how to build that skill, [in] the AI era you have a problem.

On the other hand, do you know how to code? AI can code for you. **So that exercise was literally designed to say: Make a friend. Don't worry about learning how to code.** And enough people are teaching that anyway. This is how I'm thinking about striking a balance, but I'm sure there are better answers.

**Audience Question**: We know Agentic AI or AI is mostly... the results that come [are] probabilistic in nature, not deterministic. And in a client production environment, going with a probabilistic outcome could be fatal for them. So what is your thought process around how do we manage such situations? And what is the role that humans will play in a bigger, broader scheme of things when Agentic AI, A-to-A communications, will start?

[SLIDE](https://sanand0.github.io/llmevals/double-checking/)

**Answer**: One of our clients asked us exactly the same question. And we said, why don't we do an experiment? This was specifically about tagging research papers. They said, "The accuracy from AI is not matching our expert accuracy." I said great, let's just do one quick check. How well do your experts' accuracies match with each other? **The answer was about 73%. AI was matching them at about 80%.**

So if what constitutes correctness is subjective, and humans are disagreeing on it, experts are disagreeing on it, how do I measure accuracy? I can probably say, look, are we as good as another human? So put another way: **Once we set a benchmark as the alternative, the target moves from "machines need to be perfect" to "machines need to be better than status quo."** And how much better becomes the measure.

Which leads us to the second question: How much better and how do we improve it? Humans are imperfect. If we want a process that is made up of humans to be more reliable, can we do it? Arguably we've been doing it for centuries. And one simple check that we did was we took some customer support data, passed it through a whole bunch of models. So supposing somebody asked the question, "When will I receive my order?" Different models classify it differently. They are supposed to classify it as "Track Order," but this particular model classified it as "Delivery Period." Okay, we know all the mistakes. Some questions most of the models do really well on. Some questions the models don't do very well on.

What if we said instead of taking just one model, we ask two models? And if they agree, no problem. If they disagree, then park it, have a human double-check it. Or take three models, if all three agree, then pass it. Or all four, or all five. And it turns out that when that happens, the accuracy increases considerably.

The X-axis is the number of models that check. The Y-axis... if just one model checks and you randomly pick a model—different models have different levels of quality, but this data is about a year old—so a year ago, if you had randomly picked a model on this problem, you would have gotten a 14% error. But if you said two models have to agree, that falls to 3.7%. Significantly lower. And if you said five models have to agree, and you randomly pick the models—you're not even selecting the model; if you select the models you can do much, much better—then it gets to less than 1% error.

But you'll have to do some manual work. How much? If you picked five models, you can get to 99.3% accuracy with 28% disagreement. Meaning 28% of the data, it says at least one model thinks slightly differently, so we have to validate. So what does that mean? **72% effort reduction with 99% quality.** Most people will take that.

In other words, **the strategies for dealing with hallucinations are not very different from the strategies of management processes.** We apply those.

**Audience Question**: So if I try to summarize this, is it like we try to use more models or see which set of models come closer to the best answer or the similar answer?

**Answer**: Both are valid strategies. Try out half a dozen models, see which one tends to do best on this particular problem, and use it. Approach number one. Approach number two: Try half a dozen models, pick the two best, and if they agree, then make sure that it works.

There are several other approaches. Supposing you had a group of people and you're saying, look, if you get this result wrong—for whatever is the process—we suffer a calamity. It just cannot happen. What would you do? And this is an open question. How would you organize a group of people? Keep in mind that they are very cheap. Practically free. How would you organize a group of people to get the best result?

**Audience**: Higher skills or... choice of work to be assigned.

**Answer**: Pick the right task and give it to them. Let me expand that a little bit and say that maybe you break the task down into different pieces. Find one part that goes to the person best suited to handle it, another task that goes to the best person to solve it. For example, in this case, we might have said: let the analysis be done by ChatGPT which does a good job with numbers, and the visualization be done by Claude which is nice with pictures. That's another example.

Or the Maker-Checker concept. Why pass the same question to two models? Give it to one model, take its output, tell the other one "find all the errors in this." Finding errors anyone can do. Then pass it back to the first one and say "now this guy spotted all the errors," and keep running it until they both agree. Effectively having a debate. That's another possibility.

Several ways that you can think of. And the good part is: they are cheap. **So management process techniques apply very well for agents.**

There was another question that I had asked in the form, which is: You have been given a spreadsheet... with a bunch of tickets. And this has a set of columns. Now your client wants insights for their quarterly review tomorrow. What prompt would an AI agent... what would you prompt to an AI agent? Which is roughly along the lines of the kinds of prompts that you were giving right now.

Now, in this particular case, I had them—in the interest of time I'm not going to have you maybe do the analysis... I had the usual models analyze this. Now here's the problem that I posed to them. We have a team of leaders who have been sharing their prompts. Now you figure out what are the criteria that are important for prompts, and evaluate each prompt against that, and tell me where as a group everyone is doing really well, where as a group everyone is not doing well.

So I'd like your guesses firstly on: **What makes a good prompt?** Supposing somebody gives you a prompt, what will you evaluate it on to say yes, this is a good idea?

**Audience**: Is it prescriptive?

**Answer**: Is it prescriptive. Meaning?

**Audience**: [inaudible] ...specific.

**Answer**: Okay, what do you want and is it specific. Got it.

**Audience**: [inaudible] ...context... framework.

**Answer**: Absolutely. What are some elements in the framework?

**Audience**: Context, Action, Role.

**Answer**: Which is a good one. Let's just take the first one as an example, which is Role. Saying "you are playing the role of so-and-so" which implicitly helps it understand the objective. Fair point. Any others?

**Answer**: Well, let's take a look. What I said was: I don't know what constitutes a good prompt. You do the research. I'm lazy. And then you evaluate it against it and share the results. Which are... here we go. So how did we as a group do with the business prompts?

[SLIDE](https://claude.ai/public/artifacts/510e005e-f2ac-499a-ad4f-44dd2c59808c)

The title seems a little scary. **"A significant skill gap exists in AI prompting."** But here's the thing, you can't put a McKinsey slide without the word significant in the title. So... Only 18% of the leaders crafted high-quality prompts. The majority produced prompts that would yield suboptimal AI output. This is probably true of every prompt by the way. It's almost impossible to come up with a prompt that is good enough, except using meta-prompting, which is having an AI agent review the prompt and say what is better.

So, you can ignore all of what I'm about to share. You just ask a model to improve your prompt, it will improve the prompt. But if you're saying, okay, I'm curious, I want to know what it takes to make a prompt better... then for the prompts that you shared: **Context and Persona—the role effectively—seems to be the one that the majority did not specify.**

Put another way, what we're saying is: do this, without telling it who it is or who they are and what their objective is. **Which is a classic management mistake that we all make. I tell my team members: look, just get this done.** Not "I have a meeting with this particular person, this is what I'm trying to achieve, therefore get this done." It's two more sentences, but it's easy to forget that.

**Structural Clarity**, which is: how exactly do we want the output? I'm actually very impressed that this is only 68%. Usually, people don't think of specifying the format that they want the output in. What are the columns that they want? Do I want an Excel file? Do I want a presentation? Do I want something else? Do I want multiple sheets? Should they be linked? We often specify the _how_, but not as often the output format. In this case that remains a gap, but not as large as I thought.

But **Metric Breadth**—defining the KPIs that you would want out of this—the majority of the people have come up with. So what does that mean? More iterations, inconsistent output, missed opportunity, blah blah blah.

I'm going to go into what its suggestion is in terms of things to think about when writing a prompt.

1. **Specify the objective.** What role are you playing and therefore what role should it play? And what is it trying to do? It's a good idea to begin with this. And this is probably the single biggest takeaway that you may want to consider as a group: do that more often. Tell people to do that more often.
2. **Structural Clarity.** What is the output format that you're expecting? If AI is doing the work, your bottleneck is your review time. You can get it to do ten pieces of output, but then having to sit and read the output, that's time-consuming. So you would rather make the output easier to consume. Try and get it in the final format rather than an interim format. Try and get it to go as far as it can. And the models are going further and further every day. So, may as well make the most of it.
3. **Metric Breadth** is not a problem that you have. By and large, that's working well.
4. And the **Strategic Value** is also doing pretty fine. Does the prompt request actionable insights? And you are, as a matter of habit it seems, getting those actionable insights. And this is useful.

The thing about "Prompt Engineering," so to speak, which has now become "Context Engineering," is that the models are changing so rapidly that what we know today is not necessarily true tomorrow. For example, some of you may have heard of Emotion Prompting.

[SLIDE](https://sanand0.github.io/llmevals/emotion-prompts/)

There was a time when people said, look, supposing you put in something like this in the prompt: "Oh dear, I'm absolutely overwhelmed. I need your help right this second. My life depends on it." And so on. Then models do a better job. Or bullying it: "You're a stupid model. Get me the answer right." Or even my five-year-old son can do this: "Stop being lazy." Or praise: "Well done, I really appreciate your help." Of course, models do that a lot to us. Maybe we do it back to the model and see if that helps. And there are a lot of memes around which of these work, which of these don't work.

And some of these _do_ work. So we tested it out across all of the models—well, not at that time, a whole bunch of models that we ran it against—to see if it works or not. So to take an example, let's take Emotion Prompting. Emotion Prompting is something that actually did work pretty well against o3-mini-high. There was an uptake. But on the vast majority of the models, emotion prompting actually had a negative effect. 21 models did worse when we did emotion prompting, which is saying "my life depends on it." If we tried being polite, 20 models did worse. If we tried fear, 19 models did worse.

**There was only one prompt style of the lot that consistently and clearly outperformed all the others. That is Reasoning. Which is the simple phrase: "Think step-by-step."**

This was one year ago. **Today, "think step-by-step" hurts more than it helps.** Why is that? Because the same research that I'm showing you was done by all of the AI providers, and they incorporated it into their models and their harnesses—which is their chat engine—so that it's no longer necessary. To the point where if you actually add it, more often than not it hurts. Almost always doesn't help.

So this too is a moving field. How do we resolve that problem? By trying to avoid the "Knowledge Trap."

There was a time—and now is also the time for me to gently wrap up with a few broad takeaways—there was a time when what you _knew_ was a skill. This came after a time when how much you could _lift_ was your asset. From the industrial era which made muscle power less relevant, we moved to the knowledge era which made brain power the relevant one. I don't know what era we are moving to now. Let's call it for lack of a better word the AI era.

Here, knowledge has less value. But arguably the internet was doing that a whole lot. With Google, why do I need to remember stuff? With mobile phones having contacts, why do I need to know a phone number? **So knowledge was declining in value, but intelligence had value. The ability to solve a problem.**

**But now we have something that is solving the problem. I don't know what's going to replace it. But what I do know is that skill building that we have practiced since we were children—of learning stuff, understanding it, and so on—don't worry too much about it.**

It's okay to let that slide a little bit. Because what you learn is going to be outdated so rapidly, at least over the next few years, that you are better off learning how to leverage these partners.

- If you know how to figure out the answer, don't figure out the answer. Have an AI figure out the answer.
- **If you know the answer, don't say the answer. Have the AI find the answer.**

Why? Because in the latter case your knowledge is probably outdated. You may be biased. And you have an intelligence that can cross-question. In the former case, you're wasting time applying a skill that could instead be spent on learning a new skill, which is delegating to AI agents.

What does this mean when it comes to interacting with clients? Two things.

Number one: When you practice the skill, you become someone whom they can look up to and say, "Okay, here's somebody who practices what they preach with regard to AI." You show them what you do on a daily basis. It becomes part of who you are and builds a certain kind of credibility.

The second is: It becomes part of the nature of your advisory. You are not standing on the shoulder of all of what you have learned and the organization, but on the shoulder of the entire world of giants.

[SLIDE](https://sanand0.github.io/datastories/gdpval/)

OpenAI did this study called "GDP Val," where they took various professions and asked a bunch of experts to come up with a set of questions. For example, for accountants and auditors, one of the prompts was: "You are tasked with reviewing and testing the accuracy of anti-financial crime metrics." And it goes on to share a spreadsheet with some data, and perform the variance analysis, do a sample audit, and so on. They evaluated how well different models did and compared that to the experts.

And what you see here is: in which scenarios the models did better versus in which scenarios the humans did better. By the way, any guesses whether green means models did better or humans did better?

**Audience**: [inaudible] ...models do better?

**Answer**: Slightly in favor of green means models do better. Yeah. Green means models are doing better.

So which means that software development as a job is... the average AI already does a better job than the... the good AIs do a better job than the experts, software development wise. They do a better job than retail... than general and operations managers. They do a better job than accountants... sorry, they _don't_ do a better job than accountants and auditors.

You can use them as customer service representatives. You can use them as personal financial advisors. In fact, my largest investments have been after I saw this. I said, I'm not going to hire a personal financial advisor. I'm just going to ask Claude to give me an answer and put all my money wherever it said. I don't know how it's doing, but... On the other hand, my tax is still being filed by my auditor. Going with this.

And this is a moving curve. But here is the thing. For all practical purposes, for free, you have a software developer. You have a customer service representative. You have a medical and health services manager. You have a counter and rental clerk. You have a salesperson... You have all of these skills available to you. Partly as knowledge assets, partly as agents that can do the work.

Let's leverage them. When advising, we can have a model—or Claude, ChatGPT, or internal equivalents—play different roles and say "You are so-and-so, now I am asking you for advice, give me your response as this kind of an expert." In many cases, it does better than the actual experts themselves. And you have access.

Earlier we would be constrained. "Oh, I don't know a person with this kind of skill." Now you do. "Oh, but they cost money." Now they don't. "Oh, but I don't have the time." Yes, you do.

**Assemble your internal team of experts.** And you need to get familiar with your team of experts. The team is largely your prompts. Just knowing what to ask, because the same model can be made to play different roles. Once you have a small catalog—and do share, better yet copy; copying is good—and come up with a piece of advice that within a span of a few hours, maybe even minutes, comprises of the best that the world's experts can provide... **That is now table stakes.**

This is something that every organization, once they wake up, are able to do. Are you able to get to that relationship quick enough, well enough, deep enough? Are you able to make it a part of who you are? Are you able to build using this some kind of truly defensible assets? Perhaps data assets, perhaps prompts as assets, perhaps new things that will come up. Those will start constituting some of the differentiations.

Lastly, **fact check every single thing that I said.** This may be true today. This will not be true tomorrow. **Skepticism is definitely... in the list of skills that I mentioned I would share at the end... right on top.**

So with that skepticism, and with the prayer that no more than 5% of what I said is wrong... Thank you.

I have only one ask of you: **Prompt 50 times a day.**

All the best. [Audience Applause]

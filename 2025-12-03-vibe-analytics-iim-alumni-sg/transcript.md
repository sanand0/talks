## Debi

Now let’s move to Session 2: Prompt Craft and Vibe Analytics. It is my extreme pleasure to introduce the two hosts that we have for this workshop, Anand and Nirmal. As somebody told us, he is S. Anand, and Anand might say that 'S' stands for a lot of things, but at IIM Bangalore, he was called "Stud Anand."

A few things about Anand. Just like a lot of MBAs, I think he first dabbled in finance. He interned with Lehman when Lehman was still standing. Then after that, he dabbled in consulting. He joined BCG straight from IIM Bangalore, where he was a gold medalist. But unlike a lot of MBAs, he left consulting and moved back to his first love, which is technology. He joined Infosys Consulting in London—a city he chose, he told me, because he wanted to experience the city for a while—and then he started a company called Gramener. Gramener is now a part of Straive, an Asian company.

Just to say this doesn't speak much about Anand; he is a multifaceted individual. He has hand-transcribed every Calvin and Hobbes comic strip. He is a musician of sorts—I don’t know what all he plays, but I heard mridangam, keyboards... we’ll have to confirm what else he does. He loves movies and he said that he is going to watch every movie in the IMDb 250 list. I don't know where he’s got to.

The reason why Anand set up Gramener was because it combined the three loves that he has: statistics, computing, and design. What he did in Gramener was he wanted to tell visual stories using data. That was the objective that the company has and that is one of the reasons why Straive bought the company. **Today, he is doing exactly that but building bigger stories using a lot more data, but also using LLMs.** That is why I think he is one of the best people to host this workshop.

Turning to Nirmal. Nirmal was a co-founder of Fractal in 2000. And then he co-founded Mobius Innovations in 2012, which was a company that used contextual information to be combined with AI workflows. That was the business of the company. The reason I am mentioning these two dates is that **I think Nirmal is way ahead of his time.** Fractal was set up in 2000 during the dot-com crisis, and over time they were the first few people who got into analytics from India; I would say they were the first early movers. When he set up Mobius Innovations, again, what he is talking about is what we see today. We heard the sessions before this where people are saying that you need to understand context, you’ve got to look at AI workflows, put it together, etc., except that he did it a lot earlier.

I think he definitely is a visionary; he looks into the future. The other feature set which Nirmal has—which is a common term that you use in data science—is that he is also a storyteller. He was the first person who talked about writing challenges. If anybody in this room ever wants to be a writer, I think you should talk to him. He can tell you how do you get a beginning to it, how can you join one of these challenges so that you can develop the discipline of writing every day, writing every month, and then how do you discover a community of similar amateur writers across [the world]. He is writing his first science fiction story.

So as I said, I think we have very, very interesting personalities over here. All of you must have attended AI sessions across the world—it could be Google, it could be Andrew Ng—but we think this session is very special because I think that we have got two amazing storytellers who are going to run this session. Please give a warm welcome to Anand as well as Nirmal.

## Nirmal

Thank you so much, Debi. So we are going to use Anand as an example. I call him Bhalla. We are going to use Bhalla as an example of how he has his own system. We will talk about that system later. He is constantly with his plod, which is one of the things that was mentioned. He is constantly recording everywhere. **He is an avid collector of ideas. And he collects ideas and cross-pollinates them.** His point is that two ideas that are cross-pollinated result in interesting ideas. We will show you that prompt in a bit.

But before that, what I wanted to do was let’s keep this completely informal. Let’s keep this conversation going. Let’s begin with an understanding of what’s going on in the room right now. My sense, as I was speaking to a few people, is: **A) There is a lot of FOMO. There is a whole bunch of AI stuff that's happening. It’s an avalanche of jargon. I have no clue what’s happening.** And I am part of that as well.

So much so that this is what I was doing: The three presentations that were coming in were a flurry of information that I couldn't keep track of. So here is what I did—you can do the same. I took a picture, a snapshot of every single slide. I uploaded it into Perplexity. Perplexity is the best AI ever because both of us are alums of IIT Madras, so that’s not up for debate. I uploaded every one of those slides into Perplexity and said: **"ELI5." ELI5 is "Explain Like I Am a 5-year-old."**

Immediately, whatever was going on on stage, I could understand from the perspective of a five-year-old. I could gather all this information. So the point here is that you need to have your own system which works for you. And so we will see if we can develop a system for you by the end of today.

Let’s begin with understanding what are the fears in the room. Let’s be honest about this. I run a few workshops with senior leaders, and that probably sums up and describes this group. With all due respect, senior leaders are embarrassed to learn. With all due respect, senior leaders do not open up their laptop; they probably get other people to open up their laptop. Let’s get honest and candid out here. What are the fears in the room around this whole monster that’s gathering momentum in terms of AI?

(Audience comments inaudible)

Okay, we don't understand what’s going on...

**Question:** (Audience member speaks about fear of relevance and keeping up).

How do you keep up with all this? Will humans be completely replaced? Answer is no. How do you keep up with all this? Everything that is going on every day. You have to start moving your mouse faster, is what I was told yesterday. I kid you not. I went to the NAS.IO summit—this was the last ever NAS.IO summit. Nas is this Harvard guy who did one-minute videos. He is a pioneer of one-minute videos. My son is a fan, 10-year-old; my daughter is a fan, 22-year-old. He did one-minute videos every day for a thousand days consistently and he became famous.

This guy had this seminar that he was running—I paid $250 for the ticket. There, they were talking about a huge amount of stuff. How do you keep track with all of that stuff that's coming in? What’s happening? The pace at which things are happening is just not funny at all.

One of the guys came on stage, he was wearing this Zen tie-dye t-shirt, and he said, "Slow it down." But, **increase the speed of your note-taking.** He said, **"Change the speed of your mouse to 5x."** So that you can quickly capture things. Create a system of capture, create your keyboard shortcuts, figure out all your capture devices so that you can quickly capture every single thing. **Analyze later. Don't analyze right away.**

So then your fear of "Am I losing out on the glut? Am I missing out on something?" is taken care of. You are capturing all of that. What’s your capture device? That’s one question I leave you with.

I hear a few things. One: Jargon. I hear there is a whole lot of hype. I understand there is hype. What is real? What is not? I heard somebody who said, _"Sir mein aaj kal real estate chod ke AI chalu kar diya maine"_ (Sir, these days I left real estate and started AI). I am like, yes, I understand you know AI. So everybody, you've got "AI tomato chutney" or whatever. How do you know you are not getting scammed? Absolutely. **How do you separate the hype from reality?**

What is it that we have as our strength? Let’s be clear about that. We are all MBAs. We are fast learners of any topic under the sun. How do we learn fast? Let’s figure that out. So speed, hype, and jargon are three things.

First up, I want to start off with a disclaimer. I am a student of AI. I’ve been in the analytics space for 25 years, can claim a little bit of understanding of that space, but I don't claim to understand AI at all. I am a student of AI. And so should all of us be. Because the pace at which things are going is crazy. Every day you've got new models coming up. When things are going super fast, what do we do? We slow down. Let’s take a step back and let’s look at the basic fundamentals as to what is going on. If we can understand the fundamentals, if we can get the essence of what's going on, then we probably can get to this animal and figure out what this animal is about.

I wrote a number there. This number is my approximation of 70 factorial. 69 factorial is what a calculator can do, otherwise the digits don't come in. 70 is the rough number of people in this room, which means that's the number of ways in which each of you would have sat differently in another chair. Which means if I say that your experience of this session is a function of who you're sitting with and what side conversations you're having, that's the number of different types of ways in which we can have this same experience of this session. And that's a mind-boggling number. And we are just talking about 70 people.

I equate that to the number of parameters in a large language model (LLM), and that's not 70; that’s a few billion. So we are talking about some ginormous numbers here. What is that doing really? What is this LLM fundamentally about?

The way I understand LLM is: You've seen autocomplete? You know what an autocomplete is on your WhatsApp? Your autocomplete will give you the next letter, the next word, the next two-three words. Imagine I can extend it to the next sentence. The next paragraph. The next page. The next 450-page novel. And the next four such novels. That's the context window that today the models are giving you.

**It’s an autocomplete model which predicts the next four novels from your prompt.** That's all it is. It is not claiming any accuracy. It is not claiming anything else but: "What could be the next four novels if this was the starting sentences or prompt that you're giving?" That's all it is.

Why is it such a big deal? It’s such a big deal because it’s fundamentally a neural network which has learned the mathematics of English. English is a funny language. English grammar sucks. English grammar is non-deterministic. The best two languages are Sanskrit and German—they are very deterministic. So what it has done is it’s taken a large amount of data and understood the mathematics of English. Which means **it’s understood the mathematics of grammar.** And beyond that, it’s understood the semantics of different words. The fact that an "orange" means a certain color or a certain fruit depending on the sentence that it is in, and hence you have an autocomplete connection there. That's all it is.

So what's important is for your prompt to start giving the _context_ around it. What you need to do is to ensure that the orange that you talk about is a color and not a fruit. You need to be able to say, "Bank of America did five times the profit last year." You know you're talking about a bank which has money, and not a river bank, and not a plane banking. So the context in which you provide that sentence is very important in inferring the meaning as well. So it’s understood not just grammar, but it’s also understood the semantic meaning of the surroundings. There is a meaning element to it.

There are quite a number of things and it’s gone beyond that. And we'll talk about that one by one. But the first thing that I want to talk about is: **India is going to lose its advantage—labor arbitrage of programmers—because code is going to be replaced by well-written word documents.**

And we are all masters in that. We've done back runs. We've written well-structured documents. If you can do good specs, that's all it takes to write code. And which is what Bhalla is going to help you with. We going to build some code.

Now, how do you start building this code? You can go to a few... you've got your Windsurfs, you've got your Cursor, you've got your Replit, Lovable... there’s quite a number of them. The best way I would do is I'll just ask Perplexity: "Hey Perplexity, give me some options which are the ones that..."

**Anand**: Talk to it, _yar_, don't type.

(Nirmal interacts with his phone)

> Hey Perplexity, what I am interested in is knowing the different kinds of coding assistants, or I don't know what they're called. So basically, I am someone who doesn't understand programming and I want to become a "Vibe Coder." So how do I become a Vibe Coder? Can you give me some tools?

(Pause for processing)

Okay, so what’s happening is I've already finished my free account, so I am overloading the thing. Which is what Bhalla is going to say. Bhalla wants you to take on... So over to you Bhalla, what do you want them to start downloading so that they can be well prepared for your session?

**Anand:** Get a $20 paid account on any of ChatGPT, Gemini, or Claude. It doesn't matter which one; they are all marginally better or worse than one another in trivial ways. Second, download any personal data to start with. We’ll play around with your data. You could go to [takeout.google.com](https://takeout.google.com/) and download your activity from there. Or be ready to export from your phone or WhatsApp chat. Or if you have your medical reports, bank statements that you want to analyze, utility bills that you want to analyze—any of these, just have them ready and we'll use that as a starting point. **But a paid account is going to make a huge difference.**

Okay, so while you get into your paid account... we are already running behind schedule so I am trying to interweave these things in.

Specs is greater than code. The context window we spoke about. The other fascinating thing that's happening if you notice is this concept of **Multimodal**. Okay, what does multimodal mean? That my capture need not be text. It can be voice, images, video, gestures, movement, pose. There’s quite a number of different modes in which I can capture input. And the minute I have multimodal capture, then suddenly my data capture system gets a total overhaul. So multimodal is an interesting thing to watch out for.

For example, I did not read any of those slides. I requested Pragati, my colleague, to take a picture of every one of those slides. I am going to put in a loop and just run them through ELI5 and I am going to get a sense of what happened there. So I have not missed out a single point there. And then I am going to write a summary on top of that and say "Give me the top three points that I should be [aware of] and fact check them."

Look at what I am doing. **I am doing iterative prompting. I am not happy with one thing. I am going to break it down into substeps and start iterating on what are the kind of things that need to be done one by one.**

So whenever you want to do some prompting, what you want to do is... fundamentally let’s be clear about one thing: **If you are looking at AI as a replacement to Google, you're doing it the wrong way.** It’s not like Google; it’s not about finding the right answer. Don't think of it like Google. You need to be patient and you need to keep iterating. If you don't like the result first, you say, "Hey, hang on. I don't like the result." You can scold AI. Scold AI, "I don't like the result. AI doesn't mind." And then keep repeating that and iterating that.

Now the next thing that I want to talk about is... with the "Picks and Shovels" were the ones who made money. And that was what they were saying in the early days of the internet was the way you were going to make money. Which is basically you build tools so that you can make websites, website agencies, and so on. And that was the whole meme at that point in time. That's the wrong metaphor in the age of AI.

The right metaphor in the age of AI is: **If you want to find the treasure, you need a map.** And so **Maps trump Shovels.** What does that mean? That means that you need to know the metadata, the template, the recipe, the structure of the lay of the land. So what you want to do is you want to figure out what is the way...

I was speaking to a few investment folks. I don't understand investment, I’ve never invested anything, but I am an MBA. So how do I figure out the lay of the land in investment? Oh, there’s something called options. There’s something called futures. There’s something called short. There’s something called long. What does that mean? And I need to know that because "Short" and "Long"—hang on, English is a funny language—mean different things [in finance]. I need to be clear about what do these terms mean, I need to be clear about what is the context that I am working in. Which means that if you need to know from the context, what you need is **Domain Understanding.**

You need to figure out how domain makes a difference. And that is what, ladies and gentlemen, is going to make you folks stand out from the rest of the world. **Your competitive advantage is not Deep Tech.** Let’s be clear about that. Let’s call a spade a spade. Your competitive advantage—Alok is an expert at healthcare. There’s nobody like him in Singapore, and the world I'm sure. And so that expertise... Debi used to consult for CFOs; she can teach any CFO. And so you take that expertise, that Deep Domain Expertise, and build the map around that. That's what you're good at. And how do you do that? **Ask AI.**

"Perplexity, I want to build a map for this domain. You ask me questions so that I can start building that map." And have a conversation.

So I'd requested—we actually ran out of chairs—one of the things I'd requested was one empty chair at every table and call it AI. And say AI has a seat at the table. AI is a first-class citizen, think about that. Ask AI.

And so ladies and gentlemen, I want to come back to that trust thing. This whole FOMO, this whole concept of us fearing AI... [fear of missing out] is just mindset. Let’s be clear what is our core strength. Paddy is good at humor. So Paddy is going to take on humor and build a deep domain expertise and the map and the landscape of humor. And he is going to be the person who is going to talk about what in humor can be brought about. And that any day trumps shovels.

Okay. Now I want to talk about a few examples. AlphaFold. It’s decoded the genome... once you get deep domain you can start doing various things. Fold.it is one company which decoded the protein folding structure and it was a video game that did that. And that ended up decoding the HIV virus. So AIDS no longer is such a big deal.

So now I want to move this to another level and say that the next thing is...

**Audience Member:** Which means it is going to become a part of AI... that I can just have... instead of having Debi help me, I can literally have an AI CFO. Correct?

**Answer:** Yes. Yes. So, a map is not enough. What you need is a trail. You need the ability to go from Point A to Point B. So any map is not static. That map has to be continuously expanded. I want to be able to add a newer map or an overlay on top of that. So today if I look at the Singapore map, I won't be able to go from here to Chu Kang unless I see the MRT map, which gives me a different perspective. That's a different map. And on top of that, if I see the Grab driver map, that would be a different map which will give me hotspots on various places and where I can go to get more traffic.

So your maps have to be expanded. And so if you have to expand maps... hold on to that, put a pin on that, we'll come back to _how_ to expand maps.

But I’m now going back to another point which is: It’s not enough to look at maps. **You want to start looking at directions.** It’s not enough to look at answers. **You want to look at questions.** When you're talking about Google, Google is actually a convergent concept. It’s a large tree which goes into multiple places but it’s still deterministic. But what you want to talk about when you're talking about Generative AI is the power of creativity. So don't look for answers. **Look for what is the best question I can ask.** And which is the best question that will give me the maximum bang for my buck?

And if you think there are no questions, there _are_ questions all over the place. So start increasing the kind of questions you can ask and up the game. So how do you up the game?

All of you guys are fantastic... so end of the day LLM has read every single book. Even the pirated ones. So forget copyright. Every single book is inside the LLM. So "Six Thinking Hats" is already inside LLM. Malcolm Gladwell is already inside LLM. So take your favorite paradigm and say, "You play, dear Perplexity, you play Six Thinking Hats on me. Ask me questions to help me think and brainstorm." **AI as a brainstorming partner. AI seat at the table.**

This concept is something that Bhalla taught me. He said, "AI demands a seat at the table. A brainstorming partner." And so if you have that conversation, you can start asking AI to help refine your prompts. I don't know the answer, be honest, and then start asking AI to refine the prompts.

Now, the way to go from maps to directions is surprisingly very simple: **Problem Framing.** What kind of problems are we framing? How are we looking at different kinds of problems? And so that framing is something that we understand. We understand generic concepts of problem framing. We understand root cause analysis. We understand "5 Why" techniques. And so use those skills to start getting to: What is the question you want to be getting to? And what will give you maximum bang for your buck?

And then you'll say, okay, there is so much pessimism and we've solved every problem that needs to be solved and we need to go to Mars and that's the next frontier and that's what we need to do. Excuse me. Three years ago there was this small virus. I lost an uncle. Three years the whole world was held to ransom and we couldn't do jack shit about it. There _are_ problems to be solved. There are problems to be solved. Even if it is a tiny problem.

Yesterday I was looking at an interesting problem that Apple TV solved. I was watching _Plurals_—you must watch _Plurals_. I did a 10-second rewind because I thought I missed out what Carol was saying. And immediately it recognized that I needed the subtitles, and so it came with subtitles on its own. So I was like, okay, so it understood that. That's a big enough thing for me. Now what is big and what is small, who is to say? It’s a philosophical question. So you figure out what is big enough for you. You figure out what is your _Raison d'être_. You figure out what is the purpose that you want to go and move that towards direction.

Okay. On that note, Bhalla, you want to weigh in on anything on these?

**Anand:** _Nahi yar_ (No man), my AI is taking notes. So I will wait.

Okay, one of the questions that we were asked was: "There’s so much data and how do you start looking at this glut of data?" So I posed that question to Bhalla. So the questions that I was getting from the audience was, "Okay, so I've got PDF files, I've got Excel files, I've got massive amount of data. How do I start getting all that data into one place? How should I think of my data capture device?"

So ladies and gentlemen, I present to you this gentleman who takes notes. And I want him to show one particular thing that he's built called **Ideator**. Okay, so I was blown away [by] what he did. What he did was... religiously he keeps taking notes on any interesting idea that he comes across.

Anand, over to you. You want to run us through what that is and then I'll say a few words.

## Anand

Yeah, so I put in ideas of all kinds. Whether it's stuff that I've learned about LLMs, or general things I've learned, or whatever. And these are some of the things. For example, 9th Feb last year, in a fine-tuning session by one of my colleagues, Dan, I captured a bunch of notes. A day before that, I linked to an enterprise scenarios leaderboard where Mistral 7B was one of the leaders in that. If we look at something that's a little more generic—like where I'm capturing creative ideas—here's one tip from the famous **Oblique Strategies**: "Humanize something free of error." Which is just a way of trying to get more creative ideas. Okay.

So I have all of these notes and these notes are all over the place. Stuff from Daniel Kahneman, stuff from technology, stuff from finance. Now, if we take any two random concepts—like this, and combine it with another random concept, let's say "Never delete data. Mark it for deletion instead." And use this to come up with some new concept. Now what do I want to come up with? Let's say I want to come up with a life hack or habit that I can practice. And give it an ideation nudge.

Now what this does is creates a prompt in ChatGPT. And I'll walk you through this. It says: **"You are a radical concept synthesizer, hired to astound even experts. Generate a big, useful, non-obvious idea that's aligned with 'Life Hack'—now that's what I had prompted it to—fusing the provided concepts with the Oblique Strategy."**

---

Here is the transcript of the talk on **Vibe Analytics**.

---

**Anand**: The prompt continues to say, "Do it in the following way." First, generate five candidate ideas. Here are ways in which you can generate those ideas: use [Charlie Munger's inversion](https://fs.blog/inversion/), use the idea of mechanism transplant, and use constraint violation. These are all ways of helping the LLM think in a diverse way.

Score each of these on novelty and utility. Pick the top score. For whichever idea you come up with that has the top score, tell me the insight. Tell me how to go about building or doing this. How do I test it? What is so surprising about this? And critique yourself. Write it in plain English.

These days, I don't bother putting stuff into one model. Let's do it on Gemini and on Claude, one after another, because they all have very different styles and very different ways of thinking.

One idea that came from ChatGPT was a "Wickedness Dial"—a simple dial, red to green, that raises or lowers rules based on context. The dial switches between a specialist mode and a generalist mode. I'm not sure what that idea is or how it will help, but ChatGPT tends to be a little more cryptic.

However, it picked "Wickedness Dial" as its top pick. What is the insight? Home kitchens should adapt their safety rules to the situation. We can use a context score to decide when we want to be in specialist mode versus a generalist mode.

It goes on to suggest that the mode has four pillars: Clean, Separate, Cook, or Chill. I'm not a food safety person, but these are the kinds of things that we can have an LLM come up with as a new idea in arbitrary contexts.

**Nirmal**: I’ll jump in a bit here. What he is showing you is his [Ideator system](https://tools.s-anand.net/ideator/), and some of those ideas are good, some are bad. You can have wacky ideas that you can pick from, and people like us will have a blast over that.

Now, let's come back to the question of **how do we start making this a process?** I've been trying to write my science fiction novel for the past seven years. I wake up at 4:30 in the morning, meditate, and then write for an hour. I still haven't finished because that's one project I'm a perfectionist at.

I've read a whole bunch of books, and I've understood that the map of writing boils down to **Robert McKee's five points**:

1.  Inciting Incident
2.  Three Progressive Complications (it has to be three always)
3.  Crisis
4.  Climax
5.  Resolution

I heard something very similar in the [Nas Daily](https://nasdaily.com/) one-minute videos. His formula is: **Hook, Problem, Solution, Call to Action.**

So their prompts, just like Anand’s, have that structure. Now you take that further and start getting into **insights**. How do you get insights? Insights are things that you understand intuitively. You need to start curating that.

Every time I meet Devi [Shetty], I am amazed at the clarity he has on finance. He says, "This is the way you've got to turn around a system in terms of collections." I tell her, "You need to be put into a box and have that run the system."

People have intuitions, and you have developed some filters. That is the filter that you want to start weeding out things with to grow your "garden." That is how you start expanding your map.

**What is an Insight?**
Quick digression: On Monday, I saw a black cat, dark clouds, low temperature, and it started raining. Tuesday, I saw the same three things: rain. Wednesday, Thursday, Friday: same thing, rain. Obviously, the black cat causes rain, right?

You are smart enough to figure out that is dirty data. You remove the dirty data. Then you get into this concept that **Dark Clouds + Low Temperature = Rain**. That is an insight.

**An insight is fundamentally something where I throw away the data—the data does not matter—and the insight stays with me.** I become more insightful, and now I have a new map.

You need to develop your insight generation mechanism, which is nothing but Data Science. You prune that data, grow the insights, keep the ones you like, and throw away the ones you don't. Get those "children" ideas to marry each other, and the grandchildren will be amazing.

One of the methodologies you want to look at is: **Start Multimodal, take multimodal inputs, put in your own secret sauce (your domain understanding), generate ideas, and cross-pollinate them.**

I'll leave you with this question: **What is your system?**

**Anand**: Turns out [Claude](https://claude.ai/) has come up with some ideas. Here is Claude's thought: When we are abandoning a habit, let's not quit cold turkey. Instead, reduce it to 20% intensity for a quarter and check what we are missing. Effectively, that gives me a "soft delete" period where I can recover the high-value routines before they are truly gone.

What that means is, in the process of quitting whatever I want to quit, there would be some side products which are really behavioral assets, and we want to recover or retain those. It gives me a mechanism for how exactly I soft-kick habits.

When in doubt, ask AI. When not sure whether I'm in doubt or not, ask AI. This is also true when we don't even know _what_ to ask.

### Workshop: Vibe Analysis

We are going to do a little bit of workshopping. Please take out your laptops.

You will at the very least need a browser. You will almost certainly need at least the basic paid version of any of the popular accounts—ChatGPT, Gemini, Claude, whichever you have. If you don't have one, this is easily the highest ROI investment that you can make.

There is a [WhatsApp Group](https://chat.whatsapp.com/DUxeM59JBNH47Wmm1i5qRa). The invite link is [here](https://chat.whatsapp.com/DUxeM59JBNH47Wmm1i5qRa). This is where I'll be putting in my prompts. You can use this to copy-paste.

We are going to be doing **Vibe Analysis**, which is a take on the term "Vibe Coding." Vibe Coding was coined by [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383). The crux of it is: **You code, but you don't really bother about the code.**

Put another way: You want to get somewhere. Coding happens to help you get there. Your point is not that you are coding; the code is not the output. The code is just a byproduct.

Vibe Analysis works in exactly the same way. You are ignoring the code. You are getting the analysis done. The mindset that you are adopting is:

1.  **Pragmatic**: You want the output—the insights—not how they are coded.
2.  **Skeptical**: If someone gave you an analysis, you would want to verify and cross-check, even if you don't understand the code.
3.  **Playful**: You say, "Look, I don't know what can and cannot be done. Let's try and see what breaks."

With this in mind, we are going to analyze a few datasets. Let's pick some personal and synthetic datasets—not corporate data, because that requires too much permission. There is a ton of personal data that you can use: Google, your phone, utility bills, bank statements, medical reports, Netflix usage, Spotify, YouTube, Kindle, document collections.

### Data Source 1: Google Takeout

Let's start with **[Google Takeout](https://takeout.google.com/)**. You can access it by going to takeout.google.com. I strongly encourage everyone to go there. You will see a section that says "Create a new export." By default, it will select almost all of your data, which will take days to export. Deselect all of these.

There is one particular subset of data which is especially useful. It is called **My Activity**.

If you check what it includes, note that it includes your search history, YouTube history, video search history, map location data, Gemini conversations, etc. It does not contain content—no emails, no chats—but it contains _activity_ data. Put a check against "My Activity" and click "Next step," then "Create export."

For me, it took about 45 minutes the last time. Maybe by the end of this session, you will have this data and be able to start using it.

### Data Source 2: WhatsApp Export

WhatsApp is a great starting point. What you can do on your phone (not on WhatsApp Web) is pick any chat—pick a large chat that you can analyze. I'm going to choose an IIM Alumni group.

On the phone, click the three dots, go to "More," and then "Export Chat." Save it to your drive or Dropbox. This gives you all the WhatsApp conversations in that particular chat.

**Nirmal**: Some people were trying to get to the chat export on iPhone. On the iPhone, click on the top bar of that group, scroll up all the way, and you have an "Export Chat" option.

**Anand**: Good catch. This is the structure of the text file that it exported. It has data all the way back from 2022, which is when I joined the group. Lots of people saying lots of things. I've actually not been in touch with this group, so I don't know much of what conversation is happening there. Fair enough. Let's explore.

### Analyzing the Data

There are several ways in which we can do the analysis. One of the simplest is: **Give it the data and tell it to analyze.**

I'm going to open one window and give it the data—in this case, just the `WhatsApp Chat - IIM Global.txt` file—and I'm going to give it just one word: **"Analyze."**

This is interesting partly because I don't know what I want. It almost certainly would not know what I want. We have no idea where we are going. In a way, this is good. If I don't have clarity and I give one of my team members a file and say, "Just analyze and do something," whatever he comes back with is useful as a starting point. I can say, "No, this is not useful," or start improving on it.

Let it run. I'm going to have Claude run this analysis as well.

**Nirmal**: While that is going on, one of the things we used to run was a contest. Price is just status/leaderboard. We run a contest on **who has the maximum amount of time they can make an LLM think.** I ran this with my students. The maximum time is **239 seconds**. If somebody finds a prompt that can beat 239 seconds, we'll give you a prize.

**Anand**: Claude has come back with an analysis. It says there are about 122 active members as of November, split across a whole bunch of countries. There is a sporadic communication pattern. "Alumni Networking" is one of the top themes. A lot of talk about professional life—my move to Singapore, job losses, startup updates, requests for professional help. Personal support and community: one of my classmates had a medical emergency without insurance, fundraising groups, lots of nostalgia, and miscellaneous stuff.

It spotted who are the people emerging as coordinators and organizers. It spotted some problems: [PC] has been posting multiple blank messages (actually messages that were deleted), the need to add members who left because they were angry at PC, balancing the group's utility versus spam.

With just the word "Analyze," there are a couple of things at least that I am learning that I did not know about before. For instance, I didn't realize that a reasonable amount of the conversation was actually about professional help. I actually missed the 25th Reunion discussion in December 2026. I thought this was happening in 2025. No, obviously not, it's next year. So I need to get back into this conversation.

**This is the naive way of prompting.**

One of the things I will ask everyone to share as they go along is: **Anything that you learned from the process?** Please post on the WhatsApp group.

**Anand (on WhatsApp)**: "Learnt that the planning for the IIMB 2001 25th Alumni Reunion is ongoing and I missed it."

### Conversational & Narrative Analysis

We could also do the analysis in a **Conversational** way—just talk to ChatGPT.

> **Prompt**: "I'm sharing the transcript of the IIMB 2001 WhatsApp group. I'm a part of the group but not really actively reading. I definitely would like you to do two things: catch me up on some of the recent threads, and secondly, give me a sense of the overall conversation. Don't give me boring stuff. Give me interesting stuff. I want to find out stuff that is not so obvious, something that is surprising."

The advantage with voice prompting is that I can be a lot more verbose, which might give it some more context.

We can also do it in a **Narrative** way. I store a whole bunch of prompts as I go along. One of the concepts is **Style Transfer**. If I ask it to write in a certain person's style, it helps.

[Malcolm Gladwell](https://www.masterclass.com/classes/malcolm-gladwell-teaches-writing/chapters/reading-as-a-writer) writes pieces that I find very easy to read. He opens with an unexpected anecdote, about an obscure person or an event, zooms out... overall a great style. So I'm going to ask [Claude](https://claude.ai/) to take these conversations and **write in the style of Malcolm Gladwell**.

> **Prompt**: "Summarize the content of this WhatsApp thread of my IIMB Alumni group and write in this style."

This process—Style Transfer—is like saying "Paint in the style of Da Vinci" or "Picasso." LLMs have been trained on every master's style. By telling it to copy a style, it becomes a very powerful technique. I've used this when generating images. I wanted something obscure, so I asked LLMs to suggest unusual illustration styles. It came up with "Frottage technique" or "Decalcomania."

**Nirmal**: Observe the gentleman. Even when he is doing this, he is taking notes on good ideas. He is a stickler. **Do not separately look for data. While you are doing your regular work, your data capture should be continuous.**

**Anand**: This article begins with:
_"November 29th at 3:40, a man named [P Chidambaram], not the Finance Minister but my classmate, typed 13 words into a WhatsApp group..."_

I'm not going to go through it right now, but I'm going to spend this evening going through this article because it is way more interesting than the WhatsApp group itself!

There is nothing better than a [prompt like this](https://github.com/sanand0/prompts/blob/main/styles.md#non-fiction-authors) asking it to write in the style of a Malcolm Gladwell article to read regulations, corporate policies, or even medical reports.

### Analytical Prompting ("Investigative Journalist")

We haven't been doing much by way of _proper_ analysis yet. So let's get a lot more analytical. Here is a very detailed prompt that captures everything I have learned in the last 15 years about how to go about doing an analysis.

> **Prompt**: "Start analyzing like an **investigative journalist** hunting for stories that makes a smart reader lean forward and say 'Wait, really?'..."

It goes on to say: Look for the **unspoken**. What are people _not_ talking about? Look for **outliers**. Who is speaking too much? Look for **conflicts**.

I'm going to give this prompt to the LLM along with the data.

It's trying to extract date, time, author. It's parsing the content. It displays some statistics. Based on the data, it tells me that **Somnath** is the most vocal, followed by **Pawan**, **PC**, and **Shivani**.

And it analyzes their styles:

- **Shivani**: High frequency, short conversational bursts.
- **Pawan**: More the COO kind of style.
- **Don't mention World War III**: I don't know why that is there, but I'm going to have to go back and ask!
- Ask Shivani how her job hunt is doing.
- Ask Pawan and Vohra about their mountain trek.

This is useful. I do actually want to jump back in, and these are entry points that tell me what I can use to jump back into the conversation.

**This is something I learned: What prompts or texts I can use to jump back into the conversation.**

Plot twists are a good idea. I should probably do that as well. But we'll continue this thread and come back to that.

We could get a _lot more analytical_. What we _could_ do, is, and here's [another prompt](https://github.com/sanand0/scripts/blob/main/agents/custom-prompts/analyze-insights.md) that I have used in the past, and this is a very detailed prompt. Let me show you this. **This captures everything that I have learned in the last 15 years** about doing an analysis.

It says, "Start analyzing like an investigative journalist hunting for stories that makes a smart reader lean forward and say 'Wait, really?'"

It talks about how you understand the data. List the dimensions and measures, figure out what the types are, what is the granularity, and so on. Figure out what the audience really wants. **Look for signals**. Look for unexpected distributions which I find to be a consistent signal, what are breaks in patterns, and it goes on to explain in detail how to go about doing interesting analysis. It goes on to explain how to verify and cross-check. It goes on to explain how to prioritize all of this.

So I'm going to take all of this as part of the prompt and maybe pass it to ChatGPT and give it the file. Now for some reason, ChatGPT has been failing for me for a while. I hope it runs okay this time. Not sure if it's a ChatGPT problem or my system problem.

[Technical issue with ChatGPT]

This keeps happening and I don't know why, so I'm going to take the same prompt and give it to Claude instead, which is also pretty good at writing code. Once I upload it and have it run, I’ll mention one aspect which may not be very obvious.

The interesting thing here is: **not only can it write code, it can run code. And that is an ultra-powerful capability.**

I don't have to treat it like a system that can produce code as an artifact; **I can treat it as a box, a person, an analyst.** I give you the stuff, write the code, run the code, and give me the output. Not just that—write the code, run the code, and **if there are any mistakes, correct it yourself**. You're smart enough.

While we are at it, when the output comes, the program's output is not going to be particularly meaningful for me. You read it. You interpret it. And give me the answer. We've already seen how we can have it write like Malcolm Gladwell and do stuff.

But when this is done, I'll have it continue on the prompt that I shared which also goes into the visualization side of things, which is: **Give me the output in a variety of different formats.** Give it to me as an executive summary. Give it to me as an actionable report. Give it to me as a Malcolm Gladwell New Yorker-style data story. All of these are possibilities.

Now, like Nirmal said, you have to create your own prompts. What works for me won't necessarily work for you. Partly because you don't have the context now. I've been reading the New York Times graphics team's output on a day-in-day-out basis. You may have been reading Charlie Munger. Who knows? **What works for you is what you need to craft.**

But the good part is crafting your prompt is very easy. For my style transfer prompts, all I did was, for instance—yesterday I was reading a piece, the Kalama Sutta, some of Buddha's writings which made no sense to me. And I said, "Find out who is a modern writer who would be a good person, writes easy text etc., that I could use to rewrite the Kalama Suttas." And it said Pico Iyer. And gave me a one-sentence description of Pico Iyer's style of writing. I said, "Write in the style of Pico Iyer." Beautiful reading. Close to the original, very well written, makes my life easy.

Let's see how far this has got. It's still writing the program. Okay, now it's digging deeper into the most intriguing patterns. This prompt will go on for a long time because I've given it such detailed instructions that it will run for a good—hopefully more than 200-odd seconds.

But we will continue. These are not the only formats. We can just put it into [NotebookLM](https://notebooklm.google.com/)—I'm sure many of you have tried NotebookLM. It's fabulous. What I'm going to do is create a new notebook and upload the file that I had. I’m going to give it a title, which is the "IIMB 2001 Alumni WhatsApp Group" and add it as a source. NotebookLM will take that data. It will play around with it, do some introspection, whatever. And once it does—I've completely forgotten what the interface looks like now, but there is a way for me to create a podcast.

[Clicking Audio Overview]

And it turns out that I have an edit icon here where I can choose a deep dive, a brief, a critique, a debate. I like debate. What should they focus on? "What are the most controversial topics discussed in the group?" Also, "What is the personality of each of the people?" Let's give it a shot and generate.

This is going to take its own sweet time. 10, 12 minutes. In any case, I'm probably not going to be able to play this out to you. But when I'm out on a walk, I just put on one of these podcasts and play. **It's a great way to catch up on stuff that is far more engaging than the original content.** And the multi-modality which Nirmal commented on earlier works both ways. It's not just that you can talk to it; it's not just that it can respond back to you. **You can have it generate content that you can listen to offline as well.** Very powerful.

Let's take—before we go on to the next multi-modality—just do a quick check on the chats. I encourage you—if you've started seeing any results, I do encourage you to put in any kind of insight that you have. I'll be sharing a whole bunch of things. This talk is anyway recorded so you can always go back to it. Better yet, you can have an AI coding agent tell you what are all the things that I said. But the _doing_ is often more fun. The _interpreting_ is more fun. So give it a shot. Try it with your data. Let it run in the background. What's the big deal?

Another thing that I try very often is creating sketch notes or infographics from the data. You can use Gemini, and Gemini's image generation capabilities are particularly powerful. I'm going to take the same text that I had used there: "Create a sketch note based on the most important parts of this conversation." Let's also have Gemini not just create a sketch note, but an infographic. "Analyze the data"—and this time let me not paste it, I will upload the file. Let's see if it's able to do a combination of analysis plus image generation. "Analyze the data from my IIMB 2001 Alumni WhatsApp Group and create an infographic."

This might fail. I've never tried this before. It may say, "Wait, hold on, I can either generate the image or I can do the analysis." Or, "It can just generate the image without doing the analysis." I suspect it's doing the latter, but we'll find out.

Okay, it's thinking. It's thinking a lot. Okay, and here it is. So, a sketch note that summarizes the conversation. So there's a bunch of stuff about batch endowment, campus visits. Yeah, this is actually easy to read. Sangeeta moved to Vietnam—oh, I didn't know this. Chennai Adyar Matsya, okay. Useful stuff. An insurance top-up scheme, okay, I need to check on that. Celebrating wins. Yeah, and at least one senior passed away. Junior/Senior. This is still creating the infographic. Let it run. We can always continue.

And there's lots more. I'm not going to go into all of the other formats, but there's an entire page on things that you can do further. But we can take another dataset and play around with it.

One thing that you can do is use that dataset that you upload—a dataset could be a bunch of documents as well as we've seen—and then ask it specific questions. "When did Sangeeta move to Vietnam?" Fact-check this thing. "Is the insurance rate really going up?" Cite the sources. "Who said what?" Are there any issues? Make it interactive. Just drill down into the conversation further.

Run scenarios. "What if X happens?" And it could be quantitative. "What if a new person comes into the group?" "What if my blood pressure shot up by whatever percent?"

**Nirmal:** So yesterday I heard an interesting idea. This was the NASSCOM daily summit again, an amazing summit. So dating is difficult. What they created is an app where you have an AI Avatar which dates the other person's AI Avatar, and the AIs date together. And they go on a few times and then they have a few fights and then you see whether the relationship is compatible or not.

Okay. Geeky idea. So here's my take on it. **It's a powerful risk-free simulation analysis.** I'm going to replace that dating with your finance manager. And the relationship scenario with how that person is going to work. Or with a candidate. And how that candidate is going to fare as the new CEO of my company. Or I create a persona for your company as a startup and then say, "In the China versus India war, how is that company going to fare?"

**So "What-if" scenario analysis is powerful because you start getting early warning signals.** And basis those early warning signals of a future that ain't happened yet, you can start figuring out what to do.

**Anand:** And these counterfactuals can work the other way as well. Which is: "What if in the past we had taken a different decision? Would we be here? Would we be elsewhere? What's your guess?" Now, it may be right, it may be wrong. We need to verify. And there's a whole bunch of ways of verifying.

One is simply to ask the same question to five different LLMs. Take the answer from one model, pass it to the other and say, "**Fact check this. Critique this.**" Pass it back to the original and say, "Look, that guy said this, what do you think?" See if they converge, see if they diverge. How often do they converge? How often do they diverge? It's like watching a group discussion between a bunch of people except that I have to take the conversation and paste it here and so on. Which is not that much of a problem. We can have it teach us what it did. "What you did on the analysis side—I want to be able to do next time." Apply systems thinking. What are the causal loops? Which are the levers that I can slide more for higher impact? What are the weird anomalies? All kinds of things. None of which were in any of my prompts so far, but we can keep going like this.

Do share whatever you find. I saw a few more... Ah, okay. You got a monthly sentiment—oh that's cool, Amit. And a list of issues, suggestions, benchmarks. That is lovely. And there's an angel group as well.

**Question:** (Vinod) On privacy. Giving chat history to an LLM.

**Answer:** (Anand) Vinod, your question on privacy of giving chat history to an LLM is an important one. How do you prevent LLMs from using this data? So there are three parts to this:

1.  Am I allowed to have the data?
2.  Is the LLM owner allowed to have that data?
3.  Are they allowed to train on it so that future people can access it?

Let's assume that I have access to the data and I'm allowed to use it. Now, if I'm running it on a local model, then concerns number two and three vanish. I am obviously allowed to have it, so my machine is allowed to have it. And local models are with us. The open source models are becoming more and more powerful, but it requires a certain amount of technical expertise to run them. Not too much. If you're able to run Excel, we can run a local model these days.

But if I am uploading it onto a server, then it depends on the server. If you uploaded it let's say to OpenAI, and you are _not_ using a paid account, then OpenAI's deal says that "We are going to be using your data to train our models." But **if you use a paid account, they say: A) We will not look at it. B) We will not train on it.** That gives you certain guarantees.

If you are using your organization's Azure account or Google account or AWS Bedrock or whatever, they're providing even stronger guarantees. They're saying: A) We will not train, obviously. B) We will not look at it and this is audited. C) If you get into a lawsuit, we will fight your case for you. Which are strong guarantees. So in short: **where you put the data in determines how much of the privacy concerns you're addressing.**

**Nirmal:** Just want to weigh in on that. Regulation is still up for grabs. People haven't even understood AI, where is the regulation? Regulation is going to take a while. So one of the regulations that people are fighting for—Balaji of Network State is one whose championing this—his concept is **"No undisclosed public AI."** So you want AI to disclose that it is generating AI slop. So you want every single disclosure that is in public has to be verified and so the AIs need to have an identity. And that's the conversation that's happening today. And that's the debate on whether that can be done, cannot be done.

**Anand:** By the way, I also asked it not just to do the analysis but to give me a New York Times-style data visualization which it has. And... "Inside a WhatsApp group that survived 24 years." Okay that's not true, the group is 24 years old, the WhatsApp group is not. And it goes on to explain in a nice story... Wow. I tell you this analysis is way more interesting than the group. And it's not that the group is uninteresting! "Median member posted twice." "They lurked and watched." That's me broadly. "44% solution." Okay, yeah, no. Something that I'm going to have to sit and read. But here's the thing: **if a WhatsApp group can be converted to this with me mostly just copy-pasting my well-thought-through prompts—but even without it you'd probably just be able to say "Create a New York Times data visualization" and it would come up with this—take your RFPs and do it. Take your supplier contracts and do this.** At the very least, it becomes easier to read.

My original plan was to continue with more datasets, deeper analysis, go into synthetic data, how one uses that synthetic data and creates business analysis and stuff like that. But we have nine minutes. Doesn't really make sense to do all of that. Let me just say that lots of things are possible. Your imagination is the limit. You'll figure it out. If not, you will ask people. And as Nirmal said, bring AI to the table. "Lots of people" includes AI. So ask AI and you'll be able to figure it out.

Let's take questions maybe?

**Question:** (Raveesh) AI's output on both the correctness of the research and the accuracy of the output.

**Answer:** (Nirmal) Ask AI to cross-check itself. AI cannot lie. So you can actually ask the same AI to cross-check itself, or you can pass it to another AI to cross-check. Or you could ask for fact checks. Or Perplexity does a good job because it verifies.

**Answer:** (Anand) For analysis, here's how I do it. It's the part that's highlighted on the screen here. [Refers to slide with prompt].

**Nirmal:** What is hallucination? **Hallucination is the fact that you've asked a question and it has used the context that it is orange color instead of fruit.** So there are paths where there is some ambiguity and it's taken the other path which you were not interested in. So if AI is not hallucinating, your prompt is not clear.

Let's be clear, what are we charging AI with? Why are we charging AI with accuracy? It's an autocomplete model. It's a probability that this can be a novel. So I asked for "2074 Indian science fiction cyberpunk themed stories." It gave me a top 10 list because that's the genre I'm writing in. And number five was a fascinating story I couldn't find on Amazon in any place. So I said, "This book is fascinating." It not only lies, it also lies beautifully. So notice I'm saying it also lies. **So why are we charging it with veracity? It is an autocomplete model. It's a potential autocomplete. That's all.**

**Answer:** (Anand) Yes. That's the reason why Perplexity has added the search capability and said, "Here's a reference." And even that reference could be nonsense because there are jokers who sell real estate on the moon. There's no law in the US against that.

**Question:** (Audience) High accuracy outputs. [Garbage in, garbage out concern].

**Answer:** (Nirmal) Let's get very, very candid about this. **50% of data in the world is always dirty.** There is no concept of clean data. Show me an organization which has clean data, I will eat this pen. There is no such concept. There is dirty data everywhere. And that dirtiness is a function of where is the source. I mean if Donald Trump says something, I know what whether to believe it or not.

**Question:** (Audience) I have a specific software style/code structure. I tell the specs. It generates code. But who are you replacing?

**Answer:** (Nirmal) Correct. So he needs to know the _map_ of the software coder. He needs to know what are the themes that the software coder goes for. Like what Anand had, he had a clear sense of: "First check outliers, then start looking at missing values." **So you need to know their recipe. And you need to know the specs of that recipe.** Without the specs of the recipe, you're just saying "You go ahead and code," I don't know what kind of coding style, then it will assume whatever coding style it wants to.

**Question:** (Audience) How much is prompt engineering vs getting output?

**Answer:** (Nirmal) And there are prompt libraries on the internet for free. You can go and download prompt libraries. There's enough and more people sharing prompts. So I copied one such prompt library which I use. As an amateur life coach—I don't claim to be anywhere good at it—so what I do is with my client's permission I record the conversation, I put the transcript, then I run a prompt which looks for cognitive biases in that transcript. And then I cross-check that human and then go back to my clients.

**Answer:** (Anand) [PromptHub.com]. **The largest investment that I've ever made in my life, I made a couple of months ago. It was solely based on ChatGPT's recommendation.** The model was GPT-5 thinking [likely referring to o1/latest model], which was the second smartest model in the ChatGPT suite at that time. The prompt that I gave it was a very long and detailed one which roughly summarized: what is my risk preference, investment, some constraints in terms of tax and things like that. And I said, "Look, I'm going to put my money into mutual funds. What I want you to do is first conduct an analysis. Tell me should I be going in for equity, debt, blah blah blah... figure out what all the categories are that I can invest, if I'm investing in India. Figure all of those out and tell me given the macroeconomic situation of the next five years, what are the various scenarios that are possible? In each of these scenarios which ones are likely to do better, which ones are likely to do worse? Do a certain amount of sensitivity analysis and based on my risk profile tell me which category I should invest in."

And for that particular prompt, it agreed with my prior assessment which is that I should be putting my money into debt funds. Then I said, "Now go through all of these—I'm interested in a slightly lower cost ratio, I want [usual parameters you would tell a financial investor]." It did extensive research. I cross-checked it—I mean it is a lot of money—and it looked so sound that I just straight away took its recommendation and put my money in.

There is a fair bit of research these days on which professions are overtaken by AI. That is, the average general practitioner versus AI, the average lawyer versus AI, the average paralegal versus AI, the average nurse versus AI, the average financial advisor versus AI, and so on. **And the average personal financial advisor is beaten by the majority of the top models as of the last few months.** So, short answer: Yes. At least for personal investment. Depending on the kind of financial investment you make and the kind of model you use, might or might not work out.

**Question:** (Suresh) How to analyze semi-structured data? Reading annual reports/stock picking.

**Answer:** (Nirmal) Andrew Ng has released a complete agent that will read everything that is there in all of those and give you a full detailed analysis so you don't even need to write the prompt. You just take his agent and run it.

**Answer:** (Anand) Just follow Andrew Ng on LinkedIn. He puts all this out. Every time he writes five tweets, follow him on LinkedIn. He'll tell you exactly what it is. And maybe we'll send some of this out to the group later.

**Answer:** (Nirmal) `agents.ai` is a guy called Dharmesh. Dharmesh is the guy who is the CTO of HubSpot. He's written about some 2000 agents in the last—Anand, what did he name? Thousand agents? I don't know how much. He's written thousands of these things that you can go [use].

And if you really want something, but as a professional—meaning if you want to say "I want to analyze five annual reports as an investment professional"—then you really need to do what Anand said. **You have to go in there, you have to understand the domain.** I don't know which of you are in the equity service but you know the questions that you normally ask in a meeting. The questions that you see on a PowerPoint, when you go to some CFO who's saying something. You can also get a cheat sheet of questions by going to every earnings transcript there is, just take all the questions that are asked in that and dump it in [the prompt] and say "Here are the questions." All of these will give you a pretty professional output on any company, any industry, on any comparison.

**If this is your job in financial services, 3 years from now, bye-bye.** Or maybe, I don't know. Maybe it's deepens. But I'm just saying that is the kind of stuff that it is good at. I don't know whether it's very good at Math. Math is a separate field.

**Nirmal:** There again you've got to break it down into small processes and build a workflow for that. **Don't outsource your domain expertise to the AI. You bring in your domain expertise and then you start using [AI]. That's the thing.**

So, ladies and gentlemen, we've got another minus 6 minutes to go. And so what we'll do is we'll continue this conversation over WhatsApp and be happy to come back as well.

People have started using AI as just that catch-all for "What is the best book?" or whatever advice you need. **There is AI slop out there.** There is enough and more AI slop out there. And apparently just a month ago the AI generated content has overtaken human generated content. Just about overtaken. That's apparently just the last month. Which means that there is AI is creating an echo chamber in terms of AI data itself. So all that is going on.

**Host:** I think this was the first in a series of knowledge sharing sessions that we want to run as a community. So I'll run a poll across with the group and just understand a few things, whether you are interested in more sessions such as this. Because what Anand couldn't cover—I think what I requested Anand and Nirmal was to be a lot more technical, which he was hoping to add on. How can you really look at a specific business use case, how can you do a little bit of proper vibe coding and make us go through this. So we'll run a poll and let us know what the interest level for these sessions. But otherwise, just a show of hands, would you guys like us to run more such sessions?

**Audience:** [Show of hands/Applause]

**Host:** So thank you so much for your time. A small token of appreciation for Nirmal. And again thank you everybody for attending this and good night.

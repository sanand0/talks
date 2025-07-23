# Transcript - Manufacturing (IoT performance)

# Transcript - Supply Chain (Fleet utilization)

There's only one message that I want to deliver, and that will become obvious as we go through. But the message is simply that with LLMs, you can replace a significant chunk of your data analyst or data science teams. It's increasingly becoming possible.

Now, one of the things that we've done for our clients is take a classic fleet utilization problem. They said, we have a fairly low utilization on our trucks. There's a cost leakage, that's a problem with working capital, that's a problem with service levels, that's a problem with emissions. Now, what we'd like to do, they said, is set up a team and bring in domain experts. We'd like to bring in technological experts. We'd like to bring in analytical experts, put them together, and maybe in a month, we can create something, give us a dashboard that helps us make decisions on what we need to do. And that's the norm, that's how we approach it today.

In fact, one of the managers reached out to their team members, a logistics analyst, and said almost exactly this, this was roughly the email. He said our fleet utilization and service KPIs, they're being reviewed by the leadership.

"Here's six months of dispatch level data across some of our fleet lines. Now, could you pinpoint what is driving the empty kilometers that we have? Why do we have a low load factor? And what are the top fixes that we can make on this?"

And he didn't explicitly say this, but paraphrasing him, he said, "look, I want you to come up with creative hypotheses that are really grounded in the domain, your understanding of the data. And I want to make sure that the results that you get are verifiable and robust. I want to make sure that they're statistically significant. But also, please don't use your analyst language. Give it to me in terms that I can take to the leadership. Give me concrete, actionable recommendations."

And it was a large dataset. I anonymized some of that, and it has about, let's see, yeah, about 15,000 rows of dispatch level data where we have this was the kind of payload, this was the trip plan, this was the actual trip distance, how long, how many stops it made, over what window, when the dispatch arrived. A whole bunch of things on efficiency. Data was fairly well consolidated and put together.

With some details around what each of these columns are. Now, option one, have the team work, and the team did in fact give an estimate of a month and deliver it.

Option two, why don't we put this into an agent? What if LLMs could be the analytics team? And this is where I'm getting to the one message that I want to deliver, which is that LLMs have the ability to code. They have a reasonable amount of domain expertise. They're about as good as someone with maybe three, four years experience today. And they have the ability to correct themselves if they go wrong.

So, I'm going to actually take this, literally this email, and put it into the Strive Intelligence tool, which is an agent. I've already uploaded the data set out here. It's large, but it should be able to handle it. I'm going to give it some of the context on what these columns are. And yeah, that was the entirety of the email. And let's have it run it.

Now, it functions very similar to how ChatGPT works. It first thinks a little bit. It says, let's expand this. The user wants to analyze the data. They've shared some parameters. Now I'll start by loading and analyzing the dispatch levels. It has access to a container, meaning it has access to code, both the ability to write code, as well as the ability to run code.

So, it's read the file that we've uploaded. It's understood that these are the kinds of columns. So it knows by itself that it's dealing with a data set that contains various columns related to fleet operations, payload, capacity, etc. And it goes through, looks at a few of the parameters, and starts finding the correlation between the features and the load factor, the empty kilometers. Effectively, we've asked it to figure out why do we have empty kilometers? So it's looking at the correlation. And it's seeing that some of these are highly correlated, some of these are not so highly correlated. Looking at the correlations, and it's going on and on and on. And it's made a mistake here. It's correcting itself. It's going on and on and on.

Effectively doing the work that an analyst would do, that a logistics expert would do, both in terms of hypothesizing, as well as in terms of analyzing, creating the statistical analysis. And let's ignore all the thinking that is being doing behind the scenes. But after about half a minute, it has come up with a set of conclusions. Firstly, that there's poor consolidation.

That there is, every time we improve the consolidation score, that adds about 5 kilometers of empty running. There's a lack of backhaul. If we have loads that don't have a return trip, that's 36 kilometers more of empty kilometers on average. That's useful to know. And there are traffic delays that are causing it. And these are your top three factors.

This is a solid starting point because in half a minute, what we have is a full-fledged analysis of what are the biggest drivers of empty kilometers, as well as of low load factors.

And it goes on to explain in business terminology, look, what you need to do is consolidate. Raise the cutoff times and start pooling the orders. Expand the backhaul operations. Make sure that you outsource the return loads. Partner with third-party logistics. Right-size your fleets. You want smaller deploy vans. You want dynamic routing, and you want weekend scheduling to be consolidated. Effectively, five clean, actionable recommendations based on the data at one shot.

Now, if we have this kind of capability, the ability to have a first point of support with an analytics team is replaced by the first point of with the LLM or an agent like this becoming the first point of contact.

What we're seeing though is that it's not just analytics teams that LLMs are replacing, it's full-fledged development teams that are getting replaced as well.

One of our clients said, look, we would like a team to come in and build an application where people on our frontline can walk through the shop floor, take a picture, and find out if there is a safety violation that's happening on the fly. What's your estimate of how long it would take to do this? Because our team, they said, had come up with an estimate of about three months, four people to get this done. Is that how long it will take? Is it possible to get it done with higher quality?

So we said, let's try a slightly different approach because we do find that LLMs do a great job of writing code. So could we, in fact, let me put this in, build a web application that lets the user take a picture from their webcam, send it to an LLM, identify all the objects in the picture, and find out if there's a safety violation. I'm sending this to Bedrock's Claude 3.5 Sonnet model.

Now, what that does is, firstly, bear with me, that was not a. Oh, okay. Vertex. Any one of these models should work fine, give it a shot. Yeah.

Now, what it does is, first, acts as a business analyst. The first agent is someone who understands the requirements, translates that into technical language. And the second agent is a coder that goes through, sits and writes what the application code should look like.

Once the coder is done their job, the third agent, which will get triggered in a short while, is a deployer agent. And that deployer agent creates the application, pushes it onto a deployment server, and we have this. Let me maybe put that out here, take a picture. And with that picture, it's probably already sent it to an LLM. And yeah, it doesn't seem to be any visible protective equipment, such as a hard hat or safety glasses, which are generally blah blah blah. So it appears and it appears to be an indoor office, so maybe this is not a violation. And specifically, if it's controlled, then I can analyze for more safety violations.

What we have here is effectively 12 person-months of effort estimate, condensed into approximately what took a minute.

This doesn't always work. What we're finding though is sometimes when it works, it's magical. And a big part of the change in behavior we're seeing in organizations is to start discovering these low-hanging fruits. Creating a queue of tasks that can be done by LLMs, and when they can be done by LLMs, it offers a huge boost.

Lowers the cost to the point where people are now starting to think, what if I could have this particular application built? Where earlier it was prohibitive, I would have had to interact with a development team, I would have had to hire a vendor, I'd have to do all kinds of stuff. Now I can just give it a shot. Possibly even by myself, because all it takes is this kind of a description. So it doesn't even need a full-fledged development team or even for me to interact with anyone, and get it deployed.

We've done this internally at Strive. We've had non-developers start building applications like this, and as of this moment, there are about 2,100 applications that mostly non-developers have built as utilities all by themselves.

I mentioned that there's only one message that I wanted you to take away. It is primarily that increasingly analytics teams and development teams can be replaced by agents. We are now at that stage where that's possible. We are seeing it happen. A big part of the transformation effort is figuring out what kind of work can we give to these, because now you can give a thousand tasks, and they can get done instantly. And how do you start integrating it into the organization?

Do reach out if you'd like inputs on how we're seeing this used in practice. But do try it out. This is real fun. Thank you.

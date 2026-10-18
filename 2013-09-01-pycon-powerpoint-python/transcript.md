# Transcript

<!-- PyCon India 2013, 1 September 2013. Original video: https://youtu.be/aKCXj1DyEhM. Transcribed from original audio with ~/code/scripts/call (Gemini 3 Flash Preview) on 17 Oct 2026; timestamps refer to the video. Automated draft, not yet manually verified against all speech and slides. Unclear words or speaker attributions should be checked against the video before quotation. -->

**Anand**: [00:00] I’m sure a lot of you would be wondering what the heck is PowerPoint doing in a Python conference. You'll see how among other things it made me a decent chunk of money. But more importantly, I've been programming in Python since 2009. I've been programming in PowerPoint since 96. So in that sense, I’ve got a little more credentials to talk about PowerPoint than I do about Python, probably by an order of magnitude.

**PowerPoint is one of those few tools like with Excel and Word that exists on a lot of desktops and many people that are working with numbers, data, and communication are using these tools. And they are rather underrated.** Specifically, the ability that one has to program in PowerPoint is not commonly known even though it's extremely easy. 

So I'll be walking you through a few examples of this, but before that, let me just quickly tell you that the code base for this repository is on my Twitter stream, my Twitter handle is @ananth0, and the code base is actually also at my GitHub repository, which is what that will point to. So whatever you miss out on, please feel free to go over here and pick it up. I’ve already posted the code.

Let’s start by looking at how one creates a PowerPoint slide with Python. All you need is a library—well, firstly, you need Windows and you need PowerPoint. They cost money, or not, but assuming you've got them into your system one way or the other, all you need is `pywin32`, which is a library that allows you to use COM, the Component Object Model, to automate PowerPoint or any of Windows' features. 

**The Component Object Model is one of those useful things that Microsoft’s come up with where using almost any language, you can script almost any application, and PowerPoint's one of those examples.** So what I’m going to do is import `win32com.client`. That’s the COM client. I’m going to create an application which is `win32com.client.Dispatch`. I’m just typing the line that’s out here. I might as well copy-paste it. And when I execute that, nothing happens, which is not what I expected. 

Do I already have PowerPoint open? There we go. So we’ve just opened up PowerPoint on the right-hand side and that was done using the code that was typed out here on the left-hand side. I’m going to keep typing stuff out here and executing them. To begin with, what we have on the right side is just a blank presentation. Let’s add a slide to that. 

Okay, so that’s created a new presentation with a slide. Now let’s add a shape to that. I’m not showing you the commands yet, I’m showing you the output first and then we’ll walk through the commands. Now I’ve got a circle added to that. 

Let's look at the code that we have for this. We’ve opened `win32com.client`, we’ve created a new application which is a PowerPoint application, we created a new presentation `application.Presentations.Add`. We've said `base` is equal to—I’m just calling it base, call it what you want—`presentation.Slides.Add(1, 12)`. Now the 12 here happens to stand for a blank layout. I’ll tell you how you figure out stuff like this later. And finally, we add an oval which is `base.Shapes.AddShape(9, 100, 100, 100, 100)`. 9 stands for an oval. So this number nine here, that tells me to draw a circle at position 100, 100 of width 100, 100, which is what gave you that circle out there.

**Anand**: [03:52] Simple so far and unimpressive so far. What can we really do with it? Well, **what you can really do with it is create any kind of visualization that you can do with HTML, with processing, with Java, whatever, in PowerPoint. Now why does that matter? Because a lot of people want to annotate stuff.** 

We were doing a piece of work at Novartis where they said, "Look, all of this is really fancy, but you know what? Ultimately, this is going to go into a presentation for one of the people in our board. It’s going to go into a presentation for one of their directors that will ask all sorts of questions to which there is no system-driven answer. We're just going to have to write this out, we're going to have to point to stuff, we want to be able to draw arrows, we want to be able to play around with it, and we're used to PowerPoint. Could you just give all of this in PowerPoint instead?" 

I’ve heard the same thing at P&G, I’ve heard the same thing at Unilever, I’ve heard the same thing at Walmart, I’ve heard the same thing at Nokia. Even our team says sometimes it’s just easier to play around with it in PowerPoint than it is in most other tools. And because we have it, well, let's take an example, let's take this a little further and see what we can do. 

Firstly, before I go ahead, I would also like to mention the same is applicable for Excel as well. I could open up Excel and start putting in—adding a worksheet, in that add a circle. I could also start taking the cells—you know, the first cell put in the value "values," then put in numbers in the other cells. And when I execute this, it’ll open up Excel and start putting in the values. Let’s run that. 

So I’ve got Excel open. This, incidentally, was executed by the script, in case you were taken in by the speed of it. Let me close Excel. I don’t have Excel open, I’m going to execute this again and that creates an Excel application with a circle with values and so on. Cool. 

Let’s get back to PowerPoint. Let’s start doing some interesting stuff with it. Some of you might know that I’m a hardcore movie fan. So I sort of live on the Internet Movie Database (IMDb) top 250 movies most of the time. And one of the things that I’ve been wanting to do for a long time is just to look at all of the posters at a glance. I just like looking at those posters. 

So let’s start pulling those posters and putting them onto PowerPoint. I’m going to sort of run through the easy bits first—the getting the posters. I’m using `lxml.html` from which we're going to parse the stuff. We take `imdb.com/chart/top` which is the list of the top 250 movies and when I load that, what I eventually, hopefully, will get is a list of movies with the topmost rating going to *The Shawshank Redemption*, all the way down to *Three Colors: Red*, never heard of that one, and *The Untouchables*, and so on. 

Let's just pull the links for each of these movies and once we have the links, we can get the posters from inside that. So you go inside, this is the poster. To get the links here, I just happen to know that this is the second or third table in the list. So once we parse this URL in `lxml`, we just find all the anchor elements that are inside the third table, which is table of two. And to confirm that we’ve got it right, let’s print the first movie’s text content. In case you think that I’m going a bit fast here, this is meant to be a tutorial on PowerPoint in Python, not `lxml`, so don’t worry about it. 

So yes, it’s gotten *The Shawshank Redemption*. We are able to retrieve the movies. So this array `movies` actually contains all of the anchor elements and I can get the 10th movie or whatever movie I want like this. So the 10th is *Star Wars* and I can also get its link via `get('href')`. Now that we have all of these movies, we can start extracting the posters from those. 

But before doing that, I’m going to import a library called `mso`. Now this is something that I’ve put together. There are a large number of constants that Microsoft Office defines. These constants are a little difficult to remember or even to copy-paste. So there’s this file called `mso` which has a large number of predefined constants, and what you’ll find is that it's easy to copy-paste from Visual Basic. I’m just going to import this, we’ll come back to this later. 

So let’s import that. Now let’s start scraping the movies. Now before we scrape the movies, let’s just get a sense of the layout that we’re going to plot them with. There are 250 movies, let's say we plot them as rectangular posters that are 25 wide and 10 tall. So initially, I just want to see if I can create 250 rectangles at the positions that I want them to. Let me show you what the output is and then we’ll come back to the code. 

**Anand**: [08:37] It's probably finished—okay, finished drawing. You probably want to see it being drawn, so let me keep this on the left and run it. Yeah, so rectangle by rectangle, it’s patiently drawing. Now there are some interesting quirks about how fast PowerPoint draws this stuff, which again I will come to in a while. 

But anyway, what we're doing here in the code is just looping through all the movies, we calculate the X position and the Y position to roughly fit a 25 by 10 grid and then say `r = base.Shapes.AddShape(mso.ShapeRectangle, x, y, width, height)`. This `mso.ShapeRectangle` is something that’s defined in that `from mso import *` that I pulled in. And it has a huge bunch of constants, you just open the file, you search for the constant you want and paste it in here. And as with all other shape commands, it takes the X, Y, width, and height. So as we loop through, it’s created all of these rectangles. 

Now let’s get the posters. This is where I’m retrieving the posters. I’m just going to run it first. It actually runs pretty fast because I’ve got this cached locally. What we're doing here is looping through all the movies, if I’ve already downloaded the movie then skip it, if not, go to `imdb.com/` the `href` of that particular movie and parse the URL. Inside that, find the `img_primary/img` tag and from that get the source and save it into a file name of the movie. That’s pretty much all that’s happening here. 

So somewhere out here I have a folder called `img` which has all of the posters with the file names being the MD5 hash tags of the MD5 hash of the URL. So we’ve got all of the movies sitting in my hard disk. Now let’s see if we can put the same thing into PowerPoint. 

I’m taking the same code as before but the only change that’s being made—we're again looping through all of the movies, we’re taking the X and Y—but the only change here is that instead of `AddShape`, I’ve got `AddPicture` and the first parameter is the absolute path of the file name of that movie. There are a couple of other parameters as well saying link to the file, don’t just take the file internally—saves a bit of space—and save with the document, don’t save it with the document, because that way I don’t have all of the images sitting and taking up space inside the document. But other than that, there aren’t any changes to the code. 

So what this will do is—let me run this. Did I run it? Let's run it. Okay. Okay, it’s drawing the movies one by one. Now you notice that before I switched to this slide, it actually drew them pretty fast, but now it’s being fairly patient about it. One of those quirks of PowerPoint. Like Heisenberg's uncertainty principle, if you observe it very carefully, it tries to be a bit more slippery than it normally is. 

But **there is a way around it, and this is perhaps my greatest discovery of this year: that if you hold this, if you keep dragging it, it's pretty fast.** Let’s—I’ll show this to you, okay? Let's not create a new slide, I’ll just put this stuff on the same slide. Now it’s slow, right? Let me drag it. Whoops. 

I’ve spent several hours just keeping the PowerPoint window dragged so that this damn thing can get done in time for a project. My colleague Nikhil here can attest to that, he’s been doing the same thing as well and so have a bunch of others. So what do I really do when I’m watching a movie at home? Having one window on the PowerPoint keeping it dragged. 

**Anand**: [12:31] Now, so what we have is—let's spend a bit of time on the movies as well. The movies are fun too, in fact, probably more fun than Python. So we have them sorted by rank, so that’s the top-ranked movie *Shawshank Redemption*, *Godfather I*, *Godfather II*, *Pulp Fiction*, *The Good, the Bad and the Ugly*, and so on, all the way down to all of these movies. 

Fine, posters look nice. I don’t quite know what some of these movies are, though. So this one—I think you can guess that one.

**Audience**: *American Beauty*.

**Anand**: *American Beauty*, okay. Let’s do a quiz. This one?

**Audience**: *Goodfellas*.

**Anand**: Good one. This one?

**Audience**: *Bourne Identity*?

**Anand**: *Bourne Identity*, is it? Okay, I wouldn’t even know enough to verify that. Okay, what about this one?

**Audience**: *Eternal Sunshine of the Spotless Mind*.

**Anand**: Think so? Okay. Let’s try one last one. I’m hoping I can find something that you won’t get. What about this one?

**Audience**: *Ran*? *Kagemusha*?

**Anand**: Okay, at least there’s some debate around it. Well, **at the very least, I would like on hover to see what the movie is. And when I click on it, get to the actual movie, right? Let’s do that. Now that’s fairly straightforward.** 

In PowerPoint, if I wanted to do that, I would right-click on one of these movies, select hyperlink and pick whatever is a URL. So let’s say this was the URL, I pick that and I select screen tip and say "name of the movie" and say okay. When I do that, this particular movie, as I hover over it, I get the name of the movie. It may not be too visible from the back, but you’ll get it, whereas you won’t for the others. 

Let’s try and automate this portion. The code for that—as before, let me run this and show you the output. Drag it for a few seconds. There, done. 

Okay now, hover over—what is this one? This was *Mystic River*, some of you might have gotten that right. This one is *The Bourne Ultimatum*. This one is *The Untouchables*. This one is *Eternal Sunshine of the Spotless Mind*, got that right. So on. Let’s click on one of these. Let’s take *Goodfellas*. So I click on *Goodfellas*, it opens up *Goodfellas*. Clean. 

So I have practically a web-kind of environment. Not too bad. 

**Anand**: [14:51] Let’s go further. I haven't shown you the real cool stuff yet. See, one of the problems is while I can figure out what the movie is, I can’t quite easily identify where a movie is. So on this list, I want to be able to see—find the poster for, I don’t know, *Gandhi*. It’s an order of $N$ search, it’s not order of $\log N$, which is what I’d like it to be. 

**What if we could sort this alphabetically? Now you say that’s easy, just sort it alphabetically instead of whatever order you have. Yeah, but I don’t want to either sort it alphabetically or sort it by rank, I want both. I want to be able to click on a button and then it’ll sort alphabetically. And click on another button and it’ll sort by rank.** 

And being ambitious, I also want this to look nice. I don’t want it to just change slides or anything, I want it to move. I want to see where it’s moving. Let’s do that. 

Okay, I’m going to as before execute these commands first and then show you what exactly is happening behind the scenes. Let it run. Okay, it’s drawing stuff. Drag it. Now this case, it’s doing a lot more, so I’ll have to keep it dragged for a whole lot longer. As you can see, that didn’t quite do the job. 

You may notice that I’ve got two buttons out there. Well, not buttons, two rectangles, I didn’t have time to make buttons. Two rectangles out there titled "Alphabetical" and "By Rating". Let’s see what happens. Right now, it’s sorted by rating. I know that because *Shawshank Redemption* is the first movie and *Godfather* is the second movie. Whereas if I click it as "Alphabetical"... 

PowerPoint can do that. And **the weird thing is it’s actually easier to do this in PowerPoint than it is in D3, than it is in Processing, than it is in most other libraries, which is a bizarre discovery.** There are some things that PowerPoint actually does well. 

So what is the code for this like? This is a little bit more of code, but I’m not going to walk you through all of it. I’m just going to talk you through the general principles. We create a new slide `presentation.Slides.Add` and then we create two buttons, one called "Alpha" and one called "Rating," `buttonAlpha` and `buttonRating`. And we put in the text as "Alphabetical" and "By Rating," so that’s what you see out there. And then we out here sort the movies or rather get the index of the sorted movies so that we know exactly where—is this movie going to be the 60th movie alphabetically or is it going to be the 53rd movie alphabetically? Because I don’t quite want to re-sort them or to have two different sorting orders, I just want an index. 

Now this stuff is straightforward. Let's see what happens when I actually run this portion. I get a new slide in which—oh, sorry, I think I’m running the wrong one. Interrupt the kernel and let’s run—where did it go? Yeah, this is the one I want to execute. So let’s execute that. It’s created a new slide that just has "Alphabetical" and "By Rating," nothing else. 

The next step is where I’ve got a function that’s defined. This is what is doing the bulk of the heavy lifting. The function's called `animate`. It takes a sequence. Now PowerPoint has these things called sequences which are like queues for animation, and you can have multiple animation queues. I’m going to assign one queue for the alphabetical ordering and one queue for the by-rating ordering. 

The first parameter there is the sequence, which is the queue, and the second parameter there is—what this function does is takes one image and moves it to another place. That’s all. So in a particular queue, it starts with an image. I want this to move only when a particular trigger is clicked along a certain path and take a duration of 1.5 seconds by default, which you can then change. 

And inside it is the code for actually adding the effect to move it from point A to point B. The first chunk defines an effect and says that I want to move the image along a line vertically downwards—I'll later on tweak the line—on a shape click. The actual behavior is a motion which is along a path. 

**Interestingly, the path specification is very similar to the SVG path specification. It is, to be precise, the VML path specification, which is Vector Markup Language, which was Microsoft’s alternative to SVG. But thankfully, if you know the SVG path specification, the spec here is no different, or not too different, and you can do all of the cool stuff that you can do with SVG—Bézier curves and so on.** 

And then we say make sure that it moves along with the previous element so they all move simultaneously. The trigger is the trigger and the duration is the duration, and run with it. Now this just creates the function. 

Then we get into the actual timelines. We create two queues for interactive animations and then as before draw every movie, but after drawing every movie, we do a couple of other things. We figure out what the alphabetical position should be and say that if the `buttonAlpha` is triggered, then move this particular image along this particular path. Now where exactly is the path being defined? Out here. You say move from `0, 0`—in other words, start at the original position—and go on a straight line to a secondary position. Secondary position is nothing but the—well, let’s not worry too much about the calculations. It’s ultimately saying this is where I finally want it to be. Similarly, if I click on the `buttonRating` trigger, then move the same image along a different path backwards. So which is what gives us this really cool animation. Can go back and forth. 

It really is easy. So I can go down the G's—where's F? There's *Gandhi*. So that was a lot easier to figure out than it would have been to go through all of the individual movies, right. 

**Anand**: [21:03] Okay, so now that is interesting, but is it useful? Is the question. So let me show you some pieces of work that we’ve done—pieces of work meaning people have actually paid us money to do what I just showed you, a fair bit of money. 

The newspaper *Vijay Karnataka*, when covering the Karnataka elections, said, "Look, we’d like you guys to do something fancy about it." And in terms of the format of output, we explored a variety of formats—HTML5, SVG, etc.—and finally we said, "Look, if I gave it to you as a PDF file, that’s probably going to be the safest. If you wanted to make edits, however, it would have to be only PowerPoint as the only thing that we’ve got in common." They said, "Yeah, okay, why don’t you give it to us as both?" 

So we did. They ran a series of full-page spreads, some of which I’ll show you. Okay, so let’s start with—let’s start with this one here. So this was the full-page spread. Anyone here reads Kannada? 

**Audience**: [Inaudible]

**Anand**: Okay, can you just say it as loud as you can? 

**Audience**: [22:15] [Speaking Kannada]

**Anand**: In English, please. Sorry, I don’t speak Kannada either. 

**Audience**: [22:25] **Politicians' work ethic.**

**Anand**: Okay, fair enough. Which—what we were trying to do was plot the MLAs' (Members of the Legislative Assembly) attendance. And in the inner rim is each of the parties—so the top arc is BJP followed by Congress followed by Independent followed by Janata Dal. And each of these strokes is one MLA. And the stroke is colored as blue if they are extremely attentive—as in they attend more than 95%, black if they're an MP and their attendance is not counted, green if it's between 75 to 95%, orange if it’s between 50 to 75%, red if it’s below 50%. 

So there are a few MLAs in Congress, for instance, and in BJP, and one in Janata Dal who actually had less than 50% attendance even though they were not a minister during that period. And other things around their accessibility and so on. **Now it becomes a whole lot easier for them to just go in and correct typos around their names.** Nikhil was helping me, thankfully, and he knows Kannada, but for a guy like me, it's very easy to make a spelling mistake and not even know that I made a spelling mistake in something like this. 

Or cartograms for that matter. We had a small problem—okay, this, sorry, could you help me by reading this again? 

**Audience**: [23:45] [Speaking Kannada]

**Anand**: Which is... 

**Audience**: [23:55] **Reasons for voting.**

**Anand**: Okay, fine. I still can’t remember—Nikhil, do you remember which one this is? Which party won? Okay, fine. So okay, cool. So the circles here are the parties—the color of the circle represents the party that—no, caste! Okay, fine. 

So there are three reasons why people vote and this was based on a survey that they did. Do you vote based on the party, or do you vote based on the caste, or do you vote based on the candidate? And each of these circles is one constituency. The people in that constituency predominantly have said either we vote mostly for caste, or we vote mostly for party, or we vote mostly for candidate. And that is this distribution. Now the size of the circles here represents the number of people in that constituency—larger circles are bigger constituencies. 

Now **why didn’t we use a shapefile? Why didn’t we use the actual Karnataka map? Well, here’s one trick: very often you’ll be in situations where you don’t actually have a map, and a cartogram is a phenomenal way...**



**Anand**: [24:59] **A cartogram is a phenomenal way of escaping that and still making it look cool.**
So we don’t have the maps, but we didn’t have the latest maps post-the redistribution of the assembly constituencies. So what we did was went through each of these constituencies on Google Maps, found out the centroid of those and said, "Let’s put a circle around it," and just move them around so that they don’t overlap. So that way, we have a reasonably good representation both geographically and at the same time, it has an additional dimension. **I’m not only able to bring in the color that I can put against that constituency, but I can also use size as an extra dimension for something else.** So we get more power with less effort or less data requirements.

Another thing that we were doing was focusing on what it is that the MLAs are talking about during the question-and-answer sessions. Each of these circles is one topic that was asked during the parliamentary question sessions, and these are along the lines of the three dominant parties. Questions that were mostly asked by BJP, questions that were mostly asked by the Congress, and questions that were mostly asked by Janata Dal.
So if you take this, for instance, which is I think fisheries, that is a topic that seems to be asked only almost entirely exclusively by BJP. Makes sense; they’re in power in the coastal areas. This, if I understand it right, is revenue, and that’s a topic that BJP stayed completely away from, being in power. Leave Congress and Janata Dal to split the questions; Congress probably has a slightly larger majority of questions there.
All of this was done in PowerPoint but let—not quite interactive.

Let’s get to some cooler stuff. What if we could do more? For example, one of the things that we were doing for another company was to look at the breakup of revenues. Let me close some of this and see if I can open that one.
So this represents their entire revenue worldwide base—anonymized numbers, by the way—which is let’s say 288 million. Of which, in the UK they had the largest revenue, followed by Japan, followed by China, followed by India, blah, blah, blah. Within each of these geographies, the respective channels and how much money did they make in each of those channels? Within those channels, each product and how much money do they—what is the relative size of those products? And what is the action that they need to take against each of these channel-product-geography combinations? Red means you’re doing bad, yellow means you’re doing okay, green means you’re doing good, grey is "grow the market," etc.
Now if I look at it, let’s take something near the top. Now looks like overall in China we’re not doing so well. Let’s zoom into China. Click on China, I get the details of China. Out here, there are almost no products where I’m doing well; product 8 may be the only exception. What exactly is happening to product 8? Click on product 8, I get taken into the details of that. Click on anything, blah, blah, blah, or click on the worldwide button to go in there. So **I have an interactive application in PowerPoint that is data-driven.** Tough enough to do in HTML.

Another one was for an app store company and what they said was, "We’d like to see how many downloads we’re getting." So on top is a bar chart where you have in the months of March and April how many downloads they were getting. The bar charts are colored based on whether the day-on-day revenue grows—grew or not. So for example, on this particular day, the 20th of March, the revenue actually shrank and therefore I can see that in red. Below that is a week-on-week distribution, so the week of the 18th of March was a pretty bad week. And below that is the month-on-month distribution.
Now the downloads are also broken up by country, where I can see that US had the maximum number of downloads followed by China followed by Germany; by model, Android 4 had the largest downloads followed by iOS; by category, games, education, etc.; by segment, newbies, retired people, and so on. The color here again represents growth. So this month, April, compared with the previous month, the growth was a relatively lower for Android. And I can start looking at combinations here. So US is broken by model into each one of these. The width of these bars is proportional to the number of downloads for that combination. So US-Android is the largest combination, but US-iOS 4 grew considerably. Then I can start breaking into each one of these and seeing what exactly is happening there. Now this is a lot of lines or spikes or whatever; it’s definitely tough to do this manually. No, that’s putting it mildly; you can’t do this manually.

The other thing that you would want to do is, "I want to see what exactly is happening on different days and drill down." So for example, let me click on one of these days and look at the breakup of the revenue on the 29th of April. So this is where the bulk of the downloads came from segment-wise—the newbie segment. Click on that, this is the breakup within that segment by category. Within that, this is the breakup by device, and so on. So you have a full-fledged tree map representation of the same thing as well.

Animations, not too difficult either. So this is something that I’d showed during my last talk. The axes here—the data here is the sites that people are visiting on their mobile devices, and this is I think for a period of one month, something like that. The horizontal axis is the number of pages each person visits per site. So something out here, social networking sites for instance, each visitor spends a lot of—spends time clicking on a lot of pages. The vertical axis is the number of kilobytes per page—sorry, that’s getting cut off. So the higher the page—the higher it is up here, the larger the size of the page. Which means that next to file repositories, pornography is the category that has the largest file size. One can drill down and see what exactly are the sites, right? So each of these little dots is one of those sites, and the most popular in terms of number of pages as well as size is xvideos.com by a huge factor. If you look at the search engines, there’s no prize for guessing what the biggest one is: google.com. Social networking sites, the biggest one again is Facebook, but interestingly people are spending less number of pages but slightly higher kilobytes on Facebook on average than any other site.

Let me—we’ll break for que—do I have five minutes with questions or without questions?
**Audience**: [Inaudible]
**Anand**: [30:58] Okay, fine, cool. Well, we’ll still do what I want to do. The last thing that I wanted to was look at what if we could take Twitter data and do a bit of livestreaming of that on Python? Okay, let’s give that a shot.
So somewhere out here, yeah. I’ve chosen to use this `twitter-api` package. I was Googling yesterday for what might be a good package; this seemed reasonably simple. There are a bunch of others that I found that look good; I would be very happy to hear from you what recommendations you might have on Twitter streaming API. But I’m going to instantiate this. I’m also going to open up PowerPoint and keep it ready.

Now what we can do is as we get new tweets, start populating them on the screen. So I’m defining a function called `drawTweet` which I will walk you through. And I’m going to search for—I’m not going to search for PyCon India 2013 just yet; I’ll do that during the Q&A session. So if you have any questions, just put a hashtag of PyCon India 2013 and let’s see if your face and name pop up here along with your question. But for now, I’m going to search for something like, I don’t know, something really popular: "beer," maybe? Yeah.
And let’s run that. Okay, got an error. Okay, something is happening. Now give it a few seconds. It’s still running, and once we have at least one tweet on "beer," hopefully that isn’t too uncommon a topic, we should have a slide here.
**Audience**: [Inaudible]
**Anand**: [32:43] No, I actually just meant "beer." I was hoping that the hashtag would be more common. Oh, I’m not on the first slide, good point.
Okay, PowerPoint's frozen. Oh yeah, sorry! Beer is pretty popular. So yeah, those are the tweets on "beer" going live. It may have stopped; I said stop at 12 tweets, so it may have finished all the tweets. Yeah, it did, sorry. Let’s do this again.
And all I’m doing here is get their tweet—the tweet's data, take their profile image, plot it there, draw a rectangle, put their face—their ID there, blah, blah, blah, and that’s it, and you get live tweets.

I’ll just switch over to PyCon India tag and any questions that you have, let’s see what pops up and more than happy to take that. Is it PyCon India or PyCon India 13? 2013? Okay. Okay, it’s still running "beer." Sorry, let me just interrupt the kernel. Yeah, there it comes through. Any questions?
Whoa, who’s the first question over there?
**Audience**: [Inaudible]
**Anand**: [34:39] Yeah sure, please feel free. Oh there’s an error, sorry, what is the error? Questions, raise your hands.
**Audience**: [35:03] Hey, great presentation, thank you. So my question is, **how much of this is actually valid in Keynote?** Which is the presentation software on the Mac, because I believe that has far more capabilities in terms of panning, zooming and all of those than PowerPoint does.
**Anand**: [35:20] **None of this would work in Keynote, unfortunately.** But while Keynote has more stuff in terms of animations and the Magic Move is outrageously good, there isn’t—see, **once you start doing stuff programmatically, then you stop worrying about the number of objects. When you’re manually drawing stuff, the effort is linear. When you’re programmatically doing it, the effort is completely non-linear.** So once you start thinking about doing stuff programmatically in any presentation, you then break away from the paradigm of doing stuff once—sorry, drawing a few objects. You’re saying, "Okay, I’ve got all of this data, I’ll put in 10,000 objects if I need to." That is a big win even for Keynote.
**Audience**: [35:56] But all of these I believe would also work on PowerPoint on a Mac, right?
**Anand**: [36:01] The reason I have a Windows laptop is that, to the best of my knowledge, it does not work on PowerPoint on a Mac. I am so sorry. I see.
**Audience**: [36:12] Do the interactive slides update in-slide or link between the slides?
**Anand**: [36:18] They update in-slide. So the one that we had earlier for the movies—okay, I think that’s gone, but yeah, it’s just moving within the slide and the way it moves is you have this object, you have an animation that says "draw it from this position to this position," and yeah.
**Audience**: [36:35] [Inaudible]
**Anand**: [36:36] You can’t export this to SlideShare, unfortunately. Yes, that is a disadvantage. Just wanted to get on to—okay fine.
**Audience**: [36:45] **How does using Python compare with something like PowerShell for Office automation?**
**Anand**: [36:50] If you’re familiar with PowerShell, go right ahead. See, the thing is there is no real Python that I’m doing here, right, other than LXML? So I’m just taking the COM commands and almost pasting them here. **My workflow for creating this is: use record macros in Excel, record the macro, copy-paste the Visual Basic code into Python and, if required, change the syntax.** I find that often you don’t even need to change the syntax. So it would work just as well in PowerShell.
**Audience**: [37:17] Hi sir, wonderful presentation. Actually, I have a doubt. **Can we use `win32com.client` in any other application other than these PowerPoint and Excel?**
**Anand**: [37:29] **Yep. I’ve used it quite effectively to scrape email data and figure out the social network of a few companies based on who’s exchanging mails to whom using Outlook.** I’ve used it to create maps in Excel, haven't used it in Word but you can certainly use it in Word, and that’s just the Office suite of applications. It goes well beyond that as well; you can use the Windows Instrumentation API and control practically any aspect of Windows for that matter.
One of the more interesting use cases was at the time when PhantomJS didn’t exist, the only way I had of scraping some of these weird government sites and `.aspx` sites was to use Internet Explorer. You can create a COM object for IE. It’ll open up IE like it opened up Python. You can get it to go to a particular page, insert jQuery into that page, do whatever scraping you want, get it back and store it. That’s how bulk of my scraping of weird sites used to be. It can be used for practically anything.

**Audience**: [38:29] Firstly, thank you, wonderful presentation. And there was a slide that you showed that had for a particular company the revenue model, and when you opened the slide, I saw a couple of slides were built. So when you clicked on each of them, were they going into different slides?
**Anand**: [38:47] That was also happening. So in the revenue model, where there was an initial—let me show you that slide. There was an initial slide which had the—what the heck is it called? Sorry, I’m going to stop this wall, by the way. Oh it’s already stopped, cool. And open the revenue model slide—oh sorry, not the revenue model, the App Store one, but that is a better example in this particular case, I think. Give me five seconds.
One of those things that you need to worry about here is unless you explicitly close Python from PowerPoint, it doesn’t get closed and then it doesn’t open very easily.
Okay, so this is the slide structure where for the Sankey diagram on the top left, we have a separate slide. And for each of the dates, there is a separate slide that contains the hierarchical tree maps. **So you need to create whatever interactivity you need in-slide up front.** So in this particular case, for example, what we have is on this slide, the games section which I hide on click and under that there are a bunch of sections which I then hide on click, under which there are a bunch of sections which I don’t hide on click as well. But out here, while all of the paths are drawn, only some of them are shown on slideshow and depending on what is clicked, the rest of them become visible.
**Audience**: [40:10] Did you create individual Python script for that?
**Anand**: [40:14] Oh yes, all of this is created using Python. **I can’t draw this much by hand.**
**Audience**: [40:25] These are great presentations, but what is the effort required to really, you know—like one is Python, the language you learn and you can do all these things, but second thing is you need to understand the data and, you know, other things to really present in this fashion. So I’m just typically trying to understand what is the effort required to really put these things together?
**Anand**: [40:46] **Something like this can be put together beginning to end in about a week’s time, roughly. One person, one week, roughly.**
**Audience**: [41:02] So my question is, since Python is driving all of the—the entire presentation so to say, so do you—if you need to distribute this, do you end up distributing the Python code and then get them to execute it at which point it draws the PowerPoint for you or...
**Anand**: [41:20] No, what we have is—okay, a number of mechanisms. We create an intermediate format and then have a converter to PowerPoint. But **these days we are experimenting with something else, which is the creation of a `.pptx` file directly using the OpenXML API. So in which case it can be done on the server side.** That is the way to go if you want to distribute it to—in unfriendly environments or commercial environments.
**Audience**: [41:43] Are we able to embed them and package them into a single file together using the OpenXML API?
**Anand**: [41:49] Yes, absolutely.
**Audience**: [42:10] Is the code for this shared on GitHub?
**Anand**: [42:13] **Yes, the code for this—the question was, is this shared on GitHub? Absolutely. So you can get both the link to the exact code repository on my tweet stream as well as on my GitHub repository.**
**Audience**: [42:24] Are the Windows APIs available on OSX?
**Anand**: [42:28] **To the best of my knowledge, no.** Which, as I told Lakshman, is the reason why I have a Windows machine, not a Mac machine. Sorry.
Guess we’re out of time. Thanks a lot, folks!

---
marp: true
title: Making Open Data Useful: Lessons from Diagram Chasing
  author: Vivek Matthew and Aman Bhargava
  url: https://sanand0.github.io/talks/2025-09-21-making-open-data-useful/
  theme: marpessa
  paginate: true
  # Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
  # https://chatgpt.com/c/69073893-1090-8322-8cf9-aa71bc3c4e84
---

# Making Open Data Useful: Lessons from Diagram Chasing

[IndiaFOSS](https://fossunited.org/c/indiafoss/2025/cfp/1hutna15uj) · 21 Sep 2025, 4:15 pm IST · [Bangalore](https://maps.app.goo.gl/Uon4KDWDqy65RGim8)
[Vivek Matthew](https://github.com/Vonter) · [Aman Bhargava](https://aman.bh/) · [Diagram Chasing](https://diagramchasing.fun/)
[Video](https://www.youtube.com/watch?v=7NCUE02l1DE) · [Transcript](https://github.com/sanand0/talks/blob/main/2025-09-21-making-open-data-useful/README.md)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-21-making-open-data-useful/)

[1]: https://diagramchasing.fun/?utm_source=chatgpt.com "Diagram Chasing"
[2]: https://blr-rains.netlify.app/?utm_source=chatgpt.com "BLR Water Log"
[3]: https://india-time-use-explorer.netlify.app/?utm_source=chatgpt.com "India Time Use Survey Explorer | Diagram Chasing"
[4]: https://cbfc.watch/?utm_source=chatgpt.com "CBFC Watch: Home"
[5]: https://diagramchasing.fun/authors/aman?utm_source=chatgpt.com "Aman Bhargava"

---

# Open data lands when we tell usable stories

- We thank an open data community and set up a talk about **how to make data useful** rather than just available.
- Practical examples matter because they show what people can actually click, share, and understand.
- You hear a point of view throughout: design for people who are not data professionals.
- This talk shares lessons that help you turn raw datasets into tools people love.

<transcript>

Hello everyone, good evening. Thank you for sticking around till the second-last talk of the day. And thank you to the Open Data devroom for organizing this. I wouldn't, I didn't expect IndiaFOSS to have an open data devroom, but it's nice to see that they chose to have one.

</transcript>

---

# Full-stack journalism joins reporting, design, and code

- We combine **reporting, design, and programming** into one workflow that we call full-stack journalism.
- This mix lets us chase ideas from scraping to storytelling without hand-offs.
- It keeps the focus on clarity rather than on any one tool.
- You will see how this approach raises the bar for public data work.
  ([diagramchasing.fun][1])

<transcript>

We're going to be talking about the work we do as part of Diagram Chasing, some of the lessons we've learned. Aman likes to call it **full-stack journalism**, and you'll see what that means. If you want to follow the slides along on your own device, you can scan this, but I think the screen is good enough, hopefully.

</transcript>

---

# Government data often arrives with avoidable mistakes

- We expect quality, yet **official sites ship errors** such as wrong map borders.
- These slips are common enough that they no longer surprise us.
- That is why validation and context sit at the center of our process.
- We treat “downloaded” and “trustworthy” as two different states.

<transcript>

My name is Vivek. I like government websites and I like publishing open data. And if I find a map of India with the wrong border, published by the Government of India, **I am not surprised**.

Okay, hi, I'm Aman. I'm the other half of Diagram Chasing. I'm a designer-programmer. I also, I am fond of, I'm a data journalism enthusiast. I'm not a trained professional. And yeah, I'm the other half of it. So for the past one year, we've been running this publication called Diagram Chasing, which is our kind of platform for, like, experimentation, just collaboration, bringing in both of our strengths and, you know, seeing what comes out. So, here are some of our works from our past year. I think Vivek is going to take you through the first one.

</transcript>

---

# Mapping natural drainage explains Bengaluru floods better

- Floods follow terrain. We mapped **natural drainage patterns** to show where water tends to collect.
- The site shades areas by accumulation likelihood and links flood **news reports** to places.
- A map makes a complex story simple for residents and reporters.
- People can explore and share locations that match what they see on the ground. ([blr-rains.netlify.app][2])

<transcript>

Yeah, so initially, our plan was not to make this, but it ended up being something called BLR Waterlogged. What we did is we mapped the natural drainage patterns in Bangalore. Bangalore gets floods very often, but it's actually just water flowing where it would naturally flow. So what the site has is a map where different shades of blue indicate how likely water is to accumulate in that area. Different popular places of flooding have POIs marked, and you can click them and find historical news reports from that area.

</transcript>

---

# Simple portals help people know their MPs quickly

- During elections, we shipped “Who is my Neta?” so people could **look up MPs** and activity fast.
- The portal combines affidavits and parliamentary data into clear pages.
- It worked because **many do not know this data exists** or where to find it.
- Voters got a straightforward way to learn and share information. ([diagramchasing.fun][1])

<transcript>

Another thing we built as part of an Open City Data Jam during the 2024 Lok Sabha elections is "Who is my Neta?" It's basically a platform where you could find out details of your, at that time, elected MP, find out details about their parliamentary activity, things they've reported as part of their election affidavit. So this went kind of viral because it was the elections, and **lots of people don't know that this data actually exists**. You can easily find out what your MP has said in parliament, assuming they've said something in parliament. Then after that, Aman worked on "Votes in a Name."

</transcript>

---

# Namesake candidates can flip close elections

- We studied “namesake” candidates who share similar names and can **confuse voters**.
- The analysis scanned decades of elections to spot likely swings.
- Close races can turn on tiny margins, as in a 16-vote example.
- We published many cases that were not widely reported before.

<transcript>

Okay, so while we were cleaning up the datasets and joining these affidavits and stuff, what I learned was that there are a lot of similar names for candidates who are standing in elections. And this was new to me, that there are namesake candidates who are put up by all sides to confuse, maybe to confuse voters, maybe it's organic coincidence, but I don't think so. So for example, like, there are names like S.V. Ramani and S.V. Ramani who are standing in the same election, right? So this happens to Rahul Gandhi versus a Rahul Gandhi. It gets reported because it's funny, right? But I was curious about, are there other things, are there other smaller elections where this has happened? And are there places where this could actually have like, flipped an election?

So we did this large, illustrated story on analyzing this data, on finding on how we found these similar candidates, how we passed through all of the elections that have happened since the 1960s, I think. Each election, each local election, national election. And then we did some analysis to narrow down candidates and occurrences which we were pretty sure were actually could have actually turned elections. So a popular example is Sowmya Reddy in Jayanagar versus a Sowmya A. Reddy, right? So a vote difference of 16 votes could have actually turned that election. This was a popular, like, this was also reported very widely, but we found many such examples which I did not find news reports of. So to my knowledge, this is the first analysis of its kind.

</transcript>

---

# Open data fails when people cannot use it

- The National Time Use Survey is “open,” yet **practically inaccessible** to most people.
- Files are spread across many Excel workbooks with coded columns and scattered PDFs.
- Non-programmers struggle to load, map codes, and merge the parts.
- Availability is not usefulness when the format blocks everyday users.

<transcript>

After that, we worked on the National Time Use Survey. This is just a 0.0001 percentage of the actual data they published. The National Time Use Survey is done by MoSPI. They survey 5 lakh people across the country and ask them what they did in the past 24 hours. So you have like a half-an-hour granularity detail of what 5 lakh people in India did, and it's across regions, demographics, economic groups, all that.

So when you look at that, this Excel file, it's like, not actually one Excel file, it's like 10 Excel files. And if you don't, if you're not a programmer or data person, you can't use this. So it's technically accessible, I could download it, but I can't really use it unless I'm familiar with the process of using this kind of data. So I would say **this is not accessible open data**. It's maybe somewhat open.

And there are multiple steps to get the data. First, you have to create an account on MoSPI, which is, could be easier. The data is split across like 10 different files. Each column over there is some random code. You have to map it with an actual word. So one could mean male, two could mean female, three could mean transgender. All these codes, you have to like manually reference a PDF, find the page in the PDF where it's referred. They use some random column headers. The documentation is in a bunch of PDFs. And the fundamental problem is you need to know programming or data to actually use it. Most people who would use this data in real life, like a policy person, probably does not have the skills to use it that easily. So the data is not built for the people who would really want to use it. So it's technically available, technically available but practically inaccessible to the people who would benefit from it.

</transcript>

---

# A browser explorer turns an unwieldy survey into answers

- We **cleaned and documented** the time-use data and built a browser explorer.
- People can group, filter, and run aggregations without installing anything.
- Raw rows are visible, and summary views give quick comparisons.
- You can download results and continue work in your own tools. ([india-time-use-explorer.netlify.app][3])

<transcript>

So what we ended up building is we cleaned up the data and we built an explorer. You can find it on the Diagram Chasing website. What you can do is explore all the data, run different kinds of aggregations and SQL queries directly in your browser. You don't need to open 10 Excel files and figure out what to do. So suppose you want to know who spends more time cleaning up after meals. The answer is pretty obvious, but to see the disparity is interesting. So on the website, you could group by state and gender, select the activity code as "cleaning up after," and then you get this on your browser.

So this is the raw data. You can see every survey respondent, which gender, age, state. There are lots of fields. And we also have a summary view where you can get like aggregated statistics, the mean for males in Karnataka, the mean for females in Bihar. And directly from your browser, you can download all this data and do what you want with it.

</transcript>

---

# Empty dashboards numb people and inviting tools spark curiosity

- We avoid **prompt-and-forget dashboards** that look slick and say little.
- Too many generic charts dull attention and reduce trust.
- Instead, we craft tools that reward exploration and clear questions.
- This keeps users engaged and encourages meaningful discovery.

<transcript>

So, like, a lot of our work has, **we don't want to create dashboards**. I think that's a ground rule that we have, that each project should be taken on its own merits. We do not want to create dashboards, we do not want to create charts which you just show people, right? I think right now, it's, it's never been easier to prompt a dashboard. Okay, you go to some, like, some website, give me a dashboard, here's my data, you get a, you know, something which looks like this, purple gradient text, a lot of boxes, big text, and you do, you do what you want with this. But I think the problem is that you desensitize your audience to data because I have seen like five pothole apps over the last one month, all right? On Twitter, on Reddit. I think there's a risk in desensitizing your audience where the audience just stops caring about the data or the dashboards, right?

So then how do you, our, our goal, personal goal is how can we make this more inviting? How can we make this more accessible? And these are just our subjective thoughts. A lot of it has to do with web applications because we do that kind of work. So these are subjective thoughts, obviously. But I think one of the projects that, the biggest project that we've undertaken is something called CBFC Watch, which I'll take you through. And a lot of the thoughts come from this project.

</transcript>

---

# India now has a searchable film censor archive

- We launched **CBFC Watch**, the first public, searchable archive of film modifications in India.
- The database spans about **18,000 films** and over **100,000 records**.
- People can search by theme, language, year, or creator.
- Context pages show how each film compares to peers. ([CBFC Watch][4])

<transcript>

So, CBFC Watch is the **first searchable archive of film modification in India**. So all modifications done by the Censor Board of India is searchable for the very first time. We have an archive of 18,000 movies, 1 lakh modification records that you can search for the very first time. So you can actually go to our website and we have this nice search function where you can search for keywords like "maps" in a language, in the English language movies, in a certain year, in a certain genre, for a certain actor, director, whoever you want to search for. We have also cross-linked and cross-referenced 18,000 of these movies by this metadata. So if you're interested in Akshay Kumar, you can look at Akshay Kumar, you can look at what themes he's usually censored for or not censored for. You can draw all these comparisons.

For each film, you can understand it in its context. So on each film page, we have these charts which show you what the relative distribution of modification is, where does this particular movie fall, what actions were taken, what themes were unusually modified, what were usually modified, and so on. So this is what we've been working on, and Vivek is going to start off with how we got to building this.

</transcript>

---

# Reverse-engineering URL patterns unlocks public records

- Certification pages hide behind **predictable URL parameters** and numeric patterns.
- Reading a few pages reveals prefixes, years, and sequences.
- Iterating across ranges collects many valid records while skipping gaps.
- Patient decoding turns scattered pages into a coherent dataset.

<transcript>

So I'm not sure how many of you even knew that the Censor Board publishes this. The normally how you have to find this is you'll search for a certificate that looks like this somewhere in your theater. And in person, it looks like this. It's probably next to the toilet. And when you scan, so on the bottom left, bottom right, there's a QR code. When you scan that, you get a page, this page. Each record is a modification made by the Censor Board in the film. So this particular one had seven films, seven modifications in the film, and there's supposed to be a duration attached to each one. In this case, everything is zero seconds. They didn't enter the data properly.

But since we have a URL, that which is what we want, and it has an interesting pattern. It has two URL parameters. The "i" parameter is what we're interested in. But we have a URL with numbers. So now we can try to make sense of how they host this data and how we can extract it. So we try to decode the URL parameter. We try a bunch of different numbers, which turn out to be successful 200 requests. But there are a bunch of 404s as well. But these four turn out to work. So we try to figure out, like, is there a pattern to this? So the first four is just some kind of prefix. The next two appears to be some kind of code. The four digits following that is basically the year the film was certified plus 900. And the last seven or eight digits is a sequential certificate number.

So now we cracked the code, maybe, and we can just iterate over every possible certificate which is hosted on the website. So we try out a bunch of values, we get a bunch of 404s because for some reason, the sequential numbers are not really sequential. There's like one gap in between. We haven't figured it out, and I don't think they care at this point. You'll find out soon why.

</transcript>

---

# HAR files and LLMs make complex scrapers tractable

- Some sites need **multi-step ASPX requests** with cookies and view-state.
- We export a HAR from the browser and study every request.
- An LLM helps write a script that **faithfully replays** the sequence.
- This speeds up scraping while we keep control of the logic.

<transcript>

So now that we have the URLs, we have to figure out how to extract data from each page. So my favorite thing is to just open the network tab and see what the browser is doing. So, and as an example, we open one of the certificates. And on the bottom, that last request, the QR redirect one, if you check the JSON, not the JSON response, just some random response from that, it has the data we're interested in. So what we do is we download the QR redirect post request response for every film. And you can't do that directly, actually, because there's a bunch of requests made before that. It has cookies, there's different, it's an ASPX website. I'm not sure how many people have used an ASPX website, but there's lots of state involved in every request.

So what we had to do is we had to export all the network requests as a HAR file. HAR is basically the standard format for, like, saving network requests. I'm not an expert in this, but it works for me. So what it contains is all the HTTP requests, all the cookies, session IDs, everything. So this is a small sample of what we got for our website. The actual HAR file is like 600 KB. So if we had to dig through 600 KB to find out what requests are being made, it would have been very difficult. So what we do is what everyone does these days: we fed it to an LLM. And it turns out it's very good at what we needed it to do. So we fed this HAR file to an LLM, asked it to generate a scraper, and it did a pretty good job. This is approximately what it looked like, the script it generated. Each step, one ribbon request, some other follow-up requests. And there are like seven requests you need to make before you can make the QR redirect request. But it turns out this LLM solved most of our work. And soon enough, we had a functional scraper, so we downloaded all the files we needed.

</transcript>

---

# Keep every download because sites often change or vanish

- **Never delete what you download** from government portals.
- Pages break, parameters change, and data disappears without notice.
- Your local copy protects your work and enables later audits.
- Treat downloads as evidence as well as inputs.

<transcript>

And one tip I would suggest to everyone is when you download something from a government website, **never delete what you download, because it may not be there tomorrow**.

So what, now that we had the HTMLs, we had to clean it up a bit, and we just exported it as a JSON with the fields of interest. So we have like the category of the film, language of the film, people involved in the film. And we do this for all the films. We dump it into a CSV file with the fields of interest to us. So we have a CSV file now. I think people would be pretty happy at this point, but it turns out the CSV is still a big mess because when you open it, you see they have film modifications like this. You can try to read and understand. I don't think it's that easy to understand because it's a bunch of numbers. So what we really cared about is what is being modified, where it's being modified, and how much is being modified. And also not just modifications, we also wanted to add context, like who made the movie, who acted in the movie, which studio made the movie, when did the movie release. And the end goal was to sort of analyze trends in the way the Censor Board censors stuff in films. So we made an attempt at first. Aman spent a lot of time on this.

</transcript>

---

# Clear schemas let LLMs classify messy notes well

- We do not ask LLMs to “find insights.” We **use them for classification**.
- A strict JSON schema and edge cases drive consistent labels.
- Categories like action type and topic unlock analysis at scale.
- Small costs create a large, structured layer over raw text.

<transcript>

Okay, so just a fair warning, there's some explicitives on the screen, but if I censor them, then I mean, it's, it's just pointless, right? So, the first thing that we tried was hard-coding just what to look for. I want to look for profanity. I made a huge list of profane words. I, you know, violence, religious topics, political topics. But these people sometimes don't care about spelling, right? They don't care. They just generally don't care. If you trust them enough to spell things properly, maybe this would have worked, but it does not. There are also regional languages. There are regional words which I can't account for, right?

So while I was doing this, also just since we are on the LLM topic, we never use LLMs for analysis, right? I would never ask an LLM to say what's interesting from this, please generate it for me. If I don't care about it, I can't expect someone else looking at the data to care about it. But then why here, right? So Vivek said something to me that if you are categorizing these manually anyway, if you're making these lists manually, it's a subjective decision that you can pass on to the LLM because it'll just be maybe just as good.

Right, so then the attempt number two was operationalizing a pipeline which did this. LLMs are great for classification tasks. So what, how this works is you write a detailed prompt with all edge cases, all the categories that you wanted to generate, like action types, was it a deletion, insertion, replacement, modification, what category of topic, violence, profanity, religious, political, whatever you want. And you can define a nice JSON schema. And you can ask the LLM to always respond in this structure, right? So it makes it very easy for you to then put into a CSV.

So then we could like give it random sentences and it would always like classify it correctly. And this was, this was great because the scale of this data was like a 1 lakh records and overall, like experimenting with this cost us only around like 12 to 1500 rupees, which is great, which is great value for the kind of metadata that it created for us. Because what this does is now you have sentences which initially looked like this. And now you can actually get some structure out of them. You can get a clean summary of what happened. You can actually generate categories which you can use for counts, analysis, time series analysis, whatever. You can also generate like topics. You can extract the main topics out of the sentence and generate a list of them as well, right? So suddenly then this becomes like analyzable. You can actually track changes across films over time instead of just having natural language text. So, yeah.

</transcript>

---

# Permalinks and simple search turn data into journeys

- **Permalinks make your site shareable** so people return to exact views.
- We prefer a single search box over walls of toggles.
- We use a fast search engine and a **light parser** for fielded queries.
- People search like they already think, and they get results. ([diagramchasing.fun][1])

<transcript>

So we have a CSV now, but I don't think people just look at CSVs. They need some help using it. So what we found interesting is to find ways that people will find interesting data themselves. Otherwise, like, it's just data. There's nothing interesting for them. So we wanted to communicate this excitement, and what does the user want from their point of view? That's what we wanted to figure out in the data. So they would probably want to find movies which they're interested in, search for keywords, share the movie with others, and just browse through the data set in a more convenient way than a CSV.

So a few things we like to put on our websites, one is having permalinks. **Permalinks make your site much more shareable.** Now you can just send a film you like to anyone. They don't have to open your site and click 10 different buttons to find the film they want. You can share an actor, particular content, things like that. We use something called TypeSense, which is a FOSS alternative to Algolia. We wanted to have a bit of slightly complicated search features on our website, and TypeSense turned out to work pretty well.

So by default, TypeSense, this is a demo they have on their website. This has a bunch of random toggles and buttons. We don't think this is good because I can't scroll through 50 different toggles to figure out what I want. What people want is something they're familiar with, which is something like Google search. All search engines use this, not just Google. Even DuckDuckGo can do this, by the way. What you can do is search for "Ejipura flyover" from a particular website since 2019, because everyone talks about it and you would like to search more about it.

So TypeSense by itself does not have a very straightforward parser. We have to build a slightly custom parser ourselves. So we extract this field pattern and we can get things like exact matches, wildcard searches, and comparisons. So we build this and now you have much more powerful search on the website. So when I have a website, when I'm looking at a website, I would want to search for things like this. So of course, when I'm building something for someone else, I should build it like how I would want to see it.

</transcript>

---

# One site is one view, so document the rest

- We publish **examples**, data dictionaries, and **reproducible notebooks**.
- This invites others to slice data in ways we did not.
- A documented pipeline builds trust and speeds reuse.
- Good docs turn a project into a platform others extend.

<transcript>

And one key point I feel about things we build is that **what we build is just one way of viewing a data set**. It's not the only way to view a data set. When government releases data, it's in specifically one PDF format because they don't want people to use it any other way. But I believe that data should be accessible to be used in multiple ways. So how do you think about the users who are going to look at the data and how they would like to use it?

So one thing is to give them examples of how they can use it, how they could slice it. So over here, if they're interested in the kind of content being censored or which regions of the Censor Board are censoring things differently, these are examples of how you could use it. We also try to document all the data we put out. So we put out a data dictionary with the description of every single field. And we hope that people don't have to guess what the data is about. It should be pretty clear with the data documentation how you could use it and what each field means. With CBFC Watch, we also put out a detailed notebook written in R, because Aman likes R, and you can recreate lots of the analysis we did on this notebook.

And turns out because we put a notebook and lots of documentation, other people actually used it. So this week, The Hindu published two articles using the data on CBFC Watch. This is one of them. And Vignesh is the person who published the article. This is what he said. **"What's there to consider? You brought it on a platter."** When you make data that easy for people to use, they are going to use it. And documentation obviously helps with that. And because there's a notebook, you can also recreate what they have done and fork it in a certain way, because you can just change certain things in the notebook and get a chart that might be of more interest to you.

</transcript>

---

# Bad government UX blocks real use of public data

- Gate-kept downloads, OTP walls, and opaque formats **waste citizen time**.
- Complex flows hide simple questions like “how many cars this year.”
- We show how poor design defeats the promise of “open.”
- Public data should meet people where they are.

<transcript>

So one part of this is that design and UX are not just a visual part, it's also the way the system is designed, at least with data, government data in India. But it's not just government data. Even we as engineers and programmers, I'm guessing lots of us are engineers and programmers, we feel it's not worth spending time on glitter, on like features that make it nice to use. But when you use a site or a platform with good design, it's quite evident that there was actually thought put into it.

So one example of bad government UX and design is the Survey of India. Has anyone looked at a Survey of India map? Okay, that's more than I expected because we're in an open data devroom, but if you haven't, the reason is probably because it's almost impossible to access. First, when you open this, open the site, you get this. You have to fill in what is called an C-OSM number. Now I want a map of Nemhans, I have to figure out this number. Once I get the number, I get this form. I have to give my mobile number, get an OTP, create an account, get a password, type a captcha. And then I get a file in a format I don't understand, so I have to figure out how to use the file. But you could use OpenStreetMap and you can get the data in five seconds. So why would I use this government website?

So this is not just with maps. There are like all kinds of data which the government puts out which they make impossible to access. As an example, I recently scraped the Parivahan portal, which has vehicle statistics of RTO registrations, all kinds of data about vehicles. So suppose you are interested in electric vehicles. BYD is a Chinese manufacturer of electric vehicles, which Trump really hates and I think it's banned in the US currently, if I'm not wrong. But in India, we are importing lots of electric vehicles. So if you were in the policy field related to electric vehicles, you'd be curious, how many BYD cars are being registered in different parts of India right now? So if you wanted the data from the government, luckily they at least have a portal, Parivahan. You open that, you're greeted with this. There are like 20 different panels and numbers. Where do I find numbers for Bangalore? So what you have to do is you have to select your state, your office, then select the category of the, the year, and then you have to select the manufacturer and then scroll down and you find the number you want. Now this is just the number for one RTO for one year for one manufacturer. Now if I want this for, there are like 1400 RTOs in India. How would I run any analysis on BYD cars in India with this? It's impossible.

So it's a multi-step process. It's not meant to be used the way you may want. It's for a very specific use case. They don't have any documentation. I happen to know where to click to get this data. If you didn't, you'd probably get stuck on the way. And even if they have data, it's probably not pretty, not that good, but at least it's something. But how could this be better? So what I did is I scraped the data, created a custom UI. So you can find it there, india-vehicle-stats.pages.dev. But the main point is that I can permalink to the thing I want. So I'm interested in BYD India Private Limited cars from Karnataka in 2025. So you could just share this link with someone and they could get the number just right there. They don't have to navigate a massive UI. And when I release data, like I mentioned, I try to put a data dictionary. So if you want to run some analysis, it's much easier. Now you can just run SQL queries on the data.

So when you design, it should be for the lowest common denominator. I think lots of open data tends to be built for data people, but most people who want to use data are not necessarily data people. So you should be designing for low friction, especially for people who may not be comfortable with data. And most people use a browser, so ideally you would build platforms which they can open and data they can open in a browser. Flat GitHub, Datasette, and Datawrapper are pretty nice tools for making data accessible on a browser. They don't have to download a CSV, open it in Excel, do all that.

</transcript>

---

# Static tools cut upkeep and keep projects alive

- We prefer **static sites** that run in the browser.
- Static projects have near-zero costs and fewer moving parts.
- This lets you ship, **sleep well**, and keep the work online.
- Interactive does not mean server-heavy in 2025.

<transcript>

Yeah, so when we're building web apps, Vivek is a DevOps engineer and he tells me that I don't want one more thing to maintain in life, right? So I want to build a project and I want to move on from a project. So that becomes an important consideration. We for most of our projects, I would say CBFC Watch is the only thing which has some moving parts, but almost everything can be static. If you're building something which has interaction, which is a dashboard, make it static, **move on with your life**, right? It will live forever. It will, it has no costs. Almost everything can run in the browser these days for free. I have built teaching tools with R which runs in the browser, so you don't even need to download R, right? It's a, it's a great space, it's a great time to be like building stuff. Build static stuff, that is the best thing to do for you as a builder.

</transcript>

---

# Start with intent and offer many entry points

- Begin with a user’s job, not your favorite dataset.
- Offer **search**, a notebook, and a CSV so different paths work.
- Each path lowers friction for a different audience.
- Your tool becomes useful to more people with less guidance.

<transcript>

So yeah, now this is like the philosophy part, like this is a subjective philosophy part where I think there are some general principles that maybe we can use to just when you're building stuff with our open data. Start with the user's intent. Don't not think about like, okay, this is the data, I'm just going to put out the data, CSV, done, right? How can I, how can this appeal to someone? What are the different people that I'm considering this for? What multiple entry points can I offer them? With CBFC Watch, we have a search for people who just want to search. We have a detailed notebook of analysis for journalists who just want to analyze the data. We have a CSV if you want to use that, right? It's just one view of the data. Your creation is just one view of the data. There can be many more.

</transcript>

---

# If you cannot link it, it does not exist

- Design every state so **you can link to it**.
- Copy-pasteable URLs help people share and return to answers.
- This is how insights travel inside teams and newsrooms.
- Linking is accessibility in practice, not theory.

<transcript>

**If you can't link to it, it will not exist.** If I cannot share something on my site, if I cannot directly link to it, people are never going to get to it, all right? So this is, this is something that we focus on. How can we permalink everything? Even the analysis done in the Time Use Explorer, if you set certain filters, you can copy a link and you can send it to someone, the exact same query will be loaded and it's all static in the browser, no server required.

</transcript>

---

# Documentation is a product that invites use and critique

- Treat **documentation as a first-class feature**.
- Explain fields, methods, caveats, and limits in plain language.
- Show sample analyses that reveal why the data matters.
- Good docs turn curiosity into credible reporting.

<transcript>

**Documentation is a first-class feature, it is not an afterthought.** There are detailed data dictionaries. Now we will be putting out notebooks and so on. So the idea is to invite people in. Create sample charts, do sample analysis. If you were interested in data, why did you care about the data, right? Show me that, maybe I'll get interested in it too. So yeah, documentation is a first-class feature, it's not an afterthought.

</transcript>

---

# A three-script workflow keeps scraping and cleaning sane

- Use a **fetch** script that mirrors the site’s requests.
- Use a **parse** script that normalizes HTML into tidy formats.
- Use an **aggregate** script that joins sources into a single table.
- Then combine datasets to answer harder questions.

<transcript>

I'll just go through this quickly, but normally when I scrape data, I try to keep it with a three-script workflow. One is a fetch script to actually scrape the data from the website, from the government website. I use the network tab and HAR files as I mentioned. I have a parse script to get normally HTML into a better format. And then I aggregate them all into a CSV or a more single file format which people can use easily. An example of how having multiple data sets is useful, you can combine them. So for "Who is my Neta," the data we have is actually from three different sources, but when you actually look at the UI, it's all abstracted away. You don't have to worry about where do I get this data from. When you're able to link and combine different data sets, you get better value out of this. Sometimes there may not even be a data set. What we did with BLR Waterlogged is we manually just went through all news articles of flood incidents and we aggregated them like this.

</transcript>

---

# Beauty and craft make public data spread and stick

- **Beauty and craft matter** because people share what feels polished.
- Memorable visuals reduce re-work because others adopt your work.
- Design is not glitter. It is clarity and care.
- Better presentation raises the chance your data changes minds.

<transcript>

Yeah, and like one of the last things is **beauty and craft matter**. If you don't want your data creation to be lost and someone have to recreate it all over again, make it memorable, right? We treat aesthetics with just as much like importance. We want people to share this, we want people to come back to it. I would say design is not, again, not an afterthought, it is the central thing which takes, makes these projects take longer, but I think it's worth it. So yeah, I think all of it should be open source, all of it should be reproducible as far as possible. Do not hide anything. People should be able to use it. And yeah, that's, that's Diagram Chasing. That's us. This is, do you want to, Vivek, do you want to say what this is?

</transcript>

---

# We keep filing RTIs and shipping new stories

- We continue to **file RTIs** and clean new releases.
- Fresh data keeps the pipeline alive and the audience engaged.
- We preview work only when it is ready to help.
- The cycle rewards patience and steady craft. ([diagramchasing.fun][5])

<transcript>

I filed an RTI last month with the Bangalore Metro Corporation. They sent me a 10 MB Excel file, and I'm going to publish something this week with that data, hopefully. This is a preview of that data.

Master of ceremonies says two questions. Anybody? No, no, it needs to go into the...

</transcript>

---

# The name celebrates patient pursuit of a clear picture

- We picked “Diagram Chasing” because **we chase a picture** we hold in mind.
- The process takes months of careful iteration.
- The name reminds us to keep going.
- A good name keeps the team aligned.

<transcript>

**Question**: The name behind Diagram Chasing? I'm curious about the naming, yeah.

**Answer**: Wow, this is out of syllabus. It sounded cool. The thing is, like, when we are chasing, like, when we are working with a data set, I know that in my head there's this graph that I want, and it might take like a few months to get to that. With CBFC Watch, I wanted that trends of content, and it feels like that's what I'm doing, that's what we are doing, just like sitting with this one CSV for like eight months. So yeah, Diagram Chasing. Yeah.

</transcript>

---

# Curiosity and debate sharpen your sense for interesting work

- You grow taste by **arguing, testing, and proving** ideas to yourself.
- Frustration turns into craft when you try to win the argument with facts.
- Curiosity drives you to check claims others ignore.
- That habit produces stories others want to read.

<transcript>

**Question**: How do you develop an eye for interesting analysis?

**Answer**: Okay. I think it's like a, it's an acquired taste kind of a situation where, I think it's also frustration. Like, because I would, like I think there's, I hear a lot of people complain about there's no data, there's no data, right? I think there is data. I think like we as sometimes like people who are knowledgeable about it fail to communicate it, right? So sometimes he brings up a thing and we have an argument and I want to prove him wrong or he wants to prove me wrong, right? So it, the craft then is generated out of spite. So it's about like, can I, can I have an argument over this thing? Can I have a conversation about it? If it's, if it's as interesting as that, maybe it's interesting to someone else as well. So maybe that's a short answer. Yeah, thank you.

</transcript>

---

# Making Open Data Useful: Lessons from Diagram Chasing

[IndiaFOSS](https://fossunited.org/c/indiafoss/2025/cfp/1hutna15uj) · 21 Sep 2025, 4:15 pm IST · [Bangalore](https://maps.app.goo.gl/Uon4KDWDqy65RGim8)
[Vivek Matthew](https://github.com/Vonter) · [Aman Bhargava](https://aman.bh/) · [Diagram Chasing](https://diagramchasing.fun/)
[Video](https://www.youtube.com/watch?v=7NCUE02l1DE) · [Transcript](https://github.com/sanand0/talks/blob/main/2025-09-21-making-open-data-useful/README.md)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-21-making-open-data-useful/)

[1]: https://diagramchasing.fun/?utm_source=chatgpt.com "Diagram Chasing"
[2]: https://blr-rains.netlify.app/?utm_source=chatgpt.com "BLR Water Log"
[3]: https://india-time-use-explorer.netlify.app/?utm_source=chatgpt.com "India Time Use Survey Explorer | Diagram Chasing"
[4]: https://cbfc.watch/?utm_source=chatgpt.com "CBFC Watch: Home"
[5]: https://diagramchasing.fun/authors/aman?utm_source=chatgpt.com "Aman Bhargava"

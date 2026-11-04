---
title: "ED Homework Submission Review"
date: 2026-11-04T20:33:53+05:30
source: "https://chatgpt.com/c/6aea944d-fcac-83ec-911e-8ea13c2dfa4d"
---

# User

_2026-11-04T02:11:27.548Z_

For Palanis Engineering Design class at IIT Madras, what homework did I set last time? Check out the talk transcript, etc. My emails and Google Drive will probably have some submission links. Go through those extensively and see what has been submitted and what is pending. Brief me on what the homework was, or homeworks were, if there were multiple, in simple enough a form that I can quickly understand. Make sure that your communication is very clear and sufficiently concise. Guide me on how to evaluate it. Also run an evaluation on the submissions so far and let me know what you find that is interesting and I should know about. Feel free to use* [LocalMCP2](/plugins/plugin_asdk_app_6ab0b6c561508191882e58b23665db3e)
 or* [Remote Desktop Commander](/plugins/plugin_asdk_app_6a057d268ebc81919918d37eec718425)
 as you wish.

# ChatGPT

_2026-11-04T02:11:27.548Z_

## 1. What homework did you set?

Your most recent class was on **21 October 2026**. You set two assignments, following an earlier one from 7 October.

| Assignment | What students had to do |
| --- | --- |
| **1A. Engineering visualization** | Build a visualization of an engineering process or problem, such as a production line, that helps someone understand what is happening. |
| **1B. Improve the visualization** | Rework the earlier visualization to make a specific decision obvious, with evidence supporting it. Submit the original and improved versions. |
| **2. Phone as an engineering instrument** | Build a mobile app that measures something useful (tilt, vibration, motion, etc.), visualizes the readings on the phone, and demonstrates its use in a video of at most one minute. |

The 21 October session specified **27 October** for the phone-app assignment.

The central teaching point was: *Making a visualization is easy with AI. Making one that helps somebody take the right decision is the valuable skill.*

For example, a factory dashboard shouldn't merely show machine utilization. It should help decide **which machine to improve, and why**.

## 2. What has been submitted?

I found the official response sheets, shared by Mohan Raj on 27 October.

Assignment 1B

# 32

Distinct students

Submission sheet (link: target not exposed)

Assignment 2

# 31

Distinct students

Submission sheet (link: target not exposed)

These counts exclude an apparent test entry named “Hero” with roll number `007` and deduplicate repeated submissions.

* **31 students submitted both assignments.**
* **One student, Aadhira Vikram (ED23B047), submitted 1B but not 2.**
* Five latest submissions across the two sheets were recorded after the communicated 5 pm deadline, with another later resubmission for 1B. The sheets contain no missing upload-link fields.

The class reportedly has approximately 40 students. If that is the official enrollment, around eight students have no recorded submission in either sheet. I could not verify those identities without the class roster.

## 3. Evaluation findings

**I checked all 65 student-upload URLs. None was accessible.** Each returned a 404 through your connected Google Drive account. I also tested the other connected accounts and anonymous access on samples.

Consequently, I could evaluate submission coverage and timing, **but not the actual apps, videos or visualizations**. I cannot responsibly assign content scores yet.

Three things stand out:

**First, the sharing is broken.** The course account `ed5518.2026@gmail.com` shared the response spreadsheets but apparently not the uploaded files. Mohan Raj needs to share both Google Forms file-upload folders with `root.node@gmail.com`, or provide ZIP archives of the submissions.

**Second, deadlines were inconsistent.** Your 21 October email said end of day on 27 October for Assignment 2, whereas Mohan Raj later specified 5 pm for both assignments. Seven submission rows were recorded after 5 pm, involving six distinct students, including one resubmission. I would not penalize these without resolving the ambiguity.

**Third, the original factory assignment was more substantial than a dashboard.** Its two exercises required students to discover an overlooked problem and build a timestamped, interactive factory replay. Both could be combined into one self-contained, offline `replay.html`, with evidence, rejected hypotheses and recommendations.

In the 21 October classroom walkthrough, an important weakness emerged: a dashboard suggested ST10 was the bottleneck, but downstream constraints and rework complicated that conclusion. That is an excellent teaching example, though not a verified grading result.

## 4. How I recommend evaluating

Use a simple five-point rubric for each assignment.

| 1B: Factory visualization | 2: Phone sensor app |
| --- | --- |
| 1. Original, revision and prompt included | 1. Runs on an actual phone |
| 2. Interactive replay works offline | 2. Captures genuine sensor readings |
| 3. Manager's decision is clear | 3. Visualization is understandable |
| 4. Evidence supports the recommendation | 4. Solves a practical problem |
| 5. Revision demonstrably improves decision-making | 5. Video proves functionality within 60 seconds |

Give one point per criterion, with uncertain cases flagged for review. Automate file checks first. For the most important test, show the visualization to someone unfamiliar with it for ten seconds, then ask what they would do and why.

**The key question for Assignment 1B:** Does the improved version help a manager make a better decision than the original?

## 5. One more assignment to keep track of

On **2 November**, you emailed Palani five proposed project challenges: a five-second chart, a misleading chart and its correction, an investment decision aid, a novel visual format, and a sensor-based experiment tested on unseen observations.

These have much stronger objective evaluation criteria, particularly blind human tests. However, I found no confirmation that Palani distributed them to students, nor any submission sheets for them. Treat these as **proposed future coursework**, not missing homework.

**Immediate priority:** Get Mohan Raj to share the actual uploaded files. That is the one blocker preventing a meaningful student-by-student evaluation before your next class.

# User

My next class is today and I would like you to run a possibility scan on the format that I might use to run this class. What are ways by which we could explore ways of teaching that can leverage my physical presence and synchronous presence in a way that offline and asynchronous cannot? Based on that, for this particular course, what could we do that is powerful and interesting? What is it that would be particularly powerful and interesting given the kind of work that I have been doing and sharing recently? Explore extensively and ideate using relevant skills to come up with the most interesting and effective (from a learning perspective) approach. [![Image](https://files.openai.com/content?id=file_00000000fb9881f99f77ad57947232ae&cdn=1&cp=pi&ma=31190400&ts=0&p=pi&cid=8&sig=b9da986568361f3300fc047ef19ef27b2e275443189ff9886f609f394642bbde&v=0)Remote Desktop Commander](/plugins/plugin_asdk_app_6a057d268ebc81919918d37eec718425) Plutonium is available but graphene is not.

# ChatGPT

# Possibility Scan: Turn the classroom into a laboratory

**My recommendation: Run a 90-minute session called “Looks Right. But Does It Work?”**

Your IIT Madras Engineering Design class is scheduled for **today, 4 November, 2:00–3:30 pm IST**.

Rather than another talk or live-coding demonstration, make the students simultaneously **designers, experimental subjects, skeptical customers, and investigators**.

The central idea:

**An AI can generate a beautiful visualization. Only testing it against reality and unfamiliar people tells us whether it works.**

Students have already built factory visualizations and phone-sensor apps. This is the perfect opportunity to test their work on people who have never seen it, challenge the conclusions, and discover failures the authors never anticipated.

## 1. What is special about being together?

The important distinction is not simply in-person versus online. It is **what the room can do that an individual working asynchronously cannot easily reproduce**.

| Unique opportunity | What students can experience |
| --- | --- |
| **Unprepared human reactions** | Discover what other people actually understand, instead of what the designer assumes they understand. |
| **Physical reality** | Test whether sensors and simulations correspond to real-world measurements, rather than trusting convincing graphics. |
| **Live disagreement** | Watch two reasonable people reach different conclusions from the same evidence, and investigate why. |
| **Unexpected challenges** | Defend or change a decision when someone introduces new evidence or an unforeseen constraint. |
| **Collective intelligence** | Discover something that no individual or AI had thought to investigate, through argument, collaboration, and experimentation. |

The most useful sequence is:

## 1

Predict

Commit

## 2

Test

Meet reality

## 3

Disagree

Investigate

## 4

Revise

Transfer

This is also consistent with learning research. A meta-analysis of 225 undergraduate STEM studies found better exam performance under active-learning approaches than conventional lectures. Research on peer instruction shows the benefits of students independently answering, arguing, and answering again. Research on productive failure supports having students attempt difficult problems before receiving an explanation. PNAS (+2 more sources) (source: target not exposed)

An important qualification: the evidence supports *well-designed active learning*, not the claim that physical presence automatically beats good online teaching. Your extra advantage today is access to real people and physical experiments.

## 2. The most interesting possibilities

I explored formats ranging from engineering simulations to human-AI experiments, live usability tests, and adversarial design reviews.

Here are the strongest candidates, ranked by their value for today's class.

| Format | What makes it interesting | My judgment |
| --- | --- | --- |
| **Blind design duel** | Students test whether their original or revised factory visualization helps unfamiliar people make better decisions. | Essential |
| **Break my sensor** | Students exchange phone apps and find real-world situations where they give misleading measurements. | Essential |
| **The human factory** | Students physically become a production line, creating bottlenecks and discovering why the apparent problem isn't necessarily the cause. | Most memorable |
| **Engineering courtroom** | One team recommends an investment; another cross-examines its evidence; a third introduces unexpected facts. | Strong |
| **Human versus AI perception** | Repeat your recent humans-only drawing experiment (link: target not exposed), but with engineering charts. | Great research extension |
| **Live sensor orchestra** | Use your voice choir (link: target not exposed) or phone sensors to visualize 40 people trying to synchronize. | Spectacular, but less directly tied to homework |

I would combine the first three, with a short engineering courtroom at the end.

## 3. Recommended 90-minute class

2:00–2:18

![Dualer Studiengang Maschinenbau (Bachelor of Engineering) | Hochschule Bremen](https://images.openai.com/static-rsc-4/aL0eNxoG0bKefCGhwT2xO6QUcqKmSpGR730MX6n6VTqA2oH4PKJ0yhHtaZBn3kQpj7cXpS0aHzUh0IoqXG7HfkRFDCZFE79Q6Mj58O0Z4qrm0nG-rHWyDT9tuWtBN-ahzlcnRbS6qgmOhHQGzmazsMJFolgF7j2S99ircIJgSik?purpose=inline) — **Act 1 — The human factory**

Recruit four students as ST10, ST20, ST30 and ST40, with three small buffers between them. Pass paper tokens through the line. Make one station slow, then secretly introduce rework at another.

Other students observe, record which buffers fill, and predict where extra capacity would improve throughput. Ask them to commit to a decision before revealing the hidden intervention.

**Lesson:** The machine that appears blocked may not be causing the bottleneck.


---

2:18–2:48

![2026 Most Affordable Data Science Degree Programs Ranking in the South - Cheapest Degree Schools | Research.com](https://images.openai.com/static-rsc-4/uRyh8cDsWPiysSKNaQjmGeuwHrmOYoGxAg_Ie2-eZzR9qu3yBGSzx5iNbpSc4xiJ6bFMhlNqqL_FKfOO9I_LkINeAUZD-OLRXbENHG4LhgYzeGcxlojQvBCtm59DmqFX9BFBh4pnxLO8jRihPvtWbz9DmIgMn6zYIr6YLKy1QEM?purpose=inline) — **Act 2 — Put the visualizations on trial**

Divide the roughly 40 students into eight groups of five. Pair groups. Each selects one student's Assignment 1B, showing the original visualization to some unfamiliar reviewers and the revised one to different reviewers.

Ask reviewers, before any explanation, what action the factory manager should take, what evidence supports it, and how confident they are.

Compare interpretations and identify one change that would make the recommendation clearer or better supported.

**Lesson:** A designer's intention is not the same as an audience's understanding.


---

2:48–3:13

![Physics 103 Lab - Setup Instructions: Motion With Constant Acceleration - Fall
2025](https://images.openai.com/static-rsc-4/Ac_YTqaG8FAqHadJR4s6YHKF6ZGCdt174ab-ioZdSBGkzAv-XMXQRLJKG3mZeexDc3jvXPKix2w6b-JaavMcatiqotB87k8qxpYk_BLvQBg-ajt5eKseDlFtrQA4SiOUfGbrPRGbFSsH_9UFhmVhfWEfvE-jywCZ1uFdA4F9CfA?purpose=inline) — **Act 3 — Break my sensor**

Students swap their Assignment 2 phone apps. The receiving students must test them under conditions the creator did not demonstrate.

For a tilt app, try a level desk, a book-raised surface, and different phone orientations. For vibration, compare a stationary surface with safe, repeatable movement. Check against an independent reference where possible.

Each tester finds one success and one unexpected limitation.

**Lesson:** An app that displays a plausible number is not necessarily measuring the intended physical quantity correctly.


---

3:13–3:25

![Des élèves du Campus de Lille travaillent sur la création d'un flux logistique "juste à temps" sur la ligne pédagogique | Arts et métiers](https://images.openai.com/static-rsc-4/E_1ZnJLvWnA5Xcl4BFMhh5RQ2fhkAQpKle4CKoKv3cQ2NojEQwVYUeR1EsfyvL0BcDxUeasVAAbQSa-DVyNlo4cTJq4tDLafNraqWbKnDhFh8USTIt2UuhclD3fYXvsFFIVllebag_MB0zAgGnRb7A6qU1WEunjGNzzuTcRhOGw?purpose=inline) — **Act 4 — The boardroom surprise**

Invite a team to recommend a factory investment. Introduce one new fact, such as a recently increased retest rate at ST30.

Ask everyone to decide individually whether to keep, reverse, or postpone their recommendation. Have opposing students explain their reasoning, then let everybody decide again.

**Lesson:** Good engineering judgment includes knowing when new evidence should change a decision.


---

3:25–3:30 — **Exit test — What transferred?**

Give students an unfamiliar engineering example. Independently, each writes the action they would take, the evidence they need, and one observation that would make them change their mind.

Collect these as the real learning evidence.

This can work without any new software. The physical simulation needs only paper tokens, space for three small buffers, a timer and volunteers. Students can open their own submitted visualizations and apps directly on their devices, avoiding the Google Drive sharing problem discovered earlier.

## 4. The critical design details

### Make the human factory genuinely surprising

Don't tell observers which station is artificially slowing down. Let them infer it from the process.

For example, use 20 paper tokens representing units. ST10 processes quickly; ST20 initially processes slowly; ST30 is faster but occasionally requires retesting; ST40 packs finished tokens. Give every buffer a capacity of two tokens.

Run two short rounds. Change one station rule between rounds without announcing which one. Have observers track completed parts, queues and station states.

The surprise isn't merely discovering a bottleneck. It is that **the bottleneck can move, and the evidence needed to identify it changes**.

Make clear that this is a simplified model of factory behavior, not a replay of the synthetic Varuna dataset.

### Separate persuasion from truth

This is the biggest danger with peer-evaluating factory dashboards.

A misleading visualization can persuade every student to make the same wrong decision. Therefore, measure two things separately: whether the audience understands the intended message, and whether that message is justified by evidence.

For the original-versus-revised test, use separate viewers for each version. With perhaps two or three reviewers per version, results are diagnostic, not statistically reliable enough for grading or ranking.

### Force everyone to predict before discussing

Peer discussion helps learning, but if the most confident student speaks first, you risk measuring conformity rather than understanding.

Have everyone privately commit to an answer and confidence level. Only then invite discussion and a second response. Ideally, use a new but equivalent question at the end to test whether the concept transferred, rather than whether students copied someone else's answer. PubMed (+1 more sources) (source: target not exposed)

## 5. What your recent work adds

Three connections make this class more distinctive than a conventional engineering workshop.

**Your humans-only CAPTCHA experiment** showed that human and AI interpretation can diverge. The class can extend this from recognizing drawings to interpreting engineering charts. You could eventually build a benchmark showing which visual representations work for humans, which work for vision models, and which fail both.

**Your 52 specification and verification techniques** provide a vocabulary for what students are doing. In particular, run it for real, check the checker, test alternatives, and flag guesses (link: target not exposed) are exactly the behaviors you can reinforce during the activities.

**Your TDS course-design experiments** have been moving toward assessments where agents can do the work but humans must specify what success means, decide which evidence counts, and accept responsibility. The engineering class gives that principle a physical reality: a failed measurement or mistaken investment decision is more tangible than an incorrectly generated answer.

## 6. The bigger opportunity revealed by the possibility scan

The high-leverage possibility is not merely delivering one better class.

**Turn the course into a small, ongoing research laboratory for human and AI understanding of engineering information.**

Every assignment could generate three things: a designed artifact, a test involving unfamiliar users or physical evidence, and a record of what failed. Across cohorts, you could discover reusable design principles and build real evaluation datasets.

That gives the students an unusual role: not simply learning visualization techniques, but helping discover which techniques actually work.

Two small choices would amplify this considerably. First, keep authors silent during initial testing so that their explanations cannot rescue poor design. Second, capture each unexpected failure as an anonymized record with its context, expected behavior and observed behavior.

My main caution is to **avoid turning this into a spectacle**. A crowded room, impressive demos and enthusiastic discussion do not by themselves establish learning. The individual exit test matters because it checks whether students can apply the principle independently to a new situation.

For today, I would prioritize the blind visualization test and physical sensor test if time becomes tight. Those directly evaluate the work students have already done. The human factory is the memorable opening that connects everything.

The enduring lesson is:

**A visualization isn't finished when it looks correct. It's finished when you have evidence that it helps someone understand or act correctly—and you know where it fails.**

# User

There was a Vishitra workshop that I conducted where I had five or six visualizations that different people could vote on and discuss. What I thought was I would flash pairs of these one after another and ask students to answer a specifically worded question on which is better, A or B and why? And have them submit their answers. That becomes a prediction. And then we will test a couple of things. One, whether their answers perfectly align or there is misalignment. What are the reasons they have chosen the specific visualization? And therefore what we can learn from this. Two questions. One, can you locate the links to the individual visualizations that I used there and share them here so that I can open them in tabs and pair them? Secondly, what question could I ask of any pair? And what should be the exact wording that asks them to compare A and B on? And what should be the wording of the question where I ask them for the reason? I will be creating a live form from this

# ChatGPT

I found all six visualizations from your **4 July 2026 VizChitra workshop, “The Curator’s Dilemma.”** These are the actual A3 presentation versions you used, not merely links to the underlying projects. I verified that all six URLs respond successfully.

## 1. The six visualizations

![India’s real unemployment crisis: Why headline rates don’t tell the whole story](https://images.openai.com/static-rsc-4/hLI67pP5U4XjOH9S7uxkRPTfmB9GsmmcmVQO37BrcJGDgnO_lPdsFrGfWsB1hmeOh5-809ld2IEEoONxFIUODp4pPtCQuX7eN8bbUUhojAxvU-B4ZfHKXG2jOWWIsDQObX0K9J8TgxN7XQ-EG0l1PDPNWRlIvzq9WIBmz7H9Zf0?purpose=inline) — **A. Statoistics — Education vs Jobs**

Open visualization A (link: target not exposed)


---

![Visualizations - OpenFace](https://images.openai.com/static-rsc-4/cn6644CsIZEeh5o3TYVGT3dNogwSb6mrhlDTM_UDzKppZM83nXZWQyntEKadHrtgPkbgwdn9t-XMgOn2y3SfYGQU1G7hiOwqK4csBni866utgl6G6x-AU_XSyX-PylbkAj8lrSQ3rMQEDHROF48TwPEGeXXrdp2mXwDiCfNaaOw?purpose=inline) — **B. Popular Actors — Image Similarity**

[Open visualization B](https://talks.s-anand.net/2026-07-04-vizchitra-dialog-curators-dilemma/02-popular-actors.html?utm_source=chatgpt.com)


---

![Gallery — HoloViews v1.23.2](https://images.openai.com/static-rsc-4/0L21zV1UntEQGKZoHlfMTQYULpld6vvzBs0at7Sq4yfb7qkGAnEF6lvC_l6j-MOwpvJ8nJJDRhaHcYHn05sXJsbl0za6OaqKrl39tUh3gP70LpS80FZG3K52WIH2NsbSGrJWwsWL77t_H12zIS9tte_NzDhs5ItvNfqxxhIq6VY?purpose=inline) — **C. Temporal Rosette — Weekly Patterns**

Open visualization C (link: target not exposed)


---

![Analyzing IMDb Data The Intended Way, with R and ggplot2 | Max Woolf's Blog](https://images.openai.com/static-rsc-4/vhtrbHuzIHAdSsuKKfvAv03spxWuCQYCayyNqGCh11oSfVwe4ufN2qmFN6txT0iPLIbl64pUIzapfgoTo98fY1DPDNFHIJ5jzJXrdOI1OHsg5SyletMnUZrxwS0e6RAoc5Df3xobyqw1rz1TfR9UduLCPQ2LHGOdPItlbZfUSVQ?purpose=inline) — **D. Popularity Paradox — IMDb Rankings**

Open visualization D (link: target not exposed)


---

!["The Price-Intelligence Frontier has advanced by another order of magnitude in another quarter!" – @swyx

The price of AI inference is essentially going to zero. Models are getting smaller (GPT-4o… | Emmanuel Turlay](https://images.openai.com/static-rsc-4/yLsldEOOYLS9WTasqT-d9MNLZct40RBSB7FU5WspC-DrWFtwDw3c94Uy7gw257JVb5LJjfyBDOhgxB8aSmoJOCYSCPze2POvF9qt3MZoJmbMQcva5RZObEpJilJ_pg4WvXRSEtJnhviuKgveflwesRGDzADcjVnG2dXU9G3mGjA?purpose=inline) — **E. LLM Pricing — Cost vs Performance**

Open visualization E (link: target not exposed)


---

![Josh Kale (@JoshKale) on X](https://images.openai.com/static-rsc-4/zt_-xRDcOlf-UURfik77cqeTxKADoCdbcAdfBd93gN0YlPsbeadVRr2-6TTEcIHA4dC_pH1Il43aSYk4dAeLM3sFksmOvVYYXfy9i7Z6PUA4F5sXwmUYjkrx_RSl3wQuxvDe_DZ18o4yWOtkTto4Bwu2s3QdwtEspEgZvnBljEs?purpose=inline) — **F. GDPVal — AI's Economic Impact**

Open visualization F (link: target not exposed)

The original workshop page (link: target not exposed) also contains the voting results and discussion.

## 2. Exact wording for your form

I'd recommend measuring **predicted comprehension**, rather than asking which is simply "better." That's a more precise question, and it gives you something you can subsequently test.

Writing

**Question 1: Which visualization communicates better?**

Imagine a student unfamiliar with either subject sees each visualization for just 10 seconds, without any explanation.

**Which visualization is more likely to help that student correctly understand its main message?**

* A
* B

**Question 2: Why did you choose it?**

What specifically about the visualizations made you predict that one would communicate better? Point to features you observed, not just whether you liked the design.

*Answer in 1–2 sentences.*

I would force an A/B choice, even when students think both are poor. They can explain that qualification in the second answer.

## 3. Three small additions that make the experiment stronger

**First, capture private answers before any discussion.** This is crucial. Your VizChitra workshop revealed that a group's apparent consensus concealed individual disagreement. Show the answers and reasons only after everyone submits.

**Second, separate predictions from actual performance.** After voting, you can test a few visualizations by asking different students to explain their main takeaway after ten seconds. You can then compare popularity with actual comprehension. Because the charts concern different subjects, this is an exploratory comparison, not a controlled measurement of design quality.

**Third, consider a second round:** Reveal each visualization's intended audience and purpose, then ask the same students whether they would change their choice. This was one of the strongest mechanisms in your original workshop.

For the initial pairings, I'd try **A vs D, B vs E, and C vs F**, then mix the pairings in subsequent rounds. Display order should alternate when possible.

The most interesting potential result isn't which visualization wins. It's discovering **whether students agree on what makes a visualization good, whether their stated reasons predict actual understanding, and whether evidence changes their minds.**

# User

If you have access to ~/code/liveform-data and liveform, Add three questions in the liveform-data repository following the conventions that exist there. The questions should link to three pairs of visualizations and ask exactly the same question for all three. Test this out locally if you can. And commit and push the questions. Choose the pairs of visualizations well based, for example, on feedback from the Vizchitra discussions as well as your own judgment

# ChatGPT

**Created, committed, and pushed three questions** to `sanand0/liveform-data` on `main`.

View the form configuration on GitHub (link: target not exposed)

## The three pairs

| Pair | Visualization A | Visualization B |
| --- | --- | --- |
| 1 — Audience favorites | Statoistics | Popularity Paradox |
| 2 — Different trade-offs | LLM Pricing | Popular Actors |
| 3 — Complex visualizations | GDPVal | Temporal Rosette |

I selected these using the original VizChitra voting and discussion. All six visualizations appear exactly once, with links embedded in each question.

Every question uses **identical wording**:

> Imagine a student unfamiliar with either subject sees each visualization for just 10 seconds, without any explanation. Which visualization is more likely to help that student correctly understand its main message?

Students must begin their response with **A:** or **B:** and provide a brief reason identifying specific visual features. Answers are locked after submission to preserve the original predictions.

## Verification

* **Passed:** Liveform's configuration loader accepted all three questions.
* **Passed:** Six unique visualization links, two per question.
* **Passed:** Identical wording and instructor-only results access.
* **Pushed:** Commit `dfd4b41`; working tree clean.

**One limitation:** Liveform supports one answer field per question. To keep exactly three questions, each captures the A/B vote and explanation together. The results page shows written responses, not automatic A/B voting bars. The votes can be tallied from the first letter of each response.

The configuration is ready, but **the live form is not deployed**. A full local server test was blocked because Liveform uses Unix-only `fcntl`, which doesn't run natively on Plutonium's Windows environment. The README includes Linux startup instructions.

Once Liveform is running against this repository, the form path will be:

`/ed5518-vizchitra-2026-11-04/`

# User

_2026-11-04T05:25:19.147Z_

Graphene is online. Pull the repo on graphene.

# ChatGPT

_2026-11-04T05:25:19.147Z_

**Pulled and merged `liveform-data` on Graphene.**

The repository had diverged, so I merged the GitHub changes while preserving Graphene's existing forms and responses.

* **Location:** `~/code/liveform-data/`
* **New form:** `ed5518-vizchitra-2026-11-04/form.yaml`
* **Merge commit:** `cee2205`
* **Branch:** `main`

Verified that all changes from GitHub are included.

The existing untracked directories `aipl2026/` and `iitm-ed-viz-2026-10/` remain untouched.

The merge is **committed locally on Graphene**, but not pushed back to GitHub.

# User

_2026-11-04T08:17:32.483Z_

Insert the first question asking students to share how we should be verifying visualizations. My aim is to have them think about it. What happens when they create a visualization? How do they know if this is right? How do they know if this is going to meet the intended objective? How do they go about testing this? That sort of a thing. So frame the question accordingly.

After the exisiting questions, also add a question on how they should evaluate their mobile applications. I mean, how does one even go about testing a mobile app? What are the criteria to use? The idea is that they should put in a point of view, and then we will be discussing it during the class.

Finally, add a last question asking them to swap their phone with their neighbor's and to test their neighbor's app. If possible, make this a question where they can provide an audio response that will be transcribed, either live or later. They should mention whose app they tested, what it does, what works well, and what can be improved.

# ChatGPT

_2026-11-04T08:17:32.483Z_

The ED5518 Liveform on Graphene now contains **six questions**, in the requested order:

1. **Verifying visualizations:** How would you test both correctness and whether a visualization achieves its intended purpose?
2. **Three A/B comparisons:** The existing VizChitra questions, unchanged.
3. **Evaluating mobile apps:** What tests, criteria, and evidence would establish that an app works well?
4. **Testing a neighbor’s app:** Swap phones and upload a 45–60-second audio review identifying the app, what was tested, what worked, and what could improve.

**Local validation passed:** Liveform loaded all six questions, the running server picked up the changes, and three relevant upload tests passed. Audio is accepted up to 5 MB. A `just transcribe-reviews` command is available to transcribe the recordings after class using Gemini; transcription is not automatic.

**Committed and pushed to GitHub.**

* **Commit:** `af2130f`
* **Form:** View updated questions (link: target not exposed)
* **Local form:** `http://localhost:3676/ed5518-vizchitra-2026-11-04/`
* **After class:** Run `just transcribe-reviews` from `~/code/liveform-data/`.

I verified the published configuration independently. The push included only form configuration and documentation—not the existing student response files. The untracked classroom directories on Graphene remain untouched.

# User

I've hidden the other questions and asked them to answer the first one. The responses are in responses.tsv in the same directory.

What do you observe from the responses? What's most common? What're most unusual? What's most correct, what're most wrong? Tell me what to teach. Use relevant skills. Use a meeting-response-style skill summary at the end.

I've also added another question asking them to discuss with their neighbors and share what they changed their mind on (for the same question) and I'll ask you to analyze that after they submit.

# ChatGPT

## The main finding: Students know to ask people. Fewer know how to prove a visualization works.

I read `responses.tsv` on Graphene. At the time of reading, it contained **23 responses from 23 distinct students**, all to the first visualization-verification question. The new post-discussion question had no submissions in that snapshot.

I classified the answers using non-exclusive categories:

| What students proposed | Students |
| --- | --- |
| Show the visualization to real people and collect their interpretations | 12/23 (52%) |
| Specifically involve the intended audience | 6/23 (26%) |
| Check the chart against data, calculations, or ground truth | 7/23 (30%) |
| Propose a concrete comprehension test or comparison | 5/23 (22%) |
| Compare the visualization against an alternative, such as a table | 1/23 (4%) |

These are interpretive classifications, not exam scores.

**What to teach:** A visualization needs two different kinds of verification.

1. **Is it true?** Recompute the numbers, inspect transformations, and check whether the visual representation is faithful to the data.
2. **Does it work?** Give a representative user a realistic task, observe what they understand or decide, and compare the outcome with a success criterion.

Most students have part of this picture. Few connect both parts into a reproducible experiment.

## The strongest and most unusual responses

These are identified by their position in the parsed TSV records, so you can locate them without exposing student identities.

| Response | What stood out | My assessment |
| --- | --- | --- |
| **#19** | Recalculate raw data, test with 5–8 real users without hints, and compare against a plain table | **Best overall answer.** Includes independent checks, actual users, a baseline, and conditions for rejecting the chart |
| **#12** | Verify values and calculations, then test whether users can find information and make decisions | Excellent end-to-end approach. Explicitly considers abandoning a misleading visualization |
| **#13** | Verify aggregated values and whether geometric proportions match the numbers | **Best technical detail.** A chart can contain correct labels and numbers but still encode them incorrectly |
| **#16** | Deliberately look for ways to misinterpret the visualization | **Best adversarial instinct.** It is unusual and worth building into the class |
| **#15** | Ask users to interpret the chart before revealing its context, then measure how their interpretation changes | An interesting experiment that separates first impressions from informed understanding |
| **#8 and #17** | Use AI agents to simulate audiences, generate alternative charts, and evaluate them | Interesting and potentially useful for finding issues, but insufficient to establish what real users understand |

One distinctive strength of #19 is the comparison with a table. A chart may look sophisticated yet deliver no advantage over a simpler representation. That is worth testing, though a tie does not automatically make the visualization worthless.

Response #13 deserves particular attention: *correct data* and *correct graphical encoding* are different checks. A bar chart could use the right values but start its axis at a misleading point. A bubble chart could incorrectly scale radius instead of area.

## The misconceptions to address

**1. "If people agree, the visualization works."**

Response #11 proposes redesigning if interpretations vary widely. This detects ambiguity, but agreement alone does not establish accuracy. Everyone could confidently reach the same incorrect conclusion.

Teach students to compare interpretations with an independently established answer, not just with each other.

**2. "If the chart supports my argument, it is valid."**

Response #9 suggests checking whether it supports the intended argument. That's a potentially dangerous criterion: it rewards confirmation rather than truth.

Ask: *What evidence would make you withdraw the claim?* A trustworthy visualization should survive attempts to disprove it.

**3. "An AI audience is enough."**

Responses #8 and #17 offer intriguing agent-based evaluation approaches. These can help generate edge cases, competing interpretations, or checks against source data.

But agents can share errors, invent interpretations, or fail to represent actual users. Agent agreement isn't a substitute for human comprehension testing or independent numerical verification.

**4. "I'll inspect it myself and explain it."**

Several answers rely on reviewing the graph or imagining the audience. Those are useful preparation steps, but the creator already knows what the chart is supposed to say. Explaining it to a user can conceal the very confusion being tested.

One response (#18) discusses testing phone tilt rather than a visualization. That's relevant to the mobile-app assignment, but it doesn't answer this particular question.

## What I'd teach in class

I'd spend **10–12 minutes** on one exercise rather than presenting a long verification checklist.

**1. Test the data, not just the picture.**

Take a factory chart claiming that ST20 is the bottleneck. Ask students to reproduce the relevant number directly from the data. Check the denominator, filtering, missing records, repeated items, and visual scale.


---

**2. Test a user with a task, not a request for opinions.**

Show the chart without explanation. Ask: "Which station would you investigate first, and why?" Record their action, accuracy, time, and confidence. "Do you understand this?" is a weaker test.


---

**3. Test against an alternative.**

Give other students a plain table containing the same data. Compare correct answers and time taken. Do not assume that the prettier visualization wins. Use the small classroom sample as an experiment, not a definitive ranking.


---

**4. Test the dangerous interpretation.**

Ask: "What incorrect decision could a reasonable person make after seeing this?" Then identify the missing evidence, unclear encoding, or misleading claim that might cause it.

The important missing idea across the responses is an **explicit success criterion before testing**. For example:

> At least four of five intended users should select the correct station within 30 seconds, without assistance.

That's a useful classroom pilot criterion, not a statistically established quality threshold. Students can debate whether it is appropriate, what the correct decision means, and how much evidence would be sufficient.

For the new post-discussion question, the interesting measure will be **what students added, rejected, or qualified** after talking to classmates. I would compare each student's original response with their revision and distinguish genuine conceptual changes from simply adding more checklist items.

## Here's what to say

- **Most of you recognized the need for feedback from people.**

* About half explicitly proposed testing with real people. That's a good starting point. But only about a quarter specifically identified the intended audience.

- **We need two independent checks: whether the visualization is accurate, and whether it helps someone do the intended task.**

* You can have a perfectly accurate chart that nobody understands. You can also have a beautifully understandable chart that is wrong.

- **Ask people to do something measurable.**

* Don't ask whether they like a visualization. Ask them to interpret a value, detect a problem, or make a decision. Measure what happened.

- **I particularly liked three ideas in your answers.**

* Recalculate the chart against raw data. Compare it with a plain table. Deliberately try to misinterpret it. Those make verification much stronger.

- **When you discuss with your neighbor, tell me what changed your mind.**

* Did you discover a new test, realize one of your checks wouldn't work, or change what you think "correct" means? Give a concrete example.

**Next classroom move:** Ask everyone to name one test that could *fail their own visualization*. That's a stronger learning check than collecting another list of good practices.

Source: Live `~/code/liveform-data/ed5518-vizchitra-2026-11-04/responses.tsv` on Graphene, first-question snapshot, 23 distinct respondents. Categories are my qualitative judgments and can overlap; the TSV's physical line count is larger because some responses contain embedded newlines.

# User

Now, they've submitted what they've changed their mind on. What are the most important things to teach based on that? Walk me through that, and also give me a meeting-response-style summary.

# ChatGPT

## The biggest lesson: Discussion broadened their ideas, but hasn't yet made their tests rigorous.

I compared **24 students' original answers with their 24 post-discussion responses**, matched by student, in the live `responses.tsv`.

The encouraging result is that students borrowed useful ideas from one another. Several added audience testing, raw-data verification, deliberate misinterpretation, or AI-assisted evaluation.

The concern is that **they're largely accumulating techniques, rather than explaining how they'd know whether a test passed or failed.**

I'd teach three things next, in this order:

1. **A test needs a predicted result and a failure condition.**
2. **The visualization must be correct even when everyone understands it, and useful even when all the numbers are correct.**
3. **Humans and AI agents can both help find problems, but agreement among reviewers is not proof.**

The clearest evidence that the discussion helped comes from a student who wrote:

> "I used to think correct results were enough, but now I understand that testing also means checking whether the system achieves its intended purpose reliably."

That is exactly the conceptual distinction worth reinforcing.

## What the discussion actually changed

# 24/24

Students with paired before/after responses

# 7

Revisions mentioning AI, LLMs, agents, or GPT

# 4

Students explicitly reporting no change

In the original answers, only 2 of 24 mentioned AI. The increase to 7 revisions suggests it became a prominent discussion topic, not necessarily that five students adopted it.

### 1. Teach students to turn a test idea into an experiment

This is the **biggest remaining gap**.

One student added the idea of showing a visualization for 10 seconds and asking what people understood. That's promising, but what constitutes success? If six people give six answers, which are acceptable? How much misunderstanding is tolerable?

I didn't find an explicit numerical comprehension pass/fail threshold in the 24 revisions.

Give students this concrete example:

**Visualization:** A factory chart comparing station defect rates.

**Test specification:** Show five intended users the chart for 20 seconds. Ask which station has the highest defect rate. Require at least four correct answers without assistance. Check that the answer matches independently computed rates from the raw records. Compare the result against a plain table.

**Failure:** The chart displays incorrect rates, users choose the wrong station, or the simpler table performs better on the intended task.

Ask students: "How would you rewrite your own proposal in this form?"

A threshold like four out of five is illustrative, not a validated standard. The point is to make success and failure observable.

### 2. Teach that agreeing with the creator is not necessarily understanding

One student revised their answer to say that if the audience's interpretation aligns with what the creator wants to convey, it is a good visualization.

Another proposed adding a final conclusion directly to the chart.

Both ideas deserve discussion.

**The intended message can itself be wrong.** An audience might understand a false claim perfectly. A prominent conclusion can also prime people to agree without independently examining the evidence.

I would ask the class:

> Suppose everyone correctly understands the message "Station A has the biggest problem." What if the chart compares absolute failures across stations processing very different numbers of items?

A station processing 100 items with 12 failures has a 12% defect rate; one processing 20 items with 9 failures has a 45% rate. Both the counts and rates may be correct. Which metric matters depends on the decision.

This also connects to an unusually good revision: one student proposed asking affected people **which parameters are important to their decisions**.

That moves the discussion upstream. Before verifying whether the chart communicates its message, establish that it answers a question worth asking.

### 3. Teach when AI helps, and when it creates false confidence

This became a noticeable theme after discussion.

Students suggested using AI to simulate an audience, deliberately misinterpret charts, independently check data, or generate competing visualizations.

One student made a valuable correction to their earlier AI-first proposal:

> "So first we should check the visualization against the data before ai agents are writing their opinions."

Another suggested using AI instead of people, but also recognized that numerical correctness wouldn't guarantee understanding.

I'd demonstrate three distinct roles for AI: **generate possible failure cases, independently recalculate from source data, and propose alternative designs**.

Then ask whether those activities establish that the intended users can make the right decision. They do not. Real-user testing still supplies evidence that simulated audiences cannot.

### 4. Teach deliberate falsification, including what's missing

A particularly interesting idea spread through the revisions: try to *misinterpret* or *sabotage* your own visualization. One student explicitly said a friend introduced it during discussion.

Another student added:

> "Check if any data hasn't been omitted"

And another wanted users to identify an entirely different problem the creator may have overlooked.

These are stronger than generic requests for feedback. They suggest looking for unknown errors, not merely confirming that the expected message comes across.

Give students a chart and ask: "What would I have to hide, change, or misunderstand for this chart to lead to the wrong decision?" Consider omitted categories, missing dates, denominators, selection bias, labels, and aggregation.

This is also where the original VizChitra lesson becomes practical: a chart can look compelling while concealing the very information needed to trust it.

### 5. Teach students to explain why they changed their minds

Four students explicitly said they hadn't changed their minds, although one also mentioned learning about deliberate misinterpretation. Another wrote that they had learned new things without specifying what.

Not changing one's mind is perfectly reasonable. But **a useful reflection identifies the evidence**: what was added, what was rejected, what remained convincing, and why.

The best revisions described an actual conceptual shift, such as moving beyond data accuracy to intended purpose or introducing a comparison against an independently generated chart.

For a future activity, I'd ask for three short responses: "I originally thought...", "I now think...", and "The reason is...". Students who didn't change their minds could explain what evidence reinforced their original position.

## What to do in the next 5 minutes

Use one factory chart, a plain table, and a deliberately misleading version. Ask students to specify the intended audience, the decision they should make, the correct answer according to raw data, and the observable test that would demonstrate success.

Then reveal the misleading chart and ask what their proposed test would actually catch. This connects the best ideas from their discussion to a practical verification procedure.

## Here's what to say

- **You learned useful ideas from each other, especially testing with people, checking raw data, and trying to misinterpret the chart.**

* But most of your answers still don't tell me what would make a visualization fail.

- **Before testing, say exactly what success looks like.**

* Who should understand the chart? What should they do correctly? How quickly? How many people need to succeed?

- **A clear visualization can still communicate something false.**

* Check the numbers, denominators, missing data, and whether the question itself is the right one.

- **AI is useful for finding problems, but it doesn't replace your real audience.**

* Use it to challenge your chart, recalculate numbers, and generate alternatives. Then test whether people can actually use the result.

- **Let's test these ideas rather than just discuss them.**

* Take one visualization. Write a test that might fail it. Run that test on another person. Tell us what happened.

The next learning outcome I'd look for is whether students can **write and execute a falsifiable visualization test**, not merely name sensible evaluation techniques.

Evidence: 48 TSV records, representing 24 original responses and 24 revisions, read on Graphene on 4 November 2026. Responses were paired by student email; all 24 matched. Thematic interpretations are qualitative, and the recorded statements do not by themselves prove lasting learning transfer.

# User

I asked students to answer the next 3 questions. What are the top insights from their answers? Give me the 3 most powerful ones - big, useful, surprising. Specifically, what were the biggest divergences among students? That's a teaching opportunity. Also, any correlations in the kinds of responses that lead to saying certain kinds of student responses go along with certain others - that are striking?

# ChatGPT

## Three insights from the visualization comparisons

All **24 students answered all three questions**. The biggest teaching opportunity is that students disagree about what makes a chart understandable, sometimes describing the *same design feature* as both helpful and harmful.

Students' predictions, not measured comprehension

1. Statoistics vs Popularity Paradox



A: 18 — B: 6

2. LLM Pricing vs Popular Actors



A: 9 — B: 14 — Neither: 1

3. GDPVal vs Temporal Rosette



A: 15 — B: 7 — Neither: 2

### 1. The most divisive chart is Popular Actors, because faces are both its advantage and its problem

![Local models are not there (yet) | Posit](https://images.openai.com/static-rsc-4/k5H2ZgRRe5PvhVS1cIplVzGVXtC2K3MwIiT2yynFT88aafF6afzzQXftKJ7yFNNcsmYpZvXP_HV71W4FGuI-m5IyGJINhQcKnJhrvNTZMpAbh5kcEU1D4qyIDoyvcd5ofygrP20iG3mPK5fzd_4I6g4qVOnrn1YaKgdd-86DtJk?purpose=inline)

A: LLM Pricing, 9 votes

![India’s OTT Economy Is Rewarding Trust, Not Fame: Smytten PulseAI - Chennai Patrika - Tamil Cinema News | Kollywood News | Latest Tamil Movie News | Tamil Film News | Breaking News | India News | Sports News](https://images.openai.com/static-rsc-4/er0EGLHVl1cTlBrqvc8OqPnKuvUpZADuh4TwyD4QxGcLwiZN0LvZSkw4I3rTv3_a1Mk9vLmIPedij9KxPZ6kRvIDnuXsA1Jwf4k0pCISyrdhFQT7wwRgGTsOOdDDJ5JfpwPVNediU-LTZCEAVrSBN-_wSnuH8TThGLK5BJ9en0w?purpose=inline)

B: Popular Actors, 14 votes

Students arguing for Popular Actors say photographs help them recognize people, understand the extremes, and interpret the plot quickly.

Students arguing against it say those same photographs create clutter, overlap, and distract from the axes. One calls the facial characteristics subjective.

**The disagreement isn't simply about whether images are good. It is about what the task requires.** Recognition might be faster with photographs, while precise comparison might be harder.

**Ask the class:** "Suppose I replace the faces with names. Which task becomes easier? Which becomes harder? How would we measure the difference?"

That turns a debate about design preferences into an experiment.

### 2. The surprising gap: Students often recognize a visual pattern without understanding what it means

The third pair produced a substantial split:

![Josh Kale (@JoshKale) on X](https://images.openai.com/static-rsc-4/zt_-xRDcOlf-UURfik77cqeTxKADoCdbcAdfBd93gN0YlPsbeadVRr2-6TTEcIHA4dC_pH1Il43aSYk4dAeLM3sFksmOvVYYXfy9i7Z6PUA4F5sXwmUYjkrx_RSl3wQuxvDe_DZ18o4yWOtkTto4Bwu2s3QdwtEspEgZvnBljEs?purpose=inline)

A: GDPVal, 15 votes

![Gallery — HoloViews v1.23.2](https://images.openai.com/static-rsc-4/0L21zV1UntEQGKZoHlfMTQYULpld6vvzBs0at7Sq4yfb7qkGAnEF6lvC_l6j-MOwpvJ8nJJDRhaHcYHn05sXJsbl0za6OaqKrl39tUh3gP70LpS80FZG3K52WIH2NsbSGrJWwsWL77t_H12zIS9tte_NzDhs5ItvNfqxxhIq6VY?purpose=inline)

B: Temporal Rosette, 7 votes

Two students rejected both.

Those choosing GDPVal often praised its red/green encoding, grouped rectangles, and large heading. Those choosing Temporal Rosette praised its compact circular layout and familiar depiction of activities over time.

But one GDPVal supporter wrote:

> "A - because the colour differences are evident although I have no idea what the area denotes"

**That's the most revealing answer in the entire set.** The student predicts that a visualization communicates better while admitting they cannot decode one of its visual channels.

The same distinction appears elsewhere. One student says the two lines in Statoistics clearly reveal the widening gap. Another chooses it partly because they already know the topic, although the question explicitly describes an unfamiliar viewer.

**Teaching move:** Put up GDPVal and ask everyone to answer three questions, separately:

1. What do the colours mean?
2. What does the size of each rectangle mean?
3. Which three AI pilot opportunities should an organisation actually select, and why?

The first two test graphical decoding. The third tests whether the visualization supports its intended decision. A student might pass the first and fail the third.

There's an additional important example in Popular Actors. Some students inferred people's origins from facial appearances. Yet that visualization's intended purpose was to investigate whether an AI embedding model might reproduce stereotypes. Recognizing a face and making a defensible inference about identity are very different things.

### 3. There may be a preference cluster, but the stronger result is that choices don't reliably predict one another

I matched the 24 students across all three questions.

One intriguing pattern: **6 of the 7 students who preferred Temporal Rosette also preferred Popular Actors**. Among the nine who preferred LLM Pricing, only one preferred Temporal Rosette.

That suggests a possible group attracted to recognizable images, compact layouts, or familiar subject matter.

However, the sample is small. Fisher's exact test for this association gives approximately **p = 0.34**. None of the three pairwise A/B associations is statistically convincing. So this is a hypothesis worth testing, not an established student type.

The more useful observation is that students' choices change with the visualization's subject and design. For example, 18 favoured the annotation-rich Statoistics over Popularity Paradox, yet 14 favoured the photograph-heavy Popular Actors over LLM Pricing.

**Teaching move:** Ask the class to predict which *other* classmates will succeed at a comprehension task, based on their chart preferences. Then test it. This exposes whether they have identified a genuine characteristic of a viewer or simply invented a plausible explanation afterward.

## Three questions I'd put to the room

| Ask students | Teaching objective |
| --- | --- |
| "Do faces help you understand Popular Actors, or do they obscure the actual question? What task would settle this?" | Features have benefits and costs depending on the task |
| "Can you correctly explain GDPVal's colours but still make the wrong decision from it?" | Recognizing visual cues isn't sufficient |
| "Why should we trust your prediction about an unfamiliar student's understanding?" | Replace intuition with evidence from real users |

**The key distinction to land:** These 72 responses measure students' *predictions* about comprehension, not comprehension itself. The most valuable next experiment is to give students unfamiliar visualizations, ask objective questions about their content and intended decision, then compare actual performance against these predictions.

Evidence: 72 A/B-comparison responses from 24 students, matched across the three questions in Graphene's `responses.tsv`. Choice counts were manually checked, including answers that rejected both options. Interpretations of students' reasons are qualitative; the correlation is exploratory and not statistically established.

# User

Top insights and gaps from mobile-app-evaluation responses?

# ChatGPT

I analyzed **23 mobile-app evaluation responses** from `~/code/liveform-data/ed5518-vizchitra-2026-11-04/responses.tsv`.

The main finding: **Students know many ways an app can fail, but almost nobody has specified how to prove that it works.**

## Top 3 insights

### 1. They have testing ideas, but no measurable acceptance criteria

# 8/23

Consider other devices or browsers

# 7/23

Propose real-world measurements or reference checks

# 0/23

Specify a numerical pass/fail threshold

Manual, non-exclusive coding of the responses. A reference check might still be poorly specified.

Students say things like "close approximation," "consistent results," "correctly detects," or "works as intended." Those sound reasonable, but none defines how close, how consistent, or what level of error is acceptable.

**What to teach:** A test must be reproducible and falsifiable.

For a step-counter app, for example:

> Walk exactly 100 steps, three times, on two different phones. Count manually as a reference. Accept readings between 95 and 105, and require the count to remain unchanged when stationary.

The tolerance is an illustrative design choice, not a universal standard. Have students defend it.

### 2. Students are divided between testing the technology and testing the user

One group focuses on the instrument: sensor accuracy, GPS, gyroscopes, floor-level measurements, or step counts.

Another focuses on user experience: Can a stranger use the app without help? Is it useful? Does someone need the solution?

Both are necessary, but **neither establishes the other**.

A particularly useful contrast:

* **Response #8:** Tests a floor-level checker using known level/bumpy surfaces and treats false positives as failures. Strong on technical correctness.
* **Response #19:** Tests whether a new user can use the app independently. Strong on usability.
* **Response #23:** Combines correct lift detection, consistency across phones, and understandable behavior. One of the most complete answers.

**What to teach:** Distinguish three independent tests: *Does it measure correctly? Does it survive realistic conditions? Can someone use it to accomplish the intended task?*

### 3. The best ideas emerged when students imagined failure, not normal operation

Response #18 is particularly strong:

> "Try no internet, low battery. Deny permissions, rotate screen. Watch a new user try it."

This is much stronger than checking whether the app launches.

Response #5 considers out-of-range inputs and unusual physics values. Response #13 suggests turning known bugs into regression tests.

There's also an interesting disagreement about ambition. Response #14 argues that a classroom project need only work reliably on one phone because time is limited. Others demand compatibility across devices.

**Teaching opportunity:** Ask whether that one-phone constraint is acceptable. The answer depends on the promise being made. A one-device prototype can succeed at demonstrating feasibility while failing a requirement to support arbitrary student phones.

## The biggest gaps

| Missing or weak idea | Why it matters |
| --- | --- |
| **Explicit tolerances** | Without thresholds, "accurate" and "reliable" cannot be verified |
| **Repeatability** | One successful trial doesn't test sensor noise, drift, or intermittent failure |
| **Privacy and security** | Nobody explicitly discusses location-data privacy, retention, or misuse of permissions |
| **Inclusive accessibility** | Device compatibility gets attention, but testing for users with disabilities does not |
| **Independent ground truth** | Comparing against an existing installation or estimated speed doesn't automatically establish correctness |

One caution: #12 proposes physically throwing a phone onto a soft surface as a test. That might generate interesting sensor data, but it introduces unnecessary device damage risk. A controlled shake or simulated sensor trace would be safer and more repeatable.

## What I'd teach next

Give every student this template and ask them to complete it for their own app:

**My app claims to:** Detect whether a surface is level.

**Ground truth:** A calibrated spirit level.

**Normal test:** Measure five surfaces with known orientations.

**Failure test:** Change phone orientation, deny sensor access, or test on another phone.

**User test:** Give a new user a task without instructions.

**Pass criteria:** State the permitted angle error, acceptable failure rate, and required user success rate *before* running the tests.

Then have them exchange phones and see whether the tests are actually executable.

## Here's what to say

* **You have good testing instincts.** Several of you suggested testing on other phones, checking sensor readings, and trying unusual conditions.
* **But a test needs a number or an observable outcome.** "Works correctly" isn't enough. Tell me what input you'll provide, what output you expect, and what would make you reject it.
* **An app can measure correctly and still be unusable.** A stranger should be able to accomplish its intended task without you explaining it.
* **Test when things go wrong.** Deny permissions, disconnect the internet, change orientation, and use an unfamiliar device.
* **Now swap phones.** The most interesting result is not whether your neighbor likes your app. It's whether they can make it fail in a way you hadn't anticipated.

**The strongest classroom question:** "What is one test your app would fail today?"

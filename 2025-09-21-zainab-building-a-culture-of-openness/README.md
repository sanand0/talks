---
marp: true
title: Building a culture of openness
author: Zainab Bawa
url: https://sanand0.github.io/talks/2025-09-21-zainab-building-a-culture-of-openness/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
# ChatGPT: https://chatgpt.com/c/68d16b08-cf44-8320-8893-6bb4a62735fa
---

<style>
transcript { display: none; }
</style>

# Building a culture of openness

[IndiaFOSS](https://fossunited.org/c/indiafoss/2025/cfp/0ios0i6o47) · 22 Sep 2025, 5:15 pm IST · [Bangalore](https://maps.app.goo.gl/Uon4KDWDqy65RGim8)
[Zainab Bawa](https://www.linkedin.com/in/zainabbawa/) · COO [Hasgeek](http://hasgeek.com/)
[Transcript](https://github.com/sanand0/talks/blob/main/2025-09-21-zainab-building-a-culture-of-openness/README.md)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-21-zainab-building-a-culture-of-openness/)

---

## Talk context & promise

- I know it’s late; **I’ll finish in under 15 minutes**.
- I won’t come in Nilesh’s way; I’ll keep it brisk.
- Thanks for sticking around; I’ll try to make this useful.

<transcript>

Okay, it's usually a bummer to have the last, second-last talk. Nilesh is of course, at the end after this presentation. But thanks to those of you who have stuck around and I really hope that I can sort of finish this in less than 15 minutes and then not come in the way of Nilesh and then the ending of this conference.

</transcript>

---

## Why openness in peer review

- Today I’m speaking about **building openness in peer review**.
- I frame it as **roles, rules, and returns** for clarity.
- Let’s see how far we get on this journey.

<transcript>

So, what I'm going to speak about, which the introducer mentioned, was building this culture of openness in peer review. And when I was thinking about this talk, it struck me that you know, **it's about roles, rules, and returns**. So let's see how far we can get in this journey.

</transcript>

---

## What problem are we solving?

- **How do we make peer review public?** That’s my core question.
- Typical journals keep reviewer identities hidden and comments private. (**Edit**: Single/double-anonymized review is common; open models also exist: [Wiley](https://authorservices.wiley.com/Reviewers/journal-reviewers/what-is-peer-review/types-of-peer-review.html), [Elsevier](https://www.elsevier.com/reviewer/what-is-peer-review).) ([Wiley Author Services][1])
- As an author, I’ve seen anonymous comments: “improve this, substantiate that.”
- **Readers see only the final article**, not the process. (**Edit**: Some venues publish peer-review history, e.g., [PLOS optional transparency](https://journals.plos.org/plosone/s/editorial-and-peer-review-process).) ([PLOS][2])

<transcript>

What was the problem that we were trying to solve? The problem that we were primarily trying to solve was to say, **how do you make this process of the peer review itself public?** So if any of you have—how many of you have published in a peer-reviewed journal? Please raise your hands here. Okay, Jaidev is one. Okay, not, there's one more person there. All right, so the typical process in a peer-reviewed journal, if I understand correctly because I've published in a peer-reviewed journal, is that the comments that, first of all, you don't know who your reviewers are. Most of the times the reviewers are anonymous. And secondly, you get sort of a bunch of comments on your draft saying, "improve this, improve that, these claims are not right, substantiate with data," etc.

</transcript>

---

## Why public feedback for practitioners?

- We want practitioners; **so we open up feedback to the public**.
- Conferences are a consumption experience; we also need participation.
- The question is: how do we turn review into a public conversation?

<transcript>

And so, by the time, and so the process itself is something that's hidden from the consumer, the end consumer. And it is something that the end consumer just gets to read the final article and whatever the findings of the article are. Now, in the case of Hasgeek, what we were trying to do was to say that because we want practitioners, people like yourselves who are actually in hands-on, day-to-day practice, how do we kind of **open up this very process of giving feedback to the public?** And I think there's, I mean, the learning that we've had particularly this year has been that there's the aspect which says that, oh, you know, at the end of this whole process of, you know, all the submissions, there is a conference, which is a showcase, and that's a consumption experience. But where is the participatory experience?

</transcript>

---

## From spreadsheets to **public forums**

- **We move reviews from closed spreadsheets to public forums**.
- Our old sheet showed who must comment, but little substance.
- Thin, transactional remarks don’t explain the problem or audience value.

<transcript>

So, the problems that we were trying to solve is: **how do you make this review public? How do you move this conversation that you have from closed spreadsheets to more public forums?** So let me try to give you an example over here. Here is our bulky spreadsheet that we created for this conference we ran on SRE and systems and security last year. And you can see like this is like all of this thing, okay, this person has to comment, this person has to comment. None of these comments are necessarily showing up over here. Wrong, wrong funnel. Okay, so here you can see that, you know, here are people who've submitted their work based on the work that they've done. So they've said, okay, I would like to speak about, you know, how do you move databases from Kubernetes in Flipkart's DBaaS journey. You have some comments over here, but it's by and large extremely thin.

</transcript>

---

## Transactional feedback isn’t enough

- Example: a “sidecars to serverless” talk had only slide logistics.
- The champion added notes, but **no deep discussion** on problem or impact.
- We want reviewers to probe outcomes, failures, and genuine insights.

<transcript>

Similarly, what you find over here is, let's see the next one. Here's someone who's talking about how to move, I mean, from sidecars to serverless, Achal's experience of what they did at Tecton. Now, if you see, the feedback here is extremely transactional. There's no feedback. There's just a transactional conversation about slides. Similarly, here, what has happened is the person who had tried to champion the slides, the champion, the submitter here has put in some sort of comments about the slides, but there's no substantial conversation around here with respect to saying, okay, what is the problem you're trying to solve? Why is it interesting for the audience? etc., etc.

</transcript>

---

## Hidden reviews don’t build community

- We used to **keep reviews hidden** while managing logistics.
- That produces a talk to consume, not a community to join.
- We want the **journey itself to be public** and collaborative.

<transcript>

So essentially, what was happening for us until about the end of last year was that this process of saying, okay, we're going to organize a conference, but **we're going to keep this review process hidden from the public**. And not intentionally, but it's because, oh, we are trying to manage this. And you know, the final outcome will just be this, you know, sort of a talk that people will consume, just like you're consuming my talk over here. And so we said, you know, that's not the way to kind of build a participatory community. So how do we open up this review? And how do you turn this into a conversation where you do not come in with the assumption that, you know, the person has a well-formed idea, that you actually help them go through that journey, and **that journey itself becomes public**. And I'll show you a few examples as we go through this today.

</transcript>

---

## Treat unselected submissions as an asset

- We got \~75 submissions; we select \~20%.
- Instead of discarding 80%, **we treat the rest as a community asset**.
- We keep those conversations alive through the year to grow the community.

<transcript>

And finally, the fact of, you know, if you look over here, there are about, you know, this conference last year received about 75 submissions, which is based on the work that people were doing. And, you know, typically the selection is, you know, maximum you've taken about like 20% of the submissions. Now, what do you do with the rest of the 80% submissions? Is it throwaway? Or rather, do you **treat this as an asset** and say that, hey, we're going to build this and, you know, we'll have conversations around this through the year, and that's how we will sort of, you know, build the community.

</transcript>

---

## Context: knowledge communities & tacit know-how

- Our context is knowledge-based communities (platform engineering, supply-chain security, AI in SDLC).
- We focus on **tacit knowledge**—learning from practice, not just public docs.
- This may not apply to generic communities.

<transcript>

So these were the three problems we were trying to solve. Before I move further, I'd like to qualify that the context that I'm referring to over here is that what we have been trying to build at Hasgeek have been these sort of knowledge-based communities where people want to come together to discuss a particular problem space. So that might be platform engineering, it might be as niche as supply chain security, or it's about how do you use AI in software life cycle development. And there's a desire **to learn and share from tacit knowledge**, which is that this is not knowledge that is out there in the public. It is something that you have learned over the course of your own practice, which you think is insightful, and that insight is something that, you know, people want to learn more about. So that's by and large the context, and so it may not apply in this case, it may not apply to, you know, sort of a more, you know, a more generic community, but this is generally the context in which we are operating.

</transcript>

---

## Who are the actors?

- We have editors (audience stewards), **reviewers** (today’s focus), scouts, auditors, and ops.
- I’ll walk you through the reviewer’s role.
- Happy to discuss other roles after.

<transcript>

Now, to move quickly, the way in which this whole peer review process works is that there's a variety of actors. And what I will do in this presentation is just walk you through the role of the reviewer. And as it happens, Murphy's law. Okay, we're back. So what I will do is walk you through just one of the actors over here and happy to chat with you about the others if you have an interest afterwards. And so, among the actors that we have, we have the editor who's essentially the steward of the community. They champion the audiences. Then you have reviewers, who I'll explain sort of in the subsequent slides. And you have scouts who are basically people who kind of like, you know, get people from their network to submit ideas and who want to, and who basically, it could be a manager in an organization who wants to get, you know, their team members to speak, or it could just be, hey, I have a friend who's got an interesting idea, let me, you know, get them forward, etc. And then we have an actor called the auditors, who basically are the people who review the reviewers. And then you have an ops coordinator. But like I said, in this talk, we'll just speak about the reviewers as the role.

</transcript>

---

## Why would I review?

- Reviewing is voluntary; **I want industry visibility beyond my silo**.
- I want to contribute and shape others’ work—**but with scoped time**.
- Personal branding helps, but boundaries matter for sustained contribution.

<transcript>

So what is the incentive for somebody to participate in reviewing? And please note that this is a completely voluntary activity in the sense that you're not necessarily paid for your time to sit and listen and give feedback and to write your notes about feedback, etc. So the incentives to review are, I think, you know, everybody sitting here would sort of agree that the industry in which we operate in technology is fairly siloed. It's very, it's, one operates in isolation, whether you are inside an organization or whether you're in a domain space, you generally do not know what's really happening to organizations outside unless you have friends in other companies who are sharing with you what's going on. So there is generally a need to know what's happening in a domain or in the industry, and so that becomes an incentive to review. Then there's an aspiration to say, hey, I'd like to contribute because if my contribution helps in like, you know, shaping someone else's work, in their career, in their influence, then, you know, it gives me that sort of a satisfaction that I was able to contribute. But this contribution is something that I'd like to do in a very **limited, scoped role**, which means that I need to know how much time I'm going to give, what is my role, and where is my boundary sort of like, you know, begin and end. And then, of course, there is always a need to say, hey, you know, I was a reviewer for someone, and you know, that goes into my personal branding later. So these are, this is typically the sort of, you know, hierarchy of needs that we have. And what we essentially look in most of our reviewers is where the, all right.

</transcript>

---

## Aligning incentives practically

- We build a **pool of submissions** to pick from.
- Reviewers choose topics they care about; that keeps motivation high.
- Curated funnels make “what to review next” obvious.

<transcript>

So then, how do you kind of align the incentives that people have with respect to saying that, hey, I'd like to know what's happening in the industry? So what we end up doing is create this sort of a funnel or a pool of what we call submissions where people come and sort of, you know, submit their ideas, the work that they are doing. And, you know, this is, this becomes an incentive to say, okay, you know, here I can pick and choose from like, you know, a pool of submissions that I'd like to review.

</transcript>

---

## Who is a reviewer?

- Past speakers or ecosystem contributors who **elevate the bar** of discussion.
- They push for honest outcomes, failures, and specifics—not tool listing.
- They aim to create a high-quality audience experience, even challenging editors if needed.

<transcript>

Now, what we also do over here is to induct the reviewers into their role and into rules. And this is extremely important because if you fail here, then you basically fail the entire process. And so who is a reviewer? Typically, it's a, it's a past speaker or past presenter who has received feedback and who knows how to give feedback. Or it's somebody who's an ecosystem contributor who's kind of been there, been around, and has a strong need to contribute back. It's also an individual who **elevates and pushes the bar for discussions and for sharing knowledge**. So if you remember the context that I shared over here, which is to say that we're trying to build communities of practice where people want to share tacit knowledge, the idea is that the reviewer is somebody who wants to kind of push the bar and say, hey, I'm not interested in just learning about like what tools you use, but I want to know like what were the outcomes over here? Where did you fail? Where did you succeed? So essentially, you know, kind of get to more honest discussions and just posturing. And then, you know, a reviewer is somebody who strives to create high-quality content and experience for the audience. And this sometimes even contradicts, you know, the editor's vision or roadmap, but that's a healthy tension to have.

</transcript>

---

## What rules do reviewers follow?

- **Depth over breadth**; nuance beats superficial coverage.
- **Details vs claims**: ask for metrics, proofs, and outcomes.
- **Help tease out ideas** others might miss; sharpen the takeaway.
- Manage conflicts of interest transparently.

<transcript>

And then there is, of course, the rules. What is it that you're reviewing and how do you actually go about reviewing? And here, you know, we sort of are very anal about following some of these rules, which is **depth is far more important than breadth**. You can always like, you know, sort of skirt over a lot of, you know, a broad area, but what matters is how deep do you go into this and how nuanced is your, is the experience and is the argument that you're making. Then **details versus claims**. So, if somebody says, hey, you know, I saw this XYZ outcomes, where are the metrics? What are you, you know, what is the proof that substantiates that, you know, this was a success in, you know, your sort of understanding of whatever success is? So essentially, you know, sort of push the boundary to making it more and more honest and not just posturing in the sense of like, of making claims that are not substantiated. And similarly, you know, the metrics and data points matter. So if you say that, you know, there is a success in the organization, then where are the data points to show what constitutes a success? What outcomes did your customers experience, etc.? And then among the other rules that we have is that, oh, I'm just going back and forth on my slide. Okay, and then among the other rules that are there is, what is relevant is that for the reviewer is to essentially **help a submitter to kind of tease out the very ideas and the very sort of insights that would otherwise not be so obvious to others**. So the idea is that if you are sort of, you know, in the consumption experience, you have something that you take away at the end of listening to a presentation or a session. And this is not just something that's shallow enough over here. So the rule is that you have to really help sharpen the takeaway. And if you were sitting in the audience, you know, what is it that you would take in as an insight? And then, of course, we have to manage conflicts of interest. Let's say a submitter is from the same organization as a reviewer, in which case then we call out the conflict of interest and replace the reviewer with someone else. So, the, these are sort of by and large the rules, and this is something that we follow very strongly now in our induction process with reviewers, in a way to just ensure that, you know, the points of failure are sort of fewer.

</transcript>

---

## Where does this break?

- Enthusiasm can fade; managing 15–20 people becomes overhead.
- Weak onboarding causes contradictory reviews and confusion.
- Public comment expectations raise the bar for clarity and rigor.

<transcript>

Does this mean that this process works foolproof? Well, you know, in some cases, you know, there's always challenges. And so I've mentioned failure here, but I mean, this could, you know, very well just be challenges. You have people who sort of are enthusiastic at the start but then who become uninvolved for various reasons. And, you know, then it becomes a communication overhead because what you're managing is 15-20 people at a time. If the onboarding is not right, then it leads to hiccups where if you do not specify the rules clearly, then you find that, you know, reviewers can contradict each other. And then I think the most important thing that we've seen is that, you know, while there is enthusiasm to say, "Hey, I'm going to do review," you know, when it actually comes to it and saying, "Hey, you know, you've got to post your comments in public." So for instance, you know, here is a submission that someone's made on building production-grade LLMs, blah, blah, blah with DSPy. And you can see that here, you know, the feedback is all out there, which is open for you also to see, and it's not just on my computer, which is, you know, sort of asking a lot of, you know, details and a lot of questions about saying, okay, you know, why are you doing this and, you know, why is it, you know, you know, how is it that it will help the audience, etc.

</transcript>

---

## Public feedback hesitation

- Folks say yes, then balk: **“my comments will be public.”**
- Asking for details **in public** can feel intimidating at first.
- Expertise mismatches overload a few; **gender imbalance** worsens diversity. (Evidence: women are underrepresented among reviewers/editors.) ([Science][3])
- (**Edit**: Open/signed review can increase decline rates among invited reviewers: [BMJ RCT](https://pmc.ncbi.nlm.nih.gov/articles/PMC27670/).) ([PMC][4])

<transcript>

So going back to, you know, the points of failure is that many a times people are enthusiastic to say, "Yes, I'm going to participate to review," and then it's like cold feet saying, "Oh shit, **my comments are going to be public. It's not going to be private.**" And then also the fact that, you know, you have to ask for details in public. You have to kind of give your feedback in public. So that, you know, if you didn't expect this transparency, then you kind of start out and totter in the beginning. And then you've also seen in our experience that, you know, when it comes to organizing a conference as large as IndiaFOSS, if you haven't sort of like, you know, quantified the number of reviewers you have, you find that a lesser number of people are doing more work, in which case then the overheads increase. And because, you know, the context in our case is sort of building these practice and, you know, knowledge-based communities, if the expertise is mismatched, then you have a subpar review for the submitter. And then, of course, you know, there's the gender dynamic that is always a challenge, which is that when you're building these communities of practice, particularly in the area of technologies, technology, you have few women reviewers. And so the gender dynamic sort of gets skewed more towards having male reviewers than having and fewer female reviewers.

</transcript>

---

## Onboarding, authenticity, and scope

- **Onboard reviewers clearly on roles and rules upfront**.
- Set expectations that **everything happens in public**.
- No templated AI voice; **use your authentic voice** (see _Cluetrain Manifesto_). ([cluetrain.com][5])
- Scope and bound the role; volunteers burn out without limits.

<transcript>

So I'm going to try and conclude over here in the interest of time, which is that our overall learnings have been that it's really important to be able to **onboard your reviewers both in terms of their role and the rules very clearly at the outset**, and the expectations that **everything you're going to kind of discuss is going to be in public**. We've had reviewers who've, you know, sort of, is that the warning bell? Yeah, it is the warning bell. Okay. So we've had reviewers who've, you know, sort of said, "Oh, can I resort to ChatGPT to write out my comments?" And we're like, no, you speak in your own way. So if you've sort of read the Cluetrain Manifesto, **what matters is your own authentic voice**. So there is this sort of, you know, pushing happening saying that, hey, you know, use your own authentic voice. Role clarity is important, and you also need to **scope and bound the role** because your reviewer is coming in as a volunteer. If you're asking them to do too many things, then, you know, that's where collapsing happens, and it leads to overload, and then, you know, there can be points of hiccups and tottering and, you know, lack of success.

</transcript>

---

## Outcomes over good feelings

- **Success is proportional to investment** from all actors.
- Track outcomes with metrics; show reviewers what they are contributing to.
- **Good vibes don’t suffice; outcomes matter** and should be quantified.

<transcript>

And finally, **success is really proportional to the investment of all the actors**. In this case, you know, the reviewers play a very important role in terms of not just the quality of content that comes forward over here, but also the quality of interactions that sort of leads to that, and then also the success of the presenters out there. And if, you know, the metrics and, you know, tracking these outcomes of success are not very clear, then the reviewers also do not know in terms of, you know, what are they really contributing towards. So the end learning that you know, we've had in this process is, **it's not the good feelings that matter**... because usually people say, "Oh, you know, as a community, it's very nice, we've all come together and, you know, it's a very nice feeling." But **what matters is the outcomes**. And it's important to kind of quantify and give metrics to the outcomes if you would like to have your reviewers and the review process to be invested. So yeah, with that, thank you very much, and I'm done.

</transcript>

---

## Quiz

- What concrete changes turn a consumption-only conference into a participatory one?
- How does “depth vs breadth” alter reviewer prompts and acceptance criteria?
- Which incentives keep voluntary reviewers engaged without scope creep?
- Name two risks of public/signed review and one mitigation.
- How would you repurpose the unselected 80% to grow community impact?

---

## Errata

<small>

- “Most reviewers are anonymous; readers see only the final paper.” **Correction/Context**: Single/double-anonymized is widespread, but open/transparent models (eLife reviewed preprints; PLOS optional history; F1000Research open reports) also exist. ([www.elsevier.com][6])
- “Public/signed reviews scare off reviewers.” **Nuance**: Evidence shows signing increased decline rates in a BMJ RCT; quality unchanged. ([PMC][4])
- “Gender dynamics skew male reviewers.” **Support**: Studies show women are underrepresented among reviewers/editors across fields. ([Science][3])

</small>

---

## Counterpoints

<small>

- **Open review may yield timid reviews** that avoid hard judgments on novelty or significance. (Nature Neuroscience editorial.) ([Nature][7])
- **Blinding can reduce geographic/status bias**, improving fairness of acceptance decisions. (JAMA abstract blinding study.) ([JAMA Network][8])
- **Double-blind may lower acceptance rates** vs single-blind; policy choice affects throughput and reviewer load. (Meta-analysis/report.) ([ScienceDirect][9])
- **Open models vary** (transparent, post-publication, decoupled), each with trade-offs in speed, accountability, and labor. (F1000 overview; 2024 scoping review.) ([F1000][10])

</small>

---

## Feedback

- Add a one-slide comparison of peer-review models (single/double-blind, transparent, open) with pros/cons and examples.
- Show one “before vs after” public review thread to illustrate depth-over-breadth in action.
- Quantify outcomes: acceptance rate, reviewer participation, comment depth, and speaker success metrics over time.
- Outline a minimal reviewer playbook (5 prompts, timebox, conflict-check) to lower volunteer friction.
- Close with a “reuse the 80%” roadmap: monthly salons, issue trackers, and public backlog owners.

---

# Building a culture of openness

[IndiaFOSS](https://fossunited.org/c/indiafoss/2025/cfp/0ios0i6o47) · 22 Sep 2025, 5:15 pm IST · [Bangalore](https://maps.app.goo.gl/Uon4KDWDqy65RGim8)
[Zainab Bawa](https://www.linkedin.com/in/zainabbawa/) · COO [Hasgeek](http://hasgeek.com/)
[Transcript](https://github.com/sanand0/talks/blob/main/2025-09-21-zainab-building-a-culture-of-openness/README.md)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-21-zainab-building-a-culture-of-openness/)

[1]: https://authorservices.wiley.com/Reviewers/journal-reviewers/what-is-peer-review/types-of-peer-review.html?utm_source=chatgpt.com "Types of Peer Review"
[2]: https://journals.plos.org/plosone/s/editorial-and-peer-review-process?utm_source=chatgpt.com "Editorial and Peer Review Process | PLOS One"
[3]: https://www.science.org/content/article/when-women-are-missing-peer-review?utm_source=chatgpt.com "When women are missing from peer review"
[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC27670/?utm_source=chatgpt.com "Effect of open peer review on quality ..."
[5]: https://www.cluetrain.com/?utm_source=chatgpt.com "The Cluetrain Manifesto"
[6]: https://www.elsevier.com/reviewer/what-is-peer-review?utm_source=chatgpt.com "What is peer review?"
[7]: https://www.nature.com/articles/nn0399_197?utm_source=chatgpt.com "Pros and cons of open peer review"
[8]: https://jamanetwork.com/journals/jama/fullarticle/202669?utm_source=chatgpt.com "Effect of Blinded Peer Review on Abstract Acceptance"
[9]: https://www.sciencedirect.com/science/article/abs/pii/S2589933322000805?utm_source=chatgpt.com "vs single-blind peer review effect on acceptance rates: a ..."
[10]: https://www.f1000.com/resources-for-researchers/open-research/open-peer-review/?utm_source=chatgpt.com "Open peer review | Improve your understanding with ..."

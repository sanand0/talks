---
title: "Jio Institute Convergence 2026 Talk Topics"
date: 2026-09-03T15:23:05+08:00
source: "https://chatgpt.com/c/6a92363e-5624-83ec-a95b-9843854af9a3"
---

# User

I'm delivering a keynote at Jio Institute's Convergence 2026.

- [https://www.jioinstitute.edu.in/convergence-2026](https://www.jioinstitute.edu.in/convergence-2026)

Schedule:\* [https://www.jioinstitute.edu.in/sites/default/files/media_document/Convergence%20Schedule%20%281%29.pdf](https://www.jioinstitute.edu.in/sites/default/files/media_document/Convergence%20Schedule%20%281%29.pdf)

On @LocalMCP read my recent emails about this. Research the conference, attendees, schedule, my talk's stated agenda "Inaugural Keynote II - Data Storytelling" - which we don't need to stick too closely to (I can always link almost ANYTHING to data storytelling), the audience and their profile and interests, etc.

I have 15 minutes for this talk.

OBJECTIVE: Suggest prioritized talk topics aligned with the conference, not overlapping with other talks.

I use talks to push myself to learn something new, test ideas live, learn from the audience, give them a useful surprise, and build compounding assets before/during/after.

Infer what I'm exploring from memory, chat history, then @LocalMCP - unresolved questions, emerging ambitions, changed beliefs, recurring interests, recent surprises, and connections across unrelated work. Prefer recent choices, excitements, what I keep returning to.

Find questions I genuinely don’t know the answer to (I might not even know they're worth pursuing),
that solve a REAL, frequent audience need,
that they may not learn elsewhere (novel),
that I can demo/test live - even failure should teach something,
that can produce a reusable asset,
and leave them knowing what to do differently.

Share the title, what I'd learn, why they care, the live experiment/surprise, reusable asset.

Prefer what makes me think, "I don't know, this is a great place to find out."

# ChatGPT

The best framing is: **don’t choose a topic; choose a question the room can help you answer.** “Data Storytelling” is useful cover, but I would make the keynote itself an experiment.

The conference has an unusually useful mixture: C-suite leaders, AI/DS builders, faculty, AI/DS students, and management students. Jio explicitly wants to bridge technical AI with business decision-making, around the question “When AI can act, how will businesses transform?” [JioInstitute](https://www.jioinstitute.edu.in/convergence-2026) And this is not an introductory-AI crowd: last year included AWS, Microsoft, Google, OpenAI, Grab, Schneider Electric, DBS, and Singapore universities. [JioInstitute](https://www.jioinstitute.edu.in/news-stories/convergence-2025-intelligent-futures-aligning-talent-technology-transformation?utm_source=chatgpt.com)

The schedule also defines your white space. Immediately before you is **human judgment**. Immediately after is **AI trends in APEC**. Then come **enterprise growth/innovation/marketing** and **AI in finance**. So I would actively avoid generic “humans + AI,” agentic-enterprise forecasts, AI transformation, marketing personalization, finance, governance, or “five rules of data storytelling.”

From your recent work, the thread I see becoming much more interesting is a shift from **AI executing work → AI discovering what work is worth doing**. In TDS you're increasingly interested in problem selection, verification, model choice and retiring saturated skills. In your agent work, you're watching agents choose their own search methods, build tools, revise plans and potentially improve their own capabilities. In your recent science-talk exploration, the fascinating jump is from agents solving questions to agents making discoveries. And your visual-AI question has similarly moved from “what new form can AI make?” to “what unmet need should a new form serve?”

That leads to this ranking.

1. **The Question You Didn't Ask — Can AI automate curiosity?**
   **What I'd learn:** Can an autonomous agent, given a business objective and messy data but _no question_, discover a question/hypothesis that smart humans did not think to ask, test it, try to falsify it, and produce a genuinely decision-relevant finding? That's much less settled than “can an agent analyze data?”
   **Why they care:** Answers and analyses are becoming abundant. The harder enterprise problem is increasingly deciding where to look, what might matter, and what experiment is worth running. This speaks equally well to the CEO, data scientist and student.
   **Live experiment/surprise:** Get an anonymized export of Convergence registrations if Jio will share it: roles, industries, geography, AI experience, interests, etc. First ask the audience what _they_ would investigate. Then give an agent the same data with only: “Find something this room would benefit from knowing.” Require it to generate many hypotheses, test them, discard weak ones, and tell one 45-second visual story. Then unleash a second agent whose only job is to destroy that finding. Finally the room votes: **obvious / interesting / changes what I'd do**. If it finds nothing valuable, that's a result too: autonomous execution has arrived before autonomous curiosity.
   **Reusable asset:** **Question Miner**: an open harness for `objective → candidate questions → evidence → falsification → story`, plus a growing benchmark of datasets, human questions and audience judgments. Every workshop or conference can add another test case. It could become a TDS assignment, Straive discovery tool, blog series and research project.
   This is my clear #1. It gives “data storytelling” a much better role: **the story is the final 60 seconds of a scientific discovery loop, not the starting point.**
2. **Every Skill Needs an Expiry Date — What should we stop learning?**
   **What I'd learn:** Not “which skills will AI replace?” but the much more operational question: **what evidence should make us stop teaching or investing in a skill?** Can we measure skill half-life rather than speculate about it?
   **Why they care:** This fills a conspicuous programme gap. Jio calls **Hybrid Talent Architecture** one of Convergence's four pillars—AI-bilingual talent, reskilling and job redesign—but the current schedule has no session devoted to it. [JioInstitute](https://www.jioinstitute.edu.in/convergence-2026) It is directly relevant to both employers and the Jio students sitting beside them.
   **Live experiment/surprise:** Put up 4–5 skills—say SQL, coding, prompt engineering, dashboarding, research synthesis. Have the room predict which are still worth 100 hours of human learning. Then reveal actual frontier-agent task tests, ideally ones you run/re-run just before the keynote. The surprise isn't “AI can code”; it's that **we can create an empirical retirement rule for a curriculum**.
   **Reusable asset:** A continuously updated **Skill Half-Life Index**: realistic tasks, frontier-model performance, cost, reliability and a criterion for when teaching should move from “learn to do” to “learn to delegate/check.” This could materially influence TDS and Straive's upskilling.
   I rank this second because the conference fit is superb, but you've already developed more of the underlying thesis than in #1.
3. **The Story That Fights Back — Can a data story cross-examine itself?**
   **What I'd learn:** Can autonomous adversarial review make AI-generated business analysis substantially more trustworthy, or does it merely generate more eloquent disagreement?
   **Why they care:** Soon organizations can produce 100× more analysis than humans can inspect. “Have a person verify everything” cannot scale. Yet the other speakers will mostly discuss whether humans retain judgment; you can ask the orthogonal question: **how much judgment can we build into the system itself?**
   **Live experiment/surprise:** Show a very persuasive 60-second data story containing one defensible-but-misleading conclusion. Let the audience decide whether they trust it. Then reveal the **prosecutor agent**, which searches for omitted denominators, alternative explanations, newer evidence and contradictory cuts of the data. The story visibly rewrites itself on stage. A stronger variant has two agents construct opposite stories from the same dataset before a third attacks both.
   **Reusable asset:** **StoryCourt**: storyteller → prosecutor → evidence checker → surviving claims, with a visual provenance trail. It extends naturally into your research-validation and verification work.
   The memorable rule they leave with: **never ship an AI recommendation without asking what evidence would make it change its mind.**
4. **The Last Dashboard — What is visualization for when AI can understand the data for us?**
   **What I'd learn:** Your recent hypothesis is unusually interesting: perhaps visualization's future is less “help me understand the dataset” and more **help me specify what I want and verify what the agent did**. Is that actually true?
   **Why they care:** Companies are still investing heavily in dashboards while simultaneously giving agents direct access to the underlying data. The answer affects analytics teams, product design and management workflows.
   **Live experiment/surprise:** Give three approaches the same decision problem: a conventional dashboard; an agent with the raw data; and an agent that generates a bespoke visual decision interface on demand. Give audience members 60 seconds to make the decision and compare speed, correctness and confidence. You genuinely don't know which will win.
   **Reusable asset:** A benchmark for **dashboard vs chat vs generated interface**, reusable across datasets and audiences. This also advances your broader visual-AI question: don't invent visual forms because they're novel; discover where visual interaction still adds measurable value.
   This is probably the strongest choice if you want to remain visibly closest to “Data Storytelling.”
5. **The Prompt That Deletes Itself — Can AI know what it no longer needs to be told?**
   **What I'd learn:** Can an autonomous system detect that its own instructions, workflows and “best practices” have become obsolete as models improve—and safely remove them?
   **Why they care:** Enterprises are busy accumulating prompt libraries, agent rules and playbooks. At current rates of capability improvement, much of this becomes **instruction debt**. Your actual progression from a 91-line browser skill to roughly a dozen lines is a striking starting story.
   **Live experiment/surprise:** Give today's model one of your older agent skills plus a benchmark from actual failures. Ask it to prove which instructions are still necessary and delete the rest. The visual is beautiful: a large block of “enterprise AI best practice” disappearing line by line because the underlying intelligence has learned it.
   **Reusable asset:** An **expiry-date + benchmark governor** for agent skills: periodically test every instruction; retain it only while removing it measurably hurts performance.
   This is my wildcard. It's the least obviously “data storytelling,” but perhaps the most unusual idea the audience will hear that evening.

If I were committing today, I would call the talk:

**The Question You Didn't Ask**
_Can AI automate curiosity?_

The 15 minutes almost writes itself. **0–2 min:** “We have spent three years making AI better at answering questions. I want to know whether it can find the question.” **2–4:** humans inspect the dataset and nominate what they'd ask. **4–9:** autonomous agent explores it, visibly generating/killing hypotheses. **9–11:** it tells its best data story. **11–13:** adversarial agent attacks it. **13–14:** audience judges human vs AI discovery. **14–15:** one practical takeaway and QR code to Question Miner/results.

The best part is that you should **not know the ending**. You can pre-test the mechanics but not curate the winning discovery. A weak result gives you “agents can execute, but curiosity is still hard.” A strong result gives you “we just watched an agent find something a room full of experts didn't ask.” Either is a keynote.

I would specifically not use your recent **“What can AI not do?”** survey as the main talk, despite it being fresh and having good data. It naturally ends up discussing reliability, reach, presence and what remains human—the keynote immediately before yours has already claimed precisely that intellectual territory. Likewise, I wouldn't make AI agents doing science itself the topic; **stealing the scientific method and applying it to business discovery** is the more surprising connection for this room.

One immediate move would substantially improve #1: ask Jio now for an anonymized registration export. Even five mundane columns are enough. If they also collected “why are you attending?” or “what AI challenge are you facing?”, it becomes almost ideal.

I can also watch the published programme through September 3 and flag any change that creates new overlap.

# User

Here's another answer from Claude.
Take what's better, drop what's worse, explore any new thoughts this leads you to, and rewrite your response based on that.

```markdown
## What I found

**Your slot:** 4:50–5:05 pm, Thu 3 Sep, Nanyang Executive Centre, NTU. You are Inaugural Keynote II of three, listed as "Data Storytelling."

**Who's around you (this is the important bit):**

- **Right before you:** Madhur Mayank Sharma (SAP) on _"Why Human Judgment Is the Most Valuable Intelligence in an Algorithmic World."_ He owns "humans still matter / judgment / trust."
- **Right after you:** Anni Tankhiwale (Meta) on _"Trends in AI in the APEC Region."_ She owns macro trend charts.
- **Then:** a fireside on enterprise AI growth (Rezolve, AllThings Connected, Agilitas) and a finance panel (UOB, Bank of Singapore, Crayon Data, AIII).

So three lanes are taken: human judgment, regional trends, and enterprise/finance case studies. Also note the panels are moderated by Jio Institute students, and the whole thing ends in a networking dinner.

**What nobody is doing:** anything live, anything with real numbers from the room, and anything about the flip side of "AI can act" — that AI acting means machines are now _reading_ your business.

**Two things changed since your emails:** the Meta speaker is now Anni Tankhiwale (not Sandhya Devanathan), and Suresh V Shankar moved to the finance panel. Timing also tightened to 6:30 pm.

---

## Ranked topics

### 1. "What's Left?" — a data story built live from this room

**What you'd learn:** You asked 166 people what they didn't ask AI last week because it can't do it. You got Reliability 37%, Reach 27%, "it can do everything" 14%, Presence 12%. That sample was mostly Indian, mostly services and tech. **You genuinely don't know how a Singapore C-suite answers.** You have a public, dated prediction (Reliability under 25%, Reach under 15% by December). This room is fresh evidence for or against it.

**Why they care:** Every leader in that room is privately asking "where is the boundary?" Every vendor answers with a slide. You'd answer with the boundary drawn by their own peers, sixty seconds ago.

**Live experiment:** QR code in your first minute, one question, liveform. While they answer, you tell the 166-person story. Then flip to their live chart. Before revealing it, make them guess: "Which of these four will be biggest here?" Guess-then-reveal is the surprise engine.

**The useful surprise:** the thing AI can't do is _be in a room_. You deliver that line in a room, forty minutes before a networking dinner. It hands off perfectly to the rest of the evening and to Madhur's judgment argument without repeating it.

**Reusable asset:** the liveform instrument itself, the dataset growing from 166 to 250+, a blog post, and a repeatable "boundary survey" any org can run on its own staff. It compounds at every talk you give.

**If it fails:** if Reliability is still 40% in a senior finance room, your December prediction is in trouble. That's a better story than being right.

---

### 2. "Can an agent buy from you?" — data storytelling when the reader is a machine

**What you'd learn:** You have three theories from the Fifth Elephant workshop you've said you're not sure about: tools beat tables, logs beat docs, messy beats clean. You've never tested them on the public surfaces of Singapore banks, exchanges, or universities.

**Why they care:** This is the sharpest fit with the conference theme that nobody else will touch. The theme is "when AI can act." The corollary nobody says out loud: if AI can act, AI is also acting _on you_, and most companies are invisible to it. Their docs, product pages, and APIs were written for humans. Their agent readiness has never been measured.

**Live experiment:** on stage, give an agent one buyer-shaped task against three or four named public sites. Score it: found it, got it wrong, or refused. Use Jio Institute and NTU as safe targets, plus one volunteer's company from the room. A failure on stage is the whole point.

**Reusable asset:** an "Agent Readiness Score" script and a public leaderboard, plus an`llms.txt` / `AGENTS.md`checklist. Very assetizable, and it's a live demo you can run at any client meeting.

**Risk:** conference wifi, and naming attendees' brands. Pre-record a fallback. Ask permission from one volunteer only.

---

### 3. "Six charts, one vote" — the Curator's Dilemma, compressed

**What you'd learn:** at VizChitra, the top-voted chart was 100% AI-generated and the groups disagreed with themselves once you split them. That was a room of visualisation practitioners. **Does a room of bank and enterprise leaders disagree more or less?** You don't know.

**Why they care:** they are all about to sign off on AI-generated analysis, and none of them have a verification method.

**Live experiment:** show six charts, room votes, reveal that the winner was machine-made and actually published. One round only, 15 minutes is too tight for two.

**Why it's ranked third:** it sits closest to Madhur's judgment talk. You'd be the empirical second-mover. That can be turned into a strength ("here's the evidence for what Madhur just argued"), which is generous and memorable, but it costs you the fresh lane.

---

## Wildcards

**A. "Give the agent this conference."** Live, feed an agent the Convergence schedule, the speaker list, and the three past editions, and have it produce a data story about _this event_ on stage in three minutes. What does it notice that the organisers didn't? Very high surprise, very low typicality, slightly dangerous. Reusable as a "conference mirror" skill you run at every event.

**B. Pre-registered predictions, sealed live.** Put three dated claims on screen, have the room vote, then email everyone the scored result in December. This is your prediction log turned into an audience asset and a follow-up list. Better as the closing 90 seconds of topic 1 than as a whole talk.

---

## My pick

**Topic 1 as the spine, wildcard B as the close, and 60 seconds of topic 2 as the "so what do I do Monday."**

Reason: it is the only option where the talk _is_ a data story rather than a talk _about_ data storytelling. You satisfy the stated agenda by demonstrating it. You take a lane nobody else has. The audience effort is one tap on a phone they're already holding. And you leave with data you didn't have that morning.

The one line they walk out with: _"AI's reach and reliability problems are closing faster than you think. Presence isn't. Plan your org around what's left, not what's broken today."_

---

## Things to sort with Darrsheni this week

- Can you put a QR code on screen, and is there guest wifi that phones can actually use?
- Can you get the registered attendee list beforehand? It changes what you can pre-run.
- Ask for a Jio student to read out the live poll results. It costs you nothing, frees your hands, and Jio will love it.
- Screen aspect ratio and whether you control your own laptop.
- Shailesh Kumar invited you and you said you wanted to hear how Jio teaches AI. Worth booking ten minutes at the dinner rather than leaving it to chance.
```

In any case, I'm keen on asking a few questions via a Google Form before the event and (a) doing the analysis live on stage or (b) sharing insights from the analysis during the talk. So, give me the questions I could share with the team and have them fill it out. Not too much, not too long, they should be able to fill it out in 2-3 minutes.

# ChatGPT

I would revise the recommendation toward Claude’s version in one important way: **use the room as the dataset**, but don’t make the survey only about “what AI cannot do.” That risks predetermining the story.

The better experiment is:

**What work are smart people still keeping for themselves—and why?**

That gives you several possible discoveries: perhaps reliability still dominates; perhaps access/reach has vanished; perhaps senior leaders retain judgment/accountability while students retain different things; perhaps people _want_ to delegate things they currently think AI cannot do. You genuinely don’t know which story will emerge.

For a 2–3 minute Google Form, I’d use these **6 questions**:

1. **Which best describes what you mainly do?**
   Single choice:

- Business / general management
- Technology / engineering
- Data / AI
- Finance
- Sales / marketing
- Education / research
- Student
- Other

2. **What is one recurring work task you wish AI would take off your plate completely—but you still do yourself?**
   Short text.
   _“None” is a valid answer._
3. **What mainly stops you from handing that task over to AI today?**
   Choose up to 2:

- It gets things wrong / I still need to verify it
- It cannot access the data or systems it needs
- It cannot take the actions required
- The task needs judgment or context I don’t trust it with
- The task needs human interaction / presence
- Security, privacy, compliance, or policy
- Cost / speed
- I don’t yet know how to make AI do it
- Nothing — I already delegate almost everything I reasonably can
- Other

4. **What is one thing you did last week that you deliberately did _not_ ask AI to help with? Why not?**
   Short text, one or two sentences.
5. **Imagine AI became 10× more reliable and could securely access all your work systems. What part of your work would you still want to keep for yourself?**
   Short text.
   _“Nothing” is a valid answer._
6. **What is one question about AI and work that you genuinely don’t know the answer to—but would like this room to help answer?**
   Short text.

I particularly like questions 2, 5 and 6. They separate three things that are usually muddled together:

- **“I want AI to do this, but it can't yet.”** → current bottleneck.
- **“Even if it could, I would keep this.”** → possibly durable human territory.
- **“I don't even know the answer to this.”** → unexplored territory.

That makes the live analysis much more interesting than simply reproducing your previous Reliability / Reach / Presence taxonomy.

On stage, I’d give an agent the raw responses and ask something deliberately open such as:

> “You have responses from the people in this room. Find the most important thing about how they are actually using—or not using—AI that they probably don’t already realize. Test alternative explanations before you answer.”

Then ask a second agent:

> “Try to prove that conclusion wrong.”

That becomes **data storytelling as live discovery**. You don’t know the story until the room creates the data.

A few design choices matter. Keep it anonymous by default; don’t ask company/name unless Jio specifically needs them. Ask Q2 before showing any Reliability/Reach/Judgment/Presence categories, so you get an unprimed answer. Make all free-text fields short-answer rather than paragraph fields—the visual cue itself keeps responses terse. And send the form before the event, while keeping it open during pre-conference networking so you can say, “These are literally the people in this room.”

I’d also slightly change the talk title from my previous recommendation. My current favorite is:

**What Are You Still Doing Yourself?**
_An experiment in where AI really stops._

It fits “Data Storytelling” without sounding like a data-storytelling lecture, and the answer is not something you know in advance.

# User

Create the Google Form for me on my [root.node@gmail.com](mailto:root.node@gmail.com) account. If possible use `gws` on @LocalMCP else CDP at localhost:9222

# ChatGPT

Created in `root.node@gmail.com`, published, and verified publicly accessible.

[Fill the form](#)

[Edit the form](#)

It has 5 questions, should take about 2–3 minutes, is anonymous, questions 1–4 are required, and the final “question for the room” is optional.

One limitation: Q3 says “Choose up to 2,” but the Forms API cannot enforce that maximum; respondents can technically tick more.

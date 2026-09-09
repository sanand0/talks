---
title: "Breaking out of simplification feedback loops"
date: 2026-09-09T11:09:00+08:00
source: "https://claude.ai/chat/6030d9f5-abff-45fa-b511-774e8aaa7546"
---

# User

Help me answer this question from a student:

hi anand, thank you for answering my email query. for context, one of the things i am building is a route mapping tool for people to customise their journey from place to place.

i have another question. while attempting to simplify my experiment and deploy the website, somehow the agent adds extra steps and made it more complicated to test/deploy, and then it turns into a cycle of me telling it to simplify the process, with varying success. how do i break out of this feedback loop?

# Claude

Here's a draft in your voice. I've kept it to one main point, with a couple of concrete things to try.

---

Hi [name],

The route mapping tool sounds fun. Hope you'll show it when it's up.

On the loop: I think "simplify" is the problem. It's a vague instruction. The agent doesn't know what simple means to you, so it guesses, and each guess adds a step you then have to argue against. You're negotiating with it, and it's a patient negotiator.

What tends to work better for me is to stop asking it to simplify and instead tell it exactly what the end state looks like. Something like: "The deploy is one command. There is one HTML file and one JS file. No build step, no Docker, no CI. If you think something else is needed, ask me before adding it." Now there's a target it can check itself against, and you can check too.

Two other things, maybe.

**Start a fresh session.** After a few rounds of "no, simpler", the conversation is full of the complicated version and your objections to it. The agent keeps re-reading all that. A new chat with only the constraints above, and none of the history, often just... works.

**Ask it to delete, not simplify.** "Remove the Dockerfile. Remove the test runner config. Remove anything not needed to serve index.html." Deleting is a concrete action. Simplifying is a judgment call, and the agent's judgment is what got you here.

If you use an agent that reads a project file (CLAUDE.md, AGENTS.md, etc.), put the constraints there. Then you don't have to repeat yourself every session, which is where the loop starts.

I'd be curious whether the fresh session or the delete list makes the bigger difference. Let me know?

Anand

---

One thing to consider: if you have a personal example of this happening to you (a deploy that ballooned, a session you restarted), dropping it in before "What tends to work" would make it more you. I didn't invent one.

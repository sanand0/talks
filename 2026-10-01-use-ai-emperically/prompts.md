# Prompt

## Initial Story, 01 Oct 2026

<!--
cd ~/code/talks/
dev.sh -- claude --dangerously-skip-permissions --model sonnet --effort high
-->

<!-- Source: https://chatgpt.com/c/6abdef35-b19c-83ec-83aa-6707087f9e4c -->

Create a narrative story for the talk at 2026-10-01-use-ai-emperically/, using the talk-story skill.

This was Anand's ~90-minute remote session for **[DBS Technology India](https://www.dbs.com/dbstechindia/), TechVerse Session 4: Agentic AI**, on 1 Oct 2026. The organizer's circulated title was **“Effective use of Gen AI for personal and professional productivity”**, with a more specific description: how to (and how not to) use agents effectively when writing software. Anand reduced it to one message at the start: **“use AI in an empirical way.”**

The page should feel like the talk: browser-driven experiments, audience questions in Webex chat, live detours, and discussion — not a conventional slide-deck recap.

Use the material in the directory thoughtfully:

- **transcript.md** is the source of truth for what happened, the sequence, and all verbatim quotes.
- **story-context.md** contains event/audience context, the narrative arc hidden in the transcript, the strongest scenes and quotes, benchmark caveats, and a source/asset map. Treat it as guidance, not a required outline.
- **links.md** is the list of pages used live. Honor its EMBED / LINK / INCLUDE guidance. Every listed public URL should appear somewhere appropriate.
- **chat-agent-log-analysis.md** is the deeper evidence behind the team-log section. Use it to make the “coding got fast; verification did not” section concrete, but don't leak its private ChatGPT URL.
- **chat-jev-benchmark.md** shows how the Jev benchmark was researched, costed, run, interpreted, and turned into a page. It is useful evidence for the meta-point that **benchmarking itself is delegatable to agents**. Use only its public/share URL from links.md, never the private chat URL in frontmatter/comments.
- **comic-page.avif** should be prominent near the top.
- **2026-10-01-use-ai-emperically.opus** is the talk recording; include audio using the usual public talks-release URL convention.

The strongest story is NOT “here are the demos Anand showed.” It is a discovery arc:

1. Plausible AI advice is now cheap to **test**.
2. Generic benchmarks are useful, but your own tasks and logs can become better **personal benchmarks**.
3. Agent logs are a lab notebook: they reveal what users and tools actually do, not what they think they do.
4. Faster generation creates a verification bottleneck; **verification must become part of the workflow**.

A particularly good opening scene is the pre-talk exchange where Venky says image generation keeps giving bald men the same hairstyle, and Anand immediately asks what worked, what failed, and starts imagining a benchmark. It embodies the thesis before the formal talk even starts.

A particularly good ending is the transcript's own ending: prompting advice, models and agents are all hypotheses; logs are diagnostic data; tests/double-checking/calibration belong inside the workflow; **“let's test.”**

Preserve the humor where it helps — especially the deliberately cynical developer anti-patterns around 62–65 minutes — but make the pivot explicit: the joke works because AI can generate output faster than organizations can verify and own it.

Prefer the audience's questions and observations when they sharpen the story. Venky's challenge around comparing agents/harnesses leads to the useful **specification → verification → execution** framework. Uttam's “ask the agents to do test-driven development” neatly reinforces the team-log finding.

For benchmark numbers and technical claims, use the local source files listed in story-context.md to cross-check transcript shorthand. Do not universalize results from one benchmark/task. Date fast-changing model/pricing claims to the talk rather than presenting them as timeless facts.

Search/link additional public context when it genuinely enhances the reading experience, as the talk-story skill prescribes. Do not expose internal DBS links, internal email content, or private ChatGPT/Claude browser URLs.

<!-- Comic page: https://chatgpt.com/c/6abe6599-dcb4-83ec-a352-aee6a03ef7e0 -->

---

Use these images for my photo: https://www.s-anand.net/blog/assets/Anand-5a-1.webp
which Venky modified into: 2026-10-01-use-ai-emperically/session-invite.avif

Check color contrast on all elements. The prompt text "What am I repeatedly..." is almost invisible on the background.
Run any other relevant accessibility checks.

--- <!-- steering -->

Replace Shri/Shree/Shri with Sree. Standardize spelling variations to Vishnu Kiran, Venkateswarlu. Everywhere, including in the transcript.

<!-- claude --resume 64c409d8-5919-4244-9dc5-a76007c88c98 --dangerously-skip-permissions -->

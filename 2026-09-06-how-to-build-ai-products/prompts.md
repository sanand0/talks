# Prompts

## Story, 3 Aug 2026

<!--
cd ~/code/talks/
dev.sh -p ~/Documents/data:ro,~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model sonnet --effort medium
-->

Create a narrative story for the talk at 2026-09-06-how-to-build-ai-products/

Go through the prompts.md in other recent files in this repo - you'll understand what I want. Implement along similar lines.

But there's one important change here. This will be a 5-day talk series. I'd like you to create an `index.html` that provides an overview (which we may update over time - keep it simple for now) and link to `day1.html`, `day2.html`, ...

As of now, just Day 1 is complete, so create `day1.html` and link to it from `index.html`. The other days can be placeholders for now.

The audience include Japanese speaking students. So we will create a Japanese version of each file, too, as `index.ja.html`, `day1.ja.html`, etc. For now, just create the English version and create placeholders for the Japanese versions. We will create those later.

Feel free to use sub-agents as required, e.g. Opus for complex tasks or judgement (planning, analysis, storyline, etc.) and Haiku for simple execution.

---

You can now access files under: ~/Documents/data/forms/sutd-ai-products/ as well as ~/code/ and ~/r2/ - incorporate content from here as required.

Revisions:

- Include links to other responses / submissions - including from emails via `gws` to askai@s-anand.net (on root.node@gmail.com account).
- Attribute the Strata Japan link (in transcript and page) to Takayuki Shuku - the TCU professor.
- Allow jumping to any scene from anywhere on the page.
- EMBED: comic-page-day-1.avif
- EMBED: [Simple writing hurts thinking](https://www.s-anand.net/blog/simple-writing-hurts-thinking/)

There are some monotonous long blocks of text. Break the monotony visually.

Search online for relevant references and include more links.

---

I've added the links submitted by students to ~/Documents/data/forms/sutd-ai-products/responses.tsv against the question "simple_app_link". Use those instead.

---

The epilog has a problem. Take a look at the cards - at least one (maybe more) of the cards isn't formatted properly. Lentera Bursa, in particular.

---

`day1.ja.md` has the Japanese translation of day1.html. Use this wisely to create day1.ja.html. Then delete day1.ja.md.

<!-- claude --resume 5c050392-5806-402d-920f-0cf0c712ec0b --dangerously-skip-permissions -->
<!-- Comic page: https://chatgpt.com/c/6a9e6332-361c-83ec-b48b-422641b246b6 -->

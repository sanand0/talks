# Prompts

## Day 2, 8 Sep 2026

<!--
cd ~/code/talks/
dev.sh -p ~/Documents/data:ro,~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model sonnet --effort medium
-->

Update the narrative story at 2026-09-06-how-to-build-ai-products/ to include day 2 content from transcript-day-2.md and comic-page-day-2.avif.

Read the prompts.md and other related files for context. Follow the same structure and instructions / style as for Day 1.

Do not create day2.ja.html yet - I'll provide a translation AFTER you create day2.html. But you can update other files (e.g. if index.html needs changes, etc.)

---

Embed (or link, if embedding doesn't work) their websites where possible. Find the links from the responses.tsv.

`day2.ja.md` has the Japanese translation of day2.html. Use this wisely to create day2.ja.html. Then delete day2.ja.md.

<!-- claude --resume 0ced6de6-b0f2-4725-bc05-7f961b7c39c1 --dangerously-skip-permissions -->
<!--
Comic page: https://chatgpt.com/c/6a9f778d-de68-83ec-a74f-5fd6cf5f31a7
Manga page: https://chatgpt.com/c/6a9f7905-1da0-83ec-bbc1-acec0c5f12b2
Manga page v2 (unused): https://chatgpt.com/c/6a9f79fc-d0e4-83ec-b840-504d3e46d240
-->

## Day 1, 7 Sep 2026

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
<!--
Comic page: https://chatgpt.com/c/6a9e6332-361c-83ec-b48b-422641b246b6
Manga page: https://chatgpt.com/c/6a9e70bb-7d14-83ec-a5ef-35e9d0b3d60f
-->

# Prompts

## Corrections, 12 Sep 2026

<!--
cd ~/code/talks/2026-09-06-how-to-build-ai-products/
dev.sh -p ~/Documents/data:ro,~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model sonnet --effort medium
-->

I plan to move the submissions/ page elsewhere. So copy from submissions/ that are used in this directory to ./ and re-reference those in the HTML files.

<!-- claude --resume 5d32e82d-7ef5-4461-9ef5-9a9be8e1cf9d --dangerously-skip-permissions -->

## Day 5, 12 Sep 2026

<!--
cd ~/code/talks/
dev.sh -p ~/Documents/data:ro,~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model sonnet --effort medium
-->

Update the narrative story at 2026-09-06-how-to-build-ai-products/ to include day 5 content from transcript-day-5.md and comic-page-day-5.avif.
Read the prompts.md and other related files for context.
Follow the same structure and instructions / style as for past days and avoid mistakes that required me to correct you.

Read ~/r2/private/straivex-methodology/ as context for the StraiveX methodology but do not reproduce the slide or any sensitive material.
Weave in content from chat-day5.md. It has multiple chats used during the day. Show individual chats, formatted as HTML in a popup, linked from the main narrative.
Also weave in submissions/evaluation-prompt-original.md which was revised using submissions/evaluation-prompt-feedback.csv (see chat-day5.md for details) into evaluation-prompt.md.
Include the above files (show them, formatted, in a popup; incorporate content into the narrative) but do not incorporate any actual evaluations based on these.
Include any other relevant links or stats from https://docs.google.com/spreadsheets/d/1069Qs1tt_fuSDJryagebnFLIyG-KqRoni-nyLYml4pc/edit
Embed (and link to) the pages the students presented.

Do not create day5.ja.html yet - I'll provide a translation AFTER you create day5.html. But you can update other files (e.g. if index.html needs changes, etc.)

---

Place the StraiveX cards in a single line when possible.
Break the flow of long blocks of text in the first half using more .band blocks in the first half.
Link to and weave in my [reframe-question](https://github.com/sanand0/blog/blob/main/pages/skills/reframe-question/SKILL.md) skill under "A meta-prompt from everyone's chats".

Fix these AND SIMILAR ERRORS:
- On hover, .doclink text has poor contrast and is almost unreadable.
- Clicking the .doclink "Open the original chat" does not open the link.
- The popup showing the raw feedback CSV doesn't look good because the "Suggestion" column which has the bulk of the text is squeezed at the end and takes up too many rows.

---

Make the StraiveX methodology a .band that can take up the full width.
Strike-throughs on "False victories the rubric explicitly rejects" make it hard to read.

---

`day5.ja.md` has the Japanese translation of day5.html. Use this wisely to create day5.ja.html - using the Japanese script and comic. Then delete day5.ja.md.

---

Update 2026-09-06-how-to-build-ai-products/{index.html,index.ja.html} based on the overall content of the 5-day talk series.
Not too much - maybe just correct what's required, improve the flow to reflect reality, and end with a short takeaway.

<!-- claude --resume 4e7667ad-3563-400c-9e39-ae38a5b3f908 --dangerously-skip-permissions -->
<!--
Comic page: https://chatgpt.com/c/6aa50c4c-e45c-83ec-b098-45f91a9502b2
Manga page: https://chatgpt.com/c/6aa50fa4-44d8-83ec-8709-17e03f7f5a52
-->

## Day 4, 10 Sep 2026

<!--
cd ~/code/talks/
dev.sh -p ~/Documents/data:ro,~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model sonnet --effort medium
-->

Update the narrative story at 2026-09-06-how-to-build-ai-products/ to include day 4 content from transcript-day-4.md and comic-page-day-4.avif.
Include links from links-day-4.md as mentioned.
Include any other relevant links or stats from https://docs.google.com/spreadsheets/d/1069Qs1tt_fuSDJryagebnFLIyG-KqRoni-nyLYml4pc/edit

Read the prompts.md and other related files for context.
Follow the same structure and instructions / style as for past days and avoid mistakes that required me to correct you.

Do not create day4.ja.html yet - I'll provide a translation AFTER you create day4.html. But you can update other files (e.g. if index.html needs changes, etc.)

---

`day4.ja.md` has the Japanese translation of day4.html. Use this wisely to create day4.ja.html - using the Japanese script and comic. Then delete day4.ja.md.

<!-- claude --resume d782aef8-b169-4db1-8e85-aa2cdaf9507c --dangerously-skip-permissions -->
<!--
Comic page: https://chatgpt.com/c/6aa21d11-3590-83ec-a50f-5025abf79694
Manga page: https://chatgpt.com/c/6aa21dc0-ed88-83ec-a72a-4d2e86aabee5
-->

## Day 3, 9 Sep 2026

<!--
cd ~/code/talks/
dev.sh -p ~/Documents/data:ro,~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model sonnet --effort medium
-->

Update the narrative story at 2026-09-06-how-to-build-ai-products/ to include day 3 content from transcript-day-3.md and comic-page-day-3.avif.
Include links from links-day-3.md as mentioned.

Read the prompts.md and other related files for context. Follow the same structure and instructions / style as for Day 1.

Do not create day3.ja.html yet - I'll provide a translation AFTER you create day3.html. But you can update other files (e.g. if index.html needs changes, etc.)

---

The underlining inside `a.shot-link` doesn't look good.
Break the monotony of long blocks: EMBED these sites:

- [City, By You](https://city-by-you-mayusuzuki-20260908.mayu-s-feb-27.chatgpt.site/) - If you could build a city, what kind of city would you create?. Tell us a little about you, then make eight small decisions. We will turn them into your own corner of the world.
- [Study Walker](https://yuriciv.github.io/study-walker/)
- Embed test-automation-codex/playwright-report/index.html

... and find other ways to break the monotony of long blocks of text. Rendered blocks (maybe with different widths / colors / ... - like `.band`) from the market research, test cases, etc. might help.

Across all three days, include the audio files at https://github.com/sanand0/talks/releases/download/talks/2026-09-07-how-to-build-ai-products-day-{1,2,3}.opus similar to how audio files are included in other talks.

---

`day3.ja.md` has the Japanese translation of day3.html. Use this wisely to create day3.ja.html. Then delete day3.ja.md.

---

`day3.html` doesn't have the `.masthead-date` link to `day3.ja.html` yet.
This indicates that there may be other bugs and inconsistencies. Investigate carefully and fix them.

<!-- claude --resume ff6c07a0-b3b6-4fd0-b9fb-667c939855d1 --dangerously-skip-permissions -->
<!--
Comic page: https://chatgpt.com/c/6aa0ecbd-1e5c-83ec-a6c8-fa66367a03ad
Manga page: https://chatgpt.com/c/6aa0ee70-8908-83ec-b902-30d9af2dcc38
-->

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

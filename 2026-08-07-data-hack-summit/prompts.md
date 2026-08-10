# Prompts

<!-- Prep links:

- DHS Talk Prep for Specification: https://chatgpt.com/c/6a73eed7-e64c-83ec-a7a5-a408a74f80fc
- DHS Talk AI Verification Mechanisms: https://chatgpt.com/c/6a749238-3418-83ec-b156-693eb2d5bda3
- DHS Talk FDE skills for AI-era software development: https://claude.ai/chat/547157bc-cdb8-4e9f-9b06-d8c938ce6041

-->

## Revision, 07 Aug 2026

<!--
cd ~/code/talks/
dev.sh -p ~/Documents/forms:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Update 2026-08-07-data-hack-summit/index.html.

Read prompt.md for context. I think people who said they run tests on AI output (in the survey) find errors about twice as often as people who spot-check it. Analyze, verify, and incorporate.

## Initial draft, 07 Aug 2026

<!--
cd ~/code/talks/
dev.sh -p ~/Documents/forms:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Generate a beautiful narrative story as a single-page HTML at 2026-08-07-data-hack-summit/index.html about this 1-hour AI Workshop [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted at [Data Hack Summit 2026](https://www.analyticsvidhya.com/datahacksummit-2026/#agenda) on 7 Aug 2026 at Bangalore.

Use the following as examples to follow LOOSELY, not strictly:

- 2026-07-04-vizchitra-dialog-curators-dilemma/index.html
- 2026-07-07-when-data-is-for-agents-fifth-elephant/index.html
- 2026-07-25-ai-unboxed-agentic-analysis/index.html

Sources:

- 2026-08-07-data-hack-summit/transcript.md - Use the talk transcript and the main content source.
- 2026-08-07-data-hack-summit/links.md - Read links in links.md and weave them into the narrative.
- ~/Documents/forms/dhs2026/ - Read the questions, analyze the answers, share insights in the narrative.
  - form.yaml: Form used to collect responses from participants.
  - responses.tsv: Responses collected from participants.

Based on your reading, think about the most useful narrative to craft, and the most engaging way to present it.

Prominently include these:

- embed the video near the top: `<video controls preload="metadata" width="100%"><source src="https://media.s-anand.net/2026-08-07-data-hack-summit.webm" type='video/webm; codecs="vp9, opus"'></video>` in a full width container.
- link to the transcript near the top - clicking it should open in a popup and render as HTML.
- embed the audio near the top: https://github.com/sanand0/talks/releases/download/talks/2026-08-07-data-hack-summit.opus
- include this visual summary at an appropriate place: `2026-08-07-data-hack-summit/comic-page.avif` - clicking on it should open the full-size image in a new tab

Include links from the sources at the appropriate places (as links, embeds, or copying content from the links as appropriate).
Search online & research material that will improve the reading experience and include these as well.

Here's how to include the links from the transcript:

- Make sure ALL links from the Markdown files are included inline the relevant points in the narrative, captions, cards, etc.
- Where links are chats, also read chat contents and include relevant snippets to enhance the narrative.
- Prefer links, not buttons, when adding click event handlers to linkable content. That way, right-clicking to open in a new tab works.
- Where images are present, include them - along with a caption. The image and caption should link to the associated link (if present), else open the image in a new tab.

Style:

- Weave in plenty of memorable, funny, or insightful quotes from the transcript/responses. Make these blockquotes stand out.
- Highlight what was insightful or funny.
- Make the story more scannable by using **bold** to highlight the key points in the flow.
- Make sure the design is engaging. Allow visual elements (e.g. comic page, videos, embedded content, etc.) to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc.
- Ensure that bands (e.g. .stat-band, .gallery-band, and any other similar full-width bands) have a bottom margin to create more breathing room between sections.
- Add the top maybe 6 takeways from the talk at the end, rendered as cards.

This will be deployed at https://sanand0.github.io/talks/2026-08-07-data-hack-summit/

Update README.md to include this talk in the list of talks.

---

Revisions:

- https://files.s-anand.net/pages/ai-jagged-edge/ is embedded via an IFRAME. Instead, just copy from the file and insert it here.
- Same for https://files.s-anand.net/pages/ai-jagged-edge/
- Include a navigation mechanism to jump to any of the 5 specification or 5 verification sections - or the sections above or below - from anywhere on the page.
- Link to https://contractanalysis.straivedemo.com/ instead of embedding
- The .cards currently only allow 4 columns at most. For wide enough screens, allow 5 columns.
- The embeds and the videos can take up more width.

<!-- claude --resume 7d79827f-05eb-4ae9-8997-aa9dcc046364 --dangerously-skip-permissions -->

## Comic Page

<!--
GPT Image 2 - https://chatgpt.com/c/6a75ae8e-62f0-83ec-b04b-796227835a0c
-->

Draw this as a full-color explainer comic page (portrait) - sequential explanation, friendly narrator, diagrams embedded inside panels, visual metaphors, self-aware captions, and clear cause-and-effect storytelling.
Style: expressive characters, comic-style ALL CAPS, vibrant modern colors, clear visual hierarchy.
Prefer pictures over words. Use recurring visual metaphors so the reader understands the idea even while skimming.

First, write a memorable storyline that captures the most important points to convey.
Just reading the storyline should communicate the entire message unambiguously.
Draw each storyline element (typically a sentence, but sometimes a continued phrase, or multiple sentences) as a panel's caption. (If there are 8 panels, there must be 8 storyline elements)
Each panel's image should support and strengthen its caption - and reinforcing past panels / anticipating future panels where helpful.

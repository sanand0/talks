# Prompts

<!--
cd ~/code/talks/
dev.sh -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Generate a beautiful narrative story as a single-page HTML at 2026-07-25-ai-unboxed-agentic-analysis/index.html about this 2-hour AI Workshop [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted for the [IIM Alumni in Singapore](https://iimalumni.sg/) on 25 July 2026 as part of the "AI Unboxed" series. This is the third of four workshops and the topic was "Agentic Analysis". The workshop was held online via Microsoft Teams. (Details of the first workshop are at 2026-05-23-ai-unboxed-context-engineering/ and the second at 2026-06-20-ai-unboxed-tools-workflows/)

Use the following as examples to follow LOOSELY, not strictly:

- 2026-05-23-ai-unboxed-context-engineering/index.html
- 2026-06-20-ai-unboxed-tools-workflows/index.html
- 2026-07-07-when-data-is-for-agents-fifth-elephant/index.html

Sources:

- Use the talk transcript and the main content source. It's at 2026-07-25-ai-unboxed-agentic-analysis/transcript.md.
- Read all links in links.md, chat messages in messages.md, and the AI conversations (saved as chats/\*.md) as additional sources to find relevant content to weave into the narrative.

Based on your reading, think about the most useful narrative to craft, and the most engaging way to present it.

Prominently include these:

- embed the video near the top: `<video controls preload="metadata" width="100%"><source src="https://media.s-anand.net/2026-07-25-ai-unboxed-agentic-analysis.webm" type='video/webm; codecs="vp9, opus"'></video>` in a full width container.
- link to the transcript near the top - clicking it should open in a popup and render as HTML.
- embed the audio near the top: https://github.com/sanand0/talks/releases/download/talks/2026-07-25-ai-unboxed-agentic-analysis.opus
- include the invitation poster at an appropriate place: `https://files.s-anand.net/images/2026-07-25-ai-unboxed-agentic-analysis-poster.avif` - clicking on it should open the full-size image in a new tab
- include this visual summary at an appropriate place: `2026-07-25-ai-unboxed-agentic-analysis/comic-page.avif` - clicking on it should open the full-size image in a new tab

Include links from the transcript / chats / responses at the appropriate places.
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

This will be deployed at https://sanand0.github.io/talks/2026-07-25-ai-unboxed-agentic-analysis/

Update README.md to include this talk in the list of talks.

---

Include a link to Anand's weather data story: https://sanand0.github.io/datastories/rainy-seasons/

<!-- claude --resume --dangerously-skip-permissions -->

## Comic Page

<!--
GPT Image 2 - https://chatgpt.com/c/6a707c2a-0104-83ec-b2ce-1677defed0bb
-->

Draw this as a full-color explainer comic page (portrait) - sequential explanation, friendly narrator, diagrams embedded inside panels, visual metaphors, self-aware captions, and clear cause-and-effect storytelling.
Style: expressive characters, comic-style ALL CAPS, vibrant modern colors, clear visual hierarchy.
Prefer pictures over words. Use recurring visual metaphors so the reader understands the idea even while skimming.

First, write a memorable storyline that captures the most important points to convey.
Just reading the storyline should communicate the entire message unambiguously.
Draw each storyline element (typically a sentence, but sometimes a continued phrase, or multiple sentences) as a panel's caption. (If there are 8 panels, there must be 8 storyline elements)
Each panel's image should support and strengthen its caption - and reinforcing past panels / anticipating future panels where helpful.

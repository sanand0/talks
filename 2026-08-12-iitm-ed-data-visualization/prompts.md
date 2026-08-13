# Prompts

## Initial draft, 13 Aug 2026

<!--
cd ~/code/talks/
dev.sh -p ~/code:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Generate a beautiful narrative story as a single-page HTML at 2026-08-12-iitm-ed-data-visualization/index.html about this 1-hour class [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted at IIT Madras for students of ED5518: Data Visualization for Engineers by Dr Palaniappan Ramu on 12 Aug 2026.

Use the following as examples to follow LOOSELY, not strictly:

- 2026-07-04-vizchitra-dialog-curators-dilemma/index.html
- 2026-08-07-data-hack-summit/index.html
- 2026-08-10-tds-ama/index.html

Sources:

- 2026-08-12-iitm-ed-data-visualization/transcript.md - Use the talk transcript and the main content source.
- 2026-08-12-iitm-ed-data-visualization/links.md - Read links and content in links.md and weave them into the narrative as indicated.

Based on your reading, think about the most useful narrative to craft, and the most engaging way to present it.

Prominently include these:

- link to the transcript near the top - clicking it should open in a popup and render as HTML.
- embed the audio near the top: https://github.com/sanand0/talks/releases/download/talks/2026-08-12-iitm-ed-data-visualization.opus.
- include this visual summary at an appropriate place: `2026-08-12-iitm-ed-data-visualization/comic-page.avif` - clicking on it should open the full-size image in a new tab. <!-- https://chatgpt.com/c/6a7d323f-1648-83e8-ae24-b4b111c2a1ea -->

Include links from the sources at the appropriate places (as links, embeds, or copying content from the links as appropriate).
Search online & research material that will improve the reading experience and include these as well.

Style:

- Weave in plenty of memorable, funny, or insightful quotes from the transcript/responses. Make these blockquotes stand out.
- Highlight what was insightful or funny.
- Make the story more scannable by using **bold** to highlight the key points in the flow.
- Include a navigation mechanism to jump to any section from anywhere on the page.
- Make sure the design is engaging. Allow visual elements (e.g. comic page, videos, embedded content, etc.) to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc.
- Ensure that bands (e.g. .stat-band, .gallery-band, and any other similar full-width bands) have a bottom margin to create more breathing room between sections.
- Verify that ALL elements have sufficient color contrast for accessibility.
- Fit cards in one row on large screens, where possible. For example, if there are 4 or 5 cards, keep them in 1 row rather than just an extra row with 1 card. Or, up to 1 extra card (if appropriate) to fill the additional row.
- Add the top maybe 6 takeways from the talk at the end, rendered as cards.

This will be deployed at https://sanand0.github.io/talks/2026-08-12-iitm-ed-data-visualization/

Update README.md to include this talk in the list of talks.

<!-- claude --resume 77df5334-3122-4bb5-a603-7beed263e1ed --dangerously-skip-permissions -->

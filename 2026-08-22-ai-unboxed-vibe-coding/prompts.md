# Prompts

## Initial draft, 26 Aug 2026

<!--
cd ~/code/talks/
dev.sh -p ~/Documents/data/forms:ro,~/Music:ro,~/code:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Generate a beautiful narrative story as a single-page HTML at 2026-08-22-ai-unboxed-vibe-coding/index.html about this 2-hour AI Workshop [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted for the [IIM Alumni in Singapore](https://iimalumni.sg/) on 22 Aug 2026 as part of the "AI Unboxed" series. This is the fourth of four workshops and the topic was "Vibe Coding". The workshop was held online via Microsoft Teams as well as in-person. (Details of the first workshop are at 2026-05-23-ai-unboxed-context-engineering/ and the second at 2026-06-20-ai-unboxed-tools-workflows/ ad the third at 2026-07-25-ai-unboxed-agentic-analysis/)

Use the following as examples to follow LOOSELY, not strictly:

- 2026-07-25-ai-unboxed-agentic-analysis/
- 2026-07-04-vizchitra-dialog-curators-dilemma/index.html
- 2026-08-10-tds-ama/index.html

Sources:

- 2026-08-22-ai-unboxed-vibe-coding/transcript.md - Use the talk transcript and the main content source.
- 2026-08-22-ai-unboxed-vibe-coding/links.md - Read links and content in links.md and weave them into the narrative as indicated.
- 2026-08-22-ai-unboxed-vibe-coding/chat-*.md - Exports of ChatGPT / Claude transcripts
- ~/Documents/data/forms/aiunboxed4/ - Read the questions, analyze the answers, share insights in the narrative.
  - form.yaml: Form used to collect responses from participants.
  - responses.tsv: Responses collected from participants.

Based on your reading, think about the most useful narrative to craft, and the most engaging way to present it.

Prominently include these:

- embed the video near the top: `<video controls preload="metadata" width="100%"><source src="https://media.s-anand.net/2026-08-22-ai-unboxed-4-vibe-coding.webm" type='video/webm; codecs="vp9, opus"'></video>` in a full width container.
- link to the transcript near the top - clicking it should open in a popup and render as HTML.
- embed the audio near the top: https://github.com/sanand0/talks/releases/download/talks/2026-08-22-ai-unboxed-vibe-coding.opus.
- include this visual summary at an appropriate place: `2026-08-22-ai-unboxed-vibe-coding/comic-page.avif` - clicking on it should open the full-size image in a new tab. <!-- https://chatgpt.com/c/6a8ef8e6-7e4c-83ec-8445-6843197b2aa3 -->

Include links from the sources at the appropriate places (as links, embeds, or copying content from the links as appropriate).
Search online & research material that will improve the reading experience and include these as well.

Here's how to include the links from the transcript:

- Make sure ALL links from the Markdown files are included inline the relevant points in the narrative, captions, cards, etc.
- Where links are chats, also read chat contents and include relevant snippets to enhance the narrative.
- Embed response.tsv fragments as required.
- Prefer links, not buttons, when adding click event handlers to linkable content. That way, right-clicking to open in a new tab works.
- Where images are present, include them - along with a caption. The image and caption should link to the associated link (if present), else open the image in a new tab.

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

This will be deployed at https://talks.s-anand.net/2026-08-22-ai-unboxed-vibe-coding/

Update README.md to include this talk in the list of talks.

---

Consider embedding https://files.s-anand.net/cv/S_Anand_2024.pdf (and/or https://files.s-anand.net/cv/S_Anand_2024_semantic.html) instead of cv-2024.webp. Try avoiding the vertical scroll on both CVs.
Show form responses as charts where appropriate.
Link to all movies on IMDb. Link to more sources where appropriate, e.g. https://indiankanoon.org/doc/188730914/ for the Karnataka High Court judgement, etc.
Note that the video on this page is AV1 compressed. A 900MB video was compressed to 130MB - that's over 2 hours of video.
If you want to use something from ~/Music/musicdump.csv (generated by musictag.py) - e.g. stats, charts, etc. feel free.

<!-- claude --resume b5b11ed5-927a-49fa-853a-c5fdff99d960 --dangerously-skip-permissions -->

# Prompts

<!--

cd ~/code/talks/
dev.sh
claude --dangerously-skip-permissions

-->

Generate a beautiful narrative story about this 2-hour AI Workshop [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted for the [IIM Alumni in Singapore](https://iimalumni.sg/) on 23 May 2026 as part of the "AI Unboxed" series. This is the first of four workshops and the topic was "Context Engineering". The workshop was held online via Microsoft Teams.

Generate a beautiful narrative story about this workshop as 2026-05-23-ai-unboxed-context-engineering/index.html.

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use the following as examples to follow LOOSELY, not strictly:

- 2026-04-30-harvard-education/index.html
- 2026-04-08-ai-workshop-lbsnaa/index.html
- 2026-04-06-innovation-as-a-frontier-straive/index.html

Use the talk transcript and the main content source. It's at 2026-05-23-ai-unboxed-context-engineering/transcript.md.
You may also read the chat transcripts in chats/ to find relevant content to weave into the narrative.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.

Make sure the design is engaging. Allow visual elements (e.g. comic page, videos, embedded content, etc.) to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc.

Add the top takeways from the talk at the end.

Prominently include these:

- embed the video near the top: `<video controls preload="metadata" width="100%"><source src="https://media.s-anand.net/2026-05-23-iim-ai-unboxed-context-engineering.webm" type='video/webm; codecs="vp9, opus"'></video>` in a full width container.
- link to the transcript near the top - it should open in a popup and render as HTML.
- embed the audio near the top: https://github.com/sanand0/talks/releases/download/talks/2026-05-23-ai-unboxed-context-engineering.opus
- include the comic page at an appropriate place: `2026-05-23-ai-unboxed-context-engineering/comic-page.avif` - clicking on it should open the full-size image in a new tab
- include the screenshot of the Teams background design `teams-backgrounds.avif` near the section where I talk about it, with a caption. Clicking on the image or caption should open the full-size image in a new tab.

Here's how to include the links from the transcript:

- Make sure ALL links from the transcript are included inline the relevant points in the narrative, captions, cards, etc.
- Where links are chats, also read chat transcripts from chats/ and include relevant snippets to enhance the narrative.
- Where images are present, include them - along with a caption. The image and caption should link to the associated link (if present), else open the image in a new tab.
- Embed https://sanand0.github.io/llmpricing/ as an IFRAME in a full-width container, with a caption linking to the source.

Search online and LIBERALLY add inline link to material relevant to the narrative - that are mentioned (directly or indirectly) in the workshop, as well as any material that can provide useful context to the reader.

Feel free to add tooltips and popups as informative and engaging aids.

- **Tooltips** are for: Context about non-obvious terms or phrases (only if relevant and useful); Additional context about references (where possible)
- **Popups** are for: Citations: Search for and include references; Cite the key point from the reference and link to it. Supporting material: Provide extensive context, quotes, external references, etc.

This will be deployed at https://sanand0.github.io/talks/2026-05-23-ai-unboxed-context-engineering/

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, break this into parts, generating the .html in chunks or layered edits (keeping each chunk small) and saving it, checking it, then updating it with the next iteration, and so on.

Update README.md to include this talk in the list of talks.

---

Corrections:

- The video is at https://media.s-anand.net/2026-05-23-ai-unboxed-context-engineering.webm
- FYI: the .quick-links buttons vs links look different. But don't bother with that. Instead, make all the transcript buttons into links (so right-clicking to open in a new tab works) and intercept the click to open the popup.
- Link to the AI scrapers tool at https://tools.s-anand.net/aiscrapers/
- Link to https://www.s-anand.net/blog/prompts/ which is a published version of the prompts at https://github.com/sanand0/blog/blob/live/pages/prompts/
- Link to this InsureLE demo: https://mynkpdr.github.io/insurle-demo/ (instead of https://insureli.com/) as well as the research publication: https://www.researchgate.net/publication/388354297_Computable_Contracts_for_Insurance_Establishing_an_Insurance-Specific_Controlled_Natural_Language_-_InsurLE
- Rajan is actually spelt Rajen

Also:

- Make the content more scannable by using a little more **bold** to highlight the key points in the flow.
- Find more opportunities to link to content, augment with external material and references, and enrich the content.

<!-- claude --resume 9081eb6d-10e5-4781-9198-289c7e19b5da --dangerously-skip-permissions -->

## Comic Page

<!--
GPT Image 2 - https://chatgpt.com/c/6a11a7ba-fa14-83ec-a29c-ec5eb6f632f7
-->

Draw this as a full-color explainer comic page (portrait) - sequential explanation, friendly narrator, diagrams embedded inside panels, visual metaphors, self-aware captions, and clear cause-and-effect storytelling. Style: expressive characters, comic-style ALL CAPS, vibrant modern colors, clear visual hierarchy. Prefer pictures over words. Use recurring visual metaphors so the reader understands the idea even while skimming. Think about the most important points, structure it as a memorable story.

# Prompts

<!--
cd ~/code/talks/
dev.sh -p ~/code/
claude --dangerously-skip-permissions
-->

Generate a beautiful narrative story as a single-page HTML at 2026-06-20-ai-unboxed-tools-workflows/index.html about this 2-hour AI Workshop [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted for the [IIM Alumni in Singapore](https://iimalumni.sg/) on 20 June 2026 as part of the "AI Unboxed" series. This is the second of four workshops and the topic was "Tools and Workflows". The workshop was held online via Microsoft Teams. (Details of the first workshop are at 2026-05-23-ai-unboxed-context-engineering/)

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use the following as examples to follow LOOSELY, not strictly:

- 2026-05-23-ai-unboxed-context-engineering/index.html
- 2026-06-16-eqt-data-stack-for-agents/index.html
- 2026-06-13-data-stories-with-ai/index.html

Sources:

- Use the talk transcript and the main content source. It's at 2026-06-20-ai-unboxed-tools-workflows/transcript.md.
- Read the AI Studio prompts and responses in 2026-06-20-ai-unboxed-tools-workflows/google-ai-studio-transcripts.md to find relevant content to weave into the narrative.
- Read all links in the transcript (e.g. GitHub - converted to raw links as required - or read from ~/code/, Blog posts, etc.) to find relevant content to weave into the narrative.
- Read other Markdown files in 2026-06-20-ai-unboxed-tools-workflows/ (e.g. chat transcripts, AI output, etc.) and weave them into the narrative as relevant.
- DO NOT LINK to, but mention, `forms.s-anand.net/aistories/` as the form I used to collect responses. The link will only work when I enable it - and I disabled it after the exam.
- The questions/responses from the survey are at `~/code/liveform/forms/aistories/{form.yaml,responses.tsv}` - analyze these for relevant insights and include them in the narrative (but do not link to the files directly).
- Search online and LIBERALLY add inline link to material relevant to the narrative - that are mentioned in the workshop (e.g. tools, websites, services, concepts, how-to, help documentation, ...), as well as any related material that can provide useful context to the reader (authoritative/expert opinions or research papers for/against the topic). Find opportunities to link to content, augment with external material and references, and enrich the content.

Style:

- Weave in plenty of memorable, funny, or insightful quotes from the transcript/responses. Make these blockquotes stand out.
- Highlight what was insightful or funny.
- Make the story more scannable by using **bold** to highlight the key points in the flow.
- Make sure the design is engaging. Allow visual elements (e.g. comic page, videos, embedded content, etc.) to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc.
- Add the top maybe 6 takeways from the talk at the end.

Prominently include these:

- embed the video near the top: https://youtu.be/H3GmGl1hzxM - in a full width container.
- link to the transcript near the top - clicking it should open in a popup and render as HTML.
- embed the audio near the top: https://github.com/sanand0/talks/releases/download/talks/2026-06-20-ai-unboxed-tools-workflows.opus
- include the comic page at an appropriate place: `2026-06-20-ai-unboxed-tools-workflows/comic-page.avif` - clicking on it should open the full-size image in a new tab

Here's how to include the links from the transcript:

- Make sure ALL links from the transcript are included inline the relevant points in the narrative, captions, cards, etc.
- Where links are chats, also read chat transcripts from chats/ and include relevant snippets to enhance the narrative.
- Prefer links, not buttons, when adding click event handlers to linkable content. That way, right-clicking to open in a new tab works.
- Where images are present, include them - along with a caption. The image and caption should link to the associated link (if present), else open the image in a new tab.
- Embed https://sanand0.github.io/llmpricing/ as an IFRAME in a full-width container, with a caption linking to the source.

Design: Add tooltips and popups as informative and engaging aids where relevant

- **Tooltips** are for: Context about non-obvious terms or phrases (only if relevant and useful); Additional context about references (where possible)
- **Popups** are for: Citations: Search for and include references; Cite the key point from the reference and link to it. Supporting material: Provide extensive context, quotes, external references, etc.

This will be deployed at https://sanand0.github.io/talks/2026-06-20-ai-unboxed-tools-workflows/

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, break this into parts, generating the .html in chunks or layered edits (keeping each chunk small) and saving it, checking it, then updating it with the next iteration, and so on.

Update README.md to include this talk in the list of talks.

---

Add a bottom margin to .stat-band, .gallery-band, and any other similar full-width bands to create more breathing room between sections.
Make .pull-quote wider to break the flow a bit more.
Style .prompt-box differently than .pull-quote to make the prompts stand out more.
Render the takeaway as cards. Links have low contrast inside .takeaways-band - either change the link color or the band color.

Clicking on the https://github.com/sanand0/llmartstyle/releases/download/text2/*.png images should open a popup with the image and caption that includes an option to click to download the image.

Drop the embed of https://sanand0.github.io/llmpricing and instead embed:

- [LLM Art Styles Catalog](https://sanand0.github.io/llmartstyle/?category=text2)
- [LLM double-checking](https://sanand0.github.io/llmevals/double-checking/)
- [Ideator Tool](https://tools.s-anand.net/ideator/)

Weave in more prompts / responses (verbatim) in the script.
Include the chats where possible as snippets with a link that pops the chat transcript up (rendered as Markdown) with a link to the original (shared - not private) chat link.

---

/btw Create a short blog post in my style (see anand-writing-style skill and my blog posts at ~/code/blog/) as 2026-06-20-ai-unboxed-tools-workflows/ - which I'll publish on my blog and on LinkedIn. The aim is to teach the most important concepts from this talk in a concise, engaging, and memorable way - focus on the single most important takeaway and weave a few supporting elements around it. <!-- note: this was rubbish! -->

<!-- claude --resume 480db14f-7f99-48f1-a23b-0d7df35d4f5b --dangerously-skip-permissions -->

## Comic Page

<!--
GPT Image 2 - https://chatgpt.com/c/6a375ebd-bd6c-83ee-8926-1e8354848f82
-->

Draw this as a full-color explainer comic page (portrait) - sequential explanation, friendly narrator, diagrams embedded inside panels, visual metaphors, self-aware captions, and clear cause-and-effect storytelling. Style: expressive characters, comic-style ALL CAPS, vibrant modern colors, clear visual hierarchy. Prefer pictures over words. Use recurring visual metaphors so the reader understands the idea even while skimming. Think about the most important points, structure it as a memorable story.

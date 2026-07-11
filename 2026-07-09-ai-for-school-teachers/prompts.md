# Prompts

## Data story, 5 Jul 2026

<!--
cd ~/code/talks/
dev.sh -- claude --dangerously-skip-permissions --model opus --effort high
-->

Generate a beautiful narrative story about this 2-hour session by [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted in-person for the teachers of Sivaswamy Iyer School at Mylapore, Chennai, on using AI in education, on Thu 9 Jul 2026 (3:30-5:30 pm IST).

Create this as 2026-07-09-ai-for-school-teachers/index.html.

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use the following as examples to follow LOOSELY, not strictly:

- 2026-06-16-eqt-data-stack-for-agents/index.html
- 2026-06-12-let-ai-take-your-exams/story.html
- 2026-05-23-iim-ai-unboxed-context-engineering/index.html

Use the talk transcript and the main content source. It's at 2026-07-09-ai-for-school-teachers/transcript.md.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.

You may also read any other relevant content to weave into the narrative, such as:

- 2026-07-09-ai-for-school-teachers/claude-chat.md

Make sure the design is engaging. Allow visual elements (e.g. images, videos, embedded content, etc.) to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc.

Add the top takeways from the talk as end cards.

Include links at the appropriate places as follows:

- Show this visual summary: summary.avif (I'll add it later). max-width: 100%. Clicking on it should open the full-size image in a new window. <!-- Visual summary chat: https://chatgpt.com/c/6a51b6a8-8fd4-83e8-9879-1982a5d35097 -->
- LINK: transcript.md near the top - it should open in a popup and render as HTML.

Search online and LIBERALLY add inline link to material relevant to the narrative - that are mentioned (directly or indirectly) in the workshop, as well as any material that can provide useful context to the reader.

Design:

- Make sure bands/wraps/embeds have a bottom margin.
- Ensure card groups are allowed more width, e.g. so that the 3-4 cards fit in one row on desktop.
- Feel free to add tooltips and popups as informative and engaging aids.
- **Tooltips** are for: Context about non-obvious terms or phrases (only if relevant and useful); Additional context about references (where possible)
- **Popups** are for: Citations: Search for and include references; Cite the key point from the reference and link to it. Supporting material: Provide extensive context, quotes, external references, etc.

This will be deployed at https://sanand0.github.io/talks/2026-07-09-ai-for-school-teachers/

Use sub-agents as required for token efficiency (e.g. Haiku, Sonnet, reducing context).

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, break this into parts, generating the .html in chunks or layered edits (keeping each chunk small) and saving it, checking it, then updating it with the next iteration, and so on.

Update README.md to update relevant links.

---

A few notes:

- The school is currently a co-ed school, not just a girls school.
- Transcript corrections - fix these in the HTML and in the transcript (if applicable)
  - It was Sridharan, not Anand, who said "Ava dhaan head of our AI department" - the head of the AI dept (a lady - other than Anand and Sridharan, the room only had lady teachers). Correct the transcript too.
  - Anand didn't say "I don't know for sure, that's why I'm asking". Reword correctly. Find and fix any other such incorrect interpretations.
  - "ukkaandhu iruppan" -> "ukkaandhundu iruppane"
  - "The teacher — a senior man — hesitated" -> "A senior person hesitated"
  - "Tamil-la pesungov" -> "Tamil-la pesungo"
- Embed my GDPVal visualisation: https://sanand0.github.io/datastories/gdpval/
- Render the full Claude chat in Markdown in a popup
- Link to the LBSNAA talk and content as required. Embed the song.
- Link to my TDS course: https://tds.s-anand.net/ where relevant.

When embedding pages, include a caption with a link to the embedded page opening in a new window.
Allow embedded content to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc. Just like the image.

<!-- claude --resume 1710b52e-5297-4db9-bb38-11019a27dc5d --dangerously-skip-permissions -->

# Prompts

<!--

dev.sh -v /home/sanand/code/blog/:/home/sanand/code/blog/:ro

-->

## Story (Copilot Yolo - Claude Sonnet 4.6 high)

Generate a beautiful narrative story about the talk [Anand](https://www.s-anand.net/), LLM Psychologist at Straive and faculty for the [Tools in Data Science](https://tds.s-anand.net/) course for the IITM BS Program, delivered on 18 Mar 2026 to the IIT Madras Academic Advisory Council.

Create this as 2026-03-18-iitm-academic-council/index.html

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use 2026-03-18-iitm-office-of-institutional-advancement/index.html, 2026-03-12-nie-ai-roadmap/index.html, 2026-02-26-vibe-coding-for-humanities-ashoka/index.html as examples - to follow LOOSELY, not strictly.

Use 2026-03-18-iitm-academic-council/transcript.md - that's the talk transcript.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.
- Include images and videos inline where appropriate. These are present in the transcript.
- Include ALL links from the transcripts.

Make sure the design is engaging. Allow some elements to expand beyond the width of the main content column, and use a different background color for these elements to make them pop, etc. The sketchnote could be one such.

Add the top takeways from the talk at the end.

Prominently include these near the top:

- include the sketchnote at 2026-03-18-iitm-academic-council/sketchnote.avif - clicking on it should open the full-size image in a new tab
- link to the transcript

Search online and liberally link to any other relevant material.
You will also find references in my blog. Files are at /home/sanand/code/blog/ and deployed at https://www.s-anand.net/blog/

Feel free to add tooltips, popups, or animated SVGs as informative and engaging aids.

**Tooltips** are for:

- Context about non-obvious terms or phrases (only if relevant and useful)
- Additional context about references (where possible)

**Popups** are for:

- Citations. Search for and include references. Cite the key point from the reference and link to it.
- Supporting material. Provide extensive context, quotes, extracts from slides, external references, etc.

**Animated SVGs** are for:

- Explaining processes, mechanisms, workflows, etc. The aim is to make users FEEL a process. One glance should give them an intuitive understanding of how it works, even before they read the accompanying text. Show how things are connected, what data flows from where to where, how elements, interact, etc.

This will be deployed at https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/

Update README.md to include this talk in the list of talks.

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, you MUST break this into parts, generating a SMALL scaffolding for index.html first, saving it, then then updating it with the next layer or chunk, and so on.

<!-- copilot --resume=2dde2369-5f14-40da-ae75-b828052b72d5 -->

## Ideas Page (Copilot Yolo - Claude Sonnet 4.6 high)

Modify 2026-03-18-iitm-academic-council/ideas/index.html so that the cards are of uniform height.
Move all ideas data into 2026-03-18-iitm-academic-council/ideas/ideas.json and generate the cards from that.

Create an 2026-03-18-iitm-academic-council/ideas/table.html that shows the ideas as an elegant, minimal, sortable table from the same ideas.json data.
Columns: council lens, title, importance, novelty. Clicking the title should open a popup with the full idea description and all other details.

Link to 2026-03-18-iitm-academic-council/ideas/table.html from README.md (with the ":ignore").

---

In table.html, increase the default font size, make it more compact by allowing it to collapse to a natural width (dropping the 100%) - making sure the .table-wrap is handled appropriately. Add a light/dark mode toggle (defaulting to system preference). Add a search box that filters the table in real time based on the title, description fields. Scale the importance / novelty bars so that the smallest value maps to 5%. Increase the width of the bars by 50%.

When the popup is open, arrow keys should navigate to the next/previous idea in the table, and the popup content should update accordingly. Use a more compact design. e.g. the "Explore further" is a card that has cards that has a card -- that's too much padding, condense it. Merge the source trail into Explore further, unobtrusively. The link is more important than the source trail. Unless the Evidence profile provides additional information we cannot derive from Explore further / source trail, drop it. Same with trail depth.

<!-- copilot --resume=42bfe6a5-2d25-4c14-a1f1-d5d5b71eb49a -->

## Sketchnote

<!--
Gemini Pro - https://gemini.google.com/u/2/app/b0f85aadad62ab2a
-->

Summarize this talk transcript as a visually rich, intricately detailed, colorful, and funny, sketchnote. Think about the most important points, structure it logically so that the sketchnote is easy to follow, then draw it.

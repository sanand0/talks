# Prompts

<!--

dev.sh -v /home/sanand/code/blog/:/home/sanand/code/blog/:ro

-->

## Analysis (Copilot Yolo - GPT 5.4 xhigh)

I'm speaking to the IIT Madras Academic Council on the innovations in education I've been experimenting with using AI.
Research this group and document who they are, what they care about, and what their current challenges are.

Go through the posts in /home/sanand/code/blog/ tagged "education" since 2024 as well as my transcripts in /home/sanand/Dropbox/notes/transcripts/ and the things I learned in /home/sanand/code/til/
Go through the code / commits in /home/sanand/code/tools-in-data-science-public/ - which is my actual "Tools in Data Science" course - and /home/sanand/code/exam/ - which is my evaluation portal.
Based on these, comprehensively list ALL innovations I have been experimenting along with a rating of their relative importance (based on impact and relevance) as well as novelty on a percentage scale.
Include a title, description, nature of impact, source, and impact & novelty ratings.
Finally, summarize all the innovations in a table with columns "Innovation", "Importance (0-100%)", "Novelty (0-100%)", sorted by importance.

Plan before executing. Be comprehensive. Use sub-agents where needed.
Save this in 2026-03-18-iitm-academic-council/ideas.md

---

Now that you have a better idea of the structure of the folders and files, think about a better strategy to scan the content to discover innovations. How could you efficiently find high impact & novelty ideas?

Also consider: content not DIRECTLY related to education may still have AI / LLM innovations that I'm implicitly applying to education or are closely related to education (e.g. I'm learning something, coding tools that help in education, etc.) Think about effective strategies to surface these.

Using these, do another scan and update the list of innovations, their ratings, and the summary table.
Update the file 2026-03-18-iitm-academic-council/ideas.md with the new insights.

---

This (talks) folder also contains a useful source of AI innovations / experiments in education. Review the talks. Include what's NOT already covered.

---

Read my posts on /home/sanand/code/blog/pages/ai-advice.md and /home/sanand/code/blog/posts/2026/the-future-of-work-with-ai.md and any others that are related to the future in an AI world (based on the filenames).

In the light of this, and what the IITM Academic Council cares about, and the innovations I've been experimenting with, what storyline would you suggest for the talk? What are the key messages I should convey? How can I make it engaging and memorable for the audience?

Keep in mind that a good storyline should have a clear framework or metaphor that structures the talk. It should give the audience an anchor to understand and remember the key points. It should also have a narrative arc that builds up to a compelling conclusion.

Use lessons from the data-story skill but no need to create a data story. Just the storyline.

Document the storyline as an outline in 2026-03-18-iitm-academic-council/storyline.md. Include the key messages, the framework or metaphor, and the narrative arc.

---

If I wanted to give material to another coding agent to construct a storyline independently and would like to give it context, what files would you suggest I share with it for context, along with 2026-03-18-iitm-academic-council/ideas.md? List the files in order of descending priority and save in 2026-03-18-iitm-academic-council/storyline-context.md.

---

Do a post-mortem of the process you followed to identify the ideas. Specifically:

- What tools or techniques did you use to scan the content? How effective were they? What could have been better?
- What upfront documentation (e.g. in the README.md of the root) would have helped you discover content faster?

Document this in 2026-03-18-iitm-academic-council/ideas-post-mortem.md. Include specific examples of what worked well and what could be improved.

---

Based on the transcripts, list all pain points people have expressed when innovating in education with AI, and how they are stopped by the board, senate or management. You might want to find transcript that deal with education in some shape or form (NIE with Srikanth Nadhamuni, any IIT discussions, and IIM discussions, Ashoka University, any other college, school, or university discussions, discussion with Vishnu Agnihotri, Rajat in the Straive team, etc.) and then probe in different ways they might have expressed constraints.

Document this in 2026-03-18-iitm-academic-council/education-pain-points.md. Include specific examples and quotes from the transcripts.

---

Create a beautiful single-page 2026-03-18-iitm-academic-council/ideas/index.html ideas gallery that lists all the ideas in ideas.md as filterable, sortable, searchable cards. Include all information on the cards that would be relevant for the council to pick an idea to explore. Clicking on the card should beautifully open a popup with full details of the idea include (and especially) one or more links where they can explore it further, e.g. on my GitHub (see the repos for deployment), my blog (https://www.s-anand.net/blog/... - see the blog repo for URL structure). Feel free to also include any relevant material from proven research or respected experts for context.

<!-- copilot --resume=a6ed9c59-6a61-4aef-82f3-4e0aaad83366 -->

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

---

Assign each idea a unique concise id - slug-like, based on the title, but much shorter than the title, that captures the essence of what the idea is about.
Make all the popup cards in ideas/{index.html,table.html} linkable. For example, ?id=${id} should open the popup for that idea, allowing us to share links to specific ideas. Avoid polluting history when doing this - use pushState or replaceState appropriately.

---

When the page opens, display it in the same order as the id. Add an id column and make it sortable.

---

When I open the page, I see the highest ID first, not 1.

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

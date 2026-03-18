# IITM Academic Council Prompts

<!--
dev.sh -v /home/sanand/code/blog/:/home/sanand/code/blog/:ro \
       -v /home/sanand/code/exam/:/home/sanand/code/exam/:ro \
       -v /home/sanand/code/tools-in-data-science-public/:/home/sanand/code/tools-in-data-science-public/:ro \
       -v /home/sanand/Dropbox/notes/transcripts:/home/sanand/Dropbox/notes/transcripts:ro \
       -v /home/sanand/code/til:/home/sanand/code/til:ro
-->

## Discover ideas (Copilot Yolo - gpt-5.x xhigh)

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

### Storyline

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

## Alternate storyline (Copilot Yolo - Claude Sonnet 4.6)

I'm speaking to the IIT Madras Academic Council on the innovations in education I've been experimenting with using AI.

Based on the research done (see prompts.md), ideas are at 2026-03-18-iitm-academic-council/ideas.md.

Do NOT read 2026-03-18-iitm-academic-council/storyline.md - which is the alternate storyline. Instead, read the recommended files in 2026-03-18-iitm-academic-council/storyline-context.md as well as any other files you need (be liberal).

Use the data-story skill. Use sub-agents where needed.

In the light of this, and what the IITM Academic Council cares about, and the innovations I've been experimenting with, what storyline would you suggest for the talk? What are the key messages I should convey? How can I make it engaging and memorable for the audience?

Keep in mind that a good storyline should have a clear framework or metaphor that structures the talk. It should give the audience an anchor to understand and remember the key points. It should also have a narrative arc that builds up to a compelling conclusion.

Document the storyline as an outline in 2026-03-18-iitm-academic-council/storyline-v2.md. Include the key messages, the framework or metaphor, and the narrative arc.

---

Using this storyline, and the data-story skill, create a compelling Malcolm Gladwell-style narrative for the talk.

Include animated, interactive SVGs as explainers where required. The aim is to make users FEEL the process. One glance should give them an intuitive understanding of how it works, even before they read the accompanying text. Show how things are connected, what data flows from where to where, how elements, interact, etc.

Use tooltips, popups, interactions, and animations as informative and engaging aids.

**Tooltips** are for:

- Context about non-obvious terms or phrases (only if relevant and useful)
- Additional context about references (where possible)

**Popups** are for:

- Citations. Search for and include references. Cite the key point from the reference and link to it.
- Files. Link liberally to files as supporting evidence. You can use GitHub (which most files are committed / pushed to.)
  - Clicking on file links should open the files in a popup, with a link to open the original in a new tab.
  - Syntax-highlighted if code
  - Show sortable for tabular data, gradient-coloring important numeric / categorical columns if that will help understand the context

Plan the design and layout carefully before coding.

Create this as a single page in 2026-03-18-iitm-academic-council/v2/index.html.

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, you MUST break this into parts, generating the .html as a scaffolding first, then adding layered edits (keeping each chunk small, max 100KB of edits) and saving it, checking it, then updating it with the next iteration, and so on.

<!-- copilot --resume=9dd3cdbd-af56-4b72-86ba-2e7d8a99ab80 -->

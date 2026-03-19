# IITM

<!--

dev.sh -v /home/sanand/code/blog/:/home/sanand/code/blog/:ro \
       -v /home/sanand/Dropbox/notes/transcripts:/home/sanand/Dropbox/notes/transcripts:ro \
       -v /home/sanand/code/til:/home/sanand/code/til:ro

-->

## Discover (Codex - gpt-5.4 xhigh)

I'm speaking to the IIT Madras Office of Institutional Advancement on how they can use AI better in their daily activities.

Research them and form a picture of who they are, what they do (and how), and what their current challenges are.

The transcript is at `/home/sanand/Dropbox/notes/transcripts/2026-03-17 Kaviraj Vasudha IITM.md`. Read it.

Then, read required blog posts related to LLMs `/home/sanand/code/blog/` and other transcripts at `/home/sanand/Dropbox/notes/transcripts` (especially extracted AI advice at `/home/sanand/Dropbox/notes/transcripts/extracts/ai/`) and things I learnt at `/home/sanand/code/til/` as well as other talks under this directory.

Be comprehensive. Use sub-agents as required. See 2026-03-18-iitm-academic-council/ideas-port-mortem.md for tips on scanning content effectively.

Suggest what tips and tricks I could share with them that will have the most impact and they're not likely to know about.

Document these in 2026-03-18-iitm-funding-team/ideas.md. Include the source of each tip (e.g. which blog post, transcript, or TIL - as a publiclink to where the content is deployed), a description, and why you think it would be impactful for them.

## Data Visualization (Copilot Yolo - Claude Sonnet 4.6 high)

Generate a beautiful narrative story about the talk [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, delivered at the [Office of Institutional Advancement at IIT Madras](https://ia.iitm.ac.in/) on 18 Mar 2026.

Create this as 2026-03-18-iitm-office-of-institutional-advancement/index.html

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use 2026-03-12-nie-ai-roadmap/index.html, 2026-02-26-vibe-coding-for-humanities-ashoka/index.html and 2026-01-11-nptel-vibe-coding-workshop/index.html as examples - to follow LOOSELY, not strictly.

Use 2026-03-18-iitm-office-of-institutional-advancement/transcript.md - that's the talk transcript.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.

Make sure the design is engaging. Allow some elements to expand beyond the width of the main content column, and use a different background color for these elements to make them pop, etc. The sketchnote could be one such.

Add the top takeways from the talk at the end.

Here are some links to the vibe coding output Anand generated. Weave these in as links where appropriate. (These are not embeddable, so just link to them as cards. Ignore the links in comments.)

Claude - What use cases would be interesting to the team: https://claude.ai/share/369fbd8e-548f-483c-b643-d440ae074576 <!-- https://claude.ai/chat/05f5dc8c-4cf7-4f39-9ec3-30dab9c13ee7 -->
Gemini - What use cases would be interesting to the team: https://gemini.google.com/share/f732aa2acec5 <!-- https://gemini.google.com/app/ff437ad6035ed7d3 -->
ChatGPT - List of IIT Madras alumni based in Mumbai: https://chatgpt.com/share/69badcc9-fbe8-8003-bae0-252e43b697bc <!-- https://chatgpt.com/c/69ba4a26-f4d8-83a1-9682-0c70463e92dd -->
ChatGPT - Synthetic attendance data: https://chatgpt.com/share/69badcf4-35b0-8003-8725-3dbd61d6a40b <!-- https://chatgpt.com/c/69ba4af1-4570-8399-95ab-d14b91401b13 -->
ChatGPT - Data analysis of attendance data: https://chatgpt.com/share/69badd59-9be4-8003-a6de-8e04b470ef19 <!-- https://chatgpt.com/c/69ba4b84-8fc4-839a-a35e-23d42708f6f6 -->

Before this session I generated a set of use cases using 2026-03-18-iitm-office-of-institutional-advancement/prompts.md into 2026-03-18-iitm-office-of-institutional-advancement/ideas.md and generated a HTML page out of it at 2026-03-18-iitm-office-of-institutional-advancement/ideas.html. Mention the process used and link to the files, making ideas.html prominent. This is where readers can explore further use cases themselves.

Prominently include these near the top:

- include the sketchnote at 2026-03-18-iitm-office-of-institutional-advancement/sketchnote.avif - clicking on it should open the full-size image in a new tab
- link to the transcript
- link to the ideas.html page with the use cases

Search online and liberally link to any other relevant material.

Feel free to add tooltips, popups, or animated SVGs as informative and engaging aids.

**Tooltips** are for:

- Context about non-obvious terms or phrases (only if relevant and useful)
- Additional context about references (where possible)

**Popups** are for:

- Citations. Search for and include references. Cite the key point from the reference and link to it.
- Supporting material. Provide extensive context, quotes, extracts from slides, external references, etc.

**Animated SVGs** are for:

- Explaining processes, mechanisms, workflows, etc. The aim is to make users FEEL a process. One glance should give them an intuitive understanding of how it works, even before they read the accompanying text. Show how things are connected, what data flows from where to where, how elements, interact, etc.

This will be deployed at https://sanand0.github.io/talks/2026-03-18-iitm-office-of-institutional-advancement/

Update README.md to include this talk in the list of talks.

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, you MUST break this into parts, generating a scaffolding for index.html, saving it, then then updating it with the next layer or chunk, and so on.

---

We also discussed JSON and structured prompting and a few other things. Here are the links. Include these.

ChatGPT - JSON meta-prompting: https://chatgpt.com/share/69bb520a-fdac-8003-b8da-a85c74ab6982
ChatGPT - Structured meta-prompting: https://chatgpt.com/share/69bb5220-1800-8003-860f-82dd2d56cd6c
Claude - Human Verified QR Campaign Matcher: https://claude.ai/share/087a929c-c8bf-4231-9dcc-3c13c9b93591

Search for relevant links from my blog at www.s-anand.net (same as the .md files at /home/sanand/code/blog/posts/) and link to them as well, e.g. birthday cake story, IIMB panel, and any others you can find that are relevant.

---

.cite-btn does not look good. The removed border-bottom makes it feel incomplete. The super vertical alignment breaks the flow of text. It may not be apt in all places, e.g. the definition of LLM psychologist. Restructure this.

Replace all https://s-anand.net/ links with https://www.s-anand.net/ for consistency.

<!-- copilot --resume=85187af4-5c79-47e5-af24-55ff2967ca7e -->

## Sketchnote

<!--
Gemini Pro - https://gemini.google.com/u/2/app/838c68e80b53f107
-->

Summarize this talk transcript as a visually rich, intricately detailed, colorful, and funny, sketchnote. Think about the most important points, structure it logically so that the sketchnote is easy to follow, then draw it.

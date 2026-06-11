# Prompts

<!--
cd ~/code/talks/
dev.sh -p ~/code/research/3dmesh,~/Dropbox/notes/transcripts
claude --dangerously-skip-permissions
-->

Generate a beautiful narrative story about this 2-hour AI Workshop [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, had along with the Engineering Design faculty at IIT Madras at 2026-06-11-engineering-design-iitm/index.html.

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use the following as examples to follow LOOSELY, not strictly:

- 2026-04-30-harvard-education/index.html
- 2026-04-08-ai-workshop-lbsnaa/index.html
- 2026-04-06-innovation-as-a-frontier-straive/index.html

Use the talk transcripts at `~/Dropbox/notes/transcripts/2026-06-11\ Engineering\ Design*.md`. There are two versions - one recorded on phone and one on laptop. Use content unambiguously inferrable from both.
You may also read other transcripts, e.g. `find ~/Dropbox/notes/transcripts/*Palani*.md` etc., to find relevant content to weave into the narrative.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.

Make sure the design is engaging. Allow visual elements (e.g. comic page, videos, embedded content, etc.) to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc.

Make the content more scannable by **bold** to highlight the key points in the flow. Just reading the **bolded** text should give a good summary of the article.

Add the top takeways from the talk at the end.

Prominently include these:

- User prompts and relevant response snippets (potentially an image or two) from `chatgpt-fem-moving-boundary-problem.md` (show public link: https://chatgpt.com/share/6a2ae62f-7638-83ec-ad78-3a132b670079), `claude-fem-moving-boundary-problem.md` (show public link: https://claude.ai/share/01443759-9d0c-40ae-a488-d99564a16446) and `heim_visual_test_assets/heim_visual_test/`
- User prompts and relevant response snippets from `chatgpt-mesh-simulation-experiment.md` (show public link: https://chatgpt.com/share/6a2ae72e-7468-83ec-9fd8-2a29f328589f) which generated the prompt used in `~/code/research/3dmesh/prompts.md` that led to creating the output there.
  - Embed `~/code/research/3dmesh/*.html` in the flow, as well as relevant snippets from `~/code/research/3dmesh/prompts.md` other files in the directory.

Search online and LIBERALLY add inline link to material relevant to the narrative - that are mentioned (directly or indirectly) in the workshop, as well as any material that can provide useful context to the reader.

Feel free to add tooltips and popups as informative and engaging aids.

- **Tooltips** are for: Context about non-obvious terms or phrases (only if relevant and useful); Additional context about references (where possible)
- **Popups** are for: Citations: Search for and include references; Cite the key point from the reference and link to it. Supporting material: Provide extensive context, quotes, external references, etc.

I repeat: Link liberally at every opportunity. Find more opportunities to link to content, augment with external material and references, and enrich the content.

This will be deployed at https://sanand0.github.io/talks/2026-06-11-engineering-design-iitm/

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, break this into parts, generating the .html in chunks or layered edits (keeping each chunk small) and saving it, checking it, then updating it with the next iteration, and so on.

Update README.md to include this talk in the list of talks.

--- <!-- steering -->

I've uploaded:

https://files.s-anand.net/pages/3dmesh/jaw_fit_experiment.html
https://files.s-anand.net/pages/3dmesh/skull_patch_experiment.html

You may link to and/or embed these.

---

Add a dark/light mode toggle.
Add a margin below .wide-figure and .band-quote.
Center the grid elements in .cast-inner.
Inside .wf-grid the figcaption has too low a contrast. Check all contrast - ensure it's OK in dark AND light modes.

In the chat popups, skip the YAML metadata or render it better.

Link to the speakers: https://www.s-anand.net/, Sundar (https://home.iitm.ac.in/snatarajan/), search https://ed.iitm.ac.in/team.html for the rest - replace Palani's with this link.

There are two embeddings of the synthetic jaw fit. Drop one.
Include an embedding of https://files.s-anand.net/pages/3dmesh/skull_patch_experiment.html.

Sundar said, "This could be a first or second-year PhD student." - not "The creativity of a first-year student. The knowledge of a tenured professor." Reword that section and surrounding areas correctly.
"To interact with ChatGPT is a boon for married men..." - Sundar said that, not Anand.
"Nirav's response isn't to fight the collaboration..." -> "Anand's response isn't to fight the collaboration..." - this is based on the TDS course.
"... Code reviews now happen through LLMs anyway ..." - Anand said that, not Nirav.
"I get two outputs..." - Anand said that, not Nirav.
"Only 10%, I bet, will be able to do that in the exam." - Anand said that, not Nirav.
"Saravana names with the famous meme: a junior writes one line..." - Bijoy said that, not Saravana.
"Saravana raises the institutional blocker" -> Nirav raises the institutional blocker.
"For 800 students, it's $100. For the whole term. Put together." - Anand said that, not Nirav.
"Maybe in a few years, most automotive industries ..." - Anand said that, not Nirav.

Since so many quotes were wrong, do a careful fact-check, list ALL quotation errors you find. (Treat what I said above as correct - I was in the room. Sometimes, the transcripts may be wrong.)
Then, one-by-one, correct them, and produce an error report so I can verify.

---

Add bottom margin to .full-embed.

It's Nirav's "70 students", not Saravana's, that Anand will add to AI Pipe.
Live leaderboard hidden names is actually Nirav.
Saravana doesn't have an entrance exam - hidden names is Nirav's dashboard. WhatsApp-gaming is also in Nirav's course.

<!-- claude --resume b861b76e-acc5-4be4-b96c-a68922fef290 --dangerously-skip-permissions -->

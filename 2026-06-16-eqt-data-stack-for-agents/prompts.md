# Prompts

## Data story, 16 Jun 2026

<!--
cd ~/code/talks/
dev.sh -p ~/code/,~/r2/media,~/Documents/chatgpt/
claude --dangerously-skip-permissions --model opus --effort high
-->

Generate a beautiful narrative story about this 1-hour session by [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted in-person for the [EQT](https://eqtgroup.com/) India AI & Cyber Summit on 16 Jun 2026 (3:30-4:30 pm IST).

Create this as 2026-06-16-eqt-data-stack-for-agents/index.html.

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use the following as examples to follow LOOSELY, not strictly:

- 2026-06-12-let-ai-take-your-exams/story.html
- 2026-05-23-iim-ai-unboxed-context-engineering/index.html
- 2026-04-30-harvard-education/index.html

Use the talk transcript and the main content source. It's at 2026-06-16-eqt-data-stack-for-agents/transcript.md.
You may also read any other relevant content to weave into the narrative.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.

Make sure the design is engaging. Allow visual elements (e.g. images, videos, embedded content, etc.) to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc.

Add the top takeways from the talk at the end.

Include links from the transcript at the appropriate places as follows:

- Embed the audio near the top: https://github.com/sanand0/talks/releases/download/talks/2026-06-16-eqt-data-stack-for-agents.opus
- Link to the transcript near the top - it should open in a popup and render as HTML.
- Show this visual summary: summary.avif. max-width: 100%. Clicking on it should open the full-size image in a new window. <!-- Visual summary chat: https://chatgpt.com/c/6a317ee0-edd0-83ec-9302-db5c50a08137 -->
- Customer master dataset:
  - Link to the page with the files and prompt: https://files.s-anand.net/pages/customer-masters-data/
  - Embed the Excel: https://view.officeapps.live.com/op/embed.aspx?src=https://files.s-anand.net/pages/customer-masters-data/customer-masters.xlsx (full-width)
- ChatGPT conversation for reconciliation
  - Link to ./reconciliation-chatgpt.md - it should open in a popup and render as HTML. (This is a temporary chat and there is no shareable link)
  - Include relevant quotes and snippets and summaries from the chat in the narrative.
  - Embed the reconciliation report Excel: https://view.officeapps.live.com/op/embed.aspx?src=https://files.s-anand.net/pages/customer-masters-data/reconciliation.xlsx (full-width)
- HR Analysis: Embed ./hr-analysis.html (full-width, appropriate aspect ratio - inspect its contents).
- Cortex-generated AI use cases and analyses: Embed https://files.s-anand.net/pages/ai-use-cases-commercial-data/ (full-width, appropriate aspect ratio - inspect its contents).
- Claude survey analysis:
  - Link to ./survey-analysis-claude.md - it should open in a popup and render as HTML.
  - Include relevant quotes and snippets and summaries from the chat in the narrative.

DO NOT LINK to, but mention, `forms.s-anand.net/datastack/` as the form I used to collect responses. The link will only work when I enable it - and I disabled it after the exam.
DO go through the analysis in 2026-06-16-eqt-data-stack-for-agents/survey-analysis-claude.md and weave all relevant insights into the narrative.
The questions/responses are at `~/code/liveform/forms/datastack/{form.yaml,responses.tsv}` - you may use that for further analysis and include insights from it, but do not link to it directly.

Here's how to include the links:

- Make sure ALL links mentioned above are included at the right places (e.g. in the narrative, captions, cards, etc.)
- Embed pages with a caption. The caption should include a link to the embedded page opening in a new window.

Search online and LIBERALLY add inline link to material relevant to the narrative - that are mentioned (directly or indirectly) in the workshop, as well as any material that can provide useful context to the reader.

Feel free to add tooltips and popups as informative and engaging aids.

- **Tooltips** are for: Context about non-obvious terms or phrases (only if relevant and useful); Additional context about references (where possible)
- **Popups** are for: Citations: Search for and include references; Cite the key point from the reference and link to it. Supporting material: Provide extensive context, quotes, external references, etc.

This will be deployed at https://sanand0.github.io/talks/2026-06-16-eqt-data-stack-for-agents/

Use sub-agents as required for token efficiency (e.g. with Haiku, reducing context), planning (e.g. with Opus), etc.

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, break this into parts, generating the .html in chunks or layered edits (keeping each chunk small) and saving it, checking it, then updating it with the next iteration, and so on.

Update README.md to update relevant links.

---

FYI: I've added `margin-bottom:2rem;` to .summary-wrap, .stat-band, .embed-wrap. Retain that.

Modify .cards so that it can take up more width so that the 3 card .cards fit in one row on desktop.

Render the takeaways as elegant, responsive cards.

<!-- claude --resume 488ab50c-7394-4a48-b41a-49b29aebca80 --dangerously-skip-permissions -->

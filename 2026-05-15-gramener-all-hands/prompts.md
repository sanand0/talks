# Prompts

## Write the talk, 16 May 2026

<!--

cd ~/code/talks/
dev.sh -v /home/sanand/code/private-research/2026-05-gramener-all-hands/:/home/sanand/code/private-research/2026-05-gramener-all-hands/:ro
copilot --yolo --model claude-sonnet-4.6 --effort medium

-->

Create a talk transcript of my May 2026 Gramener talk in 2026-05-15-gramener-all-hands/index.html

Use the "# Email" section from `/home/sanand/code/private-research/2026-05-gramener-all-hands/README.md` as the content but ANONYMIZE all sensitive information.

Highlight what was insightful or funny.

Make sure the design is engaging. Allow visual elements (e.g. sketchnote.avif, embedded slides, etc.) to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc.

Add the top takeways from the talk at the end.

Prominently include the sketchnote near the top. Clicking on it should open the full-size image in a new tab.

Here's how to include the links, images, and videos:

- Make sure ALL links are included, except sensitive / private links. Specifically:
  - Skip tool links: https://tools.s-anand.net/slide - they are covered in the transcript.
  - Include everything from *.github.io, github.com, s-anand.net, metr.org, agentskills.io, claude.ai/share, files.s-anand.net/pages/ed-content-pipeline, docs.google.com
  - Exclude stride-feedback, https://claude.ai/chat/
- Where images are present, include them - along with a caption. The image and caption should link to the associated link (if present), else open the image in a new tab.
- Embed these links as IFRAMEs:
  - https://agentskills.io/
  - https://docs.google.com/presentation/d/1lQx2Xa_vjVQohvAvht2SWgj2KcuWXH3K/edit?usp=sharing&ouid=105685292426632572114&rtpof=true&sd=true
  - https://files.s-anand.net/pages/ed-content-pipeline/
  - https://github.com/sanand0/blog/blob/live/pages/prompts/fragments.md
  - https://github.com/sanand0/scripts/blob/main/agents/data-story/SKILL.md
  - https://metr.org/time-horizons/
  - https://mynkpdr.github.io/insurle-demo/
  - https://sanand0.github.io/journalists/statnostics/
  - https://sanand0.github.io/talks/2026-03-18-verifiable-agents/
  - https://www.s-anand.net/blog/derived-formats-with-gemini/
  - https://www.s-anand.net/blog/prompts/
  - https://www.s-anand.net/blog/prompts/fragments/#meeting-preparation

Search online and liberally link to any other relevant material that are mentioned (directly or indirectly) in the talk, as well as any material that can provide useful context to the reader.

This will be deployed at https://sanand0.github.io/talks/2026-05-15-gramener-all-hands/

**IMPORTANT**: Remember the content is primarily and almost entirely the anonymized transcript. We're just linking from it, embedding content along with the flow, adding takeaways at the end, adding context at the beginning, etc.

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, break this into parts, generating the .html in chunks or layered edits (keeping each chunk small) and saving it, checking it, then updating it with the next iteration, and so on.

Update README.md to include this talk in the list of talks.

---

agentskills.io is not embeddable. Just link to it.
github.com links are not embeddable. Instead, render the Markdown version of the raw content for https://raw.githubusercontent.com/sanand0/blog/refs/heads/live/pages/prompts/fragments.md and https://raw.githubusercontent.com/sanand0/scripts/refs/heads/main/agents/data-story/SKILL.md

The content may be a bit different from my transcript? Align it with the original perfectly.

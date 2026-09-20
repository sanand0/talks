# Prompts

## Story, 20 Sep 2026

<!--
cd ~/code/talks/
dev.sh -- claude --dangerously-skip-permissions --model sonnet --effort high
-->

Create a narrative story for the talk at 2026-09-19-shree-niketan-schools/ similar to other recent talks, using the talk-story skill.

---

Changes:

- Ensure that the user can jump to any section from anywhere - similar to how this was done in other talks.
- Link more extensively - e.g. Vercel, Github Pages, Shree Niketan schools, etc.
- The link to "ASD-STE100" inside .prompt-box .plabel has too little contrast: it's dark on dark. Fix this and similar issues.
- Update config.json with all relevant links - the comic is certainly one. (Maybe that's the only one to add, but check.)

Also, modify both talk-story/SKILL.md files minimally (using an Opus sub-agent for planning / judgement / review) to ensure that the above mistakes don't happen again, and also any other mistakes you made in this session (e.g. unbalanced tags, cards where one was standing out, etc.) that had to be corrected in multiple other prompt.md files don't happen again. It's fine to give examples from specific talks in this repo.

BTW, don't emphasize Infinite Engineers so much. Remove the button on the navbar and the link in the footer - just one link overall is fine.

--- <!-- steering -->

I've made https://indigo-ledger-class-8.root-node.chatgpt.site - you can embed it if possible.

--- <!-- steering -->

Markdown bullets in popups are too close to the left.

--- <!-- steering -->

The jump menu looks odd when the contents are justified - they don't look aligned. Instead, maybe make it a grid of 3-4 items per row and ensure they're aligned, or something like that?

---

In config.json, drop the link and mention of Infinite Engineers. Add a link to Shree Niketan Schools.

Also have Opus review the skills to see if anything in those skills are CAUSING issues that I'm having to fix in prompt.md files, and if there are opportunities to simplify the SKILL.md (e.g. by delegating to examples). Also, when using examples, make sure to use the latest. For example, 2026-09-19-shree-niketan-schools/ would be a better example for the jump menu because we left-aligned it. To make things future-proof, having it find the latest example might work better - but you decide.

<!-- claude --resume cc54bd9e-889d-4735-85d2-436926706fae --dangerously-skip-permissions -->

<!-- Comic page: https://chatgpt.com/c/6aafa40d-abf0-83ec-893d-a763c183b61d -->

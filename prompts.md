# Prompts

## Update skill, 11 Jul 2026

<!--
cd ~/code/talks/
dev.sh -- claude --dangerously-skip-permissions --model fable --effort medium
-->

I created `.claude/skills/talk-story/` a few months ago. Since then, I've created several stories. You can check the talk directory filenames or git timestamps to understand this.

I haven't looked at the skill. I have been creating `*/prompts.md` files based on past prompts, editing it myself.

Some of my prompts overlap with the talk-story skill. Some might even contradict it.

Go through the skill, my prompts.md, the way in which Claude Code session have used it (see ~/.claude/ and look up session IDs based on the `<!-- claude resume $ID ... -->` in the prompts.md files) - what's worked well, what hasn't, what corrections I've had to make, etc.

Based on this, suggest two things:

1. A revised skill (feel free to write it from scratch, editing the existing talk-story skill in-place) that I can use.
2. A sample prompt or prompt template that I can copy paste and edit for future talk stories. This should cover the common variations. I mean, if there's something I've specified in two prompt.md files, it should probably be in the template. If it's in most prompt.md files, it should probably be in the skill. If it was in just one prompt.md, we can ignore it unless you think it important.

<!-- claude --resume dbf91323-9f06-4dda-bcdc-e0bc2b961fc1 --dangerously-skip-permissions -->

## Talks skill, 26 Mar 2026 (Claude Code - Sonnet 4.6 medium)

In many of my recent talks, I have used a prompts.md to generate interactive HTML using the inputs, which almost always includes a transcript, maybe slides as PDF converted to images, YouTube video links, audio recording, screenshots, links, etc.

Create a skill that automated this.

It should be able to convert PDF to compressed images the way some prompts.md describe how (and text, for reference, perhaps?)

It should be able to get screenshots of links and embed them - which is currently manual but is best automated.

It should be able to tell the user what is missing (e.g. context about the event which the user needs to provide, additional files maybe, design choices, etc.) and use that to generate the page. Maybe the user could provide these as a separate file in the directory?

Read up on the latest, not outdated, SKILL.md best practices that are proven to work and likely to be timeless. Think about the best way to get context from the user.

Based on these, create the skill with any associated scripts.

Try it on a few samples but not by running the entire skill - instead, check if the skill would produce the desired output (which must be good - need not be exactly what I produced).

Also suggest improvements to the skill after this. Document your notes, process, evaluations, suggestions, and any other items in a notes.md.

Keep all additions in a single folder whose location you should decide.

---

Revisions:

- pdf-to-images.sh: Resize before encoding. Even avif files should be reduced to 1280x or less.
- screenshot-url.sh: Test out `uvx rodney` for screenshots. If that works, we might not even need this script and just mention the usage in the SKILL.md.
- SKILL.md - audio will only be .opus, not .ogg or .mp3

Go through recent past chat sessions by browsing ~/.claude/ and ~/.copilot/ and based on the process, see if any changes are needed. For example, remove what's redundant (since the coding agents are doing this properly anyway even uninstructed), add guidance where things go wrong, etc.

<!-- claude --resume d2b4048b-11c5-4b50-9e0d-e53f53d44b2f -->

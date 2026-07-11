# When Data is for Agents, Fifth Elephant, 7 Jul 2026

## Revise story, 11 Jul 2026

<!--
cd ~/code/talks/2026-07-07-when-data-is-for-agents-fifth-elephant
dev.sh -p ~/code/research:ro,~/Documents/forms:ro,~/Dropbox/notes/transcripts:ro -- claude --dangerously-skip-permissions --model fable --effort high
-->

Update index.html as follows.

Link to the original ChatGPT and Claude chats used in this workshop - including preps. (Skip the links in comments. They're private.)

- chatgpt-chat-prep.md: https://chatgpt.com/share/6a525b21-2bcc-83ee-9da3-a4bf8a691f8e <!-- https://chatgpt.com/c/6a4282d9-7250-83ec-a4a7-324e533d33b2 -->
- chatgpt-chat-1.md (prompt preparation): https://chatgpt.com/share/6a5259f6-ce64-83e8-be4b-989e13f8dadd <!-- https://chatgpt.com/c/6a4c51b7-9700-83ec-8d88-8798ccff3b79 -->
- chatgpt-chat-2.md (research): https://chatgpt.com/share/6a4ce075-cf20-83ec-bbc3-ad7621c2221e <!-- https://chatgpt.com/c/6a4cbe37-b288-83ec-aa42-f78f26393f9b -->
- NEW: chatgpt-chat-collation.md: https://chatgpt.com/share/6a525953-3da0-83e8-94a5-a8d99b291fc7 <!-- https://chatgpt.com/c/6a4cc169-d84c-83ec-8321-a4fa0f5eea7d -->
- chatgpt-chat-insights.md: https://chatgpt.com/share/6a5259bb-f858-83ee-8497-9882a849a66a <!-- https://chatgpt.com/c/6a521805-f364-83ee-b879-3aaf198d1492 -->
- claude-chat-prep.md: https://claude.ai/share/5b3d4f2d-c5b1-4b7b-9a66-c55fccf89da4 <!-- https://claude.ai/chat/e48c26cc-42e3-4b7c-8677-0bbc70f310b4 -->
- claude-chat-1.md (research): https://claude.ai/share/f620c868-00e9-4b93-a09e-d3cb18af0e26 <!-- https://claude.ai/chat/615864e9-b0f1-4db3-a24d-d6a1adf113a5 -->
- claude-chat-2.md (analysis): https://claude.ai/share/19d72406-b262-482e-895e-c7da0fde3382 <!-- https://claude.ai/chat/8827adb5-7e3b-415a-af71-7f3950057ecf -->

Also, rewrite relevant parts of the story based on the following inputs. If these trigger ideas for rewrites in other parts, please do so.

- Incorporate what's in chatgpt-chat-collation.md into the story. Specifically, mention some of top collated hypotheses briefly in the story, and include a popup to list all.
- "The results trickled onto the shared form [(sample verdicts)](https://sanand0.github.io/talks/2026-07-07-when-data-is-for-agents-fifth-elephant/#v1), and they were… deflating" - add a table here showing the actual results, e.g. from all thirteen participants at all 3 levels, with the cells showing the results, and a clickable popup on each cell or row showing the full result.
- Link to the original chats, in context, wherever possible. For example, "The audit [found one structural flaw and several smaller ones](https://sanand0.github.io/talks/2026-07-07-when-data-is-for-agents-fifth-elephant/#audit)" could have a link to the original shared chat appended to it.
- claude-chat-2.md has content I missed copying earlier. Specifically, the results of auditing the first benchmark. (Use git diff to see the differences.) Incorporate that into the story - specifically, the exact results of the audit and Claude's revised suggestion on the prompt.

## Data story, 11 Jul 2026

<!--
cd ~/code/talks/
dev.sh -p ~/code/research:ro,~/Documents/forms:ro,~/Dropbox/notes/transcripts:ro -- claude --dangerously-skip-permissions --model fable --effort high
-->

Generate a beautiful narrative story about this 3-hour workshop as part of [Fifth Elephant](https://hasgeek.com/fifthelephant/) titled
[When data is for agents, not humans](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/) by
[Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted at
at [Microsoft Luxor North Tower](https://maps.app.goo.gl/muEa7bHZbVBX4sW8A) on Tue 07 Jul 2026 (2:00 pm IST).

Create this as 2026-07-07-when-data-is-for-agents-fifth-elephant/index.html.

Use the following as examples to follow LOOSELY, not strictly:

- 2026-07-04-vizchitra-dialog-curators-dilemma/index.html
- 2026-06-20-ai-unboxed-tools-workflows/index.html
- 2026-06-16-eqt-data-stack-for-agents/index.html

Use the talk transcript as the main content source: 2026-07-07-when-data-is-for-agents-fifth-elephant/transcript-{phone,laptop}.md. I transcribed on phone AND laptop. Both have minor phonetic errors. Double-check to be sure.

You may also read any other relevant content to weave into the narrative, such as these files from 2026-07-07-when-data-is-for-agents-fifth-elephant/:

- Chats used to prepare for the workshop
  - chatgpt-chat-prep.md
  - claude-chat-prep.md
- Chats used during the workshop:
  - chatgpt-chat-1.md
  - chatgpt-chat-2.md
    - Genreated SKILL: corpus-for-agents-skill.md and script: make_catalog.py
  - claude-chat-1.md
  - claude-chat-2.md
- Transcripts of the session (might contain phonetic errors):
  - transcript-laptop.md
  - transcript-phone.md
- Prompts prepared for the session:
  - benchmark-prompt.md
  - collation-prompt.md
  - postmortem-prompt.md
  - research-prompt.md
  - skill-prompt.md
- Analysis of the results
  - chatgpt-chat-insights.md
- Survey documents at ~/Documents/forms/data-is-for-agents:
  - form.yaml: Form used to collect responses from participants.
  - responses.tsv: Responses collected from participants.
- Also check out my claude Code / Codex sessions run on 7 July 2026 in the `~/code/research/` folder - you'll find these in `~/.claude/` and `~/.codex/`

Based on your reading, think about the most useful narrative to craft, and the most engaging way to present it.

Prominently include near the top:

- Link to the transcript (whichever is better) and promptss as popups, rendered as HTML.
- Embed chat or response.tsv fragments as required. Summarize in the narrative and show popups that render the more detailed chat sections as HTML.
- Show this visual summary: summary.avif. Clicking opens the full-size image in a new window. <!-- Visual summary chat: https://chatgpt.com/c/6a521805-f364-83ee-b879-3aaf198d1492 -->

Include links from the transcript / responses at the appropriate places.
Search online & research material that will improve the reading experience and include these as well.

This will be deployed at https://sanand0.github.io/talks/2026-07-07-when-data-is-for-agents-fifth-elephant/

<!-- claude --resume dea7a0a5-c078-4b16-b9bc-fd3eee3b51f9 --dangerously-skip-permissions -->

# Talk story prompt template

Copy the block below into `<talk-dir>/prompts.md`, delete what doesn't apply, fill in the
rest. Everything constant (Gladwell style, blockquotes, bold-scannability, takeaway cards,
full-width bands with margins, tooltip/popup rules, link/embed/caption conventions,
share-links-only, chunked generation, QA pass, README update) lives in the talk-story skill —
don't repeat it unless you want to override it.

---

# Talk Title, DD Mon YYYY

## Data story, DD Mon YYYY

<!--
cd ~/code/talks/
dev.sh -p ~/Documents/forms:ro,~/Dropbox/notes/transcripts:ro -- claude --dangerously-skip-permissions --model opus --effort high
-->

Generate a beautiful narrative story about this N-hour session/workshop/panel by
[Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted in-person/online
for AUDIENCE at [EVENT](EVENT-URL) on DD Mon YYYY (H:MM-H:MM IST).
<!-- Panels: list each speaker with LinkedIn/website URL and role; name the moderator. -->

Create this as YYYY-MM-DD-slug/index.html.
<!-- Use story.html instead when a landing page with multiple sub-pages is planned. -->

Use the following as examples to follow LOOSELY, not strictly:
<!-- Usually the 3 most recent talks you liked. -->

- RECENT-TALK-1/index.html
- RECENT-TALK-2/index.html
- RECENT-TALK-3/index.html

Use the talk transcript as the main content source: YYYY-MM-DD-slug/transcript.md.

You may also read any other relevant content to weave into the narrative, such as:

- YYYY-MM-DD-slug/claude-chat.md — used to plan this session.
- YYYY-MM-DD-slug/chatgpt-chat.md — used to run/analyze this session.
- YYYY-MM-DD-slug/{form.yaml,responses.tsv} — survey questions and responses.
  <!-- If PII: "Original with PII is at ~/code/liveform/forms/SLUG/responses.tsv" -->

Prominently include near the top:

- Embed the video: https://media.s-anand.net/YYYY-MM-DD-slug.webm (or https://youtu.be/...) — full-width container.
- Embed the audio: https://github.com/sanand0/talks/releases/download/talks/YYYY-MM-DD-slug.opus
- Link to the transcript — popup, rendered as HTML.
- Show this visual summary: summary.avif (add "I'll add it later" if pending). Clicking opens
  the full-size image in a new window. <!-- Visual summary chat: PRIVATE-URL -->

Include links from the transcript at the appropriate places as follows:
<!-- One line per item. Prefixes: LINK / EMBED / IMAGE / DO NOT LINK but mention.
     Private chat URLs go in HTML comments; give the share link or a local .md copy. -->

- LINK: TITLE — URL
- EMBED: TITLE — URL
- LINK: chats as required — open in a popup and render as HTML.
- DO NOT LINK but mention: `forms.s-anand.net/SLUG/` — the form I used to collect responses;
  I disabled it after the session.

Key points I took away — incorporate these, finding supporting (and contradictory) evidence
in the transcript and sources:

- TAKEAWAY-1
- TAKEAWAY-2

This will be deployed at https://sanand0.github.io/talks/YYYY-MM-DD-slug/

--- <!-- Optional: landing page when there are multiple sub-pages -->

Create a landing page at YYYY-MM-DD-slug/index.html with centered cards (title + brief
description) linking to: story.html — the narrative story; OTHER.html — description.
(I might add more cards later.)

--- <!-- Optional: attendee email -->

I'm emailing the attendees (and some non-attendees). Link to the talk page(s) and briefly
mention the most important thing(s) they should remember and practice. Draft the email in my
writing style.

--- <!-- Corrections: append after reviewing the draft -->

- Transcript/quote corrections: "QUOTE" was said by X, not Y. Fix in the HTML and transcript.
- Design fixes: SELECTOR has low contrast / needs margin / etc. Find similar issues and fix them.

<!-- claude --resume SESSION-ID --dangerously-skip-permissions -->

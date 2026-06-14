# Prompts

## Talk summary, 14 Jun 2026

<!--
cd ~/code/talks/
dev.sh -p ~/code/,~/r2/media
claude --dangerously-skip-permissions --model opus --effort high
-->

Generate a beautiful narrative story about this 2-hour AI Workshop [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted at
[Paradox](https://www.iitmparadox.org/workshops) for the [BS students at IITM](https://study.iitm.ac.in/ds/)
on 12 Jun 2026 (2-4 pm IST) at [DOMS](https://doms.iitm.ac.in/) Room 101.

Generate a beautiful narrative story about this workshop as 2026-06-12-let-ai-take-your-exam/story.html (not index.html).

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use the following as examples to follow LOOSELY, not strictly:

- 2026-05-23-iim-ai-unboxed-context-engineering/index.html
- 2026-04-30-harvard-education/index.html
- 2026-04-08-ai-workshop-lbsnaa/index.html

Use the talk transcript and the main content source. It's at 2026-06-12-let-ai-take-your-exam/transcript.md.
You may also read any other relevant content to weave into the narrative.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.

Make sure the design is engaging. Allow visual elements (e.g. comic page, videos, embedded content, etc.) to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc.

Add the top takeways from the talk at the end.

Prominently include these:

- embed the video near the top: `<video controls preload="metadata" width="100%"><source src="https://media.s-anand.net/2026-06-12-let-ai-take-your-exam.webm" type='video/webm; codecs="vp9, opus"'></video>` in a full width container.
- link to the transcript near the top - it should open in a popup and render as HTML.
- embed the audio near the top: https://github.com/sanand0/talks/releases/download/talks/2026-06-12-let-ai-take-your-exam.opus
- include the invitation poster at an appropriate place: `https://files.s-anand.net/images/2026-05-18-let-ai-take-your-exams.avif` - clicking on it should open the full-size image in a new tab

Include these links as part of the narrative at the right places:

- ChatGPT conversation: "Okay, I'm trying to figure out the ROI of an AI subscription for a student, and I don't really know ...": https://chatgpt.com/share/6a2e44a1-8494-83ec-88c6-78f2f7790a14 <!-- https://chatgpt.com/c/6a2bc74d-f648-83ec-a55d-b74c1abbbcd7 -->
- Link to my WhatsApp scraper tool: https://tools.s-anand.net/whatsappscraper/
- Embed my LLM evaluations - specifically dealing with hallucinations by double-checking: https://sanand0.github.io/llmevals/double-checking/. The specific chart I spoke of is at https://sanand0.github.io/llmevals/double-checking/improvement.webp - embed it.
- Embed my evaluation of LLMs doing multiplication: https://sanand0.github.io/llmmath/
- Embed my LLM pricing scrollytelling: https://sanand0.github.io/llmpricing/
- Link to my "Compare Models" prompt: https://github.com/sanand0/blog/blob/a0d641d46a689295cd2c7a451406f92d2aefc5b4/pages/prompts/fragments.md#compare-models
- Link to my Generative AI group podcast: https://github.com/sanand0/generative-ai-group/
- Link to my talks page: https://sanand0.github.io/talks/ - which features
- Link to my AI-era capability test that I had Codex solve in the background: https://exam.sanand.workers.dev/2026-06-test - and here is a screenshot with it scoring 9/10: 2026-06-12-let-ai-take-your-exam/exam-results.avif.
  - Link to the ChatGPT conversation where I copied and pasted a question from this quiz into ChatGPT, which I pasted back and it worked: https://chatgpt.com/share/6a2e4acb-d3d4-83ec-9460-abd94d04ac6f <!-- https://chatgpt.com/c/6a2bc942-ee58-83ec-99bf-c585d5fbfd5e -->
  - FYI: The exam source is a ~/code/exam/src/exam-2026-06-test.js and associated q-\* questions. It may not be relevant.
- Link to my AI-era skills advice: https://www.s-anand.net/blog/ai-advice/#what-skills-should-i-learn
- Link to my analysis of the survey results: https://chatgpt.com/share/6a2e709c-9f74-83ec-b02d-d02e35c03ef6 - which is also copied to 2026-06-12-let-ai-take-your-exams/survey-analysis-chatgpt.md - allow this as a popup converted to HTML.

DO NOT LINK TO, but feel free to use details of the question difficulties for my course are at ~/code/exam/dumps/difficulty.md. I've mentioned this in the talk.

DO NOT LINK to, but mention, `forms.s-anand.net/aiexam/` as the form I used to collect responses. The link will only work when I enable it - and I disabled it after the exam.
DO go through the analysis in 2026-06-12-let-ai-take-your-exams/survey-analysis-chatgpt.md and weave all insights into the narrative.
The questions/responses are at `~/code/liveform/forms/aiexam/{form.yaml,responses.tsv}` - you may use that for further analysis and include insights from it, but do not link to it directly.

If you think it'll help, you may take screenshots of `~/r2/media/2026-06-12-let-ai-take-your-exam.webm` which has timestamps that can sometimes deviate by as much as 2 minutes from the transcript. Transcript timings for the last setion of the transcript - after the last `---` are offset by about 1h42m. But do this if you really think it necessary and can do it efficiently.

Here's how to include the links:

- Make sure ALL links mentioned above are included at the right places (e.g. in the narrative, captions, cards, etc.)
- Include images with a caption. The image and caption should link to the associated link (if present), else open the image in a new tab.
- When embedding websites, include them as IFRAMEs in a full-width container, slightly less than 100vh, with a caption linking to the source.

Search online and LIBERALLY add inline link to material relevant to the narrative - that are mentioned (directly or indirectly) in the workshop, as well as any material that can provide useful context to the reader.

Feel free to add tooltips and popups as informative and engaging aids.

- **Tooltips** are for: Context about non-obvious terms or phrases (only if relevant and useful); Additional context about references (where possible)
- **Popups** are for: Citations: Search for and include references; Cite the key point from the reference and link to it. Supporting material: Provide extensive context, quotes, external references, etc.

This will be deployed at https://sanand0.github.io/talks/2026-06-12-let-ai-take-your-exam/

Use sub-agents as required for token efficiency (e.g. with Haiku, reducing context), planning (e.g. with Opus), etc.

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, break this into parts, generating the .html in chunks or layered edits (keeping each chunk small) and saving it, checking it, then updating it with the next iteration, and so on.

--- <!-- #TODO -->

Create a landing page for this talk at 2026-06-12-let-ai-take-your-exam/index.html. Include the following cards, centered, with a title and brief description, linking to the respective content:

- story.html - the narrative story of the talk
- codex.html - how Codex solved the test exam in the background, and what the session logs reveal about students' questions and hesitations about using AI coding agents like Codex to solve problems.
- techniques.html - a collection of exam-taking techniques that I originally planned to drive the talk with, but didn't end-up using, but still useful for students
- preparation.md - how I ideated and prepared for this talk. Render as HTML in a popup. Link to https://chatgpt.com/share/6a2e4cc2-f5f0-83ec-9ecd-17594b744aec <!-- https://chatgpt.com/c/6a2b746c-addc-83ec-aea0-144b1ff0f025 -->

(I might add more cards later.)

Update README.md to include this talk in the list of talks.

---

I'm emailing the attendees (and some non-attendees). I want to link to the talk page(s) and briefly mention the most important thing(s) they should remember and practice. Draft the email for me in my writing style.

<!-- claude --resume d21905c8-9be6-44c4-929b-1d6765387b40 --dangerously-skip-permissions -->

## Codex Analysis, 14 Jun 2026

<!--
cd ~/code/talks/
dev.sh -p ~/r2/files/blog/2026-06-12-let-ai-take-your-exams/,~/code/exam/
claude --dangerously-skip-permissions --model opus --effort medium
-->

Write `2026-06-12-let-ai-take-your-exams/codex.html`, a companion story to `2026-06-12-let-ai-take-your-exams/story.html`, documenting how Codex solved <https://exam.sanand.workers.dev/2026-06-test>

Both Jaideep and I tried solving it.

- ~/r2/files/blog/2026-06-12-let-ai-take-your-exams/ has Jaideep's solution using Codex on his ChatGPT Pro account. It got 10/10
- ~/.codex/sessions/2026/06/12/rollout-2026-06-12T14-48-26-019ebb20-24f9-7ea2-b13c-17c49fd40308.jsonl has my Codex solution my ChatGPT Plus account. I interrupted it after 9/10 because I was eating into my credits.
- ~/code/exam/src/exam-2026-06-test.js has the source of the exam questions. Inspect the q-*.js in the same folder for the question details and solutions.

ChatGPT analyzed it. The analysis is at `2026-06-12-let-ai-take-your-exams/codex-analysis-chatgpt.md`. You can show that as a popup rendered in HTML and link to https://chatgpt.com/share/6a2e7d02-ce58-83ec-9919-a2828e846b83 <!-- https://chatgpt.com/c/6a2e7ab3-e340-83ec-9420-04b9cfc3e20b -->

Write the Codex story in the same style and design as the main story (see `2026-06-12-let-ai-take-your-exams/prompts.md` for further input) that answers these questions:

- How did Codex solve the questions? Did it make mistakes? If so, how did it recover?
- Based on the transcript at `2026-06-12-let-ai-take-your-exams/transcript.md` what are the questions / hesitations students have in their minds about using AI coding agents like Codex to solve the problem, and what do the session logs reveal in response to those questions / hesitations?

--- <!-- steering -->

Make sure you put in plenty of examples. Syntax-highlight code as required.

--- <!-- steering -->

Calculate and prominently mention the API cost.

---

Make the .qcard elements collapsible. They are too detailed. By default, they're collapsed, and show just the .qcard-head and .verdict but clicking anywhere on the cards toggles them and it's clear that they're toggle-able.

<!-- claude --resume c0ce9366-e339-404c-a2f8-84821465fb33 --dangerously-skip-permissions -->

## Techniques, 08 Jun 2026

<!--
cd /home/sanand/code/talks/2026-06-12-let-ai-take-your-exams/
dev.sh -p ~/code/
claude --dangerously-skip-permissions --model opus --effort medium
-->

Modify `techniques.html` - which was designed for a different `techniques.jsonl` format - to work with the current `techniques.jsonl`. Specifically:

- There is no `n`. Either add it to `techniques.jsonl` or modify the code to work without it.
- Use "category" instead of "stage". setting" is an additional tag.
- Use "steps" instead of "move".
- "provenance" and "try_it" are unused. "learn_instead" is used.
- etc.

Read `claude-chat.md` to understand the context and how `techniques.jsonl` was generated.

Modify the title and any other framing appropriate to the context - but the rest of the _functionality_ in `techniques.html` (no label-overlap, tour, hover tooltip, brush, popup on click, URL state, light/dark mode, ...) should be preserved and adapted to the new format.

Ensure that the points are spread out. The values are subjective - you can edit the impact and ease values to make them distinguishable, as long as you are convinced that the relative ordering is correct.

Go through the content in "techniques.jsonl". Will a layman understand it, standalone? For example, "A constrained format that travels on social and survives print" isn't as clear as "A fixed format can be repeatedly used on print and social media as a recurring series". Revise the tagline, move, why, try_it, watch_for and examples.context in `techniques.jsonl` where required to make it simple and clear for a layman.

---

Rewrite `techniques.jsonl` to remove & avoid LLM smells.

- Write plainly. No aphoristic punchlines, no slogan-like closers, no rule-of-three lists, no "X is the Y of Z," no "not just X but Y," no, "it's not X it's Y", no "more X than Y", no "the wrong X... the right one is Y", no "honest/genuine X", no "X matters", no excessive bullets, no em-dash or unicode.
- Vary sentence length: don't stack short ones for effect.
- Use my wording and examples where possible.

Find more examples of these 30 techniques as you can from ~/code/exam/ or ~/code/blog/ (or ~/Documents/notes/transcripts/ or ~/Documents/claude/).
Include them only if they're apt and absolutely spot-on as an exemplar for that technique - and make sure that comes through when you write the "context" for each example.

---

In the "Solve - Study - Verify" legend row, also add filters for "Open book OK", "Endorsed" and "Demo only".
Drop the "Delegate to AI, then keep what AI can't do:".

---

Where you are linking to an exam/q\*.js, instead, find the exam that uses it and link to that. For example, `q-axis-scale-manipulation-repair.js` is used in ~/code/exam/src/exam-tds-2026-01-ga7.js - so you can link to <https://exam.sanand.workers.dev/tds-2026-01-ga7#q-axis-scale-manipulation-repair>.

<!-- claude --resume 27e30390-48d5-47d5-9aaf-dddabed9a94f --dangerously-skip-permissions -->

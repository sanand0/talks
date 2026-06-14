# Prompts

## Data story, 14 Jun 2026

<!--
cd ~/code/talks/
dev.sh -p ~/code/,~/r2/media,~/Documents/chatgpt/
claude --dangerously-skip-permissions --model opus --effort high
-->

Generate a beautiful narrative story about this 2-hour AI Workshop [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, conducted online for data journalists and designers on 13 Jun 2026 (3-5 pm IST). This was organized by [Rohit Saran](https://www.linkedin.com/in/rohitsaran/), Managing Editor of The Times of India.

Create this as 2026-06-13-data-stories-with-ai/story.html (not index.html).

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use the following as examples to follow LOOSELY, not strictly:

- 2026-06-12-let-ai-take-your-exams/story.html
- 2026-05-23-iim-ai-unboxed-context-engineering/index.html
- 2026-04-30-harvard-education/index.html

Use the talk transcript and the main content source. It's at 2026-06-13-data-stories-with-ai/transcript.md.
You may also read any other relevant content to weave into the narrative.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.

Make sure the design is engaging. Allow visual elements (e.g. comic page, videos, embedded content, etc.) to expand beyond the width of the main content column, even to full width, and use a different background color for these elements to make them pop, etc.

Add the top takeways from the talk at the end.

Prominently include these:

- embed the video near the top: `<video controls preload="metadata" width="100%"><source src="https://media.s-anand.net/2026-06-13-data-stories-with-ai.webm" type='video/webm; codecs="vp9, opus"'></video>` in a full width container.
- link to the transcript near the top - it should open in a popup and render as HTML.
- embed the audio near the top: https://github.com/sanand0/talks/releases/download/talks/2026-06-13-data-stories-with-ai.opus
- include the invitation poster at an appropriate place: `https://files.s-anand.net/images/2026-06-08-data-stories-with-ai-poster.avif` - clicking on it should open the full-size image in a new tab

Include these as part of the narrative at the right places:

- Link to the Gramener Mahabharatha visualization Rohit mentioned: https://gramener.com/mahabharatha/
- Link to the IMDb movies page Anand uses as a personal movie selector that Rohit mentioned: https://sanand0.github.io/imdb/
- Link to the Times of India Hack of the Day page: https://timesofindia.indiatimes.com/technology/hack-of-day
- Link to Anand's AI generated Hack of the Day page: https://sanand0.github.io/journalists/hackoftheday/
  - Embed a Hack of the (Day as an example) at 2026-06-13-data-stories-with-ai/hack-of-the-day-121.html
- Extract excerpts from `~/Documents/chatgpt/Hack of the Day Format.md` to explain and support how the Hack of the Day cards were developed
- Embed my evaluation of LLMs doing multiplication: https://sanand0.github.io/llmmath/
- Link to my testing of LLM arithmentic capabilities: https://chatgpt.com/share/6a2ecfa2-bd2c-83ec-bcaf-a6fd7a97d74e - and include excerpts from `2026-06-13-data-stories-with-ai/llm-arithmetic-demonstration-chatgpt.md` <!-- https://chatgpt.com/c/6a2d2a39-8d20-83ec-be15-93132c744f07 -->
- Link to my discovery of interesting datasets and include excerpts at the relevant places. There may be some interesting elements in the responses - include what enhances the story.
  - https://chatgpt.com/share/6a2ed033-5a9c-83ec-8b4f-4a594d52b5fb = `2026-06-13-data-stories-with-ai/dataset-ideation-chatgpt.md` <!-- https://chatgpt.com/c/6a2d2bf8-f1a0-83ec-9015-056a5af58da7 -->
  - https://claude.ai/share/6b22af52-cefb-4dd9-9b0f-50a6c2b4799c = `2026-06-13-data-stories-with-ai/dataset-ideation-claude.md` <!-- https://claude.ai/chat/e1266d92-1121-410b-b584-3efc904fd7bc -->
  - https://chatgpt.com/share/6a2ed103-3d30-83ec-85d9-50237af26622 = `2026-06-13-data-stories-with-ai/dataset-ideation-2-chatgpt.md` <!-- https://chatgpt.com/c/6a2d2c92-8bf4-83ec-b7f3-b6f4597b3588 -->
- Link to the India NCAP dataset from where I downloaded the CSVs: https://urbanemissions.info/india-air-quality/india-ncap-aqi-indian-cities-2015-2023/
- Link to the Dataful Vahan data I purchased for Rs 299: https://dataful.in/datasets/21577/ (but it was too small and I didn't use it)
- Link to the Air Quality Index dataset ZIP I had Claude download and shared with the audience: https://files.s-anand.net/blog/2026-06-13-data-stories-with-ai/aqi.zip
- Link to publicly accessible shares by the audience on `~/code/liveform/forms/aistories/responses.tsv` after you confirm that you can access them
- Link to the Air Quality Insights ChatGPT generated: https://chatgpt.com/share/6a2d3460-2c70-83ec-b419-94e997da6bb9 = `2026-06-13-data-stories-with-ai/air-quality-insights-chatgpt.md` <!-- https://chatgpt.com/c/6a2d30d7-a100-83ec-b29b-3f77a37c2a58 -->
  Embed the Air Quality Index page ChatGPT generated. https://chatgpt.com/share/6a2d3b0b-cf58-83ec-98ad-7d918b7a9dab = `2026-06-13-data-stories-with-ai/audience-data-insights-chatgpt.md` <!-- https://chatgpt.com/c/6a2d3145-c9d4-83ec-91b3-ccfac86de4ed -->
  - 2026-06-13-data-stories-with-ai/aqi.html - first version
  - 2026-06-13-data-stories-with-ai/aqi2.html - includes Ghaziabad
- Embed the air quality index comic strip ChatGPT generated: 2026-06-13-data-stories-with-ai/aqi-comic.avif <!-- https://chatgpt.com/c/6a2d37a4-85ac-83ec-b96a-b547282f0b99 -->
- Embed the "unlivability calendar" that Narendra shared: 2026-06-13-data-stories-with-ai/unlivability-calendar.avif (rows = cities, columns = months, color = unlivability index) - we discussed this a fair bit
- Link to the Olmo Earth analysis Varun talked through: https://pythonicvarun.github.io/olmoearth-change-insights/
  - If you can go through the contents and include images of then vs now, and link them (like the page above does), that'll be great
- Embed my LLM Art Style: https://sanand0.github.io/llmartstyle/?category=text2
- Embed my LLM pricing scrollytelling: https://sanand0.github.io/llmpricing/

DO NOT LINK to, but mention, `forms.s-anand.net/aistories/` as the form I used to collect responses. The link will only work when I enable it - and I disabled it after the exam.
DO go through the analysis in 2026-06-13-data-stories-with-ai/survey-analysis-chatgpt.md and weave all relevant insights into the narrative. <!-- https://chatgpt.com/c/6a2edfc9-d3f4-83ec-954f-8526faffa0fc -->
The questions/responses are at `~/code/liveform/forms/aistories/{form.yaml,responses.tsv}` - you may use that for further analysis and include insights from it, but do not link to it directly.

Here's how to include the links:

- Make sure ALL links mentioned above are included at the right places (e.g. in the narrative, captions, cards, etc.)
- Include images with a caption. The image and caption should link to the associated link (if present), else open the image in a new tab.
- When embedding websites, include them as IFRAMEs in a full-width container, slightly less than 100vh, with a caption linking to the source.

Search online and LIBERALLY add inline link to material relevant to the narrative - that are mentioned (directly or indirectly) in the workshop, as well as any material that can provide useful context to the reader.

Feel free to add tooltips and popups as informative and engaging aids.

- **Tooltips** are for: Context about non-obvious terms or phrases (only if relevant and useful); Additional context about references (where possible)
- **Popups** are for: Citations: Search for and include references; Cite the key point from the reference and link to it. Supporting material: Provide extensive context, quotes, external references, etc.

This will be deployed at https://sanand0.github.io/talks/2026-06-13-data-stories-with-ai/

Use sub-agents as required for token efficiency (e.g. with Haiku, reducing context), planning (e.g. with Opus), etc.

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, break this into parts, generating the .html in chunks or layered edits (keeping each chunk small) and saving it, checking it, then updating it with the next iteration, and so on.

---

Create a landing page for this talk at 2026-06-13-data-stories-with-ai/index.html. Include the following cards, centered, with a title and brief description, linking to the respective content. (Similar to 2026-06-12-let-ai-take-your-exams/index.html)

- story.html - the narrative story of the talk
- techniques.html - a collection of exam-taking techniques that I originally planned to drive the talk with, but didn't end-up using, but still useful for students
- techniques.md - how I ideated and prepared techniques.html. Render as HTML in a popup. Link to https://claude.ai/share/15d507c1-df0e-4136-888d-5336abb25b0e <!-- https://claude.ai/chat/0222a4e5-7aa3-430b-8d56-3bca7a707edf -->

(I might add more cards later.)

Update README.md to update relevant links.

Also, I'm emailing the attendees (and some non-attendees). I want to link to the talk page(s) and briefly mention the most important thing(s) they should remember and practice. Draft the email for me in my writing style.

<!-- claude --resume abdc6d31-8123-4b1f-858f-45c0d59195db --dangerously-skip-permissions -->

## Initial draft, 07 Jun 2026

<!--
cd /home/sanand/code/talks/2026-06-13-data-stories-with-ai
dev.sh -p ~/code/
claude --dangerously-skip-permissions --model claude-opus --effort medium
-->

Create a `techniques.html` that will fetch and render `techniques.jsonl`.

Read `claude-chat.md` to understand the context and how `techniques.jsonl` was generated.

I want `techniques.html` to fit on a single page and show all the techniques on a scatter plot with impact on the Y axis and ease on the X axis.

Ensure that the points are spread out. The values are subjective - you can edit the impact and ease values to make them distinguishable, as long as you are convinced that the relative ordering is correct.

Label the quadrants with large light/subtle text in the background. Top-left is "Moonshots". Top-right is "Quick Wins". Bottom-left is "Time sinks". Bottom-right is "Small wins".

Color them based on the "stage". Add a legend showing which color corresponds to which stage. The legend should be styled like a workflow. Hovering on a legend should highlight the points of that stage and fade out the others. Clicking on a legend item should persist the highlight. Clicking on multiple legend items should allow selecting multiple stages. Allow clearing the selection to show all points again.

If possible, label the points with the technique name in a way that avoids label overlap. Move labels intelligently to ensure they do not overlap. It's OK not to show some labels if there are too many points, but show as many as possible without overlap. The labels should be styled nicely and be easy to read.

When hovering over a point, show a tooltip with the technique name, tagline, and stage (colored). The tooltip should be styled nicely and be easy to read.

When brushing a region, open a popup that shows the selected techniques, mentioning their name, tagline, and stage (colored). The popup should be scrollable if there are many techniques.

When clicking on a point or the technique in the popup, open a sidebar that shows the full details of the technique, including the description and example. The sidebar should be well-designed and easy to read. For links to files, point to GitHub. For example, `~/code/journalists/prompts.md` -> `https://github.com/sanand0/journalists/blob/main/prompts.md`. Where possible, link to specific sections as a permalink, for example: `https://github.com/sanand0/journalists/blob/cdfa61e0a1854b56c1aa83d283f7286512186147/prompts.md#statnostics-2-mar-2026` for the `source-sweep` technique where we mention "In the section 'Statnostics, 2 Mar 2026 -> Find stories via Codex'...".

Preserve the state of the brushing, legend selection, and sidebar selection in the URL so that it can be shared. Use #?key=value&key=value...

Ensure that the colors look good on dark AND light mode, the app can be used on mobile AND desktop, and the layout is responsive.

---

Change the title to "Data Stories with AI - Technique Atlas". Drop the subtitle.
Remove the .lcap "Find → … → Orchestrate" -- this is obvious.

On hover and brush, also show "Why it works".

Go through the content in "techniques.jsonl". Will a layman understand it, standalone? For example, "A constrained format that travels on social and survives print" isn't as clear as "A fixed format can be repeatedly used on print and social media as a recurring series". Revise the tagline, move, why, try_it, watch_for and examples.context in `techniques.jsonl` where required to make it simple and clear for a layman.

Find more examples of as many techniques as you can from ~/code/journalists/ or ~/code/datastories/ (or ~/Documents/chatgpt/ or ~/Documents/claude/ - which are dumps of some of my older chats).
Include them only if they're apt and absolutely spot-on as an exemplar for that technique - and make sure that comes through when you write the "context".

Also, create a "Tour" that guides the user through the techniques. Don't pick all the techniques. Just a sequence of the 1-2 most powerful techniques for each stage. Make sure you show progress along the tour, allow the user to use the keyboard to navigate without clashing with other keyboard usage (e.g. for scrolling), make the next / previous buttons easy to see and click, ensure that it will look and work well on mobile.

<!-- claude --resume eb5216a1-8b16-4bcd-9255-81822ca5bf7a --dangerously-skip-permissions -->

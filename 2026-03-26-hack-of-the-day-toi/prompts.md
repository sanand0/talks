# Prompts

<!--

dev.sh -v /home/sanand/code/journalists/:/home/sanand/code/journalists/:ro

-->

## Story v1, 26 Mar 2026 (claude --enable-auto-mode - Sonnet 4.6 medium)

Generate a beautiful narrative story about the work [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, did with [The Times of India](https://en.wikipedia.org/wiki/The_Times_of_India) in March 2026 to automate some of their journalistic processes using LLMs.

Create this as 2026-03-26-hack-of-the-day-toi/index.html

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use 2026-02-11-amat-dt-day/index.html, 2025-12-06-mining-digital-exhaust/index.html and 2026-01-11-nptel-vibe-coding-workshop/index.html as examples - to follow LOOSELY, not strictly.

Use 2026-03-26-hack-of-the-day-toi/transcript.md. This is long and detailed - and has rich material!

It's broken into sections, each level 1 heading (`#`) being a conversation [Anand](https://www.s-anand.net/) had with the Times of India team:

- [Rohit Saran](https://www.linkedin.com/in/rohitsaran/), Managing Editor
- [Saurabh Banerjee](https://x.com/bansaurabh), Editor
- [Saikat Dasgupta](https://www.linkedin.com/in/saikat-dasgupta-1180b797/), Editor
- [Sajeev Kumarapuram](https://www.linkedin.com/in/sajeev-kumarapuram-205ba933/), Visual Journalist

Based on this, Anand created a series of content. (The calls discussed this content and more.)

- See /home/sanand/code/journalists/ to understand the code. (Review git history if required. Certaily glance through the prompts.md files.)
- This is published at http://sanand0.github.io/journalists/ - especially https://sanand0.github.io/journalists/hackoftheday/

On 20 Mar 2026, the first of these "Hack of the Day" stories was published:

[![Show Gemini your screen or camera for live help :http://toi.in/l3xRob](https://pbs.twimg.com/media/HD0_dtbboAMrZZW?format=png&name=small)](https://x.com/timesofindia/status/2034925416444829727?s=20)

and was followed by:

[![Free up space without deleting your apps: http://toi.in/mddDqa](https://pbs.twimg.com/media/HEJqHOQaIAM6aAA?format=webp&name=small)](https://x.com/timesofindia/status/2036321109831041376?s=20)

[![Check your #Aadhaar authentication history: http://toi.in/hpRluZ](https://pbs.twimg.com/media/HEOxKZqbQAAb0kr?format=webp&name=small)](https://x.com/timesofindia/status/2036707153512403193?s=20)

[![File your EPFO e-nomination now http://toi.in/JnpoIa](https://pbs.twimg.com/media/HEU3gTibYAEsvsO?format=webp&name=small)](https://x.com/timesofindia/status/2037103515231752665?s=20)

More are being published, tagged [#hackoftheday](https://x.com/search?q=%23hackoftheday&src=typed_query&f=live).

As you can see from the discussions, this represents a fundamental shift in the way the Times of India creates content.

Document the story - the origins, the ideation, the process, the setbacks, the learnings, the wins, the outcomes, the future plans - in a narrative format.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.
- Include relevant images, links, prompt snippets, etc. from the code base.

Use the transcripts as primary source material, but feel free to re-structure, re-order, and re-word for better storytelling. The story should be engaging and insightful, not just a dry summary of events.

Make sure the design is engaging. Allow some elements to expand beyond the width of the main content column, and use a different background color for these elements to make them pop, etc. The sketchnote could be one such.

Add the top takeways from the talk at the end.

Prominently include the sketchnote at 2026-03-26-hack-of-the-day-toi/sketchnote.avif - clicking on it should open the full-size image in a new tab.

DO NOT link to the transcript! I will delete this later.

Search online and liberally link to any other relevant material.

Feel free to add tooltips and popups as informative and engaging aids.

**Tooltips** are for:

- Context about non-obvious terms or phrases (only if relevant and useful)
- Additional context about references (where possible)

**Popups** are for:

- Citations. Search for and include references. Cite the key point from the reference and link to it.
- Supporting material. Provide extensive context, quotes, extracts from slides, external references, etc. Render Markdown content as HTML.

This will be deployed at https://sanand0.github.io/talks/2026-03-26-hack-of-the-day-toi/

Update README.md to include this talk in the list of talks.

<!-- claude --resume 9f83725f-3df3-4d7b-9d8b-b67345f3ea83 -->

## Story v2, 26 Mar 2026 (claude --dangerously-skip-permissions - Sonnet 4.6 medium)

Generate a beautiful narrative story about the work [Anand](https://www.s-anand.net/), LLM Psychologist at Straive, did with [The Times of India](https://en.wikipedia.org/wiki/The_Times_of_India) in March 2026 to automate "Hack of the Day" - a series of short, actionable tech tips for readers - using LLMs.

Create this as 2026-03-26-hack-of-the-day-toi/index.html

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use 2026-02-11-amat-dt-day/index.html, 2025-12-06-mining-digital-exhaust/index.html and 2026-01-11-nptel-vibe-coding-workshop/index.html as examples - to follow LOOSELY, not strictly.

Use 2026-03-26-hack-of-the-day-toi/transcript.md. This is long and detailed - and has rich material! You may want to extract material related to Hack of the Day as well as the implications of AI on journalism, e.g. using sub-agents. It's broken into sections, each level 1 heading (`#`) being a conversation [Anand](https://www.s-anand.net/) had with the Times of India team:

- [Rohit Saran](https://www.linkedin.com/in/rohitsaran/), Managing Editor
- [Saurabh Banerjee](https://x.com/bansaurabh), Editor
- [Saikat Dasgupta](https://www.linkedin.com/in/saikat-dasgupta-1180b797/), Editor
- [Sajeev Kumarapuram](https://www.linkedin.com/in/sajeev-kumarapuram-205ba933/), Visual Journalist

Based on this, Anand created "Hack of the Day" (and other things, but that's relevant).

On 20 Mar 2026, the first of these "Hack of the Day" stories was published. That's an incredible outcome!!

[![Show Gemini your screen or camera for live help :http://toi.in/l3xRob](hack-of-the-day-1.webp)](https://x.com/timesofindia/status/2034925416444829727?s=20)

and was followed by:

[![Free up space without deleting your apps: http://toi.in/mddDqa](hack-of-the-day-2.webp)](https://x.com/timesofindia/status/2036321109831041376?s=20)

[![Check your #Aadhaar authentication history: http://toi.in/hpRluZ](hack-of-the-day-3.webp)](https://x.com/timesofindia/status/2036707153512403193?s=20)

[![File your EPFO e-nomination now http://toi.in/JnpoIa](hack-of-the-day-4.webp)](https://x.com/timesofindia/status/2037103515231752665?s=20)

More are being published, tagged [#hackoftheday](https://x.com/search?q=%23hackoftheday&src=typed_query&f=live).

This was generated by code at /home/sanand/code/journalists/ (feel free to review the git history - and certainly glance through the prompts.md files.) This is published at http://sanand0.github.io/journalists/ - especially https://sanand0.github.io/journalists/hackoftheday/.

As you can see from the discussions, this represents a fundamental shift in the way the Times of India creates content. The automation of journalism is a big leap forward and is a key milestone - especially for a mainstreap paper like the Times of India.

Document the story - the origins, the ideation, the process, the setbacks, the learnings, the wins, the outcomes, the future plans - in a narrative format.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.
- Include relevant images, links, prompt snippets, etc. from the code base.

Use the transcripts as primary source material, but feel free to re-structure, re-order, and re-word for better storytelling. The story should be engaging and insightful, not just a dry summary of events.

MAKE SURE THE DESIGN IS ENGAGING! Allow some elements to expand beyond the width of the main content column, and use a different background color for these elements to make them pop, etc. The sketchnote could be one such.

MAKE SURE YOU INCLUDE IMAGES LIBERALLY - you can render the /home/sanand/code/journalists/hackoftheday/template.svg with any of the cards in /home/sanand/code/journalists/hackoftheday/cards.json to generate as many images as you want to break up the text and make it more engaging.

Add the top takeways from the talk at the end.

Prominently include the sketchnote at 2026-03-26-hack-of-the-day-toi/sketchnote.avif - clicking on it should open the full-size image in a new tab.

DO NOT link to the transcript! I will delete this later.

Search online and liberally link to any other relevant material.

Feel free to add tooltips and popups as informative and engaging aids.

**Tooltips** are for:

- Context about non-obvious terms or phrases (only if relevant and useful)
- Additional context about references (where possible)

**Popups** are for:

- Citations. Search for and include references. Cite the key point from the reference and link to it.
- Supporting material. Provide extensive context, quotes, extracts from slides, external references, etc. Render Markdown content as HTML.

This will be deployed at https://sanand0.github.io/talks/2026-03-26-hack-of-the-day-toi/

Update README.md to include this talk in the list of talks.

<!-- claude --resume 24f3cdfd-9e34-466a-82f0-869898e62e3b -->

## Sketchnote

<!-- Gemini Pro - https://gemini.google.com/u/2/app/0ce0571156c2b189 -->

Summarize this talk transcript as a visually rich, intricately detailed, colorful, and funny, sketchnote. Think about the most important points, structure it logically so that the sketchnote is easy to follow, then draw it.

<!--
- Ideation: https://claude.ai/chat/ea04db77-c6a9-476e-be83-d0cde504669c
- Bach Faucet: https://claude.ai/chat/243b709c-e8a9-4574-a54c-77df3e0b72f2
-->

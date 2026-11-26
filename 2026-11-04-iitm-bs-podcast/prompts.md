# IITM BS Insider podcast

## Initial draft, 04 Nov 2026

<!--
cd ~/code/talks
claude --model opus --effort high
-->
<!-- Source: https://chatgpt.com/c/6b078d9c-72d0-83ec-ab5c-de8e8d376431 + Prep: https://chatgpt.com/c/6ae9fc51-8ee8-83ec-9153-d46f3cd7b0f2 + https://chatgpt.com/c/6aeaa271-6f8c-83ec-850d-a9ab123d063a -->

```markdown
Create a beautiful, distinctive, **video-driven narrative story** about the 68-minute in-person IITM BS Insider podcast interview of [Anand S](https://www.s-anand.net/), LLM Psychologist at Straive and Tools in Data Science faculty at IIT Madras, by Kusuma Komali Priya of the [IITM BS Insider podcast team](https://www.youtube.com/@iitmbsinsider/videos), at IIT Madras on 4 Nov 2026. A student joins the live exam and Q&A.

Create `2026-11-04-iitm-bs-podcast/index.html` using the talk-story skill. **Full creative and design authority belongs to you.** Choose the title, narrative arc, editorial emphasis, design, interactions and implementation yourself.

Use these completed video-driven summaries as examples. Read their actual HTML and prompts, not just their appearance. Follow them loosely:

- `2026-11-23-tds-ideation/{index.html,prompts.md}` — the most recent video-driven story.
- `2026-11-16-tds-ideation/{index.html,prompts.md}`
- `2026-11-09-tds-ideation/{index.html,prompts.md}`
- `2026-10-07-iitm-ed-data-visualization/{index.html,prompts.md}` — video-driven IITM class story.
- `2026-10-05-tds-orientation/{index.html,prompts.md}` — closely related subject and established video/story experience.

## Content

Read the complete polished `transcript.md`, the real recording, and the accompanying `story-context.md`, `research-notes.md` and `links.md`. The latter three are an evidence shelf and editorial suggestions, not a prescribed outline or design specification. Research further as useful.

The interview is itself a demonstration of TDS: the host used Claude to create her questions, Anand turns the interview around and asks how she did it, and the participants eventually attempt actual TDS problems. Make the reader experience TDS rather than merely learn about it. A possible central question is: **What should we teach humans when we can teach agents the same thing?**

In particular, look for the striking and funny moments, the examples of changing questions and discovering blind spots, the recursive argument about teaching humans to use agents, class gossip as information, learning from auditors, the tension between collaboration and individual learning, the failed agent at Paradox, and the live mini-exam's model-benchmarking and Japanese instructions. The concluding conversation about personal software and delegation is also worth exploring. Use the video as evidence throughout.

Distinguish events observed in this recording, anecdotes about earlier events, research findings and planned activities. The NCERT findings are associations, not causal effects. There are no saved podcast exam scores in the local archive; don't confuse the earlier Paradox scores with this exam. Verify significant quotations, names and timestamps. Use the linked sources where they add value, and do not expose private preparation material or student identifiers. Review personal and corporate digressions before quoting them. Feel free to include experiences or interactions that make the ideas clearer, if warranted by the story.

## Media

- **Video:** https://media.s-anand.net/2026-11-04-iitm-bs-podcast.webm — public, checked 26 Nov. Local master: `~/r2/media/2026-11-04-iitm-bs-podcast.webm`. 4060.335 s (67:40), 1920×1080 AV1 + Opus. Remote server supports byte ranges but returns `audio/webm`, like several earlier videos; test actual video playback and seek as in the reference summaries.
- **Audio:** https://github.com/sanand0/talks/releases/download/talks/2026-11-04-iitm-bs-podcast.opus — uploaded; duration 4060.327 s.
- **Transcript:** `transcript.md` uses continuous recording-relative timestamps. The interview runs until 48:14; the live mini-exam and Q&A follow. Use the real video to refine anchors as needed. No embedded subtitle stream in the video; create captions from the recording/transcript if useful.
- No separate official YouTube episode URL, slides or comic supplied.

Follow the quality and functionality of the video-driven references and the talk-story skill, including actual playback, timestamp seeking, deep links and mobile behavior. The story should work as a coherent reading and viewing experience.

The eventual URL is https://talks.s-anand.net/2026-11-04-iitm-bs-podcast/. Update the talk catalog as appropriate after QA. Create the page and necessary supporting assets only; no commit, push or deployment unless asked.
```

When focusing on the video, some of the wider content, e.g. .exch, .say, .bio, etc. that spill over to the left and right of the content, gets cut off on the left and right.
When focusing on the video, I'm not able to scroll the `#chapters li` elements to see the chapters. When my screen isn't tall enough, I can see the chapters at the top but have no way of scrolling to the chapters below that, since the block seems fixed on the screen.
Fix and fix any similar issues.

<!-- claude --resume 894cb793-b01a-4684-b74f-ffae69b25ffd -->

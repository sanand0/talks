# Prompts

<!--

cd ~/code/talks
dev.sh
codex --yolo --model gpt-5.4 --config model_reasoning_effort=xhigh

-->

## Workshop activities, live exercises, 08 Apr 2026

Find out what live activities I did or had the audience perform in each of these talks.

Every talk is a folder. I have identified the Markdown slides in each folder (typically a README.md) and/or the transcript of my talk (transcript.md), sometimes both.

For each folder, create an activities.md (e.g. 2024-10-19-ai-in-education-webinar/activities.md) that specifically lists what I did or what the audience did **using AI**.

For each activity:

- Mention WHO did the activity - audience or speaker.
- Mention WHEN they did the activity - during or before the talk.
- Mention MODEL/TOOL used when possible - e.g. ChatGPT, Codex, Claude, GitHub Copilot, NotebookLM, etc.
- CITE the source - verbatim line from the source that I can search for to verify this

Here are the only files you need to do read for this exercise.

2024-10-19-ai-in-education-webinar/README.md
2025-01-18-how-to-use-ai-to-generate-code/README.md
2025-05-10-vibe-coding/README.md
2025-06-27-data-design-by-dialogue/README.md
2025-06-27-data-design-by-dialogue/transcript.md
2025-06-28-prompt-to-plot/README.md
2025-06-28-prompt-to-plot/transcript.md
2025-06-pycon-sg/README.md
2025-06-pycon-sg/llm-cli.md
2025-07-13-goodbye-mba-hello-ai/README.md
2025-07-13-goodbye-mba-hello-ai/transcript.md
2025-07-18-tug-true-but-irrelevant-rob-schrauwen/transcript.md
2025-07-23-supply-chain-automl/README.md
2025-07-23-supply-chain-automl/transcript.md
2025-07-24-pugs-agent-loop/README.md
2025-08-11-social-code-analysis/README.md
2025-08-11-social-code-analysis/transcript.md
2025-08-21-ai-coding-guide/README.md
2025-08-21-rip-data-scientists/README.md
2025-08-21-rip-data-scientists/transcript.md
2025-09-13-duckdb-is-the-new-pandas/README.md
2025-09-15-llm-ama-gale/README.md
2025-09-16-vibe-analysis/README.md
2025-09-18-llm-ama-bi-worldwide/README.md
2025-09-21-making-open-data-useful/README.md
2025-09-22-llm-trends/README.md
2025-09-22-llm-trends/transcript.md
2025-09-llm-workflows/README.md
2025-10-16-vibe-analysis/README.md
2025-10-23-vibe-coding/README.md
2025-10-29-llm-data-visualization/README.md
2025-11-06-llm-psychology/README.md
2025-11-15-applied-vibe-coding/README.md
2025-11-15-applied-vibe-coding/transcript.md
2025-12-03-vibe-analytics-iim-alumni-sg/transcript.md
2025-12-05-scdm-keynote/README.md
2025-12-05-scdm-keynote/transcript.md
2025-12-06-mining-digital-exhaust/transcript.md
2026-01-11-nptel-vibe-coding-workshop/transcript.md
2026-01-20-agentic-ai-in-action-deloitte/transcript.md
2026-02-11-amat-dt-day/transcript.md
2026-02-26-vibe-coding-for-humanities-ashoka/transcript.md
2026-03-12-nie-ai-roadmap/transcript.md
2026-03-15-pyconf-ai-in-sdlc/transcript.md
2026-03-18-iitm-academic-council/transcript.md
2026-03-18-iitm-office-of-institutional-advancement/transcript.md
2026-03-18-verifiable-agents/transcript.md
2026-03-21-design-in-the-age-of-infinite-generativity/transcript.md
2026-03-21-faculty-ai-transformation-nie/transcript.md
2026-03-26-hack-of-the-day-toi/transcript.md
2026-04-06-innovation-as-a-frontier-straive/transcript.md

Plan to do this EFFICIENTLY. Use sub-agents as required.

Do this for 3 diverse folders and pause to ask for my input on style and content.

---

Ensure that the title is `# Activities`. No description required below that.
The document should JUST be a ordered list of unordered lists like this:

```markdown
1. **(clear activity description in bold)** e.g. **Create the opening interactive visualization in Claude**
  - Who: [speaker|audience]
  - When: [before|after] the talk
  - Model/tool: ...
  - What happened: ...
  - Source:
    > ... (verbatim)

2. ...
```

Rewrite existing files accordingly. Run this EFFICIENTLY for all folders.

After completing for the folders I listed based on the files I mentioned in my previous chat, synthesize into a single analysis/activities.md that lists the different kinds/categories of activities and when I performed these. This should be a single list with sub-list elements mentioning exactly the same top-level activity descriptions that were present in the individual activities.md, along with filename. For example:

```markdown
- Use voice to prompt an LLM instead of typing
  - 2026-06-28-prompt-to-plot/activities.md: Use ChatGPT by voice to find a dataset for the workshop
  - ...
- ...
```

---

Document this conversation so that we can learn from it and do better next time.

- List decisions you made independently (without me telling you to), with reason, and rejected alternatives.
- List what worked well, with examples.
- List problems faced: failures, inefficiencies and mis-alignments (my corrections, your shortcuts, following letter not spirit). Suggest pragmatic & safe fixes (if any) to prompts, skills, tools, environment, at a root cause level (resolving **such classes/patterns of problems**, not just a specific instance).
- Share a single prompt that can re-do such analysis more effectively instead of the conversation we had.

Save this in `analysis/activities.post-mortem.md` mentioning today's date.

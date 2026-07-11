Turn what this experiment learned into a SKILL.md — a reusable instruction file for AI agents.

WHAT A SKILL.MD IS (in case you don't know): an open-standard Markdown file that teaches any AI agent a repeatable workflow. Format: a folder named after the skill containing SKILL.md, which starts with YAML frontmatter (`name:` and `description:`), then Markdown instructions in imperative form. Optional: a scripts/ folder for deterministic steps. Agents see only the description until the skill triggers, then load the body — so the description decides whether the skill ever gets used, and the body must stay under ~200 lines.

RULES:
1. SOURCE. Use ONLY RESULTS.md and POSTMORTEM.md. Every instruction must trace to a measured result or an observed trace. No generic advice ("follow best practices", "handle errors appropriately"). If you can't cite evidence for a line, cut it.
2. SCOPE. The skill teaches ONE thing: when and how to apply the tested data-organization technique. If the result was inconclusive or negative, write that skill instead: when NOT to apply this technique, and below what scale it makes no difference.
3. BODY. Include: (a) when this applies and when it doesn't, from the difficulty-level results; (b) the transformation as concrete imperative steps, with one before/after example from the actual data; (c) a "Known failure modes" section from the post-mortem's trace clusters — what agents did wrong and what to do instead; (d) an "Evidence" block: model tested, corpus sizes, accuracy A vs B per level, tokens, n, and the one-line conclusion. Move any deterministic transformation into scripts/ and reference it.
4. DESCRIPTION. One or two sentences, under 200 characters if you can. Front-load the words a user would actually type. Say what it does, when to use it, and when not to. Err toward triggering.
5. SELF-TEST. Before finishing, simulate being a fresh agent that just triggered this skill on a new dataset. Walk the steps. Flag every point where you'd have to guess, fix those lines, and note what you fixed.

Output the complete skill folder, then a 3-line summary: what the skill claims, what evidence backs it, and what it deliberately doesn't claim.

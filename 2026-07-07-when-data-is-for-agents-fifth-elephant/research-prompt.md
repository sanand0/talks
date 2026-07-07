Research current (2026) best practices for organizing data for AI AGENTS to consume, as opposed to humans. "Data" includes: structured data (tables, JSON, schemas), documents (markdown, PDFs, web pages), code, media, folder and site organization, tool definitions and docs, tool outputs, errors, logs, metrics, and traces. EXCLUDE agent-harness artifacts (system prompts, AGENTS.md, SKILL.md, memory, permissions, hooks).

Search the web. Prefer primary sources: engineering blogs and docs from Anthropic, OpenAI, Google, and similar; standards (e.g., MCP, llms.txt); papers and benchmarks; practitioners who prepare data or APIs for agents. Mark clearly what is MEASURED evidence vs expert OPINION.

Return the TOP 10 techniques, ranked by: (impact × how often the situation occurs) × (how DIFFERENTLY you would do it for agents vs humans). Skip anything where the human and agent way match.

First, one compact ranked table:
Rank | Technique | For humans | For agents | Evidence: measured/opinion

Then one card per technique, EXACTLY this format — self-contained, under 120 words, no cross-references, so each card can be copy-pasted alone:

```markdown
### T{n}. {Short technique name}

- Type: representation (same facts, reorganized) | augmentation (adds info) | access (changes how it's fetched)
- For humans: {traditional organization}
- For agents: {organize it this way instead}
- Why: {mechanism — token budget, retrieval, trust, error recovery, ...}
- Matters when: {what should make the gap appear — corpus size, distractor density, multi-hop questions, ...}
- Testable claim: {ONE measurable sentence: "Agents do task X more
  accurately / with fewer tokens when data is B instead of A"}
- Evidence: {measured | opinion} — {1–3 links}
```

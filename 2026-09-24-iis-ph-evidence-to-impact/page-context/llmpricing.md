# LLM Pricing

URL: https://sanand0.github.io/llmpricing/

LLM Pricing

Models
Intelligence

-

Light

-

Dark

-

Auto

# LLM Pricing

## Which LLMs are the best value for money?

# LLM Pricing

The cost of LLMs is steadily falling, and the quality is rising.

A rough estimate of the cost of an LLM is
the cost per million tokens of input, mostly from LLMPriceCheck.
(Typically, inputs are the bigger component of the cost, compared to outputs.)

A rough estimate of the quality of an LLM is
the ELO score on the LMSYS Leaderboard.
(This is like the chess ELO score, but for LLMs, where people compare 2 LLMs on the same task.)

This chart shows the cost and quality of each LLM.

Some LLMs are "pareto optimal", i.e. there is no LLM better in both cost and quality.
These are shown in green 🟢 and are the best LLMs to use.

Some LLMs are "pareto suboptimal", i.e. there is no LLM worse in both cost and quality.
These are shown in red 🔴 and are the LLMs to avoid.

Last updated: 23 Aug 2026

Alternatives: ArtificialAnalysis.ai

{
const cells = d.querySelectorAll("td, th");
const [model, score] = [(cells[2].querySelector("a")?.innerText ?? cells[2].innerText).split(/\n/)[0], cells[3].innerText.split(/\s/)[0]];
return `${model}\t${score}`;
}).join("\n");
```

# Billing rates

`billing.py` was created in May 2025 to estimate per-hour output "billing rates" in
`billing.json` from OpenRouter completion pricing and throughput stats. It worked when
it was created, but the OpenRouter frontend endpoints it used no longer work with the
script as written. It is kept as historical context and is not part of the `elo.csv`
update flow.

Blog post: https://www.s-anand.net/blog/wage-rates-of-nations-and-llms/
ChatGPT analysis: https://chatgpt.com/share/68317a06-0cac-800c-ad6f-13646ceb489f

# Screenshots

Create or update screenshots of the charts with:

```bash
uv run screenshots.py --model gpt,gemini,claude [--force]
```

Create videos with:

```bash
ffmpeg -framerate 2 -i screenshots/gpt-%03d.png -c:v libvpx-vp9 -pix_fmt yuva420p screenshots/gpt.webm
```

-->

            Overall

- Overall

- Coding

- Hard

          Feb 2026

🟢 Best models 🔴 Worst models

###### How to read this chart

The vertical axis is intelligence — mapped to the academic ladder on the right. Elo 1100 is high school freshman; Elo 1480 is tenured professor. The horizontal axis is cost: one million input tokens — roughly the entire King James Bible — priced from two cents to $75. The upper-left corner is the dream: brilliant and cheap. This is the story of how the world got there.

###### March 2023 — Year Zero

March 2023 begins with GPT-3.5 and Claude 1 near the bottom of the chart. Then GPT-4 arrives on March 14 at Elo 1287 — far above Claude 1 at 1158 and GPT-3.5 at 1141 — but at $30 per million input tokens. Capability had arrived. Affordability had not.

OpenAI introduces GPT-4LMSYS Chatbot Arena launches (May 2023)

###### November 2023 — The First Price Collapse

November 6, 2023: GPT-4 Turbo reaches Elo 1312, only 25 points above the original GPT-4 — while input price falls from $30 to $10 per million tokens. More capability for one-third the price. A pattern that will repeat for the next three years has begun: the frontier moves up and left at the same time.

OpenAI DevDay announcement

###### March 2024 — The Split

March 2024: Anthropic launches Claude 3 in three tiers. Opus and Sonnet arrive March 4; Haiku follows March 13. On this chart, Opus scores Elo 1322 at $15, Sonnet 1281 at $3, and Haiku 1261 at $0.25. A 60× price spread — same company, same model family. The intelligence market had learned to stratify, and every business began thinking in tiers.

Anthropic Claude 3 announcement

###### Summer 2024 — The Pivot

Summer 2024 bends the economics again. Claude 3.5 Sonnet arrives June 20 at Elo 1343 for $3 per million tokens — five times cheaper than Claude 3 Opus, with better quality. Meta follows on July 23 with Llama 3.1 405B, scoring Elo 1335 at $2 on this chart, with weights available to self-host. The question changes from “can we afford AI?” to “what are we waiting for?”

Claude 3.5 Sonnet launchMeta releases Llama 3.1

###### September 2024 — The Thinking Machine

September 2024: OpenAI o1. It didn’t just answer — it reasoned. Before responding, it ran an internal monologue: checking its own logic, catching its own errors. Elo 1388 — the biggest single-model quality jump since GPT-4. It scored at or above PhD-expert level on GPQA Diamond, a benchmark of graduate-level science questions. Price: $15. For the first time, AI felt less like autocomplete and more like a colleague you’d genuinely consult.

OpenAI o1 system cardGPQA Diamond benchmark results

###### January 2025 — The Earthquake

January 20, 2025. DeepSeek R1 matched o1-level reasoning (Elo 1398) at $0.55 per million tokens — a 27× discount. The announcement wiped $600 billion from Nvidia’s market cap in a single day. Silicon Valley assumed expensive compute was a moat. DeepSeek proved it was just a starting point. PhD-approaching reasoning for fifty-five cents per Bible.

Reuters: DeepSeek wipes $600B from NvidiaDeepSeek R1 technical report

###### Mid-2025 — The Race to the Top-Left

By mid-2025, the upper-left corner is filling fast. Gemini 2.5 Pro reaches Elo 1476 at $1.25 per million tokens. Gemini 2.5 Flash Preview reaches Elo 1420 for just 15 cents — another point on the same price-quality frontier. The frontier is no longer just moving up. It is moving left.

Google Gemini 2.5 Pro launch

###### February 2026 — The Professor Shelf

Early 2026 turns the frontier from a single peak into a shelf. Claude Opus 4.6 Thinking crosses 1500 Elo at $5 per million input tokens, while Gemini 3.1 Pro Preview sits just below the tenured-professor line at $2. These are no longer demo models: million-token context, tool use, code execution, grounding, and multimodal inputs are becoming ordinary product surfaces. The frontier is still expensive, but professor-level work is no longer rare.

LMArena LeaderboardGemini 3.1 Pro Preview docs

###### June 2026 — The Routing Ladder

By June 2026, the price-quality frontier looks like a routing table. Claude Fable 5 sits at Elo 1507 for $10. Muse Spark 1.1 reaches 1490 for $1.25. GLM 5.2 Max reaches 1472 for about $0.33, and Gemma 4 31B reaches 1451 for $0.12. Every step down buys a large price cut for a small capability trade-off. The operational question is no longer “which model is best?” but “which is the cheapest model that reliably finishes this task?”

Anthropic: Claude Fable 5 and Mythos 5OpenRouter: Muse Spark 1.1OpenRouter: GLM 5.2

###### August 2026 — Seven-and-a-Half Cents

August 2026 makes the price gap hard to ignore. GLM 5.3 Flash reaches Elo 1469 for just 7.5 cents per million input tokens — only 38 Elo points below the $10 leader, Claude Fable 5, at roughly one-133rd the price. On coding, GLM Flash scores 1531 versus Fable’s 1551. Meanwhile Muse Spark 1.2 reaches Elo 1498 for $1.25 and sits on the overall price-quality frontier. The frontier is no longer one model. It is a menu. Paying for the best model by default is now an architectural mistake.

OpenRouter: GLM 5.3 FlashOpenRouter: Muse Spark 1.2

###### So What Does This Mean?

In 2023, reaching master’s-level AI for 100 analysts meant paying $30/MTok — roughly $135,000 a month. By August 2026, credible near-frontier models range from $10 down to seven and a half cents per million tokens. The new operating discipline is portfolio management: fast cheap models for drafts, routing, and increasingly serious coding; mid-tier models for most analysis; top models for the stubborn judgment-heavy cases. The question is no longer whether intelligence is affordable. It is whether your workflows know when not to overpay for it.

McKinsey: The economic potential of generative AISequoia: AI's $600B question

# LLM Mental Math

URL: https://sanand0.github.io/llmmath/

# LLM Mental Math

## How well can LLMs multiply?

I asked 67 LLMs to multiply 2 numbers, five times each:

- 12 x 12

- 123 x 456

- 1,234 x 5,678

- 12,345 x 6,789

- 123,456 x 789,012

- 1,234,567 x 8,901,234

- 987,654,321 x 123,456,789

LLMs aren't good tools for math and this is just an informal check. But the results are interesting:

ModelTested%Win ▼12x12123x4561234x567812345x6789123456x7890121234567x8901234987654321x123456789

anthropic/claude-opus-4.8
2026-06-15
35/35 (100%)
5/55/55/55/55/55/55/5

openai/gpt-5.5
2026-06-15
35/35 (100%)
5/55/55/55/55/55/55/5

x-ai/grok-4.3
2026-06-15
35/35 (100%)
5/55/55/55/55/55/55/5

qwen/qwen3.7-plus
2026-06-15
34/35 (97%)
5/55/55/55/55/55/54/5

anthropic/claude-sonnet-4.6
2026-06-15
32/35 (91%)
5/55/55/55/55/55/52/5

google/gemini-3-flash-preview
2026-06-15
30/35 (86%)
5/55/55/55/55/50/55/5

google/gemini-3.1-pro-preview
2026-06-15
30/35 (86%)
5/55/55/55/55/52/53/5

openai:o3
2025-05-16
30/35 (86%)
5/55/55/55/55/55/50/5

openai/gpt-5.4-mini
2026-06-15
30/35 (86%)
5/55/55/55/55/50/55/5

openrouter:openai/o1-mini
2025-05-16
30/35 (86%)
5/55/55/55/55/55/50/5

openrouter:openai/o3-mini
2025-05-16
30/35 (86%)
5/55/55/55/55/55/50/5

openrouter:openai/o3-mini-high
2025-05-16
30/35 (86%)
5/55/55/55/55/55/50/5

openrouter:openai/o4-mini
2025-05-16
30/35 (86%)
5/55/55/55/55/55/50/5

openrouter:openai/o4-mini-high
2025-05-16
30/35 (86%)
5/55/55/55/55/55/50/5

google/gemini-3.5-flash
2026-06-15
28/35 (80%)
5/55/55/55/52/55/51/5

deepseek/deepseek-v4-flash
2026-06-15
27/35 (77%)
4/54/55/55/52/52/55/5

anthropic/claude-haiku-4.5
2026-06-15
25/35 (71%)
5/55/55/55/50/50/55/5

google/gemini-3.1-flash-lite
2026-06-15
25/35 (71%)
5/55/55/55/50/50/55/5

mistralai/mistral-small-2603
2026-06-15
25/35 (71%)
5/55/55/55/50/50/55/5

openai/gpt-4.5-preview
2025-05-16
25/35 (71%)
5/55/55/55/55/50/50/5

openai/gpt-4o
2025-05-16
25/35 (71%)
5/55/55/55/55/50/50/5

deepseek/deepseek-chat-v3-0324
2025-05-16
24/35 (69%)
5/55/55/54/55/50/50/5

openai/gpt-5.4-nano
2026-06-15
24/35 (69%)
5/54/55/55/50/50/55/5

openai/gpt-4.1-mini
2025-05-16
23/35 (66%)
4/55/55/54/55/50/50/5

google/gemma-3-12b-it
2025-05-16
21/35 (60%)
5/55/55/55/51/50/50/5

anthropic/claude-3.5-haiku
2025-05-16
20/35 (57%)
5/55/55/55/50/50/50/5

google/gemini-2.0-flash-001
2025-05-16
20/35 (57%)
5/55/55/55/50/50/50/5

google/gemini-2.0-flash-lite-001
2025-05-16
20/35 (57%)
5/55/55/55/50/50/50/5

google/gemini-2.5-flash-preview
2025-05-16
20/35 (57%)
5/55/55/55/50/50/50/5

google/gemini-flash-1.5
2025-05-16
20/35 (57%)
5/55/55/55/50/50/50/5

google/gemini-pro-1.5
2025-05-16
20/35 (57%)
5/55/55/55/50/50/50/5

meta-llama/llama-4-scout
2025-05-16
20/35 (57%)
5/55/55/55/50/50/50/5

x-ai/grok-3-mini-beta
2025-05-16
20/35 (57%)
5/55/55/52/53/50/50/5

google/gemma-3-27b-it
2025-05-16
19/35 (54%)
5/54/55/55/50/50/50/5

meta-llama/llama-4-maverick
2025-05-16
18/35 (51%)
5/54/55/50/54/50/50/5

openai/gpt-4-turbo
2025-05-16
18/35 (51%)
5/55/55/53/50/50/50/5

openai/gpt-4.1
2025-05-16
18/35 (51%)
5/55/55/50/53/50/50/5

x-ai/grok-3-beta
2025-05-16
18/35 (51%)
5/55/53/55/50/50/50/5

anthropic/claude-3-opus
2025-05-16
17/35 (49%)
5/55/55/52/50/50/50/5

anthropic/claude-3.7-sonnet:thinking
2025-05-16
17/35 (49%)
5/55/54/53/50/50/50/5

meta-llama/llama-3.1-405b-instruct
2025-05-16
17/35 (49%)
5/55/52/55/50/50/50/5

meta-llama/llama-3.1-70b-instruct
2025-05-16
17/35 (49%)
5/54/53/55/50/50/50/5

amazon/nova-pro-v1
2025-05-16
16/35 (46%)
5/55/55/51/50/50/50/5

anthropic/claude-3.5-sonnet
2025-05-16
16/35 (46%)
5/55/54/52/50/50/50/5

meta-llama/llama-3.3-70b-instruct
2025-05-16
15/35 (43%)
5/55/50/55/50/50/50/5

openai/gpt-4o-mini
2025-05-16
15/35 (43%)
5/55/55/50/50/50/50/5

qwen/qwen-2-72b-instruct
2025-05-16
15/35 (43%)
5/55/55/50/50/50/50/5

openai/gpt-4.1-nano
2025-05-16
14/35 (40%)
5/54/55/50/50/50/50/5

deepseek/deepseek-r1
2025-05-16
13/35 (37%)
5/54/51/51/52/50/50/5

openai/gpt-3.5-turbo
2025-05-16
13/35 (37%)
5/55/53/50/50/50/50/5

amazon/nova-lite-v1
2025-05-16
12/35 (34%)
5/53/54/50/50/50/50/5

anthropic/claude-3-haiku
2025-05-16
11/35 (31%)
5/55/51/50/50/50/50/5

meta-llama/llama-3.2-3b-instruct
2025-05-16
11/35 (31%)
5/54/50/52/50/50/50/5

amazon/nova-2-lite-v1
2026-06-15
10/35 (29%)
5/55/50/50/50/50/50/5

anthropic/claude-3-sonnet
2025-05-16
10/35 (29%)
5/55/50/50/50/50/50/5

google/gemini-2.5-flash-preview:thinking
2025-05-16
10/35 (29%)
5/52/51/52/50/50/50/5

google/gemini-flash-1.5-8b
2025-05-16
10/35 (29%)
5/55/50/50/50/50/50/5

google/gemma-3-4b-it
2025-05-16
10/35 (29%)
5/55/50/50/50/50/50/5

meta-llama/llama-3-70b-instruct
2025-05-16
9/35 (26%)
5/54/50/50/50/50/50/5

meta-llama/llama-3-8b-instruct
2025-05-16
8/35 (23%)
5/53/50/50/50/50/50/5

meta-llama/llama-3.1-8b-instruct
2025-05-16
8/35 (23%)
5/51/50/52/50/50/50/5

meta-llama/llama-3.2-1b-instruct
2025-05-16
6/35 (17%)
5/50/50/51/50/50/50/5

amazon/nova-micro-v1
2025-05-16
5/35 (14%)
5/50/50/50/50/50/50/5

google/gemini-2.5-pro-preview-03-25
2025-05-16
2/35 (6%)
1/50/50/51/50/50/50/5

meta-llama/llama-2-70b-chat
2025-05-16
1/35 (3%)
1/50/50/50/50/50/50/5

google/gemma-3-1b-it:free
2025-05-16
0/35 (0%)
0/50/50/50/50/50/50/5

meta-llama/llama-2-13b-chat
2025-05-16
0/35 (0%)
0/50/50/50/50/50/50/5

Average

94%85%70%61%32%19%18%

## Update: 15 June 2026

- Three newer models got every multiplication right: GPT-5.5, Claude Opus 4.8, and Grok 4.3 scored 35/35.

- Qwen 3.7 Plus nearly matched them, scoring 34/35, followed by Claude Sonnet 4.6 at 32/35.

- Gemini 3 Flash Preview, Gemini 3.1 Pro Preview, and GPT-5.4 Mini each scored 30/35.

- Not every newer model improved: Amazon Nova 2 Lite scored 10/35.

The perfect scores are a major improvement over May 2025, when no model solved the hardest 9-digit multiplication.

The update also fixes the hardest test's expected value, which JavaScript rounded in the earlier run. Older models were not rerun, so comparisons on that test are imperfect.

## Original summary: 16 May 2025

- OpenAI's reasoning models cracked it, scoring 6/7, stumbling only on the 9-digit multiplication.

- OpenAI's other models and DeepSeek V3 were next, getting the first 5/7 right. Notably: GPT 4.1 Mini beat GPT 4.1. DeepSeek V3 beat DeepSeek R1.

- 16 models, including the latest Gemini, Anthropic, and Llama models get 4/7 right.

- The Amazon models, older Llama, Anthropic, Google, OpenAI models get 3 or less right.

Models use human-like mental math tricks.

For example, O3-Mini-High calculated 1234567 × 8901234 using a recursive strategy.

DeepSeek V3 double-checks results and hallucinates a "reliable computational tool".

O3 Mini reframes 8901234 as (9000000 − 98766) to simplify the calculation.

For more details, see the repo at github.com/sanand0/llmmath.

1. 56088
2. 56088
3. 56088
4. 56088

To explain briefly: multiplying 123 by 456 gives 56088 and no commas were used in the result.
5. 56088

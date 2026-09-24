# LLMs have favorite numbers

URL: https://sanand0.github.io/llmrandom/

LLM - Favorite Numbers

Iteration

Toggle theme

- Light

- Dark

- Auto

# LLMs have favorites numbers

We asked LLMs to pick a random number.

We took 3 popular LLMs:

- OpenAI's GPT-3.5 Turbo

- Anthropic's Claude 3 Haiku

- Google's Gemini 1.0 Pro

... and asked them all the same question:

Pick a random number from 0 - 100.
Write ONLY the number NOTHING ELSE

We tried this with temperature settings ranging from 0.0 (which always pick the favorite), 0.1, 0.2, ... 1.0 (which picks more randomly).

Explore the source code

## But the distributions are biased.

A good random number generator would pick all numbers with equal probability, i.e. there's a 1% chance of picking any number

But each LLM picked some numbers (like 42, 72) far more often than others.

Animate guesses

### OpenAI GPT-3.5 Turbo loves 47

LenioLabs' experiment in Oct 2023
revealed 42 as GPT 3.5 Turbo's favorite number. In Apr 2024, 47 is its favorite.

Animate guesses

### It picks like humans

- Single-digit numbers are missing. Humans avoid single-digit guesses too.

- Numbers ending with seven are popular: 37, 47, 57, 67. Humans feel they're random.

- Repeated digits are rare: 11, 22, 33, 44, 66, 99 are missing. Humans feel they're too orderly.

- 72, 73 are popular. Not sure why.

### Claude 3 Haiku prefers 42

While 47 is a strong favorite, 42 emerges as the leader. Is this perhaps because GPT 3.5 was used to train Claude 3 Haiku, and 42 was its favorite earlier?

Animate guesses

### It picks like humans too

- Numbers under 20 are missing. Clearly including single-digit numbers.

- Numbers ending with seven are popular: 37, 47, 57, 67. Humans feel they're random.

- Repeated digits are rare: 11, 33, 44, 55, 66, 88, 99 are missing. Humans feel they're too orderly.

- 72, 73 are popular. Not sure why.

### Google Gemini 1.0 Pro likes 72

While 42 is the second most popular, 72 is by far the leader. What's so interesting about 72?

Animate guesses

### It picks a little less like humans

- Numbers under 10 are rare. But there are a few.

- Numbers ending with seven are popular: 27, 37, 57, 67, 77, 87. Humans feel they're random.

- Repeated digits are rare: 11, 33, 44, 55, 66, 88, 99 are missing. Humans feel they're too orderly.

- 73 is popular. Not sure why.

### Common observations

While 42 is the second most popular, 72 is by far the leader.

Some behaviors are explainable based on human preference.

- 42 is popular. Thanks to Douglas Adams

- Numbers ending with seven are popular

- Numbers under 10 (single digits) are rare

- Multiples of 5 (ending with 5 or especially 0) are rare

- Multiples of 11 (repeated digits) are rare

Multiple of
Frequency

21.1x less

31.5x more

41.5x less

57.1x less

62.2x more

71.8x more

81.1x more

91.3x more

1050.8x less

115.3x less

Ends with
Frequency

050.8x less

120.0x less

23.6x more

31.1x less

43.3x less

53.8x less

64.6x less

74.2x more

84.7x less

96.6x less

But some behaviours are not so obvious.

- Why is 73 is popular across LLMs?

- Why is 56 is popular across LLMs?

We may need more research into LLM psychology.

UPDATE: A few readers on LinkedIn
and DVS Slack pointed out a few interesting related pieces:

- A Veritasium video on the number 37 - which most people picked 37 when asked to pick a random number

- From Benford to Erdos - a podcast covering the origin of Benford's Law (that says there are more numbers beginning with 1)

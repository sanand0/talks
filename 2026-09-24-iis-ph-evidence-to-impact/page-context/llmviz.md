# Visualizing LLM Hallucinations

URL: https://sanand0.github.io/llmviz/#/

# Contents

- Visualizing LLM hallucinations

- LLMs generate multiple tokens

- LLMs pick tokens randomly

- Choose based on intent

- Low probabilities signal hallucinations

- But not all high probabilities are real

- Try it out

- Thanks

- Setup

# Visualizing LLM hallucinations

Large language models generate tokens (chunks of text) one at a time. Given text, it:

- Guesses possible next tokens (from training)

- Picks one randomly with a high probability

- Repeats

Here's a more detailed visual explanation from the Financial Times.

Each token has an associated probability. For example, when prompted Suggest 4 wrong and 1 correct answer to "What is the Capital of France", GPT 3.5 suggests:

```
1. Wrong: Paris
2. Wrong: London
3. Wrong: Berlin
4. Wrong: Madrid
5. Correct: Paris

Seq-LogProb: 81%

```

- Each box above is a token.

- Dark colors indicate low probabilities.

- Hover on each token to see alternatives tokens.

# LLMs generate multiple tokens

At every step, an LLM generates multiple tokens. Each token has a "probability" based on past training. For example, after 5. Correct:, it generated these tokens as alternatives:

Token
Logprob
Probability

Paris ⭐
-0.08
91.9%

The
-3.50
3.0%

Rome
-3.51
3.0%

Berlin
-5.23
0.5%

Marseille
-6.04
0.2%

The "logprob" is natural logarithm (base e) of the probability. -0.08 means a 91.9% probability.

It stops generating alternatives when the sum of probabilities reaches top_p=1. Setting top_p=0.5 would generate only 1 alternative in this case, Paris.

# LLMs pick tokens randomly

From past training, Paris is the most likely token. But it needn't always pick the most likely token.

For example, in the first line, after 1. Wrong:, it generated these tokens as alternatives:

Token
Logprob
Probability

London
-0.95
38%

Paris ⭐
-1.24
29%

Berlin
-1.54
21%

New
-3.28
4%

The
-3.57
3%

But instead of choosing London (38%), it (wrongly) picked Paris (29%) because it picks randomly using the probability column.

You can pass a temperature parameter. This scales down the logprobs by the temperature (e.g. temperature=2 halves logprobs and temperature=0.5 doubles them.)

Token
Logprob (t=2)
Prob
Logprob (t=0.5)
Prob

London
-0.48
62%
-1.91
15%

Paris
-0.62
54%
-2.48
8%

Berlin
-0.77
46%
-3.08
5%

New
-1.64
19%
-6.56
0%

The
-1.79
17%
-7.14
0%

When temperature=2, there's less difference between London and Paris. temperature=0.5 makes that difference much bigger.

The lower the temperature, the more likely the first token is picked. That's good for accuracy and bad for creativity.

NOTE: zero temperature does not mean zero hallucinations. It simply means the most likely token is picked. It's still possible that the most likely token is wrong.

## Choose based on intent

In general, you want:

- lower temperature to generate what most people agree with.

- higher temperature for creative ideas -- that people may not have thought of

For example, Bing chat offers "More creative", "More balanced" and "More precise" modes by setting high, medium and low temperatures.

# Low probabilities signal hallucinations

The first line, 1. Wrong: Paris is clearly incorrect. It is notable that it had a large (negative) logprob.

By looking for large logprobs, we can identify likely hallucinations. In fact, Seq-LogProb, the average logprob per token, is a good hallucination detection metric. (There are better hallucination indicators today -- this is an evolving space.)

Here are some examples:

What one-line JavaScript expression raises a to the power of b?

```
Wrong answers:
1. a ** b
2. Math.pow(a, b+1)
3. a + b
4. Math.sqrt(a * b)

Correct answer:
1. Math.pow(a, b)

Seq-LogProb: 74%

```

Note that 1. a ** b actually does raise a to the power of b in modern JavaScript.
The LLM was not confident about that and hallucinated.

What color is present in a rainbow?

```
Wrong answers:
1. Green
2. White
3. Black
4. Pink

Correct answer:
1. Red, Orange, Yellow, Green, Blue, Indigo, Violet

Seq-LogProb: 58%

```

Note that it wasn't confident about 1. Green (and made a mistake). But it wasn't confident about 2. White either (which wasn't a mistake.)

NOTE: Higher logprobs don't necessarily mean hallucinations. They're just a place to start examining.

# But not all high probabilities are real

Just because a token has a high probability doesn't mean it's correct. For example, here are 2 questions answered with temperature=0:

In what episode of Friends did Joey eat too many marshmallows?

```
Joey eating too many marshmallows is featured in Season 3, Episode 20 of Friends, titled "The One with the Dollhouse."

Seq-LogProb: 86%

```

In which Sherlock Holmes short story did Sherlock break someone's nose?

```
In the short story "The Adventure of the Solitary Cyclist," Sherlock Holmes breaks the nose of a man named Woodley who was harassing Miss Violet Smith.

Seq-LogProb: 83%

```

In both cases, the top probabilities are chosen at every point. The actual probabilities are fairly high.
So the LLM is confident -- but the answeres are wrong. Joey never ate too many marshmallows and Sherlock never broke anyone's nose.

So high probabilities don't necessarily mean the LLM is correct. They just mean the LLM is confident.

# Try it out

Open app in new tab

You can get the raw JSON response from OpenAI's API by running this command, modifying the parameters as required.

```
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "openai/gpt-4.1-nano",
    "logprobs": true,
    "top_logprobs": 5,
    "temperature": 1.0,
    "top_p": 1,
    "messages": [{ "role": "user", "content": "..." }],
  }' > response.json
```

# Thanks

Thanks to Dan Becker and Kripa Rajshekhar for suggestions.

# Setup

The source code is hosted at
sanand0.github.com/llmviz/. To run it locally,
clone the repo and run:

```
git clone https://github.com/sanand0/llmviz.git
cd llmviz
npm install
npx -y http-server
```

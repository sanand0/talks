---
title: "LLM Arithmetic Demonstration"
date: 2026-06-14T21:26:14+05:30
source: "https://chatgpt.com/c/6a2d2a39-8d20-83ec-be15-93132c744f07"
---

## User

I'm in a workshop, and we are exploring the capabilities of large language models to do arithmetic, keeping in mind that large language models don't really do mental arithmetic well, but they can write programs that do powerful arithmetic. Can you write and run a simple yet mind-blowing program that will help the audience understand the sophistication to which LLMs can reliably do? Keep in mind that my aim is that the audience will appreciate the following. First, it is simple enough for them to glance at it and understand, and this is a lay audience. Keep this to the level of something that, let's say, a grade 8 student can understand. Second, it should be obvious that this is something that is both useful as well as difficult, one would think, for a language model to be able to do based on a conventional understanding. And the instant I look at it, it should come through this way. Think carefully about the objective, but make sure that what you finally present on screen is concise.

---

## ChatGPT

I’ll show one compact “LLM + code” arithmetic demo: a useful real-life optimization where the program checks hundreds of possibilities exactly, without mental arithmetic.

```python
from itertools import combinations

# Tiny arithmetic assistant:
# Pick the most protein, staying under both budget and calories.

foods = [
    ("Idli",        30,  4, 120),   # name, rupees, protein grams, calories
    ("Dosa",        70,  6, 220),
    ("Paneer roll", 90, 18, 280),
    ("Curd cup",    40,  8,  90),
    ("Peanuts",     50, 12, 300),
    ("Eggs",        60, 13, 140),
    ("Banana",      20,  1, 100),
    ("Milk",        35,  7, 150),
]

budget = 200
calorie_limit = 500

best = None
checked = 0

for size in range(1, len(foods) + 1):
    for basket in combinations(foods, size):
        checked += 1
        cost = sum(item[1] for item in basket)
        protein = sum(item[2] for item in basket)
        calories = sum(item[3] for item in basket)

        if cost <= budget and calories <= calorie_limit:
            score = (protein, -cost, -calories)  # more protein; then cheaper; then lighter
            if best is None or score > best[0]:
                best = (score, basket, cost, protein, calories)

_, basket, cost, protein, calories = best

print(f"Checked {checked} possible food baskets.")
print(f"Best under ₹{budget} and {calorie_limit} calories:\n")
for name, price, p, c in basket:
    print(f"  {name:11} ₹{price:3}   protein {p:2}g   {c:3} cal")

print(f"\nTOTAL       ₹{cost}   protein {protein}g   {calories} cal")
```

```
Checked 255 possible food baskets.
Best under ₹200 and 500 calories:

  Idli        ₹ 30   protein  4g   120 cal
  Curd cup    ₹ 40   protein  8g    90 cal
  Eggs        ₹ 60   protein 13g   140 cal
  Milk        ₹ 35   protein  7g   150 cal

TOTAL       ₹165   protein 32g   500 cal
```

Use this framing:

“An LLM may not reliably multiply big numbers in its head. But it can write a tiny program that checks every possibility exactly. This is arithmetic as a tool, not arithmetic as memory.”

The demo above is good because it is instantly understandable: choose the best food basket under a budget and calorie limit. But it checked 255 combinations perfectly, which would be tedious by hand.

One-line punchline for the audience:

“Eight foods created 255 possible baskets. With 20 foods, this same idea checks over 1 million baskets — and still gives the exact best answer.”

For live impact, change `budget = 200` or `calorie_limit = 500` in front of them and rerun. The answer will update instantly.

## User

Explain to me in very simple terms what you did, just two or three sentences, covering why this is important.

## ChatGPT

I gave the computer a small menu, a budget, and a calorie limit, then made it try every possible food basket and pick the one with the most protein.

This matters because the language model does not need to “do arithmetic in its head”; it can write a simple program that does exact arithmetic and checks hundreds or millions of options reliably.

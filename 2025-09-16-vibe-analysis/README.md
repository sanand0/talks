---
marp: true
title: Vibe Analysis
author: Anand S
url: https://sanand0.github.io/talks/2025-09-16-vibe-analysis/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
---

<style>
  blockquote {
    font-style: italic;
  }

</style>

# Vibe Analysis

[Fifth Elephant Workshop](http://has.gy/hV8U) · 16 Sep 2025, 2:00 pm IST · [Bangalore](https://maps.app.goo.gl/fU3VHCjUGzUWVz6C6)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-16-vibe-analysis/)

---

## You need some software before we start

- A modern browser (Edge, Chrome, Firefox...)
- A $20 ChatGPT Plus account
- Sign into [github.com](https://github.com), [chatgpt.com/codex](https://chatgpt.com/codex), [jules.google.com](https://jules.google.com/)

For programmers:

- Install [uv](http://github.com/astral-sh/uv). Run `uv run --with pandas python`
- Install [NodeJS](https://nodejs.org/en/download). Run `npx -y @openai/codex` and log in
- Optional: Install [VS Code](https://code.visualstudio.com/) + [GitHub Copilot](https://github.com/copilot) / [Cursor](https://cursor.com/) / [Windsurf](https://windsurf.com/) / ...

---

## We will be sharing prompts on WhatsApp

[WhatsApp Invite](https://chat.whatsapp.com/BsQJXLOJrhi23dWlhtAssq)

![h:200px](https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://chat.whatsapp.com/BsQJXLOJrhi23dWlhtAssq)

---

## Vibe Coding: code like code doesn't exist

> ... where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.

> I "Accept All" always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment

> Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away.

[Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383)

---

## Vibe Analysis: analyze, but ignore the code

Here's the vibe analysis mindset:

- You're **pragmatic**. You care about insights, not how they're coded.
- You're **sceptical**. You cross-question and find errors.
- You're **playful**. You try weird "what ifs" just to see what breaks.

Let's analyze some datasets with this mindset.

---

## Pick any dataset. Here are some datasets

- [MovieLens movies](https://grouplens.org/datasets/movielens/32m/) (review license)
- [IMDb movies](https://datasets.imdbws.com/) (non-commercial)
- [Occupational Employment and Wage Statistics (OEWS)](https://www.bls.gov/oes/tables.htm)
- [Global AI Job Market & Salary Trends 2025](https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025)
- [Flight Delay Dataset](https://www.kaggle.com/datasets/shubhamsingh42/flight-delay-dataset-2018-2024)
- [London House Price Data](https://www.kaggle.com/datasets/jakewright/house-price-data)
- [Exchange Rates to USD](https://www.kaggle.com/datasets/robikscube/exhange-rates-to-usd-from-imforg-updated-daily)
- [Thailand Road Accidents (2019-2022)](https://www.kaggle.com/datasets/thaweewatboy/thailand-road-accident-2019-2022)

---

## Here are some India-specific datasets

- [CBFC Censor Board Cuts](https://github.com/diagram-chasing/censor-board-cuts/tree/master/data)
- [India Vehicle Data](https://github.com/Vonter/india-vehicle-stats/blob/main/DATA.md)
- [India Air Quality Index](https://github.com/Vonter/india-cpcb-aqi/blob/main/DATA.md)
- [Bengaluru Bus Routes](https://github.com/Vonter/bmtc-gtfs)
- [India Air Traffic](https://github.com/Vonter/india-aviation-traffic)
- [India Census 2011](https://www.kaggle.com/datasets/danofer/india-census)
- [India Exams Database](https://github.com/lalithaar/indian-exams-database)

---

## Now we'll use LLMs for _everything_

1. Explore data
2. Clean data
3. Model data
4. Explain data
5. Deploy data
6. Anonymize data

---

## We'll _ad lib_ this

1. I have no script / preparation. We'll do this live.
2. _You_ pick a dataset. _You_ suggest hypotheses.
3. _You_ guide the agents, even on my system. I'll just "facilitate".
4. **Publish** your findings _and prompts_. Make it reproducible.
5. **Red team** this. Critique sceptically. See what survives.
6. **Synthesize** learnings. Let's see what emerges / drops.

---

## I'm keen to experiment

- Do **multiple versions** pay off?
- **Explain-then-code** vs code-then-explain?
- What **sceptical review** approaches are effective?
- What **unit tests** help most? Any _invariants_?
- What's the **minimal stack** for analysis?
- What **schema context** helps LLMs most? (Ablation)
- Do **data tools** via AGENTS.md (`dbt`, `rclone`, ...) help?
- What **sub-agent specializations** work well?
- Where are **pre-mortems** effective?

<!-- Ideas from https://chatgpt.com/c/68c8bea3-c348-832b-a011-cc2723a47279 -->

---

## Let's cook some insights!

![h:500px](cooking-insights.webp)

---

# Vibe Analysis

[Fifth Elephant Workshop](http://has.gy/hV8U) · 16 Sep 2025, 2:00 pm IST · [Bangalore](https://maps.app.goo.gl/fU3VHCjUGzUWVz6C6)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

Please share your feedback here:

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://forms.gle/CfiZDDUGCG73vfdM7)

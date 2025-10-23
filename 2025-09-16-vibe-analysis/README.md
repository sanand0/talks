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

https://sanand0.github.io/talks/

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

---

## Insights from IMDb rating histogram

- **Dense cluster around 7–7.5**. [Vote-weighted mean][imdb-weight] is ~7.21.
- **Scarcity of low-end titles (<4)** despite millions of records. [Self-selection bias][self-selection]
- **Sharp drop beyond ~8.5**. IMDb emphasizes “regular” voters. High averages require consistently enthusiastic voters. [IMDb’s Top 1,000 voters][top-reviewers] rate critically (lower than typical users 98% of the time)
- **Spike at perfect 10.0**: [coordinated fan campaigns and vote brigading][ringer]

[imdb-weight]: https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV "“Ratings FAQ,” IMDb Help Center. Weighted rating formula: (\\text{WR} = \\frac{v}{v+m}R + \\frac{m}{v+m}C), where (C) is the overall mean and (m) the minimum votes for chart eligibility."
[self-selection]: https://link.springer.com/chapter/10.1007/978-0-387-73655-6_17 "Kramer, M. A. “Self-Selection Bias in Reputation Systems.” *Trust Management*, IFIP, 2007."
[top-reviewers]: https://hbr.org/2025/01/research-how-top-reviewers-skew-online-ratings "Bondi, T., Rossi, M., & Stevens, R. L. “Research: How Top Reviewers Skew Online Ratings.” *Harvard Business Review*, Jan. 9, 2025."
[ringer]: https://www.theringer.com/2019/6/12/tv/imdb-rating-system-problems-chernobyl "Bereznak, A. “The Problem With IMDb’s Rating System.” *The Ringer*, June 12, 2019."

---

# Lockdown-era genre peaks

<small>

Reality-TV reached its highest output during lockdown with 78 feature releases in 2020, a 2.07× surge versus the 2017–2019 baseline of 37.7 films per year and 3.12× the 2022–2024 recovery average of 25 releases.

Talk-Show titles also peaked in 2020, delivering 26 releases—double the pre-lockdown average of 13 per year and 2.23× the immediate post-lockdown average of 11.7 releases.

Both genres cleared the study’s thresholds (at least 25 lockdown-year films and ≥20% growth over the pre-lockdown window), marking them as the only categories with statistically meaningful release spikes tied to the COVID-19 lockdown period

</small>

---

<small>

| Director           | Movies | Preferred Letter |
| ------------------ | -----: | ---------------: |
| Rakesh Roshan      |      6 |                K |
| Haruo Sotozaki     |      5 |                D |
| Keishi Otomo       |      5 |                R |
| Frank Darabont     |      4 |                T |
| Chad Stahelski     |      4 |                J |
| Alan Mak           |      4 |                I |
| Kunihiko Yuyama    |      4 |                P |
| Michael Chaves     |      4 |                T |
| John R. Cherry III |      4 |                E |
| Saeed Roustayi     |      3 |                L |

</small>

---

## Any genres that rate 1950-60s films too high?

<small>

- **Film-noir** ratings cluster in the classic period: about 13.3 % of all noir ratings come from 1950s–1960s releases and another 25 % from the 1930s–1940s. The median genre sees only ~4.5 % of its ratings tied to 1950s–1960s titles, so noir is roughly 3× as concentrated there. Those mid-century titles are strong performers (e.g., 1950s average 3.997, 1960s 4.053), but later decades (1970s neo-noir at 4.12) keep the overall average high too.
- **War films** also skew earlier: 1950s–1960s releases account for 11.3 % of war-movie ratings versus that same ~4.5 % median elsewhere. Their 1950s/1960s averages (3.963 and 4.004) are among the genre’s best, yet pre/post-1960 decades remain relatively strong (e.g., 1930s at 3.86, 1990s at 3.85).
- **It isn’t solely a volume imbalance** though; even later entries hold up reasonably well, suggesting a combination of historical canon effects and comparatively consistent quality.

</small>

---

## Feedback analysis

Lessons from [vibe analysis of feedback](https://chatgpt.com/share/68ca37db-14dc-800c-8cfa-34f7dcd1538e):

- Share **setup instructions** + video/asciinema to reduce setup friction.
- Share **self-check instructions** for a default dataset with prompts.
- Add explicit checkpoints with **self-tests**.
- Use two-lane pacing: **Cruise** (safe, minimal path) vs **Sprint** (optional accelerators).

[Participant feedback](https://hasgeek.com/fifthelephant/data-analytics-using-ai-workshop/updates/llms-in-action-what-participants-learned-at-the-vi-KAAiTUtoJNrmJ61Gxrdxgf)

---

## Participant feedback: Ambarish

> Before the workshop, I was curious about the name and content, but trusted the organizer (Hasgeek) & Anand. Anand’s deep knowledge and lucid explanations guided us through using LLMs for data analysis, testing hypotheses, and running parallel tasks with tools like Claude and Codex. I learned how BI and data analysis are evolving in the AI age, and how using multiple models reduces hallucinations and errors. Even as a remote participant, the pace was comfortable. Thanks again, Anand, for a wonderful session!

## Participant feedback: Anindo Chakraborty

> Yesterday’s workshop cut through the hype around ‘vibe coding’ and showed how it applies to analytics and data science. Anand walked us through the full lifecycle — from raw data to hypotheses, AI-driven testing, and refining results into business-ready insights. Advanced topics included building Agents, sub-agents, and using AGENTS.md files for task automation. The hands-on ‘flow state’ approach made learning incredibly practical. My biggest takeaway: start small, get your hands dirty, and practical experience will follow. Outstanding workshop — thank you, Anand!

---
marp: true
title: Vibe Analysis
author: Anand S
url: https://sanand0.github.io/talks/2025-10-16-vibe-analysis/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
---

[sheet]: https://docs.google.com/spreadsheets/d/1z88_6xa-uVgE4BTScpwIC7jKYfnstYLk-UEoflhdQ0g/edit?usp=sharing

<style>
  blockquote {
    font-style: italic;
  }

</style>

# Vibe Analysis

[Landmark Group](https://www.landmarkgroup.com/) · 16 Sep 2025, 11:00 am UAE · Remote
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-10-16-vibe-analysis/)

---

## This is an online workshop

- Ask **questions** on **chat**.
  - Feel free to answer each others' questions.
- **Unmute directly** to ask **verbal** questions. Don't raise your hand.
- Share your progress on this [**Google Sheet**][sheet] against your name.

If you're bored, do something else. This is not a classroom.

---

## Quick check: How are we set up?

[**Please answer on this Google Sheet**][sheet] against your name:

- What's your [ChatGPT plan](https://chatgpt.com/pricing/)? (Free, Go, Plus, Pro, Business, ...)?
  - You need any non-free plan for this workshop
- Do you have [Visual Studio Code](https://code.visualstudio.com/) installed?
  - Not required for the first half, recommended for the second half

---

## Quick check: What can AI do?

[**Please answer on this (public) Google Sheet**][sheet] against your name:

- Can LLMs provide robust data insights for exec reporting?
  - They are powerful, but can they be trusted?
- What data + analyses would you like to explore with high impact?
  - Think about what your stakeholders would value
  - Think about what's difficult / time-consuming today
  - The Google sheet is public. Don't share sensitive info.

---

## Today, we analyze public + private data

**Part A: Public Data**. 45 min. You analyze a public dataset with [Codex Cloud](https://chatgpt.com/codex) and publish the story.

**Part B: Private Data**: 45 min. You analyze your (real) dataset with [Codex on VS Code](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt) and share your learnings.

**No programming knowledge required** for either part.

**We probably won't finish both parts**. The goal is to get you started.

---

## A1. Pick _any_ public data (or use one here)

- [MovieLens movies](https://grouplens.org/datasets/movielens/32m/) (review license)
- [IMDb movies](https://datasets.imdbws.com/) (non-commercial)
- [Occupational Employment and Wage Statistics (OEWS)](https://www.bls.gov/oes/tables.htm)
- [Global AI Job Market & Salary Trends 2025](https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025)
- [Flight Delay Dataset](https://www.kaggle.com/datasets/shubhamsingh42/flight-delay-dataset-2018-2024)
- [London House Price Data](https://www.kaggle.com/datasets/jakewright/house-price-data)
- [Exchange Rates to USD](https://www.kaggle.com/datasets/robikscube/exhange-rates-to-usd-from-imforg-updated-daily)
- [Thailand Road Accidents (2019-2022)](https://www.kaggle.com/datasets/thaweewatboy/thailand-road-accident-2019-2022)

Share your **dataset** on the [**Google Sheet**][sheet] against your name

---

## A2. Set up GitHub

1. Sign up at [github.com](https://github.com)
2. Create a public repo, e.g. `vibe-analysis` with a README
3. Download the dataset and [upload it to your repository](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)

Share your **GitHub repo link** on the [**Google Sheet**][sheet] against your name

---

## A3. Analyze it on Codex Cloud

- On [Codex Cloud](https://chatgpt.com/codex), click Settings > Environments > Create Environment
  - Select your GitHub repository
  - Set "Agent internet access": ON.
  - Set "Domain allowlist": "All (unrestricted)"
- Describe the task **specifically**. E.g. "Analyze data _[explain how]_. Share insights _[explain what]_ as a visual web data story."
  - Make **long, detailed** requests. Be creative!

Copy-paste your **task** on the [**Google Sheet**][sheet] against your name

---

## A4. Publish your story

- Click on "Create PR" on the top right. Then click on "View PR".
- On GitHub, click on "Merge pull request" > "Confirm merge".
- Go to "Settings" > "Pages" and set the source to "main" branch and "/ (root)" folder. Click "Save".
- Go to "Actions" and watch the latest workflow run.

Share your **story link** on the [**Google Sheet**][sheet] against your name

---

## B1. Install VS Code + Codex extension

- Install [VS Code](https://code.visualstudio.com/)
- Install [Codex extension](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)
- Install [Python](https://www.python.org/)

See [this tutorial](https://sanand0.github.io/tutorials/codex-vscode/) for step-by-step instructions.

Share whether you **installed** Codex in VS Code & Python on the [**Google Sheet**][sheet] against your name (Yes/No).

---

## B2. Prompt Codex in VS Code

- Open your dataset folder in VS Code.
- Open the Codex sidebar (ChatGPT icon).
- Describe the task **specifically**. E.g. "Analyze data _[explain how]_. Share insights _[explain what]_ as a visual web data story."
  - Make **long, detailed** requests. Be creative!

Copy-paste your **task** on the [**Google Sheet**][sheet] against your name.
(Don't share sensitive data.)

---

## Quick check: What can AI do?

Since we've now explored what LLMs can do...

[**Please answer on this (public) Google Sheet**][sheet] against your name:

NOW, Can LLMs provide robust data insights for exec reporting?

---

# Vibe Analysis

[Landmark Group](https://www.landmarkgroup.com/) · 16 Sep 2025, 11:00 am UAE · Remote
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

https://sanand0.github.io/talks/

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-10-16-vibe-analysis/)

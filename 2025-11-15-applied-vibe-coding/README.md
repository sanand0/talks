---
marp: true
title: Applied Vibe Coding
author: Anand S
url: https://sanand0.github.io/talks/2025-11-15-applied-vibe-coding/
theme: gaia
paginate: true
style: |
  transcript { display: none; }

# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
# ChatGPT: https://chatgpt.com/c/69022cb0-f664-8321-846d-c398709e497d
---

<!-- _class: title -->

# Applied Vibe Coding

[IIT Madras](https://www.iitm.ac.in/) · 15 Nov 2025, 3:30 pm IST · Remote
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Spreadsheet](https://docs.google.com/spreadsheets/d/1qX8TRuWl5pbhj6K34eqxHPUYb9qd9g-P1joWkasosC4/edit?usp=sharing)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-11-15-applied-vibe-coding/)

---

<!-- _class: title -->

## Set up GitHub

1. Sign up at [github.com](https://github.com)
2. [Create a public repo](https://github.com/new), e.g. `vibe-coding-workshop`
3. Click on the "LICENSE" button and add a license, e.g., MIT

Now you have a GitHub repo to store your code!

[Fill up your profile in this spreadsheet](https://docs.google.com/spreadsheets/d/1qX8TRuWl5pbhj6K34eqxHPUYb9qd9g-P1joWkasosC4/edit?usp=sharing).
It will look like `https://github.com/your-username/`

---

<!-- _class: title -->

## Use an online coding agent

- Jules: [jules.google.com](https://jules.google.com/)
  - Currently free for limited use
- GitHub Copilot: [github.com/copilot](https://github.com/copilot)
  - Request a paid ChatGPT subscription.
- Codex: [chatgpt.com/codex](https://chatgpt.com/codex)
  - Requires a paid ChatGPT subscription.
- Claude Code: [claude.ai/code](https://claude.ai/code)
  - Requires a paid Claude subscription.

---

## You can also try with a CLI tool or VS Code extension

```bash
npx -y @github/copilot-cli       # GitHub Copilot CLI
npx -y @openai/codex             # OpenAI Codex
npx -y @anthropic/claude-code    # OpenAI Claude Code
npx -y @google/gemini-cli        # Google Gemini CLI
npx -y opencode-ai               # OpenCode AI
```

There are many others. Most of these have Visual Studio Code extensions too.

---

## Publish any app. Here are some ideas

1. **Create a game**, e.g., crosswords, memory, quizzes, puzzles
2. **Create a tool**, e.g. synthetic data generator, Excel to JSON, password strength checker
3. **Build a web scraper**, e.g., news, weather, stocks, sports, movies
4. **Analyze data**, e.g., ratings recommender, logs analysis, sentiment analyzer, geospatial analysis, solve Kaggle contest
5. **Build a dashboard**, e.g., fitness tracker, sales analysis, social analytics, project management, bug tracker

---

## Publish any app. Here are some ideas (contd.)

6. **Generate content**, e.g., social media post, invoice/receipt PDF, meme generator
7. **Do real-world tasks**, e.g., reply to RFP, meeting TODOs, fill claims
8. **Build an API**, e.g., URL shortener, auth service, webhook receiver
9. **Chrome extension**, e.g., ad block, dark mode toggle, price track
10. **Mobile app**, e.g., recipe manager, flashcard, share with clipboard
11. **Desktop app**, e.g., note-taking, to-do list, file organizer

---

<!-- _class: title -->

## Some lessons to keep in mind

- **Don’t promise**. Deliver, _then_ share outcomes
- **Specs _are_ the product**. Code is a build artifact
- **Optimize for review**, not coding
- **Restart on failure**. It's faster than correction
- Make repos **LLM-friendly**
- **Work in parallel**
- **Expect uneven gains**: seniors benefit differently than novices

---

## **Don’t promise**. Deliver, _then_ share outcomes

AI capability is _uneven and unpredictable_ across tasks (“the jagged frontier”).

Don't commit to your manager/client. Build it. **Then** share it.
**Fixing is 10X effort**.

Or, commit to _broad_ improvement, not specific apps.

---

## **Specs _are_ the product**. Code is a build artifact

AI makes typing cheap; the bottleneck becomes the specification.

Provide structured instructions.

Commit your prompts (e.g. `SPEC.md`, `PROMPTS.md`).

---

## **Optimize for review**, not coding

AI coding agents tools boost development speed speed, shifting effort to verification.

Ask agents to write readable code.

Ask it to write test cases, **run them**, and ensure they pass.

---

## **Restart on failure**. It's faster than correction

Once a conversation goes off-track, fixing all the mistakes is often more work than starting over.

Try once, maybe twice. If it doesn't work well, start again.

Break the task into smaller chunks - that can help.

---

## Make repos **LLM-friendly**

Models perform better with consistent structure, fast tests, and machine-readable context (e.g., repo "manuals" for LLMs).

Standardize your `AGENTS.md`.

Provide examples for them to copy from.

---

## **Work in parallel**

Give an agent a task, then work with another ageint while waiting.

These can be on different parts of the same project, or entirely different projects.

This means you need a queue of coding agent friendly tasks ready to go.

---

## **Expect uneven gains**: seniors benefit differently than novices

Experienced devs get sizable productivity boosts.

But novices can develop an _illusion of competence_ without robust verification.

Plan to learn along with the agents, not just delegate.

---

# Applied Vibe Coding

[IIT Madras](https://www.iitm.ac.in/) · 15 Nov 2025, 3:30 pm IST · Remote
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Spreadsheet](https://docs.google.com/spreadsheets/d/1qX8TRuWl5pbhj6K34eqxHPUYb9qd9g-P1joWkasosC4/edit?usp=sharing)
[CC0 - Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-11-15-applied-vibe-coding/)

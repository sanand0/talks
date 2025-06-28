---
marp: true
title: Prompt-to-Plot
author: Anand S
url: https://sanand0.github.io/talks/2025-06-28-prompt-to-plot/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
---

<style>
  blockquote {
    font-style: italic;
  }

  section {
    background-image: url('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-06-28-prompt-to-plot/');
    background-repeat: no-repeat;
    background-position: top 20px right 20px;
    background-size: 80px auto;
  }

  img + img {
    margin-left: 100px;
  }
</style>

# Prompt to Plot

#### [Crafting Visual Stories with LLMs](https://hasgeek.com/VizChitra/prompt-to-plot/) | [Slides](https://sanand0.github.io/talks/2025-06-28-prompt-to-plot/)

[VizChitra](https://vizchitra.com/) · 28 June 2025, 10:00 am IST · [Bangalore](https://maps.app.goo.gl/VsnBZmVpA6Sxmyje7)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-06-28-prompt-to-plot/)

---

## We will be collaborating

- [Google Group](https://groups.google.com/g/prompttoplot): prompttoplot@googlegroups.com
- [WhatsApp Invite](https://chat.whatsapp.com/IouFXUflmjPDPlQrjzdzgY)

![h:200px](https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://groups.google.com/g/prompttoplot) ![h:200px](https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://chat.whatsapp.com/IouFXUflmjPDPlQrjzdzgY)

---

## We will be using online LLM tools

- [GitHub](https://github.com/)
- Chatbots
  - [ChatGPT](https://chatgpt.com/) (smart) | [Plus $20](https://openai.com/chatgpt/pricing/)
  - [Claude](https://claude.ai/) (front-end coder) | [Pro $17](https://www.anthropic.com/pricing)
  - [Gemini](https://gemini.google.com/) (free)
- Coding Agents
  - [Jules](https://jules.google/com/) (free)
  - [Codex](https://chatgpt.com/codex) (Plus $20)

---

## We'll also use command line tools

- [Claude Code](https://www.anthropic.com/claude-code) (💻, Pro $17)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) (💻, free)

Skip anything marked 💻 if you wish.

---

## We'll use LLMs for _everything_

1. Finding a dataset
2. Ideating what to do with it
3. Analyzing the data
4. Visualizing the data
5. Publishing it on GitHub

---

## Set up GitHub

1.  Sign up at [github.com](https://github.com)
2.  Create a public repo, e.g. `prompt-to-plot-workshop` with a README
3.  💻 Clone the repository to your local machine.
    ```bash
    git clone https://github.com/<username>/<repository-name>.git
    ```
4.  💻 Navigate into your project directory.
    ```bash
    cd <repository-name>
    ```

---

## Jules & Codex

- Jules
  - **Access:** [jules.google.com](https://jules.google.com/)
  - **Setup:** Join the waitlist. It's a remote agent, so no local installation is needed. It's currently free.
- Codex
  - **Access:** [chatgpt.com/codex](https://chatgpt.com/codex)
  - **Setup:** Requires a ChatGPT Plus subscription.

---

## 💻 Claude & Gemini CLI

[Install NodeJS](https://nodejs.org/en/download).

Then, run these commands and follow instructions.

```
npx -y https://github.com/google-gemini/gemini-cli
```

```
npx -y @anthropic-ai/claude-code
```

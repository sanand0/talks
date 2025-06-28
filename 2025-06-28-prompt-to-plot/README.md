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
[Video](https://youtu.be/SdDulR-1bBM)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-06-28-prompt-to-plot/)

---

## We will be collaborating

[Google Group](https://groups.google.com/g/prompttoplot): prompttoplot@googlegroups.com
[WhatsApp Invite](https://chat.whatsapp.com/IouFXUflmjPDPlQrjzdzgY)

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

---

## Prompt to find a dataset

<small>

I am running a workshop as part of VizChitra. This workshop is called Prompt to Plot. I am going to be showing a very mixed audience how they can take a data set and convert it into a data visualization entirely using LLMs. So, the LLMs will be doing the analysis, the LLMs will be creating the code, the whole works. Now, I want you to suggest a bunch of data sets by A, searching online, but you know from my past conversations, my interests, so pick something nice and quirky. This will be the first iteration, so I want to pick something that is small, let us say about 100,000 rowsish or 10,000 rowsish, not too big and with a reasonable variety of columns and text, longish text, categorical text, numbers, that sort of a thing. But most importantly, at the end, it does, it should not matter what kind of analysis the LLM does or we pick. The story should be interesting for a wide variety of audiences, otherwise where is the fun? Now, give me something really cool, actually give me a whole bunch of stuff that is really cool.

</small>

---

## Prompt for ideation

These are the columns in the Goodreads 100k dataset. I would like to create interesting data stories out of it that can also be visualized nicely. Can you give me a dozen suggestions on A, what stories to write, B, who they would be interesting to and why and see how I might go about doing this by having an LLM write code to do it.

---

## Prompt to analyze & Visualize

Run all of these analyses, do all that stuff you do with statistical hypothesis testing that will be useful as well and if something is not statistically significant, then flag those off, drop those analyses, do whatever you think is the best thing to do. I like charts. So, give me chart and give me pretty charts. You use matplotlib usually which is fine, go ahead and use it, but the thing is by default it looks ugly. So, think about all the beautiful data visualizations that people create, do something like that. I want to win an award with this visualization.

---

## Metaprompt to write code

<small>

I liked all of these stories that had scatter plots in them. The only issue is that there were outliers, so I would like those removed. Now, what I want you to do is give me a prompt that I will pass to an LLM along with the data set and it should write the code as HTML JavaScript in a way that I can publish on to GitHub pages. Remember that this means that we cannot have such a large data set being uploaded on to GitHub pages and users viewing it. You need to figure out some way in the prompt of telling the LLM to create these using HTML CSS JavaScript in a way that conveys the scatter plot, but without having to load the entire data set. I am ok with the page loading data of probably up to 1 or 2 megabytes. Keep that in mind, do analysis if you need to and write the prompt.

</small>

---

## Prompt to improve visual

This data visualization was nice, but not beautiful and not a story. So, let us do two things. Imagine you are writing a New York Times data visualization. How would you go about it? What fonts would you use? What color schemes would you use? What design choices would you make? Create a full-fledged data story, take a look at the results that have come out and write it in a way that will get me an award.

---

## Visualizations Created

1. https://sanand0.github.io/booksviz/
2. https://rasagy.in/books-viz/
3. https://rishabhmakes.github.io/llm-dataviz/
4. https://devanshikat.github.io/BooksVis/
5. https://nchandrasekharr.github.io/booksviz/
6. http://coffee-reviews.prayashm.com/
7. https://story-b0f1c.web.app/

---

# Prompt to Plot

#### [Crafting Visual Stories with LLMs](https://hasgeek.com/VizChitra/prompt-to-plot/) | [Slides](https://sanand0.github.io/talks/2025-06-28-prompt-to-plot/)

[VizChitra](https://vizchitra.com/) · 28 June 2025, 10:00 am IST · [Bangalore](https://maps.app.goo.gl/VsnBZmVpA6Sxmyje7)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)
[Video](https://youtu.be/SdDulR-1bBM)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-06-28-prompt-to-plot/)

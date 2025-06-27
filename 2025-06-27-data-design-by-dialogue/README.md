---
marp: true
title: Prompt-to-Plot
author: Anand S
url: https://sanand0.github.io/talks/2025-06-27-data-design-by-dialogue/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
# <iframe src="https://sanand0.github.io/" frameborder="0" style="width:100%; aspect-ratio: 5/2"></iframe>
---

<style>
  blockquote {
    font-style: italic;
  }

  section {
    background-image: url('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-06-27-data-design-by-dialogue/');
    background-repeat: no-repeat;
    background-position: top 20px right 20px;
    background-size: 80px auto;
  }
</style>

# Data Design by Dialogue

#### [Visualizing Data with LLMs](https://hasgeek.com/VizChitra/2025/schedule/data-design-by-dialogue-visualizing-data-with-llms-RM88yTfBNKrgSAJFiL2RQL) | [Slides](https://sanand0.github.io/talks/2025-06-27-data-design-by-dialogue/)

[VizChitra](https://vizchitra.com/) · 27 June 2025, 4:15 pm IST · [Bangalore](https://maps.app.goo.gl/fujVnPiBKaQhuZ3V9)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-06-27-data-design-by-dialogue/)

---

# LLMs can help in every step of the data to story value chain

- **Data Engineering**: Scraping, Cleaning, ...
- **Data Analysis**: Modeling, Insight generation, ..
- **Data Visualization**: Charting, Narrations, ...

Best democratization of data stories since Open Data.

---

## [Scraping WhatsApp](https://chatgpt.com/share/685d8a3d-384c-800c-87d9-85837b5f91a8)

Let's have [ChatGPT](https://chatgpt.com/) build us a scraper:

> I want to scrape data from a WhatsApp group by pasting JavaScript code on the DevTools console. I want you to write the code for that.
>
> Give me code that I can paste in the console that will copy any HTML or anything else from the WhatsApp web page (making sure it's not too long -- trim as required) into the clipboard. I'll paste it here. You can then write the code to scrape all the useful information in each message as an array of JSON objects.

---

## Tactics I learnt

LLMs err. Have them write code!

So, now, _anyone_ can code.

Expertise helps. But it's easier to develop.

---

## [Cleaning Data](https://chatgpt.com/share/685d8b22-ad28-800c-b283-74a0757cadfe)

> Here are WhatsApp messages. Any missing values?

– **Reactions** blank for ~64% (no reactions).
– **Author** null ~6% (system messages).
– **Time** null ~5.5% (parsing glitches).
– **Text** blank ~0.8% (likely media or deleted).

> Interpolate/extrapolate **time** from nearby messages. Give me a .json.gz download.

---

## Tactics I learnt

Practice delegating more. LLMs keep improving.

---

## Modeling Topics

<video style="float:left; margin-right: 4rem" controls width="500" loop autoplay playsinline muted src="similarity.webm"></video>

LLMs also use _[embeddings](https://en.wikipedia.org/wiki/Word_embedding)_. From these messages, let's see:

1. What messages are similar
2. Cluster into groups
3. Name each clusters

> Let me download all the .text fields as a CSV file.

Apply a [Topic Modeling tool](https://llmfoundry.straive.com/classify)

---

## [Modeling Topics](claude-code.txt)

Let's use [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) to [code it](topics.py):

> `whatsapp.json.gz` has WhatsApp msgs. Write `topics.py` to
>
> - calculate the embeddings of each `.text` <!-- with OpenAI's text-embedding-3-small -->
> - cluster embeddings using K-Means into 12 clusters
> - use gpt-4.1-mini to name all clusters <!-- Collate ALL messages for ALL clusters and send a single message asking it to name each cluster - especially in a way that CLEARLY differentiates the clusters. Use OpenAI's structured JSON output feature to get the cluster names as a JSON array -->
> - create `tagged.json` that adds a `cluster:` to each message
> - test on 20 messages & 3 clusters. Then, run for all. <!-- Add inline script metadata using use uv run topics.py. Print progress. -->

- Cost: $0.67. Time: 22m while eating [Paneer Kurchan Tacos](https://g.co/kgs/VDgPqTr)

---

## Tactics I learnt

Throw it away and redo. It's easier than fixing.

---

## [Visualizing Stories](https://chatgpt.com/share/685d8fe5-c288-800c-9d87-0661859153f3)

> These messages are from the VizChitra group.
> What interesting insights can we derive from these?
> List 10 diverse data stories we can explore. Include quirky ones.
> Then, for each of those, write the code to analyze the data.
>
> Show the results as tables and charts and interpret each as a story with surprise & human appeal.
>
> Amuse me!

---

## Tactics I learnt

Have LLMs **Write code** to analyze.

Don't ask for one. Ask for a dozen analyses.

Keep an impossibility list. Review monthly.

---

## [Let's jam!](https://chatgpt.com/share/685d8fe5-c288-800c-9d87-0661859153f3)

What questions would _you_ like to ask? E.g.:

> Correlate all metric pairs you can think of into a single scatterplot matrix and give me interesting stories.

> More metrics! More quirky!

> Redraw with Seaborn (not matplotlib) and make it beautiful! Award winning!!

> Make an interactive D3 data viz to visualize these.

---

# LLMs can help in every step of the data to story value chain

- **Data Engineering**: Scraping, Cleaning, ...
- **Data Analysis**: Modeling, Insight generation, ..
- **Data Visualization**: Charting, Narrations, ...

Try it! See where it works and fails.

---

## Data Design by Dialogue

#### [Visualizing Data with LLMs](https://hasgeek.com/VizChitra/2025/schedule/data-design-by-dialogue-visualizing-data-with-llms-RM88yTfBNKrgSAJFiL2RQL) | [Slides](https://sanand0.github.io/talks/2025-06-27-data-design-by-dialogue/)

[VizChitra](https://vizchitra.com/) · 27 June 2025, 4:15 pm IST · [Bangalore](https://maps.app.goo.gl/fujVnPiBKaQhuZ3V9)
[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-06-27-data-design-by-dialogue/)

# Activities

1. **Use ChatGPT to scrape WhatsApp messages from the browser console**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT
  - What happened: Anand asked ChatGPT for JavaScript that could copy WhatsApp web content into the clipboard and extract messages as JSON.
  - Source:
    > `I want to scrape data from a WhatsApp group and I just want to do that by pasting JavaScript into the DevTools console.`
     >
    > `you can then write the code to scrape all the useful information in each message and give it to me as an **array of JSON objects**.`

2. **Use ChatGPT to detect missing values and impute timestamps**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT
  - What happened: Anand uploaded the cleaned WhatsApp messages, asked for missing values, and then asked it to interpolate or extrapolate missing times.
  - Source:
    > `Here are a bunch of WhatsApp messages. Are there any missing values here?`
     >
    > `Interpolate or extrapolate the time from the nearby messages.`

3. **Use Claude Code to write a topic-modeling script for WhatsApp messages**
  - Who: speaker
  - When: during the talk
  - Model/tool: Claude Code
  - What happened: Anand had Claude Code write `topics.py` to embed messages, cluster them, name clusters with GPT-4.1, and create a tagged output file.
  - Source:
    > `This one I wrote using Claude Code.`
     >
    > `What I prompted it was literally what you see here. "I've got this JSON.gzip file. Now I want you to write a Python program, call it topics.py."`
     >
    > `calculate the embeddings of each of the text fields. Cluster them using K-Means and then send it to GPT 4.1 to give me names for all of those.`

4. **Rerun the topic-modeling script until cluster names improve**
  - Who: speaker
  - When: during the talk
  - Model/tool: Claude Code / LLM workflow
  - What happened: Anand reran the clustering workflow after the first names were poor.
  - Source:
    > `So, like always, I'm just going to rerun it and hopefully it will give me better cluster names.`
     >
    > `The magic rule is **try it again**.`

5. **Use ChatGPT to generate 10 quirky data stories and analysis code**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT
  - What happened: Anand asked ChatGPT for ten story ideas, code to analyze them, and story-like interpretations.
  - Source:
    > `Give me **10 diverse data stories** that we can explore.`
     >
    > `Then, for each of those, **write the code to analyze the data**.`
     >
    > `Interpret each as a story with surprise and human appeal. **Amuse me**!`

6. **Use O3 to turn the WhatsApp data into charts and story narratives**
  - Who: speaker
  - When: during the talk
  - Model/tool: O3
  - What happened: Anand switched to O3 and let it generate charts plus narrative insights from the data.
  - Source:
    > `I'm going to consciously switch over to O3.`
     >
    > `At the end of it, notice that it's creating charts and it's probably got the stories below.`

7. **Ask ChatGPT to write and apply an Economist-style guide to Matplotlib charts**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT
  - What happened: After the audience asked for the latest failure mode, Anand described asking ChatGPT to make Economist-style charts in Matplotlib.
  - Source:
    > `I said, "Create. Take all the charts from the Economist.`
     >
    > `You write the style guide. And then you rewrite it in a form that is suitable for Matplotlib.`
     >
    > `it was rubbish.`

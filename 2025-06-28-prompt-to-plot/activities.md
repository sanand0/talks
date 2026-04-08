# Activities

1. **Write the slide deck using LLMs**
  - Who: speaker
  - When: before the talk
  - Model/tool: LLMs; specific model not named
  - What happened: Anand says the deck itself was made with LLM help on the morning of the workshop.
  - Source:
    > `**Today we are going to be using LLMs for everything.** I wrote this deck this morning using LLMs.`

2. **Have the audience create and publish data stories using only LLMs**
  - Who: audience
  - When: during the talk
  - Model/tool: LLMs; specific model not named
  - What happened: The workshop goal was for participants to make and publish stories with AI doing the work.
  - Source:
    > `You can individually come up with data stories. But **let's publish a few today, and ideally only using LLMs.**`

3. **Use ChatGPT by voice to find a dataset for the workshop**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT
  - What happened: Anand used ChatGPT as the live dataset-finding assistant and explained why he preferred speaking to it.
  - Source:
    > `Now comes the hard part, which is finding a data set. Any suggestions? No, why am I saying? You're my LLM. ChatGPT.`
     >
    > `**The advantage of speaking to an LLM is you can do stuff like this.**`

4. **Ask ChatGPT to suggest visual story ideas from the Goodreads dataset**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT
  - What happened: Anand fed the dataset columns to ChatGPT and asked it for story ideas and AI-assisted coding directions.
  - Source:
    > `These are the columns in the Goodreads 100k data set. I would like to create interesting data stories out of it that can also be visualized nicely. Can you give me a dozen suggestions on, A, what stories to write, B, who they would be interesting to and why, and C, how I might go about doing this by having an LLM write code to do it?`

5. **Run Jules and Codex in parallel on the same repo**
  - Who: speaker
  - When: during the talk
  - Model/tool: Jules and Codex
  - What happened: Anand used two coding agents side by side to generate alternative implementations.
  - Source:
    > `So I'm going to run Jules and Codex in parallel.`
     >
    > `For both Jules and for Codex, you give it a GitHub repository, tell it what code changes you want it to make, it will make them.`

6. **Ask ChatGPT how to work around GitHub’s upload limit**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT
  - What happened: Anand used ChatGPT to troubleshoot an oversized dataset upload.
  - Source:
    > `I refuse to give up, and I will follow my advice, which is ask ChatGPT. "I have a 29MB .xz and a 46 MB .zip file that I want to upload into GitHub via the UI. I am unable to. Any options? I definitely want to commit."`

7. **Use Codex and Jules to debug generated output from error messages**
  - Who: speaker
  - When: during the talk
  - Model/tool: Codex and Jules
  - What happened: Anand copied error details back into the agents and asked them to fix the generated app.
  - Source:
    > `I'm going to say, "I got an error. It couldn't load \`scatter_data.gz\`." Fix it.`
     >
    > `Like before, I will pass this input to Jules and say, "I got this error. Fix it."`

8. **Use ChatGPT as a scratchpad to draft a refinement prompt**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT
  - What happened: Anand dictated a prompt for turning the current visualization into a fuller narrative story.
  - Source:
    > `And now I'm going to use ChatGPT purely as a recording tool, not to actually send a prompt.`
     >
    > `What I want to tell it is, this data visualization was nice, but not beautiful and not a story.`

9. **Switch to Claude Code locally to improve the generated story and design**
  - Who: speaker
  - When: during the talk
  - Model/tool: Claude Code
  - What happened: After trying Codex and Jules, Anand used Claude Code from the command line to improve the result.
  - Source:
    > `This command runs Anthropic AI's Claude code using \`npx\`.`
     >
    > `I'm going to paste the same prompt that I had asked Codex, which is, "Look at \`README.md\`..." Copy this thing. "The data visualization was nice, blah blah blah, and give me a full-fledged data story."`

10. **Have participants generate and publish their own AI-made stories**
  - Who: audience
  - When: during the talk
  - Model/tool: Jules and Codex
  - What happened: Participants showed AI-generated outputs, including stories made with Jules and Codex.
  - Source:
    > `_Another audience member shares their screen._`
      >
    > `And this was from Jules. Okay, that is even more impressive.`
      >
    > `Maybe you published from Jules, whereas the content you saw earlier was from Codex.`
      >
    > `So congratulations, you've created two stories!`

11. **Use a command-line LLM to write a commit message**
  - Who: speaker
  - When: during the talk
  - Model/tool: Simon Willison's `llm`
  - What happened: Anand passed a diff to a command-line LLM and used its suggested commit message.
  - Source:
    > `I will do a \`git diff\` and pass it through a command line LLM.`
      >
    > `You can run LLM commands on the command line using Simon Willison's LLM. I've tweaked it a little bit so that it will create a commit message for me`

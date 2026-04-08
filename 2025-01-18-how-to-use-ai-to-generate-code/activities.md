# Activities

1. **Prompt an AI coding tool to generate a demo election dashboard**
  - Who: speaker
  - When: during the talk
  - Model/tool: AI coding tool with a Canvas approach; tool not explicitly named in the source
  - What happened: Anand asked the tool to create a realistic election-dashboard prototype that he could show to a client.
  - Source:
    > `**Prompt:** _"Create an election dashboard for Indian national elections. It should look really beautiful and be interactive and media should love it. Give me a design for this that I can build on top of, but make it like a demo that looks like it's real so that I can show it to the client. Put in names of Parties A, B, C and all of that stuff."_`
     >
    > `It’s writing some fairly detailed code using React and Recharts.`

2. **Iteratively revise the generated dashboard with a follow-up prompt**
  - Who: speaker
  - When: during the talk
  - Model/tool: same AI coding tool as above; tool not explicitly named in the source
  - What happened: Anand used a second prompt to fit the dashboard on one screen and add animation.
  - Source:
    > `**Prompt:** _"I want it to fit in one screen. Add animation. Things should bounce around because clients like that sort of thing."_`
     >
    > `Now what it is going to do is **revise the code that it wrote earlier**.`

3. **Use ChatGPT Voice Mode to answer a live audience question**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT Voice Mode
  - What happened: Anand asked ChatGPT how a non-programmer could create a stock-trading app.
  - Source:
    > `**Anand:** Actually, rather than me taking this, let's do one thing. Let's ask ChatGPT.`
     >
    > `**Anand (to ChatGPT):** How can a person who is not a programmer create an application that helps them trade better on the stock market?`

4. **Use a two-step LLM workflow to turn rough prompts into specs and then code**
  - Who: speaker
  - When: before the talk
  - Model/tool: LLMs; specific models not named
  - What happened: Anand described an internal workflow where one model expands a rough prompt into a full specification and a second model generates code from it.
  - Source:
    > `Internally in our organization, we found that people give terrible prompts.`
     >
    > `Step 1: One LLM takes the user's rough prompt and creates a **full-fledged specification** that is enough for a software developer.`
     >
    > `Step 2: Pass that specification to the model to generate the code.`

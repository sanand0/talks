# Activities

1. **Use `llm` to learn DuckDB SQL during the talk**
  - Who: speaker
  - When: during the talk
  - Model/tool: Simon Willison's `llm`
  - What happened: Anand used `llm` as a command-line assistant to generate DuckDB SQL.
  - Source:
    > `Let's learn DuckDB using \`llm\`.`
     >
    > `.shell llm "Write DuckDB SQL: ..."`

2. **Use `ask` to speak questions and have Gemini transcribe them into SQL**
  - Who: speaker
  - When: during the talk
  - Model/tool: `ask` via Gemini 2.5 Flash
  - What happened: Anand described an audio-to-SQL workflow where he asks questions by voice.
  - Source:
    > `Typing is boring. Let's **ask** our questions.`
     >
    > `It records audio via \`ffmpeg\`, and`
     >
    > `Sends it to Gemini 2.5 Flash via \`llm\``

3. **Use ChatGPT code interpreter to run DuckDB inside ChatGPT**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT code interpreter
  - What happened: Anand uploaded a DuckDB wheel so ChatGPT could execute DuckDB code.
  - Source:
    > `You can run DuckDB in ChatGPT`
     >
    > `ChatGPT code interpreter cannot \`pip install duckdb\`.`

4. **Ask ChatGPT which Python and DuckDB wheel to use**
  - Who: speaker
  - When: during the talk
  - Model/tool: ChatGPT
  - What happened: Anand used ChatGPT to figure out compatibility before uploading the wheel.
  - Source:
    > `PS: To find the right \`.whl\` verion, I asked:`
     >
    > `What version of Python are you using?`
     >
    > `Which DuckDB version will run in your container?`


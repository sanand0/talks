# Activities

1. **Use Simon Willison's `llm` CLI for quick prompts**
  - Who: speaker
  - When: before the talk
  - Model/tool: `llm` CLI
  - What happened: Anand used a terminal LLM client for quick answers without leaving the shell.
  - Source:
    > `llm` is Simon Willison's command line LLM client
    > `uvx llm -m gpt-4.1-nano 'What is 2 + 2?'`

2. **Wrap `llm` in a `pyrun()` helper to generate and execute Python**
  - Who: speaker
  - When: before the talk
  - Model/tool: `llm`, `uv run`
  - What happened: Anand defined a shell function that asks for concise Python code and runs it directly.
  - Source:
    > `## Let's create a function`
    > `pyrun() {`

3. **Use `pyrun` to generate data, visuals, and scraped outputs**
  - Who: speaker
  - When: before the talk
  - Model/tool: `pyrun`, `llm`
  - What happened: Anand showed examples for fake data, images, geojson, CSV cleaning, plotting, scraping, and browser automation.
  - Source:
    > `pyrun Generate fake student data. Save as JSON and CSV`
    > `pyrun Render cities.geojson as an interactive Folium map`

4. **Ask ChatGPT to write a Pydantic AI agent that executes Python code**
  - Who: speaker
  - When: before the talk
  - Model/tool: ChatGPT, Pydantic AI
  - What happened: Anand used ChatGPT to generate an agentic coding example.
  - Source:
    > `Let's prompt ChatGPT to:`
    > `Write a Pydantic AI 0.4 agent that executes Python code`

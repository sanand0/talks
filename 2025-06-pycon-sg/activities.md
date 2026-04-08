# Activities

1. **Present Hypothesis Forge as a one-click browser analysis app**
  - Who: speaker
  - When: before the talk
  - Model/tool: Pyodide + Web Worker, with LLM-generated code
  - What happened: Anand showed a browser app that runs pandas and SciPy on CSVs without a backend.
  - Source:
    > `## Hypothesis Forge: Automating Analysis`
     >
    > `**One-click insights** over _any_ CSV right in the browser-no backend, no install`
     >
    > `After the LLM generates code, here's how we run it.`

2. **Use `llm` CLI to generate executable Python code**
  - Who: speaker
  - When: before the talk
  - Model/tool: Simon Willison's `llm`
  - What happened: Anand showed the command-line LLM client generating code that can be piped into Python.
  - Source:
    > `## \`llm\` is Simon Willison's command line LLM client`
     >
    > `## It can write code you can execute`

3. **Wrap `llm` in a `pyrun()` helper for repeatable prompt-to-code runs**
  - Who: speaker
  - When: before the talk
  - Model/tool: Simon Willison's `llm`
  - What happened: Anand defined a shell helper that turns prompts into short inline Python scripts.
  - Source:
    > `## Let's create a function`
     >
    > `pyrun() {`

4. **Use `pyrun` to generate, clean, transform, and analyze data**
  - Who: speaker
  - When: before the talk
  - Model/tool: `llm` via `pyrun`
  - What happened: Anand showed prompts for generating fake data, converting CSVs, cleaning rows, and running data science tasks.
  - Source:
    > `## Generate data`
     >
    > `pyrun Generate fake student data. Save as JSON and CSV`
     >
    > `## Clean data`
     >
    > `pyrun Create _cleaned.csv versions of all CSVs dropping missing values`

5. **Use `pyrun` to visualize, scrape, and automate the browser**
  - Who: speaker
  - When: before the talk
  - Model/tool: `llm` via `pyrun`
  - What happened: Anand showed prompts for charts, maps, web scraping, and browser automation.
  - Source:
    > `## Visualize data`
     >
    > `pyrun "From vega_datasets flights_2k data, save daily flight count as a line chart flights.png"`
     >
    > `## Automate the browser`
     >
    > `pyrun Using Playwright, save a screenshot of https://example.com as example.png`

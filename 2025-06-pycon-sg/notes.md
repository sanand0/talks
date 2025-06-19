# Notes from PyCon SG 2025

## Python performance: a personal retrospective and prospective

- Ken Jin – CPython Core Developer (kenjin@python.org). 9:30 am, Day 1
- Python is the slowest language among the GitHub top 10 languages, except for Shell
- Python 3.11+ dynamically rewrites bytecode. If it knows X is an integer, it replaced BINARY_OPP (ADD) -> BINARY_OPP_ADD_INT [Specializing Adaptive Interpreter: PEP 659](https://peps.python.org/pep-0659/)
- CPython 3.13+ uses a JIT compiler optimizer. E.g. if it adds a + b and has checked a and b are integers, it drops the bytecode to check if the sum is an integer [PEP 744](https://peps.python.org/pep-0744/)
- Python 3.14 is 40% faster than 3.10. Mainly because of the specialized byte-code interpreter (25%). Rest are incremental, e.g. Garbage collection changes, Reference counting changes
- Notes on reference counting:
  - Python does not clear small integers when garbage collecting for performance.
  - If you use `f = open("file")` Python _does_ close the file when `f` goes out of scope. Core devs prefer flexibility to change this in the future, but it's _very_ unlikely since it'll break a lot of code.
  - If reference counts go to zero, it's automatically freed immediately. Generally, garbage collection is not required.
- Optimization plans:
  - Constant propagation. Pre-compute operations with constants [#113710](https://github.com/python/cpython/issues/113710)
  - Reference counting. If a reference is going to be consumed _immediately_ we can skip reference counting, e.g. replace `BIG_INT_ADD` with `BIG_INT_ADD__NO_REF`
- To contribute to Python
  - You don't need to know C
  - The CPython Guide has excellent developer documentation
  - Pick an area you care about
  - Contribute via reviewing PRs, raising issues, writing docs, writing tests, writing code, evangalization
  - Some universities allow open source work as student credit. Some organizations have programs to support
- #Q: Will this improvement carry over to WASM?
  - Bytecode compilations carry over
  - JIT compilations require some VM features that don't have WASM support

## L7. Lightning Talks. – 1:30 pm, Day 1

- [Yocto Project](https://www.yoctoproject.org/) creates custom embedded Linux distributions.
- [OrangeTree](https://orange3.readthedocs.io/) supports
  [visual programming](https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/index.html) in Python. It supports xenographics like
  [Nomogram](https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/visualize/nomogram.html),
  [Mosaic](https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/visualize/mosaicdisplay.html),
  [Pythogorean Tree](https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/visualize/pythagoreantree.html),
  [FreeViz](https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/visualize/freeviz.html),
  [RadViz](https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/visualize/radviz.html), etc.
  (Talk by [Tze Houng Lee](https://www.linkedin.com/in/leetzehoung/), thlee018@suss.edu.sg)
- A few people who introduced themselves.
  - Siddharta Govindaraj, Silver Stripe Software, India
  - Stefan, Bangkok. Perl, JSConfCN.
  - Sridhar, Singapore. Coherent. Principal DevOps Engg.
  - Vivek, Hyderabad. EPAM. Back-end engineering.
  - Bloomberg has a large Python team.
- [Reflex](https://reflex.dev/) and [Flet](https://flet.dev/) are web app builders in Python

## Python Beats: Live Coding Music with Python. Paul Amazona. 2:30 pm, Day 1

[BespokeSynth](https://www.bespokesynth.com/) is a composable Python-based music synthesizer.

## Beyond P values: Data Analysis with Bootstrapped ESTimation (DABEST). Mai Yishan – Duke-NUS. 3:15 pm, Day 1

- p-values do not communicate numerical significance, only statistical significance. It encourages binary thinking (pass/fail).
- [DABEST](https://acclab.github.io/DABEST-python/) is a Python data visualization library to visually communicate statistics.

## Firecracker Made Easy with Python. Muhammad Yuga Nugraha – Practical DevSecOps. 4 pm, Day 1

- Micro VMs like FireCracker are lightweight VMs + containers. (Apple containers are Micro VMs)
- They're fast, not as fast as docker, and provide high isolation
- Firecracker is used by: [CodeSandbox](https://codesandbox.io/), [E2B](https://e2b.dev/), [Iximiuz](https://labs.iximiuz.com/)
- Does not run on Windows.
- Firecracker is controlled via REST APIs
- Requires non-trivial network setup
- Good for: Serverless, CI/CD, malicious code.
- Bad: No registry, no `docker exec`, less mature

# CDK Development with Python for Automation, Sreedhar Bukya, 4:50 pm, Day 1

- CDK compiles code-based configurations into AWS CloudFormation YAML. It's an Amazon-initiated open source project.
- Pick CDK when you live inside AWS and want infrastructure expressed in a familiar programming language with CloudFormation-grade safety nets.
- Pick OpenTofu when you need a truly vendor-neutral, HCL-based, Terraform-compatible tool run by a community under Linux Foundation stewardship.
- If you need both, use CDKTF (CDK for Terraform) or wrap OpenTofu modules in your language of choice.

[ChatGPT](https://chatgpt.com/share/685280ab-2ae4-800c-9c97-a9fece550e3a)

## Generative AI Monitoring with PydanticAI and Logfire. Marcelo Trylesinski – Pydantic. 9:15 am, Day 2

- [Website](fastapiexpert.com) | [Dotfiles](https://github.com/kludex/dotfiles) via [chezmoi](https://www.chezmoi.io/)
- LogFire is a freemium (10M spans/month) observability product [compatible](https://logfire.pydantic.dev/docs/how-to-guides/alternative-clients/) with [OpenTelemetry](https://opentelemetry.io/)
- Neither in FastAPI nor in Pydantic AI do you need to use Pydantic classes. Types work just fine (and are faster). Classes are required only for complex structures.
- Pydantic AI only supports OpenAI chat completions APIs
- Favorite MCP servers: GitHub (requires auth, which is hard), VS Code, Playwright, Logfire
- MCPs support sampling, where the MCP can ask the client to run an LLM call and pass the results back. Marcelo will merge the [PR](https://github.com/pydantic/pydantic-ai/pull/1884) today
- ⭐ The agent stops the loop when there are no more tool calls to run (if `end_strategy="exhaustive"`) or the first output is received (if `end_strategy="early"`). That's simple and clever!
- Use `output_type=another_agent_instance` lets you chain agents, but we're working on a more intuitive naming/mechanism

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "logfire",
#     "opentelemetry-instrumentation-httpx",
#     "pydantic-ai",
#     "tavily-python",
# ]
# ///
from pydantic_ai import Agent
import os
import datetime
import logfire
import sys
from pydantic_ai.common_tools.tavily import tavily_search_tool
from pydantic_ai.mcp import MCPServerStdio

logfire.configure()
logfire.instrument_pydantic_ai()
logfire.instrument_httpx(capture_all=True)

mcp_server = MCPServerStdio(
    command="/run/user/1000/fnm_multishells/524565_1750223552456/bin/npx",
    args=["-y", "@playwright/mcp@latest"],
)

agent = Agent(
    # "openai:gpt-4.1-nano",
    'anthropic:claude-sonnet-4-0',
    tools=[tavily_search_tool(api_key=os.getenv("TAVILY_API_KEY"))],
    mcp_servers=[mcp_server],
    instructions="Use the browser MCP rather than the search tool for browsing.",
)


@agent.tool_plain
def get_date_prior(days: int) -> str:
    """Returns the date prior to today by a specified number of days."""
    return (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")


async def main():
    async with agent.run_mcp_servers():
        result = await agent.run(sys.argv[1])
        print(result.output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Gentle Introduction to MCP

- MCPs collate tools, resources, and prompts
- MCPs connect via stdio, SSE, or streamable HTTP
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) is another local LLM client that supports LLMs
- MCPs make sense over direct tool/API use at least for
  - discovery
  - multiple endpoints
  - local services (e.g. file editing)
  - encapsulated reuse

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastmcp",
#     "httpx",
# ]
# ///
import httpx
from fastmcp import FastMCP

mcp = FastMCP(name='Pokemon abilities')

@mcp.tool
async def fetch_pokemon_abilities(pokemon_name: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        if response.status_code != 200:
            return f"Error fetching data for Pokémon: {pokemon_name}"
    data = response.json()
    abilities = [ability['ability']['name'] for ability in data.get('abilities', [])]
    return f"{pokemon_name.capitalize()} = {', '.join(abilities)}"
```

Run with `uv run --with fastmcp fastmcp dev server.py` and test via the inspector it provides.

## Vertical AI Agents. Ng Jin Pei – NUS. 11:15 am, Day 2

## AI Accessibility: How to keep your users from rage quitting? Anushka Narula – Adobe. 11:15 am, Day 2

- Works on Adobe Express, which incorporates AI features. Her presentation was built using Adobe Express
- Making content accessible makes them LLM / agent friendly too!
- Standard accessibility applies to LLM apps too
- "Avoid overusing ARIA." Regular HTML should be enough. Prefer `<button>` over `<div aria-role="button">`
- [Axe](https://www.deque.com/axe/) lets you automate accessibility testing. Available in Python, JS, Chrome extension
- Playwright can help test keyboard navigation. Use LLMs to generate test cases or pass it to a computer use agent for live testing!
- Think about it. If a chatbot pops up on a screen reader, how would it trigger for the user? How would they switch to it?
- Make sure errors are visible, explain _what_ happened, _where_ it happened, and _what_ the user needs to do. In a way screen-readers can handle

## Lightning Talks. – 1:30 pm, Day 2

- [PyConSG Education Summit](https://pycon.sg/edusummit.html) is happening at SUTD on Mon 11 Aug, 2025
- The "Mean Circuity" visualization on the [Singapore MRT/LRT in 2040](https://panda.observer/singapore-mrt-2040/) page shows the average (MRT distance / Euclidean distance) to each station. Clever!
- [Marimo](https://marimo.app/) solves 3 problems:
  - Changing a variable changes all dependent cells, like Excel
  - They're just Python scripts. So `git diff`s are cleaner
- [htmx](https://htmx.org/) by [Ronan Berder](https://github.com/hunvreus). But the browser API will probably replace:
  - `hx-boost` for AJAX navigation + history with [Navigation API](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API)
  - `hx-swap` for element transitions with [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
  - `hx-sse` with [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)

## ⭐ L7. Every Day is Day 1: Secure your LLM Application with Testing & Guardrails. Goh Jia Yi – GovTech. 2:30 pm, Day 2

## Unlock the Lock: Mastering Python Multithreading Deadlocks Before They Master You. Han Qi – Monarch Tractor APAC. 2:30 pm, Day 2

## ⭐ L7. Improving Cloud-Support Productivity with Textual. Piti Champeethong – MongoDB. 3:15 pm, Day 2

## Boosting API Reliability: Property-Based Testing in Action. Vivek Kishore – EPAM. 3:15 pm, Day 2

## Beyond the Prompt: Navigating the GenAI World as a Python Developer. Thu Ya Kyaw – Google. 4 pm, Day 2

## Day 2 Closing. – 4:45 pm, Day 2

## What’s Good in Singapore? A Personalised Food Recommender with Python. Ho Wei Sin – MOE. 9 am, Day 3

## ⭐ L7. pip install Agent: Crafting AI Agents with Python. Thu Ya Kyaw – Google. 9 am, Day 3

## Python 101 Workshop. PyLadiesSG & WomenDevsSG. 9 am, Day 3

## ⭐ L6. Testing GenAI Applications. Adrian Cole – Elastic. 10:30 am, Day 3

## Multimodal RAG in Action: Unlocking Complex Document Retrieval. Zane Lim – Manulife. 10:30 am, Day 3

## Lunch and Networking. – 12 pm, Day 3

## Data Handling and Machine Learning Introduction. En Hao Tew – Singapore Youth AI. 2:30 pm, Day 3

## ⭐ L7. Build Agentic RAG Systems that Decide Like Humans (But Faster). Tarun Jain – AI Planet. 2:30 pm, Day 3

## Python 102 Workshop. PyLadiesSG & WomenDevsSG. 2:30 pm, Day 3

## Build, Deploy, Monetize: Crawlee for Python. Saurav Jain – Apify. 4 pm, Day 3

## ⭐ L7. Writing Bug-Free Python Code with Functional Programming. Siddharta Govindaraj – Silver Stripe Software. 4 pm, Day 3

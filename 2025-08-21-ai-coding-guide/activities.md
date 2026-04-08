# Activities

1. **Parallel-prototype with `k` variants before sharing outcomes**
  - Who: speaker
  - When: during the talk
  - Model/tool: AI coding tools
  - What happened: Anand told the audience to try multiple variants first and only then share results.
  - Source:
    > `Don't commit to your manager/client. Build it. Then share it.`
    > `Do next: run _k_ variants, _then_ talk.`

2. **Treat specs and tests as the product**
  - Who: speaker
  - When: during the talk
  - Model/tool: schema-constrained outputs, PR diffs
  - What happened: He recommended keeping prompt/spec docs and using structured outputs instead of free-form code.
  - Source:
    > `Specs/tests _are_ the product. Code is a build artifact`
    > `keep PROMPTS.md/SPEC.md; use schema-constrained outputs`

3. **Optimize the validation loop with property tests and evals**
  - Who: speaker
  - When: during the talk
  - Model/tool: Copilot-style tools, evals, property tests
  - What happened: Anand told the audience to add property tests, hidden tests, and gate merges on evals.
  - Source:
    > `Optimize the validation loop, not the coding loop`
    > `add property tests ... gate merges on evals`

4. **Make repos LLM-friendly**
  - Who: speaker
  - When: during the talk
  - Model/tool: LLM-friendly repo patterns
  - What happened: He recommended llms.txt, small files, fast tests, and sample fixtures.
  - Source:
    > `Make repos "LLM-friendly"`
    > `add llms.txt ... keep small files`

5. **Prefer typed languages and DSLs**
  - Who: speaker
  - When: during the talk
  - Model/tool: JSON Schema, OpenAPI, DSLs
  - What happened: He advised typed APIs and DSLs instead of free-form code where possible.
  - Source:
    > `Prefer typed languages & DSLs`
    > `emit DSLs ... instead of free-form code`

6. **Run short feedback loops and many small PRs**
  - Who: speaker
  - When: during the talk
  - Model/tool: lint/test/typecheck loops
  - What happened: Anand recommended very fast CI and small pull requests.
  - Source:
    > `Re-design process around _short feedback loops_`
    > `CI must be <2 minutes; default to many small PRs.`

7. **Build evals-in-the-loop**
  - Who: speaker
  - When: during the talk
  - Model/tool: iterative systems, auto-benchmarking
  - What happened: He told the audience to spin up multiple variants and merge winners only.
  - Source:
    > `Always build evals-in-the-loop`
    > `spin N variants per change; auto-benchmark`

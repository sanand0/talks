# Activities

1. **Build claim-verification checks that explain why an insurance claim is rejected**
  - Who: speaker
  - When: during the talk
  - Model/tool: InsureLLM / programmatic checks
  - What happened: Anand showed claim-processing rules that convert claims into facts and run deterministic checks to produce auditable rejection reasons.
  - Source:
    > `This is not LLM generated. This is a program running a check, and cannot go wrong.`
    >
    > `it is able to tell us the "why" a claim is rejected`

2. **Run an API agent against FRED and let a validator self-correct the code**
  - Who: speaker
  - When: during the talk
  - Model/tool: API agent, validator, cheap model
  - What happened: Anand intentionally used a cheap model, let it fail on an API request, and then used the error message plus a validator loop to fix it.
  - Source:
    > `I'm intentionally going to pick a cheap model to demonstrate where it might fail.`
    >
    > `Now this is where the error message comes in handy`
    >
    > `the validator that says let's revise this`

3. **Use an LLM-as-a-judge over a golden dataset to verify agent output**
  - Who: speaker
  - When: during the talk
  - Model/tool: LLM-as-a-judge
  - What happened: Ankor described creating golden datasets and training a second LLM to judge new outputs against them.
  - Source:
    > `Along with human experts in the loop, over 50% of these agents utilize an LLM-as-a-judge strategy.`
    >
    > `you would prepare a golden dataset`
    >
    > `and judge the new output that was produced`

4. **Let coding agents self-correct in a continuous verification loop**
  - Who: speaker
  - When: during the talk
  - Model/tool: coding agents
  - What happened: Anand emphasized using code-writing agents that can iterate, run, fail, and fix themselves until verification passes.
  - Source:
    > `This ability to loop through continuously is the core of agentic behavior.`
    >
    > `The ability to write code and self-correct in the process`

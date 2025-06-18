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

## ⭐ L7. Empowering the Python Community: PSF Involvement and Introducing Python Asia Organization. Iqbal Abdullah – PAO. 10:15 am, Day 1

- #Q: What events should Pythonistas look out for?

## Photo-taking. – 11:45 am, Day 1

## Lunch and Networking. – 12 pm, Day 1

## ⭐ L7. Lightning Talks. – 1:30 pm, Day 1

## ⭐ L7. Python Beats: Live Coding Music with Python. Paul Amazona. 2:30 pm, Day 1

## Diving into LangChain, Streamlit & Claude on Amazon Bedrock to build Gen AI apps. Jiawei Lin – Gen-C. 2:30 pm, Day 1

## ⭐ L7. Beyond P values: Data Analysis with Bootstrapped ESTimation (DABEST). Mai Yishan – Duke-NUS. 3:15 pm, Day 1

- #Q: Any plans for a JS version? Or explicit WASM support?

## Building Cross-Platform Apps in Python with Flet. Cyrus Mante – Accenture PH. 3:15 pm, Day 1

## ⭐ L7. Firecracker Made Easy with Python. Muhammad Yuga Nugraha – Practical DevSecOps. 4 pm, Day 1

- #Q: What's the startup time vs Docker? Should we start 1 container and re-use it or start one for each?

## Build with Django: Your First Steps into Web Development. Freilla Mae Espinola – Misfit. 4 pm, Day 1

## ⭐ L7. Day 1 Closing. – 4:30 pm, Day 1

## Registration. – 8:30 am, Day 2

## Day 2 Opening. – 9 am, Day 2

## ⭐ L7. Generative AI Monitoring with PydanticAI and Logfire. Marcelo Trylesinski – Pydantic. 9:15 am, Day 2

## ⭐ L6. Enlightened with Python: Is it making a difference or making things worse. Yudhapratama Nugraha – ITB. 10:30 am, Day 2

## Vertical AI Agents. Ng Jin Pei – NUS. 11:15 am, Day 2

## ⭐ L6. AI Accessibility: How to keep your users from rage quitting? Anushka Narula – Adobe. 11:15 am, Day 2

## Lunch and Networking. – 11:45 am, Day 2

## Lightning Talks. – 1:30 pm, Day 2

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

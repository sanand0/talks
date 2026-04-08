# Activities

1. **Reverse-engineer censored film URLs into a dataset**
  - Who: speaker
  - When: before the talk
  - Model/tool: browser network inspection; LLM-assisted scraping
  - What happened: The team decoded certificate URL patterns, then used the requests to collect records.
  - Source:
    > `we can try to make sense of how they host this data`
    >
    > `we fed it to an LLM, asked it to generate a scraper`

2. **Use an LLM to generate a scraper from a HAR file**
  - Who: speaker
  - When: before the talk
  - Model/tool: LLM
  - What happened: They exported network traffic as HAR and asked an LLM to write the scraper.
  - Source:
    > `we had to export all the network requests as a HAR file`
    >
    > `we fed this HAR file to an LLM`

3. **Use LLMs for classification, not open-ended analysis**
  - Who: speaker
  - When: before the talk
  - Model/tool: LLM
  - What happened: They used a structured JSON-schema pipeline to classify censor-board notes.
  - Source:
    > `we never use LLMs for analysis`
    >
    > `LLMs are great for classification tasks`

4. **Use a strict schema to turn messy notes into CSV**
  - Who: speaker
  - When: before the talk
  - Model/tool: LLM + JSON schema
  - What happened: The team defined categories and edge cases so the LLM could output structured records.
  - Source:
    > `you can define a nice JSON schema`
    >
    > `always respond in this structure`

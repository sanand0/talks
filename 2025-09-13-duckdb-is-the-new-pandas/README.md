# DuckDB is the new Pandas

PyCon India, Bangalore, 13 Sep 2025

Anand S, LLM Psychologist @ Straive

Slides: <https://sanand0.github.io/talks/>

Ask **Questions** At: Slido.com - 2987 234

LICENSE: CC0 - Public Domain

<!--

Talk: https://cfp.in.pycon.org/2025/talk/W8VJX3/
Venue: [NIMHANS Convention Center](https://maps.app.goo.gl/Uon4KDWDqy65RGim8)

-->

## Why DuckDB?

DuckDB is an embedded analytical database.
Like SQLite, but for analytics.
It's just **SQL**: nothing new to learn

After 12 years of Pandas, I'm shifting to DuckDB because:

1. It's much **faster** (with less memory)
2. It can **query remote** files like Parquet
3. It has a huge **function library** you can extend
4. It's **embedded**. Runs everywhere: browser, Python, R, ...
5. It supports **geospatial** queries
6. It has fast **vector search**
7. ... and **more**!

# Cool feature #1: DuckDB is **MUCH** faster

Our client, a parcels company, asked:

> How many customers send **heavy** parcels across our 120 cities & 200 products?

We need to show this as an _interactive_ viz -- with dynamic filters.

<https://gramener.com/transportcost/>

Data is 17M rows of shipments CSV.

Calculating _unique_ customers over 120 x 200 = 24,000 cells is **slow**.

## Let's see how fast Pandas is

Create a sample dataset.

```bash
uv run make-parcels-data.py
```

Now, we'll calculate unique customers.

```python
import pandas as pd

data = pd.read_csv("parcels.csv")
data.groupby(["city", "prod"])["cust"].nunique()
```

## Let's see how fast DuckDB is

```sql
CREATE TABLE parcels AS FROM 'parcels.csv';

EXPLAIN ANALYZE
SELECT city, prod, COUNT(DISTINCT cust)
FROM parcels
GROUP BY city, prod;
```

## On my system DuckDB was **25 times faster**

Pandas: 4.13 seconds
DuckDB: 0.16 seconds

A slider refreshing in ~0.16 seconds is OK.

4 seconds is **not OK**!

# Cool feature #2: DuckDB **queries** remote files

```sql
INSTALL httpfs;
LOAD httpfs;

CREATE OR REPLACE SECRET github_api (
  TYPE http,
  BEARER_TOKEN getenv('GITHUB_TOKEN')
);

FROM read_json("https://api.github.com/search/repositories?q=duckdb")
SELECT unnest(items, recursive := true)
LIMIT 1;
```

## It can query remote .parquet files directly

You can have **remote databases at S3 prices**!

Dattam Labs scraped ~16M Indian high courts judgements.
Repo: <https://github.com/vanga/indian-high-court-judgments>

```sql
CREATE VIEW judgements AS FROM
  's3://indian-high-court-judgments/metadata/parquet'
  '/year=*/court=*/bench=*/metadata.parquet';

FROM judgements SELECT COUNT(*);

FROM judgements SELECT COUNT(*) WHERE year > 2020;
```

## Let's explore the data

```sql
DESCRIBE judgements
```

Let's learn DuckDB using `llm`.

```bash
.shell uvx llm 'Write DuckDB SQL: ...'
```

- How clean are the dates?
- How clean are categorical variables?

## Which bench has cases pending the longest?

Typing is boring. Let's **ask** our questions.

```bash
.shell ask
```

[ask](https://github.com/sanand0/scripts/blob/54560718bf2f4148d9005d74ab1543de52cff6d9/ask) is a shell script that:

- Records audio via `ffmpeg`, and
- Sends it to Gemini 2.5 Flash via `llm`
- Using context I added in [ask.md](ask.md)

# Cool feature #3: Powerful, extensible functions

DuckDB has a **HUGE** built-in library of functions.

https://duckdb.org/docs/stable/sql/functions/overview.html

This includes:

- Lists: `list_sort()`, `strlen()`, `list_concat()`, ...
- Maps: `map_concat(MAP {'a': 1, 'b': 2}, MAP {'c': 3})`
- Globs: `glob('**/*.xml')`
- Blob functions: `base64(read_blob("image.png"))`
- Lambda functions: `list_filter(array, lambda x: x > 4)`
- RegEx: `regexp_extract('abc', '([a-z])(b)', 1)`

## Let's create a function

```sql
CREATE MACRO letters(s) AS  -- Sort letters in name
    lower(s)                --   convert to lowercase
    .regexp_replace(
        '[^\p{L}]', '', 'g'
    )                         -- remove all non-Unicode letters
    .string_to_array('')    --   turn the string into a list
    .list_sort();           --   sort the list
```

Source: [Letter Scrambling Macro - DuckDB blog](https://duckdb.org/2025/09/11/solving-letter-scramble-puzzles.html)

## Let's explore the 2024 elections

You can read CSV files online. It's fast. **Auto-detects** separators.

```sql
CREATE TABLE elections AS FROM
'https://raw.githubusercontent.com/thecont1/india-votes-data/'
'refs/heads/main/2024%20Parliamentary%20Elections%20India.csv';

FROM elections LIMIT 2;
```

| State  | Const | Party         | Candidate          | Votes  |
| -------| ----- | ------------- | ------------------ | ------ |
| Andhra | Araku | Yuvajana ...  | GUMMA THANUJA RANI | 477005 |
| Andhra | Araku | Bharatiya ... | KOTHAPALLI GEETHA  | 426425 |

## Which candidates names are anagrams?

```sql
SELECT
  e1.Candidate AS name1,
  e2.Candidate AS name2
FROM
  elections e1,
  elections e2
WHERE
  name1.letters() = name2.letters() AND
  name1 < name2;
```

## Some interesting candidate anagrams

Here are the guessable ones:

- ASHISH KUMAR & SHASHI KUMAR
- AMAR SINGH & ARAM SINGH
- AMARESH & RAMESH A
- BALBIR SINGH & BIRBAL SINGH

But the coolest was:

- HIRAK SINHA & KRISHNAIAH

## Any identical names in a constituency?

```sql
SELECT
  e1.Candidate AS name1, e2.Candidate AS name2,
  e1.Party as party1,    e2.Party as party2,
  e1.Constituency
FROM
  elections e1,
  elections e2
WHERE
  name1.letters() = name2.letters()
  AND name1 < name2
  AND party1 != party2
  AND e1.Constituency = e2.Constituency;
```

# Cool feature #4: DuckDB runs everywhere

You can embed it in any application.

```bash
pip install duckdb            # Python
npm install @duckdb/node-api  # JavaScript
cargo add duckdb              # Rust
install.packages("duckdb")    # R
# Go, C/C++, Java, ODBC, ...
```

Let's explore it in Python.

```bash
.shell uv run --with duckdb,ipython ipython
```

## It even runs in the browser (WASM)

Try it online: <https://shell.duckdb.org/>

Installation is easy: <https://duckdb.org/docs/stable/clients/wasm/instantiation>

Usage is pretty straightforward:

```js
const conn = await db.connect();
const response = await conn.query(sql);
const result = response.toArray();
await conn.close();
```

## I use it to evaluate student SQL

I run a course at IIT Madras: Tools in Data Science.

<https://tds.s-anand.net/>

**DuckDB WASM** evaluates student responses. Example:

<https://exam.sanand.workers.dev/tds-2025-01-roe#hq-duckdb-sales-over-time>

## FYI, this is the solution

```sql
SELECT
  strftime(CAST(timestamp AS TIMESTAMP), '%H') AS hour,
  COALESCE(SUM(CASE WHEN category = 'Electronics' THEN amount ELSE 0 END), 0) AS Electronics,
  COALESCE(SUM(CASE WHEN category = 'Clothing' THEN amount ELSE 0 END), 0) AS Clothing,
  COALESCE(SUM(CASE WHEN category = 'Home Goods' THEN amount ELSE 0 END), 0) AS "Home Goods"
FROM sales
GROUP BY hour
ORDER BY hour ASC;
```

## You can run DuckDB in ChatGPT

ChatGPT code interpreter cannot `pip install duckdb`.
But you can upload & install [a duckdb `.whl`](https://files.pythonhosted.org/packages/90/a3/41f3d42fddd9629846aac328eb295170e76782d8dfc5e58b3584b96fa296/duckdb-1.3.2-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl).

> Install the attached DuckDB wheel.
> Write and run sample Python code that uses DuckDB.

PS: To find the right `.whl` verion, I asked:

> What version of Python are you using?
> Which DuckDB version will run in your container?

[ChatGPT conversation](https://chatgpt.com/share/68c222a9-dae8-800c-8e6c-4d9f058ec8c0)

<!--

- via Simon Willison: https://simonwillison.net/2024/Jul/17/duckdb-in-chatgpt-code-interpreter/
- See all PyPi DuckDB files: https://pypi.org/project/duckdb/#files

-->

# Cool feature #5: Geospatial joins

Installing the geospatial extension lets us do geospatial queries.

```sql
INSTALL spatial;
LOAD spatial;
```

## Download Districts (SHP) & Constituencies (GeoJSON)

```sql
CREATE TABLE districts AS
SELECT * FROM ST_Read(
  'https://raw.githubusercontent.com/datameet/maps/refs/heads/master/Districts/Census_2011/2011_Dist.shp');

CREATE TABLE pc AS
SELECT * FROM ST_Read(
  'https://raw.githubusercontent.com/datameet/maps/refs/heads/master/parliamentary-constituencies/india_pc_2019_simplified.geojson');
```

## Lets explore district - constituency overlaps

- Does the total area of PCs and districts match, state-wise? Where are the largest percentage differences?
- Which districts are part of the Gurgaon parliamentary constituency?
- Which parliamentary constituencies have the largest number of fully contained districts?
- Which parliamentary constituencies have the largest number of overlapping districts?
- Which districts have the largest number of overlapping parliamentary constituencies?
- Which districts have the largest number of SC/ST parliamentary constituencies overlapping them?

# Cool feature #6: Vector search

See [vectordb.py](vectordb.py)

```sql
CREATE TABLE IF NOT EXISTS embeddings (
  doc TEXT PRIMARY KEY,
  embedding FLOAT[1536]
)
```

```sql
FROM embeddings
SELECT doc, array_inner_product(
  embedding, query_embedding) AS similarity
ORDER BY similarity DESC
LIMIT 5
```

## You can speed it up with an HNSW index

```sql
INSTALL vss;
LOAD vss;
SET GLOBAL hnsw_enable_experimental_persistence = true;

CREATE INDEX ip_idx ON embeddings USING HNSW (embedding)
WITH (metric = 'ip');
```

# Cool feature #7: There's more!

Core extensions: https://duckdb.org/docs/stable/core_extensions/overview.html

- **Cloud**: aws, azure, httpfs
- **DBs**: mysql, postgres, sqlite
- **Formats**: excel, json, parquet, avro
- **Data lakes**: ducklake, delta, iceberg
- **Search**: fts, vss

## There are plenty of Community extensions

Community extensions: https://duckdb.org/community_extensions/list_of_extensions

- **Cloud & FS**: **shellfs**, **httpserver**, webmacro, cache_httpfs, hostfs, http_client, zipfs
- **Databases & Connectors**: bigquery, nanodbc, redis, msolap, chsql_native, ofquack
- **Formats & Interchange**: arrow, nanoarrow, hdf5, read_stat, vortex, magic
- **SaaS & Office**: **gsheets**, sheetreader, **pbix**
- **Geospatial & Indexing**: geography, h3, lindel
- **Graph**: duckpgq
- **ML / AI & RAG**: faiss, quackformers, **flockmtl**, open_prompt
- **Approximate Analytics**: datasketches
- **Query Languages & Planning**: chsql, prql, psql, substrait, parser_tools
- **Networking & Web Data**: pcap_reader, wireduck, netquack
- **IDs & Crypto**: crypto, tsid, ulid
- **Scheduling**: cronjob
- **Blockchain & Finance**: **blockduck**, scrooge
- **Scripting**: evalexpr_rhai
- **Productivity & DevX**: pivot_table, fuzzycomplete, quack

## Their blog https://duckdb.org/news/ is fascinating

- Solving Letter Scramble Puzzles with DuckDB
- Lightweight Text Analytics Workflows with DuckDB
- Faster Dashboards with Multi-Column Approximate Sorting
- DuckLake: SQL as a Lakehouse Format
- Temporal Analysis with Stream Windowing Functions in DuckDB
- Fully Local Data Transformation with dbt and DuckDB
- Using DuckDB in Streamlit
- Preview: Amazon S3 Tables in DuckDB
- Parquet Bloom Filters in DuckDB
- Reading and Writing Google Sheets in DuckDB

# DuckDB is the new Pandas

Slides: <https://sanand0.github.io/talks/>

LICENSE: CC0 - Public Domain

Contact me: <https://s-anand.net/>


<!--

DuckDB vs Pandas: https://chatgpt.com/c/68bb7248-ec7c-832f-9348-3790779dbf81

#TODO

- Live questions feed

-->

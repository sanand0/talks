# DuckDB is the new Pandas

PyCon India, Bangalore, 13 Sep 2025

Anand S, LLM Psychologist @ **Straive**

**Slides**: <https://sanand0.github.io/talks/>

**Questions**: Slido.com - 2987 234

LICENSE: **CC0** - Public Domain

<!--

Talk: https://cfp.in.pycon.org/2025/talk/W8VJX3/
Venue: [NIMHANS Convention Center](https://maps.app.goo.gl/Uon4KDWDqy65RGim8)

-->

## Why DuckDB?

DuckDB is like SQLite, but for analytics.
Just **SQL**: nothing new to learn
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

FROM read_json("https://api.github.com/search/repositories?q=python&sort=stars&order=desc")
SELECT unnest(items, recursive := true)
LIMIT 5;
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
| ------ | ----- | ------------- | ------------------ | ------ |
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

# Q&A

The questons raised on Slido.com: #2987 234 are answered below.

<!-- https://admin.sli.do/event/2tkf9n716waxwmzsFC5fiU/polls -->

- **What's your terminal setup? (+9)**
  - I run `fish` in VS Code. Here is my [laptop setup](https://github.com/sanand0/scripts/blob/54560718bf2f4148d9005d74ab1543de52cff6d9/setup/linux.md) and [fish config](https://github.com/sanand0/scripts/blob/54560718bf2f4148d9005d74ab1543de52cff6d9/setup.fish).
  - I used `.shell uv run ../slide.py` to render this README.md as slides on the console. Here is the [slide.py source](https://github.com/sanand0/talks/blob/7378053fcf5ea7ca1f53168f7771884212e4b56b/slide.py).
  - I used `.shell llm "Write DuckDB SQL: ..."` to generate SQL via GPT-5 Mini using Simon Willison's [`llm`](https://llm.datasette.io/).
  - I used `.shell ask` to generate SQL from audio. Here is the [`ask` source](https://github.com/sanand0/scripts/blob/54560718bf2f4148d9005d74ab1543de52cff6d9/ask) and the [`ask.md`](ask.md) context.
- **Can we use DuckDB as a vector DB? (+2)**
  - Yes. Install the VSS extension for vector similarity search (e.g., cosine/L2) with index support directly in SQL; for scale or speed (e.g. streaming), a dedicated vector DB may still be better.
- **Can we use DuckDB instead of relational databases? Any advantages over PostgreSQL? (+2)**
  - For single-node analytics, DuckDB's embedded, columnar, vectorized engine can be simpler and faster than a row-store like PostgreSQL; for multi-user OLTP/services, PostgreSQL remains the better fit.
- **Can DuckDB process a large CSV files, say more than 10GB per CSV without running into out of memory issues. Pandas usually run into memory issues read_csv (+1)**
  - Yes. DuckDB streams CSVs and can operate out-of-core (spilling to disk) so files can exceed RAM; prefer Parquet if you'll query repeatedly.
- **Can I query my 1 million data points in disk using DuckDB without loading it in-memory? What will be the desired data format for that?**
  - Yes. Use Parquet files.
- **Will running DuckDB on large datasets affect the performance while running on containers?**
  - No inherent penalty. DuckDB is just a process; performance mainly changes if you cap container CPU/RAM or disk I/O.
- **How much compute resource do we need for large datasets?**
  - DuckDB uses all cores by default and spills to SSD when needed; give it as many cores as available and fast local disk for temp files.
- **If DuckDB is described as in-memory processing but doesn't use much RAM, how does it manage query execution without heavily relying on RAM?**
  - It executes in vectorized "data chunks" with predicate/projection pushdown. It spills intermediates to disk, keeping only small slices in memory.
- **Why is DuckDB so fast? What is Pandas doing incorrectly?**
  - DuckDB combines a columnar storage format, cost-based optimizer, vectorized operators, and parallelism: capabilities a dataframe library like Pandas doesn't target as a DBMS.
- **What are the tradeoffs when switching to DuckDB from Pandas?**
  - You trade Pythonic, row-wise APIs for SQL. For custom per-row logic/ML you'll still use Pandas/NumPy and bridge via Arrow/Pandas interop.
- **Is it as perforant on insertions?**
  - DuckDB isn't built for high-rate single-row OLTP inserts. Use bulk loading (COPY/Appender) for best write throughput.
- **How to force predicate pushdown if DuckDB client is attached connection with PostgreSQL?**
  - The Postgres scanner attempts filter/projection pushdown automatically where supported; you can't "force" unsupported cases. Verify with EXPLAIN and move filters into the scan query.
- **Do DuckDB have auth?**
  - DuckDB is embedded (no server/users), so you rely on OS/file permissions; use the Secrets Manager for external creds or the optional HTTP server extension if exposing over HTTP.
- **Since DuckDB is an OLAP database, how is it different from ClickHouse? Which one do you think is faster?**
  - DuckDB is single-node. ClickHouse is a client-server (cluster-scale). Speed depends on workload.
- **While importing tables from a file, is it possible to specify the separator (for eg.. If I'm using a dataset with tab seperated values)**
  - Yes. Use `read_csv('file', delim '\t')` or `COPY ... (FORMAT csv, DELIMITER '\t')`.
- **What are the limitations DuckDB WASM regarding threads and memory?**
  - Browser multi-threading needs `SharedArrayBuffer` with proper COOP/COEP headers. Otherwise it's single-threaded, and wasm32 memory typically tops out around 4 GB.
- **Can we connect to cloud OLAP systems with DuckDB? Can we also use it to perform writes to target cloud systems like BigQuery?**
  - Yes. Via community extensions (e.g., BigQuery, ClickHouse, Postgres) and httpfs for S3/GCS. The BigQuery extension supports reading _and writing_ tables.
- **Why was it named DuckDB?**
  - The founders named it after a pet duck ("Wilbur") and because ducks are resilient; releases even use duck species codenames.
- **Have you tried DuckLake?**
  - Just as an experiment. I haven't actually used it.
- **Have you tried MotherDuck?**
  - Just as an experiment. I haven't actually used it.
- **Can DuckDB analyze poultry data?**
  - Yes.
- **Does it has any thing to do with DuckDuckGo?**
  - No.
- **Really enjoyed your session! Can you please some materials to get started with DuckDB? Also, please share your linkedin. Thanks!**
  - The [DuckDB docs](https://duckdb.org/docs/) are a good start.
  - I'm on LinkedIn at <https://www.linkedin.com/in/sanand0/>
- **You missed mentioning Ruby and Elixir 🥲 (jk)**
  - Oh, I'm not familiar enough with either 😔
- **DDonald Duck: Can BJP continue to hijack elections if the ECI uses this? (+1)**
  - I have no idea! 😕
- **Tthecont1: Thank you for using my elections dataset. Flattered 😊 (+2)**
  - Thanks for creating it!
- **Extremely interesting presentation! Loved it (+1)**
  - Thanks!

<!--

DuckDB vs Pandas: https://chatgpt.com/c/68bb7248-ec7c-832f-9348-3790779dbf81

#TODO

- Live questions feed

-->

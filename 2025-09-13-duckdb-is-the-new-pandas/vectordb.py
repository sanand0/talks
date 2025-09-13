# /// script
# requires-python = ">=3.12"
# dependencies = ["openai", "duckdb", "numpy", "pyarrow", "polars"]
# ///
import duckdb
from openai import OpenAI

# Create an embeddings database
# -----------------------------------------------
conn = duckdb.connect("embeddings.db")
conn.execute("""
  CREATE TABLE IF NOT EXISTS embeddings (
    doc TEXT PRIMARY KEY,
    embedding FLOAT[1536]
  )""")

## Insert sample word embeddings
client = OpenAI()
model = "text-embedding-3-small"

words = ["apple", "banana", "car", "train", "Lima", "Tokyo"]
response = client.embeddings.create(model=model, input=words)
sql = "INSERT OR REPLACE INTO embeddings (doc, embedding) VALUES (?, ?)"
conn.executemany(sql, zip(words, [item.embedding for item in response.data]))


# Create a DuckDB function to return embeddings
# -----------------------------------------------


def embed(doc):
    response = client.embeddings.create(model=model, input=doc)
    return response.data[0].embedding


conn.create_function("embed", embed, ["TEXT"], "FLOAT[1536]")


# Search with inner-product similarity
# -----------------------------------------------


def search(q, n=2):
    return conn.execute(
        """
        FROM embeddings
        SELECT doc, array_inner_product(embedding, embed($q)) AS similarity
        ORDER BY similarity DESC
        LIMIT $n""",
        {"q": q, "n": n},
    ).fetchall()


print("Fruits:", search("Fruit"))
print("Vehicles:", search("Vehicle"))

# Adding a vector search index speeds this up
# -----------------------------------------------
conn.execute("""
INSTALL vss;
LOAD vss;
SET GLOBAL hnsw_enable_experimental_persistence = true;

CREATE INDEX ip_idx ON embeddings USING HNSW (embedding)
WITH (metric = 'ip');
""")

# Now searches will be much faster
print("Places:", search("Place"))

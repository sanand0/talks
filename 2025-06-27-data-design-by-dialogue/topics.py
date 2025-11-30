#!/usr/bin/env python3
"""
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "openai",
#     "scikit-learn",
#     "numpy",
#     "pandas",
# ]
# ///

WhatsApp Topic Analysis Tool

Analyzes WhatsApp messages by:
1. Computing embeddings for each message text
2. Clustering messages using K-Means
3. Using GPT-4 to name clusters
4. Creating tagged output with cluster assignments
"""

import gzip
import json
import argparse
from typing import List, Dict, Any
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from openai import OpenAI


def load_messages(file_path: str) -> List[Dict[str, Any]]:
    """Load messages from gzipped JSON file"""
    print(f"Loading messages from {file_path}...")
    with gzip.open(file_path, "rt", encoding="utf-8") as f:
        messages = json.load(f)

    # Filter out system messages and messages without text
    text_messages = [
        msg
        for msg in messages
        if not msg.get("isSystemMessage", False) and msg.get("text", "").strip()
    ]
    print(f"Loaded {len(text_messages)} text messages (filtered from {len(messages)} total)")
    return text_messages


def get_embeddings(client: OpenAI, texts: List[str]) -> np.ndarray:
    """Get embeddings for a list of texts using OpenAI's text-embedding-3-small"""
    print(f"Computing embeddings for {len(texts)} texts...")

    # Process in batches to avoid rate limits
    batch_size = 100
    all_embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        print(
            f"Processing batch {i // batch_size + 1}/{(len(texts) + batch_size - 1) // batch_size}"
        )

        response = client.embeddings.create(model="text-embedding-3-small", input=batch)

        batch_embeddings = [data.embedding for data in response.data]
        all_embeddings.extend(batch_embeddings)

    return np.array(all_embeddings)


def cluster_messages(embeddings: np.ndarray, n_clusters: int) -> np.ndarray:
    """Cluster embeddings using K-Means"""
    print(f"Clustering into {n_clusters} clusters...")

    # Standardize embeddings
    scaler = StandardScaler()
    embeddings_scaled = scaler.fit_transform(embeddings)

    # Perform clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(embeddings_scaled)

    print(f"Clustering complete. Cluster distribution: {np.bincount(cluster_labels)}")
    return cluster_labels


def name_clusters(
    client: OpenAI, messages: List[Dict[str, Any]], cluster_labels: np.ndarray
) -> List[str]:
    """Use GPT-4 to name clusters based on message content"""
    print("Generating cluster names using GPT-4...")

    # Collect sample messages for each cluster
    cluster_samples = {}
    for i, label in enumerate(cluster_labels):
        if label not in cluster_samples:
            cluster_samples[label] = []
        # Take up to 10 sample messages per cluster
        if len(cluster_samples[label]) < 10:
            cluster_samples[label].append(messages[i]["text"])

    # Prepare prompt with all cluster samples
    cluster_info = []
    for cluster_id in sorted(cluster_samples.keys()):
        samples = cluster_samples[cluster_id]
        cluster_info.append(
            f"Cluster {cluster_id} ({len([label for label in cluster_labels if label == cluster_id])} messages):"
        )
        cluster_info.extend(
            [f"  - {text[:200]}" for text in samples[:5]]
        )  # First 5 samples, truncated
        cluster_info.append("")

    prompt = f"""Analyze these message clusters and provide clear, distinctive names for each cluster.

{chr(10).join(cluster_info)}

Please provide names that:
1. Are concise (1-3 words)
2. Clearly differentiate between clusters
3. Capture the main theme/topic of each cluster
4. Are descriptive and meaningful

Return the cluster names as a JSON array, ordered by cluster ID (0, 1, 2, ...).
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
    )

    result = json.loads(response.choices[0].message.content)
    cluster_names = result.get(
        "cluster_names", [f"Cluster {i}" for i in range(len(cluster_samples))]
    )

    print(f"Generated cluster names: {cluster_names}")
    return cluster_names


def create_tagged_output(
    messages: List[Dict[str, Any]],
    cluster_labels: np.ndarray,
    cluster_names: List[str],
    output_file: str,
):
    """Create tagged JSON output with cluster information"""
    print(f"Creating tagged output file: {output_file}")

    tagged_messages = []
    for i, msg in enumerate(messages):
        tagged_msg = msg.copy()
        cluster_id = int(cluster_labels[i])
        tagged_msg["cluster"] = {
            "id": cluster_id,
            "name": cluster_names[cluster_id]
            if cluster_id < len(cluster_names)
            else f"Cluster {cluster_id}",
        }
        tagged_messages.append(tagged_msg)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(tagged_messages, f, indent=2, ensure_ascii=False)

    print(f"Tagged output saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Analyze WhatsApp messages and cluster by topics")
    parser.add_argument(
        "--test", action="store_true", help="Test mode: use only 20 messages and 3 clusters"
    )
    parser.add_argument("--messages", type=int, default=20, help="Number of messages for test mode")
    parser.add_argument(
        "--clusters", type=int, help="Number of clusters (default: 3 for test, 12 for full)"
    )
    parser.add_argument("--input", default="whatsapp.json.gz", help="Input file path")
    parser.add_argument("--output", default="tagged.json", help="Output file path")

    args = parser.parse_args()

    # Set defaults based on test mode
    if args.test:
        n_clusters = args.clusters or 3
        max_messages = args.messages
        print(f"Running in test mode with {max_messages} messages and {n_clusters} clusters")
    else:
        n_clusters = args.clusters or 12
        max_messages = None
        print(f"Running full analysis with {n_clusters} clusters")

    # Initialize OpenAI client
    client = OpenAI()

    # Load and process messages
    messages = load_messages(args.input)

    if max_messages:
        messages = messages[:max_messages]
        print(f"Using first {len(messages)} messages for analysis")

    # Extract text for embedding
    texts = [msg["text"] for msg in messages]

    # Get embeddings
    embeddings = get_embeddings(client, texts)

    # Cluster messages
    cluster_labels = cluster_messages(embeddings, n_clusters)

    # Name clusters
    cluster_names = name_clusters(client, messages, cluster_labels)

    # Create tagged output
    create_tagged_output(messages, cluster_labels, cluster_names, args.output)

    # Print summary
    print("\nAnalysis Summary:")
    print(f"Total messages analyzed: {len(messages)}")
    print(f"Number of clusters: {n_clusters}")
    print(f"Output file: {args.output}")

    # Print cluster distribution
    print("\nCluster Distribution:")
    for i, name in enumerate(cluster_names):
        count = sum(1 for label in cluster_labels if label == i)
        print(f"  {i}: {name} ({count} messages)")


if __name__ == "__main__":
    main()

"""
Self-Organizing Map (SOM) Visualization for Customer Shopping Behavior
A Complete Classroom Demonstration

This script demonstrates how to:
1. Load and preprocess the customer shopping data
2. Train a Self-Organizing Map (Kohonen network)
3. Visualize the results in multiple informative ways

Requirements:
    pip install numpy pandas matplotlib scikit-learn minisom --break-system-packages
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from minisom import MiniSom
import warnings

warnings.filterwarnings("ignore")

# Set style for better-looking plots
plt.style.use("seaborn-v0_8-darkgrid")


def load_and_preprocess_data(filepath):
    """Load customer data and prepare for SOM training."""
    print("Loading customer shopping data...")
    df = pd.read_csv(filepath)

    # Extract features (exclude customer_id and customer_segment)
    feature_cols = [
        "monthly_spending",
        "visit_frequency",
        "avg_purchase_value",
        "online_preference",
        "discount_sensitivity",
    ]
    X = df[feature_cols].values

    # Standardize features (critical for SOM)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print(f"Loaded {len(df)} customers with {len(feature_cols)} features")
    print(f"Features: {', '.join(feature_cols)}")

    return df, X_scaled, feature_cols, scaler


def train_som(X, som_shape=(10, 10), sigma=1.5, learning_rate=0.5, num_iterations=1000):
    """
    Train a Self-Organizing Map.

    Parameters:
    - som_shape: Grid size (rows, columns)
    - sigma: Neighborhood radius
    - learning_rate: Initial learning rate
    - num_iterations: Number of training iterations
    """
    print(f"\nTraining SOM with {som_shape[0]}x{som_shape[1]} grid...")

    # Initialize SOM
    som = MiniSom(
        x=som_shape[0],
        y=som_shape[1],
        input_len=X.shape[1],
        sigma=sigma,
        learning_rate=learning_rate,
        neighborhood_function="gaussian",
        random_seed=42,
    )

    # Initialize weights
    som.random_weights_init(X)

    # Train
    som.train_random(X, num_iterations)

    print(f"Training complete! ({num_iterations} iterations)")

    return som


def visualize_som_results(som, X, df, feature_cols, output_file="som_visualization.png"):
    """Create comprehensive SOM visualizations."""

    fig = plt.figure(figsize=(20, 16))

    # 1. U-Matrix (Distance Map) - Shows cluster boundaries
    ax1 = plt.subplot(3, 3, 1)
    u_matrix = som.distance_map().T
    plt.pcolor(u_matrix, cmap="bone_r", edgecolors="gray", linewidths=0.5)
    plt.colorbar(label="Distance")
    plt.title(
        "U-Matrix (Distance Map)\nDarker = Cluster Boundaries", fontsize=12, fontweight="bold"
    )
    plt.axis("equal")
    ax1.set_aspect("equal")

    # 2. Hit Map - Shows data density
    ax2 = plt.subplot(3, 3, 2)
    frequencies = np.zeros((som.get_weights().shape[0], som.get_weights().shape[1]))
    for x in X:
        winner = som.winner(x)
        frequencies[winner] += 1

    plt.pcolor(frequencies.T, cmap="YlOrRd", edgecolors="gray", linewidths=0.5)
    plt.colorbar(label="Number of Customers")
    plt.title("Hit Map (Customer Density)\nShows Popular Regions", fontsize=12, fontweight="bold")
    plt.axis("equal")
    ax2.set_aspect("equal")

    # 3. Segment Distribution on SOM
    ax3 = plt.subplot(3, 3, 3)
    segment_colors = {
        "Budget Shopper": "blue",
        "Premium Buyer": "red",
        "Frequent Visitor": "green",
        "Online Enthusiast": "purple",
        "Occasional Splurger": "orange",
    }

    for idx, (x, segment) in enumerate(zip(X, df["customer_segment"])):
        winner = som.winner(x)
        plt.plot(
            winner[0] + 0.5,
            winner[1] + 0.5,
            "o",
            color=segment_colors[segment],
            markersize=8,
            alpha=0.6,
            markeredgecolor="black",
            markeredgewidth=0.5,
        )

    # Add legend
    legend_elements = [
        plt.Line2D(
            [0], [0], marker="o", color="w", markerfacecolor=color, markersize=10, label=segment
        )
        for segment, color in segment_colors.items()
    ]
    plt.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(1.05, 1), fontsize=9)

    plt.xlim([0, som.get_weights().shape[0]])
    plt.ylim([0, som.get_weights().shape[1]])
    plt.title(
        "True Customer Segments\nSOM Discovers These Naturally!", fontsize=12, fontweight="bold"
    )
    plt.axis("equal")
    ax3.set_aspect("equal")

    # 4-8. Component Planes (one for each feature)
    subplot_positions = [4, 5, 6, 7, 8]
    for idx, feature in enumerate(feature_cols):
        ax = plt.subplot(3, 3, subplot_positions[idx])
        component_plane = som.get_weights()[:, :, idx].T

        plt.pcolor(component_plane, cmap="coolwarm", edgecolors="gray", linewidths=0.5)
        plt.colorbar(label=feature)
        plt.title(f"{feature.replace('_', ' ').title()}", fontsize=11, fontweight="bold")
        plt.axis("equal")
        ax.set_aspect("equal")

    plt.tight_layout()
    plt.savefig(f"/mnt/user-data/outputs/{output_file}", dpi=150, bbox_inches="tight")
    print(f"\nVisualization saved to: {output_file}")

    return fig


def analyze_clusters(som, X, df):
    """Analyze and report cluster characteristics."""
    print("\n" + "=" * 60)
    print("CLUSTER ANALYSIS")
    print("=" * 60)

    # Map each customer to their winning neuron
    winner_coordinates = np.array([som.winner(x) for x in X])
    df["som_x"] = winner_coordinates[:, 0]
    df["som_y"] = winner_coordinates[:, 1]
    df["som_cluster"] = df["som_x"].astype(str) + "_" + df["som_y"].astype(str)

    # Find the most populated clusters
    cluster_counts = df["som_cluster"].value_counts()
    top_clusters = cluster_counts.head(5)

    print(f"\nTop 5 Most Populated SOM Neurons:")
    for cluster_id, count in top_clusters.items():
        x, y = map(int, cluster_id.split("_"))
        cluster_data = df[df["som_cluster"] == cluster_id]

        print(f"\n  Neuron ({x}, {y}): {count} customers")
        print(f"    Segments: {cluster_data['customer_segment'].value_counts().to_dict()}")
        print(f"    Avg Monthly Spending: ${cluster_data['monthly_spending'].mean():.2f}")
        print(f"    Avg Visit Frequency: {cluster_data['visit_frequency'].mean():.1f}")
        print(f"    Avg Online Preference: {cluster_data['online_preference'].mean():.2f}")

    # Segment separation quality
    print("\n" + "-" * 60)
    print("SEGMENT SEPARATION ON SOM:")
    print("-" * 60)
    for segment in df["customer_segment"].unique():
        segment_data = df[df["customer_segment"] == segment]
        unique_neurons = segment_data["som_cluster"].nunique()
        total_neurons = len(segment_data)
        concentration = (total_neurons / unique_neurons) if unique_neurons > 0 else 0

        print(f"\n  {segment}:")
        print(f"    Spread across {unique_neurons} neurons")
        print(f"    Concentration: {concentration:.2f} customers per neuron")


def main():
    """Main execution function."""
    print("=" * 60)
    print("SELF-ORGANIZING MAP (SOM) CLASSROOM DEMONSTRATION")
    print("Customer Shopping Behavior Analysis")
    print("=" * 60)

    # Load data
    df, X_scaled, feature_cols, scaler = load_and_preprocess_data("customer_shopping_data.csv")

    # Train SOM
    som = train_som(X_scaled, som_shape=(10, 10), num_iterations=1000)

    # Visualize
    visualize_som_results(som, X_scaled, df, feature_cols)

    # Analyze clusters
    analyze_clusters(som, X_scaled, df)

    print("\n" + "=" * 60)
    print("SOM ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\nKey Insights:")
    print("  • The U-Matrix shows cluster boundaries (darker regions)")
    print("  • The Hit Map shows where most customers are mapped")
    print("  • Component planes show how each feature varies across the map")
    print("  • The SOM discovered customer segments without being told!")
    print("\nThis demonstrates unsupervised learning at work!")


if __name__ == "__main__":
    main()

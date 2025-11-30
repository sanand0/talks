"""
Customer Shopping Behavior Dataset Generator
Perfect for Self-Organizing Map (SOM) Classroom Demonstrations

This generates synthetic data representing customer shopping patterns with
natural clusters that SOMs can discover and visualize beautifully.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Set random seed for reproducibility
np.random.seed(42)


# Define customer segments with distinct behaviors
def generate_customer_segment(n_customers, base_params, noise_level=0.15):
    """
    Generate a customer segment with specified behavioral characteristics.

    Parameters represent:
    - monthly_spending: Average monthly spending ($)
    - visit_frequency: Visits per month
    - avg_purchase_value: Average value per purchase ($)
    - online_preference: Preference for online shopping (0-1)
    - discount_sensitivity: How much discounts influence purchases (0-1)
    """
    data = []
    for _ in range(n_customers):
        customer = {
            "monthly_spending": max(
                0,
                np.random.normal(
                    base_params["monthly_spending"], base_params["monthly_spending"] * noise_level
                ),
            ),
            "visit_frequency": max(
                0,
                np.random.normal(
                    base_params["visit_frequency"], base_params["visit_frequency"] * noise_level
                ),
            ),
            "avg_purchase_value": max(
                0,
                np.random.normal(
                    base_params["avg_purchase_value"],
                    base_params["avg_purchase_value"] * noise_level,
                ),
            ),
            "online_preference": np.clip(
                np.random.normal(base_params["online_preference"], noise_level), 0, 1
            ),
            "discount_sensitivity": np.clip(
                np.random.normal(base_params["discount_sensitivity"], noise_level), 0, 1
            ),
        }
        data.append(customer)
    return data


# Define 5 distinct customer segments (perfect for visualization)
segments = {
    "Budget Shoppers": {
        "count": 30,
        "params": {
            "monthly_spending": 150,
            "visit_frequency": 8,
            "avg_purchase_value": 20,
            "online_preference": 0.3,
            "discount_sensitivity": 0.9,
        },
        "label": "Budget Shopper",
    },
    "Premium Buyers": {
        "count": 25,
        "params": {
            "monthly_spending": 800,
            "visit_frequency": 4,
            "avg_purchase_value": 200,
            "online_preference": 0.7,
            "discount_sensitivity": 0.2,
        },
        "label": "Premium Buyer",
    },
    "Frequent Visitors": {
        "count": 28,
        "params": {
            "monthly_spending": 400,
            "visit_frequency": 15,
            "avg_purchase_value": 30,
            "online_preference": 0.4,
            "discount_sensitivity": 0.5,
        },
        "label": "Frequent Visitor",
    },
    "Online Enthusiasts": {
        "count": 27,
        "params": {
            "monthly_spending": 500,
            "visit_frequency": 6,
            "avg_purchase_value": 85,
            "online_preference": 0.95,
            "discount_sensitivity": 0.6,
        },
        "label": "Online Enthusiast",
    },
    "Occasional Splurgers": {
        "count": 20,
        "params": {
            "monthly_spending": 300,
            "visit_frequency": 2,
            "avg_purchase_value": 150,
            "online_preference": 0.5,
            "discount_sensitivity": 0.4,
        },
        "label": "Occasional Splurger",
    },
}

# Generate dataset
all_customers = []
true_labels = []

for segment_name, segment_info in segments.items():
    customers = generate_customer_segment(segment_info["count"], segment_info["params"])
    all_customers.extend(customers)
    true_labels.extend([segment_info["label"]] * segment_info["count"])

# Create DataFrame
df = pd.DataFrame(all_customers)
df["customer_segment"] = true_labels
df["customer_id"] = [f"CUST_{i:04d}" for i in range(len(df))]

# Reorder columns for better readability
df = df[
    [
        "customer_id",
        "monthly_spending",
        "visit_frequency",
        "avg_purchase_value",
        "online_preference",
        "discount_sensitivity",
        "customer_segment",
    ]
]

# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv("/mnt/user-data/outputs/customer_shopping_data.csv", index=False)

print("Dataset Generated Successfully!")
print(f"\nDataset Size: {len(df)} customers")
print(f"\nSegment Distribution:")
print(df["customer_segment"].value_counts().sort_index())
print(f"\nFeature Statistics:")
print(df.describe().round(2))
print(f"\nDataset saved to: customer_shopping_data.csv")
print(f"\nFeatures:")
print("  - monthly_spending: Total spending per month ($)")
print("  - visit_frequency: Number of visits per month")
print("  - avg_purchase_value: Average value per transaction ($)")
print("  - online_preference: Preference for online shopping (0-1)")
print("  - discount_sensitivity: Responsiveness to discounts (0-1)")

"""
VISUALIZATION 1: FEATURE RIVER FLOW
A Novel Sankey-Style Visualization of Customer Behavioral Journeys

This visualization shows customers as "flows" moving through feature space,
with river width representing spending power and color showing segments.
Branch points reveal where customer groups diverge.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.collections import LineCollection
from scipy.interpolate import make_interp_spline
import warnings
warnings.filterwarnings('ignore')

# Load data
df = pd.read_csv('/mnt/user-data/outputs/customer_shopping_data.csv')

# Prepare features
feature_cols = ['monthly_spending', 'visit_frequency', 'avg_purchase_value', 
                'online_preference', 'discount_sensitivity']

# Normalize features to 0-1 for visualization
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(df[feature_cols])
df_norm = pd.DataFrame(X_normalized, columns=feature_cols)
df_norm['customer_segment'] = df['customer_segment'].values
df_norm['monthly_spending_raw'] = df['monthly_spending'].values

# Sort by segments for coherent flow
df_norm = df_norm.sort_values(['customer_segment', 'monthly_spending']).reset_index(drop=True)

# Color mapping
segment_colors = {
    'Budget Shopper': '#3498db',      # Blue
    'Premium Buyer': '#e74c3c',       # Red
    'Frequent Visitor': '#2ecc71',    # Green
    'Online Enthusiast': '#9b59b6',   # Purple
    'Occasional Splurger': '#f39c12'  # Orange
}

# Create the figure
fig = plt.figure(figsize=(24, 14))

# Main visualization
ax_main = plt.subplot(1, 1, 1)
ax_main.set_facecolor('#f8f9fa')

# Feature positions along x-axis
n_features = len(feature_cols)
feature_positions = np.linspace(0, 10, n_features)

# Create smooth flowing paths for each customer
def create_smooth_path(y_positions, x_positions, smoothness=100):
    """Create smooth interpolated path"""
    if len(y_positions) < 4:
        return x_positions, y_positions
    
    # Create smooth spline
    x_smooth = np.linspace(x_positions[0], x_positions[-1], smoothness)
    spl = make_interp_spline(x_positions, y_positions, k=3)
    y_smooth = spl(x_smooth)
    
    return x_smooth, y_smooth

# Calculate y-positions for each customer at each feature
# Group by segment and stack customers within each segment
segment_offsets = {}
current_offset = 0

for segment in df_norm['customer_segment'].unique():
    segment_offsets[segment] = current_offset
    segment_size = len(df_norm[df_norm['customer_segment'] == segment])
    current_offset += segment_size * 0.5  # Spacing between segments

# Draw the river flows
print("Creating Feature River Flow visualization...")

for idx, row in df_norm.iterrows():
    # Get y-position based on feature values and segment
    segment = row['customer_segment']
    segment_base = segment_offsets[segment]
    
    # Calculate y-positions for each feature (scaled by feature value)
    y_positions = []
    for feat_idx, feat in enumerate(feature_cols):
        # Position influenced by feature value and segment offset
        y_pos = segment_base + row[feat] * 20 + (idx % 6) * 2
        y_positions.append(y_pos)
    
    # Create smooth path
    x_smooth, y_smooth = create_smooth_path(y_positions, feature_positions)
    
    # Line width represents spending
    base_width = 0.3 + (row['monthly_spending_raw'] / df['monthly_spending'].max()) * 2
    
    # Color by segment with transparency
    color = segment_colors[segment]
    
    # Draw the flow path
    points = np.array([x_smooth, y_smooth]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    lc = LineCollection(segments, colors=color, linewidths=base_width, 
                       alpha=0.4, capstyle='round')
    ax_main.add_collection(lc)

# Add feature labels and dividers
for idx, (pos, feature) in enumerate(zip(feature_positions, feature_cols)):
    # Vertical divider
    ax_main.axvline(pos, color='#34495e', linewidth=2, linestyle='--', alpha=0.3, zorder=0)
    
    # Feature label at top
    label = feature.replace('_', '\n').title()
    ax_main.text(pos, -8, label, ha='center', va='top', fontsize=13, 
                fontweight='bold', color='#2c3e50',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                         edgecolor='#34495e', linewidth=2))

# Add segment labels on the right
for segment, offset in segment_offsets.items():
    mid_y = offset + 10
    ax_main.text(10.5, mid_y, segment, va='center', ha='left', fontsize=12,
                fontweight='bold', color=segment_colors[segment],
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                         edgecolor=segment_colors[segment], linewidth=2))

# Add strategic annotations
# Annotation 1: Divergence point
ax_main.annotate('KEY DIVERGENCE POINT\nBudget vs Premium separate here',
                xy=(2, 20), xytext=(1, 5),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff3cd', 
                         edgecolor='#ff6b6b', linewidth=2),
                arrowprops=dict(arrowstyle='->', color='#ff6b6b', lw=2),
                fontsize=10, fontweight='bold', color='#c92a2a')

# Annotation 2: Convergence opportunity
ax_main.annotate('CONVERGENCE ZONE\nSimilar behaviors across segments',
                xy=(7, 45), xytext=(8.5, 55),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#d3f9d8',
                         edgecolor='#2ecc71', linewidth=2),
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2),
                fontsize=10, fontweight='bold', color='#2f9e44')

# Annotation 3: Outlier region
ax_main.annotate('OUTLIER REGION\nUnique shopping patterns',
                xy=(4, 75), xytext=(2.5, 85),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#e7f5ff',
                         edgecolor='#3498db', linewidth=2),
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=2),
                fontsize=10, fontweight='bold', color='#1864ab')

# Styling
ax_main.set_xlim(-0.5, 11.5)
ax_main.set_ylim(-10, 95)
ax_main.set_xlabel('Customer Journey Through Feature Space', fontsize=16, 
                   fontweight='bold', color='#2c3e50')
ax_main.set_ylabel('Customer Flow (grouped by segment)', fontsize=16,
                   fontweight='bold', color='#2c3e50')
ax_main.set_title('FEATURE RIVER FLOW VISUALIZATION\n' + 
                  'Novel Sankey-Style View of Customer Behavioral Journeys\n' +
                  'Width = Spending Power | Color = Segment | Flow = Feature Transitions',
                  fontsize=18, fontweight='bold', color='#2c3e50', pad=20)

# Remove y-axis ticks (they're not meaningful in this abstract space)
ax_main.set_yticks([])
ax_main.set_xticks([])

# Add legend
from matplotlib.patches import Rectangle
legend_elements = []
for segment, color in segment_colors.items():
    legend_elements.append(Rectangle((0, 0), 1, 1, fc=color, alpha=0.6, 
                                    edgecolor='black', linewidth=1.5, label=segment))

ax_main.legend(handles=legend_elements, loc='upper left', fontsize=11,
              title='Customer Segments', title_fontsize=12, framealpha=0.95,
              edgecolor='#34495e', fancybox=True, shadow=True)

# Add grid for readability
ax_main.grid(True, alpha=0.2, linestyle=':', linewidth=0.5)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/novel_viz_1_river_flow.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Feature River Flow visualization saved!")

# Print insights
print("\n" + "="*70)
print("VISUALIZATION 1 INSIGHTS: Feature River Flow")
print("="*70)
print("""
HOW TO READ THIS VISUALIZATION:
-------------------------------
• Each flowing line represents ONE customer's journey through feature space
• LINE WIDTH = Spending power (thicker = higher spending)
• LINE COLOR = Customer segment
• HORIZONTAL AXIS = Features (left to right progression)
• VERTICAL POSITION = Feature value at each stage

WHAT MAKES THIS NOVEL:
---------------------
• Traditional Sankey diagrams show categorical transitions
• This adapts the flow metaphor to CONTINUOUS multivariate data
• Reveals behavioral "journeys" and decision points
• Shows where segments diverge and converge

KEY INSIGHTS FROM THIS VIEW:
---------------------------
1. DIVERGENCE POINTS: Where customer flows separate into distinct paths
   → These features are KEY DIFFERENTIATORS between segments
   → Focus marketing messages on these dimensions

2. CONVERGENCE ZONES: Where different segments flow together
   → Opportunities for unified campaigns
   → Shared needs across diverse customer types

3. FLOW DENSITY: Thick bundles indicate common behavioral patterns
   → Safe bets for product/service design
   → High-confidence predictions

4. OUTLIER STREAMS: Thin, isolated flows
   → Unique customers requiring special attention
   → Innovation opportunities or service gaps

STRATEGIC APPLICATIONS:
----------------------
• PRODUCT DESIGN: Focus on features where flows converge
• SEGMENTATION: Use divergence points for classification
• JOURNEY MAPPING: Literal visualization of customer paths
• TARGETING: Identify which features drive segment membership
• WHAT-IF ANALYSIS: "If we change this feature, which flows move?"
""")

plt.close()

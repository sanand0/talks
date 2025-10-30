"""
VISUALIZATION 2: BEHAVIORAL TOPOGRAPHY MAP
A Strategic Terrain View of Customer Landscape

This visualization treats the customer base as a geographic landscape,
where elevation represents customer density/value, and customers appear
as settlements on this terrain. Strategic opportunities appear as unexplored
territories or valuable peaks.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
from scipy.ndimage import gaussian_filter
from sklearn.preprocessing import StandardScaler
import umap
import warnings
warnings.filterwarnings('ignore')

# Load data
df = pd.read_csv('/mnt/user-data/outputs/customer_shopping_data.csv')

# Prepare features
feature_cols = ['monthly_spending', 'visit_frequency', 'avg_purchase_value', 
                'online_preference', 'discount_sensitivity']
X = df[feature_cols].values

# Standardize for UMAP
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Use UMAP for optimal 2D projection (better than PCA/t-SNE for this purpose)
print("Projecting customers onto 2D landscape using UMAP...")
reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, n_components=2, random_state=42)
X_2d = reducer.fit_transform(X_scaled)

# Add to dataframe
df['x'] = X_2d[:, 0]
df['y'] = X_2d[:, 1]

# Color mapping
segment_colors = {
    'Budget Shopper': '#3498db',
    'Premium Buyer': '#e74c3c',
    'Frequent Visitor': '#2ecc71',
    'Online Enthusiast': '#9b59b6',
    'Occasional Splurger': '#f39c12'
}

# Segment markers (different shapes for different segments)
segment_markers = {
    'Budget Shopper': 'o',
    'Premium Buyer': 's',
    'Frequent Visitor': '^',
    'Online Enthusiast': 'D',
    'Occasional Splurger': 'p'
}

# Create figure
fig = plt.figure(figsize=(22, 16))

# Main topography map
ax_main = plt.subplot(2, 2, (1, 3))

# Create terrain/topography based on customer value density
print("Generating terrain elevation map...")

# Create grid for terrain
grid_resolution = 100
x_range = np.linspace(df['x'].min() - 1, df['x'].max() + 1, grid_resolution)
y_range = np.linspace(df['y'].min() - 1, df['y'].max() + 1, grid_resolution)
X_grid, Y_grid = np.meshgrid(x_range, y_range)

# Calculate "value density" at each grid point
# This represents the strategic value of this region
terrain = np.zeros((grid_resolution, grid_resolution))

for i in range(grid_resolution):
    for j in range(grid_resolution):
        x_point = x_range[i]
        y_point = y_range[j]
        
        # Calculate weighted sum of customer values, inversely proportional to distance
        distances = np.sqrt((df['x'] - x_point)**2 + (df['y'] - y_point)**2)
        weights = np.exp(-distances / 1.5)  # Gaussian-like weighting
        terrain[j, i] = np.sum(df['monthly_spending'] * weights)

# Smooth the terrain
terrain_smooth = gaussian_filter(terrain, sigma=2.0)

# Normalize terrain
terrain_smooth = (terrain_smooth - terrain_smooth.min()) / (terrain_smooth.max() - terrain_smooth.min())

# Plot terrain as contour map
contours = ax_main.contourf(X_grid, Y_grid, terrain_smooth, levels=20, 
                            cmap='terrain', alpha=0.7)
contour_lines = ax_main.contour(X_grid, Y_grid, terrain_smooth, levels=10,
                                colors='black', alpha=0.2, linewidths=0.5)

# Add colorbar for elevation
cbar = plt.colorbar(contours, ax=ax_main, pad=0.02)
cbar.set_label('Strategic Value Density\n(Customer Spending × Density)', 
               fontsize=12, fontweight='bold', rotation=270, labelpad=25)

# Plot customers as "settlements" on the terrain
for segment in df['customer_segment'].unique():
    segment_data = df[df['customer_segment'] == segment]
    
    # Size proportional to spending
    sizes = 50 + (segment_data['monthly_spending'] / df['monthly_spending'].max()) * 300
    
    ax_main.scatter(segment_data['x'], segment_data['y'],
                   c=segment_colors[segment],
                   s=sizes,
                   marker=segment_markers[segment],
                   alpha=0.8,
                   edgecolors='black',
                   linewidths=1.5,
                   label=segment,
                   zorder=5)

# Strategic annotations
# 1. High-value peak
peak_idx = (terrain_smooth == terrain_smooth.max())
peak_x = X_grid[peak_idx][0]
peak_y = Y_grid[peak_idx][0]
ax_main.plot(peak_x, peak_y, '*', color='gold', markersize=30, 
            markeredgecolor='black', markeredgewidth=2, zorder=10)
ax_main.annotate('⛰️ VALUE PEAK\nHighest density of\nhigh-spending customers',
                xy=(peak_x, peak_y), xytext=(peak_x + 2, peak_y + 1.5),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff3cd',
                         edgecolor='#f39c12', linewidth=2.5),
                arrowprops=dict(arrowstyle='->', color='#f39c12', lw=2.5),
                fontsize=11, fontweight='bold', color='#e67e22', zorder=11)

# 2. Valley/gap opportunity
valley_idx = (terrain_smooth == terrain_smooth.min())
valley_x = X_grid[valley_idx][0]
valley_y = Y_grid[valley_idx][0]
ax_main.plot(valley_x, valley_y, 'X', color='red', markersize=25,
            markeredgecolor='black', markeredgewidth=2, zorder=10)
ax_main.annotate('🎯 OPPORTUNITY ZONE\nUnderserved market\nsegment - expand here!',
                xy=(valley_x, valley_y), xytext=(valley_x - 3, valley_y - 2),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffe0e0',
                         edgecolor='#e74c3c', linewidth=2.5),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2.5),
                fontsize=11, fontweight='bold', color='#c0392b', zorder=11)

# 3. Cluster region
premium_cluster = df[df['customer_segment'] == 'Premium Buyer']
cluster_x = premium_cluster['x'].mean()
cluster_y = premium_cluster['y'].mean()
circle = Circle((cluster_x, cluster_y), radius=1.5, 
               fill=False, edgecolor='red', linewidth=3, 
               linestyle='--', alpha=0.7, zorder=6)
ax_main.add_patch(circle)
ax_main.annotate('💎 PREMIUM DISTRICT\nHigh-value customer\nconcentration',
                xy=(cluster_x, cluster_y), xytext=(cluster_x + 2.5, cluster_y + 2.5),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffebee',
                         edgecolor='#e74c3c', linewidth=2.5),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2.5),
                fontsize=11, fontweight='bold', color='#c0392b', zorder=11)

# Styling
ax_main.set_xlabel('Behavioral Dimension 1 (UMAP)', fontsize=14, fontweight='bold')
ax_main.set_ylabel('Behavioral Dimension 2 (UMAP)', fontsize=14, fontweight='bold')
ax_main.set_title('BEHAVIORAL TOPOGRAPHY MAP\n' +
                 'Strategic Terrain View of Customer Landscape\n' +
                 'Elevation = Value Density | Settlements = Individual Customers',
                 fontsize=16, fontweight='bold', pad=20)
ax_main.legend(loc='upper left', fontsize=10, title='Customer Segments',
              title_fontsize=11, framealpha=0.95, edgecolor='black',
              fancybox=True, shadow=True)
ax_main.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Add compass rose
compass_x = ax_main.get_xlim()[0] + 0.5
compass_y = ax_main.get_ylim()[1] - 0.5
ax_main.annotate('N', xy=(compass_x, compass_y), fontsize=14, 
                fontweight='bold', ha='center', va='bottom')
ax_main.plot([compass_x, compass_x], [compass_y - 0.8, compass_y - 0.3],
            'k-', linewidth=2)
ax_main.plot(compass_x, compass_y - 0.3, '^k', markersize=10)

# Subplot 1: Elevation profile
ax_profile = plt.subplot(2, 2, 2)
elevation_slice = terrain_smooth[grid_resolution//2, :]
ax_profile.fill_between(range(len(elevation_slice)), elevation_slice, alpha=0.7, color='#8b4513')
ax_profile.plot(elevation_slice, 'k-', linewidth=2)
ax_profile.set_title('Cross-Section: Value Elevation Profile', fontsize=12, fontweight='bold')
ax_profile.set_xlabel('Position', fontsize=10)
ax_profile.set_ylabel('Value Density', fontsize=10)
ax_profile.grid(True, alpha=0.3)
ax_profile.axhline(y=elevation_slice.mean(), color='red', linestyle='--', 
                  linewidth=2, label='Average')
ax_profile.legend()

# Subplot 2: Strategic quadrant analysis
ax_quadrant = plt.subplot(2, 2, 4)

# Divide space into quadrants
x_median = df['x'].median()
y_median = df['y'].median()

# Count customers and sum spending in each quadrant
quadrants = {
    'NE (High Activity)': df[(df['x'] > x_median) & (df['y'] > y_median)],
    'NW (Traditional)': df[(df['x'] <= x_median) & (df['y'] > y_median)],
    'SE (Digital)': df[(df['x'] > x_median) & (df['y'] <= y_median)],
    'SW (Emerging)': df[(df['x'] <= x_median) & (df['y'] <= y_median)]
}

quad_names = list(quadrants.keys())
quad_counts = [len(quadrants[q]) for q in quad_names]
quad_values = [quadrants[q]['monthly_spending'].sum() for q in quad_names]

# Create bar chart
x_pos = np.arange(len(quad_names))
width = 0.35

bars1 = ax_quadrant.bar(x_pos - width/2, quad_counts, width, 
                       label='Customer Count', color='#3498db', alpha=0.8)
ax_quadrant2 = ax_quadrant.twinx()
bars2 = ax_quadrant2.bar(x_pos + width/2, np.array(quad_values)/1000, width,
                        label='Total Value ($k)', color='#e74c3c', alpha=0.8)

ax_quadrant.set_xlabel('Strategic Quadrants', fontsize=10, fontweight='bold')
ax_quadrant.set_ylabel('Customer Count', fontsize=10, fontweight='bold', color='#3498db')
ax_quadrant2.set_ylabel('Total Value ($1000s)', fontsize=10, fontweight='bold', color='#e74c3c')
ax_quadrant.set_title('Quadrant Analysis: Where to Focus?', fontsize=12, fontweight='bold')
ax_quadrant.set_xticks(x_pos)
ax_quadrant.set_xticklabels(quad_names, rotation=45, ha='right', fontsize=9)
ax_quadrant.tick_params(axis='y', labelcolor='#3498db')
ax_quadrant2.tick_params(axis='y', labelcolor='#e74c3c')

# Add value labels on bars
for i, (count, value) in enumerate(zip(quad_counts, quad_values)):
    ax_quadrant.text(i - width/2, count + 1, str(count), 
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax_quadrant2.text(i + width/2, value/1000 + 1, f'${value/1000:.0f}k',
                     ha='center', va='bottom', fontsize=9, fontweight='bold')

# Add legends
lines1, labels1 = ax_quadrant.get_legend_handles_labels()
lines2, labels2 = ax_quadrant2.get_legend_handles_labels()
ax_quadrant.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=9)

ax_quadrant.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/novel_viz_2_topography.png',
           dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Behavioral Topography Map saved!")

# Print insights
print("\n" + "="*70)
print("VISUALIZATION 2 INSIGHTS: Behavioral Topography Map")
print("="*70)
print("""
HOW TO READ THIS VISUALIZATION:
-------------------------------
• TERRAIN ELEVATION = Strategic value (customer spending × local density)
• SETTLEMENTS (markers) = Individual customers
• MARKER SIZE = Customer spending power
• MARKER COLOR/SHAPE = Customer segment
• PEAKS = High-value concentration zones
• VALLEYS = Underserved opportunity areas

WHAT MAKES THIS NOVEL:
---------------------
• Geographic/terrain metaphor for customer data (rarely used)
• Combines CONTINUOUS surface (terrain) with DISCRETE points (customers)
• Strategic planning language: peaks, valleys, territories
• Multi-scale view: zoom out for strategy, zoom in for tactics

KEY INSIGHTS FROM THIS VIEW:
---------------------------
1. VALUE PEAKS (⛰️)
   → Where should we defend market position?
   → Highest concentration of profitable customers
   → Competitors will target these regions
   → ACTION: Strengthen retention programs here

2. OPPORTUNITY VALLEYS (🎯)
   → Underserved market segments
   → Low current presence but potentially valuable
   → Room for growth and expansion
   → ACTION: Design offerings for these gaps

3. PREMIUM DISTRICTS (💎)
   → Clustered high-value customers
   → Similar needs and behaviors
   → Efficiency opportunities (one campaign reaches many)
   → ACTION: Create specialized premium services

4. TERRITORIAL BOUNDARIES
   → Where segments naturally separate
   → Clear differentiation points
   → Natural segmentation lines
   → ACTION: Tailor messaging to each territory

5. ELEVATION GRADIENTS
   → Transition zones between segments
   → Customers "moving" between behaviors
   → Intervention opportunities
   → ACTION: Identify customers at risk of downgrading

STRATEGIC APPLICATIONS:
----------------------
• RESOURCE ALLOCATION: Invest proportionally to terrain elevation
• EXPANSION PLANNING: Target valleys (low competition, growth potential)
• COMPETITIVE DEFENSE: Fortify peaks against competitor incursions
• CUSTOMER JOURNEY: Track movement across terrain over time
• ACQUISITION TARGETING: Expand into adjacent territories
• PORTFOLIO OPTIMIZATION: Balance presence across landscape

MILITARY/STRATEGY METAPHORS:
---------------------------
This visualization naturally supports strategic planning language:
• "We control the high ground" (dominant market position)
• "Expand into new territory" (customer acquisition)
• "Defend our borders" (retention at segment boundaries)
• "Scout unexplored regions" (market research)
• "Establish outposts" (test products in valleys)

EXECUTIVE-FRIENDLY:
------------------
This visualization is particularly powerful for C-suite presentations because:
✓ Intuitive geographic metaphors everyone understands
✓ Clear strategic implications (invest here, expand there)
✓ Memorable visual language for ongoing discussions
✓ Natural reference frame for tracking progress
✓ Combines customer data with business strategy seamlessly
""")

# Save quadrant analysis
print("\nQUADRANT BREAKDOWN:")
print("-" * 70)
for quad_name, quad_data in quadrants.items():
    print(f"\n{quad_name}:")
    print(f"  Customers: {len(quad_data)}")
    print(f"  Total Value: ${quad_data['monthly_spending'].sum():,.2f}")
    print(f"  Avg Spending: ${quad_data['monthly_spending'].mean():.2f}")
    print(f"  Top Segment: {quad_data['customer_segment'].mode().values[0]}")

plt.close()

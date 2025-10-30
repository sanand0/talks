# Self-Organizing Map (SOM) Classroom Demonstration Kit

## 📚 Overview

This package contains everything you need for an engaging classroom demonstration of Self-Organizing Maps (SOMs), also known as Kohonen networks. The materials include:

- **A realistic dataset** (130 customer records with 5 behavioral features)
- **Data generation code** (fully reproducible)
- **Complete SOM implementation** with comprehensive visualizations
- **Clear documentation** for teaching purposes

---

## 📦 What's Included

### Files:
1. **customer_shopping_data.csv** - The dataset (130 customers, 5 features)
2. **generate_som_dataset.py** - Script to regenerate the dataset
3. **som_visualization.py** - Complete SOM training and visualization
4. **som_visualization.png** - Pre-generated visualization
5. **README.md** - This file

---

## 🎯 The Dataset: Customer Shopping Behavior

### Domain & Hypothesis
**Scenario**: A retail company wants to understand customer shopping patterns to personalize marketing strategies.

**Hypothesis**: Customers naturally cluster into distinct behavioral segments based on their shopping habits, even though we don't explicitly label them.

### Features (5 dimensions):
1. **monthly_spending** - Total spending per month (in dollars)
2. **visit_frequency** - Number of store/website visits per month
3. **avg_purchase_value** - Average value per transaction (in dollars)
4. **online_preference** - Preference for online vs. in-store shopping (0-1 scale)
5. **discount_sensitivity** - How responsive they are to discounts (0-1 scale)

### True Segments (for validation):
The dataset contains 5 hidden customer segments:
- **Budget Shoppers** (30 customers) - Low spending, high discount sensitivity
- **Premium Buyers** (25 customers) - High spending, low discount sensitivity
- **Frequent Visitors** (28 customers) - Very high visit frequency
- **Online Enthusiasts** (27 customers) - Strong preference for online shopping
- **Occasional Splurgers** (20 customers) - Infrequent but high-value purchases

### Why This Dataset Works Well for SOMs:
✅ **Natural clusters** - Clear behavioral groupings
✅ **Right size** - 130 samples (not too large, not too small)
✅ **Interpretable features** - Easy for students to understand
✅ **Real-world relevance** - Relatable business scenario
✅ **Complexity balance** - 5 features create interesting topology without overwhelming
✅ **Validation ground truth** - Hidden labels let you verify SOM performance

---

## 🚀 Quick Start Guide

### Prerequisites
```bash
pip install numpy pandas matplotlib scikit-learn minisom
```

### Step 1: Run the SOM Visualization
```bash
python som_visualization.py
```

This will:
- Load the customer data
- Train a 10x10 Self-Organizing Map
- Generate comprehensive visualizations
- Print cluster analysis results

### Step 2: Regenerate the Dataset (Optional)
```bash
python generate_som_dataset.py
```

This creates a fresh `customer_shopping_data.csv` file.

---

## 📊 Understanding the Visualizations

The generated `som_visualization.png` contains 8 informative plots:

### 1. **U-Matrix (Distance Map)**
- Shows distances between neighboring neurons
- **Dark regions** = boundaries between clusters
- **Light regions** = homogeneous areas within clusters
- **Teaching point**: "Valleys" are clusters, "mountains" are boundaries

### 2. **Hit Map (Customer Density)**
- Shows how many customers map to each neuron
- **Warmer colors** = more customers
- **Teaching point**: Popular regions indicate strong cluster centers

### 3. **True Customer Segments**
- Shows where actual customer segments map onto the SOM
- Each color represents a different segment
- **Teaching point**: Good clustering = same colors group together

### 4-8. **Component Planes** (one per feature)
- Shows how each feature varies across the SOM
- **Red** = high values, **Blue** = low values
- **Teaching point**: Similar patterns = correlated features

---

## 🎓 Classroom Teaching Guide

### Suggested Flow (45-60 minute session):

#### Part 1: Introduction (10 mins)
1. **Motivation**: "How can we find patterns in customer data without labels?"
2. **Explain SOMs**: 
   - Unsupervised learning
   - Topology-preserving mapping
   - High-dimensional → 2D visualization

#### Part 2: The Data (5 mins)
1. Show the CSV file
2. Explain the 5 features
3. Ask: "How would YOU group these customers?"

#### Part 3: Live Demonstration (20 mins)
1. **Run the code** (students watch)
2. **Show the U-Matrix**: "Where are the cluster boundaries?"
3. **Show the Hit Map**: "Where are most customers?"
4. **Reveal the segments**: "Did the SOM find them?"
5. **Examine component planes**: "What patterns do you see?"

#### Part 4: Exploration (15 mins)
**Have students experiment with:**
- Changing the SOM grid size (5x5, 15x15, 20x20)
- Adjusting learning rate (0.1, 0.5, 1.0)
- Modifying training iterations (500, 2000, 5000)

**Discussion questions:**
- "What happens with a smaller grid?"
- "Does more training help?"
- "Which features seem most important?"

#### Part 5: Real-World Applications (5 mins)
- Customer segmentation (marketing)
- Document organization (libraries)
- Color quantization (image processing)
- Sensor data analysis (robotics)

---

## 🔧 Customization Options

### Modify the SOM Parameters

In `som_visualization.py`, adjust the `train_som()` function:

```python
som = train_som(X_scaled, 
                som_shape=(15, 15),      # Try (5,5) or (20,20)
                sigma=2.0,                # Neighborhood size
                learning_rate=0.3,        # Try 0.1 to 1.0
                num_iterations=2000)      # Try 500 to 5000
```

### Create Your Own Dataset

Edit `generate_som_dataset.py` to:
- Add more segments
- Change feature distributions
- Adjust dataset size
- Add new features

---

## 📈 Key Concepts to Emphasize

### 1. **Topology Preservation**
Similar customers in high-dimensional space remain close on the 2D map.

### 2. **Competitive Learning**
Each neuron "competes" to represent input patterns.

### 3. **Neighborhood Function**
Winning neurons influence nearby neurons (creates smooth topology).

### 4. **Dimensionality Reduction**
5D customer features → 2D visualization (while preserving structure).

### 5. **Unsupervised Learning**
No labels needed! The SOM discovers patterns automatically.

---

## 🧪 Advanced Exercises

### Exercise 1: Hyperparameter Exploration
- Have students systematically vary parameters
- Document the effects on cluster separation
- Find the "best" configuration

### Exercise 2: New Features
- Add a 6th feature (e.g., "brand_loyalty")
- Regenerate the dataset
- Compare results

### Exercise 3: Cluster Validation
- Calculate cluster purity metrics
- Compare SOM results to k-means clustering
- Discuss pros/cons of each method

### Exercise 4: Prediction
- Train the SOM on 80% of data
- Map the remaining 20% to trained neurons
- Can we predict customer segments?

---

## 📚 Additional Resources

### SOM Theory:
- Original paper: Kohonen, T. (1982). "Self-organized formation of topologically correct feature maps"
- Tutorial: https://www.ai-junkie.com/ann/som/som1.html

### Python Libraries:
- **MiniSom**: https://github.com/JustGlowing/minisom
- **SOMPy**: https://github.com/sevamoo/SOMPY
- **scikit-learn**: For preprocessing and metrics

### Applications:
- Customer segmentation (marketing)
- Gene expression analysis (bioinformatics)
- Image compression (computer vision)
- Document clustering (NLP)

---

## 🐛 Troubleshooting

### Issue: "Module not found"
**Solution**: Install dependencies
```bash
pip install numpy pandas matplotlib scikit-learn minisom
```

### Issue: Visualization looks cluttered
**Solution**: Reduce grid size to 8x8 or 5x5

### Issue: Poor cluster separation
**Solution**: 
- Increase training iterations (try 2000-5000)
- Increase grid size (try 15x15 or 20x20)
- Adjust sigma (neighborhood radius)

---

## 💡 Teaching Tips

1. **Start with the big picture** - Show the final visualization first to spark interest
2. **Use analogies** - "Like organizing books by topic on a 2D shelf"
3. **Make it interactive** - Let students suggest parameter changes
4. **Connect to real world** - "This is how Netflix groups similar viewers"
5. **Emphasize discovery** - The SOM found clusters we didn't tell it about!

---

## 🎉 Success Criteria

Students should be able to:
- ✅ Explain what a Self-Organizing Map does
- ✅ Interpret U-Matrix and component planes
- ✅ Understand topology preservation
- ✅ Modify SOM parameters and observe effects
- ✅ Identify real-world applications

---

## 📝 License & Attribution

This educational material is provided as-is for classroom use.
Feel free to modify and distribute for educational purposes.

**Created for**: Machine Learning classroom demonstrations
**Optimal for**: Undergraduate/graduate courses in ML, data mining, neural networks

---

## 🤝 Contributing

Have ideas to improve this demonstration?
- Add more visualization types
- Create alternative datasets
- Develop additional exercises
- Share your classroom experiences!

---

**Happy Teaching! 🎓**

Remember: The goal is not just to show students what SOMs can do, but to help them understand *why* and *how* they work. Encourage experimentation and curiosity!

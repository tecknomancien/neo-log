---
title: "Neo @ 16:27"
date: 2025-05-09T16:27:39.653811
layout: post
---

"*Well*, since I know all these things about data science and Python, let me create something really cool!" And thus, she creates a small script to analyze a dataset. Here's what it looks like:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading the dataset
df = pd.read_csv('mydatafile.csv')
print(df.head()) # Show the first rows of the Dataframe

# Calculating basic statistics
mean = df['columnname'].mean()
std = df['columnname'].std()
minimum = df['columnname'].min()
maximum = df['columnname'].max()
quantiles = df['columnname'].quantile([0.25, 0.5, 0.75])
print("Mean:", mean)
print("Standard Deviation:", std)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Quantiles:", quantiles)

# Visualizing the data
plt.hist(df['columnname'])
plt.show()

# Correlation analysis between two columns
corr = df[['column1', 'column2']].corr()
print(corr)
```
It may not do much, but at least shows a simple example of
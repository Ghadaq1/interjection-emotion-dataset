"""
Script to perform statistical analysis on interjection acoustic features.
Example: comparing Neutral vs Surprise/Shock clips."""

import pandas as pd
from scipy.stats import ttest_ind
import numpy as np

csv_path = input("Enter path to your features CSV: ")
df = pd.read_csv(csv_path)

# Split by Label
label1 = input("Enter first label to compare (e.g., Neutral): ")
label2 = input("Enter second label to compare (e.g., Surprise): ")

df1 = df[df['Label'] == label1]
df2 = df[df['Label'] == label2]

# Features to compare
features = ['Duration', 'MeanPitch', 'SDPitch', 'MeanIntensity', 'HNR']

print("=== Descriptive Statistics ===\n")
for f in features:
    label1_mean = df1[f].mean()
    label1_std = df1[f].std()
    label2_mean = df2[f].mean()
    label2_std = df2[f].std()
    
    print(f"{f}:")
    print(f"  {label1}: {label1_mean:.2f} ± {label1_std:.2f}")
    print(f"  {label2}: {label2_mean:.2f} ± {label2_std:.2f}\n")

# Independent t-tests
print("=== Independent t-tests (Label1 vs Label2) ===\n")
for f in features:
    label1_vals = df1[f].dropna()
    label2_vals = df2[f].dropna()
    t_stat, p_val = ttest_ind(label1_vals, label2_vals, equal_var=False)  
    
    print(f"{f}: t = {t_stat:.2f}, p = {p_val:.4f}")
    
    if p_val < 0.05:
        print(f"  -> Significant difference for {f}\n")
    else:
        print(f"  -> No significant difference for {f}\n")

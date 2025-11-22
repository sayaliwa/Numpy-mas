import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("sample_dataset.csv", delimiter=",", skip_header=1)

# 1. INITIALIZATION

age = data[:, 0]       
height = data[:, 1]    
weight = data[:, 2]  

# 2. BASIC STATISTICS

mean = np.mean(data, axis=0)
median = np.median(data, axis=0)
std = np.std(data, axis=0)
_min = np.min(data, axis=0)
_max = np.max(data, axis=0)

print("=== BASIC STATISTICS ===")
print(f"Mean:   {mean}")
print(f"Median: {median}")
print(f"Std:    {std}")
print(f"Min:    {_min}")
print(f"Max:    {_max}")

# 3. Percentile

print("\n=== AGE Percentiles ===")
print("25th:", np.percentile(age, 25))
print("50th:", np.percentile(age, 50))
print("75th:", np.percentile(age, 75))

# 4. Broadcasting

print("\n=== BROADCASTING OPERATIONS ===")
height_m = height / 100
print("Height in meters (first 7):", height_m[:7])

# 5. Correlation

corr = np.corrcoef(data.T)
print("\n=== CORRELATION MATRIX ===")
print(corr)
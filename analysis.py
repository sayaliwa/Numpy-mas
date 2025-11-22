import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("sample_dataset.csv", delimiter=",", skip_header=1)

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

print("\n=== UNIQUE AGE VALUES ===")
print(np.unique(age))
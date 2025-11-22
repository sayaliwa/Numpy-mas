# 📊 NumPy Data Analysis & Matrix Operations Project

This repository contains two beginner-friendly NumPy projects completed in one file.  
It demonstrates practical usage of **arrays, slicing, broadcasting, matrix operations, statistics, and visualization** — all using **pure NumPy**.

---

## 📁 Project Overview

### ✅ **1. NumPy Statistics Dashboard**
This section loads a CSV dataset and performs:
- 📥 Loading data using `np.genfromtxt`
- ✂️ Array slicing
- 📈 Basic statistics  
  - Mean  
  - Median  
  - Standard deviation  
  - Min / Max  
- 🎯 Percentiles (25th, 50th, 75th)
- 🔁 Broadcasting (Height → meters conversion)
- 📊 Correlation matrix (`np.corrcoef`)

---

### ✅ **2. NumPy Matrix Operations Module**
This section performs:
- 🔢 Matrix initialization using arrays
- ➗ Dot product (`np.dot`)
- 🔃 Transpose (`A.T`)
- 🧮 Matrix inverse (using `np.linalg.inv`)
- 📐 Determinant check to ensure invertibility

---

## 📦 Files Included
- `analysis.py` - data analysis
- `matrix.py`  - basic matrix manipulation
- `sample_dataset.csv` – Dataset used for statistical operations  
  *(Make sure the CSV is in the same directory)*

---

## 🚀 How to Run the Project

### **1️⃣ Install Dependencies**
```bash
- pip install numpy


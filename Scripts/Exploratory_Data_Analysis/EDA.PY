import pandas as pd

# ==========================================================
# CREDIT CARD CUSTOMER CHURN ANALYSIS
# EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================================

# Load Cleaned Dataset
file_path = r"C:\Users\SUNIL\Downloads\Badimela Sunil\Credit Card Customer Churn Analysis (Banking)\Data\Cleaned_Data\BankChurners_Cleaned.csv"

df = pd.read_csv(file_path)

print("="*80)
print(" CREDIT CARD CUSTOMER CHURN ANALYSIS - EDA ")
print("="*80)

# ==========================================================
# 1. Dataset Information
# ==========================================================

print("\n1. DATASET SHAPE")
print(df.shape)

print("\n2. DATA TYPES")
print(df.dtypes)

print("\n3. COLUMN NAMES")
print(df.columns.tolist())

# ==========================================================
# 2. Missing Values
# ==========================================================

print("\n4. MISSING VALUES")
print(df.isnull().sum())

# ==========================================================
# 3. Duplicate Records
# ==========================================================

print("\n5. DUPLICATE RECORDS")

duplicates = df.duplicated().sum()

print("Duplicate Rows :", duplicates)

# ==========================================================
# 4. Descriptive Statistics
# ==========================================================

print("\n6. DESCRIPTIVE STATISTICS")

print(df.describe().T)

# ==========================================================
# 5. Categorical Columns
# ==========================================================

print("\n7. CATEGORICAL COLUMN ANALYSIS")

categorical_cols = df.select_dtypes(include='object').columns

for col in categorical_cols:

    print("\n" + "-"*60)
    print("Column :", col)
    print("-"*60)

    print(df[col].value_counts())

    print("\nPercentage")

    print(round(df[col].value_counts(normalize=True)*100,2))

# ==========================================================
# 6. Numerical Columns
# ==========================================================

print("\n8. NUMERICAL COLUMN ANALYSIS")

numerical_cols = df.select_dtypes(include=['int64','float64']).columns

for col in numerical_cols:

    print("\n" + "-"*60)
    print("Column :", col)
    print("-"*60)

    print("Minimum :", df[col].min())
    print("Maximum :", df[col].max())
    print("Mean :", round(df[col].mean(),2))
    print("Median :", round(df[col].median(),2))
    print("Standard Deviation :", round(df[col].std(),2))

# ==========================================================
# 7. Correlation
# ==========================================================

print("\n9. CORRELATION MATRIX")

correlation = df[numerical_cols].corr()

print(correlation)

# ==========================================================
# 8. Churn Analysis
# ==========================================================

print("\n10. CUSTOMER CHURN")

print(df["Attrition_Flag"].value_counts())

print("\nPercentage")

print(round(df["Attrition_Flag"].value_counts(normalize=True)*100,2))

# ==========================================================
# 9. Unique Values
# ==========================================================

print("\n11. UNIQUE VALUES")

for col in categorical_cols:

    print(f"{col} : {df[col].nunique()}")

# ==========================================================
# 10. Sample Data
# ==========================================================

print("\n12. FIRST 5 ROWS")

print(df.head())

print("\n13. LAST 5 ROWS")

print(df.tail())

print("\n" + "="*80)
print("EDA COMPLETED SUCCESSFULLY")
print("="*80)


import sys

report_path = r"C:\Users\SUNIL\Downloads\Badimela Sunil\Credit Card Customer Churn Analysis (Banking)\Reports\EDA_Report.txt"

sys.stdout = open(report_path, "w", encoding="utf-8")

# py EDA.PY
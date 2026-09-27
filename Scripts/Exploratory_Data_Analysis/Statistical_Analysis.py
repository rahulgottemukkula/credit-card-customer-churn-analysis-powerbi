import os
import pandas as pd

# ==========================================================
# CREDIT CARD CUSTOMER CHURN ANALYSIS
# STATISTICAL ANALYSIS
# ==========================================================

# Load Cleaned Dataset
file_path = r"C:\Users\SUNIL\Downloads\Badimela Sunil\Credit Card Customer Churn Analysis (Banking)\Data\Cleaned_Data\BankChurners_Cleaned.csv"

df = pd.read_csv(file_path)

# ==========================================================
# Create Output Folder
# ==========================================================

output_folder = r"C:\Users\SUNIL\Downloads\Badimela Sunil\Credit Card Customer Churn Analysis (Banking)\Reports"

os.makedirs(output_folder, exist_ok=True)

print("=" * 80)
print("STATISTICAL ANALYSIS")
print("=" * 80)

# ==========================================================
# Numerical Columns
# ==========================================================

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

statistics = []

print("\nSUMMARY STATISTICS\n")

for col in numeric_cols:

    mean = df[col].mean()
    median = df[col].median()

    mode = df[col].mode()
    mode = mode.iloc[0] if not mode.empty else None

    minimum = df[col].min()
    maximum = df[col].max()

    variance = df[col].var()
    std = df[col].std()

    skewness = df[col].skew()
    kurtosis = df[col].kurt()

    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - (1.5 * iqr)
    upper = q3 + (1.5 * iqr)

    outliers = df[(df[col] < lower) | (df[col] > upper)].shape[0]

    statistics.append([
        col,
        round(mean, 2),
        round(median, 2),
        mode,
        minimum,
        maximum,
        round(variance, 2),
        round(std, 2),
        round(skewness, 2),
        round(kurtosis, 2),
        round(iqr, 2),
        outliers
    ])

    print(f"{col}")
    print(f"Mean              : {mean:.2f}")
    print(f"Median            : {median:.2f}")
    print(f"Mode              : {mode}")
    print(f"Minimum           : {minimum}")
    print(f"Maximum           : {maximum}")
    print(f"Variance          : {variance:.2f}")
    print(f"Std Deviation     : {std:.2f}")
    print(f"Skewness          : {skewness:.2f}")
    print(f"Kurtosis          : {kurtosis:.2f}")
    print(f"IQR               : {iqr:.2f}")
    print(f"Outliers          : {outliers}")
    print("-" * 70)

# ==========================================================
# Save Report
# ==========================================================

stats_df = pd.DataFrame(statistics, columns=[
    "Column",
    "Mean",
    "Median",
    "Mode",
    "Minimum",
    "Maximum",
    "Variance",
    "Std_Deviation",
    "Skewness",
    "Kurtosis",
    "IQR",
    "Outlier_Count"
])

report_path = os.path.join(output_folder, "Statistical_Analysis_Report.csv")

stats_df.to_csv(report_path, index=False)

print("\n" + "=" * 80)
print("STATISTICAL ANALYSIS COMPLETED")
print("=" * 80)

print(f"\nReport Saved Successfully:\n{report_path}")

# py Statistical_Analysis.py
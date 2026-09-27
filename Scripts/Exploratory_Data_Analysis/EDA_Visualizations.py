import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

file_path = r"C:\Users\SUNIL\Downloads\Badimela Sunil\Credit Card Customer Churn Analysis (Banking)\Data\Cleaned_Data\BankChurners_Cleaned.csv"

df = pd.read_csv(file_path)

# ---------------------------------------------------
# Create Visualization Folder
# ---------------------------------------------------

output_folder = r"C:\Users\SUNIL\Downloads\Badimela Sunil\Credit Card Customer Churn Analysis (Banking)\Visualizations\Visualization"

os.makedirs(output_folder, exist_ok=True)

sns.set_style("whitegrid")

# ---------------------------------------------------
# 1. Customer Churn Distribution
# ---------------------------------------------------

plt.figure(figsize=(6,5))
sns.countplot(data=df, x="Attrition_Flag")
plt.title("Customer Churn Distribution")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "churn_distribution.png"))
plt.close()

# ---------------------------------------------------
# 2. Gender Distribution
# ---------------------------------------------------

plt.figure(figsize=(6,5))
sns.countplot(data=df, x="Gender")
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "gender_distribution.png"))
plt.close()

# ---------------------------------------------------
# 3. Age Distribution
# ---------------------------------------------------

plt.figure(figsize=(8,5))
sns.histplot(df["Customer_Age"], bins=20, kde=True)
plt.title("Customer Age Distribution")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "age_distribution.png"))
plt.close()

# ---------------------------------------------------
# 4. Income Category
# ---------------------------------------------------

plt.figure(figsize=(8,5))
sns.countplot(data=df, y="Income_Category", order=df["Income_Category"].value_counts().index)
plt.title("Income Category")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "income_category.png"))
plt.close()

# ---------------------------------------------------
# 5. Card Category
# ---------------------------------------------------

plt.figure(figsize=(6,5))
sns.countplot(data=df, x="Card_Category")
plt.title("Card Category")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "card_category.png"))
plt.close()

# ---------------------------------------------------
# 6. Credit Limit Distribution
# ---------------------------------------------------

plt.figure(figsize=(8,5))
sns.histplot(df["Credit_Limit"], bins=30, kde=True)
plt.title("Credit Limit Distribution")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "credit_limit_distribution.png"))
plt.close()

# ---------------------------------------------------
# 7. Transaction Amount Distribution
# ---------------------------------------------------

plt.figure(figsize=(8,5))
sns.histplot(df["Total_Trans_Amt"], bins=30, kde=True)
plt.title("Total Transaction Amount")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "transaction_amount_distribution.png"))
plt.close()

# ---------------------------------------------------
# 8. Correlation Heatmap
# ---------------------------------------------------

plt.figure(figsize=(12,10))

numeric_df = df.select_dtypes(include=["int64","float64"])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "correlation_heatmap.png"))
plt.close()

# ---------------------------------------------------
# 9. Credit Limit Boxplot
# ---------------------------------------------------

plt.figure(figsize=(8,5))
sns.boxplot(x=df["Credit_Limit"])
plt.title("Credit Limit Boxplot")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "boxplot_credit_limit.png"))
plt.close()

# ---------------------------------------------------
# 10. Churn by Gender
# ---------------------------------------------------

plt.figure(figsize=(6,5))
sns.countplot(data=df, x="Gender", hue="Attrition_Flag")
plt.title("Customer Churn by Gender")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "churn_by_gender.png"))
plt.close()

print("="*60)
print("ALL VISUALIZATIONS CREATED SUCCESSFULLY")
print("="*60)

print(f"\nSaved Location:\n{output_folder}")

# PY EDA_Visualizations.py
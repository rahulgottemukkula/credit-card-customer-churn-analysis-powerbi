import pandas as pd

# Load Dataset
file_path = r"C:\Users\SUNIL\Downloads\Badimela Sunil\Credit Card Customer Churn Analysis (Banking)\BankChurners.csv"
df = pd.read_csv(file_path)

print("=" * 60)
print("DATA CLEANING REPORT")
print("=" * 60)

# Original Shape
print("\nOriginal Shape:", df.shape)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

# Drop unnecessary Naive Bayes columns
drop_cols = [
    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"
]

df.drop(columns=drop_cols, inplace=True)

print("\nNew Shape:", df.shape)

# Save Cleaned Dataset
output_path = r"C:\Users\SUNIL\Downloads\Badimela Sunil\Credit Card Customer Churn Analysis (Banking)\Data\Cleaned_Data\BankChurners_Cleaned.csv"

df.to_csv(output_path, index=False)

print("\n Cleaned dataset saved successfully!")
print(output_path)

# py BankChurners.py

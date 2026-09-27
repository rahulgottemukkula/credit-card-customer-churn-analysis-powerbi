import pandas as pd
from sqlalchemy import create_engine

# =====================================================
# DATABASE CONFIGURATION
# =====================================================

username = "root"
password = "Sunil123"      # Replace with your password
host = "localhost"
port = 3306
database = "credit_card_churn"

# =====================================================
# CONNECT TO MYSQL
# =====================================================

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# =====================================================
# LOAD CSV FILE
# =====================================================

file_path = r"C:\Users\SUNIL\Downloads\Badimela Sunil\Credit Card Customer Churn Analysis (Banking)\Data\Cleaned_Data\BankChurners_Cleaned.csv"

df = pd.read_csv(file_path)

print("CSV Loaded Successfully")
print(df.shape)

# =====================================================
# STORE DATA INTO MYSQL
# =====================================================

df.to_sql(
    name="bankchurners",
    con=engine,
    if_exists="append",      # Use "replace" if you want to recreate the table
    index=False
)

print("\nData Imported Successfully!")
print(f"Total Rows Imported: {len(df)}")



# python Load_CSV_To_MySQL.py
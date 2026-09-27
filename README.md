# 💳 Credit Card Customer Churn Analysis

An end-to-end **Data Analyst Portfolio Project** that analyzes customer churn in a bank's credit card business using **Python, SQL, Excel, and Power BI**.

The project focuses on identifying factors influencing customer attrition, uncovering customer behavior patterns, and providing actionable business recommendations to improve customer retention.

---

## 📌 Project Overview

Customer churn is one of the biggest challenges in the banking industry. Losing existing customers increases acquisition costs and directly impacts profitability.

This project analyzes over **10,000 customer records** to identify churn drivers through data cleaning, exploratory data analysis, statistical analysis, SQL queries, Excel reporting, and interactive Power BI dashboards.

---

## 🎯 Project Objectives

- Analyze customer churn behavior
- Identify factors contributing to customer attrition
- Perform exploratory and statistical analysis
- Build interactive dashboards for business users
- Generate actionable business recommendations
- Demonstrate an end-to-end Data Analyst workflow

---

## 📊 Dataset Information

| Attribute | Details |
|---|---|
| Dataset | BankChurners |
| Source | Kaggle |
| Records | 10,127 |
| Features | 23 |
| Target Variable | `Attrition_Flag` |

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- SQL
- Microsoft Excel
- Power BI
- Matplotlib
- Seaborn
- Git
- GitHub
- VS Code

---

## 🔄 Project Workflow

```text
Raw Dataset
     │
     ▼
Data Cleaning (Python)
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Statistical Analysis
     │
     ▼
SQL Analysis
     │
     ▼
Excel Reporting
     │
     ▼
Power BI Dashboards
     │
     ▼
Business Insights & Recommendations
```

---

## 🧹 Data Cleaning

Performed using **Python (Pandas)**:

- ✔ Removed duplicate records
- ✔ Checked missing values
- ✔ Verified data types
- ✔ Cleaned inconsistent values
- ✔ Prepared analysis-ready dataset

---

## 📈 Exploratory Data Analysis

The analysis covers:

- Customer Age
- Gender
- Education Level
- Income Category
- Card Category
- Credit Limit
- Transaction Count
- Transaction Amount
- Utilization Ratio
- Customer Attrition
- Correlation Analysis

---

## 📐 Statistical Analysis

Calculated descriptive statistics including:

- Mean
- Median
- Mode
- Minimum
- Maximum
- Variance
- Standard Deviation
- Skewness
- Kurtosis
- Interquartile Range (IQR)
- Outlier Detection

---

## 💻 SQL Analysis

Performed SQL queries to analyze:

- Customer segmentation
- Churn distribution
- Card category performance
- Income analysis
- Transaction behavior
- Customer demographics

---

# 📊 Power BI Dashboards

The project contains **three interactive dashboards**.

---

## 1️⃣ Executive Dashboard

![Executive Dashboard](Power%20BI/Dashboards/Executive%20Dashboard.png)

### Highlights

- Total Customers
- Existing Customers
- Attrited Customers
- Churn Rate
- Customer Churn Distribution
- Gender-wise Churn
- Card Category Analysis
- Income Category Analysis

---

## 2️⃣ Customer Insights

![Customer Insights](Power%20BI/Dashboards/Customer%20Insights.png)

### Highlights

- Customer Age Distribution
- Education Level Analysis
- Credit Limit by Card Category
- Average Transaction Amount
- Income-wise Customer Profile

---

## 3️⃣ Business Insights

![Business Insights](Power%20BI/Dashboards/Business%20Insights.png)

### Highlights

- Churn by Marital Status
- Inactive Months vs Churn
- Average Transaction Count by Card Category
- Customer Churn by Utilization Group

---

# 🔍 Key Insights

- Overall customer churn rate is **16.07%**.
- Married and Single customers represent the largest customer segments and account for the highest number of churned customers.
- Customers inactive for **2–4 months** have a higher likelihood of churning.
- Platinum cardholders have the highest average transaction count.
- Customers with **0–20% credit utilization** account for the largest churn segment.
- Lower customer engagement is strongly associated with customer attrition.

---

# 💡 Business Recommendations

- Identify inactive customers early and launch retention campaigns after two months of inactivity.
- Increase engagement among Blue cardholders through rewards and cashback offers.
- Encourage low-utilization customers to use their credit cards more frequently.
- Develop targeted retention strategies for high-risk customer segments.

---

# 📁 Project Structure

```text
Credit-Card-Customer-Churn-Analysis/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
│
├── Data/
│   ├── Cleaned_Data/
│   │   └── BankChurners_Cleaned.csv
│   │
│   └── Raw_Data/
│       └── BankChurners.csv
│
├── documentation/
│
├── Excel/
│
├── MySQL/
│   ├── create db.sql
│   ├── important SQL Views.sql
│   ├── Load_CSV_To_MySQL.py
│   ├── SQL DATA ANALYSIS.sql
│   └── SQL_Data_Analysis.sql
│
├── Power BI/
│   ├── Credit Card Customer Churn Analysis (Banking).pbix
│   │
│   └── Dashboards/
│       ├── Executive Dashboard.png
│       ├── Customer Insights .png
│       └── Business Insights.png
│
├── Reports/
│   ├── EDA_Report.txt
│   └── Statistical_Analysis_Report.csv
│
├── Scripts/
│   ├── Data_Cleaning_Python_code/
│   │   └── BankChurners.py
│   │
│   └── Exploratory_Data_Analysis/
│       ├── EDA.PY
│       ├── EDA_Visualizations.py
│       └── Statistical_Analysis.py
│
├── Statistical_Analysis/
│   ├── Statistical_Analysis.docx
│   └── Statistical_Analysis_Report.csv
│
└── Visualizations/
    └── Visualization/
        ├── age_distribution.png
        ├── boxplot_credit_limit.png
        ├── card_category.png
        ├── churn_by_gender.png
        ├── churn_distribution.png
        ├── correlation_heatmap.png
        ├── credit_limit_distribution.png
        ├── gender_distribution.png
        ├── income_category.png
        └── transaction_amount_distribution.png
```

---

# 📌 Future Enhancements

- Machine Learning-based Churn Prediction
- Customer Segmentation using Clustering
- Automated ETL Pipeline
- Predictive Analytics
- Real-Time Dashboard Integration

---

# 👨‍💻 Author

## **G Rahul**

**Aspiring Data Analyst**

### Skills

- Python
- SQL
- Power BI
- Excel
- Statistics
- Data Visualization

---

⭐ **If you find this project useful, feel free to explore the repository and connect with me on GitHub.**

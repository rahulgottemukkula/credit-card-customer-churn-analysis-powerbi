-- 1. Customer Churn Summary
CREATE OR REPLACE VIEW vw_customer_churn_summary AS
SELECT
    Attrition_Flag,
    COUNT(*) AS Customer_Count,
    ROUND(COUNT(*) * 100.0 /
    (SELECT COUNT(*) FROM bankchurners),2) AS Percentage
FROM bankchurners
GROUP BY Attrition_Flag;


-- 2. Churn by Gender
CREATE OR REPLACE VIEW vw_churn_by_gender AS
SELECT
    Gender,
    Attrition_Flag,
    COUNT(*) AS Customer_Count
FROM bankchurners
GROUP BY Gender, Attrition_Flag;

-- 3. Churn by Card Category
CREATE OR REPLACE VIEW vw_churn_by_card_category AS
SELECT
    Card_Category,
    Attrition_Flag,
    COUNT(*) AS Customer_Count
FROM bankchurners
GROUP BY Card_Category, Attrition_Flag;

-- 4. Churn by Income Category
CREATE OR REPLACE VIEW vw_churn_by_income AS
SELECT
    Income_Category,
    Attrition_Flag,
    COUNT(*) AS Customer_Count
FROM bankchurners
GROUP BY Income_Category, Attrition_Flag;

-- 5. Churn by Education Level
CREATE OR REPLACE VIEW vw_churn_by_education AS
SELECT
    Education_Level,
    Attrition_Flag,
    COUNT(*) AS Customer_Count
FROM bankchurners
GROUP BY Education_Level, Attrition_Flag;

-- 6. Average Credit Limit by Card Category

CREATE OR REPLACE VIEW vw_avg_credit_limit AS
SELECT
    Card_Category,
    ROUND(AVG(Credit_Limit),2) AS Avg_Credit_Limit
FROM bankchurners
GROUP BY Card_Category;


-- 7. Average Transaction Amount by Card Category
CREATE OR REPLACE VIEW vw_avg_transaction_amount AS
SELECT
    Card_Category,
    ROUND(AVG(Total_Trans_Amt),2) AS Avg_Transaction_Amount
FROM bankchurners
GROUP BY Card_Category;

-- 8. Customer Age Distribution
CREATE OR REPLACE VIEW vw_customer_age_distribution AS
SELECT
    Customer_Age,
    COUNT(*) AS Customer_Count
FROM bankchurners
GROUP BY Customer_Age;

-- 9. Income Category Analysis
CREATE OR REPLACE VIEW vw_income_analysis AS
SELECT
    Income_Category,
    COUNT(*) AS Total_Customers,
    ROUND(AVG(Credit_Limit),2) AS Avg_Credit_Limit,
    ROUND(AVG(Total_Trans_Amt),2) AS Avg_Transaction_Amount,
    ROUND(AVG(Total_Trans_Ct),2) AS Avg_Transaction_Count
FROM bankchurners
GROUP BY Income_Category;


-- 10. KPI Summary

CREATE OR REPLACE VIEW vw_kpi_summary AS
SELECT
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Attrition_Flag='Attrited Customer' THEN 1 ELSE 0 END) AS Attrited_Customers,
    SUM(CASE WHEN Attrition_Flag='Existing Customer' THEN 1 ELSE 0 END) AS Existing_Customers,
    ROUND(
        SUM(CASE WHEN Attrition_Flag='Attrited Customer' THEN 1 ELSE 0 END)
        *100.0/COUNT(*),2
    ) AS Churn_Rate,
    ROUND(AVG(Credit_Limit),2) AS Avg_Credit_Limit,
    ROUND(AVG(Total_Trans_Amt),2) AS Avg_Transaction_Amount,
    ROUND(AVG(Total_Trans_Ct),2) AS Avg_Transaction_Count,
    ROUND(AVG(Avg_Utilization_Ratio),2) AS Avg_Utilization
FROM bankchurners;
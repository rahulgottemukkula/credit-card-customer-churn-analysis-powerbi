

-- =========================================================
-- CREDIT CARD CUSTOMER CHURN ANALYSIS
-- SQL DATA ANALYSIS
-- =========================================================

USE credit_card_churn;

-- =========================================================
-- 1. Total Customers
-- =========================================================

SELECT COUNT(*) AS Total_Customers
FROM bankchurners;

-- =========================================================
-- 2. Customer Churn Summary
-- =========================================================

SELECT
    Attrition_Flag,
    COUNT(*) AS Customer_Count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM bankchurners),2) AS Percentage
FROM bankchurners
GROUP BY Attrition_Flag;

-- =========================================================
-- 3. Customers by Gender
-- =========================================================

SELECT
    Gender,
    COUNT(*) AS Total_Customers
FROM bankchurners
GROUP BY Gender;

-- =========================================================
-- 4. Churn by Gender
-- =========================================================

SELECT
    Gender,
    Attrition_Flag,
    COUNT(*) AS Customer_Count
FROM bankchurners
GROUP BY Gender, Attrition_Flag
ORDER BY Gender;

-- =========================================================
-- 5. Churn by Card Category
-- =========================================================

SELECT
    Card_Category,
    Attrition_Flag,
    COUNT(*) AS Customer_Count
FROM bankchurners
GROUP BY Card_Category, Attrition_Flag
ORDER BY Card_Category;

-- =========================================================
-- 6. Churn by Income Category
-- =========================================================

SELECT
    Income_Category,
    Attrition_Flag,
    COUNT(*) AS Customer_Count
FROM bankchurners
GROUP BY Income_Category, Attrition_Flag
ORDER BY Income_Category;

-- =========================================================
-- 7. Churn by Education Level
-- =========================================================

SELECT
    Education_Level,
    Attrition_Flag,
    COUNT(*) AS Customer_Count
FROM bankchurners
GROUP BY Education_Level, Attrition_Flag
ORDER BY Education_Level;

-- =========================================================
-- 8. Average Credit Limit by Card Category
-- =========================================================

SELECT
    Card_Category,
    ROUND(AVG(Credit_Limit),2) AS Avg_Credit_Limit
FROM bankchurners
GROUP BY Card_Category
ORDER BY Avg_Credit_Limit DESC;

-- =========================================================
-- 9. Average Transaction Amount by Card Category
-- =========================================================

SELECT
    Card_Category,
    ROUND(AVG(Total_Trans_Amt),2) AS Avg_Transaction_Amount
FROM bankchurners
GROUP BY Card_Category
ORDER BY Avg_Transaction_Amount DESC;

-- =========================================================
-- 10. Average Transaction Count by Churn Status
-- =========================================================

SELECT
    Attrition_Flag,
    ROUND(AVG(Total_Trans_Ct),2) AS Avg_Transaction_Count
FROM bankchurners
GROUP BY Attrition_Flag;

-- =========================================================
-- 11. Average Credit Utilization by Churn Status
-- =========================================================

SELECT
    Attrition_Flag,
    ROUND(AVG(Avg_Utilization_Ratio),2) AS Avg_Utilization
FROM bankchurners
GROUP BY Attrition_Flag;

-- =========================================================
-- 12. Average Inactive Months by Churn Status
-- =========================================================

SELECT
    Attrition_Flag,
    ROUND(AVG(Months_Inactive_12_mon),2) AS Avg_Inactive_Months
FROM bankchurners
GROUP BY Attrition_Flag;

-- =========================================================
-- 13. Top 10 Customers by Transaction Amount
-- =========================================================

SELECT
    CLIENTNUM,
    Total_Trans_Amt
FROM bankchurners
ORDER BY Total_Trans_Amt DESC
LIMIT 10;

-- =========================================================
-- 14. Top 10 Customers by Credit Limit
-- =========================================================

SELECT
    CLIENTNUM,
    Credit_Limit
FROM bankchurners
ORDER BY Credit_Limit DESC
LIMIT 10;

-- =========================================================
-- 15. Customer Distribution by Age
-- =========================================================

SELECT
    Customer_Age,
    COUNT(*) AS Customer_Count
FROM bankchurners
GROUP BY Customer_Age
ORDER BY Customer_Age;

-- =========================================================
-- 16. Average Relationship Count
-- =========================================================

SELECT
    ROUND(AVG(Total_Relationship_Count),2) AS Avg_Relationship_Count
FROM bankchurners;

-- =========================================================
-- 17. Highest Average Credit Limit by Income Category
-- =========================================================

SELECT
    Income_Category,
    ROUND(AVG(Credit_Limit),2) AS Avg_Credit_Limit
FROM bankchurners
GROUP BY Income_Category
ORDER BY Avg_Credit_Limit DESC;

-- =========================================================
-- 18. Highest Average Transaction Amount by Income Category
-- =========================================================

SELECT
    Income_Category,
    ROUND(AVG(Total_Trans_Amt),2) AS Avg_Transaction_Amount
FROM bankchurners
GROUP BY Income_Category
ORDER BY Avg_Transaction_Amount DESC;

-- =========================================================
-- 19. KPI Summary
-- =========================================================

SELECT
    COUNT(*) AS Total_Customers,
    ROUND(AVG(Credit_Limit),2) AS Avg_Credit_Limit,
    ROUND(AVG(Total_Trans_Amt),2) AS Avg_Transaction_Amount,
    ROUND(AVG(Total_Trans_Ct),2) AS Avg_Transaction_Count,
    ROUND(AVG(Avg_Utilization_Ratio),2) AS Avg_Utilization
FROM bankchurners;

-- =========================================================
-- END OF SQL ANALYSIS
-- =========================================================


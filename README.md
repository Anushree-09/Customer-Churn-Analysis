# Customer-Churn-Analysis
End-to-end customer churn analysis project using Python and Power BI. Built a logistic regression model (78% accuracy) and developed an interactive dashboard to uncover key business insights and churn drivers.

# Project Overview

This project analyzes customer churn behavior in a telecom dataset to identify key factors driving customer attrition and provide actionable business insights.

The solution combines data preprocessing, machine learning, and interactive dashboarding to deliver a complete analytics workflow.

# Objective

* Understand why customers churn
* Identify high-risk customer segments
* Build a predictive model for churn
* Present insights through a business-friendly dashboard

# Tech Stack

* Python (Pandas, NumPy, Scikit-learn)
* Data Visualization (Matplotlib, Seaborn)
* Power BI (Dashboard & Insights)
* VS Code

# Dataset

* Telco Customer Churn Dataset (Kaggle)
* 7,000 customer records
* Includes demographics, services, billing, and churn status

# Project Workflow

## 1. Data Cleaning & Preprocessing

* Converted `TotalCharges` to numeric
* Handled missing values
* Encoded categorical variables
* Standardized features using scaling

## 2. Exploratory Data Analysis

* Analyzed customer distribution
* Identified patterns across tenure, contract type, and billing
* Observed relationships between pricing and churn

## 3. Machine Learning Model

* Model Used: Logistic Regression
* Accuracy: 78%
* Applied feature scaling for better performance

## 4. Key Features Impacting Churn

* Monthly Charges
* Total Charges
* Contract Type
* Payment Method

# Dashboard (Power BI)

The dashboard provides interactive insights into churn behavior.

Open the .pbix file in Power BI Desktop to explore the dashboard.

# Key Visuals:

* KPI: Overall Churn Rate (27%)
* Churn by Contract Type
* Churn by Payment Method
* Churn by Customer Tenure
* Filter: Internet Service

# Key Insights

* Customers on **month-to-month contracts** have the highest churn
* Higher **monthly charges** are linked to increased churn
* Customers using **electronic check** show higher churn rates
* **New customers (low tenure)** are more likely to leave

# Business Recommendations

* Encourage long-term contracts with incentives
* Improve onboarding experience for new customers
* Optimize pricing strategies
* Enhance digital payment experience

# Conclusion

This project demonstrates how data can be used to:

* Predict customer behavior
* Generate actionable insights
* Support business decision-making

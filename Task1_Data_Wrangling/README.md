# Task 1 – Data Immersion & Wrangling

## Data Analytics Internship – ApexPlanet Software Pvt. Ltd.

This project is part of my **60-Day Data Analytics Internship**.
The objective of this task is to explore a dataset, identify data quality issues, and clean the dataset so it becomes ready for analysis.

---

## Objective

* Understand the dataset structure
* Identify missing values and duplicate records
* Clean and transform the dataset using Python
* Create useful features for analysis

---

## Tools Used

* Python
* Pandas
* Visual Studio Code

---

## Dataset Description

The dataset contains **sales transaction data** including customer purchases.

| Column Name   | Description               |
| ------------- | ------------------------- |
| Order_ID      | Unique order identifier   |
| Customer_Name | Name of the customer      |
| Product       | Product purchased         |
| Category      | Product category          |
| Quantity      | Number of items purchased |
| Price         | Price of each item        |
| Order_Date    | Date of purchase          |
| City          | Customer city             |

---

## Data Quality Issues Found

During exploration, the following issues were found:

* Missing values in **Customer_Name**
* Missing values in **City**
* Duplicate records in the dataset
* No column for total revenue

---

## Data Cleaning Steps

The following operations were performed:

1. Loaded the dataset using Pandas
2. Checked missing values
3. Removed duplicate rows
4. Filled missing values with **"Unknown"**
5. Converted date format
6. Created a new column **Revenue = Quantity × Price**

---

## Project Structure

Task1_Data_Wrangling
│
├── sales_data.csv
├── data_cleaning.py
├── cleaned_sales_data.csv
└── README.md

---

## Output

After cleaning the data:

* Missing values were handled
* Duplicate rows were removed
* Date format was standardized
* Revenue column was created

The dataset is now ready for further analysis.

---

## Learning Outcomes

* Data exploration techniques
* Handling missing values
* Removing duplicate data
* Feature engineering
* Using Pandas for data cleaning

---

## Author

Sreejisha M Gupta
Data Analytics Intern

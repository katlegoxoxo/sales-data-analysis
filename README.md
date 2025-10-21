#  Sales Data Analysis — Excel & Python (Pandas)

## 📊 Project Overview
This project explores **data collection, management, cleaning, and analysis** using a real-world sales dataset (`Week-2-Sales-Data.csv`).  
The objective was to extract meaningful business insights through both **Microsoft Excel** and **Python (pandas)**, demonstrating the end-to-end data analysis process from raw data handling to insight generation.

---

##  Part A: Working with Data in Excel

### 1️Import and Explore
- Imported the `Week-2-Sales-Data.csv` file into Excel.  
- The dataset is **structured data** — organized into rows and columns with clearly defined data types such as text (Product Name, Region), numbers (Units Sold, Revenue), and dates (Order Date).  
- **Column Overview:**
  - **Order ID:** Unique identifier for each transaction  
  - **Product:** Item sold  
  - **Region:** Location of the sale  
  - **Sales Representative:** Employee responsible for the sale  
  - **Units Sold:** Quantity of product sold  
  - **Unit Price:** Price per unit  
  - **Order Date:** Date the order was placed  
  - **Revenue:** Total income generated (`Units Sold × Unit Price`)  

### 2️⃣ Summarize Sales Insights
Using **Excel tools** like PivotTables, SUMIF, and Charts, the following insights were derived:  
- **Total Revenue by Product:** Identified best- and lowest-performing products  
- **Total Revenue by Region:** Compared revenue performance across regions  
- **Top 3 Best-Selling Products:** Ranked products by total revenue  
- **Monthly Revenue Trend:** Analyzed revenue changes month-to-month  
- **Revenue by Region Chart:** Visualized regional performance using a column chart  

---

##  Part B: Data Cleaning and Analysis in Python

### 3️⃣ Import and Clean the Data
Using **pandas** in a Jupyter Notebook:  
- Imported the dataset and inspected for **missing values, duplicates, and incorrect data types**  
- Cleaned the data by:
  - Removing duplicate records  
  - Handling missing values (drop or fill as appropriate)  
  - Converting the `Order_Date` column to **datetime format**  

### 4️⃣ Calculate Key Performance Indicators (KPIs)
Performed analytical calculations in Python to derive key metrics:  
-  **Total Revenue:** Overall revenue for the dataset  
-  **Average Units Sold per Order:** Mean units sold per transaction  
-  **Total Revenue per Region:** Summarized revenue by region  
-  **Highest Revenue-Generating Sales Representative:** Top-performing salesperson  
-  **Top 3 Products by Units Sold:** Most frequently sold products  

---

## 🧾 Tools & Technologies
- **Microsoft Excel:** Data exploration, summarization, and visualization  
- **Python (pandas):** Data cleaning, transformation, and analysis  
- **Jupyter Notebook:** Interactive environment for running and documenting code

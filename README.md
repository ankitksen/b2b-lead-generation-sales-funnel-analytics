# B2B Lead Generation & Sales Funnel Analytics

## 📌 Project Overview

This project analyzes a B2B lead generation and sales funnel dataset to understand how leads move through different stages of the sales process, identify conversion bottlenecks, evaluate revenue performance, and uncover opportunities for sales improvement.

The project combines Python, BigQuery SQL, Power BI, and DAX to create an end-to-end data analytics solution.

---

## 🎯 Business Objective

The main objectives of this project are to:

- Analyze the complete B2B sales funnel
- Measure conversion rates between funnel stages
- Identify sales funnel bottlenecks
- Analyze revenue performance
- Compare lead sources and regions
- Evaluate industry and product performance
- Analyze sales representative performance
- Understand monthly sales trends
- Analyze customer engagement
- Identify high-value leads
- Identify high-engagement leads that were not won
- Estimate potential revenue opportunities

---

## 🛠️ Tech Stack

- Python
- Pandas
- BigQuery SQL
- Google BigQuery Sandbox
- Power BI
- DAX
- Git
- GitHub

---

## 📊 Dataset

The dataset contains **10,000 B2B leads** and includes the following fields:

- Lead_ID
- Lead_Date
- MQL_Date
- SQL_Date
- Opportunity_Date
- Won_Date
- Deal_Value
- Company_Name
- Industry
- Company_Size
- Region
- Lead_Source
- Sales_Rep
- Product_Interest
- Engagement_Score
- Lead_Status
- Sales_Cycle_Days

---

## 🔄 Sales Funnel

The project analyzes the following funnel:

**Lead → MQL → SQL → Opportunity → Won**

### Funnel Performance

| Funnel Stage | Count | Conversion Rate |
|---|---:|---:|
| Leads | 10,000 | — |
| MQLs | 6,526 | 65.26% |
| SQLs | 4,288 | 65.71% |
| Opportunities | 2,342 | 54.62% |
| Won Deals | 1,380 | 58.92% |

Overall Lead → Won conversion rate: **13.80%**

---

## 💰 Revenue Performance

- Total Revenue: **736,911,729**
- Average Deal Value: **533,994.01**
- Median Deal Value: **534,227.50**
- Maximum Deal Value: **997,905**
- Minimum Deal Value: **59,901**
- Average Sales Cycle for Won Deals: **36.45 days**

---

## 🔎 Key Analysis Areas

### Lead Analysis

- Lead source performance
- Industry distribution
- Company size distribution
- Regional performance
- Lead status distribution

### Sales Funnel Analysis

- Lead → MQL conversion
- MQL → SQL conversion
- SQL → Opportunity conversion
- Opportunity → Won conversion
- Overall Lead → Won conversion

### Revenue Analysis

- Revenue by region
- Revenue by lead source
- Revenue by industry
- Revenue by product
- Revenue by sales representative

### Sales Performance

- Sales representative performance
- Product performance
- Monthly performance
- Region + industry performance

### Engagement Analysis

- Engagement score analysis
- High-engagement leads
- High-value leads
- Unwon high-engagement opportunities

---

## 🚨 Revenue Opportunity Analysis

The analysis identified:

- High-Value Leads (Deal Value ≥ 500K): **1,261**
- High-Value Won Deals: **751**
- High-Value Revenue: **562,408,366**
- High-Engagement Unwon Leads: **2,531**
- Potential Unwon Value: **154,839,902**

These results help identify potential revenue recovery and sales follow-up opportunities.

---

## 🐍 Python Analysis

Python and Pandas were used for:

- Dataset validation
- Data type checking
- Date conversion
- Missing value analysis
- Duplicate Lead ID checking
- Funnel conversion analysis
- Revenue analysis
- Regional analysis
- Industry analysis
- Sales representative analysis
- Product analysis
- Monthly analysis
- Engagement analysis
- Revenue opportunity analysis

The Python analysis exports processed results into CSV files inside the `outputs/` directory.

---

## ☁️ BigQuery SQL Analysis

Google BigQuery Sandbox was used to analyze the dataset using SQL.

A total of **25 SQL queries** were created and executed successfully.

The SQL analysis covers:

- Funnel performance
- Conversion rates
- Revenue analysis
- Lead source analysis
- Regional analysis
- Industry analysis
- Sales representative analysis
- Product performance
- Monthly performance
- Engagement analysis
- Revenue opportunities

---

## 📈 Power BI Dashboard

Power BI is used to transform the analysis into an interactive business intelligence dashboard.

The dashboard will include:

- Executive Overview
- Sales Funnel Analysis
- Revenue & Performance Analysis
- Lead Source & Regional Analysis
- Sales Representative & Product Analysis
- Revenue Opportunity Analysis

DAX measures will be used to calculate KPIs, conversion rates, revenue metrics, and other business performance indicators.

---

## 📁 Project Structure

```text
B2B Lead Generation & Sales Funnel Analytics/
│
├── data/
│   └── leads.csv
│
├── outputs/
│   ├── engagement_performance.csv
│   ├── monthly_performance.csv
│   ├── product_performance.csv
│   ├── region_industry_performance.csv
│   ├── region_revenue.csv
│   ├── sales_rep_performance.csv
│   └── source_revenue.csv
│
├── .gitignore
├── analysis.py
├── generate_data.py
├── requirements.txt
└── README.md
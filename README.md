# B2B Lead Generation & Sales Funnel Analytics

An end-to-end B2B sales funnel and revenue analytics project built using Python, BigQuery SQL, Power BI, and DAX.

The project analyzes 10,000 B2B leads to understand funnel progression, conversion performance, revenue generation, sales efficiency, customer engagement, and potential revenue opportunities.

---

## 📌 Project Overview

B2B organizations generate a large volume of leads, but not every lead progresses through the sales funnel and becomes a customer.

This project analyzes the complete sales journey:

**Lead → MQL → SQL → Opportunity → Won**

The analysis focuses on identifying:

- Where leads are being lost
- Which funnel stages have the largest drop-offs
- Which lead sources generate stronger results
- Which regions and industries perform better
- How revenue is distributed across different dimensions
- Which sales representatives perform better
- Which products generate higher revenue
- How engagement relates to deal value
- Where potential revenue opportunities exist

The project combines Python-based exploratory analysis, BigQuery SQL analysis, and an interactive Power BI dashboard to create an end-to-end business analytics solution.

---

## 🎯 Business Objectives

The key objectives of this project are to:

- Analyze the complete B2B sales funnel
- Measure conversion rates between funnel stages
- Identify funnel bottlenecks and drop-offs
- Analyze overall revenue performance
- Compare lead source performance
- Evaluate regional and industry performance
- Analyze product performance
- Evaluate sales representative performance
- Understand monthly lead and revenue trends
- Analyze customer engagement
- Identify high-value leads and opportunities
- Identify high-engagement leads that were not won
- Estimate potential revenue opportunities
- Provide actionable business recommendations

---

## 🛠️ Tech Stack

### Data Analysis
- Python
- Pandas
- NumPy

### SQL
- Google BigQuery
- BigQuery Sandbox

### Business Intelligence
- Microsoft Power BI
- DAX

### Version Control & Portfolio
- GitHub

---

## 📊 Dataset

The project uses a synthetic B2B lead generation dataset containing **10,000 leads**.

### Key Fields

| Field | Description |
|---|---|
| Lead_ID | Unique lead identifier |
| Lead_Date | Date when the lead was generated |
| MQL_Date | Date when the lead became an MQL |
| SQL_Date | Date when the lead became an SQL |
| Opportunity_Date | Date when the lead became an opportunity |
| Won_Date | Date when the deal was won |
| Deal_Value | Deal value associated with the lead |
| Company_Name | Company associated with the lead |
| Industry | Industry of the company |
| Company_Size | Company size category |
| Region | Geographic region |
| Lead_Source | Source through which the lead was generated |
| Sales_Rep | Assigned sales representative |
| Product_Interest | Product/service of interest |
| Engagement_Score | Lead engagement score |
| Lead_Status | Current funnel status |
| Sales_Cycle_Days | Sales cycle duration |

---

## 🔄 Sales Funnel

The project evaluates the following funnel:

**Lead → MQL → SQL → Opportunity → Won**

### Funnel Performance

| Funnel Stage | Count | Conversion Rate |
|---|---:|---:|
| Leads | 10,000 | — |
| MQLs | 6,526 | 65.26% |
| SQLs | 4,288 | 65.71% |
| Opportunities | 2,342 | 54.62% |
| Won Deals | 1,380 | 58.92% |

### Overall Lead → Won Conversion

**13.80%**

This indicates that approximately 14 out of every 100 generated leads ultimately become won deals.

---

## 💰 Revenue Performance

Key revenue metrics from the analysis include:

| Metric | Value |
|---|---:|
| Total Revenue | $736.91M |
| Average Deal Value | ~$533.99K |
| Median Deal Value | ~$534.23K |
| Maximum Deal Value | ~$997.91K |
| Minimum Deal Value | ~$59.90K |
| Average Sales Cycle | ~36 days |

The revenue analysis helps understand how deal value varies across lead sources, regions, industries, products, and sales representatives.

---

## 🔎 Key Analysis Areas

### 1. Lead Analysis

The project evaluates:

- Lead source distribution
- Industry distribution
- Company size
- Regional distribution
- Lead status
- Engagement score

---

### 2. Sales Funnel Analysis

The funnel analysis measures:

- Lead → MQL conversion
- MQL → SQL conversion
- SQL → Opportunity conversion
- Opportunity → Won conversion
- Overall Lead → Won conversion
- Funnel drop-off at each stage

This helps identify where the sales pipeline is losing the highest number of leads.

---

### 3. Revenue Analysis

Revenue is analyzed across:

- Lead Source
- Region
- Industry
- Product Interest
- Sales Representative
- Month

This provides a multidimensional view of revenue performance.

---

### 4. Sales Performance

Sales representative performance is evaluated using:

- Won Deals
- Revenue
- Win Rate
- Deal Value
- Sales Cycle

This helps identify high-performing representatives and potential areas for improvement.

---

### 5. Product Performance

Product analysis evaluates:

- Revenue by product
- Won deals by product
- Funnel performance by product
- Product-level sales contribution

---

### 6. Engagement Analysis

Engagement analysis examines:

- Engagement score
- Deal value
- Lead status
- High-engagement leads
- High-value leads
- High-engagement leads that were not won

This helps identify leads that may require additional sales attention.

---

# 🚨 Revenue Opportunity Analysis

The project also focuses on identifying potential revenue recovery opportunities.

### High-Value Lead Analysis

**High-Value Lead:** Deal Value ≥ $500K

- High-Value Leads: **1,261**
- High-Value Won Deals: **751**
- High-Value Revenue: **$562.41M**

The analysis highlights a significant concentration of revenue among high-value opportunities.

### High-Engagement Unwon Leads

The project also identifies leads with strong engagement signals that have not yet converted into won deals.

These leads represent potential follow-up opportunities for the sales team.

The Power BI dashboard provides an interactive view of:

- Potential Unwon Revenue
- High-Value Leads
- High-Value Won Deals
- Total Opportunities
- Won Deals
- Win Rate
- Priority Opportunities

---

# 🐍 Python Analysis

Python and Pandas were used for data preparation, validation, analysis, and output generation.

### Python Analysis Includes

- Dataset validation
- Data type validation
- Date conversion
- Missing value analysis
- Duplicate Lead ID checking
- Funnel stage analysis
- Conversion rate analysis
- Revenue analysis
- Regional analysis
- Industry analysis
- Lead source analysis
- Sales representative analysis
- Product analysis
- Monthly trend analysis
- Engagement analysis
- High-value lead analysis
- Revenue opportunity analysis

The processed analytical outputs are exported as CSV files into the `outputs/` directory.

---

# ☁️ BigQuery SQL Analysis

Google BigQuery Sandbox was used to perform SQL-based business analysis on the lead dataset.

A total of **25 SQL queries** were created and executed.

### SQL Analysis Covers

- Total leads
- Funnel stage counts
- Funnel conversion rates
- Funnel drop-off
- Revenue metrics
- Average and median deal value
- Lead source performance
- Regional performance
- Industry performance
- Product performance
- Sales representative performance
- Monthly performance
- Engagement analysis
- High-value opportunities
- Revenue opportunity analysis

BigQuery was used to demonstrate SQL-based analytical skills on a cloud data warehouse environment.

---

# 📈 Power BI Dashboard

The final Power BI dashboard converts the analytical findings into an interactive business intelligence solution.

The dashboard contains **5 pages**.

---

## 1. Executive Overview

Provides a high-level summary of the complete B2B sales funnel.

### KPIs

- Total Leads
- Total MQLs
- Total SQLs
- Total Opportunities
- Total Won Deals
- Total Revenue
- Lead to Won %
- Average Sales Cycle

### Visuals

- Sales Funnel Conversion
- Lead Source Performance
- Revenue by Lead Source
- Monthly Lead Trend

---

## 2. Sales Funnel Analysis

Focuses on funnel progression and stage-level performance.

### KPIs

- Total Leads
- Total MQLs
- Total SQLs
- Total Opportunities
- Total Won Deals
- Lead to Won %

### Visuals

- Sales Funnel Conversion
- Conversion Rate by Stage
- Funnel Drop-off Analysis
- Monthly Funnel Performance

---

## 3. Revenue & Performance

Focuses on revenue trends and commercial performance.

### KPIs

- Total Revenue
- Average Deal Value
- Median Deal Value
- Potential Unwon Revenue
- Win Rate
- Average Sales Cycle

### Visuals

- Monthly Revenue Trend
- Revenue by Lead Source
- Revenue by Industry
- Revenue by Region
- Sales Cycle vs Deal Value

---

## 4. Sales & Product Performance

Focuses on sales representative, product, and engagement performance.

### KPIs

- Total Won Deals
- Win Rate
- High-Value Won Deals
- High-Value Leads
- Average Deal Value
- Average Sales Cycle

### Visuals

- Revenue by Product Interest
- Won Deals by Sales Representative
- Win Rate by Sales Representative
- Product Funnel Performance
- Engagement vs Deal Value

---

## 5. Revenue Opportunity & Action Center

Focuses on identifying high-value opportunities and potential revenue recovery areas.

### KPIs

- Potential Unwon Revenue
- High-Value Leads
- High-Value Won Deals
- Total Opportunities
- Total Won Deals
- Win Rate

### Visuals

- Potential Unwon Revenue by Industry
- Unwon Revenue by Lead Source
- High-Value Leads by Region
- Deal Value by Lead Status
- Priority Opportunities Table

The Priority Opportunities table provides detailed lead-level information for sales follow-up.

---

# 📐 DAX

DAX measures were used in Power BI to calculate business KPIs and funnel metrics.

Examples include:

- Total Leads
- Total MQLs
- Total SQLs
- Total Opportunities
- Total Won Deals
- Total Revenue
- Lead to Won %
- Win Rate
- Average Deal Value
- Median Deal Value
- Average Sales Cycle
- High-Value Leads
- High-Value Won Deals
- Potential Unwon Revenue

DAX measures allow the dashboard KPIs and visualizations to respond dynamically to slicer selections.

---

# 🎛️ Dashboard Filters

Interactive slicers are available across the dashboard to allow users to analyze performance by:

- Lead Source
- Region
- Industry

These filters allow business users to drill into specific segments and understand performance differences.

---

# 💡 Business Insights

The analysis provides several important business perspectives:

### Funnel Efficiency

The overall Lead → Won conversion rate is **13.80%**, highlighting that a significant proportion of generated leads do not reach the final stage.

### Funnel Bottlenecks

The stage-level conversion analysis helps identify where the largest proportional and absolute losses occur in the sales pipeline.

### Revenue Concentration

A large portion of revenue comes from high-value deals, making high-value opportunity management important for revenue growth.

### Lead Source Performance

Lead sources can be compared based on lead volume, revenue contribution, and funnel performance rather than evaluating them only on lead quantity.

### Regional Performance

Revenue and high-value lead analysis can identify stronger and weaker geographic markets.

### Sales Performance

Sales representative analysis allows management to compare sales outcomes and identify performance differences across the team.

### Engagement Opportunities

High-engagement but currently unwon leads represent a potential follow-up segment for sales teams.

---

# 🎯 Business Recommendations

Based on the analysis, the following actions can be considered:

1. **Focus on funnel bottlenecks**  
   Investigate stages with significant lead drop-offs and identify the underlying reasons.

2. **Prioritize high-value opportunities**  
   Give additional attention to leads and opportunities with high potential deal values.

3. **Follow up with high-engagement unwon leads**  
   Create targeted sales follow-up campaigns for engaged prospects that have not yet converted.

4. **Optimize lead source allocation**  
   Compare lead sources based on conversion and revenue contribution instead of lead volume alone.

5. **Analyze regional performance**  
   Identify high-performing regions and investigate opportunities in weaker markets.

6. **Improve sales cycle efficiency**  
   Monitor sales cycle duration and identify opportunities to reduce delays between funnel stages.

7. **Use product-level insights**  
   Focus sales and marketing efforts on products with stronger revenue and funnel performance.

---

# 📁 Project Structure

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
├── README.md
│
├── B2B Lead Generation & Sales Funnel Analytics.pbix
└── B2B Lead Generation & Sales Funnel Analytics.pdf

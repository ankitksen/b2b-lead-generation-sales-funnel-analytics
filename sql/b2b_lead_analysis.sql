-- ============================================================
-- B2B Lead Generation & Sales Funnel Analytics
-- BigQuery SQL Analysis
-- Project: b2b-lead-generation-analytics
-- Total Queries: 25
-- ============================================================


-- ============================================================
-- Query 01: Test Leads Table
-- ============================================================

SELECT *
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
LIMIT 10;


-- ============================================================
-- Query 02: Total Leads
-- ============================================================

SELECT COUNT(*) AS total_leads
FROM `b2b-lead-generation-analytics.lead_analytics.leads`;


-- ============================================================
-- Query 03: Total MQLs
-- ============================================================

SELECT COUNT(*) AS total_mqls
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
WHERE MQL_Date IS NOT NULL;


-- ============================================================
-- Query 04: Total SQLs
-- ============================================================

SELECT COUNT(*) AS total_sqls
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
WHERE SQL_Date IS NOT NULL;


-- ============================================================
-- Query 05: Total Opportunities
-- ============================================================

SELECT COUNT(*) AS total_opportunities
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
WHERE Opportunity_Date IS NOT NULL;


-- ============================================================
-- Query 06: Total Won Deals
-- ============================================================

SELECT COUNT(*) AS total_won_deals
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
WHERE Won_Date IS NOT NULL;


-- ============================================================
-- Query 07: Total Revenue
-- ============================================================

SELECT SUM(Deal_Value) AS total_revenue
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
WHERE Won_Date IS NOT NULL;


-- ============================================================
-- Query 08: Average Deal Value
-- ============================================================

SELECT AVG(Deal_Value) AS average_deal_value
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
WHERE Won_Date IS NOT NULL
  AND Deal_Value > 0;


-- ============================================================
-- Query 09: Average Sales Cycle
-- ============================================================

SELECT AVG(Sales_Cycle_Days) AS average_sales_cycle_days
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
WHERE Won_Date IS NOT NULL
  AND Sales_Cycle_Days IS NOT NULL;


-- ============================================================
-- Query 10: Lead Source Performance
-- ============================================================

SELECT
  Lead_Source,
  COUNT(*) AS total_leads,
  COUNTIF(MQL_Date IS NOT NULL) AS mqls,
  COUNTIF(SQL_Date IS NOT NULL) AS sqls,
  COUNTIF(Opportunity_Date IS NOT NULL) AS opportunities,
  COUNTIF(Won_Date IS NOT NULL) AS won_deals,
  SUM(CASE WHEN Won_Date IS NOT NULL THEN Deal_Value ELSE 0 END) AS revenue
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY Lead_Source
ORDER BY revenue DESC;


-- ============================================================
-- Query 11: Funnel Conversion Analysis
-- ============================================================

SELECT
  COUNT(*) AS total_leads,

  COUNTIF(MQL_Date IS NOT NULL) AS total_mqls,

  COUNTIF(SQL_Date IS NOT NULL) AS total_sqls,

  COUNTIF(Opportunity_Date IS NOT NULL) AS total_opportunities,

  COUNTIF(Won_Date IS NOT NULL) AS total_won_deals,

  ROUND(
    COUNTIF(MQL_Date IS NOT NULL) * 100.0 / COUNT(*), 2
  ) AS lead_to_mql_pct,

  ROUND(
    COUNTIF(SQL_Date IS NOT NULL) * 100.0 /
    COUNTIF(MQL_Date IS NOT NULL), 2
  ) AS mql_to_sql_pct,

  ROUND(
    COUNTIF(Opportunity_Date IS NOT NULL) * 100.0 /
    COUNTIF(SQL_Date IS NOT NULL), 2
  ) AS sql_to_opportunity_pct,

  ROUND(
    COUNTIF(Won_Date IS NOT NULL) * 100.0 /
    COUNTIF(Opportunity_Date IS NOT NULL), 2
  ) AS opportunity_to_won_pct,

  ROUND(
    COUNTIF(Won_Date IS NOT NULL) * 100.0 / COUNT(*), 2
  ) AS overall_conversion_pct

FROM `b2b-lead-generation-analytics.lead_analytics.leads`;


-- ============================================================
-- Query 12: Regional Performance
-- ============================================================

SELECT
  Region,
  COUNT(*) AS total_leads,
  COUNTIF(MQL_Date IS NOT NULL) AS mqls,
  COUNTIF(SQL_Date IS NOT NULL) AS sqls,
  COUNTIF(Opportunity_Date IS NOT NULL) AS opportunities,
  COUNTIF(Won_Date IS NOT NULL) AS won_deals,
  SUM(CASE WHEN Won_Date IS NOT NULL THEN Deal_Value ELSE 0 END) AS revenue
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY Region
ORDER BY revenue DESC;


-- ============================================================
-- Query 13: Company Size Performance
-- ============================================================

SELECT
  Company_Size,
  COUNT(*) AS total_leads,
  COUNTIF(MQL_Date IS NOT NULL) AS mqls,
  COUNTIF(SQL_Date IS NOT NULL) AS sqls,
  COUNTIF(Opportunity_Date IS NOT NULL) AS opportunities,
  COUNTIF(Won_Date IS NOT NULL) AS won_deals,
  SUM(CASE WHEN Won_Date IS NOT NULL THEN Deal_Value ELSE 0 END) AS revenue
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY Company_Size
ORDER BY revenue DESC;


-- ============================================================
-- Query 14: Industry Performance
-- ============================================================

SELECT
  Industry,
  COUNT(*) AS total_leads,
  COUNTIF(MQL_Date IS NOT NULL) AS mqls,
  COUNTIF(SQL_Date IS NOT NULL) AS sqls,
  COUNTIF(Opportunity_Date IS NOT NULL) AS opportunities,
  COUNTIF(Won_Date IS NOT NULL) AS won_deals,
  SUM(CASE WHEN Won_Date IS NOT NULL THEN Deal_Value ELSE 0 END) AS revenue
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY Industry
ORDER BY revenue DESC;


-- ============================================================
-- Query 15: Sales Representative Performance
-- ============================================================

SELECT
  Sales_Rep,
  COUNT(*) AS total_leads,
  COUNTIF(MQL_Date IS NOT NULL) AS mqls,
  COUNTIF(SQL_Date IS NOT NULL) AS sqls,
  COUNTIF(Opportunity_Date IS NOT NULL) AS opportunities,
  COUNTIF(Won_Date IS NOT NULL) AS won_deals,
  SUM(CASE WHEN Won_Date IS NOT NULL THEN Deal_Value ELSE 0 END) AS revenue
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY Sales_Rep
ORDER BY revenue DESC;


-- ============================================================
-- Query 16: Product Interest Performance
-- ============================================================

SELECT
  Product_Interest,
  COUNT(*) AS total_leads,
  COUNTIF(MQL_Date IS NOT NULL) AS mqls,
  COUNTIF(SQL_Date IS NOT NULL) AS sqls,
  COUNTIF(Opportunity_Date IS NOT NULL) AS opportunities,
  COUNTIF(Won_Date IS NOT NULL) AS won_deals,
  SUM(CASE WHEN Won_Date IS NOT NULL THEN Deal_Value ELSE 0 END) AS revenue
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY Product_Interest
ORDER BY revenue DESC;


-- ============================================================
-- Query 17: Lead Status Distribution
-- ============================================================

SELECT
  Lead_Status,
  COUNT(*) AS total_leads
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY Lead_Status
ORDER BY total_leads DESC;


-- ============================================================
-- Query 18: Monthly Lead Trend
-- ============================================================

SELECT
  FORMAT_DATE('%Y-%m', Lead_Date) AS lead_month,
  COUNT(*) AS total_leads
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY lead_month
ORDER BY lead_month;


-- ============================================================
-- Query 19: Monthly MQL Trend
-- ============================================================

SELECT
  FORMAT_DATE('%Y-%m', MQL_Date) AS mql_month,
  COUNT(*) AS total_mqls
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
WHERE MQL_Date IS NOT NULL
GROUP BY mql_month
ORDER BY mql_month;


-- ============================================================
-- Query 20: Monthly Won Revenue
-- ============================================================

SELECT
  FORMAT_DATE('%Y-%m', Won_Date) AS won_month,
  COUNT(*) AS won_deals,
  SUM(Deal_Value) AS revenue
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
WHERE Won_Date IS NOT NULL
GROUP BY won_month
ORDER BY won_month;


-- ============================================================
-- Query 21: Lead Source Conversion Rate
-- ============================================================

SELECT
  Lead_Source,
  COUNT(*) AS total_leads,
  COUNTIF(Won_Date IS NOT NULL) AS won_deals,
  ROUND(COUNTIF(Won_Date IS NOT NULL) * 100.0 / COUNT(*), 2) AS lead_to_won_pct
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY Lead_Source
ORDER BY lead_to_won_pct DESC;


-- ============================================================
-- Query 22: Sales Representative Conversion Rate
-- ============================================================

SELECT
  Sales_Rep,
  COUNT(*) AS total_leads,
  COUNTIF(Won_Date IS NOT NULL) AS won_deals,
  ROUND(COUNTIF(Won_Date IS NOT NULL) * 100.0 / COUNT(*), 2) AS lead_to_won_pct
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY Sales_Rep
ORDER BY lead_to_won_pct DESC;


-- ============================================================
-- Query 23: Engagement Score Performance
-- ============================================================

SELECT
  CASE
    WHEN Engagement_Score < 25 THEN 'Low'
    WHEN Engagement_Score < 50 THEN 'Medium'
    WHEN Engagement_Score < 75 THEN 'High'
    ELSE 'Very High'
  END AS engagement_level,
  COUNT(*) AS total_leads,
  COUNTIF(MQL_Date IS NOT NULL) AS mqls,
  COUNTIF(Won_Date IS NOT NULL) AS won_deals,
  ROUND(COUNTIF(Won_Date IS NOT NULL) * 100.0 / COUNT(*), 2) AS lead_to_won_pct
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
GROUP BY engagement_level
ORDER BY lead_to_won_pct DESC;


-- ============================================================
-- Query 24: Sales Cycle by Lead Source
-- ============================================================

SELECT
  Lead_Source,
  COUNTIF(Sales_Cycle_Days IS NOT NULL) AS completed_deals,
  ROUND(AVG(Sales_Cycle_Days), 2) AS average_sales_cycle_days
FROM `b2b-lead-generation-analytics.lead_analytics.leads`
WHERE Sales_Cycle_Days IS NOT NULL
GROUP BY Lead_Source
ORDER BY average_sales_cycle_days;


-- ============================================================
-- Query 25: Executive KPI Summary
-- ============================================================

SELECT
  COUNT(*) AS total_leads,
  COUNTIF(MQL_Date IS NOT NULL) AS total_mqls,
  COUNTIF(SQL_Date IS NOT NULL) AS total_sqls,
  COUNTIF(Opportunity_Date IS NOT NULL) AS total_opportunities,
  COUNTIF(Won_Date IS NOT NULL) AS total_won_deals,
  SUM(CASE WHEN Won_Date IS NOT NULL THEN Deal_Value ELSE 0 END) AS total_revenue,
  ROUND(AVG(CASE WHEN Won_Date IS NOT NULL AND Deal_Value > 0 THEN Deal_Value END), 2) AS average_deal_value,
  ROUND(AVG(CASE WHEN Won_Date IS NOT NULL THEN Sales_Cycle_Days END), 2) AS average_sales_cycle_days
FROM `b2b-lead-generation-analytics.lead_analytics.leads`;


-- ============================================================
-- END OF SQL ANALYSIS
-- ============================================================

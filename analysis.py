import pandas as pd

df = pd.read_csv("data/leads.csv")

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("\nData Types:")
print(df.dtypes)
date_columns = [
    "Lead_Date",
    "MQL_Date",
    "SQL_Date",
    "Opportunity_Date",
    "Won_Date"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

print("\nDate columns converted successfully!")
print(df[date_columns].dtypes)
print("\nMissing Values:")
print(df.isna().sum())
print("\nStatistical Summary:")
print(df.describe())
print("\nDuplicate Lead IDs:")
print(df["Lead_ID"].duplicated().sum())

print("\nLead Status Distribution:")
print(df["Lead_Status"].value_counts())
print("\nLead Source Distribution:")
print(df["Lead_Source"].value_counts())
print("\nIndustry Distribution:")
print(df["Industry"].value_counts())
print("\nCompany Size Distribution:")
print(df["Company_Size"].value_counts())
print("\nRegion Distribution:")
print(df["Region"].value_counts())

print("\nSales Representative Distribution:")
print(df["Sales_Rep"].value_counts())

print("\nProduct Interest Distribution:")
print(df["Product_Interest"].value_counts())

print("\nEngagement Score Summary:")
print(df["Engagement_Score"].describe())

print("\nLead Date Range:")
print("Minimum:", df["Lead_Date"].min())
print("Maximum:", df["Lead_Date"].max())

print("\nWon Deals Check:")
print("Won Deals:", df["Won_Date"].notna().sum())
print("Won Deal Value:", df.loc[df["Won_Date"].notna(), "Deal_Value"].sum())

print("\nSales Cycle Check:")
print("Completed Sales Cycles:", df["Sales_Cycle_Days"].notna().sum())
print("Average Sales Cycle:", df["Sales_Cycle_Days"].mean())

print("\n=== Overall Funnel Conversion Analysis ===")

total_leads = len(df)
total_mqls = df["MQL_Date"].notna().sum()
total_sqls = df["SQL_Date"].notna().sum()
total_opportunities = df["Opportunity_Date"].notna().sum()
total_won = df["Won_Date"].notna().sum()

print("Total Leads:", total_leads)
print("Total MQLs:", total_mqls)
print("Total SQLs:", total_sqls)
print("Total Opportunities:", total_opportunities)
print("Total Won Deals:", total_won)

print("\nConversion Rates:")

lead_to_mql = total_mqls / total_leads * 100
mql_to_sql = total_sqls / total_mqls * 100
sql_to_opportunity = total_opportunities / total_sqls * 100
opportunity_to_won = total_won / total_opportunities * 100
lead_to_won = total_won / total_leads * 100

print(f"Lead → MQL: {lead_to_mql:.2f}%")
print(f"MQL → SQL: {mql_to_sql:.2f}%")
print(f"SQL → Opportunity: {sql_to_opportunity:.2f}%")
print(f"Opportunity → Won: {opportunity_to_won:.2f}%")

print(f"Overall Lead → Won: {lead_to_won:.2f}%")
print("\n=== Revenue & Deal Analysis ===")

won_deals = df[df["Won_Date"].notna()]

total_revenue = won_deals["Deal_Value"].sum()
average_deal_value = won_deals["Deal_Value"].mean()
median_deal_value = won_deals["Deal_Value"].median()
maximum_deal_value = won_deals["Deal_Value"].max()
minimum_deal_value = won_deals["Deal_Value"].min()

print(f"Total Revenue: {total_revenue:,.0f}")
print(f"Average Deal Value: {average_deal_value:,.2f}")
print(f"Median Deal Value: {median_deal_value:,.2f}")
print(f"Maximum Deal Value: {maximum_deal_value:,.0f}")
print(f"Minimum Deal Value: {minimum_deal_value:,.0f}")

print("\n=== Revenue by Lead Source ===")

revenue_by_source = (
    won_deals.groupby("Lead_Source")["Deal_Value"]
    .agg(["count", "sum", "mean"])
    .sort_values("sum", ascending=False)
)

print(revenue_by_source)


print("\n=== Revenue by Region ===")

revenue_by_region = (
    won_deals.groupby("Region")["Deal_Value"]
    .agg(["count", "sum", "mean"])
    .sort_values("sum", ascending=False)
)

print(revenue_by_region)


print("\n=== Revenue by Industry ===")

revenue_by_industry = (
    won_deals.groupby("Industry")["Deal_Value"]
    .agg(["count", "sum", "mean"])
    .sort_values("sum", ascending=False)
)

print(revenue_by_industry)


print("\n=== Revenue by Company Size ===")

revenue_by_company_size = (
    won_deals.groupby("Company_Size")["Deal_Value"]
    .agg(["count", "sum", "mean"])
    .sort_values("sum", ascending=False)
)

print(revenue_by_company_size)


print("\n=== Won Rate by Lead Source ===")

source_performance = (
    df.groupby("Lead_Source")
    .agg(
        total_leads=("Lead_ID", "count"),
        won_deals=("Won_Date", lambda x: x.notna().sum())
    )
)

source_performance["won_rate_pct"] = (
    source_performance["won_deals"]
    / source_performance["total_leads"]
    * 100
)

source_performance = source_performance.sort_values(
    "won_rate_pct", ascending=False
)

print(source_performance)


print("\n=== Won Rate by Region ===")

region_performance = (
    df.groupby("Region")
    .agg(
        total_leads=("Lead_ID", "count"),
        won_deals=("Won_Date", lambda x: x.notna().sum())
    )
)

region_performance["won_rate_pct"] = (
    region_performance["won_deals"]
    / region_performance["total_leads"]
    * 100
)

region_performance = region_performance.sort_values(
    "won_rate_pct", ascending=False
)

print(region_performance)


print("\n=== Won Rate by Company Size ===")

company_size_performance = (
    df.groupby("Company_Size")
    .agg(
        total_leads=("Lead_ID", "count"),
        won_deals=("Won_Date", lambda x: x.notna().sum())
    )
)

company_size_performance["won_rate_pct"] = (
    company_size_performance["won_deals"]
    / company_size_performance["total_leads"]
    * 100
)

company_size_performance = company_size_performance.sort_values(
    "won_rate_pct", ascending=False
)

print(company_size_performance)

print("\n=== Sales Cycle & Engagement Analysis ===")

# Average sales cycle by lead status
sales_cycle_by_status = df.groupby("Lead_Status")["Sales_Cycle_Days"].mean().sort_values()

print("\nAverage Sales Cycle by Lead Status:")
print(sales_cycle_by_status)

# Average engagement score by lead status
engagement_by_status = df.groupby("Lead_Status")["Engagement_Score"].mean().sort_values(
    ascending=False
)

print("\nAverage Engagement Score by Lead Status:")
print(engagement_by_status)

# Engagement score for won vs lost leads
won_engagement = df.loc[
    df["Lead_Status"] == "Won",
    "Engagement_Score"
].mean()

lost_engagement = df.loc[
    df["Lead_Status"] == "Lost",
    "Engagement_Score"
].mean()

print("\nWon Lead Average Engagement Score:", round(won_engagement, 2))
print("Lost Lead Average Engagement Score:", round(lost_engagement, 2))

# Sales cycle for won deals
won_sales_cycle = df.loc[
    df["Lead_Status"] == "Won",
    "Sales_Cycle_Days"
].mean()

print("\nAverage Sales Cycle for Won Deals:", round(won_sales_cycle, 2), "days")
print("\n=== Product Interest Performance ===")

product_performance = df.groupby("Product_Interest").agg(
    total_leads=("Lead_ID", "count"),
    won_deals=("Won_Date", "count"),
    revenue=("Deal_Value", "sum")
)

product_performance["won_rate_pct"] = (
    product_performance["won_deals"]
    / product_performance["total_leads"]
    * 100
)

product_performance = product_performance.sort_values(
    "won_rate_pct",
    ascending=False
)

print(product_performance)
print("\n=== Region + Industry Performance ===")

region_industry = df.groupby(
    ["Region", "Industry"]
).agg(
    total_leads=("Lead_ID", "count"),
    won_deals=("Won_Date", "count"),
    revenue=("Deal_Value", "sum")
)

region_industry["won_rate_pct"] = (
    region_industry["won_deals"]
    / region_industry["total_leads"]
    * 100
)

region_industry = region_industry.sort_values(
    "won_rate_pct",
    ascending=False
)

print(region_industry)
print("\n=== Monthly Lead Performance ===")

df["Lead_Month"] = df["Lead_Date"].dt.to_period("M").astype(str)

monthly_performance = df.groupby("Lead_Month").agg(
    total_leads=("Lead_ID", "count"),
    mqls=("MQL_Date", "count"),
    sqls=("SQL_Date", "count"),
    opportunities=("Opportunity_Date", "count"),
    won_deals=("Won_Date", "count"),
    revenue=("Deal_Value", "sum")
)

monthly_performance["won_rate_pct"] = (
    monthly_performance["won_deals"]
    / monthly_performance["total_leads"]
    * 100
)

print(monthly_performance)


print("\n=== Lead Source Revenue Performance ===")

source_revenue = df.groupby("Lead_Source").agg(
    total_leads=("Lead_ID", "count"),
    won_deals=("Won_Date", "count"),
    revenue=("Deal_Value", "sum")
)

source_revenue["revenue_per_lead"] = (
    source_revenue["revenue"]
    / source_revenue["total_leads"]
)

source_revenue = source_revenue.sort_values(
    "revenue",
    ascending=False
)

print(source_revenue)


print("\n=== Sales Representative Performance ===")

rep_performance = df.groupby("Sales_Rep").agg(
    total_leads=("Lead_ID", "count"),
    won_deals=("Won_Date", "count"),
    revenue=("Deal_Value", "sum"),
    avg_engagement=("Engagement_Score", "mean")
)

rep_performance["won_rate_pct"] = (
    rep_performance["won_deals"]
    / rep_performance["total_leads"]
    * 100
)

rep_performance = rep_performance.sort_values(
    "won_rate_pct",
    ascending=False
)

print(rep_performance)


print("\n=== Region Revenue Performance ===")

region_revenue = df.groupby("Region").agg(
    total_leads=("Lead_ID", "count"),
    won_deals=("Won_Date", "count"),
    revenue=("Deal_Value", "sum")
)

region_revenue["revenue_per_lead"] = (
    region_revenue["revenue"]
    / region_revenue["total_leads"]
)

region_revenue = region_revenue.sort_values(
    "revenue",
    ascending=False
)

print(region_revenue)


print("\n=== Engagement Score Analysis ===")

df["Engagement_Band"] = pd.cut(
    df["Engagement_Score"],
    bins=[0, 25, 50, 75, 100],
    labels=["Low", "Medium", "High", "Very High"],
    include_lowest=True
)

engagement_performance = df.groupby(
    "Engagement_Band",
    observed=True
).agg(
    total_leads=("Lead_ID", "count"),
    won_deals=("Won_Date", "count"),
    revenue=("Deal_Value", "sum")
)

engagement_performance["won_rate_pct"] = (
    engagement_performance["won_deals"]
    / engagement_performance["total_leads"]
    * 100
)

print(engagement_performance)
print("\n=== Revenue Opportunity Analysis ===")

# Revenue from all opportunities
opportunity_leads = df[df["Opportunity_Date"].notna()]

opportunity_revenue = opportunity_leads["Deal_Value"].sum()

print("Total Opportunity Leads:", len(opportunity_leads))
print("Potential Opportunity Revenue:", round(opportunity_revenue, 2))


# Won vs Lost opportunity analysis
won_opportunities = df[
    (df["Opportunity_Date"].notna()) &
    (df["Won_Date"].notna())
]

lost_opportunities = df[
    (df["Opportunity_Date"].notna()) &
    (df["Won_Date"].isna())
]

print("\nWon Opportunities:", len(won_opportunities))
print("Unwon Opportunities:", len(lost_opportunities))

print(
    "Won Opportunity Revenue:",
    round(won_opportunities["Deal_Value"].sum(), 2)
)

print(
    "Unwon Opportunity Value:",
    round(lost_opportunities["Deal_Value"].sum(), 2)
)


# High-value leads
high_value_leads = df[df["Deal_Value"] >= 500000]

print("\nHigh-Value Leads (Deal Value >= 500K):")
print("Total:", len(high_value_leads))

print(
    "High-Value Won Deals:",
    high_value_leads["Won_Date"].notna().sum()
)

print(
    "High-Value Revenue:",
    round(
        high_value_leads.loc[
            high_value_leads["Won_Date"].notna(),
            "Deal_Value"
        ].sum(),
        2
    )
)


# High engagement but not won
high_engagement_unwon = df[
    (df["Engagement_Score"] >= 75) &
    (df["Won_Date"].isna())
]

print("\nHigh-Engagement Unwon Leads:")
print("Total:", len(high_engagement_unwon))

print(
    "Potential Unwon Value:",
    round(high_engagement_unwon["Deal_Value"].sum(), 2)
)


# Opportunity conversion rate
opportunity_conversion = (
    len(won_opportunities)
    / len(opportunity_leads)
    * 100
)

print(
    "\nOpportunity to Won Conversion:",
    round(opportunity_conversion, 2),
    "%"
)
# Export analysis results

monthly_performance.to_csv(
    "outputs/monthly_performance.csv"
)

source_revenue.to_csv(
    "outputs/source_revenue.csv"
)

rep_performance.to_csv(
    "outputs/sales_rep_performance.csv"
)

region_revenue.to_csv(
    "outputs/region_revenue.csv"
)

engagement_performance.to_csv(
    "outputs/engagement_performance.csv"
)

product_performance.to_csv(
    "outputs/product_performance.csv"
)

region_industry.to_csv(
    "outputs/region_industry_performance.csv"
)

print("\n=== Analysis Outputs Exported Successfully ===")
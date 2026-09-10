import pandas as pd
import random
from datetime import timedelta

# Number of leads
NUM_LEADS = 10000

# Lead IDs
lead_ids = [f"L{str(i).zfill(5)}" for i in range(1, NUM_LEADS + 1)]

print(f"Created {len(lead_ids)} Lead IDs")
# Generate random lead dates
start_date = pd.Timestamp("2025-01-01")

lead_dates = [
    start_date + timedelta(days=random.randint(0, 364))
    for _ in range(NUM_LEADS)
]

print("Lead dates created successfully")
# MQL dates
mql_dates = [
    lead_date + timedelta(days=random.randint(1, 7))
    if random.random() < 0.65 else pd.NaT
    for lead_date in lead_dates
]

print("MQL dates created successfully")

# Company information
industries = [
    "Manufacturing",
    "Technology",
    "Healthcare",
    "Finance",
    "Retail",
    "Logistics",
    "Education"
]

company_sizes = [
    "Small",
    "Mid-Market",
    "Enterprise"
]

company_names = [
    f"Company_{i}" for i in range(1, NUM_LEADS + 1)
]

lead_industries = random.choices(industries, k=NUM_LEADS)
lead_company_sizes = random.choices(company_sizes, k=NUM_LEADS)

print("Company information created successfully")
# Lead source and product interest
lead_sources = [
    "LinkedIn",
    "Google Ads",
    "Email Campaign",
    "Website",
    "Webinar",
    "Referral",
    "Trade Show"
]

products = [
    "CRM Software",
    "Analytics Platform",
    "Cloud Solutions",
    "ERP Software",
    "Cybersecurity"
]

lead_sources_data = random.choices(lead_sources, k=NUM_LEADS)
product_interest_data = random.choices(products, k=NUM_LEADS)

print("Lead source and product interest created successfully")
# Engagement score
engagement_scores = [
    random.randint(10, 100)
    for _ in range(NUM_LEADS)
]

print("Engagement scores created successfully")
# Lead status
lead_statuses = [
    "Lead",
    "MQL",
    "SQL",
    "Opportunity",
    "Won",
    "Lost"
]

lead_status_data = random.choices(
    lead_statuses,
    weights=[35, 20, 15, 12, 8, 10],
    k=NUM_LEADS
)
# Region
regions = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]

region_data = random.choices(regions, k=NUM_LEADS)

print("Lead status created successfully")
# Sales representatives
sales_reps = [
    "Amit",
    "Rahul",
    "Priya",
    "Neha",
    "Vikash",
    "Sneha",
    "Arjun"
]

sales_rep_data = random.choices(sales_reps, k=NUM_LEADS)

print("Sales representative data created successfully")

# SQL dates
sql_dates = [
    mql_date + timedelta(days=random.randint(2, 10))
    if pd.notna(mql_date) and random.random() < 0.65 else pd.NaT
    for mql_date in mql_dates
]

print("SQL dates created successfully")

# Opportunity dates
opportunity_dates = [
    sql_date + timedelta(days=random.randint(3, 15))
    if pd.notna(sql_date) and random.random() < 0.55 else pd.NaT
    for sql_date in sql_dates
]

print("Opportunity dates created successfully")

# Won dates
won_dates = [
    opportunity_date + timedelta(days=random.randint(5, 30))
    if pd.notna(opportunity_date) and random.random() < 0.60 else pd.NaT
    for opportunity_date in opportunity_dates
]

print("Won dates created successfully")

# Deal value
deal_values = [
    random.randint(50000, 1000000)
    if pd.notna(opportunity_date) else 0
    for opportunity_date in opportunity_dates
]

print("Deal values created successfully")

# Sales cycle days
sales_cycle_days = [
    (won_date - lead_date).days
    if pd.notna(won_date) else None
    for won_date, lead_date in zip(won_dates, lead_dates)
]

print("Sales cycle days created successfully")

# Create the main dataset
df = pd.DataFrame({
    "Lead_ID": lead_ids,
    "Lead_Date": lead_dates,
    "MQL_Date": mql_dates,
    "SQL_Date": sql_dates,
    "Opportunity_Date": opportunity_dates,
    "Won_Date": won_dates,
    "Deal_Value": deal_values,
    "Sales_Cycle_Days": sales_cycle_days,
    "Company_Name": company_names,
    "Industry": lead_industries,
    "Company_Size": lead_company_sizes,
    "Region": region_data,
    "Lead_Source": lead_sources_data,
    "Sales_Rep": sales_rep_data,
    "Product_Interest": product_interest_data,
    "Engagement_Score": engagement_scores,
    "Lead_Status": lead_status_data
})

print(df.head())




# Export dataset
df.to_csv("data/leads.csv", index=False)

print("Dataset exported successfully!")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print("Missing values:")
print(df.isna().sum())
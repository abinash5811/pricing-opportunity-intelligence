import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
from urllib.parse import quote_plus
from datetime import datetime

# ----------------------------
# Database Configuration
# ----------------------------

DB_USER = "postgres"
DB_PASSWORD = "postgres123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "pricing_intelligence"

encoded_password = quote_plus(DB_PASSWORD)

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ----------------------------
# Helper Function
# ----------------------------

def get_value(query):
    df = pd.read_sql(query, engine)
    return df.iloc[0, 0]

def get_dataframe(query):
    return pd.read_sql(query, engine)
product_df = get_dataframe("""
SELECT *
FROM vw_product_performance
ORDER BY total_revenue DESC;
""")

region_df = get_dataframe("""
SELECT *
FROM vw_region_performance
ORDER BY total_revenue DESC;
""")

discount_df = get_dataframe("""
SELECT *
FROM vw_high_discount_deals;
""")

renewal_df = get_dataframe("""
SELECT *
FROM vw_renewal_risk
WHERE renewal_status = 'High Risk';
""")

upsell_df = get_dataframe("""
SELECT *
FROM vw_upsell_candidates;
""")

# ----------------------------
# KPI Queries
# ----------------------------

total_bookings = get_value("""
SELECT COUNT(*)
FROM fact_booking;
""")

completed_bookings = get_value("""
SELECT COUNT(*)
FROM fact_booking
WHERE booking_status = 'Completed';
""")

total_revenue = get_value("""
SELECT SUM(booking_amount)
FROM fact_booking;
""")

average_booking = get_value("""
SELECT AVG(booking_amount)
FROM fact_booking;
""")

high_discount_deals = get_value("""
SELECT COUNT(*)
FROM vw_high_discount_deals;
""")

renewal_risk = get_value("""
SELECT COUNT(*)
FROM vw_renewal_risk
WHERE renewal_status = 'High Risk';
""")

upsell_candidates = get_value("""
SELECT COUNT(*)
FROM vw_upsell_candidates;
""")

completion_rate = round((completed_bookings / total_bookings) * 100, 2)

# ----------------------------
# Business Health Score
# ----------------------------

health_score = 100

if completion_rate < 50:
    health_score -= 20

if renewal_risk > 400:
    health_score -= 15

if high_discount_deals > 3000:
    health_score -= 10

if upsell_candidates > 300:
    health_score += 5

health_score = max(0, min(100, health_score))

if health_score >= 90:
    overall_health = "EXCELLENT"
    summary = "Business performance is excellent across all monitored KPIs."
elif health_score >= 75:
    overall_health = "GOOD"
    summary = "Business performance is healthy with a few areas for improvement."
elif health_score >= 60:
    overall_health = "MODERATE"
    summary = "Business performance is stable but requires management attention."
else:
    overall_health = "NEEDS ATTENTION"
    summary = "Immediate attention is recommended due to multiple risk indicators."

health_bar = "█" * (health_score // 10) + "░" * (10 - health_score // 10)

# ----------------------------
# Console Output
# ----------------------------

print("=" * 70)
print("        EPAP DAILY EXECUTIVE KPI REPORT")
print("=" * 70)
print(f"Business Health Score : {health_score}/100")
print(f"Overall Health        : {overall_health}")
print("-" * 70)
print(f"Total Revenue         : INR {total_revenue:,.2f}")
print(f"Total Bookings        : {total_bookings:,}")
print(f"Completed Bookings    : {completed_bookings:,}")
print(f"Completion Rate       : {completion_rate}%")
print(f"Average Booking Value : INR {average_booking:,.2f}")
print("-" * 70)
print(f"High Discount Deals   : {high_discount_deals:,}")
print(f"Renewal Risk          : {renewal_risk:,}")
print(f"Upsell Candidates     : {upsell_candidates:,}")
print("=" * 70)

# ----------------------------
# Save Report
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = BASE_DIR / "Reports"
REPORT_DIR.mkdir(exist_ok=True)

filename = REPORT_DIR / f"Daily_KPI_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write("=" * 70 + "\n")
    f.write("        EPAP DAILY EXECUTIVE KPI REPORT\n")
    f.write("=" * 70 + "\n\n")

    f.write(f"Generated On : {datetime.now():%d-%b-%Y %I:%M:%S %p}\n\n")

    f.write("=" * 70 + "\n")
    f.write("EXECUTIVE SUMMARY\n")
    f.write("=" * 70 + "\n\n")
    f.write(f"Overall Business Health : {overall_health}\n")
    f.write(f"Business Health Score   : {health_score}/100\n")
    f.write(f"Health Meter            : {health_bar}\n")
    f.write(f"Executive Summary       : {summary}\n\n")

    f.write("=" * 70 + "\n")
    f.write("KEY BUSINESS METRICS\n")
    f.write("=" * 70 + "\n\n")
    f.write(f"Total Revenue                     : INR {total_revenue:,.2f}\n")
    f.write(f"Total Bookings                    : {total_bookings:,}\n")
    f.write(f"Completed Bookings                : {completed_bookings:,}\n")
    f.write(f"Booking Completion Rate           : {completion_rate}%\n")
    f.write(f"Average Booking Value             : INR {average_booking:,.2f}\n\n")

    f.write("=" * 70 + "\n")
    f.write("PRICING & CUSTOMER INSIGHTS\n")
    f.write("=" * 70 + "\n\n")
    f.write(f"High Discount Deals               : {high_discount_deals:,}\n")
    f.write(f"Customers at Renewal Risk         : {renewal_risk:,}\n")
    f.write(f"High Upsell Opportunity Customers : {upsell_candidates:,}\n\n")

    f.write("=" * 70 + "\n")
    f.write("RECOMMENDED ACTIONS\n")
    f.write("=" * 70 + "\n\n")

    if completion_rate < 50:
        f.write("- Improve booking conversion pipeline.\n")

    if renewal_risk > 400:
        f.write("- Customer Success team should prioritize renewal-risk accounts.\n")

    if high_discount_deals > 3000:
        f.write("- Review pricing approvals for excessive discounting.\n")

    if upsell_candidates > 300:
        f.write("- Launch upsell campaign for highly engaged customers.\n")

    f.write("\n")

    f.write("=" * 70 + "\n")
    f.write("REPORT INFORMATION\n")
    f.write("=" * 70 + "\n\n")
    f.write("Data Source        : PostgreSQL\n")
    f.write("Automation         : Python + SQLAlchemy\n")
    f.write("Analytics Layer    : Business Views + Pricing Intelligence Views\n")
    f.write("Platform           : EPAP Pricing Intelligence\n")
    f.write("Version            : v0.9\n\n")

    f.write("=" * 70 + "\n")
    f.write("Generated Automatically by EPAP Analytics Engine\n")
    f.write("=" * 70 + "\n")

print(f"\nReport saved to:\n{filename}")

excel_file = REPORT_DIR / f"Daily_KPI_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

summary_df = pd.DataFrame({
    "Metric": [
        "Business Health",
        "Health Score",
        "Total Revenue",
        "Total Bookings",
        "Completed Bookings",
        "Completion Rate",
        "Average Booking Value"
    ],
    "Value": [
        overall_health,
        health_score,
        total_revenue,
        total_bookings,
        completed_bookings,
        f"{completion_rate}%",
        average_booking
    ]
})

with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    summary_df.to_excel(writer, sheet_name="Executive Summary", index=False)
    product_df.to_excel(writer, sheet_name="Product Performance", index=False)
    region_df.to_excel(writer, sheet_name="Regional Performance", index=False)
    discount_df.to_excel(writer, sheet_name="High Discount Deals", index=False)
    renewal_df.to_excel(writer, sheet_name="Renewal Risk", index=False)
    upsell_df.to_excel(writer, sheet_name="Upsell Candidates", index=False)

print(f"Excel report saved to:\n{excel_file}")
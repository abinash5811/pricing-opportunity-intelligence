# Tableau Dashboard Notes

## Dashboard Name
Pricing Intelligence Executive Dashboard

## Data Source
PostgreSQL database: pricing_intelligence

## Views Used
- vw_revenue_summary
- vw_product_performance
- vw_region_performance
- vw_open_pipeline
- vw_renewal_risk
- vw_customer_revenue

## Dashboard Sections
1. KPI Summary
2. Revenue by Product
3. Revenue by Region
4. Open Pipeline by Stage
5. Renewal Status Distribution

## Key Insights
- Total Revenue: 1.54B
- Total Bookings: 20,000
- Completed Bookings: 6,653
- North America is the highest revenue region.
- Learning Enterprise is the top revenue product.
- 444 customers are currently high renewal risk.

## Known Limitation
Cross-filtering across all visuals is limited because the dashboard uses multiple aggregated SQL views with different dimensions.
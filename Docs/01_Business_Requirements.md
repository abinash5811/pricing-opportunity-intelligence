# Enterprise Pricing Analytics Platform (EPAP)
## Business Requirements Document

## 1. Project Background

NovaLearn Technologies is a fictional SaaS company that sells enterprise subscription products across learning, recruiting, sales, and marketing solutions.

The business needs a centralized analytics platform to analyze revenue, pricing, discounts, contracts, renewals, customer usage, and sales opportunities.

## 2. Business Objective

Build an end-to-end analytics platform that can:

- Centralize pricing and revenue data
- Track customer renewals
- Identify pricing risk
- Detect high-discount contracts
- Recommend upsell and renewal actions
- Support Tableau dashboards
- Automate reporting using Python and SQL

## 3. Key Stakeholders

| Stakeholder | Business Need |
|---|---|
| Executive Leadership | Revenue, ARR, forecast, risk |
| Pricing Team | Discount analysis, pricing exceptions |
| Sales Managers | Pipeline, win rate, renewal tracking |
| Account Managers | Customer-level insights |
| Customer Success | Usage, health score, churn risk |
| Finance | Bookings and contract value |

## 4. Key Business Questions

### Revenue
- What is total revenue?
- What is ARR?
- Which regions generate the most revenue?
- Which products generate the most revenue?
- Who are the top customers?

### Pricing
- Which customers have high discounts?
- Which contracts are below pricing threshold?
- What is the average discount by product?
- Which pricing exceptions need review?

### Sales
- What is the open pipeline value?
- What is the win rate?
- Which opportunities are close to renewal?
- Which account managers own high-risk deals?

### Customer Success
- Which customers have low seat utilization?
- Which customers are good upsell candidates?
- Which customers are at renewal risk?

## 5. Success Criteria

The project is successful if:

- Data is loaded into PostgreSQL
- Data quality checks are automated
- SQL views generate business KPIs
- Python produces recommendations and risk scores
- Tableau dashboards can connect to the processed data
- GitHub contains clean documentation and project history
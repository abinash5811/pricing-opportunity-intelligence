# 🚀 EPAP Pricing Intelligence Platform

An end-to-end Business Intelligence and Analytics project built using **PostgreSQL, SQL, Python, Tableau and Git** to simulate a real-world Pricing & Monetization Analytics platform.

The project demonstrates how raw transactional booking data can be transformed into meaningful business insights through data modeling, SQL analytics, automated KPI reporting, and executive dashboards.

---

# 📌 Project Overview

The EPAP (Enterprise Pricing Analytics Platform) simulates the workflow of a Pricing & Monetization Analytics team.

The project covers the complete analytics lifecycle:

- Data Warehouse Design
- Star Schema Data Modeling
- SQL Business Analytics
- Business Views
- Automated KPI Reporting
- Executive Dashboard Development
- Git Version Control

The objective is to provide business leaders with actionable insights into revenue, bookings, customer performance, pipeline health, and renewal risks.

---

# 🏗️ Project Architecture

```
                  Raw Business Data
                         │
                         ▼
                PostgreSQL Database
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
     SQL Business Views          Python Automation
          │                             │
          ▼                             ▼
  Executive Dashboards         KPI Reports (TXT/Excel)
          │
          ▼
      Business Insights
```

---

# 📂 Project Structure

```
pricing-opportunity-intelligence/
│
├── Data/
│
├── SQL/
│   ├── Schema
│   ├── Views
│   ├── Analytics Queries
│
├── Python/
│   ├── daily_kpi_report.py
│
├── Tableau/
│   ├── tableau_dashboard.twb
│
├── Reports/
│   ├── Daily KPI Reports
│
├── Docs/
│   ├── Project Documentation
│
├── README.md
└── .gitignore
```

---

# 🗄 Database Design

The project follows a Star Schema design optimized for Business Intelligence and reporting.

## Fact Tables

| Table | Description |
|-------|-------------|
| fact_booking | Booking transactions |
| fact_contract | Customer contracts |
| fact_quote | Pricing quotations |
| fact_usage | Product usage metrics |

## Dimension Tables

| Table | Description |
|-------|-------------|
| dim_customer | Customer master data |
| dim_product | Product catalog |
| dim_region | Geographic regions |
| dim_account_manager | Sales representatives |

---

# 📊 Business Views

Business views simplify reporting and Tableau dashboard development.

| View | Purpose |
|------|---------|
| vw_revenue_summary | Executive KPI Summary |
| vw_region_performance | Revenue by Region |
| vw_product_performance | Product Performance |
| vw_customer_revenue | Top Customers by Revenue |
| vw_open_pipeline | Pipeline Analysis |
| vw_renewal_risk | Renewal Risk Analysis |

---

# 🐍 Python Automation

Python automates business reporting directly from PostgreSQL.

### Current Automation

- Daily KPI Report
- Executive TXT Report
- Executive Excel Report
- Booking Metrics
- Revenue Metrics
- Renewal Risk Summary
- Upsell Opportunity Summary

Generated reports are automatically exported into the Reports folder.

---

# 📈 Tableau Executive Dashboard

The Tableau dashboard provides executives with a real-time overview of business performance.

### Dashboard Components

- Executive KPI Summary
- Revenue by Product
- Revenue by Region
- Open Pipeline by Stage
- Renewal Status Distribution

The dashboard connects directly to PostgreSQL business views.

---

# 📊 Business KPIs

The dashboard tracks several key business metrics including:

- Total Revenue
- Total Bookings
- Average Booking Value
- Completed Bookings
- Revenue by Product
- Revenue by Region
- Pipeline Value
- Renewal Risk
- Customer Distribution

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| PostgreSQL | Data Warehouse |
| SQL | Business Analytics |
| Python | Automation |
| Pandas | Data Processing |
| SQLAlchemy | Database Connectivity |
| OpenPyXL | Excel Report Generation |
| Tableau | Data Visualization |
| Git | Version Control |
| GitHub | Source Code Repository |

---

# ✨ Key Features

- End-to-End Analytics Project
- Star Schema Data Model
- SQL Business Views
- Automated KPI Reporting
- Executive Tableau Dashboard
- Business Analytics
- Revenue Analysis
- Pipeline Analysis
- Renewal Risk Analysis
- Git Version Control

---

# 📚 Skills Demonstrated

This project demonstrates practical experience in:

- SQL
- PostgreSQL
- Data Warehousing
- Data Modeling
- Business Intelligence
- Tableau Dashboard Development
- Python Automation
- Pandas
- SQLAlchemy
- OpenPyXL
- Git
- GitHub
- KPI Reporting
- Data Visualization

---

# 🚀 Future Enhancements

Planned improvements include:

- Interactive Dashboard Filters
- Email Report Automation
- Scheduled Daily Reporting
- Incremental ETL Pipeline
- Data Quality Framework
- Audit Logging
- Advanced Business Analytics
- Predictive Revenue Forecasting
- Customer Churn Prediction

---

# 📷 Dashboard Preview

```
tableau/dashboard_preview.png

```
![Pricing Intelligence Executive Dashboard](image.png)

---

# 📄 Sample Reports

The project automatically generates:

- Daily KPI TXT Report
- Daily KPI Excel Report

Reports are stored inside the Reports folder.

---

# 🎯 Business Use Cases

This project can answer questions such as:

- Which products generate the highest revenue?
- Which region contributes the most revenue?
- How healthy is the sales pipeline?
- Which customers are at renewal risk?
- What is the average booking value?
- Which customers present upsell opportunities?

---

# 📈 Project Status

✅ Database Design Complete

✅ SQL Views Complete

✅ Python Automation Complete

✅ Executive Dashboard Complete

✅ Documentation Complete

🚀 Ready for Portfolio Demonstration

---

# 👨‍💻 Author

**Abinash Patra**

Senior Associate – Data & Intelligence

Pricing & Monetization Analytics

GitHub:
https://github.com/abinash5811

---

⭐ If you found this project useful, consider giving it a Star.
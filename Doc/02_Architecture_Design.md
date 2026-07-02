# Enterprise Pricing Analytics Platform (EPAP)
## Architecture Design Document

## 1. Architecture Overview

EPAP is designed as an end-to-end analytics platform for pricing, revenue, renewals, customer usage, and recommendations.

The platform follows a layered architecture:

Raw Data  
↓  
PostgreSQL Data Warehouse  
↓  
SQL Analytics Layer  
↓  
Python Automation Layer  
↓  
Recommendation & Risk Engine  
↓  
Tableau Dashboards  

## 2. Technology Stack

| Layer | Tool |
|---|---|
| Development | VS Code |
| Version Control | Git + GitHub |
| Database | PostgreSQL |
| SQL Layer | PostgreSQL SQL |
| Automation | Python |
| Data Processing | Pandas |
| Visualization | Tableau |
| ML | scikit-learn |

## 3. Data Flow

1. Python generates realistic source data.
2. Source data is stored as CSV files.
3. CSV files are loaded into PostgreSQL.
4. SQL scripts validate and transform the data.
5. SQL views produce business metrics.
6. Python automation creates recommendations and risk scores.
7. Tableau connects to PostgreSQL/output tables for dashboards.

## 4. Data Warehouse Layers

### Dimension Layer
Stores descriptive business entities:
- dim_customer
- dim_product
- dim_region
- dim_account_manager
- dim_date

### Fact Layer
Stores measurable business events:
- fact_opportunity
- fact_quote
- fact_contract
- fact_booking
- fact_usage

### Analytics Layer
Stores reusable business views:
- revenue summary
- discount analysis
- renewal pipeline
- customer health
- pricing risk

### Recommendation Layer
Stores Python-generated outputs:
- recommendations
- alerts
- risk_scores

## 5. Design Principles

- Every table must support a business question.
- Every SQL query must produce reusable insight.
- Python should automate manual effort.
- Tableau dashboards should support decisions.
- Git commits should represent meaningful progress.
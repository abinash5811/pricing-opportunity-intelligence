# Enterprise Pricing Analytics Platform (EPAP)
## Data Dictionary

## Dimension Tables

### dim_customer
Stores customer profile information.

| Column | Description |
|---|---|
| customer_id | Unique customer identifier |
| customer_name | Customer/company name |
| region_id | Links customer to region |
| industry | Customer industry |
| segment | Enterprise, Mid-Market, or SMB |
| company_size | Size category |
| current_seats | Current contracted seats |
| seat_utilization_percent | Percentage of seats actively used |

### dim_product
Stores product catalog details.

| Column | Description |
|---|---|
| product_id | Unique product identifier |
| product_name | Product name |
| product_family | Learning, Sales, Marketing, Recruiting |
| package_type | Basic, Pro, Enterprise |
| list_price | Standard product price |

### dim_account_manager
Stores sales/account ownership.

| Column | Description |
|---|---|
| account_manager_id | Unique account manager identifier |
| account_manager_name | Account manager name |
| manager_region | Region owned |
| role_title | Job role/title |

## Fact Tables

### fact_opportunity
Stores sales pipeline opportunities.

| Column | Description |
|---|---|
| opportunity_id | Unique opportunity identifier |
| customer_id | Linked customer |
| product_id | Linked product |
| account_manager_id | Sales owner |
| opportunity_stage | Current sales stage |
| opportunity_type | New, Renewal, Expansion |
| renewal_date | Renewal due date |
| expected_value | Expected opportunity value |
| probability_percent | Win probability |

### fact_quote
Stores pricing proposals.

| Column | Description |
|---|---|
| quote_id | Unique quote identifier |
| opportunity_id | Linked opportunity |
| list_price | Standard quoted price |
| quoted_price | Proposed customer price |
| discount_percent | Discount offered |
| quote_status | Draft, Approved, Rejected, Accepted |

### fact_contract
Stores signed customer contracts.

| Column | Description |
|---|---|
| contract_id | Unique contract identifier |
| customer_id | Linked customer |
| product_id | Linked product |
| contract_start_date | Contract start date |
| contract_end_date | Contract end date |
| contract_value | Total contract value |
| contract_term_months | Contract duration |

### fact_booking
Stores recognized bookings/revenue events.

| Column | Description |
|---|---|
| booking_id | Unique booking identifier |
| customer_id | Linked customer |
| product_id | Linked product |
| booking_date | Booking date |
| booking_amount | Revenue amount |
| booking_status | Completed, Pending, Cancelled |

### fact_usage
Stores customer product usage.

| Column | Description |
|---|---|
| usage_id | Unique usage record |
| customer_id | Linked customer |
| product_id | Linked product |
| usage_date | Usage snapshot date |
| active_users | Number of active users |
| licensed_seats | Purchased seats |
| utilization_percent | Active users divided by licensed seats |
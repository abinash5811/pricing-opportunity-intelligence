-- Sprint 3: Star Schema Design
-- Enterprise Pricing Analytics Platform

CREATE TABLE dim_region (
    region_id SERIAL PRIMARY KEY,
    region_name VARCHAR(100) NOT NULL,
    market VARCHAR(100)
);

CREATE TABLE dim_customer (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    region_id INT REFERENCES dim_region(region_id),
    industry VARCHAR(100),
    segment VARCHAR(50),
    company_size VARCHAR(50),
    current_seats INT,
    seat_utilization_percent NUMERIC(5,2)
);

CREATE TABLE dim_product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    product_family VARCHAR(100),
    package_type VARCHAR(100),
    list_price NUMERIC(12,2)
);

CREATE TABLE dim_account_manager (
    account_manager_id SERIAL PRIMARY KEY,
    account_manager_name VARCHAR(150) NOT NULL,
    manager_region VARCHAR(100),
    role_title VARCHAR(100)
);

CREATE TABLE fact_booking (
    booking_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES dim_customer(customer_id),
    product_id INT REFERENCES dim_product(product_id),
    booking_date DATE,
    booking_amount NUMERIC(12,2),
    booking_status VARCHAR(50)
);

CREATE TABLE fact_pricing (
    pricing_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES dim_customer(customer_id),
    product_id INT REFERENCES dim_product(product_id),
    list_price NUMERIC(12,2),
    contract_price NUMERIC(12,2),
    discount_percent NUMERIC(5,2),
    annual_contract_value NUMERIC(12,2),
    contract_term_months INT
);

CREATE TABLE fact_opportunity (
    opportunity_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES dim_customer(customer_id),
    product_id INT REFERENCES dim_product(product_id),
    account_manager_id INT REFERENCES dim_account_manager(account_manager_id),
    opportunity_stage VARCHAR(100),
    opportunity_type VARCHAR(100),
    renewal_date DATE,
    expected_value NUMERIC(12,2),
    probability_percent NUMERIC(5,2)
);
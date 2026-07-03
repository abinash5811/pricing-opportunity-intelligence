DROP TABLE IF EXISTS fact_usage CASCADE;
DROP TABLE IF EXISTS fact_booking CASCADE;
DROP TABLE IF EXISTS fact_contract CASCADE;
DROP TABLE IF EXISTS fact_quote CASCADE;
DROP TABLE IF EXISTS fact_opportunity CASCADE;

DROP TABLE IF EXISTS dim_opportunity_stage CASCADE;
DROP TABLE IF EXISTS dim_contract_type CASCADE;
DROP TABLE IF EXISTS dim_account_manager CASCADE;
DROP TABLE IF EXISTS dim_product CASCADE;
DROP TABLE IF EXISTS dim_customer CASCADE;
DROP TABLE IF EXISTS dim_region CASCADE;
DROP TABLE IF EXISTS dim_date CASCADE;

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

CREATE TABLE dim_contract_type (
    contract_type_id SERIAL PRIMARY KEY,
    contract_type_name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE dim_opportunity_stage (
    stage_id SERIAL PRIMARY KEY,
    stage_name VARCHAR(100) NOT NULL,
    stage_order INT,
    stage_category VARCHAR(100)
);

CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,
    full_date DATE NOT NULL,
    day INT,
    month INT,
    quarter INT,
    year INT,
    day_name VARCHAR(20)
);

CREATE TABLE fact_opportunity (
    opportunity_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES dim_customer(customer_id),
    product_id INT REFERENCES dim_product(product_id),
    account_manager_id INT REFERENCES dim_account_manager(account_manager_id),
    stage_id INT REFERENCES dim_opportunity_stage(stage_id),
    contract_type_id INT REFERENCES dim_contract_type(contract_type_id),
    opportunity_type VARCHAR(100),
    expected_value NUMERIC(12,2),
    probability_percent NUMERIC(5,2),
    renewal_date DATE,
    created_date DATE
);

CREATE TABLE fact_quote (
    quote_id SERIAL PRIMARY KEY,
    opportunity_id INT REFERENCES fact_opportunity(opportunity_id),
    list_price NUMERIC(12,2),
    quoted_price NUMERIC(12,2),
    discount_percent NUMERIC(5,2),
    quote_status VARCHAR(100),
    quote_date DATE
);

CREATE TABLE fact_contract (
    contract_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES dim_customer(customer_id),
    product_id INT REFERENCES dim_product(product_id),
    account_manager_id INT REFERENCES dim_account_manager(account_manager_id),
    contract_type_id INT REFERENCES dim_contract_type(contract_type_id),
    contract_start_date DATE,
    contract_end_date DATE,
    contract_value NUMERIC(12,2),
    contract_term_months INT,
    is_renewal BOOLEAN
);

CREATE TABLE fact_booking (
    booking_id SERIAL PRIMARY KEY,
    contract_id INT REFERENCES fact_contract(contract_id),
    customer_id INT REFERENCES dim_customer(customer_id),
    product_id INT REFERENCES dim_product(product_id),
    booking_date DATE,
    booking_amount NUMERIC(12,2),
    booking_status VARCHAR(50)
);

CREATE TABLE fact_usage (
    usage_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES dim_customer(customer_id),
    product_id INT REFERENCES dim_product(product_id),
    usage_date DATE,
    active_users INT,
    licensed_seats INT,
    utilization_percent NUMERIC(5,2)
);
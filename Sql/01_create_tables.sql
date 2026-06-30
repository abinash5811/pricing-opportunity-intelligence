CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    region TEXT NOT NULL,
    industry TEXT NOT NULL,
    current_seats INTEGER,
    seat_utilization_percent INTEGER

);

CREATE TABLE opportunities(
    opportunity_id INTEGER PRIMARY KEY,
    customer_id INTEGER ,
    stage TEXT,
    renewal_date DATE,
    contract_term_months INTEGER,
    account_manager TEXT
);

CREATE TABLE pricing (
    customer_id INTEGER PRIMARY KEY,
    list_price NUMERIC,
    current_price NUMERIC,
    discount_percent NUMERIC,
    annual_contract_value NUMERIC
);

CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_name TEXT,
    booking_amount NUMERIC,
    booking_date DATE,
    status TEXT
);
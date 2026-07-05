-- high discount deals
CREATE OR REPLACE VIEW vw_high_discount_deals AS
SELECT
    q.quote_id,
    c.customer_name,
    p.product_name,
    q.list_price,
    q.quoted_price,
    q.discount_percent,
    q.quote_status,
    q.quote_date
FROM fact_quote q
JOIN fact_opportunity o
    ON q.opportunity_id = o.opportunity_id
JOIN dim_customer c
    ON o.customer_id = c.customer_id
JOIN dim_product p
    ON o.product_id = p.product_id
WHERE q.discount_percent >= 40
ORDER BY q.discount_percent DESC;

-- renewal risk
CREATE OR REPLACE VIEW vw_renewal_risk AS
SELECT
    customer_name,
    current_seats,
    seat_utilization_percent,
    CASE
        WHEN seat_utilization_percent < 50
            THEN 'High Risk'
        WHEN seat_utilization_percent BETWEEN 50 AND 75
            THEN 'Medium Risk'
        ELSE 'Healthy'
    END AS renewal_status
FROM dim_customer;


-- upsell opportunities
CREATE OR REPLACE VIEW vw_upsell_candidates AS
SELECT
    customer_name,
    current_seats,
    seat_utilization_percent
FROM dim_customer
WHERE seat_utilization_percent >= 90
ORDER BY current_seats DESC;

-- opportunity pipeline
CREATE OR REPLACE VIEW vw_open_pipeline AS
SELECT
    s.stage_name,
    COUNT(*) AS opportunities,
    SUM(expected_value) AS pipeline_value
FROM fact_opportunity o
JOIN dim_opportunity_stage s
ON o.stage_id = s.stage_id
WHERE s.stage_category = 'Open'
GROUP BY s.stage_name;

-- account manager performance
CREATE OR REPLACE VIEW vw_account_manager_performance AS
SELECT
    am.account_manager_name,
    COUNT(fc.contract_id) AS total_contracts,
    SUM(fc.contract_value) AS total_contract_value
FROM fact_contract fc
JOIN dim_account_manager am
ON fc.account_manager_id = am.account_manager_id
GROUP BY am.account_manager_name;
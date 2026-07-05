-- =====================================================
-- EPAP Business Analytics Views
-- =====================================================

-- Revenue Summary
CREATE OR REPLACE VIEW vw_revenue_summary AS
SELECT
    COUNT(*) AS total_bookings,
    SUM(booking_amount) AS total_revenue,
    ROUND(AVG(booking_amount),2) AS average_booking,
    MIN(booking_amount) AS minimum_booking,
    MAX(booking_amount) AS maximum_booking
FROM fact_booking;


-- Product Performance
CREATE OR REPLACE VIEW vw_product_performance AS
SELECT
    dp.product_name,
    COUNT(fb.booking_id) AS total_bookings,
    SUM(fb.booking_amount) AS total_revenue,
    ROUND(AVG(fb.booking_amount),2) AS average_booking
FROM fact_booking fb
JOIN dim_product dp
ON fb.product_id = dp.product_id
GROUP BY dp.product_name;


-- Regional Performance
CREATE OR REPLACE VIEW vw_region_performance AS
SELECT
    dr.region_name,
    COUNT(fb.booking_id) AS total_bookings,
    SUM(fb.booking_amount) AS total_revenue
FROM fact_booking fb
JOIN dim_customer dc
ON fb.customer_id = dc.customer_id
JOIN dim_region dr
ON dc.region_id = dr.region_id
GROUP BY dr.region_name;


-- Customer Revenue
CREATE OR REPLACE VIEW vw_customer_revenue AS
SELECT
    dc.customer_name,
    SUM(fb.booking_amount) AS total_revenue
FROM fact_booking fb
JOIN dim_customer dc
ON fb.customer_id = dc.customer_id
GROUP BY dc.customer_name;
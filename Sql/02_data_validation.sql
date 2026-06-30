-- Row counts
SELECT 'customers' AS table_name, COUNT(*) AS row_count FROM customers
UNION ALL
SELECT 'opportunities', COUNT(*) FROM opportunities
UNION ALL
SELECT 'pricing', COUNT(*) FROM pricing
UNION ALL
SELECT 'bookings', COUNT(*) FROM bookings;

-- Duplicate checks
SELECT customer_id, COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT opportunity_id, COUNT(*) AS duplicate_count
FROM opportunities
GROUP BY opportunity_id
HAVING COUNT(*) > 1;

SELECT booking_id, COUNT(*) AS duplicate_count
FROM bookings
GROUP BY booking_id
HAVING COUNT(*) > 1;

-- Null checks
SELECT *
FROM customers
WHERE customer_id IS NULL
OR customer_name IS NULL
OR region IS NULL
OR segment IS NULL;

SELECT *
FROM pricing
WHERE customer_id IS NULL
OR list_price IS NULL
OR current_price IS NULL
OR discount_percent IS NULL;

-- Pricing anomaly checks
SELECT *
FROM pricing
WHERE current_price > list_price
OR discount_percent < 0
OR discount_percent > 60;
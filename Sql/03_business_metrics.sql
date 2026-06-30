-- Revenue by region
SELECT c.region, SUM(b.booking_amount) AS total_revenue
from bookings b
JOIN customers c ON b.customer_id = c.customer_id
where b.status = 'COMPLETED'
GROUP BY c.region
order by total_revenue DESC;

-- High discount customers
SELECT
    c.customer_id,
    c.customer_name,
    c.region,
    c.segment,
    p.list_price,
    p.current_price,
    p.discount_percent
FROM customers c
JOIN pricing p
    ON c.customer_id = p.customer_id
WHERE p.discount_percent >= 40
ORDER BY p.discount_percent DESC;

-- Renewal opportunities in next 90 days
SELECT
    o.opportunity_id,
    c.customer_name,
    c.region,
    c.segment,
    o.stage,
    o.renewal_date,
    o.contract_term_months,
    o.account_manager
FROM opportunities o
JOIN customers c
    ON o.customer_id = c.customer_id
WHERE o.renewal_date <= CURRENT_DATE + INTERVAL '90 days'
ORDER BY o.renewal_date;

-- Seat utilization risk
SELECT
    customer_id,
    customer_name,
    region,
    segment,
    current_seats,
    seat_utilization_percent
FROM customers
WHERE seat_utilization_percent < 60
ORDER BY seat_utilization_percent ASC;

-- Top 10 customers by completed bookings
SELECT
    c.customer_id,
    c.customer_name,
    SUM(b.booking_amount) AS total_completed_revenue
FROM customers c
JOIN bookings b
    ON c.customer_id = b.customer_id
WHERE b.status = 'Completed'
GROUP BY c.customer_id, c.customer_name
ORDER BY total_completed_revenue DESC
LIMIT 10;

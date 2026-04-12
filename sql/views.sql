-- 1. summarise the order sales
CREATE OR REPLACE VIEW order_summary AS
SELECT
    DATE(order_ts) AS date,
    COUNT(*) AS numb_orders,
    SUM(total_amount) AS order_revenue,
    ROUND(AVG(total_amount),2) AS average_sale
FROM orders
GROUP BY 1;

-- 2. Top N customers
CREATE OR REPLACE VIEW topn_customers AS
SELECT
    customer_id,
    SUM(total_amount) AS lifetime_spend
FROM orders
GROUP BY customer_id
ORDER BY lifetime_spend DESC
LIMIT 10;

-- 3. Top N SKU
CREATE OR REPLACE VIEW topn_skus AS
SELECT
    sku,
    SUM(quantity * unit_price) AS revenue,
    SUM(quantity) AS units_sold
FROM order_items
GROUP BY sku
ORDER BY revenue DESC;

-- 4.  Duplicate customers
CREATE OR REPLACE VIEW duplicate_customers AS
SELECT
    email,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;

-- 5. Orders referencing missing customers
CREATE OR REPLACE VIEW orders_missing_customers AS
SELECT
    o.order_id,
	o.customer_id
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL; -- ant-join patterns
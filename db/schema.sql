-- 1. DROP TABLE and VIEWS
--	customers (Dimesion)
--	orders (Fact)
--	order_items (Fact)
DROP VIEW IF EXISTS order_summary;
DROP VIEW IF EXISTS topn_customers;
DROP VIEW IF EXISTS topn_skus;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;


-- 2. CREATE TABLES
-- customers (Dimesion)
--	orders (Fact)

CREATE TABLE customers
(
	customer_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	email TEXT NOT NULL,
	full_name TEXT NOT NULL,
	signup_date DATE NOT NULL,
	country_code CHAR(2),
	is_active BOOLEAN NOT NULL,
	CONSTRAINT email_constraint UNIQUE (email)
);

CREATE TABLE orders
(
    order_id BIGINT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_ts TIMESTAMPTZ NOT NULL,
    status TEXT NOT NULL,
    total_amount NUMERIC(12,2) NOT NULL,
    currency CHAR(3) NOT NULL,
	CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
	CONSTRAINT chk_status CHECK (status IN ('placed','shipped','cancelled','refunded'))
);

CREATE TABLE order_items 
(
    order_id BIGINT,
    line_no INT,
    sku TEXT NOT NULL,
    quantity INT NOT NULL,
    unit_price NUMERIC(12,2) NOT NULL,
    category TEXT NOT NULL,
	PRIMARY KEY (order_id, line_no),
    CONSTRAINT fk_items_order FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CONSTRAINT chk_quantity CHECK (quantity > 0),
    CONSTRAINT chk_price CHECK (unit_price > 0)
);

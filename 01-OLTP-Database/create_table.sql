use sales;
create table if not exists sales_data (
    product_id INT,
    customer_id INT,
    price INT,
    quantity INT,
    timestamp DATETIME
);

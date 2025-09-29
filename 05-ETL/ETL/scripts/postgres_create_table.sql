create table if not exists sales_data (
    rowid integer constraint firstkey primary key,
    product_id integer not null,
    customer_id integer not null,
    price decimal DEFAULT 0.0 NOT NULL,
    quantity integer not null,
    timeestamp timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
)




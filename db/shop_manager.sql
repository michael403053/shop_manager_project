DROP TABLE IF EXISTS reciepts;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact VARCHAR(255)
);

CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity INT,
    buy_price FLOAT(8),
    sell_price FLOAT(8),
    manufacturer_id INT REFERENCES manufacturers(id)
);

CREATE TABLE reciepts (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    staff_id INT REFERENCES staff(id),
    time_stamp VARCHAR(255),
    quantity INT
    
);


CREATE DATABASE IF NOT EXISTS BANKAYA;
USE BANKAYA;
CREATE TABLE IF NOT EXISTS CUSTOMER(
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    phone_number VARCHAR(30),
    curp VARCHAR(30),
    rfc VARCHAR (30) NOT NULL,
    address_cust TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS ITEMS(
    id INT PRIMARY KEY AUTO_INCREMENT,
    item VARCHAR(30) NOT NULL,
    price decimal NOT NULL
);
CREATE TABLE IF NOT EXISTS ITEMS_BOUGHT(
    id_number INT PRIMARY KEY AUTO_INCREMENT,
    order_number varchar(20) NOT NULL,
    date_order date NOT NULL,
    price decimal NOT NULL,
    comments text,
    id_items INT,
    id_customers INT,
    INDEX id_order_number (id_number,order_number),
    FOREIGN KEY (id_items) REFERENCES ITEMS(id) ON DELETE SET NULL,
    FOREIGN KEY (id_customers) REFERENCES CUSTOMER(id) ON DELETE SET NULL
);
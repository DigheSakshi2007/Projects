CREATE DATABASE plantdb;
\c plantdb;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100)
);
CREATE TABLE plants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    image VARCHAR(200),
    disease TEXT,
    growth_time VARCHAR(50),
    description TEXT
);

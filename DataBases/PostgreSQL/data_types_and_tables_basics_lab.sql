-- task 1
CREATE DATABASE gamebar;

-- Task 2
CREATE TABLE employees
(
    id            SERIAL PRIMARY KEY NOT NULL,
    first_name    VARCHAR(30),
    last_name     VARCHAR(50),
    hiring_date   DATE DEFAULT '2023-01-01',
    salary        NUMERIC (10, 2),
    devices_number INT
);

CREATE TABLE departments
(
    id          SERIAL PRIMARY KEY NOT NULL,
    name        VARCHAR(50),
    code        CHARACTER(3),
    description TEXT
);

CREATE TABLE issues
(
    id          SERIAL PRIMARY KEY UNIQUE,
    description VARCHAR(150),
    date        DATE,
    start       TIMESTAMP
);

-- Task 3

ALTER TABLE employees
    ADD COLUMN middle_name varchar(50);

-- Task 4

ALTER TABLE employees
    ALTER COLUMN salary SET DEFAULT 0,
    ALTER COLUMN salary SET NOT NULL,
    ALTER COLUMN hiring_date SET NOT NULL;

-- Task 5

ALTER TABLE employees
    ALTER COLUMN middle_name TYPE VARCHAR(100);

-- Task 6

TRUNCATE TABLE issues;

-- Task 7

DROP TABLE departments
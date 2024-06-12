-- Task 1

-- CREATE DATABASE taxi_db;

CREATE TABLE addresses(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE categories(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(10) NOT NULL
);

CREATE TABLE clients(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE drivers(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL ,
    age INT NOT NULL CHECK ( age > 0 ),
    rating NUMERIC(2) DEFAULT 5.5
);

CREATE TABLE cars(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    make VARCHAR(20) NOT NULL,
    model VARCHAR(20),
    year INT DEFAULT 0 NOT NULL CHECK ( year > 0 ),
    mileage INT DEFAULT 0 CHECK ( mileage > 0 ),
    condition CHAR(1) NOT NULL,
    category_id INT NOT NULL REFERENCES categories
                 ON DELETE CASCADE
                 ON UPDATE CASCADE
);

CREATE TABLE courses(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    from_address_id INT NOT NULL REFERENCES addresses
                    ON UPDATE CASCADE
                    ON DELETE CASCADE,
    start TIMESTAMP NOT NULL,
    bill NUMERIC(10,2) DEFAULT 10 CHECK ( bill > 0 ),
    car_id INT NOT NULL REFERENCES cars
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
    client_id INT NOT NULL REFERENCES clients
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
);

CREATE TABLE cars_drivers(
    car_id INT NOT NULL REFERENCES cars
                         ON DELETE CASCADE
                         ON UPDATE CASCADE ,
    driver_id INT NOT NULL REFERENCES drivers
                         ON DELETE CASCADE
                         ON UPDATE CASCADE
);

-- Task 2
INSERT INTO
    clients(
            full_name,
            phone_number
)
(SELECT
    CONCAT(first_name,' ',last_name) AS full_name,
    CONCAT('(088) 9999', (id * 2))
FROM
    drivers
WHERE
    id BETWEEN 10 AND 20);

-- Task 3

UPDATE
    cars
SET
    condition = 'C'
WHERE
    (mileage >= 800000 OR mileage IS NULL )
        AND
    year <= 2010
        AND
    make <> 'Mercedes-Benz';

-- Task 4

DELETE FROM
           clients AS c
WHERE
    LENGTH(c.full_name) > 3
        AND
    (SELECT COUNT(id) FROM courses AS crs WHERE crs.client_id = c.id) = 0;

-- Task 5

SELECT
    make,
    model,
    condition
FROM
    cars
ORDER BY
    id;

-- Task 6

SELECT
    d.first_name,
    d.last_name,
    make,
    model,
    mileage
FROM
    drivers AS d
JOIN
    cars_drivers AS cd
ON
    cd.driver_id = d.id
JOIN
    cars AS c
ON
    cd.car_id = c.id
WHERE
    mileage IS NOT NULL
ORDER BY
    mileage DESC,
    first_name;

-- Task 7

SELECT
    c.id AS car_id,
    c.make,
    c.mileage,
    COUNT(crs) AS count_of_courses,
    ROUND(AVG(crs.bill),2) AS average_bill
FROM
    cars AS c
LEFT JOIN
    courses AS crs
ON
    crs.car_id = c.id
GROUP BY
    c.id,
    c.make,
    c.mileage
HAVING
    COUNT(crs) <> 2
ORDER BY
    count_of_courses DESC,
    c.id;

-- Task 8

SELECT
    c.full_name,
    COUNT(crs.car_id) AS count_of_cars,
    SUM(crs.bill) AS total_sum
FROM
    clients AS c
JOIN
    courses AS crs
ON
    crs.client_id = c.id
WHERE
    c.full_name LIKE '_a%'
GROUP BY
    c.full_name
HAVING
    COUNT(crs.car_id) > 1
ORDER BY
    c.full_name;

-- Task 9

SELECT
    a.name AS address,
    CASE
        WHEN cou.start::TIME BETWEEN '06:00:00' AND '20:59:59' THEN
            'Day'
        ELSE
            'Night'
    END
    AS day_time,
    cou.bill,
    full_name,
    make,
    model,
    cat.name AS category_name
FROM
    courses AS cou
JOIN
    addresses AS a
ON
    a.id = cou.from_address_id
JOIN
    clients AS cl
ON
    cl.id = cou.client_id
JOIN
    cars AS c
ON
    c.id = cou.car_id
JOIN
    categories AS cat
ON
    cat.id = c.category_id
ORDER BY
    cou.id;

-- Task 10

CREATE OR REPLACE FUNCTION fn_courses_by_client(
    phone_num VARCHAR(20)
)
RETURNS INT
AS
    $$
        BEGIN
            RETURN
            (SELECT
                COUNT(co)
            FROM
                courses AS co
            RIGHT JOIN
                clients AS cl
            ON
                co.client_id = cl.id
            WHERE
                cl.phone_number = phone_num);
        END;
    $$
LANGUAGE plpgsql;

-- Task 11

CREATE OR REPLACE PROCEDURE sp_courses_by_address(
    address_name VARCHAR(100)
)
AS
    $$
        BEGIN
        CREATE TABLE IF NOT EXISTS search_results (
            id SERIAL PRIMARY KEY,
            address_name VARCHAR(50),
            full_name VARCHAR(100),
            level_of_bill VARCHAR(20),
            make VARCHAR(30),
            condition CHAR(1),
            category_name VARCHAR(50)
        );
            TRUNCATE TABLE search_results;

            INSERT INTO
                search_results(
                               address_name,
                               full_name,
                               level_of_bill,
                               make,
                               condition,
                               category_name
            )
            SELECT
                a.name AS address_name,
                cl.full_name,
                CASE
                    WHEN cou.bill <= 20 THEN
                        'Low'
                    WHEN cou.bill <= 30 THEN
                        'Medium'
                    ELSE
                        'High'
                END
                AS level_of_bill,
                car.make,
                car.condition,
                cat.name AS category_name
            FROM
                addresses AS a
            JOIN
                courses AS cou
            ON
                cou.from_address_id = a.id
            JOIN
                clients AS cl
            ON
                cl.id = cou.client_id
            JOIN
                cars AS car
            ON
                car.id = cou.car_id
            JOIN
                categories AS cat
            ON
                cat.id = car.category_id
            WHERE
                a.name = address_name
            ORDER BY
                car.make,
                cl.full_name;
        END;
    $$
LANGUAGE plpgsql;





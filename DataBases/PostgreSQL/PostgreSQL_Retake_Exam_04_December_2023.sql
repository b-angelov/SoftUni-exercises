-- Task 1

-- CREATE DATABASE bio_bakery_db;

CREATE TABLE countries(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- CREATE TYPE gender_types AS ENUM ('M','F');

CREATE TABLE customers(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender CHAR(1) CHECK(gender IN ('F','M')),
    age INT NOT NULL,
    phone_number CHAR(10) NOT NULL,
    country_id INT NOT NULL,

    CONSTRAINT valid_age CHECK(age > 0),
    CONSTRAINT fk_customers_countries FOREIGN KEY (country_id)
                      REFERENCES countries(id)
                      ON DELETE CASCADE
                      ON UPDATE CASCADE

);

CREATE TABLE products(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(25) NOT NULL,
    description VARCHAR(250),
    recipe TEXT,
    price NUMERIC(10,2) NOT NULL,

    CONSTRAINT products_check_price CHECK (price > 0)
);

CREATE TABLE feedbacks(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    description VARCHAR,
    rate NUMERIC(4,2),
    product_id INT NOT NULL,
    customer_id INT NOT NULL,

    CONSTRAINT feedback_rate_range CHECK(rate BETWEEN 0 AND 10),
    CONSTRAINT fk_feedback_products FOREIGN KEY (product_id)
                      REFERENCES products(id)
                      ON DELETE CASCADE
                      ON UPDATE CASCADE,
    CONSTRAINT fk_feedback_customers FOREIGN KEY (customer_id)
                      REFERENCES customers(id)
                      ON DELETE CASCADE
                      ON UPDATE CASCADE
);

CREATE TABLE distributors(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(25) UNIQUE NOT NULL,
    address VARCHAR(30) NOT NULL,
    summary VARCHAR(200) NOT NULL,
    country_id INT NOT NULL,

    CONSTRAINT fk_distributors_countries FOREIGN KEY (country_id)
                         REFERENCES countries(id)
                         ON DELETE CASCADE
                         ON UPDATE CASCADE
);

CREATE TABLE ingredients(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(30) NOT NULL,
    description VARCHAR(200),
    country_id INT NOT NULL,
    distributor_id INT NOT NULL,

    CONSTRAINT fk_ingredients_countries FOREIGN KEY (country_id)
                         REFERENCES countries(id)
                         ON DELETE CASCADE
                         ON UPDATE CASCADE,
    CONSTRAINT fk_ingredients_distributors FOREIGN KEY (distributor_id)
                        REFERENCES distributors(id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
);

CREATE TABLE products_ingredients(
    product_id INT,
    ingredient_id INT,

    CONSTRAINT fk_product_ingredients_ingredients FOREIGN KEY (ingredient_id)
                                 REFERENCES ingredients(id)
                                 ON DELETE CASCADE
                                 ON UPDATE CASCADE,
    CONSTRAINT fk_product_ingredients_products FOREIGN KEY (product_id)
                                 REFERENCES products(id)
                                 ON DELETE CASCADE
                                 ON UPDATE CASCADE,
    CONSTRAINT pk_product_ingredients PRIMARY KEY (product_id, ingredient_id)
);

-- Task 2

CREATE TABLE gift_recipients(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(76),
    country_id INT NOT NULL REFERENCES countries ON DELETE CASCADE ON UPDATE CASCADE,
    gift_sent BOOLEAN DEFAULT FALSE
);

INSERT INTO gift_recipients(
            name,
            country_id
)
(SELECT
    CONCAT(first_name,' ', last_name) AS name,
    country_id
FROM
    customers);

UPDATE
    gift_recipients
SET
    gift_sent = TRUE
WHERE
    country_id IN (7, 8, 14, 17, 26);

-- select * from gift_recipients;
--
-- alter sequence gift_recipients_id_seq restart with 1;
--
-- delete from gift_recipients;

-- Task 3

UPDATE
    products AS p
SET
    price = p.price * 1.1
WHERE
    (SELECT MAX(f.rate) FROM feedbacks AS f WHERE f.product_id = p.id) > 8
RETURNING *;

-- select * from products order by id;

-- Task 4

DELETE FROM
           distributors
WHERE
    name LIKE 'L%';

-- Task 5

SELECT
    name,
    recipe,
    price
FROM
    products
WHERE
    price BETWEEN 10 AND 20
ORDER BY
    price DESC;

-- Task 6

SELECT
    f.product_id,
    f.rate,
    f.description,
    f.customer_id,
    c.age,
    c.gender
FROM
    feedbacks AS f
JOIN
    customers AS c
ON
    c.id = f.customer_id
WHERE
    rate < 5
        AND
    c.gender = 'F'
        AND
    c.age > 30
ORDER BY
    f.product_id DESC;

-- Task 7

SELECT
    p.name AS product_name,
    ROUND(AVG(price),2) AS average_price,
    COUNT(f) AS total_feedbacks
FROM
    feedbacks AS f
JOIN
    products AS p
ON
    f.product_id = p.id
WHERE
    price > 15
GROUP BY
    p.name
HAVING
    COUNT(f) > 1
ORDER BY
    total_feedbacks;

-- Task 8

SELECT
    i.name AS ingredient_name,
    p.name AS product_name,
    d.name AS distributor_name
FROM
    ingredients AS i
JOIN
    distributors AS d
ON
    i.distributor_id = d.id
JOIN
    products_ingredients AS pi
ON
    pi.ingredient_id = i.id
JOIN
    products AS p
ON
    p.id = pi.product_id
WHERE
    i.name ILIKE '%mustard%'
        AND
    d.country_id = 16
ORDER BY
    product_name;

-- Task 9

SELECT
    d.name AS distributor_name,
    i.name AS ingredient_name,
    p.name AS product_name,
    AVG(f.rate) AS average_rate
FROM
    products AS p
JOIN
    feedbacks AS f
ON
    f.product_id = p.id
JOIN
    products_ingredients AS pi
ON
    p.id = pi.product_id
JOIN
    ingredients AS i
ON
    pi.ingredient_id = i.id
JOIN
    distributors AS d
ON
    i.distributor_id = d.id
GROUP BY
    p.name,
    p.id,
    distributor_name,
    ingredient_name
HAVING
    AVG(f.rate) BETWEEN 5 AND 8
ORDER BY
    distributor_name,
    ingredient_name,
    product_name;

-- Task 10

CREATE OR REPLACE FUNCTION fn_feedbacks_for_product(
    product_name VARCHAR(25)
)
RETURNS TABLE(
    customer_id INT,
    customer_name VARCHAR(75),
    feedback_description VARCHAR,
    feedback_rate NUMERIC(4,2)
             )
AS
    $$
        BEGIN
            RETURN QUERY
                SELECT
                    c.id,
                    c.first_name,
                    f.description,
                    f.rate
                FROM
                    customers AS c
                JOIN
                    feedbacks AS f
                ON
                    c.id = f.customer_id
                JOIN
                    products AS p
                ON
                    p.id = f.product_id
                WHERE
                    p.name = product_name
                ORDER BY
                    c.id
            ;
        END;
    $$
LANGUAGE plpgsql;


-- SELECT * FROM fn_feedbacks_for_product('Bread');


-- Task 11

CREATE OR REPLACE PROCEDURE sp_customer_country_name(
    IN customer_full_name VARCHAR(50),
    OUT country_name VARCHAR(50)
)
AS
    $$
        BEGIN
            SELECT
                cou.name
            INTO
                country_name
            FROM
                customers AS c
            JOIN
                countries AS cou
            ON
                c.country_id = cou.id
            WHERE
                customer_full_name = CONCAT(c.first_name,' ',c.last_name);

        END;
    $$
LANGUAGE plpgsql;

CALL sp_customer_country_name('Jerry Andrews', '');



-- Task 1

CREATE TABLE accounts(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    gender CHAR(1) NOT NULL CHECK ( gender IN ('M','F') ),
    age INT NOT NULL,
    job_title VARCHAR(40) NOT NULL,
    ip VARCHAR(30) NOT NULL
);

CREATE TABLE addresses(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    street VARCHAR(30) NOT NULL,
    town VARCHAR(30) NOT NULL,
    country VARCHAR(30) NOT NULL,
    account_id INT NOT NULL REFERENCES accounts
                      ON UPDATE CASCADE
                      ON DELETE CASCADE
);

CREATE TABLE photos(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description text,
    capture_date TIMESTAMP NOT NULL,
    views INT DEFAULT 0 NOT NULL CHECK ( views >= 0 )
);

CREATE TABLE comments(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    content VARCHAR(255) NOT NULL,
    published_on TIMESTAMP NOT NULL,
    photo_id INT NOT NULL REFERENCES photos
                     ON DELETE CASCADE
                     ON UPDATE CASCADE
);

CREATE TABLE accounts_photos(
    account_id INT NOT NULL REFERENCES accounts
                            ON UPDATE CASCADE
                            ON DELETE CASCADE ,
    photo_id INT NOT NULL REFERENCES photos
                            ON UPDATE CASCADE
                            ON DELETE CASCADE,
    CONSTRAINT pk_acounts_photos PRIMARY KEY (account_id,photo_id)
);

CREATE TABLE likes(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    photo_id INT NOT NULL REFERENCES photos
                  ON DELETE CASCADE
                  ON UPDATE CASCADE,
    account_id INT NOT NULL REFERENCES accounts
                  ON UPDATE CASCADE
                  ON DELETE CASCADE
);

-- Task 2

INSERT INTO
    addresses(
        street,
        town,
        country,
        account_id
)
SELECT
    a.username,
    a.password,
    a.ip,
    a.age
FROM
    accounts AS a
WHERE
    a.gender = 'F';

-- Task 3

UPDATE
    addresses
SET
    country =
    CASE
        WHEN country LIKE 'B%' THEN
            'Blocked'
        WHEN country LIKE 'T%' THEN
            'Test'
        WHEN country LIKE 'P%' THEN
            'In Progress'
        ELSE
            country
    END;

-- Task 4

DELETE FROM
           addresses
WHERE
    id % 2 = 0
        AND
    street ILIKE '%r%';

-- Task 5

SELECT
    username,
    gender,
    age
FROM
    accounts AS a
WHERE
    age >= 18
        AND
    LENGTH(username) > 9
ORDER BY
    a.age DESC,
    a.username;

-- Task 6

SELECT
    p.id AS photo_id,
    p.capture_date,
    p.description,
    COUNT(c) AS comments_count
FROM
    photos AS p
JOIN
    comments AS c
ON
    c.photo_id = p.id
WHERE
    p.description IS NOT NULL
GROUP BY
    p.id,
    p.capture_date,
    p.description
ORDER BY
    comments_count DESC,
    photo_id
LIMIT 3;

-- Task 7

SELECT
    CONCAT(a.id,' ',a.username) AS id_username,
    email
FROM
    accounts AS a
JOIN
    accounts_photos AS ap
ON
    ap.account_id = a.id
WHERE
    ap.photo_id = a.id
ORDER BY
    a.id;

-- Task 8
SELECT
    id AS photo_id,
    (SELECT
         COUNT(l)
     FROM
         likes AS l
     WHERE
         l.photo_id = p.id) AS likes_count,
    (SELECT
         COUNT(c)
     FROM
         comments AS c
     WHERE
         c.photo_id = p.id) AS comments_count
FROM
    photos AS p
ORDER BY
    likes_count DESC,
    comments_count DESC,
    photo_id;

-- Task 9

SELECT
    CONCAT(LEFT(description, 10), '...') AS summary,
    TO_CHAR(capture_date,'DD.MM HH24:MI') AS date
FROM
    photos AS p
WHERE
    EXTRACT(DAY FROM capture_date) = 10
ORDER BY
    capture_date DESC;

-- Task 10

CREATE OR REPLACE FUNCTION udf_accounts_photos_count(
    account_username VARCHAR(30)
)
RETURNS INT
AS
    $$
        BEGIN
            RETURN (SELECT
                COUNT(p)
            FROM
                accounts AS a
            JOIN
                accounts_photos AS ap
            ON
                a.id = ap.account_id
            JOIN
                photos AS p
            ON
                ap.photo_id = p.id
            WHERE
                account_username = a.username
            );
        END;
    $$
LANGUAGE plpgsql;

-- SELECT udf_accounts_photos_count('ssantryd') AS photos_count;

-- Task 11

CREATE OR REPLACE PROCEDURE udp_modify_account(
    address_street VARCHAR(30),
    address_town VARCHAR(30)
)
AS
    $$
        BEGIN
            UPDATE
                accounts AS a
            SET
                job_title = CONCAT('(Remote) ', job_title)
            WHERE
                a.id IN
                (SELECT ad.account_id
                FROM
                    addresses AS ad
                WHERE
                    a.id = ad.account_id
                AND
                    CONCAT(ad.street,ad.town) = CONCAT(address_street,address_town)
                );
        END;
    $$
LANGUAGE plpgsql;



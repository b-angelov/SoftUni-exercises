-- Task 1
CREATE VIEW view_river_info AS
SELECT
    CONCAT(
               'The river',
               ' ',
               river_name,
               ' ',
               'flows into the',
               ' ',
               outflow,
               ' ',
               'and is',
               ' ',
               "length",
               ' ',
               'kilometers long.') AS "River Information"
FROM
    rivers
ORDER BY
    river_name;

-- Task 2

CREATE VIEW view_continents_countries_currencies_details AS
SELECT
    CONCAT(TRIM(cnt.continent_name), ': ',cnt.continent_code) AS continent_details,
    CONCAT_WS(' - ',coun.country_name, coun.capital, coun.area_in_sq_km, 'km2') AS country_information,
    CONCAT(curr.description, ' (', curr.currency_code,')') AS currencies
FROM
    continents AS cnt,
    countries AS coun,
    currencies AS curr
WHERE
    cnt.continent_code = coun.continent_code
        AND
    coun.currency_code = curr.currency_code
ORDER BY
    country_information,
    currencies;

-- Task 3

ALTER TABLE countries
    ADD COLUMN capital_code CHAR(2);

UPDATE countries
    SET
        capital_code = SUBSTRING(capital,1,2);

-- SELECT capital,capital_code FROM countries;

-- Task 4

SELECT
    SUBSTRING(description,5) AS description
FROM
    currencies;

-- Task 5

SELECT
    SUBSTRING("River Information",'[0-9]{1,4}') as river_length
FROM
    view_river_info;

-- Task 6

SELECT
    REPLACE(mountain_range,'a','@') AS replace_a,
    REPLACE(mountain_range,'A','$') AS replace_A
FROM
    mountains;

-- Task 7

SELECT
    capital,
    TRANSLATE(capital, 'áãåçéíñóú', 'aaaceinou') AS translated_name
FROM
    countries;

-- Task 8

SELECT
    continent_name,
    TRIM(LEADING continent_name)
FROM
    continents;

-- Task 9

SELECT
    continent_name,
    TRIM(TRAILING continent_name)
FROM
    continents;

-- Task 10

SELECT
    LTRIM(peak_name,'M') AS left_trim,
    RTRIM(peak_name,'m') AS right_trim
FROM
    peaks;

-- Task 11

SELECT
    CONCAT(m.mountain_range, ' ', p.peak_name) AS mountain_information,
    CHAR_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) AS characters_length,
    BIT_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) AS bits_of_a_tring
FROM
    mountains AS m,
    peaks AS p
WHERE
    p.mountain_id = m.id;

-- Task 12

SELECT
    population,
    LENGTH(CAST(population AS TEXT))
FROM countries;

-- Task 13

SELECT
    peak_name,
    LEFT(peak_name, 4) as positive_left,
    LEFT(peak_name, -4) as negative_left
FROM
    peaks;

-- Task 14

SELECT
    peak_name,
    RIGHT(peak_name, 4) as positive_left,
    RIGHT(peak_name, -4) as negative_left
FROM
    peaks;

-- Task 15

UPDATE
    countries
SET
    iso_code = UPPER(LEFT(country_name, 3))
WHERE
    iso_code IS NULL
RETURNING iso_code;

-- Task 16

UPDATE
    countries
SET
    country_code = LOWER(REVERSE(country_code))
RETURNING country_code;

-- Task 17

SELECT
    CONCAT_WS(' ',elevation,CONCAT(REPEAT('-',3),REPEAT('>',2)),peak_name) AS "Elevation --->> Peak Name"
FROM
    peaks
WHERE
    elevation >= 4884;

-- Task 18

CREATE TABLE bookings_calculation AS
    SELECT
        booked_for
    FROM
        bookings
    WHERE
        apartment_id = 93;

ALTER TABLE bookings_calculation
    ADD COLUMN multiplication NUMERIC,
    ADD COLUMN  modulo NUMERIC;

UPDATE
    bookings_calculation
SET
    multiplication = booked_for * 50,
    modulo = booked_for % 50
RETURNING *;

-- Task 19

SELECT
    latitude,
    ROUND(latitude,2),
    TRUNC(latitude,2)
FROM
    apartments;

-- Task 20

SELECT
    longitude,
    ABS(longitude)
FROM
    apartments;

-- Billing Day - 21

ALTER TABLE
    bookings
ADD COLUMN
    billing_day TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP;

SELECT
    TO_CHAR(billing_day,'DD "Day" MM "Month" YYYY "Year" HH24:MI:SS') AS "Billing Day"
FROM
    bookings;

-- Task 22

SELECT
    EXTRACT('YEAR' FROM booked_at) AS "YEAR",
    EXTRACT('MONTH' FROM booked_at) AS "MONTH",
    EXTRACT('DAY' FROM booked_at) AS "DAY",
    EXTRACT('HOUR' FROM booked_at AT TIME ZONE 'UTC') AS "HOUR",
    EXTRACT('MINUTE' FROM booked_at) AS "MINUTE",
    CEIL(EXTRACT('SECOND' FROM booked_at)) AS "SECOND"
FROM
    bookings;

-- Early Birds - 23

SELECT
    user_id,
    AGE(starts_at, booked_at) AS early_birds
FROM
    bookings
WHERE
    AGE(starts_at,booked_at) >= INTERVAL '10 months'

-- Task 24

SELECT
    companion_full_name,
    email
FROM
    users
WHERE
    companion_full_name ILIKE '%aNd%'
    AND
    email NOT LIKE '%@gmail'

-- Task 25

SELECT
    LEFT(first_name, 2) as initials,
    count(*) AS user_count
FROM
    users
GROUP BY
    initials
ORDER BY
    user_count DESC,
    initials;

-- Task 26

SELECT
    SUM(booked_for) AS total_value
FROM
    bookings
WHERE
    apartment_id = 90;

-- Task 27

SELECT
    AVG(multiplication) AS average_value
FROM
    bookings_calculation;

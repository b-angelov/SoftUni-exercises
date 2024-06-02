-- Task 1

SELECT
    CONCAT(a.address, ' ', a.address_2) AS apartment_address,
    b.booked_for AS nights
FROM
    apartments AS a
JOIN
    bookings AS b
USING
    (booking_id)
ORDER BY
    a.apartment_id;

-- Task 2

SELECT
    a.name,
    a.country,
    b.booked_at::DATE
FROM
    apartments AS a
LEFT JOIN
    bookings AS b
USING
    (booking_id)
LIMIT 10;

-- Task 3

SELECT
    b.booking_id,
    b.starts_at::DATE,
    b.apartment_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM
    bookings AS b
RIGHT JOIN
    customers AS c
USING
    (customer_id)
ORDER BY
    customer_name
LIMIT 10;

-- Task 4

SELECT
    b.booking_id,
    a.name AS apartment_owner,
    a.apartment_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM
    bookings AS b
FULL JOIN
        apartments AS a
    ON
        a.booking_id = b.booking_id
FULL JOIN
    customers AS c
ON
    b.customer_id = c.customer_id
ORDER BY
    b.booking_id,
    apartment_owner,
    customer_name;

-- Task 5

SELECT
    b.booking_id,
    c.first_name AS customer_name
FROM
    bookings AS b
CROSS JOIN
    customers AS c
ORDER BY
    customer_name;

-- Task 6

SELECT
    b.booking_id,
    b.apartment_id,
    c.companion_full_name
FROM
    bookings AS b
LEFT JOIN
    customers AS c
USING
    (customer_id)
WHERE apartment_id IS NULL;


-- Task 7

SELECT
    apartment_id,
    booked_for,
    first_name,
    country
FROM
    bookings AS b
JOIN
    customers AS c
ON
    b.customer_id = c.customer_id
WHERE
    c.job_type = 'Lead';

-- Task 8

SELECT
    COUNT(*)
FROM
    bookings AS b
JOIN
    customers AS c
USING
    (customer_id)
WHERE
    c.last_name = 'Hahn';

-- Task 9

SELECT
    a.name,
    SUM(b.booked_for)
FROM
    apartments AS a
JOIN
    bookings AS b
ON
    b.apartment_id = a.apartment_id
GROUP BY
    a.name
ORDER BY
    a.name;

-- Task 10

SELECT
    a.country,
    COUNT(b.booking_id) AS booking_count
FROM
    apartments AS a
JOIN
    bookings AS b
ON
    b.apartment_id = a.apartment_id
WHERE
    b.booked_at > '2021-05-18 07:52:09.904+03' AND b.booked_at < '2021-09-17 19:48:02.147+03'
GROUP BY
    a.country
ORDER BY
    booking_count DESC;

-- Task 11

SELECT
    mc.country_code,
    m.mountain_range,
    p.peak_name,
    p.elevation
FROM
    mountains AS m
JOIN
    peaks AS p
ON
    m.id = p.mountain_id
JOIN
    mountains_countries AS mc
ON
    mc.mountain_id = m.id
WHERE
    p.elevation > 2835
        AND
    mc.country_code = 'BG'
ORDER BY
    p.elevation DESC;

-- Task 12

SELECT
    mc.country_code,
    COUNT(m.mountain_range) AS mountain_range_count
FROM
    mountains AS m
JOIN
    mountains_countries AS mc
ON
    mc.mountain_id = m.id
WHERE
    mc.country_code IN ('BG','US','RU')
GROUP BY
    mc.country_code
ORDER BY mountain_range_count DESC;

-- Task 13

SELECT
    c.country_name,
    r.river_name
FROM
    countries AS c
LEFT JOIN
    countries_rivers AS cr
USING
    (country_code)
LEFT JOIN
    rivers AS r
ON
    cr.river_id = r.id
WHERE
    c.continent_code = 'AF'
ORDER BY
    country_name
LIMIT 5;

-- Task 14

SELECT
    MIN(x.avg) AS min_average_area
FROM
    (
        SELECT
            AVG(c.area_in_sq_km)
        FROM
            countries AS c
        GROUP BY
            c.continent_code
    ) AS x;

-- Task 15

SELECT
    COUNT(x) AS countries_without_mountains
FROM
    (
        SELECT
            COUNT(mc)
        FROM
            countries AS c
        LEFT JOIN
                mountains_countries AS mc
        USING(country_code)
        WHERE
            mc.mountain_id IS NULL
        GROUP BY
            c.id
    ) AS x;

-- Task 16

CREATE TABLE monasteries(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    monastery_name VARCHAR(255),
    country_code CHAR(2)
);

INSERT INTO
    monasteries (monastery_name, country_code)
VALUES
    ('Rila Monastery "St. Ivan of Rila"', 'BG'),
  ('Bachkovo Monastery "Virgin Mary"', 'BG'),
  ('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
  ('Kopan Monastery', 'NP'),
  ('Thrangu Tashi Yangtse Monastery', 'NP'),
  ('Shechen Tennyi Dargyeling Monastery', 'NP'),
  ('Benchen Monastery', 'NP'),
  ('Southern Shaolin Monastery', 'CN'),
  ('Dabei Monastery', 'CN'),
  ('Wa Sau Toi', 'CN'),
  ('Lhunshigyia Monastery', 'CN'),
  ('Rakya Monastery', 'CN'),
  ('Monasteries of Meteora', 'GR'),
  ('The Holy Monastery of Stavronikita', 'GR'),
  ('Taung Kalat Monastery', 'MM'),
  ('Pa-Auk Forest Monastery', 'MM'),
  ('Taktsang Palphug Monastery', 'BT'),
  ('Sümela Monastery', 'TR');

ALTER TABLE countries
ADD COLUMN
    three_rivers BOOLEAN DEFAULT FALSE;

UPDATE
    countries
SET
    three_rivers = true
WHERE
    (SELECT
         COUNT(*)
     FROM
         countries_rivers
     WHERE
         countries.country_code = countries_rivers.country_code
) >= 3;

SELECT
    m.monastery_name AS monastery,
    c.country_name AS country
FROM
    monasteries AS m
JOIN
    countries AS c
USING
    (country_code)
WHERE
    NOT c.three_rivers
ORDER BY
    monastery_name;

-- Task 17

UPDATE countries
SET
    country_name = 'Burma'
WHERE
    country_name = 'Myanmar';

INSERT INTO
    monasteries (monastery_name, country_code)
VALUES
    ('Hanga Abbey', (SELECT DISTINCT country_code FROM countries WHERE country_name = 'Tanzania')),
    ('Myin-Tin-Daik', (SELECT DISTINCT country_code FROM countries WHERE country_name = 'Myanmar'));

SELECT
    con.continent_name,
    cou.country_name,
    COUNT(mon) AS monasteries_count
FROM
    continents AS con
JOIN
    countries AS cou
USING
    (continent_code)
LEFT JOIN
    monasteries AS mon
ON
    mon.country_code = cou.country_code
WHERE
    NOT cou.three_rivers
GROUP BY
    con.continent_name,
    cou.country_name
ORDER BY
    monasteries_count DESC,
    country_name;

-- Task 18

SELECT
    tablename,
    indexname,
    indexdef
FROM
    pg_indexes
WHERE
    schemaname = 'public'
ORDER BY
    tablename,
    indexname;

-- Task 19

CREATE VIEW
    continent_currency_usage
AS
SELECT
    e.continent_code,
    e.currency_code,
    e.currency_usage
FROM
(SELECT
    d.continent_code,
    d.currency_code,
    d.currency_usage,
    DENSE_RANK() OVER (PARTITION BY d.continent_code ORDER BY d.currency_usage DESC) AS currency_usage_ranked
FROM
    (SELECT
        continent_code,
        currency_code,
        COUNT(*) AS currency_usage
    FROM
        countries
    GROUP BY
        continent_code,
        currency_code
    HAVING
        COUNT(*) > 1) AS d) as e
WHERE
    e.currency_usage_ranked = 1
ORDER BY
    e.currency_usage DESC;


-- Task 20

WITH row_number AS (
    SELECT
        c.country_name,
        p.peak_name AS highest_peak_name,
        p.elevation,
        ROW_NUMBER() OVER (PARTITION BY c.country_name ORDER BY p.elevation DESC) AS highest_peak_rank,
        m.mountain_range AS mountain
    FROM
        peaks AS p
    RIGHT JOIN
        mountains_countries AS mc
    USING
        (mountain_id)
    FULL JOIN
        countries AS c
    USING
        (country_code)
    LEFT JOIN
        mountains AS m
    ON
        mc.mountain_id = m.id
)

SELECT
    country_name,
    COALESCE(highest_peak_name,'(no highest peak)') AS highest_peak_name,
    COALESCE(elevation, 0) AS highest_peak_elevation,
    CASE
        WHEN highest_peak_name IS NOT NULL THEN mountain
        ELSE ('(no mountain)')
    END
FROM
    row_number
WHERE
    highest_peak_rank = 1
ORDER BY
    country_name,
    highest_peak_elevation;


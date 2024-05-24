-- Task 1

SELECT
    title
FROM
    books
WHERE
    title ILIKE 'The%'
ORDER BY id;

-- Task 2

UPDATE books
    SET
        title = repeat('*',3) || substr(title,4)
WHERE
    title ILIKE 'The%'
RETURNING title;

-- Task 3

SELECT
    id,
    (side * height) / 2::NUMERIC AS area
FROM
    triangles
ORDER BY id;

-- Task 4

SELECT
    title,
    ROUND(cost,3) as cost
FROM
    books;

-- Task 5

SELECT
    first_name,
    last_name,
    extract('year' FROM born) as year
FROM
    authors;

-- Task 6

SELECT
    last_name AS "Last Name",
    TO_CHAR(born, 'DD (Dy) Mon YYYY') as "Date of Birth"
FROM
    authors;

-- Task 7

SELECT
    title
FROM
    books
WHERE
    title ILIKE '%Harry Potter%';
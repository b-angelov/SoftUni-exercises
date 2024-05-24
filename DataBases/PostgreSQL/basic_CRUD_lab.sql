-- Task 1

SELECT
    id,
    CONCAT_WS(' ', first_name, last_name) AS "Full Name",
    job_title AS "Job Title"
FROM
    employees;

-- Task 2

SELECT
    id,
    CONCAT(first_name,' ',last_name) AS full_name,
    job_title,
    salary
FROM
    employees
WHERE
    salary > 1000.00
ORDER BY
    id;

-- Task 3

SELECT
    *
FROM
    employees
WHERE
    salary >= 1000.00
        AND
    department_id = 4;

-- Task 4

INSERT INTO
    employees(
              first_name,
              last_name,
              job_title,
              department_id,
              salary
)
VALUES
    ('Samantha', 'Young', 'Housekeeping', 4, 900),
    ('Roger', 'Palmer', 'Waiter', 3, 928.33);

SELECT  * FROM employees;

-- Task 5

UPDATE
    employees
SET
    salary = salary + 100
WHERE
    job_title = 'Manager'
RETURNING *;

-- Task 6

DELETE FROM
           employees
WHERE
    department_id IN (1,2);

SELECT * FROM employees;

-- Task 7

CREATE VIEW
    top_paid
AS SELECT
       *
FROM
    employees
ORDER BY
    salary DESC
LIMIT 1;

SELECT * FROM top_paid;
-- Task 1

SELECT
    count(*)
FROM
    wizard_deposits;

-- Task 2

SELECT
    SUM(deposit_amount) AS total_amount
FROM
    wizard_deposits;

-- Task 3

SELECT
    ROUND(AVG(magic_wand_size),3) AS average_magic_wand_size
FROM
    wizard_deposits;

-- Task 4

SELECT
    MIN(deposit_charge) AS minimum_deposit_charge
FROM
    wizard_deposits;

-- Task 5

SELECT
    MAX(age) AS maximum_age
FROM
    wizard_deposits;

-- Task 6

SELECT
    deposit_group,
    SUM(deposit_interest) as deposit_interest
FROM
    wizard_deposits
GROUP BY
    deposit_group
ORDER BY
    deposit_interest DESC;

-- Task 7

SELECT
    magic_wand_creator,
    MIN(magic_wand_size) AS minimum_wand_size
FROM
    wizard_deposits
GROUP BY
    magic_wand_creator
ORDER BY
    minimum_wand_size
LIMIT 5;

-- Task 8

SELECT
    deposit_group,
    is_deposit_expired,
    FLOOR(AVG(deposit_interest)) AS deposit_interest
FROM
    wizard_deposits
WHERE
    deposit_start_date > '1985-01-01'
GROUP BY deposit_group, is_deposit_expired
ORDER BY
    deposit_group DESC,
    is_deposit_expired;

-- Task 9

SELECT
    last_name,
    count(notes) AS notes_with_dumbledore
FROM
    wizard_deposits
WHERE
    notes LIKE '%Dumbledore%'
GROUP BY
    last_name;

-- Task 10

CREATE VIEW view_wizard_deposits_with_expiration_date_before_1983_08_17 AS
SELECT
    CONCAT(first_name, ' ', last_name) AS wizard_name,
    deposit_start_date AS start_date,
    deposit_expiration_date AS expiration_date,
    deposit_amount AS amount
FROM
    wizard_deposits
WHERE
    deposit_expiration_date <= '1983-08-17'
GROUP BY
    wizard_name,
    start_date,
    expiration_date,
    amount
ORDER BY
    expiration_date;

-- Task 11

SELECT
    magic_wand_creator,
    MAX(deposit_amount) AS max_deposit_amount
FROM
    wizard_deposits
WHERE
    deposit_amount NOT BETWEEN 20000 AND 40000
GROUP BY
    magic_wand_creator
ORDER BY
    max_deposit_amount DESC
LIMIT 3;

-- Task 12

SELECT
    CASE
        WHEN age BETWEEN 0 AND 10 THEN '[0-10]'
        WHEN age BETWEEN 11 AND 20 THEN '[11-20]'
        WHEN age BETWEEN 21 AND 30 THEN '[21-30]'
        WHEN age BETWEEN 31 AND 40 THEN '[31-40]'
        WHEN age BETWEEN 41 AND 50 THEN '[41-50]'
        WHEN age BETWEEN 51 AND 60 THEN '[51-60]'
        WHEN age >= 61 THEN '[61+]'
    END AS age_group,
    count(age)
FROM
    wizard_deposits
GROUP BY
    age_group
ORDER BY
    age_group;

-- Task 13

SELECT
    COUNT(CASE department_id WHEN 1 THEN 'Engineering' END) AS "Engineering",
    COUNT(CASE department_id WHEN 2 THEN 'Tool Design' END) AS "Tool Design",
    COUNT(CASE department_id WHEN 3 THEN 'Sales' END) AS "Sales",
    COUNT(CASE department_id WHEN 4 THEN 'Marketing' END) AS "Marketing",
    COUNT(CASE department_id WHEN 5 THEN 'Purchasing' END) AS "Purchasing",
    COUNT(CASE department_id WHEN 6 THEN 'Research and Development' END) AS "Research and Development",
    COUNT(CASE department_id WHEN 7 THEN 'Production' END) AS "Production"
FROM
    employees;

-- Task 14

UPDATE
    employees
SET
    salary = CASE
                WHEN hire_date < '2015-01-16' THEN salary + 2500
                WHEN hire_date < '2020-03-04' THEN salary + 1500
                ELSE salary
            END,
    job_title = CASE
                    WHEN hire_date < '2015-01-16' THEN CONCAT('Senior ', job_title)
                    WHEN hire_date < '2020-03-04' THEN CONCAT('Mid-', job_title)
                    ELSE job_title
                END
RETURNING *;

-- Task 15

SELECT
    job_title,
    CASE
        WHEN AVG(salary) > 45800 THEN 'Good'
        WHEN AVG(salary) BETWEEN 27500 AND 45800 THEN 'Medium'
        WHEN AVG(salary) < 27500 THEN 'Need Improvement'
    END AS category
FROM
    employees
GROUP BY
    job_title
ORDER BY
    category,
    job_title;

-- Task 16

SELECT
    project_name,
    CASE
        WHEN start_date IS NULL AND end_date IS NULL THEN 'Ready for development'
        WHEN start_date IS NOT NULL AND end_date IS NULL THEN 'In Progress'
        ELSE 'Done'
    END AS project_status
FROM
    projects
WHERE
    project_name LIKE '%Mountain%';

-- Task 17

SELECT
    department_id,
    COUNT(*) AS num_employees,
    CASE
        WHEN AVG(salary) > 50000 THEN 'Above average'
        WHEN AVG(salary) <= 50000 THEN 'Below average'
    END AS salary_level
FROM
    employees
GROUP BY
    department_id
HAVING
    AVG(salary) > 30000
ORDER BY
    department_id;


-- Task 18

CREATE VIEW view_performance_rating AS
SELECT
    first_name,
    last_name,
    job_title,
    salary,
    department_id,
    CASE
        WHEN salary >= 25000 THEN CASE
            WHEN job_title LIKE 'Senior%' THEN 'High-performing Senior'
            ELSE 'High-performing Employee'
        END
        ELSE 'Average-performing'
    END AS performance_rating
FROM
    employees;

-- Task 19

CREATE TABLE employees_projects(
    id INT PRIMARY KEY,
    employee_id INT REFERENCES employees(id),
    project_id INT REFERENCES projects(id)
);

-- Task 20

SELECT
    *
FROM
    departments as d
JOIN employees ON d.id = department_id;


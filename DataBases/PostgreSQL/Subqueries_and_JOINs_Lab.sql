-- Task 1

SELECT
    t.town_id,
    t.name,
    a.address_text
FROM
    towns AS t
JOIN
    addresses AS a
USING
    (town_id)
WHERE
    t.name IN ('San Francisco', 'Sofia', 'Carnation')
ORDER BY
    t.town_id,
    a.address_id;

-- Task 2

SELECT
    e.employee_id,
    CONCAT(e.first_name , ' ' , e.last_name) AS full_name,
    d.department_id,
    d.name
FROM
    employees AS e
JOIN
    departments AS d
ON
    e.employee_id = d.manager_id
ORDER BY
    e.employee_id
LIMIT 5;

-- Task 3

SELECT
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
    ep.project_id,
    p.name
FROM
    employees AS e
JOIN
    employees_projects AS ep
USING
    (employee_id)
JOIN
    projects AS p
ON
    p.project_id = ep.project_id
WHERE
    p.project_id = 1;

-- Task 4

SELECT
    COUNT(*)
FROM
    employees
WHERE
    salary > (SELECT AVG(salary) AS salary FROM employees);
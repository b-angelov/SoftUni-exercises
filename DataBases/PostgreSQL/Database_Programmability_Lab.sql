-- Task 1

CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
    RETURNS INT AS
$$
DECLARE
    result INT;
BEGIN
    SELECT
        count(*) AS count
    FROM
        towns AS t
    JOIN
        addresses AS a
    USING
        (town_id)
    JOIN
        employees AS e
    USING
        (address_id)
    WHERE
        t.name = town_name INTO result;

    RETURN result;
END;
$$
    LANGUAGE plpgsql;

-- SELECT *
-- FROM fn_count_employees_by_town('Sofia');

-- Task 2

CREATE OR REPLACE PROCEDURE sp_increase_salaries(department_name VARCHAR(50))
    AS
$$
    BEGIN
        UPDATE
            employees
        SET
            salary = salary * 1.05
        WHERE
            department_id = (
                SELECT
                    department_id
                FROM
                    departments AS d
                WHERE
                    department_name = d.name
            );
    END;
$$
LANGUAGE plpgsql;

-- CALL sp_increase_salaries('Finance');
--
-- SELECT first_name,salary From employees WHERE department_id = (select department_id from departments where name = 'Finance') order by first_name, salary;


-- Task 3

CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
AS
    $$
        BEGIN
            UPDATE
                employees AS e
            SET
                salary = salary * 1.05
            WHERE
                e.employee_id = id;
            IF (SELECT employee_id FROM employees WHERE employee_id = id) IS NULL
                THEN
            ROLLBACK;
            END IF;
        END;
    $$
LANGUAGE plpgsql;

-- CALL sp_increase_salary_by_id(17);
--
-- select first_name, salary from employees where employee_id = 17;

-- Task 4

CREATE TABLE deleted_employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    middle_name VARCHAR(20),
    job_title VARCHAR(50),
    department_id INT,
    salary NUMERIC(19,4)
);

CREATE OR REPLACE FUNCTION tr_fn_deleted_employees_log()
RETURNS TRIGGER
AS
    $$
        BEGIN
            INSERT INTO deleted_employees(first_name, last_name, middle_name, job_title, department_id, salary)
            VALUES
                (OLD.first_name, OLD.last_name,OLD.middle_name, OLD.job_title, OLD.department_id,OLD.salary);
            RETURN NULL;
        END;
    $$
LANGUAGE plpgsql;

CREATE TRIGGER tr_deleted_employees
    AFTER DELETE
    ON
        employees
    FOR EACH ROW
    EXECUTE FUNCTION
        tr_fn_deleted_employees_log();

-- delete from employees where employee_id = 2;
--
-- select * from deleted_employees;


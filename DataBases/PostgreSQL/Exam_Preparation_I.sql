-- Task 1

-- CREATE DATABASE zoo_db;

CREATE TABLE owners(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    name VARCHAR(50) NOT NULL ,
    phone_number VARCHAR(15) NOT NULL ,
    address VARCHAR(50)
);

CREATE TABLE animal_types(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    animal_type VARCHAR(50) NOT NULL
);

CREATE TABLE cages(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    animal_type_id INT NOT NULL REFERENCES animal_types
                  ON UPDATE CASCADE
                  ON DELETE CASCADE
);

CREATE TABLE animals(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    birthdate DATE NOT NULL,
    owner_id INT REFERENCES owners
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
    animal_type_id INT NOT NULL REFERENCES animal_types
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
);

CREATE TABLE volunteers_departments(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    department_name VARCHAR(30) NOT NULL
);

CREATE TABLE volunteers(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address VARCHAR(50),
    animal_id INT REFERENCES animals
                       ON DELETE CASCADE
                       ON UPDATE CASCADE,
    department_id INT NOT NULL REFERENCES volunteers_departments
                       ON DELETE CASCADE
                       ON UPDATE CASCADE
);

CREATE TABLE animals_cages(
    cage_id INT NOT NULL REFERENCES cages
                          ON UPDATE CASCADE
                          ON DELETE CASCADE ,
    animal_id INT NOT NULL REFERENCES animals
                          ON DELETE CASCADE
                          ON UPDATE CASCADE--,
--     CONSTRAINT pk_animals_cages PRIMARY KEY (cage_id,animal_id)
);

-- Task 2

INSERT INTO
    volunteers(
    name,
    phone_number,
    address,
    animal_id,
    department_id
)
VALUES
    ('Anita Kostova',	'0896365412',	'Sofia, 5 Rosa str.',	15,	1),
    ('Dimitur Stoev',	'0877564223',	NULL,	42,	4),
    ('Kalina Evtimova',	'0896321112',	'Silistra, 21 Breza str.',	9,	7),
    ('Stoyan Tomov',	'0898564100',	'Montana, 1 Bor str.',	18,	8),
    ('Boryana Mileva',	'0888112233',	NULL,	31,	5);

INSERT INTO
    animals(
            name,
            birthdate,
            owner_id,
            animal_type_id
)
VALUES
    ('Giraffe',	'2018-09-21',	21,	1),
    ('Harpy Eagle',	'2015-04-17',	15,	3),
    ('Hamadryas Baboon',	'2017-11-02',	NULL,	1),
    ('Tuatara',	'2021-06-30',	2,	4);

-- Task 3

UPDATE
    animals
SET
    owner_id = (SELECT id FROM owners WHERE name = 'Kaloqn Stoqnov')
WHERE
    owner_id IS NULL;

-- Task 4

DELETE FROM
    volunteers_departments
WHERE
    department_name = 'Education program assistant';

-- Task 5

SELECT
    name,
    phone_number,
    address,
    animal_id,
    department_id
FROM
    volunteers
ORDER BY
        name,
        animal_id,
        department_id;

-- Task 6

SELECT
    name,
    animal_type,
    TO_CHAR(birthdate,'DD.MM.YYYY') AS birthdate
FROM
    animals AS a
JOIN
    animal_types AS at
ON
    at.id = a.animal_type_id
ORDER BY
    a.name;

-- Task 7

SELECT
    o.name AS owner,
    COUNT(a) AS count_of_animals
FROM
    owners AS o
JOIN
    animals AS a
ON
    a.owner_id = o.id
GROUP BY
    o.name
ORDER BY
    count_of_animals DESC,
    o.name
LIMIT 5;

-- Task 8

SELECT
    CONCAT(o.name,' - ',a.name) AS "owners - animals",
    phone_number,
    cage_id
FROM
    owners AS o
JOIN
    animals AS a
ON
    o.id = a.owner_id
JOIN
    animals_cages AS ag
ON
    ag.animal_id = a.id
JOIN
    cages AS cg
ON
    cg.id = ag.cage_id
JOIN
    animal_types AS at
ON
    at.id = a.animal_type_id
WHERE
    at.animal_type = 'Mammals'
ORDER BY
    o.name,
    a.name DESC;

-- Task 9

SELECT
    v.name AS volunteers,
    phone_number,
    LTRIM(address, 'Sofia, ') AS address
FROM
    volunteers AS v
JOIN
    volunteers_departments AS vd
ON
    vd.id = v.department_id
WHERE
    address ILIKE '%Sofia%'
        AND
    vd.department_name = 'Education program assistant'
ORDER BY
    v.name;

-- Task 10

SELECT
    a.name AS animal,
    EXTRACT(YEAR FROM a.birthdate) AS birth_year,
    animal_type
FROM
    animals AS a
JOIN
    animal_types AS at
ON
    at.id = a.animal_type_id
WHERE
    a.owner_id IS NULL
        AND
    '01/01/2022'::DATE - INTERVAL '5 years' < a.birthdate
        AND
    at.animal_type <> 'Birds'
ORDER BY
    a.name;

-- Task 11

CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(
    searched_volunteers_department VARCHAR(30)
)
RETURNS INT
AS
    $$
        BEGIN
                RETURN
                (SELECT
                    COUNT(v)
                FROM
                    volunteers_departments AS vd
                JOIN
                    volunteers AS v
                ON
                    v.department_id = vd.id
                WHERE vd.department_name = searched_volunteers_department);
        END;
    $$
LANGUAGE plpgsql;

-- SELECT fn_get_volunteers_count_from_department('Zoo events')

-- Task 12

CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    animal_name VARCHAR(30),
    OUT owner_name VARCHAR(50)
)
AS
    $$
--         DECLARE
--             owner_name VARCHAR(50);
        BEGIN
            SELECT
                COALESCE(o.name,'For adoption')
            INTO
                owner_name
            FROM
                animals AS a
            LEFT JOIN
                owners AS o
            ON
                a.owner_id = o.id
            WHERE
                a.name = animal_name;
            RAISE NOTICE '%',owner_name;
        END;
    $$
LANGUAGE plpgsql;


-- CALL sp_animals_with_owners_or_not('Pumpkinseed Sunfish','');
-- CALL sp_animals_with_owners_or_not('Hippo','');
-- CALL sp_animals_with_owners_or_not('Brown bear', '');
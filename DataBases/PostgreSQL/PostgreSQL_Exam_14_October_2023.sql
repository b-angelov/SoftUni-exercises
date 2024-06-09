-- Task 1

-- CREATE DATABASE soccer_talent_db;

CREATE TABLE towns(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    name VARCHAR(45) NOT NULL
);

CREATE TABLE stadiums(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    name VARCHAR(45) NOT NULL,
    capacity INT NOT NULL CHECK(capacity > 0),
    town_id INT NOT NULL
                     REFERENCES towns(id)
                     ON DELETE CASCADE
                     ON UPDATE CASCADE
);

CREATE TABLE teams(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    name VARCHAR(45) NOT NULL,
    established DATE NOT NULL,
    fan_base INT DEFAULT 0 NOT NULL CHECK ( fan_base >= 0),
    stadium_id INT NOT NULL
                     REFERENCES stadiums(id)
                     ON DELETE CASCADE
                     ON UPDATE CASCADE
);

CREATE TABLE coaches(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    salary NUMERIC(10,2) DEFAULT 0 NOT NULL CHECK(salary >= 0),
    coach_level INT DEFAULT 0 NOT NULL CHECK(coach_level >= 0)
);

CREATE TABLE skills_data(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    dribbling INT DEFAULT 0 CHECK ( dribbling >= 0 ),
    pace INT DEFAULT 0 CHECK ( pace >= 0 ),
    passing INT DEFAULT 0 CHECK ( passing >= 0 ),
    shooting INT DEFAULT 0 CHECK ( shooting >= 0 ),
    speed INT DEFAULT 0 CHECK ( speed >= 0 ),
    strength INT DEFAULT 0 CHECK ( strength >= 0 )

);

CREATE TABLE players(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE PRIMARY KEY,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    age INT DEFAULT 0 NOT NULL CHECK ( age >= 0 ),
    position CHAR(1) NOT NULL,
    salary NUMERIC(10,2) DEFAULT 0 NOT NULL CHECK ( salary >= 0 ),
    hire_date TIMESTAMP,
    skills_data_id INT NOT NULL,
    team_id INT,

    CONSTRAINT fk_players_skills_data FOREIGN KEY (skills_data_id)
                    REFERENCES skills_data(id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE,
    CONSTRAINT fk_players_teams FOREIGN KEY (team_id)
                    REFERENCES teams(id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
);

CREATE TABLE players_coaches(
    player_id INT ,
    coach_id INT ,

    CONSTRAINT fk_players_coaches_players FOREIGN KEY (player_id)
                            REFERENCES players(id)
                            ON DELETE CASCADE
                            ON UPDATE CASCADE,
    CONSTRAINT fk_players_coaches_coaches FOREIGN KEY (coach_id)
                            REFERENCES coaches(id)
                            ON UPDATE CASCADE
                            ON DELETE CASCADE,
    CONSTRAINT pk_players_coaches PRIMARY KEY (player_id,coach_id)
);

-- Task 2

INSERT INTO coaches(
    first_name,
    last_name,
    salary,
    coach_level
)
SELECT
    first_name,
    last_name,
    salary * 2 AS salary,
    LENGTH(first_name) AS coach_level
FROM
    players AS p
WHERE
    p.hire_date < '2013-12-13 07:18:46';

select * from coaches;

-- truncate coaches cascade;

-- Task 3

UPDATE
    coaches AS c
SET
    salary = c.salary * c.coach_level
WHERE
    c.first_name LIKE 'C%'
        AND
    (SELECT COUNT(p) FROM players AS p
                     JOIN
                        players_coaches AS pc
                     ON
                         pc.player_id = p.id
                     WHERE c.id = pc.coach_id) > 0;

-- Task 4

DELETE FROM
    players AS p
WHERE
    p.hire_date < '2013-12-13 07:18:46';

-- Task 5

SELECT
    CONCAT(first_name,' ',last_name) AS full_name,
    age,
    hire_date
FROM
    players
WHERE
    first_name LIKE 'M%'
ORDER BY
    age DESC,
    full_name;

-- Task 6

SELECT
    p.id,
    CONCAT(first_name,' ',last_name) AS full_name,
    p.age,
    p.position,
    p.salary,
    sd.pace,
    sd.shooting
FROM
    players AS p
JOIN
    skills_data AS sd
ON
    p.skills_data_id = sd.id
WHERE
    (sd.pace + sd.shooting) > 130
        AND
    p.team_id IS NULL
        AND
    p.position = 'A';

-- Task 7

SELECT
    t.id AS team_id,
    t.name AS team_name,
    COUNT(p) AS player_count,
    t.fan_base
FROM
    teams AS t
LEFT JOIN
    players AS p
ON
    p.team_id = t.id
WHERE
    t.fan_base > 30000
GROUP BY
    t.id,
    t.name,
    t.fan_base
ORDER BY
    player_count DESC,
    fan_base DESC;


-- Task 8

SELECT
    CONCAT(c.first_name,' ',c.last_name) AS coach_full_name,
    CONCAT(p.first_name,' ',p.last_name) AS player_full_name,
    t.name AS team_name,
    sd.passing,
    sd.shooting,
    sd.speed
FROM
    players AS p
JOIN
    teams AS t
ON
   t.id = p.team_id
JOIN
    players_coaches AS pc
ON
    p.id = pc.player_id
JOIN
    coaches AS c
ON
    c.id = pc.coach_id
JOIN
    skills_data AS sd
ON
    p.skills_data_id = sd.id
ORDER BY
    coach_full_name,
    player_full_name DESC;

-- Task 9

CREATE OR REPLACE FUNCTION fn_stadium_team_name(
    stadium_name VARCHAR(30)
)
RETURNS TABLE(team_name VARCHAR(45))
AS
    $$
        DECLARE
            team_name VARCHAR(45);
        BEGIN
            RETURN QUERY
                SELECT
                    t.name
                FROM
                    teams AS t
                JOIN
                    stadiums AS s
                ON
                    t.stadium_id = s.id
                WHERE
                    s.name = stadium_name
                ORDER BY
                    t.name;
        END;
    $$
LANGUAGE plpgsql;


-- SELECT fn_stadium_team_name('Jaxworks')

-- Task 10

CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(45)
)
AS
    $$
        BEGIN
            SELECT
                COALESCE(t.name,'The player currently has no team')
            INTO
                team_name
            FROM
                players AS p
            LEFT JOIN
                teams AS t
            ON
                p.team_id = t.id
            WHERE
                CONCAT(p.first_name,' ',p.last_name) = player_name;
        END;
    $$
LANGUAGE plpgsql;

-- CALL sp_players_team_name('Isaak Duncombe', '');
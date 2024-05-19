-- Task 0

CREATE DATABASE minions_db;

-- Task 1

CREATE TABLE minions
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(30),
    age  INT
);

-- Task 2

ALTER TABLE minions
    RENAME TO minions_info;

-- Task 3

ALTER TABLE minions_info
    ADD COLUMN code   CHAR(4),
    ADD COLUMN task   TEXT,
    ADD COLUMN salary NUMERIC(8, 3);

-- Task 4

ALTER TABLE minions_info
    RENAME COLUMN salary TO banana;

-- Task 5

ALTER TABLE minions_info
    ADD COLUMN email    VARCHAR(20),
    ADD COLUMN equipped BOOLEAN NOT NULL DEFAULT false;

-- Task 6

CREATE TYPE type_mood AS ENUM ('happy', 'relaxed', 'stressed', 'sad');

ALTER TABLE minions_info
    ADD COLUMN mood type_mood;

-- Task 7

ALTER TABLE minions_info
    ALTER COLUMN age SET DEFAULT 0,
    ALTER COLUMN name SET DEFAULT '',
    ALTER COLUMN code SET DEFAULT '';

-- Task 8

ALTER TABLE minions_info
    ADD CONSTRAINT unique_containt
        UNIQUE (id, email),
    ADD CONSTRAINT banana_check
        CHECK (banana > 0);

-- Task 9

ALTER TABLE minions_info
    ALTER COLUMN task TYPE varchar(150);

-- Task 10

ALTER TABLE minions_info
    ALTER COLUMN equipped DROP NOT NULL;

-- Task 11

ALTER TABLE minions_info
    DROP COLUMN age;

-- Task 12

CREATE TABLE minions_birthdays
(
    id            SERIAL NOT NULL,
    name          VARCHAR(50),
    date_of_birth DATE,
    age           INT DEFAULT 0,
    present       VARCHAR(100),
    party         TIMESTAMPTZ,
    UNIQUE (id)

);

-- Task 13

INSERT INTO minions_info
    (name, code, task, banana, email, equipped, mood)
VALUES ('Mark', 'GKYA', 'Graphing Points', 3265.265, 'mark@minion.com', false, 'happy'),
       ('Mel', 'HSK', 'Science Investigation', 54784.996, 'mel@minion.com', true, 'stressed'),
       ('Bob', 'HF', 'Painting', 35.652, 'bob@minion.com', true, 'happy'),
       ('Darwin', 'EHND', 'Create a Digital Greeting', 321.958, 'darwin@minion.com', false, 'relaxed'),
       ('Kevin', 'KMHD', 'Construct with Virtual Blocks', 35214.789, 'kevin@minion.com', false, 'happy'),
       ('Norbert', 'FEWB', 'Testing', 3265.500, 'norbert@minion.com', true, 'sad'),
       ('Donny', 'L', 'Make a Map', 8.452, 'donny@minion.com', true, 'happy');

-- Task 14

SELECT "name", "task", "email", "banana" FROM minions_info;

-- Task 15

TRUNCATE TABLE minions_info;

-- Task 16

DROP TABLE minions_birthdays;

-- Task 17

DROP DATABASE minions_db;
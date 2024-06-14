-- Task 1

CREATE TABLE categories(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE addresses(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    street_name VARCHAR(100) NOT NULL,
    street_number INT NOT NULL CHECK ( street_number > 0 ),
    town VARCHAR(30) NOT NULL,
    country VARCHAR(50) NOT NULL,
    zip_code INT NOT NULL CHECK ( zip_code > 0 )
);

CREATE TABLE publishers(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    address_id INT NOT NULL REFERENCES addresses
                       ON UPDATE CASCADE
                       ON DELETE CASCADE ,
    website VARCHAR(40),
    phone VARCHAR(20)
);

CREATE TABLE players_ranges(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    min_players INT NOT NULL CHECK ( min_players > 0 ),
    max_players INT NOT NULL CHECK ( max_players > 0 )
);

CREATE TABLE creators(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL ,
    last_name VARCHAR(30) NOT NULL ,
    email VARCHAR(30) NOT NULL
);

CREATE TABLE board_games(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    release_year INT NOT NULL CHECK ( release_year > 0 ),
    rating NUMERIC(10,2) NOT NULL,
    category_id INT NOT NULL REFERENCES categories
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,
    publisher_id INT NOT NULL REFERENCES publishers
                        ON UPDATE CASCADE
                        ON DELETE CASCADE,
    players_range_id INT NOT NULL REFERENCES players_ranges
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
);

CREATE TABLE creators_board_games(
    creator_id INT NOT NULL REFERENCES creators
                                 ON UPDATE CASCADE
                                 ON DELETE CASCADE ,
    board_game_id INT NOT NULL REFERENCES board_games
                                 ON UPDATE CASCADE
                                 ON DELETE CASCADE
);

-- Task 2

INSERT INTO
    board_games(
                name,
                release_year,
                rating,
                category_id,
                publisher_id,
                players_range_id
)
VALUES
    ('Deep Blue',	2019,	5.67,	1,	15,	7),
    ('Paris',	2016,	9.78,	7,	1,	5),
    ('Catan: Starfarers',	2021,	9.87,	7,	13,	6),
    ('Bleeding Kansas',	2020,	3.25,	3,	7,	4),
    ('One Small Step',	2019,	5.75,	5,	9,	2);

INSERT INTO
    publishers(
               name,
               address_id,
               website,
               phone
)
VALUES
('Agman Games',	5,	'www.agmangames.com',	'+16546135542'),
('Amethyst Games',	7,	'www.amethystgames.com',	'+15558889992'),
('BattleBooks',	13,	'www.battlebooks.com',	'+12345678907');

-- Task 3

UPDATE
    players_ranges
SET
    max_players = max_players + 1
WHERE
    CONCAT(min_players,max_players) = '22';

UPDATE
    board_games
SET
    name = name || ' V2'
WHERE
    release_year >= 2020;

-- Task 4

DELETE FROM
           board_games
CASCADE
WHERE
    id IN (SELECT bg.id FROM
                board_games AS bg
                JOIN
                    publishers AS p
                ON
                    p.id = bg.publisher_id
                JOIN
                    addresses AS a
                ON
                    a.id = p.address_id
                 WHERE a.town LIKE 'L%');

DELETE FROM
           addresses
WHERE
    town LIKE 'L%';

-- Task 5

SELECT
    name,
    rating
FROM
    board_games
ORDER BY
    release_year,
    name DESC ;

-- Task 6

SELECT
    bg.id,
    bg.name,
    bg.release_year,
    cat.name AS category_name
FROM
    board_games AS bg
JOIN
    categories AS cat
ON
    bg.category_id = cat.id
WHERE
    cat.name IN ('Strategy Games' , 'Wargames' )
ORDER BY
    release_year DESC;

-- Task 7

SELECT
    cs.id,
    CONCAT(cs.first_name, ' ', cs.last_name) AS creator_name,
    cs.email
FROM
    creators AS cs
LEFT JOIN
    creators_board_games AS cbg
ON
    cbg.creator_id = cs.id
WHERE
    cbg.creator_id IS NULL;

-- Task 8

SELECT
    bg.name,
    bg.rating::NUMERIC(10,2),
    c.name AS category_name
FROM
    board_games AS bg
JOIN
    categories AS c
ON
    c.id = bg.category_id
JOIN
    players_ranges AS pr
ON
    bg.players_range_id = pr.id
WHERE
    rating > 7.00
        AND
    ((bg.name ILIKE '%a%')
        OR
    (rating > 7.50 AND (pr.min_players = 2 AND pr.max_players = 5)))
ORDER BY
    bg.name,
    bg.rating DESC
LIMIT 5;


-- Task 9

SELECT
    CONCAT(first_name,' ',last_name) AS full_name,
    c.email,
    MAX(bg.rating) AS rating
FROM
    creators AS c
JOIN
    creators_board_games AS cbg
ON
    cbg.creator_id = c.id
JOIN
    board_games AS bg
ON
    cbg.board_game_id = bg.id
WHERE
    RIGHT(c.email,4) = '.com'
GROUP BY
    c.first_name,
    c.last_name,
    c.email
ORDER BY
    full_name;

-- Task 10

SELECT
    c.last_name,
    CEILING(AVG(bg.rating)) AS average_rating,
    p.name AS publisher_name
FROM
    creators AS c
JOIN
    creators_board_games AS cbg
ON
    cbg.creator_id = c.id
JOIN
    board_games AS bg
ON
    bg.id = cbg.board_game_id
JOIN
    publishers AS p
ON
    bg.publisher_id = p.id
WHERE
    p.name = 'Stonemaier Games'
GROUP BY
    c.last_name,
    p.name
ORDER BY
    average_rating DESC;

-- Task 11


CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
    BOARD_GAME_CREATOR VARCHAR(30)
)
RETURNS INT
AS
    $$
        BEGIN
            RETURN
            (SELECT
                count(bg)
            FROM
                creators AS c
            JOIN
                creators_board_games AS cbg
            ON
                cbg.creator_id = c.id
            JOIN
                board_games AS bg
            ON
                bg.id = cbg.board_game_id
            WHERE
                board_game_creator = c.first_name);
        END;
    $$
LANGUAGE plpgsql;

-- Task 12

CREATE OR REPLACE PROCEDURE usp_search_by_category(
    category VARCHAR(50)
)
AS
    $$
        DECLARE
            category_name VARCHAR(50);
        BEGIN

            CREATE TABLE IF NOT EXISTS search_results (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                release_year INT,
                rating FLOAT,
                category_name VARCHAR(50),
                publisher_name VARCHAR(50),
                min_players VARCHAR(50),
                max_players VARCHAR(50)
                                        );

            category_name = category;

            INSERT INTO
                search_results(
                    name,
                    release_year,
                    rating,
                    category_name,
                    publisher_name,
                    min_players,
                    max_players
            )
            SELECT
                bg.name,
                bg.release_year,
                bg.rating,
                c.name AS category_name,
                p.name AS publisher_name,
                CONCAT(min_players,' people'),
                CONCAT(max_players,' people')
            FROM
                board_games AS bg
            JOIN
                categories AS c
            ON
                bg.category_id = c.id
            JOIN
                publishers AS p
            ON
                p.id = bg.publisher_id
            JOIN
                players_ranges AS pr
            ON
                bg.players_range_id = pr.id
            WHERE
                category_name = c.name
            ORDER BY
                publisher_name,
                bg.release_year DESC;

        END;
    $$
LANGUAGE plpgsql;



-- CALL usp_search_by_category('Wargames');
--
-- SELECT * FROM search_results;

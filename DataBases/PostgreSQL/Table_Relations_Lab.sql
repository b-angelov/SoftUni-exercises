-- Task 1
CREATE TABLE mountains
(
    id   INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(50)
);

CREATE TABLE peaks
(
    id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name        VARCHAR(50),
    mountain_id INT ,
    CONSTRAINT fk_peaks_mountains
        FOREIGN KEY (mountain_id)
            REFERENCES mountains(id)
);

-- Task 2

SELECT
    driver_id,
    vehicle_type,
    CONCAT(first_name,' ', last_name) AS driver_name
FROM
    vehicles AS v
JOIN
    campers AS c
ON
    c.id = v.driver_id;

-- Task 3

SELECT
    r.start_point,
    r.end_point,
    r.leader_id,
    CONCAT(c.first_name,' ',c.last_name) AS leader_name
FROM
    routes AS r
JOIN
    campers AS c
ON
    r.leader_id = c.id;

-- Task 4
DROP TABLE peaks;

DROP TABLE mountains;

CREATE TABLE mountains(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE peaks(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50),
    mountain_id INT,
    CONSTRAINT fk_mountain_id
                  FOREIGN KEY (mountain_id)
                  REFERENCES mountains(id) ON DELETE CASCADE

);

-- Task 5

CREATE TABLE clients(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE employees(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    project_id INT
);

CREATE TABLE projects(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    client_id INT,
    project_lead_id INT,
    CONSTRAINT fk_client_id_clients
                     FOREIGN KEY (client_id)
                     REFERENCES clients(id),
    CONSTRAINT fk_project_lead_id_projects
                     FOREIGN KEY (project_lead_id)
                     REFERENCES employees(id)
);

ALTER TABLE employees
    ADD CONSTRAINT fk_project_id_projects
        FOREIGN KEY (project_id)
    REFERENCES
        projects(id);


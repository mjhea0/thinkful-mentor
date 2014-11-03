drop table if exists person;

CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    email_addr TEXT,
    phone_num TEXT
);

CREATE TABLE pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed_id INTEGER,
    age INTEGER,
    adopted INTEGER,
    dead INTEGER
);

CREATE TABLE species (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE breed (
    id INTEGER PRIMARY KEY,
    name TEXT,
    species_id INTEGER
);

CREATE TABLE person_pet (
    person_id INTEGER,
    pet_id INTEGER
);

INSERT INTO person VALUES (0, "Michael", "Johnson", 31, "michael@johnson.com", "555-555-5555");

INSERT INTO species VALUES (0, "Cat");
INSERT INTO species VALUES (1, "Dog");

INSERT INTO breed VALUES (0, "Black", 0);
INSERT INTO breed VALUES (1, "German Shepherd", 0);
INSERT INTO breed VALUES (2, "Poodle", 1);

INSERT INTO pet VALUES (0, "Wilson", 0, 5, 1, 0);
INSERT INTO pet VALUES (1, "Hollie", 1, 8, 1, 1);
INSERT INTO pet VALUES (0, "Einstein", 2, 2, 1, 1);

INSERT INTO person_pet VALUES (0, 0);
INSERT INTO person_pet VALUES (0, 1);
CREATE DATABASE cvmaker;

\c cvmaker;

CREATE TABLE contact_info (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    title VARCHAR(100),
    phone VARCHAR(25),
    email VARCHAR(100),
    address VARCHAR(30)
);

CREATE TABLE language (
    id SERIAL PRIMARY KEY,
    language_name VARCHAR(100),
    language_level INTEGER
);

CREATE TABLE study (
    id SERIAL PRIMARY KEY,
    school VARCHAR(100),
    career VARCHAR(100),
    description VARCHAR(400)
);

CREATE TABLE certification (
    id SERIAL PRIMARY KEY,
    certification VARCHAR(100)
);

CREATE TABLE skill (
    id SERIAL PRIMARY KEY,
    skill VARCHAR(100)
);

CREATE TABLE experience (
    id SERIAL PRIMARY KEY,
    company VARCHAR(100),
    job_title VARCHAR(100),
    job_description VARCHAR(400),
    date1 VARCHAR(100),
    date2 VARCHAR(100)
);

CREATE TABLE site (
    id SERIAL PRIMARY KEY,
    site_name VARCHAR(100)
);

CREATE TABLE about_me (
    id SERIAL PRIMARY KEY,
    description VARCHAR(400)
);
CREATE DATABASE API_AER WITH ENCODING 'UTF8'
CONNECT API_AER
CREATE TABLE IF NOT EXISTS problems
(
    id_problem            serial PRIMARY KEY,
    title                 VARCHAR(255) UNIQUE NOT NULL,
    no_repeated_accepteds INT                 NOT NULL,
    wrong_answer          INT                 NOT NULL,
    accepteds             INT                 NOT NULL,
    shipments             INT                 NOT NULL,
    time_limit            INT                 NOT NULL,
    memory_limit          INT                 NOT NULL,
    presentation_error    INT                 NOT NULL,
    attempts              INT                 NOT NULL,
    other                 INT                 NOT NULL,
    restricted_function   INT                 NOT NULL,
    compilation_error     INT                 NOT NULL,
    c_shipments           INT                 NOT NULL,
    cpp_shipments         INT                 NOT NULL,
    java_shipments        INT                 NOT NULL,
    category_id           INT,
    CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES categories (id_category)
);

CREATE TABLE IF NOT EXISTS users
(
    id_user         serial PRIMARY KEY,
    nick            VARCHAR(25) UNIQUE NOT NULL,
    name            VARCHAR(25) UNIQUE NOT NULL,
    country         VARCHAR(25)        NOT NULL,
    institution     VARCHAR(100)       NOT NULL,
    logo_src        VARCHAR(255),
    shipments       INT                NOT NULL,
    total_accepteds INT                NOT NULL,
    intents         INT                NOT NULL,
    accepteds       INT                NOT NULL
);

CREATE TABLE IF NOT EXISTS blacklist_users
(
    id_blacklist serial PRIMARY KEY,
    number_user  INT NOT NULL
);

CREATE TABLE IF NOT EXISTS categories
(
    id_category      serial PRIMARY KEY,
    name             VARCHAR(255) UNIQUE NOT NULL,
    related_category INT,
    CONSTRAINT fk_category_id FOREIGN KEY (related_category) REFERENCES categories (id_category)
);

CREATE TABLE IF NOT EXISTS categories
(
    id_category      serial PRIMARY KEY,
    name             VARCHAR(255) NOT NULL,
    related_category INT
);
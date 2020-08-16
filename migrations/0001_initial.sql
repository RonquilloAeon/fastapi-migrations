CREATE TABLE category (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE source (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    author text NOT NULL,
    work text NOT NULL
);

CREATE TABLE quote (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category integer REFERENCES category(id) NOT NULL,
    source integer REFERENCES source(id) NOT NULL,
    content text NOT NULL
);

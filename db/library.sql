DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS library;

CREATE TABLE libraries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    library_id INT REFERENCES libraries(id)
);

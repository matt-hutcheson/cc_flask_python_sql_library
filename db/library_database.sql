DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  publisher VARCHAR(255),
  genre VARCHAR(255),
  loan_status BOOLEAN,
  author_id INT REFERENCES authors(id)
);

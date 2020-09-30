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
  number_of_pages INT,
  author_id INT REFERENCES authors(id)
);

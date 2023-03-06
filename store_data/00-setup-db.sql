DROP DATABASE IF EXISTS nc_flix;

CREATE DATABASE buissiness_data;

\c buissiness_data

CREATE TABLE stores (
    store_id SERIAL PRIMARY KEY,
    city VARCHAR
);

CREATE TABLE customers (
  customer_id SERIAL PRIMARY KEY,
  customer_name VARCHAR,
  date_of_birth DATE,
  location VARCHAR
);

CREATE TABLE movies (
  movie_id SERIAL PRIMARY KEY,
  title VARCHAR,
  release_date DATE,
  rating INT,
  cost DECIMAL,
  classification VARCHAR
);

CREATE TABLE stock (
  stock_id SERIAL PRIMARY KEY,
  store_id INT REFERENCES stores(store_id),
  movie_id INT REFERENCES movies(movie_id)
);

INSERT INTO stores
(city)
VALUES
('Leeds'),
('Manchester'),
('Newcastle'),
('Birmingham');


INSERT INTO customers
(customer_name, date_of_birth, location)
VALUES
('David','1992-12-30', 'Leeds'),
('Joe','1989-06-21', 'Liverpool'),
('Verity','1997-01-07', 'Leicester'),
('Cat','1985-11-02', 'Manchester'),
('Alex','2001-06-24', 'Manchester'),
('Duncan', '1994-01-19', 'Manchester'),
('Jersey', '2022-05-01', 'Leicester'),
('Paul C', '1991-03-28', 'Bolton'),
('Haz', '1992-07-02', 'Bolton');


INSERT INTO movies
(title, release_date, rating, cost, classification)
VALUES
('Ghostbusters II', '1989-12-01', null, 1.50, 'U'),
('The Breakfast Club', '1985-06-07', 3, 2.00, '12'),
('Todo Sobre Mi Madre', '2015-08-15', 5, 1.25, '12'),
('The Lion King II: Simba''s Pride', '1998-10-26', 1, 1.50, 'U'),
('The Care Bears Movie', '1985-08-14', 10, 1.00, null),
('Tron', '1982-10-21', null, 2.00, '15'),
('Highlander', '1986-08-29', 3, 1.00, '15'),
('Cleopatra', '1963-07-31', 6, 1.00, 'U'),
('Catch Me If You Can', '2003-01-27', 7, 2.00, '15'),
('Taxi Driver', '1976-08-19', null, 1.00, '15'),
('The Princess Switch', '2018-11-16', null, 1.00, null),
('Girl, Interrupted', '2000-03-24', 8, 2.00, '12'),
('The Fellowship of the Ring', '2001-12-19', 9, 2.50, '12'),
('Episode I - The Phantom Menace', '1999-05-19', 7, 1.50, null),
('Episode IV - A New Hope', '1977-05-25', 10, 2.25, '12'),
('Episode IX - The Rise of Skywalker', '2019-12-20', 3, 1.25, '15'),
('Back to the Future', '1985-07-03', 10, 2.50, 'U'),
('Back to the Future Part II', '1989-11-22', null, 1.75, 'U'),
('The Godfather', '1972-03-14', 10, 1.50, '18'),
('Raiders of the Lost Ark', '1981-06-12', 9, 2.25, '12'),
('Pulp Fiction', '1994-05-21', 5, 2.00, null),
('Toy Story', '1995-11-19', 10, 1.50, 'U'),
('Groundhog Day', '1993-02-12', 7, 1.50, 'U'),
('A Fish Called Wanda', '1988-07-07', 7, 1.50, null),
('Independance Day', '1996-07-03', 7, 1.00, '15');

INSERT INTO stock
(store_id, movie_id)
VALUES
(1, 22),
(1, 22),
(1, 21),
(1, 7),
(1, 7),
(1, 7),
(1, 15),
(1, 15),
(1, 16),
(1, 16),
(2, 22),
(2, 17),
(2, 17),
(2, 18),
(2, 18),
(2, 9),
(2, 9),
(2, 9),
(2, 9),
(2, 10),
(3, 12),
(3, 21),
(3, 21),
(3, 21),
(3, 5),
(4, 14),
(4, 14),
(4, 14),
(4, 14),
(4, 14),
(4, 14),
(4, 15),
(4, 15),
(4, 13),
(4, 16);




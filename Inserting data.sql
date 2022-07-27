INSERT INTO books (book_name, author, release_year)
VALUES ('1984', 'George Orwell', 1949),
       ('The old man and the sea', 'Ernest Hemingway', 1952),
       ('Crime and punishment', 'Fyodor Dostoevsky', 1866),
       ('To kill a mockingbird', 'Harper Lee', 1960),
       ('Notes from undeground', 'Fyodor Dostoevsky', 1864),
       ('The kite runner', 'Khaled Hosseini', 2003),
       ('L\'étranger', 'Albert Camus', 1942),
       ('Les misérables', 'Victor Hugo', 1862),
       ('Sans famille', 'Hector Malot', 1878),
       ('Le dernier jour d\'un condamné', 'Victor Hugo', 1829),
       ('Pride and Prejudice', 'Jane Austen', 1813),
       ('The Great Gatsby', 'Scott Fitzgerald', 1925),
       ('La gloire de mon père', 'Marcel Pagnol', 1957),
       ('The brothers Karamazov', 'Fyodor Dostoevsky', 1879),
       ('Le petit prince', 'Antoine de Saint-Exupéry', 1943);

INSERT INTO countries (country_name, last_release_id, last_release_year)
VALUES ('France', 15, 1943),
       ('UK', 1, 1949);
INSERT INTO countries (country_name)
VALUES ('Spain');
INSERT INTO countries (country_name, last_release_id, last_release_year)
VALUES ('Afghanistan', 6, 2003),
       ('USA', 4, 1960),
       ('Russia', 14, 1879);

INSERT INTO authors (author, birth_year, country_id)
VALUES ('Victor Hugo', 1802, 400),
       ('Fyodor Dostoevsky', 1821, 405),
       ('Marcel Pagnol', 1946, 400),
       ('Jane Austen', 1775, 401),
       ('Scott Fitzgerald', 1896, 404),
       ('George Orwell', 1903, 401),
       ('Khaled Hosseini', 1965, 403),
       ('Ernest Hemingway', 1899, 404),
       ('Harper Lee', 1926, 404),
       ('Antoine de Saint-Exupéry', 1900, 400),
       ('Albert Camus', 1913, 400),
       ('Hector Malot', 1830, 400);

UPDATE books
	JOIN authors ON books.author = authors.author
		SET books.author_id = authors.author_id
		WHERE books.author = authors.author; # disable safe update mode

INSERT INTO publishers (publisher_name)
VALUES ('folio'),
       ('Le livre de poche'),
       ('Harper Collins'),
       ('Simon and Schuster'),
       ('Fayard'),
       ('Oxford University Press'),
       ('Pearson');

INSERT INTO publishing (publisher_id, author_id, total_sales)
VALUES (200, 100, 400000),
       (200, 110, 120000),
       (200, 111, 80000),
       (201, 100, 250000),
       (201, 110, 150000),
       (201, 111, 100000),
       (202, 101, 200000),
       (202, 103, 60000),
       (202, 105, 70000),
       (203, 104, 150000),
       (203, 107, 120000),
       (203, 108, 90000),
       (204, 100, 60000),
       (204, 110, 50000),
       (204, 111, 30000),
       (205, 101, 250000),
       (205, 104, 130000),
       (206, 103, 120000),
       (206, 106, 60000),
       (206, 108, 100000);

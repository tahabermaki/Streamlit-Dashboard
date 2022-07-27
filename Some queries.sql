SELECT * FROM books;
SELECT * FROM authors;
SELECT * FROM countries;
SELECT * FROM publishers;
SELECT * FROM publishing;


SELECT countries.country_name, COUNT(countries.country_name) 
FROM authors 
JOIN books ON books.author_id=authors.author_id 
JOIN countries ON countries.country_id=authors.country_id 
GROUP BY country_name;

SELECT publishers.publisher_name, sum(publishing.total_sales) as total_sales FROM publishing
JOIN publishers ON publishers.publisher_id=publishing.publisher_id
GROUP BY publishing.publisher_id
ORDER BY sum(publishing.total_sales) DESC;

SELECT books.book_name FROM books 
WHERE books.author IN (
SELECT authors.author FROM authors
JOIN countries ON authors.country_id=countries.country_id
WHERE countries.country_name="France");

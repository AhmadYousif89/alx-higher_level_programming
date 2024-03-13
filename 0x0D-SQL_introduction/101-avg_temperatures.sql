-- SQL script that displays the average temperature by (city) ordered by (value) (descending).
SELECT city, AVG(value) AS 'avg_temp'
FROM temperatures GROUP BY city ORDER BY avg_temp DESC;

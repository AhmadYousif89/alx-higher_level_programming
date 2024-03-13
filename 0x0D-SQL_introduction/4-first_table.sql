-- SQL script that creates a table called (first_table) in the current database (mysql).
-- Table description:
	-- id INT
	-- name VARCHAR(256)
-- If the table already exists, script should not fail.
-- The SELECT and SHOW statements are not allowed.

CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));

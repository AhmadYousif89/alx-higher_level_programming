-- SQL script that lists the number of records with the same score in the table (second_table) of the database (hbtn_0c_0).
-- The result should display:
	-- The score.
	-- The number of records for this score with the label number.
-- The list should be sorted by the number of records (descending).
SELECT score, COUNT(score) AS 'number'
FROM second_table GROUP BY score ORDER BY number DESC;
-- script that lists the number of records with the same score in the table
-- second_table of the database hbtn_0c_0 in a MySQL server
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score HAVING
COUNT(score) >= 1 ORDER BY score DESC;

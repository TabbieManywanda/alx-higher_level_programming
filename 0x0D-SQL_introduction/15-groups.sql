-- lists number of records with the same score
-- result should display score and number of records with label number
-- list sorted by number of records (descending)
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

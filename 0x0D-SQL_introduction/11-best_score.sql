-- lists all records with score >= 10 in second_table
-- results display both score and name in that order
-- ordered by score; top first
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC

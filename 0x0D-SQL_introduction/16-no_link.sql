-- lists all records of the table
-- dont list rows without name value
-- display score and name in that order
-- descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

-- lists all cities contained in the database
-- display: cities.id, cities.name, states.name
-- sorted in ascending order by cities.id
-- only use one SELECT statement
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY id ASC;

-- creates table
-- if table name already exists, script should not fail
CREATE TABLE IF NOT EXISTS force_name(
	id	INT,
	name	VARCHAR(256)	NOT NULL
);

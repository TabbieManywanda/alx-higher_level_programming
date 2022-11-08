-- creates database and table
-- implementing foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL, CONSTRAINT FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);

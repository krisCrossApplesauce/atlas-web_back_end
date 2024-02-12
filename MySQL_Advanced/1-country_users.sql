-- write an SQL script that creates a table called users that:
-- contains the attributes: id, email, name, and country
-- doesn't fail if table already exists
-- is executable on any database
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    country ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);

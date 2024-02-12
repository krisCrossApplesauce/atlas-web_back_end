-- write an SQL script that creates a table called users that:
-- contains the attributes: id, email, and name
-- doesn't fail if table already exists
-- is executable on any database
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    PRIMARY KEY (id)
)

-- write an SQL script that creates a stored procedure called AddBonus
-- that adds a new correction for a student
delimiter //
CREATE PROCEDURE AddBonus
(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
    IF NOT EXISTS (SELECT name FROM projects WHERE projects.name = project_name)
        INSERT INTO projects (name) VALUES (project_name);
    INSERT INTO corrections
    VALUES (user_id, SELECT id FROM projects WHERE name = project_name, score);
END//
delimiter;

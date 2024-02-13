-- write an SQL script that creates a trigger
-- that resets the attribute valid_email
-- only when the email has been changed
CREATE TRIGGER change_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
IF OLD.email != NEW.email
    SET NEW.valid_email = 0;

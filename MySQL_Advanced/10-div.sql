-- write an SQL script that creates a function called SafeDiv
-- that divides (and returns) the first number (a), by the second number (b)
-- or returns 0 if the second number (b) is equal to 0
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    END IF;
    RETURN a / b;
END;
//

DELIMITER ;

-- write an SQL script that creates a function called SafeDiv
-- that divides (and returns) the first number by the second number
-- or returns 0 if the second number is equal to 0
DELIMITER//
CREATE FUNCTION SafeDiv(
    a INT,
    b INT
) RETURNS FLOAT
BEGIN
    DECLARE @c AS INT = 0
    IF b != 0 THEN
        SET @c = (a / b);
    END IF;
    RETURN @c;
END;
//

DELIMITER ;

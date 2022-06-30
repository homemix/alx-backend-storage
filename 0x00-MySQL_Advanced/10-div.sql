--  SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
DELIMITER $$
CREATE FUNCTION SafeDiv(IN a INT, IN b INT)
    RETURNS INT
    DETERMINISTIC
    BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a = a / b;
    END IF;
    END $$
DELIMITER ;
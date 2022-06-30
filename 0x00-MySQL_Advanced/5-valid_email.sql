-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
CREATE TRIGGER reset_valid_email_on_update
    AFTER UPDATE ON users
    FOR EACH ROW
    BEGIN
        UPDATE users
        SET valid_email = 1
        WHERE id = NEW.id;
END;

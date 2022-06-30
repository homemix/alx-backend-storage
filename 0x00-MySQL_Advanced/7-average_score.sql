-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    SET @average_score = (SELECT AVG(score) FROM corrections WHERE user_id = user_id);
    UPDATE users SET average_score = average_score WHERE user_id = user_id;
END $$;
DELIMITER ;
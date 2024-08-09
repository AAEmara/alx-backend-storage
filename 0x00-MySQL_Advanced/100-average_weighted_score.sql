-- A SQL Script that creates a stored procedure
-- `ComputeAverageWeightedScoreForUser` that computes the weighted average
-- score for a student and stores it.
DELIMITER |

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
	DECLARE weighted_avg FLOAT;

	SELECT SUM(score * weight) / SUM(weight) INTO weighted_avg
	FROM corrections AS c
	LEFT JOIN projects AS p
	ON c.project_id = p.id
	WHERE c.user_id = user_id;

	UPDATE users
	SET average_score = weighted_avg
	WHERE users.id = user_id;
END|

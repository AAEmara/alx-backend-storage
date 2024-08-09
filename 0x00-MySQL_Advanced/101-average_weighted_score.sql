-- A SQL Script that creates a stored procedure
-- `ComputeAverageWeightedScoreForUsers` that computes the weighted average
-- score for all students and stores it.
DELIMITER |

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE weighted_avg FLOAT;
	DECLARE user_id INT;
	DECLARE done BOOLEAN DEFAULT false;

	-- Declaring cursor for User ID.
	DECLARE user_cursor CURSOR FOR
	SELECT id
	FROM users;

	-- Declaring NOT FOUND handler for the user_cursor.
	DECLARE CONTINUE HANDLER FOR
	NOT FOUND SET done = true;

	-- Opening the user_cursor.
	OPEN user_cursor;

	users_wavg: LOOP
		FETCH user_cursor INTO user_id;

		IF done THEN
			LEAVE users_wavg;
		END IF;

		-- Calculating the user's weighted average score.
		SELECT SUM(c.score * p.weight) / SUM(p.weight)
		INTO weighted_avg
		FROM corrections AS c
		LEFT JOIN projects AS p
		ON c.project_id = p.id
		WHERE c.user_id = user_id;

		-- Updating the user's weighted average score.
		UPDATE users
		SET average_score = weighted_avg
		WHERE users.id = user_id;
	END LOOP;

	-- Closing the user_cursor.
	CLOSE user_cursor;
END|
 

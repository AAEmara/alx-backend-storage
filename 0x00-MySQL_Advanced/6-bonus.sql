-- Creating a Stored Procedure `AddBonus` that adds a new correction
-- of a student.
DELIMITER |
CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
)

BEGIN
	-- Declared a project_id variable for the Project's ID.
	DECLARE project_id INT;

	-- Querying about if the Project's Name is available or not.
	SELECT id INTO project_id
	FROM projects
	WHERE name = project_name;

	-- If the Project's ID is not available, create a new one and
	-- assign it to the project_id variable.
	IF project_id IS NULL THEN
		INSERT INTO projects (name)
		VALUES (project_name);
		-- LAST_INSERT_ID function that returns the latest
		-- AUTOINCREMENTED id.
		SET project_id = LAST_INSERT_ID();
	END IF;

	-- Creating the new correction.
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, project_id, score);
END|

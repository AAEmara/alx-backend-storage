-- A SQL Script that creates a view `need_meeting` where it lists all students
-- that have a score under 80 and didn't have a `last_meeting` field date value
-- or had a `last_meeting` field value for more than a month.
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE (score < 80 AND 
	(last_meeting IS NULL OR
	 DATEDIFF(CURDATE(), last_meeting) > 30)
);

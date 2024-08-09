-- Create veiw need_meeting
CREATE VIEW need_meeting AS
SELECT name
FROM students -- select name column from students table
WHERE score < 80
  AND (last_meeting IS NULL OR DATEDIFF(CURDATE(), last_meeting) > 30);

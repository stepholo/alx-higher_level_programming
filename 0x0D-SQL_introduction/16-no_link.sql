-- List all records of the table
-- Dont list rows without a name value
-- Result should be listed by descending score
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;

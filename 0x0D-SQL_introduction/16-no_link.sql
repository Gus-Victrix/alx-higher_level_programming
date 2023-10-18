-- Lists all records of the table where name is not empty.
SELECT `score`, `name`, FROM `second_table`
WHERE `name` != ""
ORDER BY `score` desc;

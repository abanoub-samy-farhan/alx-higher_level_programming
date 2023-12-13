-- print a group of data --
SELECT score, COUNT(id) AS number 
FROM second_table
GROUP BY score
ORDER BY number DESC;


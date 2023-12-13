-- File to add the final results --
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month in (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
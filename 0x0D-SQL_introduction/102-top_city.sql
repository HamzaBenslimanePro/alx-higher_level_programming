SELECT city, temperature
FROM Temperatures
WHERE month IN ('July', 'August')
ORDER BY temperature DESC
LIMIT 3;


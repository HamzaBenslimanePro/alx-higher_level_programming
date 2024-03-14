-- Display the top 3 cities with the highest temperature during July and August
SELECT city, temperature
FROM Temperatures
WHERE month IN ('July', 'August')
ORDER BY temperature DESC
LIMIT 3;

SELECT state, MAX(temperature) AS max_temperature
FROM Temperatures
GROUP BY state
ORDER BY state;


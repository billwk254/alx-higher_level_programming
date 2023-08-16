-- Calculate and display average temperature (Fahrenheit) by city
SELECT city, AVG(temp_fahrenheit) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

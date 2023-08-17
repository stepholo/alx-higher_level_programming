-- Displays the max tempreture of each state(Orderd by State name)
SELECT state, MAX(value) AS max_temp
FROM tempretures
GROUP BY state
ORDER BY state;

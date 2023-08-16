-- Lists all genres contained in hbtn_0d_tvshow
-- and displays the number of shows linked to each other
SELECT g.`genre`, COUNT(*) AS `number_of_shows
FROM `tv_genres AS g
INNER JOIN `tv_show_genres` AS s
ON g.`id` = s.`show_id`
GROUP BY g.`name`
ORDER BY `number_of_shows` DESC;

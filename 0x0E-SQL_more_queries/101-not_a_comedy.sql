-- List all genres not linked to the show
SELECT ts.title
FROM tv_shows ts
LEFT JOIN (
	SELECT tsg.show_id
	FROM tv_show_genres tsg
	JOIN tv_genres tg ON tsg.genre_id = tg.id
	WHERE tg.name = "Comedy"
) AS comedy_shows ON ts.id = comedy_shows.show_id
WHERE comedy_shows.show_id IS NULL
ORDER BY ts.title ASC;

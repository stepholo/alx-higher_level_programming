-- List all genres not linked to the show
SELECT tg.name
FROM tv_genres tg
LEFT JOIN (
	SELECT tsg.genre_id
	FROM tv_show_genres tsg
	JOIN tv_shows ts ON tsg.show_id = ts.id
	WHERE ts.title = "Dexter"
) AS linked_genres ON tg.id = linked_genres.genre_id
WHERE linked_genres.genre_id IS NULL
ORDER BY tg.name ASC;

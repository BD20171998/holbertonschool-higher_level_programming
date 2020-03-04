-- script that uses the hbtn_0d_tvshows database to list all genres not linked
-- to the show Dexter
SELECT DISTINCT tv_genres.name AS name
FROM tv_show_genres, tv_genres, tv_shows
WHERE tv_show_genres.show_id = tv_shows.id

AND tv_genres.id = tv_show_genres.genre_id
AND tv_show_genres.genre_id NOT IN
(SELECT tv_show_genres.genre_id FROM tv_shows, tv_show_genres
WHERE tv_shows.title = 'Dexter' AND tv_show_genres.show_id = tv_shows.id)

ORDER BY tv_genres.name ASC;

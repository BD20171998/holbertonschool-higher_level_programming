-- script that lists all shows without the genre Comedy in the database
-- hbtn_0d_tvshows
SELECT DISTINCT tv_shows.title AS title FROM tv_show_genres, tv_genres, tv_shows

WHERE tv_shows.id NOT IN

(SELECT tv_shows.id
FROM tv_genres, tv_shows, tv_show_genres
WHERE tv_genres.name = 'Comedy' AND tv_show_genres.genre_id = tv_genres.id
AND tv_show_genres.show_id = tv_shows.id
)

ORDER BY title ASC;

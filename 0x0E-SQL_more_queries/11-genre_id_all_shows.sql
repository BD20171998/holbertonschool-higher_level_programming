-- Write a script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_genres, tv_shows, tv_show_genres
WHERE (tv_genres.id = tv_show_genres.genre_id OR tv_genres.id IS NULL)
AND tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

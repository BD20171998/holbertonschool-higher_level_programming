-- script that lists all shows contained in hbtn_0d_tvshows that have at
-- least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_genres, tv_shows, tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
AND tv_shows.id = tv_show_genres.show.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

-- script that uses the hbtn_0d_tvshows database to lists all genres of the
-- show Dexter
SELECT tv_genres.name AS NAME FROM tv_genres WHERE tv_shows.title = 'Dexter'
AND tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_genres.name ASC;

-- script that lists all genres from hbtn_0d_tvshows and displays the number of
-- shows linked to each
SELECT tv_genres.names AS genre, COUNT(tv_shows_genres.genre_id)
AS number_of_shows FROM tv_genres, tv_shows_genres
WHERE tv_genres.id = tv_shows_genres.genre_id
ORDER BY number_of_shows DESC;

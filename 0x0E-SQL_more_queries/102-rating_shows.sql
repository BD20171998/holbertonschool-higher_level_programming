-- script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT tv_shows.title AS title, SUM(tv_show_ratings.rate) AS rating
FROM tv_show_ratings, tv_shows

WHERE tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC

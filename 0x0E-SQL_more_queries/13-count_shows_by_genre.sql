-- lists all genres from hbtn_0d_tvshows
-- displays the number of shows linked to each
-- display: <TV Show genre> - <Number of shows linked to this genre>
-- don’t display a genre that doesn’t have any shows linked
-- sorted in descending order by the number of shows linked
SELECT tv_genres.name AS genre, COUNT(DISTINCT tv_show_genres.show_id) AS number_of_shows
FROM tv_genres INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;

-- lists all genres of the show Dexter
    SELECT name
      FROM tv_shows
INNER JOIN  tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
INNER JOIN  tv_genres
        ON tv_genres.id = tv_show_genres.genre_id
     WHERE title = 'Dexter' ORDER BY name;
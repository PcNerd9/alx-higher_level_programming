-- lists all shows contained in a databases
    SELECT ts.title, tsg.genre_id
      FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg
        ON ts.id = tsg.show_id
  ORDER BY ts.title, tsg.genre_id;

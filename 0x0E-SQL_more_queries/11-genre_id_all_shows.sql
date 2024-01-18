-- left join two tables to display it content
   SELECT ts.title, tsg.genre_id
     FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg
       ON ts.id = tsg.show_id
 ORDER BY ts.title, tsg.genre_id;

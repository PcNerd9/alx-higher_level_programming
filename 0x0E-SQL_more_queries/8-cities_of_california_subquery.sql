-- lists all the citiees of california that can be found in the database
SELECT  id name
  FROM 	cities
 WHERE id = (
	SELECT id 
	  FROM states
	 WHERE name = 'California'
	);

UPDATE movies SET Revenue = '$358380478' WHERE Name = 'Spirited Away
       (2001)';
UPDATE movies SET Revenue = '$241145634' WHERE Name ='Howl''s Moving Castle
       (2004)';
UPDATE movies SET Revenue= '$205906593' WHERE Name='Ponyo
       (2008)';
UPDATE movies SET Revenue = '$170333762' WHERE Name='Princess Mononoke
       (1997)';
UPDATE movies SET Revenue='$22261' WHERE Name='My Neighbors the Yamadas
       (1999)';
	   

UPDATE movies SET Revenue='$172766713' WHERE Name='The Boy and the Heron';
UPDATE movies SET Revenue= '$149689984' WHERE Name='The Secret World of Arrietty
       (2010)';
UPDATE movies SET Revenue='$136865366' WHERE Name='The Wind Rises
       (2013)';
UPDATE movies SET Revenue='$68673762' WHERE Name='Tales from Earthsea
       (2006)';
UPDATE movies SET Revenue='$61485364' WHERE Name='From Up on Poppy Hill
       (2011)';

	   
UPDATE movies SET Revenue='$54505827' WHERE Name='The Cat Returns';
UPDATE movies SET Revenue='$30327833' WHERE Name='My Neighbor Totoro
       (1988)';
UPDATE movies SET Revenue='$35012681' WHERE Name='When Marnie Was There
       (2014)';
UPDATE movies SET Revenue='$4420615' WHERE Name='Whisper of the Heart
       (1995)';
UPDATE movies SET Revenue='$1458536' WHERE Name='Porco Rosso';



UPDATE movies SET Revenue='$24751400' WHERE Name='The Tale of The Princess Kaguya
       (2013)';
UPDATE movies SET Revenue='$9010711' WHERE Name='Nausicaä of the Valley of the Wind';
UPDATE movies SET Revenue='$6218229' WHERE Name='Castle in the Sky
       (1986)';
UPDATE movies SET Revenue='$10403278' WHERE Name='Kiki''s Delivery Service
       (1989)';
UPDATE movies SET Revenue='$801143' WHERE Name='Grave of the Fireflies
       (1988)';

	   
	   
UPDATE movies SET Revenue='$608562' WHERE Name='Only Yesterday
       (1991)';
UPDATE movies SET Revenue='$87738' WHERE Name='Ocean Waves
       (1994)';
UPDATE movies SET Revenue='$1279218' WHERE Name='Pom Poko';

/*Updating budgets from the moviedb.org, making it blank where there is no information*/

UPDATE movies SET Budget='$50000000' WHERE Name='The Boy and the Heron';
UPDATE movies SET Budget='$49300000' WHERE Name='The Tale of The Princess Kaguya
       (2013)';
UPDATE movies SET Budget='$34000000' WHERE Name='Ponyo
       (2008)';

/*Updating missing numbers (of 8 movies) with values from wikipedia*/
UPDATE movies SET Budget='10500000' WHERE Name='When Marnie Was There
       (2014)';
UPDATE movies SET Budget='15270000' WHERE Name='My Neighbors the Yamadas
       (1999)';
UPDATE movies SET Budget='20000000' WHERE Name='The Cat Returns';
/*The following 5 movies don't have much information about budget, so setting it to '' for now*/

UPDATE movies SET Budget='' WHERE Name='Pom Poko';
UPDATE movies SET Budget='' WHERE Name='Porco Rosso';
UPDATE movies SET Budget='' WHERE Name='Whisper of the Heart
       (1995)';
UPDATE movies SET Budget='' WHERE Name='Ocean Waves
       (1994)';
UPDATE movies SET Budget='' WHERE Name='Only Yesterday
       (1991)';

/*Analysis Commands: */
SELECT Name, ( CAST(REPLACE(Revenue, '$', '') AS REAL)) AS BoxOffice_Revenue
FROM movies
ORDER BY BoxOffice_Revenue DESC LIMIT 5;

SELECT "Genre 1" AS Genre,  SUM(CAST(REPLACE(Revenue, '$', '') AS REAL)) AS Total_revenue
FROM movies
GROUP BY "Genre 1"  ORDER BY  Total_revenue DESC ;

SELECT Director, SUM( CAST(REPLACE(Revenue, '$', '') AS REAL)) AS Total_revenue
FROM movies
GROUP BY Director ORDER BY Total_revenue DESC;

SELECT Director, AVG( CAST(REPLACE(Revenue, '$', '') AS REAL)) AS Average_Revenue
FROM movies
GROUP BY Director ORDER BY Average_Revenue DESC;

SELECT Name, Director, ( CAST(REPLACE(Revenue, '$', '') AS REAL)) AS BoxOffice_Revenue
FROM movies
ORDER BY BoxOffice_Revenue DESC LIMIT 5;


SELECT Name, ( CAST(REPLACE(Budget, '$', '') AS REAL)) AS Budget, 
( CAST(REPLACE(Revenue, '$', '') AS REAL)) AS BoxOffice_Revenue
from movies WHERE Name NOT IN('')
ORDER BY BoxOffice_Revenue DESC ;

/*Formatting changed for graph to exclude movies where budget data is not provided, 
       so running a different query*/

SELECT Name, ( CAST(REPLACE(Budget, '$', '') AS REAL)) AS Budget, ( CAST(REPLACE(Revenue, '$', '') AS REAL)) AS BoxOffice_Revenue
from movies
WHERE Name NOT IN('Pom Poko', 'Porco Rosso', 'Whisper of the Heart
       (1995)', 'Ocean Waves
       (1994)', 'Only Yesterday
       (1991)')
ORDER BY BoxOffice_Revenue ASC;

/*Average Revenue per Movie by decade*/

SELECT 
    CASE 
        WHEN year >= 1980 AND year < 1990 
			THEN '1980s'
        WHEN year >= 1990 AND year < 2000 
			THEN '1990s'
        WHEN year >= 2000 AND year < 2010 
			THEN '2000s'
        WHEN year >= 2010 AND year < 2020
		THEN '2010s'
		ELSE 'Error'
    END AS Decade,
    AVG(CAST(REPLACE(Revenue, '$', '') AS REAL)) AS Average_BoxOfficeRevenue
FROM movies
WHERE year >= 1980 AND year < 2020
GROUP BY Decade
ORDER BY Decade;








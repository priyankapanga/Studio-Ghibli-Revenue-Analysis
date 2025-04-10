## Copyright 2025 Priyanka Panga
## Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at

###     http://www.apache.org/licenses/LICENSE-2.0

### The original dataset is "Studio Ghibli Dataset" from Kaggle
### (https://www.kaggle.com/datasets/shruthiiiee/studio-ghibli-dataset),
### which is also licensed under the Apache 2.0 License. The dataset has been
### modified by Priyanka Panga to update some column contents, and this modified 
### version is the one used in the project.
###
### The modified dataset 'movies' is uploaded on Kaggle(https://kaggle.com/datasets/ca30befe447b3b37970625788f3794d1ea91677ce8e0a4130c0a1ceea66c2077), and is also
### licensed under the Apache 2.0 License. 
#

## An-Analysis-on-Studio-Ghibli-Films
This project uses SQL to analyse the Studio Ghibli Films, tracking the film's box office revenue across various factors like director, genre, budget, and other important factors. 


### Acknowledgements

- Original dataset by Shruthi on Kaggle.  
  Dataset link: https://www.kaggle.com/datasets/shruthiiiee/studio-ghibli-dataset

   "Studio Ghibli Dataset" available on Kaggle (https://www.kaggle.com/datasets/shruthiiiee/studio-ghibli-dataset), which is licensed under the Apache 2.0 License. The dataset was modified by Priyanka to adjust the contents of certain columns.

- This project uses an updated version of the dataset with adjusted revenue and budget values. The revenue and the budget columns have been updated to reflect the Box Office Numbers from IMDb Pro's Box Office Mojo and Budget Numbers from TMDB respectively. Some budget values(For 'When Marnie Was There', 'My Neighbors the Yamadas', 'The Cat Returns') are from Wikipedia. For the values for which I could not find suffient information(Budget for: 'Pom Poko', 'Porco Rosso', 'Whisper of The Heart', 'Ocean Waves','Only Yesterday'), the slot has been set to '' and left blank. The sources for the information are once again referred to and linked at the bottom of this text. 

### Introduction to Project


The aim of this project is to practise analysis of a given dataset using SQL. I've taken the Studio Ghibli films as an example, specifically focussing on Box Office Revenue as the defining metric of a movie's "success". 

A few examples of the questions explored: 

 -  Which movies were the most succesful?
 -  Which genres were the most succesful?
 -  Which decade had the highest revenue per movie? How did these values change over the decades?
 -  Who directed the top performing movies?
 -  Does a higher budget indicate higher success?

### Introduction to the Dataset

The csv file contained is the updated version. The number and type of columns remain the same from the source dataset.
Relevant columns: 
- 'Name': Movie name
- 'Year': Release year of the movie
- 'Budget': Budget values in USD 
- 'Revenue': Box Office Revenue, raw values in USD. 
- 'Director': Director Name
- 'Genre1': The primary genre of the film

'Budget' and 'Revenue' columns contain TEXT values, '$' followed by the value. This quality of the dataset has been kept the same from the original data set. 

You can choose to download this from kaggle, where it is stored under a different name: 'Studio Ghibli Films' by Priyanka. 


### Tools Used 
 
 **SQLite** : For querying and analysis
 **DB Browser for SQLite**: For visualising database operations
 **Visual Studio Code**: For organising this project and editing the README file. 
 **Google Sheets**: For creating graphs to visualise trends over budget, director, year, etcetera. 

### Steps 
Notes: 
   - I removed the dollar sign (`$`) from revenue values and converted them to numerical format using SQL 
     for the calculations. 
Step 1. Updated revenue and budget values 
Step 2. Extracting various data from the table using data analysis
Step 3. Created charts in Google Sheets using the extracted data
Step 4. Analysing the trends. 
   - Extract various data from the table using data analysis. 
   
### Below are all the SQL update queries I used: 

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

/*Updating missing numbers (of 3 movies) with values from wikipedia*/
UPDATE movies SET Budget='$10500000' WHERE Name='When Marnie Was There
       (2014)';
UPDATE movies SET Budget='$15270000' WHERE Name='My Neighbors the Yamadas
       (1999)';
UPDATE movies SET Budget='$20000000' WHERE Name='The Cat Returns';

/*The following 5 movies don't have much information about budget, so will be leaving them blank*/

UPDATE movies SET Budget='' WHERE Name='Pom Poko';
UPDATE movies SET Budget='' WHERE Name='Porco Rosso';
UPDATE movies SET Budget='' WHERE Name='Whisper of the Heart
       (1995)';
UPDATE movies SET Budget='' WHERE Name='Ocean Waves
       (1994)';
UPDATE movies SET Budget='' WHERE Name='Only Yesterday
       (1991)';

### Conclusions from analysis
 ## Below are the questions, along with the queries used and conclusions drawn from results. The queries in their entirety can be found in the script. 

-  Which movies were the most succesful?
   **Query**
   SELECT Name, ( CAST(REPLACE(Revenue, '$', '') AS REAL)) AS BoxOffice_Revenue
   FROM movies
   ORDER BY BoxOffice_Revenue DESC LIMIT 5;
   **Result**
   ## Studio Ghibli Box Office Revenue

| Name                               | Box Office Revenue (USD)   |
|------------------------------------|----------------------------|
| Spirited Away (2001)               | $358,380,478.0             |
| Howl's Moving Castle (2004)        | $241,145,634.0             |
| Ponyo (2008)                       | $205,906,593.0             |
| The Boy and the Heron              | $172,766,713.0             |
| Princess Mononoke (1997)           | $170,333,762.0             |

- Which genres were the most succesful( highest box office revenue)

   **Query**
   SELECT "Genre 1" AS Genre,  SUM(CAST(REPLACE(Revenue, '$', '') AS REAL)) AS Total_revenue
   FROM movies
   GROUP BY "Genre 1"  ORDER BY  Total_revenue DESC ;
   
   **Result**
| Genre            | Total Box Office Revenue |
|------------------|--------------------------|
| Animation	     | 770553875.0              |
| Fantasy	     | 593930164.0              |
| Adventure	     | 241347747.0              |
| Drama	     | 136865366.0              |
| Family	     | 1458536.0                |

  
 -  Who directed the top performing movies?

    **Query**
    SELECT Director, SUM( CAST(REPLACE(Revenue, '$', '') AS REAL)) AS Total_revenue
    FROM movies
    GROUP BY Director ORDER BY Total_revenue DESC;

    **Results**

| Director	                | Total_revenue |
|-----------------------------|---------------|
|  Hayao Miyazaki	         |  1342817133.0 |
|  Hiromasa Yonebayashi	  |  184702665.0  |
|  Goro Miyazaki	         |  130159126.0  |
|  Hiroyuki Morita	         |  54505827.0   |
|  Isao Takahata	         |  27462584.0   |
|  Yoshifumi Kondo	         |  4420615.0    |
|  Tomomi Mochizuki	         |  87738.0      |


 ## Some more deeper analysis. 
 - Does a higher budget indicate higher box office success?
    
    To understand this, I first needed values of the budget along with the values of the box office revenue. I will be using a table, but ommitting the movies that do not have a budget value, so that our conclusions can be more accurate.
    **Query**
    SELECT Name, ( CAST(REPLACE(Budget, '$', '') AS REAL)) AS Budget, ( CAST(REPLACE(Revenue, '$', '') AS REAL)) AS BoxOffice_Revenue
    from movies 
    WHERE Name NOT IN('Ocean Waves
       (1994)', 'Only Yesterday
       (1991)','Whisper of the Heart
       (1995)', 'Pom Poko' , 'Porco Rosso');
    **Result**
   
   When graphed, there seems to be direct relation between budget and Box Office Revenue. There were only two outliers of the movies graphed. 
   
   The Tale of Princess Kaguya: Had a much higher budget than the box office revenue. This is one of the most expensive studio ghibli films, having a budget of $49,300,000 .This budget is only topped by The Boy and the Heron, the recent release of 2023. Despite its budget, it could not perform more than its budget. Perhaps the reason could lie in the differentiating factors between this movie and the other films from the Studio. It was animated using watercolor-like style, and a slower, thoughtful pace. 


   My Neighbour Totoro: The Budget exceeded the Box Office Revenue probably because of the limited intitial release. After this initial period, it has since amassed enormous acclaim and revenue, and makes up for its initial days. It is now one of the most well-known and succesful Studio Ghibli Movies.The graphs can be found in the 'Images' folder, titled 'Budget and BoxOffice_Revenue' and 'Budget and BoxOffice_Revenue (2)'.


-  Which decade had the highest revenue per movie? How did these values change over the decades?
**Query**
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

**Results**

The movies in the 2000's had the highest average movie revenue by a lot, followed by the 2010's, then the 1990's, then the 1980's. 

2000's performance is because of breakthrough successes like Howl's Moving Castle, Spirited Away, and Ponyo, which are the top three box office performing movies from Studio Ghibli. But it is important to note 2010's also had successes like The Secret World of Arrietty and The Wind Rises, and it still had a much higher average revenue than the 1990's and the 1980's. 

Information about the 2020's is still limited, but it looks promising as the film that was released in 2023: The Boy and the Heron, is the fourth highest Box Office Performing movie of the Studio, amassing a $172,766,713 revenue. 

After the 2000's, the films performed much better than before. This is perhaps because of the exposure to international audiences. The increase in popularity of Japanese films and animations have increased, providing a larger audience for the newer releases. 

**Analysis Complete**


### Future Work

1. **Adjust for Inflation**: Analyze revenues in inflation-adjusted terms for a fair comparison.
2. **Explore Movie Count**: Examine whether fewer releases in the 2010s contributed to the revenue decline.
3. **Global Market Influence**: Investigate how Ghibli's expansion to international markets impacted revenues.
4. **Adjust for Impact**: Using BoxOffice Revenue is an imperfect metric of success. For example, My Neighbour Totoro, had lesser Box Office than its budget, but now it has become one of the most iconic films, in the era of streaming and global audience. This should be accounted for in the future. 

### Files in Repository

- **`SQL_Script.sql`**: This file contains the SQL scripts for data preparation and analysis, containing the queries used. 
- **`Images/`**: Folder containing exported charts from Google Sheets.
- **'movies.csv/'**: Updated database by using update queries listed near the top of this document. This is the database used by the project, and this is licensed under the Apache 2.0 License. All credits can be found at the top-most and bottom-most parts of this document. Can download from here as well: 
  Original Database(which is the version before Priyanka's edits/updates) is by Shruthi from Kaggle
                     (https://www.kaggle.com/datasets/shruthiiiee/studio-ghibli-dataset)
                     which is also licensed under the Apache 2.0 License.
- **studio_ghibli.db'**: NOTE: This has been taken out from the depository, but you will need to create one
 			 to run the commands.
  			 Database created for use in VSCode, SQLite, and DB Browser for SQLite. 
- **`README.md`**: This document.

### 
Sources for changes to 'Budget' and 'Revenue': 
Revenue numbers from IMDb Pro's Box Office Mojo. 
Link: https://www.boxofficemojo.com/?ref_=bo_nb_tt_mojologo 
Budget numbers from TMD 
Link: https://www.themoviedb.org/list/4309-the-studio-ghibli-collection
   except for 'When Marnie Was There', 'My Neighbors the Yamadas', 'The Cat Returns', which is from Wikipedia.
   Link: https://www.wikipedia.org

---

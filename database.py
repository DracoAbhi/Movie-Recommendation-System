import mysql.connector as connector;
import pandas as pd;

conn = connector.connect(host="127.0.0.1",
                        port="3306",
                        user="root",
                        password="",
                        database="moviesdb")

cursor = conn.cursor()

dbQuery = "SELECT * from imdb_top_1000"
cursor.execute(dbQuery)
rs = cursor.fetchall()
db = pd.DataFrame(rs)

#Query for fetching Action Genre Movies
actionQuery = "SELECT Series_Title,Poster_Link,Overview from imdb_top_1000 where Genre LIKE '%Action%' and(IMDB_Rating > (SELECT AVG(IMDB_Rating) from imdb_top_1000) and no_of_votes > (SELECT AVG(no_of_votes) from imdb_top_1000)) ORDER BY Meta_score DESC"
cursor.execute(actionQuery)
rs = cursor.fetchall()
actionList = []
actionPosterList = []
actionMovieDesc = []

for movie in rs :
    actionList.append(movie[0])
    actionPosterList.append(movie[1])
    actionMovieDesc.append(movie[2])

#Query for fetching Romance Genre Movies
romanceQuery = "SELECT Series_Title,Poster_Link,Overview from imdb_top_1000 where Genre LIKE '%Romance%' and(IMDB_Rating > (SELECT AVG(IMDB_Rating) from imdb_top_1000) and no_of_votes > (SELECT AVG(no_of_votes) from imdb_top_1000)) ORDER BY Meta_score DESC"
cursor.execute(romanceQuery)
rs = cursor.fetchall()
romanceList = []
romancePosterList = []
romanceMovieDesc = []

for movie in rs :
    romanceList.append(movie[0])
    romancePosterList.append(movie[1])
    romanceMovieDesc.append(movie[2])

#Query for fetching Drama Genre Movies
dramaQuery = "SELECT Series_Title,Poster_Link, Overview from imdb_top_1000 where Genre LIKE '%Drama%' and(IMDB_Rating > (SELECT AVG(IMDB_Rating) from imdb_top_1000) and no_of_votes > (SELECT AVG(no_of_votes) from imdb_top_1000)) ORDER BY Meta_score DESC"
cursor.execute(dramaQuery)
rs = cursor.fetchall()
dramaList = []
dramaPosterList = []
dramaMovieDesc = []

for movie in rs :
    dramaList.append(movie[0])
    dramaPosterList.append(movie[1])
    dramaMovieDesc.append(movie[2])

#Query for fetching Crime Genre Movies
crimeQuery = "SELECT Series_Title,Poster_Link,Overview from imdb_top_1000 where Genre LIKE '%Crime%' and(IMDB_Rating > (SELECT AVG(IMDB_Rating) from imdb_top_1000) and no_of_votes > (SELECT AVG(no_of_votes) from imdb_top_1000)) ORDER BY Meta_score DESC"
cursor.execute(crimeQuery)
rs = cursor.fetchall()
crimeList = []
crimePosterList = []
crimeMovieDesc = []

for movie in rs :
    crimeList.append(movie[0])
    crimePosterList.append(movie[1])
    crimeMovieDesc.append(movie[2])

#Query for fetching Sci-Fi Genre Movies
scienceQuery = "SELECT Series_Title,Poster_Link,Overview from imdb_top_1000 where Genre LIKE '%Sci-Fi%' and(IMDB_Rating > (SELECT AVG(IMDB_Rating) from imdb_top_1000) and no_of_votes > (SELECT AVG(no_of_votes) from imdb_top_1000)) ORDER BY Meta_score DESC"
cursor.execute(scienceQuery)
rs = cursor.fetchall()
scienceList = []
sciencePosterList = []
scienceMovieDesc = []

for movie in rs :
    scienceList.append(movie[0])
    sciencePosterList.append(movie[1])
    scienceMovieDesc.append(movie[2])

#Query for fetching Adventure Genre Movies
advQuery = "SELECT Series_Title,Poster_Link,Overview from imdb_top_1000 where Genre LIKE '%Adventure%' and(IMDB_Rating > (SELECT AVG(IMDB_Rating) from imdb_top_1000) and no_of_votes > (SELECT AVG(no_of_votes) from imdb_top_1000)) ORDER BY Meta_score DESC"
cursor.execute(advQuery)
rs = cursor.fetchall()
advList = []
advPosterList = []
advMovieDesc = []

for movie in rs :
    advList.append(movie[0])
    advPosterList.append(movie[1])
    advMovieDesc.append(movie[2])


#Query for fetching Fantasy Genre Movies
fanQuery = "SELECT Series_Title,Poster_Link,Overview from imdb_top_1000 where Genre LIKE '%Fantasy%' and(IMDB_Rating > (SELECT AVG(IMDB_Rating) from imdb_top_1000) and no_of_votes > (SELECT AVG(no_of_votes) from imdb_top_1000)) ORDER BY Meta_score DESC"
cursor.execute(fanQuery)
rs = cursor.fetchall()
fanList = []
fanPosterList = []
fanMovieDesc = []

for movie in rs :
    fanList.append(movie[0])
    fanPosterList.append(movie[1])
    fanMovieDesc.append(movie[2])


#Query for fetching War Genre Movies
warQuery = "SELECT Series_Title,Poster_Link,Overview from imdb_top_1000 where Genre LIKE '%War%' and(IMDB_Rating > (SELECT AVG(IMDB_Rating) from imdb_top_1000) and no_of_votes > (SELECT AVG(no_of_votes) from imdb_top_1000)) ORDER BY Meta_score DESC"
cursor.execute(warQuery)
rs = cursor.fetchall()
warList = []
warPosterList = []
warMovieDesc = []

for movie in rs :
    warList.append(movie[0])
    warPosterList.append(movie[1])
    warMovieDesc.append(movie[2])


#Query for fetching Family Genre Movies
familyQuery = "SELECT Series_Title,Poster_Link,Overview from imdb_top_1000 where Genre LIKE '%Family%' and(IMDB_Rating > (SELECT AVG(IMDB_Rating) from imdb_top_1000) and no_of_votes > (SELECT AVG(no_of_votes) from imdb_top_1000)) ORDER BY Meta_score DESC"
cursor.execute(familyQuery)
rs = cursor.fetchall()
familyList = []
familyPosterList = []
familyMovieDesc = []

for movie in rs :
    familyList.append(movie[0])
    familyPosterList.append(movie[1])
    familyMovieDesc.append(movie[2])

#Query for fetching Comedy Genre Movies
comQuery = "SELECT Series_Title,Poster_Link,Overview from imdb_top_1000 where Genre LIKE '%Comedy%' and(IMDB_Rating > (SELECT AVG(IMDB_Rating) from imdb_top_1000) and no_of_votes > (SELECT AVG(no_of_votes) from imdb_top_1000)) ORDER BY Meta_score DESC"
cursor.execute(comQuery)
rs = cursor.fetchall()
comList = []
comPosterList = []
comMovieDesc = []

for movie in rs :
    comList.append(movie[0])
    comPosterList.append(movie[1])
    comMovieDesc.append(movie[2])

cursor.close()
conn.close()
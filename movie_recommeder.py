import difflib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cosine
from database import *

#Helper Functions
def get_title_from_index(index) : 
    return movies[movies.index == index][1].values[0]

def get_index_from_title(title) : 
    try :
        title_list = movies[1].tolist()
        common_matches = difflib.get_close_matches(title, title_list, 1)
        similar_titles = common_matches[0]
        return movies[movies[1] == similar_titles][16].values[0]
    except :
        print("Movie Not found ")

def get_ratings_from_index(index) :
    return movies[movies.index == index][6].values[0]

def get_genres_from_index(index) :
    return movies[movies.index == index][5].values[0]

def get_directors_from_index(index) :
    return movies[movies.index == index][9].values[0]

def get_posters_from_index(index) :
    return movies[movies.index == index][0].values[0]


#Fetching the movies Dataframe from the database file
movies = db

#selecting specific features from the dataset
feature_names = [5,9,10,11]

for feature in feature_names :
    movies[feature] = movies[feature].fillna('')

#Creating a new dataframe to combine all these features
def combine_data(row) :
    return( row[5] + " " + row[9] + " " + row[10] + " " + row[11])

movies[17] = movies.apply(combine_data,axis=1)

#Suggesting similar Movies
def fetch_Recommendations(user_pref,choice) :
    
    #Creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(movies[17])

    #Calculating the cosine similarity
    similarity = cosine(count_matrix)

    #Calling helper function to fetch movie index based on the title entered
    movie_index = get_index_from_title(user_pref)

    #Generating a list of similar movies using cosine similarity
    similar_movies = list(enumerate(similarity[movie_index]))

    #Sorting the values from high to low similarity (descending order)
    recommendation = sorted(similar_movies , key = lambda x:x[1] , reverse=True)
    
    i=0
    movies_recommended = []
    movies_genres = []
    movies_ratings = []
    movies_directors = []
    movies_posters = []


    #Printing the recommendations
    for movie in recommendation : 
        movies_recommended.append(get_title_from_index(movie[0]))
        movies_genres.append(get_genres_from_index(movie[0]))
        movies_ratings.append(get_ratings_from_index(movie[0]))
        movies_directors.append(get_directors_from_index(movie[0]))
        movies_posters.append(get_posters_from_index(movie[0]))

        i+=1
        if(i>choice) :
            break
    return movies_recommended, movies_genres, movies_ratings, movies_directors, movies_posters


#Top rated movies based on genre
def list_top_movies(genre,num) :
    topMovies = []
    topMoviesPoster = []
    topMoviesDesc = []
    
    if(genre=="Action") :
        topMovies = actionList
        topMoviesPoster = actionPosterList
        topMoviesDesc = actionMovieDesc
    
    elif(genre=="Romance") :
        topMovies = romanceList
        topMoviesPoster = romancePosterList
        topMoviesDesc = romanceMovieDesc
    
    elif(genre=="Drama") :
        topMovies = dramaList
        topMoviesPoster = dramaPosterList
        topMoviesDesc = dramaMovieDesc
    
    elif(genre=="Crime") :
        topMovies = crimeList
        topMoviesPoster = crimePosterList
        topMoviesDesc = crimeMovieDesc
    
    elif(genre=="Sci-Fi") :
        topMovies = scienceList
        topMoviesPoster = sciencePosterList
        topMoviesDesc = scienceMovieDesc
    
    elif(genre=="Adventure") :
        topMovies = advList
        topMoviesPoster = advPosterList
        topMoviesDesc = advMovieDesc
    
    elif(genre=="Fantasy") :
        topMovies = fanList
        topMoviesPoster = fanPosterList
        topMoviesDesc = fanMovieDesc
    
    elif(genre=="War") :
        topMovies = warList
        topMoviesPoster = warPosterList
        topMoviesDesc = warMovieDesc
    
    elif(genre=="Family") :
        topMovies = familyList
        topMoviesPoster = familyPosterList
        topMoviesDesc = familyMovieDesc
    
    elif(genre=="Comedy") :
        topMovies = comList
        topMoviesPoster = comPosterList
        topMoviesDesc = comMovieDesc
    
    movieList = []
    posterList = []
    descList = []
    i=0
    j=0
    k=0

    for movie in topMovies :
        movieList.append(movie)
        i = i+1
        if(i>(num-1)) :
            break
    
    for movie in topMoviesPoster :
        posterList.append(movie)
        j = j+1
        if(j>(num-1)) :
            break
    
    for movie in topMoviesDesc :
        descList.append(movie)
        k = k+1
        if(k>(num-1)) :
            break
    
    return movieList,posterList,descList

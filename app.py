from flask import Flask, render_template, request
from movie_recommeder import list_top_movies,fetch_Recommendations

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def show_index_html():
    return render_template('index.html', headings = {}, data = {})

@app.route('/suggestions', methods = ['POST'])
def get_data_from_html():
        moviename = request.form['moviename']
        moviechoice = request.form['moviechoice']
        
        #typecasting to int because we received a string from the html form
        moviechoice = int(moviechoice) 

        #Calling the function and receiving the values 
        movies,genres,ratings,directors,posterList = fetch_Recommendations(moviename,moviechoice)
        return render_template('index.html', movies = movies , genres = genres, ratings = ratings, directors = directors, posterList=posterList)

@app.route('/topMovies' , methods=['POST'])
def get_top_movies() :
    topmoviegenre = request.form['topmovie']
    topmoviechoice = request.form['topmovienum']

    topmoviechoice = int(topmoviechoice)

    movietitles,posters,summary = list_top_movies(topmoviegenre,topmoviechoice)
    return render_template('index.html', movietitles=movietitles , posters=posters , summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, Response
import json

app = Flask(__name__)

movie = {
    "1" : { "name": "stargate", "release_date": "1999" },
    "2" : { "name": "theholidays", "release_date": "2004"},
    "3" : { "name": "RRR", "release_date": "2022"}
}
 
@app.route("/hello")
def hello_message():
    return "Hello world"

@app.route("/movie")
def listmovies():
    return movie

@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    return movie[movie_id]

@app.route("/movie/delete/<movie_id>")
def del_movie(movie_id):
    del movie[movie_id]
    return "Deleted"


@app.route("/movie/add", methods=['POST'])
def add_movie():
    # step1: get the last primary key
    # step2: increment the last primary key
    #step3 : add the data to the new primarykey
    last_key = len(movie)
    last_key += 1
    request_data = request.get_json()
    new_entry_movie = { str(last_key) : request_data } #this is where the POST data is stored
    movie.update(new_entry_movie)
    return "the movie was added succesful"
    
if __name__ == "__main__":
   app.run(host="127.0.0.1")
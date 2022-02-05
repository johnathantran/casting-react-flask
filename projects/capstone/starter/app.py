from flask import Flask, render_template, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)

  return app

APP = create_app()

# import models after db is instantiated
from models import Movie, Actor


@APP.route('/')
def index():

  return render_template('index.html')

# GET: movies
@APP.route('/movies')
def movies():
  # TODO: replace with real venues data.
  #       num_upcoming_shows should be aggregated based on number of upcoming shows per venue.

  movie = Movie.query.first()
  return 'Movie: ' + movie.title + movie.releaseDate

#GET: actors
@APP.route('/actors')
def actors():

  actor = Actor.query.first()
  return 'Actor: ' + actor.name + actor.age

if __name__ == '__main__':
  APP.run(debug=True)
  #APP.run(host='0.0.0.0', port=8080, debug=True)
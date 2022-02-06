from venv import create
from flask import Flask, render_template, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie, Actor, setup_db

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app)
  
  @app.route('/')
  def index():
    return render_template('index.html')


  # GET: get all movies
  @app.route('/movies')
  def movies():

    movies = Movie.query.all()
    return jsonify({
      'success': True,
      'categories': [movie.format() for movie in movies]
    })

  #GET: get all actors
  @app.route('/actors')
  def actors():

    actors = Actor.query.all()
    return jsonify({
      'success': True,
      'categories': [actor.format() for actor in actors]
    })

    # POST: add a movie
  @app.route('/movies', methods=['POST'])
  def movies():

    body = request.get_json()
    title = body.get("title", None)
    releasedate = body.get("releasedate", None)

    movie = Movie(
      title=title,
      releasedate=releasedate
    )
    movie.insert()

    return jsonify(
        {
            "success": True,
            "created": movie.id + ": " + movie.title,
            "total_movies": len(Movie.query.all()),
        }
      )


  # POST: add an actor
  @app.route('/actors', methods=['POST'])
  def actors():

    return
    

  return app

if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)
  #APP.run(host='0.0.0.0', port=8080, debug=True)




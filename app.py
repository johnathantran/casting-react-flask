from venv import create
from flask import Flask, render_template, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie, Actor, setup_db, db
from auth import AuthError, requires_auth
from flask_migrate import Migrate

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  migrate = Migrate(app, db)
  setup_db(app)

  # home page
  @app.route('/')
  def index():
    return render_template('index.html')

  # GET: get all movies
  @app.route('/movies', endpoint='getMovies')
  def movies():
    try:
      movies = Movie.query.all()
      current_movies = [movie.format() for movie in movies]
      return jsonify(
        {
            "success": True,
            "movies": current_movies,
        }
      )
    except Exception as e:
        abort(404)

  # POST: post a new movie
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def movies(payload):

    try:
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
            "movies": movie.format(),
        }
      )
    except Exception as e:
        abort(422)
  

  # GET: get all actors
  @app.route('/actors', endpoint='getActors')
  def actors():
    try:
      actors = Actor.query.all()
      current_actors = [actor.format() for actor in actors]
      return jsonify(
        {
            "success": True,
            "actors": current_actors,
        }
      )
    except Exception as e:
        abort(404)

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def actors(payload):

    try:
      body = request.get_json()
      name = body.get("name", None)
      gender = body.get("gender", None)
      age = body.get("age", None)

      actor = Actor(
        name=name,
        age=age,
        gender=gender
      )
      actor.insert()

      return jsonify(
        {
            "success": True,
            "actors": actor.format(),
        }
      )
    
    except Exception as e:
        print("this is an error: \n\n\n")
        print(e)
        abort(422)


  # DELETE: delete a movie
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(payload, movie_id):

      try:
          movie = Movie.query.filter(
              Movie.id == movie_id).one_or_none()
          movie.delete()

          return jsonify({
              'success': True,
              'deleted': movie_id,
          })

      except Exception as e:
          print(e)
          abort(422)

  # DELETE: delete an actor
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(payload, actor_id):

      try:
          actor = Actor.query.filter(
              Actor.id == actor_id).one_or_none()
          actor.delete()

          print("Actor is: ")
          print(actor_id)

          return jsonify({
              'success': True,
              'deleted': actor_id,
          })

      except Exception as e:
          print(e)
          abort(422)
  
  # PATCH: update actor info
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def edit_actor(payload, actor_id):

      try:
          body = request.get_json()
          name = body.get("name", None)
          gender = body.get("gender", None)
          age = body.get("age", None)

          actor = Actor.query.filter(
              Actor.id == actor_id).one_or_none()

          actor.name = name
          actor.gender = gender
          actor.age = age
          actor.update()

          return jsonify({
              'success': True,
              'updated': actor_id,
          })

      except Exception as e:
          print(e)
          abort(422)
  
  # PATCH: update movie info
  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def edit_movie(payload, movie_id):

      try:
          body = request.get_json()
          title = body.get("title", None)
          releasedate = body.get("releasedate", None)

          movie = Movie.query.filter(
              Movie.id == movie_id).one_or_none()

          movie.title = title
          movie.releasedate = releasedate

          movie.update()

          return jsonify({
              'success': True,
              'updated': movie_id,
          })

      except Exception as e:
          print(e)
          abort(422)


  @app.errorhandler(400)
  def bad_request(e):
      return jsonify({
          "success": False,
          "error": 400,
          "message": "Bad request"
      }), 400

  @app.errorhandler(404)
  def page_not_found(e):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "Resource not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(e):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "Unprocessable"
      }), 422

  @app.errorhandler(500)
  def internal_server_error(e):

      print('error: ')
      print(e)

      return jsonify({
          "success": False,
          "error": 500,
          "message": "Internal server error"
      }), 500

  return app

if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)
  #APP.run(host='0.0.0.0', port=8080, debug=True)




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
  
  # home page
  @app.route('/')
  def index():
    return render_template('index.html')

  # GET: get all movies
  # POST: post a new movie
  @app.route('/movies', methods=['GET', 'POST'])
  def movies():

      # handle the POST request
      if request.method == 'POST':
          title = request.form.get('title')
          releasedate = request.form.get('releasedate')

          movie = Movie(
            title=title,
            releasedate=releasedate
          )

          movie.insert()
          return '''
            <h1>The movie {} released on {} is now listed in our system!</h1>
            <a href="/movies">Return to Movies page</a>'''.format(title, releasedate)

      # otherwise handle the GET request
      else:
        movies = Movie.query.all()
        return render_template('movies.html', movies=movies)

  # GET: get all actors
  # POST: post a new actor
  @app.route('/actors', methods=['GET', 'POST'])
  def actors():
    print('endpoint hit')
    # handle the POST request
    if request.method == 'POST':

      print("\n\n POST METHOD: \n\n\n")

      #name = request.form.get('name')
      ##gender = request.form.get('gender')
      print(request)
      body = request.get_json()
      print(body)

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

    # otherwise handle the GET request
    else:  
      actors = Actor.query.all()
      current_actors = [actor.format() for actor in actors]
      return jsonify(
        {
            "success": True,
            "actors": current_actors,
        }
      )



  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  def delete_movie(movie_id):

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

  # @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  # def delete_actor(actor_id):

  #     try:
  #         actor = Movie.query.filter(
  #             Actor.id == actor_id).one_or_none()
  #         actor.delete()

  #         return jsonify({
  #             'success': True,
  #             'deleted': actor_id,
  #         })

  #     except Exception as e:
  #         print(e)
  #         abort(422)
  
  
  @app.route('/actors/<int:actor_id>/edit', methods=['PATCH'])
  def edit_actor(actor_id):

      try:
          actor = Movie.query.filter(
              Actor.id == actor_id).one_or_none()

          actor.title="Zootopia"

          actor.update()

          return jsonify({
              'success': True,
              'deleted': actor_id,
          })

      except Exception as e:
          print(e)
          abort(422)

  return app

if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)
  #APP.run(host='0.0.0.0', port=8080, debug=True)




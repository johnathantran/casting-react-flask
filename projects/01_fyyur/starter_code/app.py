#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import dateutil.parser
import babel
from flask import render_template, request, flash, redirect, url_for
from flask_moment import Moment
import logging
from logging import Formatter, FileHandler
#from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
import sys
from datetime import datetime

from models import db, app, Venue, Artist, Show

moment = Moment(app)
app.config.from_object('config')

# TODO: connect to a local postgresql database
migrate = Migrate(app, db)

# import models after db is instantiated
from models import Venue, Artist, Show

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_upcoming_shows should be aggregated based on number of upcoming shows per venue.
  
  # initialize with city names

  dbQuery = db.session.query(Venue).all()
  locations = []

  for venue in dbQuery:
    locationExists = False

    for location in locations:
      
      if venue.city == location['city'] and venue.state == location['state']:
        locationExists = True
        location['venues'].append(
          {
            "id": venue.id,
            "name": venue.name,
            "num_upcoming_shows": 0
          }
        )
        break
    
    if not locationExists:
      locations.append({
      "city": venue.city,
      "state": venue.state,
      "venues": [{
        "id": venue.id,
        "name": venue.name,
        "num_upcoming_shows": 0
      }]
      })
  
  return render_template('pages/venues.html', areas=locations)

@app.route('/venues/search', methods=['POST'])
def search_venues():

  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"

  search_term = request.form['search_term']
  search = "%{}%".format(search_term)
  query = db.session.query(Venue).filter(Venue.name.ilike(search)).all()

  venues = []
  for venue in query:
    print(venue)

    venues.append({
      "id": venue.id,
      "name": venue.name,
      #"num_upcoming_shows": 0,
    })

  response={
    "count": len(query),
    "data": venues
  }
  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  
  try:
    venue = db.session.query(Venue).get(venue_id)
    pastShows = []
    upcomingShows = []

    for show in venue.shows:
      # determine past and upcoming shows
      formattedDate = dateutil.parser.parse(show.start_time)
      now = datetime.now()

      if formattedDate < now:
          pastShows.append(show)
      else:
          upcomingShows.append(show)
    
    genres = list(venue.genres.translate(str.maketrans({'{':'','}':''})).split(","))
    data = {
      "id": venue.id,
      "name": venue.name,
      "genres": genres,
      "address": venue.address,
      "city": venue.city,
      "state": venue.state,
      "phone": venue.phone,
      "website_link": venue.website_link,
      "facebook_link": venue.facebook_link,
      "seeking_talent": venue.seeking_talent,
      "seeking_description": venue.seeking_description,
      "image_link": venue.image_link,
      "past_shows": pastShows,
      "upcoming_shows": upcomingShows,
      "past_shows_count": len(pastShows),
      "upcoming_shows_count": len(upcomingShows),
    }
    
  except:
    print(sys.exc_info())
  finally:
    db.session.close()

  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  form = VenueForm()
  error = False

  try:
    venue = Venue(
      name=form.name.data,
      city=form.city.data,
      state=form.state.data,
      address=form.address.data,
      phone=form.phone.data,
      image_link=form.image_link.data,
      facebook_link=form.facebook_link.data,
      seeking_talent=form.seeking_talent.data,
      genres=form.genres.data,
      website_link=form.website_link.data,
      seeking_description=form.seeking_description.data
    )

    db.session.add(venue)
    db.session.commit()
    # on successful db insert, flash success
    flash('Venue ' + request.form['name'] + ' was successfully listed!')

  except:
    error = True
    db.session.rollback()
    print(form.data)
    print(sys.exc_info())

  finally:
    db.session.close()
    
  if error:
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
    flash('An error occurred. Venue ' + form.name.data + ' could not be listed.')

  # TODO: modify data to be the data object returned from db insertion
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.route('/venues/delete/<venue_id>', methods=['POST'])
def delete_venue(venue_id):

  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  error = False
  try:
    shows = db.session.query(Show).filter(Show.venue_id == venue_id)
    shows.delete()
    db.session.execute('delete from "Venue" where id =' + str(venue_id))
    
    db.session.commit()
    flash('Venue ' + str(venue_id) + ' and any shows at this venue were successfully deleted.')

  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())

  finally:
    db.session.close()
    if error:
      flash('An error occurred. Venue ' + str(venue_id) + ' could not be deleted.')

    # redirect to index not working, implemented in AJAX promise instead
    return redirect(url_for('index'))

  
  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage


#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database

  dbQuery = db.session.query(Artist).all()

  data = []
  for artist in dbQuery:
    data.append({
        "id": artist.id,
        "name": artist.name,
      })

  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".

  search_term = request.form['search_term']
  search = "%{}%".format(search_term)
  query = db.session.query(Artist).filter(Artist.name.ilike(search)).all()

  artists = []
  for artist in query:

    artists.append({
      "id": artist.id,
      "name": artist.name,
      #"num_upcoming_shows": 0,
    })

  response={
    "count": len(query),
    "data": artists
  }
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  # TODO: replace with real artist data from the artist table, using artist_id

  try:
    artist = db.session.query(Artist).get(artist_id)
    pastShows = []
    upcomingShows = []

    for show in artist.shows:

      # determine past and upcoming shows
      formattedDate = dateutil.parser.parse(show.start_time)
      now = datetime.now()

      if formattedDate < now:
          pastShows.append(show)
      else:
          upcomingShows.append(show)

    genres = list(artist.genres.translate(str.maketrans({'{':'','}':''})).split(","))
    data = {
      "id": artist.id,
      "name": artist.name,
      "genres": genres,
      "city": artist.city,
      "state": artist.state,
      "phone": artist.phone,
      "website": artist.website_link,
      "facebook_link": artist.facebook_link,
      "seeking_venue": artist.seeking_venue,
      "seeking_description": artist.seeking_description,
      "image_link": artist.image_link,
      "past_shows": pastShows,
      "upcoming_shows": upcomingShows,
      "past_shows_count": len(pastShows),
      "upcoming_shows_count": len(upcomingShows)
    }
  except:
    print(sys.exc_info())
  finally:
    db.session.close()

  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):

  form = ArtistForm()
  artist = db.session.query(Artist).get(artist_id)
  genres = list(artist.genres.translate(str.maketrans({'{':'','}':''})).split(","))

  artistData = {
    "id": artist.id,
    "name": artist.name,
    "genres": genres,
    "city": artist.city,
    "state": artist.state,
    "phone": artist.phone,
    "website": artist.website_link,
    "facebook_link": artist.facebook_link,
    "seeking_venue": artist.seeking_venue,
    "seeking_description": artist.seeking_description,
    "image_link": artist.image_link
  }

  form.name.data = artist.name
  form.genres.data = genres
  form.city.data = artist.city
  form.state.data = artist.state
  form.phone.data = artist.phone
  form.website_link.data = artist.website_link
  form.facebook_link.data = artist.facebook_link
  form.seeking_venue.data = artist.seeking_venue
  form.seeking_description.data = artist.seeking_description
  form.image_link.data = artist.image_link

  db.session.close()

  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artistData)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes

  form = ArtistForm()
  artist = {
    "name": form.name.data,
    "genres": form.genres.data,
    "city": form.city.data,
    "state": form.state.data,
    "phone": form.phone.data,
    "website_link": form.website_link.data,
    "facebook_link": form.facebook_link.data,
    "seeking_venue": form.seeking_venue.data,
    "seeking_description": form.seeking_description.data,
    "image_link": form.image_link.data
  }

  try:
    db.session.query(Artist).filter(Artist.id == artist_id).update(artist)
    db.session.commit()

  except:
    print("Error!")
    db.session.rollback()
    print(sys.exc_info())

  finally:
    db.session.close()

  return redirect(url_for('show_artist', artist_id=artist_id))


@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):

  form = VenueForm()
  venue = db.session.query(Venue).get(venue_id)
  genres = list(venue.genres.translate(str.maketrans({'{':'','}':''})).split(","))

  venueData={
    "id": venue.id,
    "name": venue.name,
    "genres": genres,
    "address": venue.address,
    "city": venue.city,
    "state": venue.state,
    "phone": venue.phone,
    "website": venue.website_link,
    "facebook_link": venue.facebook_link,
    "seeking_talent": venue.seeking_talent,
    "seeking_description": venue.seeking_description,
    "image_link": venue.image_link
  }

  form.name.data = venue.name
  form.genres.data = genres
  form.address.data = venue.address
  form.city.data = venue.city
  form.state.data = venue.state
  form.phone.data = venue.phone
  form.website_link.data = venue.website_link
  form.facebook_link.data = venue.facebook_link
  form.seeking_talent.data = venue.seeking_talent
  form.seeking_description.data = venue.seeking_description
  form.image_link.data = venue.image_link

  db.session.close()

  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venueData)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes

  form = VenueForm()
  venue = {
    "name": form.name.data,
    "genres": form.genres.data,
    "address": form.address.data,
    "city": form.city.data,
    "state": form.state.data,
    "phone": form.phone.data,
    "website_link": form.website_link.data,
    "facebook_link": form.facebook_link.data,
    "seeking_talent": form.seeking_talent.data,
    "seeking_description": form.seeking_description.data,
    "image_link": form.image_link.data
  }

  try:
    db.session.query(Venue).filter(Venue.id == venue_id).update(venue)
    db.session.commit()

  except:
    print("Error!")
    db.session.rollback()
    print(sys.exc_info())

  finally:
    db.session.close()

  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  form = ArtistForm()
  error = False

  try:
    artist = Artist(
      name=form.name.data,
      city=form.city.data,
      state=form.state.data,
      phone=form.phone.data,
      image_link=form.image_link.data,
      facebook_link=form.facebook_link.data,
      seeking_venue=form.seeking_venue.data,
      genres=form.genres.data,
      website_link=form.website_link.data,
      seeking_description=form.seeking_description.data
    )

    db.session.add(artist)
    db.session.commit()

    # on successful db insert, flash success
    flash('Artist ' + form.name.data + ' was successfully listed!')
  
  except:
    error = True
    db.session.rollback()
    print(form.data)
    print(sys.exc_info())

  finally:
    db.session.close()

  if error:
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
    flash('An error occurred. Artist ' + form.name.data + ' could not be listed.')
  # TODO: modify data to be the data object returned from db insertion
  
  return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.

  dbQuery = db.session.query(Show).all()
  data=[]

  for show in dbQuery:

    venueQuery = db.session.query(Venue).get(show.venue_id)
    artistQuery = db.session.query(Artist).get(show.artist_id)

    data.append({
      "venue_id": show.venue_id,
      "venue_name": venueQuery.name,
      "artist_id": show.artist_id,
      "artist_name": artistQuery.name,
      "artist_image_link": show.artist_image_link,
      "start_time": show.start_time
    })

  db.session.close()

  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead

  form = ShowForm()
  error = False
  try:

    # add venue name, artist name, and artist image to Show model
    venueQuery = db.session.query(Venue).filter_by(id=form.venue_id.data).first()
    artistQuery = db.session.query(Artist).filter_by(id=form.artist_id.data).first()

    show = Show(
      venue_id=form.venue_id.data,
      venue_name=venueQuery.name,
      artist_id=form.artist_id.data,
      artist_name=artistQuery.name,
      artist_image_link=artistQuery.image_link,
      start_time=form.start_time.data
    )

    db.session.add(show)
    db.session.commit()

    # on successful db insert, flash success
    flash('Show was successfully listed!')
  
  except:
    error = True
    db.session.rollback()
    print(form.data)
    print(sys.exc_info())

  finally:
    db.session.close()

  if error:
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Show could not be listed.')
    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    flash('An error occurred. Show could not be listed.')
  
  return render_template('pages/home.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''

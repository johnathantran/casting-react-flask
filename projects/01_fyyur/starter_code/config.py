import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# TODO IMPLEMENT DATABASE URL
# dialect://username:password@host:port/dbName
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Hien3045@localhost:5432/fyyur'
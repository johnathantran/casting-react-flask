import config
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

database_name = "capstone"
#database_path = "postgres://{}/{}".format('localhost:5432', database_name)
database_path = "postgresql://{}:{}@{}/{}".format(config.user, config.password, 'localhost:5432', database_name)
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Movie

'''
class Movie(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  releaseDate = Column(String)

  def __init__(self, title, releaseDate):
    self.title = title
    self.releaseDate = releaseDate

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'releaseDate': self.releaseDate,
    }

'''
Actor

'''
class Actor(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(String)
  gender = Column(String)

  def __init__(self, name, age, gender):
    self.id = id
    self.name = name
    self.age = age
    self.gender = gender

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
    }
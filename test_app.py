import config
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie
import os
from dotenv import load_dotenv
load_dotenv()

class CastingTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        #self.database_name = "casting_test"
        #self.database_path = "postgresql://{}:{}@{}/{}".format('postgres', os.environ['PASSWORD'],'localhost:5432', self.database_name)
        self.database_path = os.environ["DATABASE_TEST_URL"]
        setup_db(self.app, self.database_path)

        self.actor = {
            "name": "John Doe",
            "age": 24,
            "gender": "Male"
        }

        self.movie = {           
            "title": "Shrek 4",
            "releasedate": "01-01-2021"
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()


    def tearDown(self):
        """Executed after reach test"""
        pass

# GET TESTS: SUCCESS AND FAILURE (requires no auth so will not test for auth failure, Casting Director can access without requiring token)

    # 1 SUCCESS: GET movies
    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # 2 SUCCESS: GET actors
    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)




# POST TESTS: SUCCESS AND FAILURE

    # 3 SUCCESS: POST movies
    # RBAC SUCCESS Test: Executive producer can post a movie
    def test_post_movies(self):
        res = self.client().post('/movies', json=self.movie, headers={ 
            'Authorization': "Bearer " + config.producer_token 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # 4 SUCCESS: POST actors
    # RBAC SUCCESS Test: Executive producer can post an actor
    def test_post_actors(self):
        res = self.client().post('/actors', json=self.actor, headers={ 
            'Authorization': "Bearer " + config.producer_token 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
    
    # 5 FAIL: POST movies & RBAC Test #1, not authenticated, expect 500 because auth.py 401 middleware error translates to 500 internal server error in app.py
    # RBAC FAIL Test: Casting Director has no permissions except GET, so they don't have a token
    def test_500_post_movies(self):
        res = self.client().post('/movies', json=self.movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)

    # 6 FAIL: POST actors & RBAC Test #2, not authenticated
    # RBAC FAIL Test: Casting Director has no permissions except GET, so they don't have a token
    def test_500_post_actors(self):
        res = self.client().post('/actors', json=self.actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)



# PATCH TESTS: SUCCESS AND FAILURE

    # 7 SUCCESS: PATCH movie (use an ID that exists)
    def test_patch_movie(self):
        
        # edit the most recent movie
        selection = Movie.query.order_by(Movie.id).all()
        id = selection[-1].id
  
        res = self.client().patch('/movies/' + str(id), json=self.movie, headers={ 
            'Authorization': "Bearer " + config.producer_token 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])
    
    # 8 FAIL: PATCH movie (use an ID that does not exist)
    def test_422_patch_nonexistent_movie(self):
        
        # edit the most recent movie
        res = self.client().patch('/movies/1000', json=self.movie, headers={ 
            'Authorization': "Bearer " + config.producer_token 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
    
    # 9 SUCCESS: PATCH actor (use an ID that exists)
    def test_patch_actor(self):
        
        # patch the most recent actor
        selection = Actor.query.order_by(Actor.id).all()
        id = selection[-1].id
  
        res = self.client().patch('/actors/' + str(id), json=self.actor, headers={ 
            'Authorization': "Bearer " + config.producer_token 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])
    
    # 10 FAIL: PATCH actor (use an ID that does not exist)
    def test_422_patch_nonexistent_actor(self):
        
        res = self.client().patch('/actors/1000', json=self.actor, headers={ 
            'Authorization': "Bearer " + config.producer_token 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)



# DELETE TESTS: SUCCESS AND FAILURE

    # 11 SUCCESS: DELETE movie (use an ID that exists)
    def test_delete_movie(self):
        
        # delete the most recent movie
        selection = Movie.query.order_by(Movie.id).all()
        id = selection[-1].id
  
        res = self.client().delete('/movies/' + str(id), headers={ 
            'Authorization': "Bearer " + config.producer_token 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    # 12 FAIL: DELETE movie (use an ID that does not exist)
    def test_422_delete_nonexistent_movie(self):
        
        res = self.client().delete('/movies/1000', headers={ 
            'Authorization': "Bearer " + config.producer_token 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
    
    # 13 SUCCESS: DELETE actor (use an ID that exists)
    def test_delete_actor(self):
        
        # delete the most recent actor
        selection = Actor.query.order_by(Actor.id).all()
        id = selection[-1].id
  
        res = self.client().delete('/actors/' + str(id), headers={ 
            'Authorization': "Bearer " + config.producer_token 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    # 14 FAIL: DELETE actor (use an ID that does not exist)
    def test_422_delete_nonexistent_actor(self):
        
        res = self.client().delete('/actors/1000', headers={ 
            'Authorization': "Bearer " + config.producer_token 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
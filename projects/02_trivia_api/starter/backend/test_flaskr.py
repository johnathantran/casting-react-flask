import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('postgres','Hien3045','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.test_question = {
            "id": "100",
            "question": "Test question",
            "answer": "Test answer",
            "category": 1,
            "difficulty": 5
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

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # SUCCESS: GET categories
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # SUCCESS: GET questions
    def test_get_paginated_questions(self):
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])
        self.assertTrue(data['questions'])

    # FAIL: GET questions
    def test_404_sent_beyond_valid_page(self):
        res = self.client().get('/questions?page=100')
        self.assertEqual(res.status_code, 404)  

    # SUCCESS: POST question
    # in backend folder, to test using a curl request, run:
    # curl -H "Content-Type: application/json" --data @body.json http://localhost:3000/questions
    # def test_add_question(self):
    #     res = self.client().post('/questions', json=self.test_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['total_questions'])
   
    # SUCCESS: DELETE question (use an ID that exists)
    # def test_delete_question(self):
    #     res = self.client().delete('/questions/25')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    

    # SUCCESS: POST request to search for questions by search term
    def test_search_question(self):
        res = self.client().post('/questions?title', json=self.test_question)
        data = json.loads(res.data)

        search = "%{title}%"
        selection = Question.query.filter(Question.question.ilike(search)).all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(selection) >= 0)
        
    # SUCCESS: GET request to search for questions by category
    def test_get_by_category(self):
        res = self.client().get('/categories/1/questions', json=self.test_question)
        data = json.loads(res.data)

        selection = Question.query.filter(Question.category == 1).all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(selection) >= 0)

    # SUCCESS: POST request to get the next question
    def test_get_next_question(self):
        print("Starting tes: get next question...")
        requestBody = {
            "previous_questions": [],
            "quiz_category": 1
        }
        res = self.client().post('/quizzes', json=requestBody)
        print(res)
        print(res.data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
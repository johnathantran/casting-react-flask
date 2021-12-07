import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  # CORS Headers 
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE')
      return response


  def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * 10
    end = start + 10

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_categories():

    categories = Category.query.all()
    categoryDict = {}
    for category in categories:
      categoryDict[category.id] = category.type
    
    return jsonify({
      'success': True,
      'categories': categoryDict
    })

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
 
  #@app.route('/questions?page=<int:page_number>&category=<int:current_category>') 
  @app.route('/questions')
  @app.route('/questions?page=<int:page_number>')
  def get_questions():
    
    page = request.args.get("page", 1, type=int)
    selection = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)

    if len(current_questions) == 0:
      abort(404)
    
    if (page * 10) > (len(selection) + 10):
      abort(404)

    categories = Category.query.all()
    categoryDict = {}
    for category in categories:
      categoryDict[category.id] = category.type

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(Question.query.all()),
      'categories': categoryDict,
      'current_category': None
    })

  
  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):

    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None:
        abort(404)

      question.delete()
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)
    
      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions': current_questions,
        'total_questions': len(Question.query.all())
      })
    
    except:
      abort(422)

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def add_question():

    body = request.get_json()
    new_question = body.get("question", None)
    new_answer = body.get("answer", None)
    new_category = body.get("category", None)
    new_difficulty = body.get("difficulty", None)
    
    try:
        question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
        question.insert()

        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)

        return jsonify(
            {
                "success": True,
                "created": question.id,
                "questions": current_questions,
                "total_questions": len(Question.query.all()),
            }
        )

    except:
        abort(422)
    
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/<string:search_term>', methods=['POST'])
  def submit_search(search_term):

    search = "%{}%".format(search_term)
    selection = Question.query.filter(Question.question.ilike(search)).all()
    #current_questions = paginate_questions(request, selection)
    current_questions = [question.format() for question in selection]

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(Question.query.all()),
      'current_category': None
    })

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  def get_by_category(category_id):
 
    selection = Question.query.filter(Question.category == category_id).all()
    current_questions = [question.format() for question in selection]

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(Question.query.all()),
      'current_category': category_id
    })

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def play_quiz():

    # get request params
    body = request.get_json()
    previousQuestions = body.get("previous_questions", None)
    quizCategory = body.get("quiz_category", None)

    try:
      # filter selection based on previous questions and category
      selection = Question.query.filter(Question.category == quizCategory['id']).all()

      filtered_selection = []
      for question in selection:
        if question.id not in previousQuestions:
          filtered_selection.append(question)

      index = random.randint(0, len(filtered_selection)-1)
      next_question = filtered_selection.pop(index)
      
      return jsonify({
        'success': True,
        'question': {
          'id': next_question.id,
          'question': next_question.question,
          'answer': next_question.answer, 
          'difficulty': next_question.difficulty,
          'category': next_question.category,
      }
      })
    
    except:
      abort(404)
    

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(400)
  def bad_request(e):
      return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
      }), 404

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
      return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
      }), 500

      
  return app

if __name__ == '__main__':
  app = create_app()
  app.run()
    
# Capstone Project: Casting Service
This app will allow a user to view various actors and movies for a casting web application. Special users can add, modify, or delete actors and movies from the casting service.

The app features 2 forms that can be dynamically toggled between the Actors view and the Movies view.

### Setting Environment Variables
There are 2 files you will need to modify to setup your environment variables correctly.

1. **.env** 
In the /backend folder, environment variables with the Heroku Postgres database credentials, Auth0 domain information, and a token are provided. 

The token will be used to configure authorization headers for the Executive Producer role as part of the unit tests in /backend/test_app.py.

There is another file called '.env testCopy' and this can be used to test the app with a local database. 

2. **env.js** 
In the /frontend folder, copy the env_template.js file provided, rename to env.js, and fill out the correct Auth0 information (domain and Client ID).

For the purpose of submitting this app as a capstone project to Udacity, I will be sending both a complete config.py and env.js file separately.

### Logging In
To access the application, please login using the Auth0 service with the following provided credentials:
Here is the login info for the 2 users:

User #1: Casting Director (can only view movies and actors)
Username: jtran304@gmail.com
Password: Testing123!

User #2: Executive Producer (has full permissions to add, edit, delete movies and actors)
Username: jtran.testing@gmail.com
Password: Testing123!

The bearer token is provided in config.py in the producer_token, but will also be sent separately as this will be need to test the API endpoints using the Postman collection provided in the project root.

If you experience any issues with Auth0 logging out, please clear your browser cache and try to log in again.

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


### Running the server and the app

First ensure you are working using your created virtual environment and you are in the /backend directory.

To run the server, execute:

```bash
python app.py
```

Afterward, navigate to the /frontend directory to start the React application and run:
```bash
npm start
```

You may need to run npm install first to collect any needed packages in the /frontend directory.



## API Endpoints
A Postman Collection is provided in the project root to test the endpoints. For the DELETE and PATCH endpoints, make sure to edit the movie or actor ID in the endpoint itself to test for successful cases.

```

Endpoints
GET '/movies'
GET '/actors'
POST '/movies'
POST '/actors'
DELETE '/movies/${id}'
DELETE '/actors/${id}'
PATCH '/movies/${id}'
PATCH '/actors/${id}'


GET '/movies'
- Fetches a list of all movies
- Request Arguments: None
- Returns: An object with key "movies" mapping to a list of movies 
{
    "movies": [
        {
            "id": 17,
            "releasedate": "01-01-2021",
            "title": "Shrek 4"
        },
        {
            "id": 24,
            "releasedate": "01-01-2021",
            "title": "Shrek 4"
        }
    ],
    "success": true
}


GET '/actors'
- Fetches a list of all actors
- Request Arguments: None
- Returns: An object with key "movies" mapping to a list of movies 
{
    "actors": [
        {
            "age": 12,
            "gender": "male",
            "id": 13,
            "name": "test"
        },
        {
            "age": 52,
            "gender": "Feale",
            "id": 12,
            "name": "Tammy"
        }
    ],
    "success": true
}


POST '/movies'
- Sends a post request in order to add a new movie
- Request Body: 
{
    'title':  'Shrek',
    'releasedate':  '01-01-2021',
}
- Returns: A list of all movies including the added movie


POST '/actors'
- Sends a post request in order to add a new actor
- Request Body: 
{
    "age": 12,
    "gender": "Male",
    "name": "Tim"
}
- Returns: A list of all actors including the added actor


DELETE '/movies/${id}'
- Deletes a specified movie using the id of the movie
- Request Arguments: id - integer
- Returns: The appropriate HTTP status code and the deleted movie ID.


DELETE '/actors/${id}'
- Deletes a specified actor using the id of the actor
- Request Arguments: id - integer
- Returns: The appropriate HTTP status code and the deleted actor ID.


PATCH '/movies/${id}'
- Sends a post request in order to edit info of existing movie
- Request Body: 
{
    'title':  'Shrek',
    'releasedate':  '01-01-2021',
}
- Returns: The updated movie id


PATCH '/actors/${id}'
- Sends a patch request in order to edit info of existing actor
- Request Body: 
{
    "age": 12,
    "gender": "Male",
    "name": "Tim"
}
- Returns: The updated actor id





```


## Testing
To run the tests, you need to have a test database setup first with the tables Actor and Movie with the correct columns according to their models.

Then just run:
```
python test_app.py
```

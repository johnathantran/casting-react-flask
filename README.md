# Capstone Project: Casting Service
This app will allow a user to view various actors and movies for a casting web application. Special users can add, modify, or delete actors and movies from the casting service.

The app features 2 forms that can be dynamically toggled between the Actors view and the Movies view.

# Endpoint Testing
To test all endpoints, please refer to the Postman Collection found in the root of the submitted project folder.

To test endpoints through the frontend, please run the frontend locally by running 'npm start' in the project root, and then interacting with the React application that launches in the browser.

### Setting Environment Variables
There are 2 files that contain environment variables.

1. **.env** 
In the /backend folder, environment variables with the Heroku Postgres database credentials, Auth0 domain information, and a token are provided. 

The token will be used to configure authorization headers for the Executive Producer role as part of the unit tests in /backend/test_app.py.

Follow the below steps if you want to connect a local database to your frontend (by default, the local frontend will connect to the Heroku database).

# Local app info, 4 step process to initialize locally:
1. Uncomment the local environment variables in '.env' to use, and comment out the Heroku environment variables
2. Change the 'proxy' key in package.json to value: 'http://localhost:5000/')
3. Start the local server on port 5000 by running 'python app.py'
4. Start the frontend with 'npm start'

To switch back to the Heroku database, simply change the 'proxy' key back to: "https://casting-jtran.herokuapp.com/"
And switch back the environment variables in '.env' to the production credentials.


2. **env.js** 
In the /frontend folder, the env.js file is already provided and will automatically detect between test and production environments. Because the frontend is not deployed to Heroku as its own server, it will automatically use the test configurations because you will be running it locally.


### Logging In
To access the application, please login using the Auth0 service with the following provided credentials:
Here is the login info for the 2 users:

User #1: Casting Director (can only view movies and actors)
Username: jtran304@gmail.com
Password: Testing123!

User #2: Executive Producer (has full permissions to add, edit, delete movies and actors)
Username: jtran.testing@gmail.com
Password: Testing123!

The bearer token is this (will be updated as it expires):
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlljTHNYanJFc1RhV2pwQV82S1RoMyJ9.eyJpc3MiOiJodHRwczovL2Rldi1ycGsyMWlqNi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjIwNGMzMGY3ZjI3OWIwMDZjZDliNDczIiwiYXVkIjpbImNhc3RpbmciLCJodHRwczovL2Rldi1ycGsyMWlqNi51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjQ0NTMwODAzLCJleHAiOjE2NDQ2MTcyMDMsImF6cCI6IndqQUVjMzlaeUI1Z0hFdTVHWW9hQkg5S1I3V0Z4NkhCIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.b98CVQP1swdpf3qgkfxi6rMZIBOnS7BfB9RVyZkURp58njRGX4xFOIeGzTh7VrhHmNkz7YoU2-2emQc_VFLDlZYMlJ1V6rrmk_RaA-fsyT5ey0rnOYal4mr2Ne7qzsVFRQNo2O5azN1OOodJqIsKIw-H28WtwxKNIm3uR1FTUpGG7YbzSpppFgJgZd0pSkXoOcoENNWVYMNeYF37xfseemY9h-Mpjx_3Uodzxym3R-jPG8Bck130bNaNxmOKhpe_nS0WF2KG4VeENdcRJejkoiQJiPILfHKJvJ_-8T-nLevDgy7D15Wpr6tNVfIlKbSSTi-92h5MbnyfkW4m9MF0Ag

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

To run the server, execute (note that you don't have to do this if you are using the deployed Heroku backend):

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

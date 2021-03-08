## Casting Agency

## Full Stack Nano - IAM Final Project

# Introduction

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

No frontend developed yet, only backend side.

Application hosted on Heroku:

https://deploy-capston.herokuapp.com/


## Motivation

For buliding final Project in Nano Show what i learn

1. Database with postgres and sqlalchemy (models.py)
2. API with Flask (app.py)
3. TDD Unittest (test_app.py)
4. Authorization with Auth0 (auth.py)
5. Deployment on Heroku

## Development Setup

1. **Download the project starter code locally**
```
git clone https://github.com/rsha-tw/fsnd-capston.git

```

3. **Initialize and activate a virtualenv using:**
```
source env/Scripts/activate
source env/bin/activate 

```

4. **Install the dependencies:**
```
pip install -r requirements.txt
or 
pip3 install -r requirements.txt

```

5. **Run the development server:**
```
export FLASK_APP=myapp
export FLASK_ENV=development # enables debug mode
python3 app.py

```
6. **Export Environment Variables:**

Refer to the setup.sh file and export the environment variables for the project.

7. **Run Database Migrations:**
```
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade

```
## Testing

To run the tests, run
```
dropdb capstone
createdb capstone
python test_app.py 

```
## API Reference
* Base URL: Currently this application is only hosted locally. The backend is hosted at https://deploy-capston.herokuapp.com/

* Authentication: This application use Auth0 service

* Use this link to get new token https://dev-cg254k-8.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=0BJq9aQKYdBaRMQFvKmZWEbe2PMJ06Rz&redirect_uri=https://localhost:8080/login-results

Users in this application are:
  * Assistant : Can view actors and movies
    * Email: ashootibebal@gmail.com
    * Password: Rr12345678@
  * Director : Assistant Access +  Modify on actors and movies
    * Email: rasha@gmail.com
    * Password: Rr12345678@
  * Executive: Full Access
    * Email: aseel@gmail.com
    * Password: Rr12345678@

# Error Handling
Errors are returned as JSON in the following format:
```
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}

```
The API will return three types of errors:

* 404 – resource not found
* 422 – unprocessable
* 401 - Unauthorized
* 400 - bad request

# Endpoints

# GET /actors

  * General: Return list of actors in Database

  * Sample: curl -L -X GET 'vast-stream-21858.herokuapp.com/actors' \ -H 'Authorization: Bearer Director_Token'
```
{ 
    "actors":[     {
            "age": 20,
            "gender": "Fmale",
            "id": 4,
            "name": "Rasha"
        }
    ],
    "success": true
}

```
# GET /movies
  * General: Return list of movies in Database

  * Sample: curl -L -X GET 'vast-stream-21858.herokuapp.com/movies' \ -H 'Authorization: Bearer Assisant_Token'
```
{    
    "movies":[   {
            "id": 8,
            "release_date": "Mon, 26 Oct 2020 00:00:00 GMT",
            "title": "BoyzBeforFlower"
        }
    ],
    "success": true
}
```
# POST /actors
* General:

    * Create actor using JSON Request Body
    * Return ID of created actor

    * Sample:curl --location --request POST 'localhost:8080/actors' \
    --header 'Authorization: Bearer Producer_Token \
    --header 'Content-Type: application/json' \
    --data-raw '{"name": "Rasha","age": "20","gender":"Fmale"}'
```
{
    "created_id": 1,
    "success": true
}

```
# POST /movies
* General:

  * Create movie using JSON Request Body
  * Return ID of created movie
  * curl --location --request POST 'localhost:8080/movies' \
--header 'Authorization: Bearer Producer_Token \
--header 'Content-Type: application/json' \
--data-raw '{"title": "The Dark","release_date": "2020/10/26"}'
```
{
    "created_id": 3,
    "success": true
}
```

# PATCH /actors/<actor_id>
* General:

    * Modify actor given id in URL provided the information to update
    * Sample: curl --location --request PATCH 'http://127.0.0.1:8080/actors/2' \
    --header 'Authorization: Bearer Producer_Token \
    --header 'Content-Type: application/json' \
    --data-raw ' {"name": "Sabah-Salem","age": "28","gender":"Fmale"}'
```
{
  "actor": {
    "age": 27, 
    "gender": "Fmale", 
    "id": 2, 
    "name": "Sabah-Salem"
  }, 
  "success": true
}
```

# PATCH /movies/<movie_id>
* General:
   * Modify movie given id in URL provided the information to update
   * Sample:curl --location --request PATCH 'localhost:8080/movies/2' \
--header 'Authorization: Bearer Producer_Token \
--header 'Content-Type: application/json' \
--data-raw '{"release_date": "Mon, 26 Oct 2020 00:00:00 GMT","title": "The Dark5"}'
```
{
    "movie": {
        "id": 2,
        "release_date": "Mon, 26 Oct 2020 00:00:00 GMT",
        "title": "The Dark5"
    },
    "success": true
}
```
# DELETE /actors/<actor_id>
  * General: Delete an actor given id in URL
  * Sample:curl --location --request DELETE 'localhost:8080/actors/1' \
--header 'Authorization: Bearer Producer_Token \
--header 'Content-Type: application/json' \
--data-raw '{"name": "Rasha","age": "20","gender":"Fmale"}'
```
{
    "deleted_id": 6,
    "success": true
}
```
# DELETE /movies/<movie_id>
  * General: Delete movie given id in URL
  * curl --location --request DELETE 'localhost:8080/movies/3' \
--header 'Authorization: Bearer Producer_Token \
--header 'Content-Type: application/json' \
--data-raw '{"title": "test","release_date": "2010/10/26"}'
```
{
    "deleted_id": 5,
    "success": true
}
```
# Postman user

In this repo there is collection file exported 

you can use it to test all API Provided in here


<img src="https://i.pinimg.com/736x/ff/3d/ac/ff3dacf36806047a53e7582bbee93cd4.jpg" alt="OpenAI Logo" width="420" height="220">


# Diksha's Casting Agency Backend

## Overview

   - This Application is for a casting agency to organise Movies and Actors Database
   - Features 
      - The Users for this application are Casting Assitant, Casting Director and Executive Producer
      - The Application has end points:
      ------------------------------------
         - GET /movies
         - GET /actors
         - GET /movies/id
         - GET /actors/id
      ------------------------------------
         - POST /movies
         - POST /actors
      ------------------------------------
         - PATCH /movies/id
         - PATCH /actors/id
      ------------------------------------
         - DELETE /movies/id
         - DELETE /actors/id


## Getting Started

### Prerequisite

   - Tools
      - Postman

------------------------------------------------------


#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   ---------------------------
   - `get:movies`
   - `post:movies`
   - `patch:movies`
   - `delete:movies`
   ---------------------------
   - `get:actors`
   - `post:actors`
   - `patch:actors`
   - `delete:actors`
6. Create new roles for:

   - Casting Assitant

      - `get:actors`
      - `get:movies`

   - Casting Director
   
      - `get:actors`
      - `get:movies`
      - `post:actors`
      - `patch:actors`
      - `patch:movies`
      - `delete:actors`
   
   - Executive Producer
      - `get:movies`
      - `post:movies`
      - `patch:movies`
      - `delete:movies`
      - `get:actors`
      - `post:actors`
      - `patch:actors`
      - `delete:actors`
     - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com).
   - Register 2 users - assign the Barista role to one and Manager role to the other.
   - Sign into each account and make note of the JWT.
   - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
   - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`


## Render steps
   - Connect your Repository with Render 
   - Create a web service and deploy it with the repositroy connect and add DATABASE_URL




### Deployment Link for the Application : [Diksha's Casting Agency](https://render-cloud-example-ymr0.onrender.com)


## TEST and Post-Man collection

Attached `casting-agency apis` file 
   - Upload it in post man and run the requests 
-----------------------------------------------------
    Note 
    -  `The collection contains the fresh jwt token`
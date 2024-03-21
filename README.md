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

## Prerequisite

   ### Tools
      - Postman
      - VS Code 

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


   - Create a new, single page web application say `"Casting Agency"`

   - Create a new API say `"casting-agency-service"`

   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token

   - Create new API permissions:
      
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

   - Create new roles for:

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


### Application Login URL - [Casting Agency Login](https://deekshagg.us.auth0.com/authorize?audience=casting-agency-service&response_type=token&client_id=KqhSPVijK1qPtIvVAaRZgk7JyQBer3vj&redirect_uri=https://127.0.0.1:8080/login-results)



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

    - Open `'.env'` to see sensitive information
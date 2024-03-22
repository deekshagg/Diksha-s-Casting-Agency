from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from Actor import delete_actor, insert_actor, patch_actor, select_actor, select_actor_detail
from Movie import delete_movie, insert_movie, patch_movie, select_movie, select_movie_detail
from auth.auth import requires_auth
from database.models import Actor, Movie, setup_db


def create_app(active=True, test_config=None):

    app = Flask(__name__)

    with app.app_context():
        if active:
            setup_db(app)

    CORS(app)


# -------------------------------------------Movie---------------------------------------

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def movies(payload):
        return select_movie()
    
    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth('get:movies')
    def movies_detail(payload, movie_id):
        return select_movie_detail(movie_id)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(payload):
        return insert_movie()

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('post:movies')
    def update_movie(payload, movie_id):
        return patch_movie(movie_id)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def remove_movie(payload, movie_id):
        return delete_movie(movie_id)

# --------------------------------------------Actor--------------------------------------

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def actors(payload):
        return select_actor()
    
    @app.route('/actors/<int:actor_id>', methods=['GET'])
    @requires_auth('get:actors')
    def actors_detail(payload, actor_id):
        return select_actor_detail(actor_id)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(payload):
        return insert_actor()

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, actor_id):
        return patch_actor(actor_id)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def remove_actor(payload, actor_id):
        return delete_actor(actor_id)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()

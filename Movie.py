from flask import abort, jsonify, request
from database.models import Movie


def select_movie():
    try:
        movies = Movie.query.all()
        movie_data = []
        for movie in movies:
            movie_data.append({
                'id': movie.id,
                'title': movie.title,
                'release_date': movie.release_date.strftime('%Y-%m-%d')
            })
        response = {
            'success': True,
            'Movies': movie_data
        }
        return jsonify(response), 200

    except Exception as e:
        abort(401)


def select_movie_detail(movie_id):
    try:
        movie = Movie.query.get(movie_id)

        if not movie:
            abort(404)

        response = {
            'success': True,
            'id': movie.id,
            'title': movie.title,
            'release_date': movie.release_date.strftime('%Y-%m-%d')
        }
        return jsonify(response), 200

    except Exception as e:
        abort(401)


def insert_movie():
    try:

        data = request.json
        title = data['title']
        release_date = data['release_date']

        new_movie = Movie(title=title, release_date=release_date)

        Movie.insert(new_movie)

        response = {
            'success': True,
            'message': 'Movie added successfully',
            'movie': new_movie.title
        }
        return jsonify(response), 201

    except Exception as e:
        abort(422)


def patch_movie(movie_id):
    try:
        movie = Movie.query.get(movie_id)

        if not movie:
            abort(404)

        upadted_date = request.json
        title = upadted_date['title']
        release_date = upadted_date['release_date']

        Movie.patch(movie, title, release_date)

        response = {
            'success': True,
            'message': 'Movie updated successfully',
            'movie': movie.title
        }
        return jsonify(response), 201

    except Exception as e:
        abort(422)


def delete_movie(movie_id):
    try:
        movie = Movie.query.get(movie_id)

        if not movie:
            abort(404)

        Movie.delete(movie)

        response = {
            'success': True,
            'message': 'Movie deleted successfully',
            'movie': movie.title
        }
        return jsonify(response), 201

    except Exception as e:
        abort(422)

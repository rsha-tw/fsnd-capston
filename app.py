import os
import sys
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import setup_db, Movie, Actor
import random


def create_app():
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    

    # Get all actors

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(self):
        actors = Actor.query.order_by(Actor.id).all()
        formatted_actors = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': formatted_actors
        })
    # Post a new actors

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(self):
        body = request.get_json()


        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')

        actor = Actor(name, age, gender)
        actor.insert()

        return jsonify({
            'success': True,
            'created_id': actor.id
        })

    # DELETE Actors
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(self, actor_id):
        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({
            'success': True,
            'deleted_id': actor_id
        })

    # PATCH Update Actors
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(self, actor_id):
        body = request.get_json()

        actor = Actor.query.get(actor_id)

        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')

        try:
            actor.name = name
            actor.age = age
            actor.gender = gender

            actor.update()

            return jsonify({
                'success': True,
                'actor': actor.format()
            })
        except BaseException:
            abort(400)

    # GET all Movies
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(self):
        movies = Movie.query.order_by(Movie.id).all()
        formatted_movies = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': formatted_movies
        })
    # POST a new Movies

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(self):
        body = request.get_json()

        if body is None:
            abort(422)

        title = body.get('title')
        release_date = body.get('release_date')

        movie = Movie(title, release_date)
        movie.insert()

        return jsonify({
            'success': True,
            'created_id': movie.id
        })
    # PATCH Update Moveis

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(self, movie_id):
        body = request.get_json()

        if body is None:
            abort(422)

        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)

        title = body.get('title')
        release_date = body.get('release_date')

        try:
            movie.title = title
            movie.release_date = release_date
            movie.update()

            return jsonify({
                'success': True,
                'movie': movie.format()
            })
        except BaseException:
            abort(400)

    # DELETE Actors

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie( self,movie_id):
        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)
        movie.delete()

        return jsonify({
            'success': True,
            'deleted_id': movie_id
        })

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(404)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resources not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(AuthError)
    def handle_auth_error(e):
        response = jsonify(e.error)
        response.status_code = e.status_code
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.auth import auth_ns
from views.movies import movie_ns
from views.genres import genre_ns
from views.directors import director_ns
from views.users import user_ns


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    register_extentions(app)
    return app


def register_extentions(app):
    api = Api(app)
    db.init_app(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(debug=True, port=10001)
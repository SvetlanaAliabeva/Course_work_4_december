from flask import Flask, render_template
from flask_restx import Api

from config import Config
from setup_db import db
from views.auth import auth_ns
from views.movies import movie_ns
from views.genres import genre_ns
from views.directors import director_ns
from views.users import user_ns

api = Api(title="Flask Course Project 3", doc="/docs")


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	@app.route('/')
	def index():
		return render_template('index.html')

	db.init_app(app)
	api.init_app(app)

	api.add_namespace(movie_ns)
	api.add_namespace(genre_ns)
	api.add_namespace(director_ns)
	api.add_namespace(user_ns)
	api.add_namespace(auth_ns)

	return app

app = create_app()


if __name__ == '__main__':
	app.run(debug=True, port=25000)

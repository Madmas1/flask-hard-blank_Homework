from flask import Flask
from flask_restx import Api
from setup_db import db
from config import Config

from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


# Application object registration and downloading configurations
def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


# Registration namespaces for application
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)


# Create application object
app = create_app(Config())

# Run application
if __name__ == '__main__':
    app.run()

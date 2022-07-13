# Container of mappings between DAOs and services

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from services.director import DirectorService
from services.genre import GenreService
from services.movie import MovieService
from setup_db import db

# Creating DAO objects based on an imported db session
director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)
genre_dao = GenreDAO(db.session)

# Creating service objects based on an imported DAO objects
director_service = DirectorService(director_dao)
movie_service = MovieService(movie_dao)
genre_service = GenreService(genre_dao)

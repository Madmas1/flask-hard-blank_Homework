# CRUD movie DAO

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie.title, Movie.description, Movie.year, Movie.rating, Movie.trailer,
                     Genre.name.label('genre'), Director.name.label('director')).join(Genre).join(Director).filter(Movie.id == mid).one()

    def get_all(self):
        movies_query = self.session.query(Movie.title, Movie.description, Movie.year, Movie.rating, Movie.trailer,
                     Genre.name.label('genre'), Director.name.label('director')).join(Genre).join(Director)
        return movies_query

    def genre_filter(self, query, value):
        return query.filter(Genre.id == value)

    def director_filter(self, query, value):
        return query.filter(Director.id == value)

    def year_filter(self, query, value):
        return query.filter(Movie.year == value)

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()

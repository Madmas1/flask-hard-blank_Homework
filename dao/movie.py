# CRUD movie DAO

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def join_query(self):
        return self.session.query(Movie.title, Movie.description, Movie.year, Movie.rating, Movie.trailer,
                     Genre.name.label('genre'), Director.name.label('director')).join(Genre).join(Director)

    def get_one(self, mid, data=None):
        if data:
            return data.filter(Movie.id == mid).first()
        else:
            return self.session.query(Movie).filter(Movie.id == mid).one()

    def get_all(self, data=None):
        if data:
            return data.all()
        else:
            return self.session.query(Movie).all()

    def genre_filter(self, data, value):
        return data.filter(Genre.id == value)

    def director_filter(self, data, value):
        return data.filter(Director.id == value)

    def year_filter(self, data, value):
        return data.filter(Movie.year == value)

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

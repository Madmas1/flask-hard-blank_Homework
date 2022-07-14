# Service logic for movies view

from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        movie_data = self.dao.join_query()
        return self.dao.get_one(mid, movie_data)

    def get_all(self, did=None, gid=None, year=None):
        movies_data = self.dao.join_query()
        movies_data = self.dao.get_all(movies_data)
        if did:
            movies_data = self.dao.director_filter(movies_data, did)
        if gid:
            movies_data = self.dao.genre_filter(movies_data, gid)
        if year:
            movies_data = self.dao.year_filter(movies_data, year)
        return movies_data

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.dao.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("movie_id")

        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get("id")
        movie = self.dao.get_one(mid)

        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.description = data.get("description")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "year" in data:
            movie.year = data.get("year")
        if "rating" in data:
            movie.rating = data.get("rating")
        if "genre_id" in data:
            movie.genre_id = data.get("genre_id")
        if "movie_id" in data:
            movie.movie_id = data.get("movie_id")

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)

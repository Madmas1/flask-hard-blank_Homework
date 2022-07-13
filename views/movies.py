# Movies view

from flask_restx import Namespace, Resource
from flask import request

from container import movie_service
from dao.model.movie import MovieSchema

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        did = request.args.get('director_id', None)
        gid = request.args.get('genre_id', None)
        year = request.args.get('year', None)
        movies_list = movie_service.get_all(did, gid, year)
        return movies_schema.dump(movies_list)

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "The element was successfully added", 204


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        if not movie:
            return "this element does not exist", 404
        return movie_schema.dump(movie)

    def put(self, mid: int):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)
        return "The element was successfully changed", 202

    def patch(self, mid: int):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update_partial(req_json)
        return "The element was successfully updated", 202

    def delete(self, mid: int):
        movie_service.delete(mid)
        return "The element was successfully deleted", 203
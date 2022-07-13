from flask_restx import Namespace, Resource
from flask import request

from container import genre_service
from dao.model.genre import GenreSchema

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres_list = genre_service.get_all()
        return genres_schema.dump(genres_list)

    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return "The element was successfully added", 204


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        if not genre:
            return "this element does not exist", 404
        return genre_schema.dump(genre)

    def put(self, gid: int):
        req_json = request.json
        req_json["id"] = gid
        genre_service.update(req_json)
        return "The element was successfully changed", 202

    def patch(self, gid: int):
        req_json = request.json
        req_json["id"] = gid
        genre_service.update_partial(req_json)
        return "The element was successfully updated", 202

    def delete(self, gid: int):
        genre_service.delete(gid)
        return "The element was successfully deleted", 203
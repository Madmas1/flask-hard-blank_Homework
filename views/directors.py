from flask_restx import Namespace, Resource
from flask import request

from container import director_service
from dao.model.director import DirectorSchema

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors_list = director_service.get_all()
        return directors_schema.dump(directors_list)

    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "The element was successfully added", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = director_service.get_one(did)
        if not director:
            return "this element does not exist", 404
        return director_schema.dump(director)

    def put(self, did: int):
        req_json = request.json
        req_json["id"] = did
        director_service.update(req_json)
        return "The element was successfully changed", 202

    def patch(self, did: int):
        req_json = request.json
        req_json["id"] = did
        director_service.update_partial(req_json)
        return "The element was successfully updated", 202

    def delete(self, did: int):
        director_service.delete(did)
        return "The element was successfully deleted", 203
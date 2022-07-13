# Directors serilization models
from marshmallow import Schema, fields

from setup_db import db


class Director(db.Model):
    __tablename_ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()



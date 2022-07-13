# CRUD director DAO
from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Director).get(gid)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        new_director = Director(**data)
        self.session.add(new_director)
        self.session.commit()
        return new_director

    def update(self, director):
        self.session.add(director)
        self.session.commit()

    def delete(self, gid):
        director = self.get_one(gid)
        self.session.delete(director)
        self.session.commit()

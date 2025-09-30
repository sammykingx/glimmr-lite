from app.extensions import db


class BaseService:
    """
    Base service containing common DB CRUD utilities for all services.
    """
    def __init__(self, model):
        self.model = model

    def get_by_id(self, id):
        return self.model.query.get(id)

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    def update(self, obj, **kwargs):
        for key, value in kwargs.items():
            setattr(obj, key, value)
        db.session.commit()
        return obj

    def delete(self, obj):
        db.session.delete(obj)
        db.session.commit()

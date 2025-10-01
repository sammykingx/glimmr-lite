from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError


class BaseService:
    """
    Base service containing common DB CRUD utilities for all services.
    """
    def __init__(self, model):
        if not model:
            raise ValueError("A valid SQLAlchemy model is required.")
        
        self.model = model

    def get_by_field(self, field: str, value: str):
        if not hasattr(self.model, field):
            raise AttributeError(f"{self.model.__name__} has no attribute '{field}'")
        
        return self.model.query.filter(getattr(self.model, field) == value).first()

    def create(self, unique_field: str, unique_value, **kwargs):
        """
        Create a new record if it doesn't exist, else return existing.

        Args:
            unique_field (str): Field name to enforce uniqueness (e.g. 'email').
            unique_value: Value of the unique field.
            **kwargs: Fields for creating a new instance.

        Returns:
            model instance (existing or newly created).
        """
        if not unique_value or not unique_field:
            raise ValueError("Unique field/identifier value is required.")

        existing = self.get_by_field(unique_field, unique_value)
        if existing:
            return existing

        obj = self.model(**kwargs)
        try:
            db.session.add(obj)
            db.session.commit()
            db.session.refresh(obj)
            
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        
        return obj

    def update(self, obj, **kwargs):
        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        try:
            db.session.commit()
            db.session.refresh(obj)
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        return obj

    def delete(self, obj):
        try:
            db.session.delete(obj)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

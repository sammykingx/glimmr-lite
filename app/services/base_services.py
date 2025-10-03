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
        """
            Retrieve a single record by matching a field/value pair.

            This method requires that the field specified is unique (e.g., email, username, id).
            If the field is not unique, a ValueError is raised since multiple records could
            match the same value. For non-unique lookups or fetching multiple results, you
            should inherit from this class and use the query object directly.

            Args:
                field (str): The column name to filter by (must be a unique column).
                value (str): The value to compare against the given field.

            Raises:
                AttributeError: If the field does not exist on the model.
                ValueError: If the field is not defined as unique on the model.

            Returns:
                The model instance if found, otherwise None.
        """
        if not hasattr(self.model, field):
            raise AttributeError(f"{self.model.__name__} has no attribute '{field}'")
        
        column = getattr(self.model, field)

        if not getattr(column.property.columns[0], "unique", False):
            raise ValueError(
                f"The field '{field}' is not unique. Use a unique field to match against the value."
            )
            
        return self.model.query.filter(getattr(self.model, field) == value).first()

    def create(self, unique_field: str, unique_value, obj):
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
            else:
                raise AttributeError(f"{self.model.__name__} has no attribute '{key}'")
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

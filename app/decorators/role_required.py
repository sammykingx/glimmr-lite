# app/decorators/role_required.py
from functools import wraps
from flask import flash, request
from flask_login import current_user
from typing import List, Tuple, Union


def role_required(allowed_roles: Union[List[str], Tuple[str, ...]]):
    """
    Flask decorator to restrict access to routes based on user role.
    :param allowed_roles: list/tuple of allowed roles for this route
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated:
                if current_user.role not in allowed_roles:
                    flash("You do not have permission to access this resource.", "info")
                    return request.referrer
                return func(*args, **kwargs)
            else:
                flash("You need to log in to access this resource.", "error")
                return request.referrer
        return wrapper
    return decorator

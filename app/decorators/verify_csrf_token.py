from functools import wraps
from flask import request, jsonify, flash
from flask_wtf.csrf import CSRFError, validate_csrf


def verify_csrf(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            token = request.headers.get("X-CSRFToken")
            validate_csrf(token)
        except CSRFError:
            print("Missing/Invalid or expired CSRF token.")
            return (
                jsonify(
                    {
                        "status": "Error",
                        "message": "Looks like your session timed out. Please refresh the page to fix this.",
                    }
                ),
                400,
            )
        return func(*args, **kwargs)
    return wrapper
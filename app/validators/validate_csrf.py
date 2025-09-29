from flask_wtf.csrf import CSRFError, validate_csrf


def validate_csrf_token(csrf_token: str) -> bool:
    """
    Validate the provided CSRF token.

    :param csrf_token: The CSRF token to validate.
    :return: True if the token is valid, False otherwise.
    """
    try:
        validate_csrf(csrf_token)
        return True
    except CSRFError:
        return False
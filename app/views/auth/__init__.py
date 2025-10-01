from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix="/auth")

from . import login, register, reset_password, logout
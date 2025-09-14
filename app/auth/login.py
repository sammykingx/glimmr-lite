from . import bp
from flask import render_template

@bp.route("/auth")
@bp.route("/login")
def user_login():
    return render_template("auth/login.html")
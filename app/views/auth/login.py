from . import bp
from flask import current_app, render_template, request, url_for
from flask_login import login_user
from urllib.parse import urlparse
from app.models.user_profile import UserProfile
from app.decorators.verify_csrf_token import verify_csrf
import json


@bp.route("/login")
def user_login():
    return render_template("auth/login.html")


@bp.route("/checkpiont", methods=["POST"])
@verify_csrf
def user_checkpiont():
    data = request.get_json()
    next_url = data.get("next")
    # current_app.logger.info(f"PAYLOAD: {json.dumps(data, indent=2)}")
    user = UserProfile.query.filter_by(email=data.get("email")).first()
    if not user or not user.verify_pwd(data.get("password", None)):
        return {
            "status": "error",
            "message": "Incorrect email or password"
        }, 401
    
    login_user(user, remember=data.get("remember", False))
    if next_url and urlparse(next_url).netloc == "":
        return {
            "status": "success",
            "redirect": next_url
        }
    else:
        return {
            "status": "success",
            "redirect": url_for("accounts.dashboard")
        }
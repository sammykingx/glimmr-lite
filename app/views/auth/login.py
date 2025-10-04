from . import bp
from flask import current_app, render_template, request, url_for
from flask_login import login_user
from urllib.parse import urlparse
from app.services.user_service import UserService
from app.decorators.verify_csrf_token import verify_csrf
from app.constants.templates_map import Templates


@bp.route("/login")
def user_login():
    return render_template(Templates.Auth.LOGIN)


@bp.route("/checkpiont", methods=["POST"])
@verify_csrf
def user_checkpiont():
    account_manager = UserService()
    data = request.get_json()
    next_url = data.get("next")
    user = account_manager.get_user("email", data.get("email"))
    if not user or not user.verify_pwd(data.get("password", None)):
        return {
            "status": "error",
            "message": "Incorrect credentials provided"
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
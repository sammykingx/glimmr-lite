from . import bp
from flask import current_app, render_template, request, url_for
from app.models.user_profile import UserProfile
from app.services.base_services import BaseService
from app.decorators.verify_csrf_token import verify_csrf


@bp.route("/join", methods=["GET"])
def register_user():
    return render_template("auth/register.html")


@bp.route("/create-account", methods=["POST"])
@verify_csrf()
def create_account():
    data = request.get_json()
    new_user = UserProfile(
        email=data.get("email"),
        password=data.get("password"),
    )
    new_user.hash_pwd()
    account_service = BaseService(UserProfile)
    account_service.create("email", data.get("email"), **new_user.serialize())
        
    return {
        "status": "Succcess",
        "msg": "Account created successfully",
        "url": url_for("auth.user_login"),
    }, 201
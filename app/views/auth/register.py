from . import bp
from flask import render_template, request, url_for
from app.services.user_service import UserService
from app.decorators.verify_csrf_token import verify_csrf
from app.constants.templates_map import Templates

@bp.route("/join", methods=["GET"])
@verify_csrf
def register_user():
    return render_template(Templates.Auth.REGISTER)


@bp.route("/create-account", methods=["POST"])
@verify_csrf
def create_account():
    data = request.get_json()
    account_service = UserService()
    account_service.create_user(**data)
        
    return {
        "status": "Succcess",
        "msg": "Account created successfully",
        "redirect": url_for("auth.user_login"),
    }, 201
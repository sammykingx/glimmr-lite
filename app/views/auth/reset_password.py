from . import bp
from flask import current_app, render_template, request
from app.decorators.verify_csrf_token import verify_csrf


@bp.route("/recover-account")
def password_reset_link():
    return render_template("auth/forgot-password.html")

@bp.route("/send-reset-link", methods=["POST"])
@verify_csrf
def send_reset_link():
    """Sends a password reset link to the user's email."""
    email = request.get_json().get("email")
    

@bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    
    if request.method == "POST":
        form_data = request.form.to_dict()
        current_app.logger.info(f"Received password reset data: {form_data}")
        
    return render_template("auth/reset-password.html", token=token)
from . import bp
from flask import current_app, flash, render_template, redirect, request, url_for
from app.decorators.verify_csrf_token import verify_csrf
from app.services.user_service import UserService


@bp.route("/recover-account")
def password_reset_link():
    return render_template("auth/forgot-password.html")

@bp.route("/send-reset-link", methods=["POST"])
@verify_csrf
def send_reset_link():
    """Sends a password reset link to the user's email."""
    email = request.get_json().get("email")
    

@bp.route("/reset-password", methods=["GET", "POST"])
def reset_password(token):
    
    account_manager = UserService()
    verf_token = request.args.get("verf_id")
    token_data = account_manager.verify_token(verf_token, purpose="password reset")
    
    if not token_data:
        flash("Invalid reset link", "warning")
        return render_template("auth/reset-password.html", disable_input=True)
    
    if request.method == "POST":
        form_data = request.form.to_dict()
        user = account_manager.get_user("reset_token", token_data.get("token"))
        user.hash_pwd()
        account_manager.update_user(user, password=form_data.get("password"))
        return redirect(url_for("auth.user_checkpiont"))
        
    # GET Request
    return render_template("auth/reset-password.html")
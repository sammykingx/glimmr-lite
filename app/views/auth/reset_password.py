from . import bp
from flask import current_app, render_template, request


@bp.route("/recover-account", methods=["GET", "POST"])
def password_reset_link():
    
    if request.method == "POST":
        form_data = request.form.to_dict()
        current_app.logger.info(f"Received registration data: {form_data}")
        
    return render_template("auth/forgot-password.html")


@bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    
    if request.method == "POST":
        form_data = request.form.to_dict()
        current_app.logger.info(f"Received password reset data: {form_data}")
        
    return render_template("auth/reset-password.html", token=token)
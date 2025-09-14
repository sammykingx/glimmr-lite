from . import bp
from flask import current_app, render_template, request


@bp.route("/join", methods=["GET", "POST"])
def register_user():
    
    if request.method == "POST":
        form_data = request.form.to_dict()
        current_app.logger.info(f"Received registration data: {form_data}")
        
    return render_template("auth/register.html")
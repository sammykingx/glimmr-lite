from . import accounts_bp
from flask import render_template, Response
from app.constants.templates_map import Templates


@accounts_bp.route("/profile")
def user_profile() -> Response:
    """
    Profile view  for the logged in user accounts.
    
    :return: HTTP Response containing rendered HTML template
    """
    return render_template(Templates.Dashboard.PROFILE, role="admin",)
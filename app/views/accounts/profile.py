from . import accounts_bp
from flask import render_template, Response


@accounts_bp.route("/profile")
def user_profile() -> Response:
    """
    Profile view  for the logged in user accounts.
    
    :return: HTTP Response containing rendered HTML template
    """
    return render_template("pages/accounts/user-profile.html", role="admin",)
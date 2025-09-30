from . import accounts_bp
from flask import render_template, Response


@accounts_bp.route("/dashboard")
def dashboard() -> Response:
    """
    Dashboard view  for user accounts.
    
    :return: HTTP Response containing rendered HTML template
    """
    return render_template("dashboards/s.html", role="admin",)
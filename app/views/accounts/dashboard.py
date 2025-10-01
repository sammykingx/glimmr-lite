from . import accounts_bp
from flask import render_template, Response
from flask_login import current_user, login_required


@accounts_bp.route("/dashboard")
@login_required
def dashboard() -> Response:
    """
    Dashboard view  for user accounts.
    
    :return: HTTP Response containing rendered HTML template
    """
    return render_template("dashboards/admin.html", role="admin", user=current_user,)
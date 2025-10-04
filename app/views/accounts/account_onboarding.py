from . import accounts_bp
from flask import render_template, Response, url_for
from flask_login import current_user, login_required
from app.constants.templates_map import Templates



@accounts_bp.route("/onboarding")
@login_required
def onboarding_user() -> Response:
    """
    Onboarding view  for user accounts.
    
    :return: HTTP Response containing rendered HTML template
    """

    return render_template(
        Templates.Dashboard.PROFILE,
        user=current_user,
    )
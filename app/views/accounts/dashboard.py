from . import accounts_bp
from flask import flash, render_template, Response, url_for
from flask_login import current_user, login_required
from app.constants.templates_map import Templates
from app.models.user_profile import UserRole


@accounts_bp.route("/dashboard")
@login_required
def dashboard() -> Response:
    """
    Dashboard view  for user accounts.
    
    :return: HTTP Response containing rendered HTML template
    """
    flash(
        {
            "title": "Profile Updated",
            "message": "Great work! Your profile is all set. You’re good to go!",
        }, "success")
    role_template_map = {
        UserRole.ADMIN: Templates.Dashboard.ADMIN,
        UserRole.MANAGER: Templates.Dashboard.MANAGER,
        UserRole.AGENT: Templates.Dashboard.AGENT,
        UserRole.CLIENT: Templates.Dashboard.CLIENT,
    }

    template = role_template_map.get(current_user.role, None)
    return render_template(
        template if template else Templates.Dashboard.CLIENT,
        user=current_user,
    )
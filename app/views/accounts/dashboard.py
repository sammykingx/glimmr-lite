from . import accounts_bp
from flask import render_template, Response
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
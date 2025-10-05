from . import accounts_bp
from flask import flash, render_template, Response
from flask_login import current_user, login_required
from app.constants.templates_map import Templates
from app.models.user_profile import UserRole



@accounts_bp.route("/onboarding")
@login_required
def onboarding_user() -> Response:
    """
    Renders the onboarding page for the current user based on their role
    (manager, agent, or client).

    :return: HTTP 200 HTML response with the appropriate onboarding template.
    """
    flash(
        {
            "title": "Profile Updated",
            "message": "Your profile information was successfully saved.",
        }, "info")
    role_template_map = {
        UserRole.MANAGER: Templates.Onboarding.MANAGERS,
        UserRole.AGENT: Templates.Onboarding.AGENTS,
        UserRole.CLIENT: Templates.Onboarding.CLIENTS,
    }
    template = role_template_map.get(current_user.role, None)
    # template = Templates.AGENT_AVAILABILITY
    return render_template(
        template if template else Templates.ONBOARDING.CLIENTS,
    )
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from app.security import APP_CSP_POLICY
from flask_mail import Mail
from flask_htmx import HTMX
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
talisman = Talisman()
csrf = CSRFProtect()
mail = Mail()
htmx = HTMX()
login_manager = LoginManager()


def init_extensions(app):
    db.init_app(app)
    migrate.init_app(
        app,
        db,
    )
    csrf.init_app(app)
    mail.init_app(app)
    htmx.init_app(app)
    # talisman.init_app(
    #     app,
    #     content_security_policy=APP_CSP_POLICY,
    #     content_security_policy_nonce_in=["script-src", "style-src"],
    #     # content_security_policy_report_only=True,  # Use this for testing
    #     frame_options="DENY",
    #     x_content_type_options="nosniff",
    #     # force_https=True,
    #     # strict_transport_security=True,
    #     # strict_transport_security_preload=True,
    #     # strict_transport_security_max_age=31536000,  # 1 year
    #     # strict_transport_security_include_subdomains=True
    # )
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    return app


@login_manager.user_loader
def load_user(user_id):
    """
        Given *user_id*, return the associated User object.
        :param unicode user_id: user_id (email) user to retrieve
    """
    from app.models.user_profile import UserProfile

    return UserProfile.query.get(user_id)

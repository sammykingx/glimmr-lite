from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from app.security import APP_CSP_POLICY
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
talisman = Talisman()
csrf = CSRFProtect()
mail = Mail()

def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db,)
    csrf.init_app(app)
    mail.init_app(app)
    # talisman.init_app(
    #     app,
    #     content_security_policy=APP_CSP_POLICY,
    #     content_security_policy_nonce_in=['script-src', 'style-src'],
    #     content_security_policy_report_only=True,  # Use this for testing
    # )
    
    return app
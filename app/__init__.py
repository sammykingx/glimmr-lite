from flask import Flask
from app.extensions import db, init_extensions
from app.config import DevelopmentConfig
from app.routes import main as main_blueprint
from app.views.auth import bp as auth_blueprint
from app.views.accounts import accounts_bp as accounts_blueprint
from app.accounts.admins import admin_bp as admin_blueprint


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)

    app.config.from_object(config_object)
    app = init_extensions(app)
    # talisman configurations

    with app.app_context():
        db.create_all()

    # register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(accounts_blueprint)
    app.register_blueprint(admin_blueprint)

    return app

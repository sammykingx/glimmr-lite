from flask import Flask
from app.extensions import db, init_extensions
from app.config import DevelopmentConfig
from app.routes import main as main_blueprint
from app.views.auth import bp as auth_blueprint
from app.views.accounts import accounts_bp as accounts_blueprint
from app.views.bookings import booking_bp as booking_blueprint
from app.views.goelocation import geo_bp as geolocation_blueprint
from app.views.coupons import coupons_bp as coupons_blueprint
from app.views.messages import msg_bp as messages_blueprint
from app.views.payments import pay_bp as payments_blueprint
from app import error_handler
from logging.handlers import RotatingFileHandler
import logging, os


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)

    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    app = init_extensions(app)
    

    with app.app_context():
        db.create_all()

    # register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(accounts_blueprint)
    app.register_blueprint(booking_blueprint)
    app.register_blueprint(geolocation_blueprint)
    app.register_blueprint(coupons_blueprint)
    app.register_blueprint(messages_blueprint)
    app.register_blueprint(payments_blueprint)
    
    # Logging configuration
    # if not os.path.exists('logs'):
    #     os.mkdir('logs')

    # file_handler = RotatingFileHandler(
    #     'logs/app.log', maxBytes=10240, backupCount=10
    # )
    # file_handler.setFormatter(logging.Formatter(
    #     '%(asctime)s [%(levelname)s] %(message)s in %(pathname)s:%(lineno)d'
    # ))
    # file_handler.setLevel(logging.ERROR)
    
    # register error handlers
    app.register_error_handler(400, error_handler.bad_request)
    app.register_error_handler(401, error_handler.unauthorized_request)
    app.register_error_handler(403, error_handler.forbidden_request)
    app.register_error_handler(404, error_handler.page_not_found)
    app.register_error_handler(405, error_handler.method_not_allowed)
    app.register_error_handler(500, error_handler.internal_server)
    
    return app

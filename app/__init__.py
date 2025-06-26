from flask import Flask
from app.extensions import init_extensions
from app.config import DevelopmentConfig
from app.routes import main as main_blueprint

def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    
    app.config.from_object(config_object)
    app = init_extensions(app)
    # talisman configurations
    
    # register blueprints
    app.register_blueprint(main_blueprint)
    
    

    return app
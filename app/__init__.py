from flask import Flask
from app.extensions import init_extensions
from app.config import DevelopmentConfig

def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    
    app.config.from_object(config_object)
    app = init_extensions(app)
    # talisman configurations
    
    

    return app
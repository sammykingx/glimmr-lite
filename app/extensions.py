from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
migrate = Migrate()
talisman = Talisman()
#csrf = CSRFProtect()

def init_extensions(app):
    # db.init_app(app)
    # migrate.init_app(app, db)
    #csrf.init_app(app)
    # talisman.init_app(app)
    
    return app
class Config:
    SECRET_KEY = 'my_secret_key'
    DEBUG = False
    DATABASE_URI = 'sqlite:///app.db'
    WTF_CSRF_ENABLED = True
    WTF_CSRF_METHODS = ["POST", "PUT", "PATCH", "DELETE"]
    WTF_CSRF_HEADERS = ['X-CSRFToken', 'X-CSRF-Token']

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass
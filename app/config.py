import os

class Config:
    SECRET_KEY = 'my_secret_key'
    DEBUG = False
    DATABASE_URI = 'sqlite:///app.db'
    WTF_CSRF_ENABLED = True
    WTF_CSRF_METHODS = ["POST"] # allowed methods for CSRF protection
    WTF_CSRF_HEADERS = ["X-CSRFToken",] # allowed headers for CSRF protection

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    WTF_CSRF_ENABLED = True
    PREFERRED_URL_SCHEME = 'https'
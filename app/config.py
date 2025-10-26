from dotenv import load_dotenv
import os


load_dotenv(override=True)
class Config:
    SECRET_KEY = (
        os.getenv("APP_SECRET_KEY")
        or "b6059dc8db3bcf7bd4e2dc3b01d8e57994b2275e101ad7bdd2a446482990df9b"
    )
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or "sqlite:///app.db"

    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.getenv("CSRF_SECRET_KEY")
    WTF_CSRF_TIME_LIMIT = 900  # 15 minutes in seconds
    SESSION_COOKIE_NAME = "glimmr_session"
    WTF_CSRF_METHODS = ["POST", "PUT", "PATCH", "DELETE"]
    WTF_CSRF_HEADERS = [
        "X-CSRFToken",
    ]

    # Flask-Mail configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = 465
    MAIL_USE_SSL = bool(os.getenv("MAIL_USE_SSL", "true"))
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")
    MAIL_MAX_EMAILS = int(os.getenv("MAIL_MAX_EMAILS", 20))


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PREFERRED_URL_SCHEME = "https"
    PERMANENT_SESSION_LIFETIME = 86400  # 1 day in seconds
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 20,  # Number of connections to keep open
        "max_overflow": 10,  # Extra connections beyond pool_size
        "pool_timeout": 30,  # Time in seconds to wait before giving up on getting a connection
        "pool_recycle": 1800,  # Recycle connections every 30 mins
        "pool_pre_ping": True,  # Check connection liveness before using
        "echo": False,  # No SQL logging in prod
        "future": True,  # Use SQLAlchemy 2.0 API style if desired
    }

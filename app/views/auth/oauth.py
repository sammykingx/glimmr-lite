from app.extensions import db
from flask_login import current_user
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.contrib.facebook import make_facebook_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from app.models.Oauth import OAuth

google_bp = make_google_blueprint(
    client_id="GOOGLE_CLIENT_ID",
    client_secret="GOOGLE_CLIENT_SECRET",
    scope=["profile", "email"],
    redirect_url="/login/google/authorized",
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user, user_required=True)
)

facebook_bp = make_facebook_blueprint(
    client_id="FACEBOOK_CLIENT_ID",
    client_secret="FACEBOOK_CLIENT_SECRET",
    scope=["email"],
    redirect_url="/login/facebook/authorized",
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user, user_required=True)
)
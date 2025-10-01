from app.extensions import db
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin


class OAuth(OAuthConsumerMixin, db.Model):
    __tablename__ = "oauth"

    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(
        db.String(50), db.ForeignKey("user_profiles.email"), nullable=False, index=True
    )
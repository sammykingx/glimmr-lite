from app.extensions import db
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin


class OAuth(OAuthConsumerMixin, db.Model):
    __tablename__ = "oauth"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user_profiles.id"), nullable=False, index=True
    )
    user_email = db.Column(
        db.string(50), db.ForeignKey("user_profiles.email"), nullable=False, index=True
    )
    user = db.relationship("UserProfile", backref="oauth_accounts")
import uuid
from flask import current_app
from sqlalchemy import Table
from sqlalchemy.orm import Session
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from app.constants import TORONRO_TZ
from datetime import datetime


class TokenManagerMixin:
    """
    Provides token generation and verification utilities for UserService or others.
    Supports one-time-use tokens by storing in DB.
    """

    def _get_serializer(self) -> URLSafeTimedSerializer:
        return URLSafeTimedSerializer(current_app.config["SECRET_KEY"])

    def generate_token(self, user_id: int, purpose: str = "general") -> str:
        """
        Generate a unique, signed, URL-safe token.
        Includes a UUID so every token is unique, even for same user.
        """
        token_uuid = uuid.uuid4().hex
        data = {"user_id": user_id, "uuid": token_uuid, "purpose": purpose}

        s = self._get_serializer()
        return s.dumps(data, salt=f"{purpose}-salt")

    def verify_token(self, token: str, max_age: int = 1800, purpose: str = "general") -> dict | bool:
        """
        Verify token validity and expiration.
        Returns payload dict if valid, else None.
        Enforces one-time use by checking DB.
        """
        s = self._get_serializer()
        try:
            data = s.loads(token, salt=f"{purpose}-salt", max_age=max_age)

        except SignatureExpired:
            return False
        except BadSignature:
            return False
        
        return data

    def is_token_used(self, token_uuid: str, model: Table) -> bool:
        """Check if a token UUID has already been used."""
    
        
        used = model.query.filter_by(reset_token=token_uuid, reset_token_used=True).first()
        return True if used else False

    def mark_token_used(self, token_uuid: str, model:Table, session: Session):
        """
        Store a used token in DB to enforce one-time use.
        """
        used = model.query.filter_by(reset_token=token_uuid).first()
        used.reset_token_used = True
        used.reset_token_used_at = datetime.now(tz=TORONRO_TZ)
        session.add(used)
        session.commit()

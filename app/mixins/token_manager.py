from flask import current_app
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
import uuid


class TokenManagerMixin:
    """
    Provides token generation and verification utilities for UserService or others.
    Supports one-time-use tokens by storing in DB.
    """

    def _get_serializer(self) -> URLSafeTimedSerializer:
        return URLSafeTimedSerializer(current_app.config["SECRET_KEY"])

    def generate_token(self) -> str:
        """
        Generate a unique, URL-safe token.
        
        THis token can further be serialized to encode data by the serializer method
        """
        return uuid.uuid4().hex

    def serialize_token(self, token, purpose) -> str:
        data = {"token": token, "purpose": purpose}
        s = self._get_serializer()
        return s.dumps(data, salt=f"{purpose}-salt")
        
    def verify_token(self, token: str, max_age: int = 3600, purpose: str = "general") -> dict | bool:
        """
        Verify token validity and expiration.
        Returns payload dict if valid, else None.
        
        Args:
            token: the token string which is a result from URLSafeTimedSerializer
            max_age: maximun age of the string in seconds, defaults to 3,600 which is 60 minutes
        """
        s = self._get_serializer()
        try:
            data = s.loads(token, salt=f"{purpose}-salt", max_age=max_age)

        except SignatureExpired:
            return False
        except BadSignature:
            return False
        
        return data

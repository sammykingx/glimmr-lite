from app.extensions import db
from sqlalchemy import func
from flask_login import UserMixin
from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    AGENT = "agent"
    Client = "client"
    
    
class UserProfile(db.Model, UserMixin):
    __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True, index=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.Client, nullable=False)
    profile_picture = db.Column(db.String(50), nullable=True)
    social_links = db.Column(db.JSON, nullable=True)
    oauth_accounts = db.relationship("OAuth", backref="user", lazy=True)
    addresses = db.relationship("UserAddress", backref="user", lazy=True)
    joined_at = db.Column(db.DateTime, default=func.now())
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    
    
    def get_id(self) -> str:
        return self.email
    
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"<UserProfile(first_name={self.first_name}, last_name={self.last_name}," \
               f" email={self.email}, phone={self.phone}, role={self.role})>"
               
    def __str__(self) -> str:
        return "{{'first_name': '%s', 'last_name': '%s', 'email': '%s', 'phone': '%s', 'role': '%s'}}" % (
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
            self.role
        )

    def to_dict(self):
        return {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "role": self.role.value,
            "is_active": self.is_active,
            "is_verified": self.is_verified,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            phone=data.get("phone"),
            role=data.get("role", UserRole.Client),
        )
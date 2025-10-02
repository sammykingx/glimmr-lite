# manage the user actions
# send reset link via mail
# reset user pwd
# change the pwd for logggeed in user
# update the prfile info
# user on-boarding steps
from flask import current_app
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from flask_sqlalchemy.query import Query, Pagination
from app.extensions import db
from app.extensions import mail
from app.models.user_profile import UserProfile, UserRole
from app.services.base_services import BaseService
from app.mixins.token_manager import TokenManagerMixin
from typing import Union


class UserService(BaseService, TokenManagerMixin):
    """
    Service class for managing users.
    Builds on BaseService with user-specific business logic.
    """
    def __init__(self):
        super().__init__(UserProfile)
        
    def get_user(self, user_email) -> UserProfile | None:
        """Fetch a user record by email.
        
        This could be current logged-in user or any user by email.
        
        :param email: User's email address.
        :return: UserProfile instance or None if not found.
        """
        return self.get_by_field("email", user_email)
    
    def get_users(self, role:Union[UserRole, None]=None, page:int=1, per_page:int=7) -> Pagination:
        """Fetch multiple users, optionally filtered by role."""
        query:Query = self.model.query
        if role:
            query = query.filter_by(role=role)
        return query.paginate(page=page, per_page=per_page, error_out=False)

    def create_user(self, is_admin=False, **kwargs) -> UserProfile:
        """
        Create a new user if not exists, else return existing.
        Handles password hashing.
        """
        user_obj = UserProfile(
            **kwargs, role=UserRole.ADMIN if is_admin else UserRole.CLIENT
        )
        user_obj.hash_pwd()
        return self.create("email", kwargs.get("email"), user_obj)
    
    def update_user(self, user: UserProfile, **kwargs) -> UserProfile:
        """Update user profile details."""
        return self.update(user, **kwargs)

    def delete_user(self, user: UserProfile, soft_delete: bool = True):
        if soft_delete:
            user.is_active = False
            db.session.commit()
            return user
        return self.delete(user)

    def assign_role(self, user_obj: UserProfile, role: str) -> UserProfile:
        """Assign a role to a user."""
        user_obj.role = role
        db.session.commit()
        return user_obj

    def generate_reset_token(user_id: int) -> str:
        import uuid
        s = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        token = uuid.uuid4().hex
        return s.dumps(
            {
                "user_id": user_id,
                "token": token,
            }, salt="password-reset-salt")

    def send_password_reset_email(self, email: str) -> bool:
        # notification service should handle email
        # just load the email template message
        user = self.get_by_field("email", email)
        if not user:
            return False

        email_msg = None
        try:
            msg = Message(
                subject="Password Reset Request",
                recipients=[email],
                html=email_msg
            )
            mail.send(msg)
    
        except Exception as e:
            return False
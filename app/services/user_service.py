# manage the user actions
# send reset link via mail
# reset user pwd
# change the pwd for logggeed in user
# update the prfile info
# user on-boarding steps
from flask import render_template, url_for
from flask_mail import Message
from flask_sqlalchemy.query import Query, Pagination
from app.extensions import db
from app.extensions import mail
from app.models.user_profile import UserProfile, UserRole
from app.services.base_services import BaseService
from app.mixins.token_manager import TokenManagerMixin
from datetime import datetime, timedelta
from typing import Union


class UserService(BaseService, TokenManagerMixin):
    """
    Service class for managing users.
    Builds on BaseService with user-specific business logic.
    """
    def __init__(self):
        super().__init__(UserProfile)
        
    def get_user(self, unique_field_name, field_value) -> UserProfile | None:
        """
            Retrieve a user record from the database.

            This method returns a single user matching the given field/value pair. 
            The field must be unique (e.g., email, reset_token, id). If the field is 
            not unique, the first matching record will be returned.

            Args:
                unique_field_name: The column name to filter by (must be unique for accurate results).
                field_value: The value to match against the specified field.

            Returns:
                A UserProfile instance if a matching record exists, otherwise None.
        """
        return self.get_by_field(unique_field_name, field_value)
    
    def get_users_by(self, page:int=1, per_page:int=7, **kwargs) -> Pagination:
        """Fetch multiple users, optionally filtered by kwargs"""
        query:Query = self.model.query
        if kwargs:
            query = query.filter_by(**kwargs)
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

    def save_user_token(self, user: UserProfile) -> Union[str, None]:
        """
            Generate and save a unique reset token for the user.
            Enforces one-time use and 7-day cooldown after usage.

            :param user: UserProfile instance
            :return: Token string or None if cooldown not passed
        """
        if user.reset_token and not user.reset_token_used:
            return user.reset_token

        if user.reset_token_used and user.reset_token_used_at:
            cooldown_until = user.reset_token_used_at + timedelta(days=7)
            if datetime.now() < cooldown_until:
                return None

        token = self.generate_token()
        self.update(user, reset_token=token)
        return token

    def send_reset_email(self, user: UserProfile, token: str) -> bool:
        reset_token = self.serialize_token(token, purpose="password reset")

        if not user or not isinstance(user, UserProfile):
            raise ValueError("The user object is required")

        email_msg = render_template(
            "email/auth/password-reset.html",
            reset_url = url_for("auth.reset_password", verf_id=reset_token)
        )
        # send email via mail notification service
        try:
            msg = Message(
                subject="Password Reset Request",
                recipients=[user.email],
                html=email_msg
            )
            mail.send(msg)
    
        except Exception as e:
            return False
        
        return True
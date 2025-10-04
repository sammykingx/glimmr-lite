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
from app.services.notification_service import EmailService
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
            Create and persist a new user profile, or return an existing one.

            This method initializes a `UserProfile` object with the provided keyword
            arguments, assigns the appropriate role (admin or client), hashes the
            supplied password, and attempts to create the user in the database.
            If a user with the same unique field (e.g., email) already exists,
            the existing record is returned instead of creating a duplicate.

            Args:
                is_admin (bool, optional): Flag indicating whether the new user should
                    be assigned the `ADMIN` role. Defaults to False (assigned `CLIENT` role).
                **kwargs: Arbitrary keyword arguments corresponding to `UserProfile`
                    fields (e.g., `email`, `password`, `full_name`, etc.).

            Returns:
                UserProfile: The newly created `UserProfile` object, or the existing one
                if a user with the same unique identifier already exists.

            Raises:
                ValueError: If required fields (e.g., `email`, `password`) are missing
                in `kwargs`.
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

    def send_user_token(
        self, 
        user: UserProfile,
        template_name: str,
        token_purpose: str,
        token: str, 
        subject: str,
        **kwargs
    ) -> bool:
        """
            Generate an email with a serialized token and send it.
        
            Args:
                user (UserProfile): The user receiving the email.
                token (str): The token to include in the email.
                template_name (str): The Jinja2 template for rendering the email.
                token_purpose (str): Purpose of the token (e.g., "reset", "verify").
                subject (str): Email subject line.
                **kwargs: Additional context for the template.

            Returns:
                bool: True if sent successfully, False otherwise.
        """
        serialized_token = self.serialize_token(token, purpose=token_purpose)

        if not user or not isinstance(user, UserProfile):
            raise ValueError("The user object is required")

        email_msg = render_template(
            template_name,
            url = url_for("auth.reset_password", verf_id=serialized_token, _external=True),
            **kwargs
        )
        
        return EmailService.send_email(
            subject=subject,
            to_email=user.email,
            html_content=email_msg
        )
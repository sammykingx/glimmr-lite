from flask import Blueprint

accounts_bp = Blueprint("accounts", __name__, url_prefix="/user")

from . import dashboard, profile, role_views, account_onboarding
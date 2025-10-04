# app/constants/templates_map.py

class Templates:
    """Central registry for template names."""

    class Auth:
        LOGIN = "auth/login.html"
        REGISTER = "auth/register.html"
        FORGOT_PASSWORD = "auth/forgot-password.html"
        RESET_PASSWORD = "auth/reset-password.html"

    class Emails:
        VERIFICATION = "email/auth/verify-account.html"
        PASSWORD_RESET = "email/auth/password-reset.html"
        WELCOME = "email/welcome-email.html"

    class Payments:
        SUCCESS = "payments/success.html"
        CANCELLED = "payments/cancelled.html"
        PROCESSING = "payments/processing.html"

    class Dashboard:
        ADMIN = "dashboards/admin.html"
        AGENT = "dashboards/agent.html"
        CLIENT = "dashboards/clients.html"
        MANAGER = "dashboards/manager.html"
        SETTINGS = "dashboard/settings.html"
        PROFILE = "pages/accounts/user-profile.html"

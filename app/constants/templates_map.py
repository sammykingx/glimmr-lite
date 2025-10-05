# app/constants/templates_map.py

class Templates:
    """Central registry for template names."""

    AGENT_AVAILABILITY = "htmx-partials/agent-availability.html"
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
        
        
    class Onboarding:
        AGENTS = "pages/onboarding/onboard-agents.html"
        CLIENTS = "pages/onboarding/onboard-clients.html"
        MANAGERS = "pages/onboarding/onboard-managers.html"
        
    
    class Errors:
        ERROR_400 = "errors/error-400.html"
        ERROR_401 = "errors/error-401.html"
        ERROR_403 = "errors/error-403.html"
        ERROR_404 = "errors/error-404.html"
        ERROR_405 = "errors/error-405.html"
        ERROR_500 = "errors/error-500.html"

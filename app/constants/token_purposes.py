# app/constants/token_purposes.py

class TokenPurposes:
    """Centralized registry for all token purposes in the app."""

    # Authentication & Security
    EMAIL_VERIFICATION = "email_verification"
    PASSWORD_RESET = "password_reset"
    MAGIC_LOGIN = "magic_login"

    # Payments
    PAYMENT_CONFIRMATION = "payment_confirmation"
    PAYMENT_REFUND = "payment_refund"

    # Bookings
    BOOKING_CONFIRMATION = "booking_confirmation"
    BOOKING_CANCELLATION = "booking_cancellation"

    # Notifications / Misc
    API_ACCESS = "api_access"
    INVITE = "invite"
    

# app/constants/email_headers.py

class EmailHeaders:
    """Centralized registry for email subjects/headers."""

    class Auth:
        VERIFY_EMAIL = r"Verify Your Email Address"
        PASSWORD_RESET = r"Password Reset Request"
        WELCOME = r"Welcome to Our Platform"

    class Payments:
        PAYMENT_SUCCESS = r"Your Payment Was Successful"
        PAYMENT_FAILED = r"Payment Failed – Please Try Again"
        PAYMENT_PENDING = r"Your Payment is Processing"

    class Notifications:
        BOOKING_CONFIRMED = r"Your Booking Has Been Confirmed"
        BOOKING_CANCELLED = r"Booking Cancelled"
        BOOKING_REMINDER = r"Reminder: Upcoming Booking"

from flask import Blueprint

booking_bp = Blueprint("booking", __name__, url_prefix="/bookings")

from . import booking_routes, service_listing
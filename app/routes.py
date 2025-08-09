from flask import Blueprint, current_app, jsonify, request, render_template
from flask_wtf.csrf import CSRFError, validate_csrf
from app.extensions import htmx
from app.models import User
from app.utils import booking_data_serializer, ValidateBookingData
from app.services.booking_service import BookingService
from app.helpers import demo_booking_data
from pydantic import ValidationError
from app.constants import ALLOWED_SERVICE

main = Blueprint("main", __name__)


@main.route("/booking", methods=["POST"])
def place_booking():

    try:
        csrf_token = request.headers.get("X-CSRFToken")
        validate_csrf(csrf_token)

        data = booking_data_serializer(request.get_json())
        cleaned_data = ValidateBookingData(**data)
        Booking = BookingService(cleaned_data)
        # booked_service = Booking.place_booking()

    except CSRFError as e:
        # return jsonify({'status': 'error', 'message': 'CSRF validation failed'}), 403
        return (
            jsonify(
                {
                    "status": "Error",
                    "message": "Looks like your session timed out. Please refresh the page to fix this.",
                }
            ),
            403,
        )

    except ValidationError as e:
        current_app.logger.error(f"Validation error: {e}", exc_info=True)
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Booking not completed. Please correct the fields and try again.",
                }
            ),
            422,
        )

    except Exception as e:
        current_app.logger.error(f"Unexpected error: {e}", exc_info=True)
        return (
            jsonify(
                {
                    "status": "Error",
                    "message": "Something went wrong on our end. Please try again shortly",
                }
            ),
            500,
        )

    return jsonify(
        {
            "status": "success",
            "message": "Booking Successfull",
            # "checkout_url": "https://oliveglitters.com",  # booked_service.to_dict() if booked_service else None,
        }
    )


@main.route("/demo-data")
def return_demo_data():
    demo_data = demo_booking_data.create_sample_data()

    return jsonify(demo_data)


@main.route("/available-slots")
def retrun_available_slots():
    from app.booking_availability import generate_sample_availability

    return jsonify(generate_sample_availability())


@main.route("/service-options/<category>")
def render_service_options(category):
    if not htmx or category not in ALLOWED_SERVICE.keys():
        return "", 400

    return render_template(
        "htmx-partials/services-selection.html",
        service=ALLOWED_SERVICE.get(category),
    )

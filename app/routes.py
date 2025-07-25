from flask import Blueprint, jsonify, request, render_template
from flask_wtf.csrf import CSRFError, validate_csrf
from app.extensions import db, htmx
from app.models import User
from app.utils import booking_data_serializer, ValidateBookingData
from app.services.booking_service import BookingService
from pydantic import ValidationError
from app.constants import ALLOWED_FREQUENCIES, ALLOWED_SERVICE, ALLOWED_SERVICE_ADDONS

main = Blueprint('main', __name__)

@main.route('/booking', methods=['POST'])
def place_booking():
    
    try:
        csrf_token = request.headers.get('X-CSRFToken')
        validate_csrf(csrf_token)
    
        data = booking_data_serializer(request.get_json())
        # cleaned_data = ValidateBookingData(**data)
        # Booking = BookingService(cleaned_data)
        # booked_service = Booking.place_booking()

    except CSRFError as e:
      # return jsonify({'status': 'error', 'message': 'CSRF validation failed'}), 403
      return jsonify({
        "status": "Error",
        "message": "Looks like your session timed out. Please refresh the page to fix this.",
      }), 403
    
    except ValidationError as e:
      print(e)
      return jsonify({
        "status": "error",
        "message": "Booking not completed. Please correct the fields and try again.",
        }), 422
      
    except Exception as e:
      return jsonify({
        "status": "Error",
        "message": "Something went wrong on our end. Please try again shortly",
      }), 500
    
    
    return jsonify(
        {
            'status': 'success',
            'message': 'Booking Successfull',
            # 'checkout_url': "https://oliveglitters.com",#booked_service.to_dict() if booked_service else None,
        }
    )

@main.route("/demo-data")
def return_demo_data():
  demo_data = create_sample_data()
  
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

from faker import Faker
    
faker = Faker("en_CA")

# Sample data for testing
# This data is used to test the booking endpoint.
def create_sample_data():
    """Creates sample data for testing the booking endpoint."""
    from datetime import datetime
    
    return {
        "category": faker.random_element(elements=ALLOWED_SERVICE.keys()),
        "service": faker.random_element(elements=ALLOWED_SERVICE.values()),
        "bedrooms": faker.random_int(min=1, max=6),
        "bathrooms": faker.random_int(min=1, max=3),
        "frequency": faker.random_element(elements=ALLOWED_FREQUENCIES),
        "addOns": [faker.random_element(elements=ALLOWED_SERVICE_ADDONS) for _ in range(faker.random_int(min=0, max=3))],
        "selectedDate": datetime.now().date(),
        "selectedTime": str(datetime.now().time()),
        "personalInfo": {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "phone": faker.phone_number(),
        },
        "address": {
            "street": faker.street_address(),
            "city": faker.city(),
            "state": faker.administrative_unit(),
            "zipCode": faker.postalcode(),
        },
        "price": float(faker.random_element(elements=[faker.pydecimal(left_digits=2, right_digits=2, positive=True) for _ in range(10)])),
        "additionalInfo": faker.sentence(),
    }

def bad_demo_data():
  return {
    "category": "Standard Cleaning", # Invalid category
    "service": "Regular House Cleaning", # Invalid service
    "bedrooms": 1,
    "bathrooms": 1,
    "frequency": "weekly",
    "addOns": [],
    "selectedDate": "2025-06-30",
    "selectedTime": "10:00",
    "personalInfo": {
      "firstName": "Moon",
      "lastName": "Chaser",
      "email": "nelly@mailer.com",
      "phone": "08056109384",
    },
    "address": {
      "street": faker.street_address(),
      "city": faker.city(),
      "state": faker.state(),
      "zipCode": faker.zipcode(),
    },
    "additionalInfo": "no additional info"
  }

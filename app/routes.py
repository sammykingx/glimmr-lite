from flask import Blueprint, jsonify, request
from flask_wtf.csrf import CSRFError, validate_csrf
from app.extensions import db
from app.models import User
from app.utils import booking_data_serializer, ValidateBookingData
from app.services.booking_service import BookingService
from pydantic import ValidationError
from app.constants import ALLOWED_FREQUENCIES, ALLOWED_SERVICE_CATEGORY, ALLOWED_SERVICE_TYPE, ALLOWED_SERVICE_ADDONS

main = Blueprint('main', __name__)

@main.route('/booking', methods=['POST'])
def place_booking():
    
    try:
    #     csrf_token = request.headers.get('X-CSRFToken')
    #     validate_csrf(csrf_token)  # Manual validation
    
        data = booking_data_serializer(create_sample_data())
        cleaned_data = ValidateBookingData(**data)
        Booking = BookingService(cleaned_data)
        booked_service = Booking.place_booking()

    except CSRFError as e:
      # return jsonify({'status': 'error', 'message': 'CSRF validation failed'}), 403
      return "", 403
    
    except ValidationError as e:
      return "validation error", 422
      
    # except Exception as e:
    #   return "", 500
    
    return jsonify(
        {
            'status': 'success',
            'message': 'Booking saved',
            'data': booked_service.to_dict() if booked_service else None,
        }
    )

# Sample data for testing
# This data is used to test the booking endpoint.
def create_sample_data():
    """Creates sample data for testing the booking endpoint."""
    from datetime import datetime, timedelta
    from faker import Faker
    
    faker = Faker()
    
    return {
        "category": faker.random_element(elements=ALLOWED_SERVICE_CATEGORY),
        "service": faker.random_element(elements=ALLOWED_SERVICE_TYPE),
        "bedrooms": faker.random_int(min=1, max=6),
        "bathrooms": faker.random_int(min=1, max=3),
        "frequency": faker.random_element(elements=ALLOWED_FREQUENCIES),
        "addOns": [faker.random_element(elements=ALLOWED_SERVICE_ADDONS) for _ in range(faker.random_int(min=0, max=3))],
        "cleaningDate": datetime.now().date(),
        "cleaningTime": datetime.now().time(),
        "personalInfo": {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "phone": faker.phone_number(),
        },
        "address": {
            "street": faker.street_address(),
            "city": faker.city(),
            "state": faker.state(),
            "zipCode": faker.zipcode(),
        },
        "price": float(faker.random_element(elements=[faker.pydecimal(left_digits=2, right_digits=2, positive=True) for _ in range(10)])),
        "additionalInfo": faker.sentence(),
    }
    
bad_data = {
  "category": "Standard Cleaning", # Invalid category
  "service": "Regular House Cleaning", # Invalid service
  "bedrooms": 1,
  "bathrooms": 1,
  "frequency": "weekly",
  "addOns": [],
  "cleaningDate": "2025-06-30",
  "cleaningTime": "10:00",
  "personalInfo": {
    "firstName": "Moon",
    "lastName": "Chaser",
    "email": "nelly@mailer.com",
    "phone": "08056109384",
  },
  "address": {
    "street": "49 Baale Street, Lagos,Nigeria",
    "city": "Lagos",
    "state": "Lagos",
    "zipCode": "00035",
  },
  "additionalInfo": "no additional info"
}

good_data = {
  "category": "residential",
  "service": "standard-cleaning",
  "bedrooms": 1,
  "bathrooms": 1,
  "frequency": "weekly",
  "addOns": [],
  "cleaningDate": "2025-06-30",
  "cleaningTime": "10:00",
  "personalInfo": {
    "firstName": "Moon",
    "lastName": "Chaser",
    "email": "johndoe@user.com",
    "phone": "08056109384",
  },
  "address": {
    "street": "49 Baale Street, Lagos,Nigeria",
    "city": "Lagos",
    "state": "Lagos",
    "zipCode": "00035",
  },
  "additionalInfo": "no additional info in the booking",
}
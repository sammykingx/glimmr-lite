from flask import Blueprint, jsonify, request
from flask_wtf.csrf import CSRFError, validate_csrf
from app.extensions import db
from app.models import User
from app.utils import booking_data_serializer
from app.services.booking_service import BookingService


main = Blueprint('main', __name__)

@main.route('/booking', methods=['POST'])
def place_booking():
    
    print("Received booking request")
    try:
        csrf_token = request.headers.get('X-CSRFToken')
        validate_csrf(csrf_token)  # Manual validation

    except CSRFError as e:
        return jsonify({'status': 'error', 'message': 'CSRF validation failed'}), 400
    
    data = booking_data_serializer(request.get_json())
    
    try:
        Booking = BookingService(data)
        booked_service = Booking.create_booking()
        
    except Exception as e:
        return jsonify(
          {
            'status': 'error',
            'message': str(e)
          }
        ), 400

    print("Booking data received:", data)
    
    return jsonify(
        {
            'status': 'success',
            'message': 'Booking saved',
            'data': booked_service.to_dict() if booked_service else None,
        }
    )
'''
booking_data = {
  "category": "Standard Cleaning",
  "service": "Regular House Cleaning",
  "bedrooms": 1,
  "bathrooms": 1,
  "frequency": "weekly",
  "addOns": [],
  "cleaningDate": "2025-06-30",
  "cleaningTime": "10:00",
  "personalInfo": {
    "firstName": "Moon",
    "lastName": "Chaser",
    "email": "finsec@napsuniben.com",
    "phone": "08056109384"
  },
  "address": {
    "street": "49 Baale Street, Lagos,Nigeria",
    "city": "lagos",
    "state": "lagos",
    "zipCode": "00035",
  },
  "additionalInfo": "no additional info"
}
'''    
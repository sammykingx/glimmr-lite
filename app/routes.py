from flask import Blueprint, jsonify, render_template, request
from app.extensions import db
from app.models import User
from flask_wtf.csrf import CSRFError, validate_csrf

main = Blueprint('main', __name__)

@main.route('/booking', methods=['POST'])
def place_booking():
    
    try:
        csrf_token = request.headers.get('X-CSRFToken')
        validate_csrf(csrf_token)  # Manual validation

        data = request.get_json()

    except CSRFError as e:
        return jsonify({'status': 'error', 'message': 'CSRF validation failed'}), 400
    
    # Process your booking data
    # booking handling logic here
    
    return jsonify(
        {
            'status': 'success',
            'message': 'Booking saved',
            'data': data,
        }
    )
'''
booking_data ={
  "category": "Standard Cleaning",
  "service": "Regular House Cleaning",
  "bedrooms": 1,
  "bathrooms": 1,
  "frequency": "weekly",
  "addOns": [],
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
    "date": "2025-06-25",
    "time": "14:09"
  },
  "additionalInfo": "no additional info"
}
'''    
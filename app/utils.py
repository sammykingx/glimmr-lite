from app.constants import ALLOWED_SERVICE_TYPE, ALLOWED_SERVICE_CATEGORY, ALLOWED_FREQUENCIES, ALLOWED_SERVICE_ADDONS
from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime
from typing import Dict, List, Tuple, Union
from datetime import date, time


def booking_data_serializer(booking_data: Dict) -> Dict:
    """Serializes booking data to a dictionary."""
    return {
        "service": booking_data.get("service"),
        "service_category": booking_data.get("category"),
        "bedrooms": booking_data.get("bedrooms"),
        "bathrooms": booking_data.get("bathrooms"),
        "frequency": booking_data.get("frequency", "one-off"),
        "add_ons": booking_data.get("addOns", []),
        "booking_date": booking_data.get("cleaningDate"),
        "booking_time": booking_data.get("cleaningTime"),
        "price": booking_data.get("price", 0.0),
        "user_info": booking_data.get("personalInfo", {}),
        "address": booking_data.get("address", {}),
        "additional_info": booking_data.get("additionalInfo", "")
    }
class ValidateBookingData(BaseModel):
    service: str
    service_category: str
    bedrooms: int
    bathrooms: int
    frequency: str = "one-off"
    add_ons: Union[List[str], Tuple[str, ...]] = None
    booking_date: Union[date, str] = None  # ISO format date string
    booking_time: Union[time,str]
    price:float = 0.0
    user_info: Dict[str, str]
    address: Dict[str, str]
    additional_info: str = None
    
    @field_validator('user_info', mode='before')
    def validate_user_info(cls, user_payload):
        """Validates the user info dictionary."""
        
        if not isinstance(user_payload, dict):
            raise ValueError("User info must be a dictionary.")
        
        required_fields = ['firstName', 'lastName', 'email', 'phone']
        if user_payload.keys() not in required_fields:
            raise ValueError(f"User info must contain the following fields: {required_fields}")
        
        for field in list(user_payload.values()):
            if field.strip() == "":
                raise ValueError(f"{field} is required for the user.")
        
        return user_payload
    
        
    @field_validator('service', mode='before')
    def validate_services(cls, value):
        if not value.strip():
            raise ValueError("Service is required.")
        
        if value.lower() not in ALLOWED_SERVICE_TYPE:
            raise ValueError("Invalid service type.")
        
        return value.strip()
    
    @field_validator('service_category', mode='before')
    def validate_service_category(cls, value):
        if not value.strip():
            raise ValueError("Service category is required.")
        
        if value.lower() not in ALLOWED_SERVICE_CATEGORY:
            raise ValueError("Invalid service category.")
        
        return value.strip()
    
    @field_validator('frequency', mode='before')
    def validate_frequency(cls, value):
        if not value.strip():
            raise ValueError("Frequency is required.")
        
        if value.lower() not in ALLOWED_FREQUENCIES:
            raise ValueError("Invalid frequency.")
        
        return value.strip()
    
    @field_validator('booking_date', mode='before')
    def validate_booking_date(cls, value):
        if isinstance(value, str):
            try:
                value = datetime.fromisoformat(value).date()
            except ValueError:
                raise ValueError("Invalid date format. Use ISO format (YYYY-MM-DD).")
        
        elif not isinstance(value, date):
            raise ValueError("Booking date must be a valid date.")
        
        if value < date.today():
            raise ValueError("Booking date cannot be in the past.")
        
        if value.weekday() == 6:  # Sunday
            raise ValueError("Bookings cannot be made on Sundays.")
        
        # booking date can only be 45 days days into the future frnom today
        if (value - date.today()).days > 45:
            raise ValueError("Booking date cannot be more than 45 days in the future.")
        
        return value
    
    @field_validator('bedrooms', 'bathrooms', mode='before')
    def validate_bedrooms_bathrooms(cls, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Bedrooms and bathrooms must be non-negative integers.")
        
        return value
    
    @field_validator('add_ons', mode='before')
    def validate_add_ons(cls, value):
        if value is None:
            return []
        
        if isinstance(value, str):
            value = [v.strip() for v in value.split(',')]
        
        if not isinstance(value, (list, tuple)):
            raise ValueError("Add-ons must be a list or tuple.")
        
        if value.lower() not in ALLOWED_SERVICE_ADDONS:
            raise ValueError(f"Invalid add-on: {value}. Allowed add-ons are: {ALLOWED_SERVICE_ADDONS}")
        
        return value
    
    @field_validator("price", mode='before')
    def validate_price(cls, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number.")
        
        return value
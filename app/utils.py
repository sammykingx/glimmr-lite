from app.constants import (
    ALLOWED_SERVICE,
    ALLOWED_FREQUENCIES,
    ALLOWED_SERVICE_ADDONS,
    RESIDENTIAL_SERVICE_PRICING,
)
from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Dict, List, Tuple, Union
from datetime import date, time


def booking_data_serializer(booking_data: Dict) -> Dict:
    """Serializes booking data to a dictionary."""

    user_info = {
        "first_name": booking_data.get("personalInfo", {}).get("firstName", ""),
        "last_name": booking_data.get("personalInfo", {}).get("lastName", ""),
        "email": booking_data.get("personalInfo", {}).get("email", ""),
        "phone": booking_data.get("personalInfo", {}).get("phone", ""),
    }

    address = {
        "street": booking_data.get("address", {}).get("street", ""),
        "city": booking_data.get("address", {}).get("city", ""),
        "state": booking_data.get("address", {}).get("state", ""),
        # "country": booking_data.get("address", {}).get("country", ""),
    }

    return {
        "service": booking_data.get("service"),
        "category": booking_data.get("category"),
        "bedrooms": booking_data.get("bedrooms"),
        "bathrooms": booking_data.get("bathrooms"),
        "frequency": booking_data.get("frequency"),
        "add_ons": booking_data.get("addOns", []),
        "booking_date": booking_data.get("selectedDate"),
        "booking_time": booking_data.get("selectedTime"),
        "price": booking_data.get("price", 0.0),
        "payment_method": booking_data.get("paymentMethod", "interac"),
        "user_info": user_info,
        "address": address,
        "additional_info": booking_data.get("additionalInfo", ""),
    }


class ValidateBookingData(BaseModel):
    service: str
    category: str
    bedrooms: Union[int, str]
    bathrooms: Union[int, str]
    frequency: str
    add_ons: List[Dict[str, Union[str, int]]]
    booking_date: Union[date, str] = None  # ISO format date string
    booking_time: Union[time, str]
    price: float = 0.0
    payment_method: str
    user_info: Dict[str, str]
    address: Dict[str, str]
    additional_info: str = None

    @field_validator("user_info", mode="before")
    @classmethod
    def validate_user_info(cls, user_payload):
        """Validates the user info dictionary."""

        if not isinstance(user_payload, dict):
            raise ValueError("User info must be a dictionary.")

        for field in list(user_payload.values()):
            if field.strip() == "":
                raise ValueError(f"{field} is required for the user.")

        return user_payload

    @field_validator("category", mode="before")
    @classmethod
    def validate_service_category(cls, value):
        if not value.strip():
            return ValueError("Service category is required.")

        if value.lower() not in ALLOWED_SERVICE.keys():
            return ValueError("Invalid service category.")

        return value.strip().lower()
    
    @field_validator("bedrooms", mode="before")
    @classmethod
    def validate_bedrooms(cls, value):
        if isinstance(value, str):
            if not value.isdigit() or int(value) < 0:
                raise ValueError("Bedrooms must be a non-negative integer.")
            value = int(value)
            
        elif not isinstance(value, int) or value < 0:
            raise ValueError("Bedrooms must be a non-negative integer.")
        
        if value not in range(7):
            raise ValueError("Bedrooms must be between 0 and 6.")
        
        return value
    
    @field_validator("bathrooms", mode="before")
    @classmethod
    def validate_bathrooms(cls, value):
        # if bathrooms is a string and not equall to 'studio' raise error
        # if the bathrooms is a postive integer greater than 3 then raise error
        if isinstance(value, str):
            if value.strip().lower() != "studio":
                raise ValueError("Bathrooms must be 'studio' or a non-negative integer.")
            
        elif not isinstance(value, int) or value < 0:
            raise ValueError("Bathrooms must be a non-negative integer or 'studio'.")
        
        return value
    
    @field_validator("frequency", mode="before")
    @classmethod
    def validate_frequency(cls, value):
        if not value.strip():
            raise ValueError("Frequency is required.")

        if value.lower() not in set(ALLOWED_FREQUENCIES):
            raise ValueError("Invalid frequency.")

        return value.strip()

    @field_validator("booking_date", mode="before")
    @classmethod
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

        # if value.weekday() == 6:  # Sunday
        #     raise ValueError("Bookings cannot be made on Sundays.")

        # booking date can only be 45 days days into the future frnom today
        if (value - date.today()).days > 45:
            raise ValueError("Booking date cannot be more than 45 days in the future.")

        return value

    @field_validator("add_ons", mode="before")
    @classmethod
    def validate_add_ons(cls, value):
        # disabling addons validation for now
        return value

    @field_validator("price", mode="before")
    @classmethod
    def validate_price(cls, value):
        if not isinstance(value, float) or value < 0:
            raise ValueError("Price must be a non-negative decimal.")

        return value

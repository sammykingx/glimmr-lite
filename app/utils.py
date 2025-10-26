from app.constants.services import ALLOWED_SERVICE, ALLOWED_FREQUENCIES
from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Dict, List, Tuple, Union
from datetime import date, time


def booking_data_serializer(booking_data: Dict) -> Dict:
    """Serializes booking data to a dictionary."""
    
    cleaning_date = datetime.strptime(
        f"{booking_data.get("selectedDate")} {booking_data.get("selectedTime")}",
        "%Y-%m-%d %H:%M"
    )

    user_info = {
        "first_name": booking_data.get("personalInfo", {}).get("firstName", ""),
        "last_name": booking_data.get("personalInfo", {}).get("lastName", ""),
        "email": booking_data.get("personalInfo", {}).get("email", ""),
        "phone": booking_data.get("personalInfo", {}).get("phone", ""),
    }

    address = {
        "street_line_1": booking_data.get("address", {}).get("street", ""),
        "city": booking_data.get("address", {}).get("city", ""),
        "state": booking_data.get("address", {}).get("state", ""),
        "country": "canada", #booking_data.get("address", {}).get("country", ""),
    }

    print(f"Date payload: {booking_data.get("selectedDate")}, Time payload: {booking_data.get("selectedTime")}")
    return {
        "service": booking_data.get("service"),
        "service_category": booking_data.get("category"),
        "bedrooms": booking_data.get("bedrooms"),
        "bathrooms": booking_data.get("bathrooms"),
        "frequency": booking_data.get("frequency"),
        "add_ons": booking_data.get("addOns", []),
        "cleaning_date": cleaning_date,
        "price": float(booking_data.get("price", 0.0)),
        # "payment_method": booking_data.get("paymentMethod", "interac"),
        "user_info": user_info,
        "address": address,
        "additional_info": booking_data.get("additionalInfo", ""),
    }


class ValidateBookingData(BaseModel):
    service: str
    service_category: str
    bedrooms: Union[int, str]
    bathrooms: Union[int, str]
    frequency: str
    add_ons: List[Dict[str, Union[str, int]]]
    cleaning_date: datetime
    price: float = 0.0
    # payment_method: str
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

    @field_validator("service", mode="before")
    @classmethod
    def validate_service(cls, value):
        if not value.strip():
            return ValueError("Service is required.")

        return value.strip().lower()

    @field_validator("service_category", mode="before")
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
        if isinstance(value, str):
            err_msg = "Bathrooms must be a non-negative integer or 'studio'."
            if value.isdigit():
                if int(value) < 0:
                    raise ValueError(err_msg)
                value = int(value)
                
            elif value.strip().lower() != "studio":
                raise ValueError(err_msg)
            
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

        return value.strip().lower()

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

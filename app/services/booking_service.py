# Booking Service Module
# This module handles the booking process, including validation, saving to the database,
# payment processing, and notifications.

from app.models import Address, Booking, RecurringBooking, User, db
from app.utils import ValidateBookingData
from app.services.payment_service import PaymentGateway
from app.services.notification_service import NotificationService


class BookingService:
    def __init__(self, booking_data:dict) -> None:
        self.clean_data = ValidateBookingData(**booking_data)
        self.booking_info = self.clean_data.model_dump()
        self.user_info = self.booking_info.pop("user_info", {})
        self.address = self.booking_info.pop("address", {})
        self.recurring_booking = True if self.booking_info.get("frequency") != "one-off" else False
        self.booking_info["recurring"] = self.recurring_booking
        self.booking = None
        self.user = None

    def create_or_get_user(self):
        """Creates or returns a new user if not already exists."""
        
        # gets user record by email if the user object is not set
        if not self.user:
            self.user = User.query.filter_by(email=self.user_info.get("email")).first()
            
            # if user does not exist in the db, create a new one
            if not self.user:
                self.user = User(**self.user_info)
                db.session.add(self.user)
                db.session.commit()
        
        return self.user
    
    def save_user_address(self, user: User):
        """Creates or returns a new address for the user."""
        
        if not self.user.address:
            Address(
                user_id=self.user.user_id,
                **self.address
            )

        return self.address
    
    def save_booking(self):
        """Creates the booking in the database."""
        
        # Check if booking object already exists
        if not self.booking:
            self.user = self.create_or_get_user()
            self.save_user_address(self.user)
            self.booking = Booking(
                **self.booking_info,
                user_id=self.user.id,
            )
            
            db.session.add(self.booking)
            db.session.commit()
    
        return self.booking

    def process_payment(self):
        """Handle optional payment processing."""
        if self.booking.price > 0:
            result = PaymentGateway.charge(self.user, self.booking)
            if self.booking.payment_status == "paid":
                # it's a recurring service payment
                # update the recurring booking table
                pass
            
            else:
                # it's a one-off service payment
                # update the booking status and payment status
                self.booking.status = "approved"
                self.booking.payment_status = "paid"
                db.session.add(self.booking)
                db.session.commit()
            return result
        
        return None

    def notify(self):
        """Send mail notifications."""
        
        NotificationService.send_to_customer(self.booking)
        NotificationService.send_to_admin(self.booking)

    def create_booking(self):
        """Run the entire booking flow."""
        #self.validate()
        self.save_booking()
        
        self.process_payment()
        
        self.notify()
        
        return self.booking
    
    def to_dict(self):
        """Convert booking to dictionary format."""
        if not self.booking:
            raise ValueError("Booking not found. Ensure you have run the booking process.")
        return {
            "id": self.booking.id,
            "user_id": self.booking.user_id,
            "service": self.booking.service,
            "service_category": self.booking.service_category,
            "bedrooms": self.booking.bedrooms,
            "bathrooms": self.booking.bathrooms,
            "frequency": self.booking.frequency,
            "add_ons": self.booking.add_ons,
            "booking_date": self.booking.booking_date.isoformat(),
            "price": self.booking.price,
            "status": self.booking.status,
            "payment_status": self.booking.payment_status,
            "user_info": self.user_info,
            "address": self.address
        }
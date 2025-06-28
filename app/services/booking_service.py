# Booking Service Module
# This module handles the booking process, including validation, saving to the database,
# payment processing, and notifications.
from flask import render_template
from app.models import Address, Booking, RecurringBooking, User, db
from app.services.payment_service import PaymentService
from app.services.notification_service import NotificationService


class BookingService:
    def __init__(self, cleaned_data:dict) -> None:
        self.booking_info = cleaned_data.model_dump()
        self.user_info = self.booking_info.pop("user_info", {})
        self.address = self.booking_info.pop("address", {})
        self.booking_info["recurring"] = True if self.booking_info.get("frequency") != "one-off" else False
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
    
    def save_user_address(self):
        """Creates or returns a new address for the user."""
        
        if not self.user.address:
            self.address = Address(
                user_id=self.user.id,
                **self.address
            )
            
            db.session.add(self.address)
            db.session.commit()

        return self.address
    
    def save_booking(self):
        """Creates the booking record in the database."""
        
        # Check if booking object already exists
        if not self.booking:
            print("Creating new booking record...")
            self.user = self.create_or_get_user()
            self.save_user_address()
            self.booking = Booking(
                **self.booking_info,
                user_id=self.user.id,
                # user_id=2,  # For testing purposes, replace with self.user.id
            )
            
            db.session.add(self.booking)
            db.session.commit()
            
        print("Booking record saved successfully.")
        return self.booking

    def process_payment(self):
        """Handle optional payment processing."""

        if not self.booking.price > 0:
            raise ValueError("Booking price must be greater than zero for payment processing.")
            # 
            # result = payment.charge_user(payment_gateway=None)  # Replace None with actual payment gateway
            
        elif self.booking.frequency != "one-off":
            # it's a recurring service payment
            # update the recurring booking table
            pass
            
        else:
            # it's a one-off service payment
            payment = PaymentService(self.booking)
            response = payment.charge_user(self.user)
            if not response:
                raise Exception("Payment processing failed.")
            
            # Update booking status and payment status
            self.booking.status = "approved"
            self.booking.payment_status = "paid"
            db.session.add(self.booking)
            db.session.commit()
        
        return response

    def notify(self):
        """Send mail notifications."""
        
        from app.constants import APP_NAME, APP_SUPPORT_EMAIL
        
        email_message =  render_template(
            "email/payment-confirmation.html",
            client_name=f"{self.user.full_name()}",
            client_email= "wofer57222@iridales.com", #self.user.email,
            amount=self.booking.price,
            service_type=self.booking.service,
            payment_date=self.booking.booking_date,
            app_name= APP_NAME,
            app_support_email=APP_SUPPORT_EMAIL,
            partner_name="Kleen & Spotless",
            partner_support_email="contact@kleenspotless.com",
            footer_comp_name="Divgm Technologies",
        )
        print("email_message ready for sending")
        
        mail_service = NotificationService(
            user=self.user,
            subject=f"Booking Confirmation - {APP_NAME}",
            message=email_message
        )
        mail_service.send_to_customer()
        # NotificationService.send_to_customer(self.booking)
        # NotificationService.send_to_admin(self.booking)
        return True
    
    def place_booking(self):
        """Run the entire booking flow."""
        #self.validate()
        self.save_booking()
        
        # self.process_payment()
        
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